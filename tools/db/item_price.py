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
    default_db = get_default_table()
    def create_from(filepath):
        with open(filepath, "r") as file:
            for line in file:
                if match := re.match(r"#export\s*.DBKey:(\S*):(\S*)\s*(\S*)", line):
                    obj = match.group(1)
                    attr = match.group(2)
                    key = match.group(3)

                    if attr.startswith("ShopPrice"):
                        byte_id = int(key[0:2], 16)
                        area_id = int(key[2:4], 16)
                        map_id =  int(key[4:6], 16)
                        index =  int(key[6:8], 16)
                        
                        map_area, created = MapArea.get_or_create(name=obj, defaults={
                            "area_id": area_id,
                            "map_id": map_id,
                        })

                        data = default_db.get(obj, {}).get(attr, {})
                        
                        item_price, created = ItemPrice.get_or_create(
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
    