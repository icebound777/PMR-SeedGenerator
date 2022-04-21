import json
from pathlib import Path

from peewee import *

from db.db import db
from db.map_area import MapArea
from db.item import Item

from metadata.item_source_types import item_source_types

# A table that represents all areas of interactivity
class Node(Model):

    # MapArea this node is found in
    map_area = ForeignKeyField(MapArea, backref = "nodes", lazy_load=False)

    # Entrance data of the Map if this note represents an entrance
    entrance_id = IntegerField(null = True)
    entrance_type = CharField(null = True) # like walk, pipe, door etc.
    entrance_name = CharField(null = True) # verbose name of entrance

    # Human readable name of item location (eg ItemA) or item price (eg ShopPriceA)
    key_name_item = CharField(null = True)
    key_name_price = CharField(null = True)
    item_source_type = IntegerField(null = True)

    # reference to item placed here in the unmodified game
    vanilla_item = ForeignKeyField(Item, null = True, lazy_load=False)

    # reference to item placed here during randomization
    current_item = ForeignKeyField(Item, null = True, lazy_load=False)

    # vanilla item price if shop
    vanilla_price = IntegerField(null = True)

    # index bytes of the DBKey
    item_index = IntegerField(null = True)
    price_index = IntegerField(null = True)

    identifier = TextField(null = True)

    def __str__(self):
        """Return string representation of current node"""
        entrance = ("[" + format(self.entrance_id) + "] ") if self.entrance_id else ''
        itemkey = ("[" + format(self.key_name_item) + "] ") if self.key_name_item else ''
        item = format(self.current_item.item_name) if self.current_item else ''
        price = (" (" + format(self.current_item.base_price) + ")") if self.current_item and self.key_name_price else ''

        return f"[{self.map_area.name}]{entrance}{itemkey}{item}{price}"

    def get_item_key(self):
        """Return convention key for item location"""
        if self.current_item is None:
            return None
        return (self._meta.key_type << 24) | (self.map_area.area_id << 16) | (self.map_area.map_id << 8) | self.item_index

    def get_price_key(self):
        """Return convention key for item location"""
        if self.current_item is None:
            return None
        return (self._meta.key_type << 24) | (self.map_area.area_id << 16) | (self.map_area.map_id << 8) | self.price_index

    def is_shop(self):
        """Return whether this location is a shop or not."""
        return self.key_name_price is not None

    class Meta:
        database = db
        key_type = 0xA1


def create_nodes():
    """Rebuild Node table and add nodes"""
    db.drop_tables([Node])
    db.create_tables([Node])
    db.drop_tables([MapArea])
    db.create_tables([MapArea])

    with open("./debug/keys.json", "r") as file:
        keys_dict = json.load(file)
        item_keys = keys_dict["items"]
        price_keys = keys_dict["item_prices"]
        entrance_keys = keys_dict["entrances"]

    with open("./debug/values.json", "r") as file:
        values_dict = json.load(file)
        item_values = values_dict["items"]
        price_values = values_dict["item_prices"]

    entrance_links = {}
    for child in Path("./maps/links").iterdir():
        if child.is_file() and child.name.endswith(".json"):
            with open(child, "r") as file:
                entrance_links |= json.load(file)

    # Create item only nodes
    for _, data in item_keys.items():
        map_area, created = MapArea.get_or_create(
            area_id = data["area_id"],
            map_id = data["map_id"],
            name = data["map_name"],
            verbose_name = MapArea.get_verbose_name(data["map_name"])
        )

        vanilla_item = Item.get(
            Item.value == item_values[data["map_name"]][data["name"]]
        )

        price_index = None
        key_name_price = None
        vanilla_price = None
        if data["name"].startswith("ShopItem") or data["name"].startswith("ShopBadge"):
            # Search for corresponding item_price and set index & key_name_price
            for price_id, price_data in price_keys.items():
                # Look for corresponding "ShopPriceX" for "ShopItemX" on same map
                if price_data["map_name"] == data["map_name"] and price_data["name"][-1] == data["name"][-1]:
                    price_index = price_data["value_id"]
                    key_name_price = price_data["name"]
                    vanilla_price = price_values[price_data["map_name"]][price_data["name"]]

        print(f"map_name={data['map_name']}, name={data['name']}")
        try:
            item_source_type = item_source_types.get(data["map_name"]).get(data["name"])
            if item_source_type is None:
                raise AttributeError
        except AttributeError as err:
            print(f"{err.args}: No item source type for {data['map_name']}/{data['name']}!")
            raise

        node, created = Node.get_or_create(
            map_area = map_area,
            key_name_item = data["name"],
            key_name_price = key_name_price if key_name_price else None,
            item_source_type = item_source_type,
            vanilla_item = vanilla_item,
            current_item = None,
            vanilla_price = vanilla_price,
            item_index = data["value_id"],
            price_index = price_index if price_index else None
        )
        print(node, created)

    # Create entrance only nodes
    for map_id, link_data in entrance_links.items():
        maparea_data_found = False

        for entrance_id, entrance_data in entrance_keys.items():

            if entrance_data["name"] == map_id:
                map_area, created = MapArea.get_or_create(
                    area_id = entrance_data["area_id"],
                    map_id = entrance_data["map_id"],
                    name = entrance_data["name"],
                    verbose_name = MapArea.get_verbose_name(entrance_data["name"])
                )
                maparea_data_found = True
                break

        if maparea_data_found:
            for entrance_id, entrance_data in link_data.items():
                node, created = Node.get_or_create(
                    map_area = map_area,
                    entrance_id = entrance_id,
                    entrance_type = entrance_data["type"],
                    entrance_name = entrance_data["verbose_name"]
                )
                print(node, created)
