import json
import xml.dom.minidom

from peewee import *
from playhouse.sqlite_ext import JSONField

from db.db import db
from metadata.progression_items import progression_items
from metadata.item_exclusion import taycet_items
from enums import Enums
from parse import get_default_table
from utility import get_files


class Item(Model):
    # keyitem, badge etc
    item_type = CharField(null=True)
    # item byte value as int (eg 348 = 0x15c (StarPiece))
    value = IntegerField()
    # actual item name w/o spaces or apostrophe
    item_name = CharField()
    # base sell price of the item
    base_price = IntegerField()
    # True if item can be required to reach locations
    progression = BooleanField(default=False)

    def __str__(self):
        return f"{self.item_name} ({self.item_type})[{hex(self.value)}]"
    
    @classmethod
    def get_type(cls, item_id:int):
        if item_id <= 0x7F or (0x16D <= item_id <= 0x17E ):
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
        elif 0x17F <= item_id <= 0x1C5:
            return "STARPIECE"
        elif 0x1C6 <= item_id <= 0x1CE:
            return "PARTNER"
        else:
            return "OTHER"

    class Meta:
        database = db
            
            
# Run this to create all items in Item table
def create_items():
    db.drop_tables([Item])
    db.create_tables([Item])

    with open("./debug/keys.json", "r") as file:
        item_keys = json.load(file)["items"]

    with open("./debug/values.json", "r") as file:
        item_values = json.load(file)["items"]

    items_doc = xml.dom.minidom.parse("../../globals/Items.xml")
    # need index (itemid), sell value
    item_data = []
    for item in items_doc.getElementsByTagName("Item"):
        item_index = item.getAttribute("index")
        item_sell_value = item.getAttribute("sellValue")
        if item_sell_value is None or item_sell_value == "":
            item_sell_value = "50"
        item_data.append(
            {
                "Index": item_index,
                "Sell Value": item_sell_value
            }
        )

    # abuse dict as list of unique entries
    unique_itemvalues = {}

    for _,data in item_keys.items():

        unique_itemvalues[item_values[data["map_name"]][data["name"]]] = ""

    # Tayce T. items are never placed in the game anywhere, so the parsed data
    # does not include them. Add them manually here
    for item_value in taycet_items:
        unique_itemvalues[item_value] = ""

    for value in unique_itemvalues.keys():
        try:
            for item in item_data:
                if int(item["Index"], 16) == value:
                    item,created = Item.get_or_create(
                        item_type = Item.get_type(value),
                        value = value,
                        item_name = Enums.get("Item")[value],
                        base_price = int(item["Sell Value"], 10) if item["Sell Value"] != "FFFF" else 50,
                        progression = (Item.get_type(value) in ["KEYITEM","PARTNER"] and value in progression_items.keys())
                    )
                    break
        except ValueError as err:
            print(f"{err.args}: {value}")
            raise
