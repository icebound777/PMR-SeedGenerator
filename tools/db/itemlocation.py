import json

from peewee import *

from db.db import db
from db.map_area import MapArea
from db.item import Item
from db.item_price import ItemPrice

class ItemLocation(Model):
    area_id = IntegerField(default=0)
    map_id = IntegerField(default=0)
    index = IntegerField(default=0)

    # FK
    map_area = ForeignKeyField(MapArea, null=True, backref="itemlocations")
    # human readable name of item location (eg ItemA)
    key_name = CharField()
    # reference to item placed here in the unmodified game
    vanilla_item = ForeignKeyField(Item, backref="itemlocation")
    # reference to item placed here during randomization
    current_item = ForeignKeyField(Item, null=True, backref="itemlocation")
    # reference to price of item places at this location
    item_price = ForeignKeyField(ItemPrice, null=True, backref="itemlocation")


    def __str__(self):
        """Return string representation of current location including former and current item"""
        if self.map_area:
            return f"[{self.map_area.name}]: {self.key_name} ({self.vanilla_item} -> {self.current_item})"
        return f"{self.vanilla_item}"


    def get_key(self):
        """Return convention key for location"""
        return (self._meta.key_type << 24) | (self.map_area.area_id << 16) | (self.map_area.map_id << 8) | self.index
        
    #def get_type():

    class Meta:
        database = db
        key_type = 0xA1


def create_item_locations():
    """Rebuild ItemLocation table and add all item locations"""
    db.drop_tables([ItemLocation])
    db.create_tables([ItemLocation])

    with open("./debug/keys.json", "r") as file:
        item_keys = json.load(file)["items"]

    with open("./debug/values.json", "r") as file:
        item_values = json.load(file)["items"]

    for key, data in item_keys.items():
        map_area, created = MapArea.get_or_create(
            area_id = data["area_id"],
            map_id = data["map_id"],
            name = data["map_name"],
            verbose_name = MapArea.get_verbose_name(data["map_name"])
        )

        vanilla_item, created = Item.get_or_create(
            value = item_values[data["map_name"]][data["name"]]
        )

        #value = item_values[data["map_name"]][data["name"]]

        itemlocation, created = ItemLocation.get_or_create(
            area_id = data["area_id"],
            map_id = data["map_id"],
            index = data["value_id"],
            map_area = map_area,
            key_name = data["name"],
            vanilla_item = vanilla_item,
            current_item = vanilla_item
            #item_price = null
        )
        print(itemlocation, created)