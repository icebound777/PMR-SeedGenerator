import re

from peewee import *

from db.db import db
from db.map_area import MapArea
from enums import Enums
from parse import get_default_table


class ItemPrice(Model):
    area_id = IntegerField()
    map_id = IntegerField()
    index = IntegerField()

    map_area = ForeignKeyField(MapArea, null=True, backref="item_prices")
    key_name = CharField()
    value = IntegerField()

    def __str__(self):
        return f"{self.key_name} ({self.value:02X})"

    def get_key(self):
        return (ItemPrice._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index

    class Meta:
        database = db
        key_type = 0xA1


# Run this to create all items in Item table
def create_item_prices():
    db.drop_tables([ItemPrice])
    db.create_tables([ItemPrice])

    with open("./debug/keys.json", "r") as file:
        item_prices = json.load(file)["item_prices"]


    for key,data in item_prices.items():
        map_area,created = MapArea.get_or_create(name=data["name"], defaults={
            "area_id": data["area_id"],
            "map_id": data["map_id"],
            "verbose_name": MapArea.get_verbose_name(data["name"]),
        })

        item_price,created = ItemPrice.get_or_create(
            map_area=map_area,
            area_id=area_id,
            map_id=map_id,
            index=index,
            value=data["value"],
            key_name=attr,
        )








    for key,data in entrances.items():
        # Create MapArea if neccessary
        map_area,created = MapArea.get_or_create(
            area_id=data["area_id"],
            map_id=data["map_id"],
            name=data["name"],
            verbose_name=MapArea.get_verbose_name(data["name"]),
        )
        # Create Entrance
        entrance,created = Entrance.get_or_create(
            map_name=data["name"],
            area_id=data["area_id"],
            map_id=data["map_id"],
            index=data["entrance"],
            map_area=map_area,
        )



    map_area,created = MapArea.get_or_create(name=obj, defaults={
        "area_id": area_id,
        "map_id": map_id,
        "verbose_name": MapArea.get_verbose_name(obj),
    })

    data = default_db.get(obj, {}).get(attr, {})
    
    item_price,created = ItemPrice.get_or_create(
        map_area=map_area,
        area_id=area_id,
        map_id=map_id,
        index=index,
        value=data["value"],
        key_name=attr,
    )
    print(item_price, created)

    # Update item with reference to this ItemPrice
    from db.item import Item
    item = Item.get(Item.map_area==item_price.map_area, Item.key_name == f"ShopItem{item_price.key_name[-1]}")
    item.item_price = item_price
    item.save()

    create_from("../globals/patch/DatabaseKeys.patch")
    create_from("../globals/patch/generated/keys.patch")
    