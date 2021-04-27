import json

from peewee import *
from playhouse.sqlite_ext import JSONField

from db.db import db
from db.map_area import MapArea
from db.item_price import ItemPrice
from enums import Enums
from parse import get_default_table


class Item(Model):
    area_id = IntegerField(default=0)
    map_id = IntegerField(default=0)
    index = IntegerField(default=0)

    map_area = ForeignKeyField(MapArea, null=True, backref="items")
    item_price = ForeignKeyField(ItemPrice, null=True, backref="item")
    key_name = CharField()
    item_type = CharField(null=True)
    original_item_type = CharField(null=True)
    value = IntegerField()
    item_name = CharField()
    original_item_name = CharField()

    logic = JSONField(default=dict())
    placed = BooleanField(default=False)

    def __str__(self):
        if self.map_area:
            return f"[{self.map_area.name}]: {self.key_name} ({self.original_item_name})"
        return f"{self.original_item_name}"

    def get_key(self):
        return (Item._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index

    def swap(self, other):
        self.original_item_name = self.item_name
        other.original_item_name = other.item_name

        self.original_item_type = self.item_type
        other.original_item_type = other.item_type

        self.value, other.value = other.value, self.value
        self.item_type, other.item_type = other.item_type, self.item_type
        self.item_name, other.item_name = other.item_name, self.item_name

        self.save()
        other.save()

    @classmethod
    def get_type(cls, item_id:int):
        if item_id <= 0x7F:
            return "KEYITEM"
        elif 0x7F < item_id <= 0xDF:
            return "ITEM"
        elif 0xDF < item_id <= 0x155:
            return "BADGE"
        elif 0x155 < item_id <= 0x15C:
            return {
                0x156: "HEART",
                0x157: "COIN",
                0x159: "STARPOINT",
                0x15A: "FULLHEAL",
                0x15B: "FLOWER",
                0x15C: "STARPIECE",
            }.get(item_id)
        else:
            return "OTHER"

    class Meta:
        database = db
        key_type = 0xA1


""" A table representing a graph of progression between all items. For example, starting at the Koopa Bro's Fortress:
FortressKey - First room
    FortressKey - Basement room with firebars
        Bombette - With the second key, bombette becomes accessible
    (Bombette) - If you have bombette, more becomes accessible
        Refund - This does not lead to anything else
        PowerBounce - Neither does this
        FortressKey - Behind the bars (right side)
            (Kooper) - If you have Kooper, you can cross the upper area
                (Bombette) - If you have Bombette, you can blow up the wall
                    FortressKey - Behind the bars (left side)
                        SmashCharge - This does not lead to anything else
                        (Bombette) - If you have Bombette, you can break the rock
                            MapleSyrup - Leads nowhere
                        END - There's nothing else to do but beat the chapter

For the above diagram, the following table entries would exist:
    FortressKey -> FortressKey
    FortressKey -> Bombette
    Bombette -> Refund
    Bombette -> PowerBounce
    Bombette -> FortressKey
    FortressKey -> _Kooper (underscore means don't receive, just required to progress)
    Kooper -> _Bombette
    Bombette -> FortressKey
    FortressKey -> SmashCharge
    FortressKey -> _Bombette
    Bombette -> MapleSyrup

To traverse the graph, get a list of all ItemRelation for FortressKey (or rather, the specific FortressKey using its DBKey value):
    1) For each relation, determine if Mario has the neccessary item or partner.
    2) If so, append it to a list of valid nodes.
    3) Modify a copy of Mario's state as necessary to simulate traversing through the game (preserving the original at the root node)
    4) For each valid node, repeat steps 1-3, growing the valid node list.
    5) We now have a list of valid places Mario can reach given a certain inventory and partners.
"""
class ItemRelation(Model):
    chapter = IntegerField()
    src = ForeignKeyField(Item, null=True) # The item that unlocks the destination item
    dest = ForeignKeyField(Item) # The item unlocked by the source item
    level = IntegerField(default=0)
    comment = CharField(default="")

    def __str__(self):
        return f"{self.src} -> {self.dest}"

    # Returns whether or not a Mario state can reach the destination item
    # E.g. If The source item is FortressKey, that item must be present in mario["items"]
    # E.g. If the source "item" is Bombette, that partner must be present in mario["partners"]
    def valid(self, mario:dict) -> (bool, str):
        if self.src.original_item_name == "Nothing":
            return True
        elif self.src.original_item_name == "Panel":
            if mario["hammer"] >= 2 or mario["boots"] >= 1:
                return True
        elif self.src.original_item_name in mario["items"]:
            return True
        elif self.src.original_item_name in mario["partners"]:
            return True
        return False

    @classmethod
    def get_relations(cls, item):
        # Yield a list of expanded item relation data for a particular item
        query = """
            SELECT itemrelation.id, src_id, dest_id, s.area_id, s.map_id, s.`index`, s.item_name AS source_item, d.area_id, d.map_id, d.`index`, d.item_name as dest_item
            FROM itemrelation
            INNER JOIN item AS s ON src_id = s.id
            LEFT JOIN item AS d ON dest_id = d.id
            WHERE s.area_id=7 AND s.map_id=3 AND s.`index`=1
        """
        for row in ItemRelation._meta.database.execute_sql(query).fetchall():
            dest = Item.get(Item.id == row[2])
            yield {
                "relation": ItemRelation.get(ItemRelation.id == row[0]),
                "src": item,
                "src_name": item.item_name,
                "dest": dest,
                "dest_name": dest.item_name,
            }

    class Meta:
        database = db
        

# Run this to create all item relationships in ItemRelation table
# Reads from an external data source
def create_item_relationships():
    db.drop_tables([ItemRelation])
    db.create_tables([ItemRelation])

    """ TODO: Add to item_relations.csv
    This way, we can look up the source and destination items using the keys
    A source item can have multiple item relationships but each one should have a unique destination
    """

    partners = ["Goombario", "Kooper", "Bombette", "Parakarry", "Bow", "Watt", "Sushi", "Lakilester"]
    require = {partner: 0 for partner in partners}
    with open("./progression/ch1.csv", "r") as file:
        for i,line in enumerate(file.readlines()):
            if i == 0:
                continue
            src_map,src_index,dest_map,dest_index,level,comment = line.split(",")

            src_item = None

            if src_map in partners:
                src_item = Item.get(Item.item_type == "PARTNER", Item.item_name == src_map)
            elif src_map == "Panel":
                src_item = Item.get(Item.item_type == "PANEL", Item.item_name == src_map)
            elif src_map == "Nothing":
                src_item = Item.get(Item.item_type == "NOTHING", Item.item_name == src_map)
            elif src_map != "":
                src_map = MapArea.get(MapArea.name == src_map)
                src_item = Item.get(Item.map_area == src_map, Item.index == src_index)
            
            if dest_map.startswith("_"):
                dest_item,created = Item.get_or_create(
                    key_name=dest_map[1:],
                    item_type="PARTNER_REQUIRED",
                    original_item_type="PARTNER_REQUIRED",
                    item_name=dest_map[1:],
                    original_item_name=dest_map[1:],
                    index=require[dest_map[1:]],
                    value=0,
                )
                require[dest_map[1:]] += 1
            else:
                if dest_map in partners:
                    dest_item = Item.get(Item.item_type == "PARTNER", Item.item_name == dest_map)
                else:
                    dest_map = MapArea.get(MapArea.name == dest_map)
                    dest_item = Item.get(Item.map_area == dest_map, Item.index == dest_index)

            relation,created = ItemRelation.get_or_create(
                chapter=1, # TODO: Variable
                src=src_item,
                dest=dest_item,
                level=int(level),
                comment=comment.strip(),
            )

            print(relation, created)
            
            
# Run this to create all items in Item table
def create_items():
    db.drop_tables([Item])
    db.create_tables([Item])

    with open("./debug/keys.json", "r") as file:
        item_keys = json.load(file)["items"]

    with open("./debug/values.json", "r") as file:
        item_values = json.load(file)["items"]

    # Create "items" for partners
    for partner in ["Goombario", "Kooper", "Bombette", "Parakarry", "Bow", "Watt", "Sushi", "Lakilester"]:
        item,created = Item.get_or_create(
            area_id=0,
            map_id=0,
            index=0,
            item_type="PARTNER",
            original_item_type="PARTNER",
            value=0,
            item_name=partner,
            original_item_name=partner,
            key_name=partner,
            logic={},
        )

    # Create "item" to represent ability to find hidden panels
    item,created = Item.get_or_create(
        area_id=0,
        map_id=0,
        index=0,
        item_type="PANEL",
        original_item_type="PANEL",
        value=0,
        item_name="Panel",
        original_item_name="Panel",
        key_name="Panel",
        logic={},
    )

    # Create "item" that signifies having nothing
    item,created = Item.get_or_create(
        area_id=0,
        map_id=0,
        index=0,
        item_type="NOTHING",
        original_item_type="NOTHING",
        value=0,
        item_name="Nothing",
        original_item_name="Nothing",
        key_name="Nothing",
        logic={},
    )

    for key,data in item_keys.items():
        map_area,created = MapArea.get_or_create(
            area_id=data["area_id"],
            map_id=data["map_id"],
            name=data["map_name"],
            verbose_name=MapArea.get_verbose_name(data["map_name"]),
        )

        value = item_values[data["map_name"]][data["name"]]

        item,created = Item.get_or_create(
            map_area=map_area,
            area_id=data["area_id"],
            map_id=data["map_id"],
            index=data["value_id"],
            item_type=Item.get_type(value),
            original_item_type=Item.get_type(value),
            value=value,
            item_name=Enums.get("Item")[value],
            original_item_name=Enums.get("Item")[value],
            key_name=data["name"],
            logic={},
        )
        print(item, created)










    