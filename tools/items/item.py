from table import Table
from maps.map import Map

from enums import Enums

        
class Item:
    items = {}

    def __init__(self, data):
        self.name = data["attribute"]
        self.key = data["key"]
        self.value = data["value"]
        self.map = Map.maps[data["table"]]
        Item.items[self.key] = self

    def __str__(self):
        return f"[{self.map}] {self.name} - {Enums.get('Item')[self.value]} ({Item.get_type(self.value)})"

    # Update the ROM Table with the current data
    def update(self):
        Table.instance[self.map.name][self.name] = {
            "key": self.key,
            "value": self.value,
            "attribute": self.name,
            "table": self.map.name,
            "enum_type": "Item",
        }

    def swap(self, other):
        self.name, other.name = other.name, self.name
        #self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value
        self.map, other.map = other.map, self.map
        
        self.update()
        other.update()

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