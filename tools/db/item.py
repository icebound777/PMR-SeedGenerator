import json

from peewee import *
from playhouse.sqlite_ext import JSONField

from db.db import db
from db.map_area import MapArea
from db.item_price import ItemPrice
from enums import Enums
from parse import get_default_table


class Item(Model):
    area_id = IntegerField()
    map_id = IntegerField()
    index = IntegerField()

    map_area = ForeignKeyField(MapArea, null=True, backref="items")
    item_price = ForeignKeyField(ItemPrice, null=True, backref="item")
    key_name = CharField()
    item_type = CharField(null=True)
    value = IntegerField()
    item_name = CharField()

    logic = JSONField()
    placed = BooleanField(default=False)

    def __str__(self):
        return f"[{self.map_area.name}]: {self.key_name} ({self.item_name})"

    def get_key(self):
        return (Item._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index

    def swap(self, other):
        # self.key_name, other.key_name = other.key_name, self.key_name
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
    FortressKey -> _Kooper (_ means you don't receive him, he's just necessary to progress)
    Kooper -> _Bombette
    Bombette -> FortressKey
    FortressKey -> SmashCharge
    FortressKey -> _Bombette
    Bombette -> MapleSyrup

To traverse the graph, get a list of all ItemRelation for FortressKey:
    1) For each relation, determine if Mario has the neccessary item or partner.
    2) If so, append it to a list of valid nodes.
    3) Modify Mario's state as necessary to simulate traversing through the game.
    4) For each valid node, repeat steps 1-3, growing the valid node list.
    5) We now have a list of valid places Mario can reach given a certain inventory and partners.
"""
class ItemRelation(Model):
    src = ForeignKeyField(Item) # The item that unlocks the destionation item
    dest = ForeignKeyField(Item) # The item unlocked by the source item

    def __str__(self):
        return f"{self.src} -> {self.dest}"

    # Returns whether or not a Mario state can reach the destination item
    # E.g. If The source item is FortressKey, that item must be present in mario["items"]
    # E.g. If the source "item" is Bombette, that partner must be present in mario["partners"]
    def can_pass(self, mario:dict) -> (bool, str):
        if self.src.item_name in mario["items"]:
            return True
        elif self.src.item_name in mario["partners"]:
            return True
        return False

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

    with open("item_relations.csv", "r") as file:
        for i,line in enumerate(file.readlines()):
            if i == 0:
                continue
            src_map,src_index,dest_map,dest_index = line.split(",")

            if src_map.startswith("_") or dest_map.startswith("_"):
                continue
            if src_map.startswith("+") or dest_map.startswith("+"):
                continue

            src_map = MapArea.get(MapArea.name == src_map)
            dest_map = MapArea.get(MapArea.name == dest_map)

            src_item = Item.get(Item.map_area == src_map, Item.index == src_index)
            dest_item = Item.get(Item.map_area == dest_map, Item.index == dest_index)

            relation,created = ItemRelation.get_or_create(
                src=src_item,
                dest=dest_item,
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
            value=value,
            item_name=Enums.get("Item")[value],
            key_name=data["name"],
            logic={},
        )
        print(item, created)










    