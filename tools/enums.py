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
            item = random.choice([key for key in self.data if Item.get_type(self.data[key]) == item_type])
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