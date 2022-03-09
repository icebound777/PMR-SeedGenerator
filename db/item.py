import xml.dom.minidom

from peewee import *

from db.db import db
from metadata.progression_items import progression_items
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

    def __str__(self):
        return f"{self.item_name} ({self.item_type})[{hex(self.value)}]"
    
    @classmethod
    def get_type(cls, item_id:int):
        if item_id <= 0x7F or (0x16D <= item_id <= 0x17E):
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
        elif 0x185 <= item_id <= 0x1CB:
            return "STARPIECE"
        elif 0x1CC <= item_id <= 0x1D4:
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

    for item in item_data:
        item_id = int(item["Index"], 16)
        if item_id == 0x18:
            # Ignore fake Volcano Vase
            continue
        item,_ = Item.get_or_create(
            item_type = Item.get_type(item_id),
            value = item_id,
            item_name = Enums.get("Item")[item_id],
            base_price = int(item["Sell Value"], 10) if item["Sell Value"] != "FFFF" else 50,
            progression = (Item.get_type(item_id) in ["KEYITEM","PARTNER"] and item_id in progression_items.keys())
        )
