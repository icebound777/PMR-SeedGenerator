import re
import random


class Enums:
    all = {}

    def __init__(self, filepath):
        self.data = {}
        with open(filepath, "r") as file:
            self.namespace, self.library, self.reversed = [next(file).split("%")[0].strip() for i in range(3)]
            self.reversed = True if self.reversed == "true" else False
            
            for line in file:
                if match := re.match(r"(\S*)\s*=\s*(\S*)", line):
                    if self.reversed:
                        key = match.group(1)
                        value = match.group(2)
                    else:
                        key = match.group(2)
                        value = match.group(1)
                    value = int(value, 16)
                    self.data[key] = value
        Enums.all[self.namespace] = self
        
    @classmethod
    def get(cls, key):
        return Enums.all[key]

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.data[key]
        elif isinstance(key, int):
            for k,v in self.data.items():
                if key == v:
                    return k

    def get_random(self, item_type=None):
        if item_type is None:
            item = random.choice([key for key in self.data])
        else:
            item = random.choice([key for key in self.data if get_item_type(self.data[key]) == item_type])
        return self.__getitem__(item)

def enum_int(enum:str) -> (int, str):
    enum_type,enum_value = enum[1:].split(":")
    filename = {
        "Item": "../globals/enum/items.enum",
    }.get(enum_type)

    if not filename:
        raise Exception(f"Enum type {enum_type} isn't defined!")

    with open(filename, "r") as file:
        for line in file:
            if line.startswith(enum_value):
                value = line.strip().replace(" ", "").split("=")[-1]
                value = int(value, 16)
                return (value,enum_type)

def get_item_type(item_id:int) -> str:
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