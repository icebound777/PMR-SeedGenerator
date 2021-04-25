import re
import os
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

def create_enums():
    for name in os.listdir("../globals/enum/"):
        name = name.split(".")[0]
        Enums(f"../globals/enum/{name}.enum")

def enum_int(enum:str) -> (int, str):
    enum_type,enum_value = enum[1:].split(":")
    filename = {
        "Item": "../globals/enum/items.enum",
    }.get(enum_type)

    if not filename:
        raise Exception(f"Enum type {enum_type} isn't defined!")

    with open(filename, "r") as file:
        longest = ""
        for line in file:
            try:
                name,value = line.strip().replace(" ", "").split("=")
                if "%" in value:
                    value = value.split("%")[0]
                value = int(value, 16)
                if name == enum_value:
                    return (value,enum_type)
            except:
                pass