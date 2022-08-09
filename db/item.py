import xml.dom.minidom

from peewee import *

from db.db import db
from metadata.progression_items import progression_items
from metadata.item_general import unused_items, unplaceable_items
from enums import Enums


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
    # Is the item unused in the vanilla game, but functional
    unused = BooleanField(default=False)
    # Is the item unintended to be placed in the world and could break things,
    # or is unused but non-functional
    unplaceable = BooleanField(default=False)

    def __str__(self):
        return f"{self.item_name} ({self.item_type})[{hex(self.value)}]"

    def is_trapped(self):
        trap_flag = 0x2000
        return self.value & trap_flag == trap_flag

    @classmethod
    def get_type(cls, item_id:int):
        if 0x00 == item_id:
            return "NOTHING"
        if 0x01 <= item_id <= 0x06:
            return "GEAR"
        if 0x07 <= item_id <= 0x7F or (0x16D <= item_id <= 0x17E):
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
        elif 0x185 <= item_id <= 0x1D8:
            return "STARPIECE"
        elif 0x1E1 <= item_id <= 0x1E9:
            return "PARTNER"
        else:
            return "OTHER"

    class Meta:
        database = db


# Run this to create all items in Item table
def create_items():
    db.drop_tables([Item])
    db.create_tables([Item])

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

    # Base mod doesn't treat the hammers and boots as unique items, but we 
    # have to in the generator, so yay ugly workarounds
    boots_found = 0
    hammers_found = 0
    gear_rename = {
        0x1: {
            0: "BootsA",
            1: "BootsB",
            2: "BootsC",
        },
        0x4: {
            0: "HammerA",
            1: "HammerB",
            2: "HammerC",
        }
    }

    for item in item_data:
        item_id = int(item["Index"], 16)
        if item_id == 0x18:
            # Ignore fake Volcano Vase
            continue
        if 0x1 <= item_id <= 0x3:
            item_name = gear_rename[0x1][boots_found]
            boots_found = boots_found + 1
            item_id = 0x1
        elif 0x4 <= item_id <= 0x6:
            item_name = gear_rename[0x4][hammers_found]
            hammers_found = hammers_found + 1
            item_id = 0x4
        else:
            item_name = Enums.get("Item")[item_id]
        item,_ = Item.get_or_create(
            item_type = Item.get_type(item_id),
            value = item_id,
            item_name = item_name,
            base_price = int(item["Sell Value"], 10) if item["Sell Value"] != "FFFF" else 50,
            progression = (Item.get_type(item_id) in ["KEYITEM","PARTNER"] and item_id in progression_items.keys()),
            unused = item_name in unused_items,
            unplaceable = item_name in unplaceable_items
        )
