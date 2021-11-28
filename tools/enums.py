import re
import os
import xml.dom.minidom



class Enums:
    all = {}

    def __init__(self, filepath):
        self.data = {}
        if ("Items.xml" not in filepath):
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
        else:
            items_doc = xml.dom.minidom.parse(filepath)
            self.namespace = "Item"
            self.library = "itemID"
            self.reversed = True
            for item in items_doc.getElementsByTagName("Item"):
                key = item.getAttribute("name")
                value = int(item.getAttribute("index"), 16)
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
    Enums("../globals/Items.xml")

def enum_int(enum:str) -> (int, str):
    # enum = .Item:KootTheTape
    enum_type,enum_value = enum[1:].split(":") # enum_type,enum_value = Item, KootTheTape
    filename = {
        "Item": "../globals/Items.xml",
    }.get(enum_type)

    if not filename:
        raise Exception(f"Enum type {enum_type} isn't defined!")

    items_doc = xml.dom.minidom.parse(filename)
    for item in items_doc.getElementsByTagName("Item"):
        name = item.getAttribute("name")
        if (name == enum_value):
            value = int(item.getAttribute("index"), 16)
            return (value,enum_type)
