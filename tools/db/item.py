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
            return f"[{self.map_area.name}]: {self.key_name} ({self.original_item_name} -> {self.item_name})"
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

# A table that represents all areas of interactivity
class Node(Model):

    # One of the non-null values must be present to activate
    partner = CharField(null=True)
    item_required = CharField(null=True)
    hammer = IntegerField(null=True)
    boots = IntegerField(null=True)

    # Whether or not this node is required to progress further through the list
    required = BooleanField(default=False)

    # Whether the required object is removed
    remove = BooleanField(default=False)

    # Things that are received when this node is activated
    level = IntegerField()
    item_received = CharField(null=True)
    partner_received = CharField(null=True)

    # Misc
    comment = CharField()
    map_name = CharField()
    index = IntegerField(null=True)

    def __str__(self):
        requirements = []
        if self.partner:
            requirements.append(self.partner)
        if self.item_required:
            requirements.append(self.item_required)
        if self.hammer:
            requirements.append(f"Hammer({self.hammer})")
        if self.boots:
            requirements.append(f"Boots({self.boots})")
        requirements = " | ".join(requirements)

        receive = []
        if self.item_received:
            receive.append(self.item_received)
        if self.partner_received:
            receive.append(self.partner_received)
        if self.required:
            receive.append("Progress+")
        receive = ", ".join(receive)

        return f"[{self.map_name}][{self.index if self.index else ''}] Have [{requirements}] -> Receive [{receive}]"

    def can_activate(self, mario):
        if all([self.partner is None, self.item_required is None, self.hammer is None, self.boots is None]):
            return True

        # Check Partners
        if self.partner and self.partner in mario.partners:
            return True

        # Check Items
        if self.item_required and self.item_required in [item for item,db_key in mario.items]:
            return True

        # Check Hammer
        if self.hammer and mario.hammer >= self.hammer:
            return True

        # Check Boots
        if self.boots and mario.boots >= self.boots:
            return True

        return False

    class Meta:
        database = db


def create_nodes():
    db.drop_tables([Node])
    db.create_tables([Node])

    with open("./progression/ch1_objects.csv", "r") as file:
        for i,line in enumerate(file.readlines()):
            if i == 0:
                continue
            comment,partner,item_required,hammer,boots,item_received,partner_received,required,remove,level,map_name,index = line.strip().split(",")

            node,created = Node.get_or_create(
                partner=partner if partner else None,
                item_required=item_required if item_required else None,
                hammer=int(hammer) if hammer else None,
                boots=int(boots) if boots else None,
                required=True if required == "1" else False,
                remove=True if remove == "1" else False,
                level=int(level),
                item_received=item_received if item_received else None,
                partner_received=partner_received if partner_received else None,
                comment=comment,
                map_name=map_name,
                index=int(index) if index else None,
            )

            print(node, created)
            
            
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










    