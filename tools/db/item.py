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










    