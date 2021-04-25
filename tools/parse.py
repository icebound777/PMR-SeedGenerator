import re
import os
import json
import xml.etree.ElementTree as ET

from enums import Enums, enum_int, create_enums


def get_files(directory_name):
    files = list()
    for entry in os.listdir(directory_name):
        full_path = os.path.join(directory_name, entry)
        if os.path.isdir(full_path):
            files += get_files(full_path)
        else:
            files.append(full_path)

    return files

# Gather a list of ALL keys under the ../globals/patch/ directory
# AF = Options
# A1 = Items
# A2 = Actors
# A3 = Entrances
# A4 = Palettes
# A5 = 
# AF = Quizzes
def gather_keys():
    files = get_files("../globals/patch")
    keys = {
        "items": dict(),
        "item_prices": dict(),
        "actors": dict(),
        "entrances": dict(),
        "palettes": dict(),
        "options": dict(),
        "quizzes": dict(),
    }
    for filepath in files:
        with open(filepath, "r") as file:
            for line in file:
                if match := re.match(r"#export\s*.DBKey:", line):
                    data = line[match.end():]
                    match = re.match(r"(\S*)\s*(\S*)", data)
                    key_info,number = match.group(1), match.group(2)
                    
                    byte_id = int(number[0:2], 16)
                    area_id = int(number[2:4], 16)
                    map_id =  int(number[4:6], 16)
                    value_id =  int(number[6:8], 16)
                    key = (byte_id << 24) | (area_id << 16) | (map_id << 8) | value_id

                    if byte_id == 0xA1:
                        name = key_info.split(":")[-1]
                        if "ShopPrice" in name:
                            keys["item_prices"][key] = {
                                "name": name,
                                "map_name": key_info.split(":")[0],
                                "byte_id": byte_id,
                                "area_id": area_id,
                                "map_id": map_id,
                                "value_id": value_id,
                            }
                        else:
                            keys["items"][key] = {
                                "name": name,
                                "map_name": key_info.split(":")[0],
                                "byte_id": byte_id,
                                "area_id": area_id,
                                "map_id": map_id,
                                "value_id": value_id,
                            }
                    elif byte_id == 0xA2:
                        name,attribute = key_info.split(":")
                        if key not in keys["actors"]:
                            keys["actors"][key] = {}
                        keys["actors"][key][attribute] = {
                            "name": name,
                            "byte_id": byte_id,
                            "area_id": area_id,
                            "map_id": map_id,
                            "value_id": value_id,
                        }
                    elif byte_id == 0xA3:
                        _,map_name,entrance = key_info.split(":")
                        entrance = int(entrance, 16)
                        keys["entrances"][key] = {
                            "name": map_name,
                            "entrance": entrance,
                            "byte_id": byte_id,
                            "area_id": area_id,
                            "map_id": map_id,
                            "value_id": value_id,
                        }
                    elif byte_id == 0xAF:
                        name,attribute = key_info.split(":")
                        if name == "Options" or name == "Cosmetic":
                            keys["options"][key] = {
                                "name": attribute,
                                "byte_id": byte_id,
                                "area_id": area_id,
                                "map_id": map_id,
                                "value_id": value_id,
                            }
                        elif name == "Quiz":
                            keys["quizzes"][key] = {
                                "name": attribute,
                                "byte_id": byte_id,
                                "area_id": area_id,
                                "map_id": map_id,
                                "value_id": value_id,
                            }
    with open("./debug/keys.json", "w") as file:
        json.dump(keys, file, indent=4)

def gather_values():
    def get_value(value):
        # Booleans
        if value == ".True":
            return True
        elif value == ".False":
            return False

        # Numbers
        if value.endswith("`"):
            return int(value[:-1])
        try:
            value = int(value, 16)
        except:
            pass
        else:
            return value

        # Items
        if value.startswith(".Item"):
            item = value.split(":")[-1]
            value = Enums.get("Item")[item]
            return value

    create_enums()

    values = {
        "items": dict(),
        "item_prices": dict(),
        "actors": dict(),
        "entrances": dict(),
        "palettes": dict(),
        "options": dict(),
        "quizzes": dict(),
    }
    with open("../globals/patch/DatabaseDefaults.patch", "r") as file:
        for line in file:
            if match := re.match(r"\s*.DBKey:(\S*)\s*(\S*)", line):
                key_info = match.group(1)
                value = match.group(2)
                if "Options" in key_info or "Cosmetic" in key_info:
                    name = key_info.split(":")[-1]
                    values["options"][name] = get_value(value)
                elif "Quiz" in key_info:
                    name = key_info.split(":")[-1]
                    values["quizzes"][name] = get_value(value)
                elif match := re.match(r"([A-Z]{2,5}_\d+):(\S*)", key_info):  # Check for map name (which means it's an item or item price)
                    map_name = match.group(1)
                    key_name = match.group(2)
                    if "ShopPrice" in key_name:
                        if map_name not in values["item_prices"]:
                            values["item_prices"][map_name] = {}
                        values["item_prices"][map_name][key_name] = get_value(value)
                    else:
                        if map_name not in values["items"]:
                            values["items"][map_name] = {}
                        values["items"][map_name][key_name] = get_value(value)
                elif any(["HP" in key_info, "Damage" in key_info, "Level" in key_info, "Increment" in key_info]): # Check for actor data
                    actor,attribute = key_info.split(":")
                    value = get_value(value)
                    if actor not in values["actors"]:
                        values["actors"][actor] = {}
                    values["actors"][actor][attribute] = value

    with open("./debug/values.json", "w") as file:
        json.dump(values, file, indent=4)

def get_default_table():
    # Get general data
    db = {}
    with open("../globals/patch/DatabaseDefaults.patch", "r") as file:
        db_found = False
        while not db_found:
            if match := re.match(r"#export:Data\s*\$DefaultDatabase", next(file)):
                db_found = True
        for line in file:
            if line.startswith("}"):
                break
            if match := re.match(r"\s*.DBKey:(\S*):(\S*)\s*(\S*)", line):
                table = match.group(1)
                attribute = match.group(2)
                value = match.group(3)
                enum_type = None

                if value == ".True":
                    value = True
                elif value == ".False":
                    value = False
                elif value.endswith("`"): # Decimal
                    value = int(value[:-1])
                else:
                    try:
                        value = int(value, 16) # Hexadecimal
                    except:
                        value,enum_type = enum_int(value) # Convert enum to number

                if table not in db:
                    db[table] = {}
                db[table][attribute] = {
                    "value": value,
                    "enum_type": enum_type,
                    "attribute": attribute,
                    "table": table,
                }
                
    # Get entrance data
    db["Entrance"] = {}
    with open("../globals/patch/RandomEntrances.patch", "r") as file:
        for line in file:
            if match := re.match(r"#export\s*.DBKey:Entrance:(\S*):(\S*)\s*(\S*)", line):
                map_name = match.group(1)
                map_exit = int(match.group(2), 16)
                key = match.group(3)
                byte_id = int(key[0:2], 16)
                area_id = int(key[2:4], 16)
                map_id =  int(key[4:6], 16)
                entry_id =  int(key[6:8], 16)

                if map_name not in db["Entrance"]:
                    db["Entrance"][map_name] = {}
                db["Entrance"][map_name][map_exit] = {
                    "byte_id": byte_id,
                    "area": area_id,
                    "map": map_id,
                    "entry": entry_id,
                }
    return db
            
def get_table_info():
    # Defaults
    table_info = {
        "magic_value": 0x504D4442,
        "header_size": 0x20,
        "num_entries": 0,
        "seed": 0xDEADBEEF,
        "address": 0x1D00000,
    }
    with open("../globals/patch/Database.patch", "r") as file:
        for line in file:
            if match := re.match(r"#define\s*.Table:RomOffset\s*(\S*)", line):
               table_info["address"] = int(match.group(1), 16)
            elif match := re.match(r"#define\s*.Table:Header:MagicValue\s*(\S*)", line):
                table_info["magic_value"] = int(match.group(1), 16)
    return table_info

def create_table(default_table):

    def get_keys(db, filepath):
        with open(filepath, "r") as file:
            for line in file:
                if match := re.match(r"#export\s*.DBKey:(\S*):(\S*)\s*(\S*)", line):
                    table = match.group(1)
                    attribute = match.group(2)
                    key = int(match.group(3), 16)
                    if table not in db:
                        db[table] = {}

                    if data := default_table.get(table, {}).get(attribute):
                        default_value = data["value"]
                        default_type = data["enum_type"]
                        db[table][attribute] = {
                            "key": key,
                            "value": default_value,
                            "attribute": attribute,
                            "table": table,
                            "enum_type": {
                                0xAF: "Option",
                                0xA1: "Item" if "ShopPrice" not in attribute else "ItemPrice",
                                0xA2: "Actor",
                                0xA3: "Entrance",
                                0xA4: "Palette",
                            }.get((key & 0xFF000000) >> 24)
                        }
    db = {}
    get_keys(db, "../globals/patch/DatabaseKeys.patch")
    get_keys(db, "../globals/patch/generated/keys.patch")
    

    db["Entrance"] = {}
    for map_name,entrance_data in default_table["Entrance"].items():
        db["Entrance"][map_name] = {}
        for entrance,data in entrance_data.items():
            db_key = (data["byte_id"] << 24) | (data["area"] << 16) | (data["map"] << 8) | data["entry"]
            db["Entrance"][map_name][entrance] = {
                "key": db_key,
                "value": db_key & 0x00FFFFFF,
                "map_name": map_name,
                "entrance": entrance,
                "enum_type": {
                    0xAF: "Option",
                    0xA1: "Item",
                    0xA2: "Actor",
                    0xA3: "Entrance",
                    0xA4: "Palette",
                }.get((db_key & 0xFF000000) >> 24)
            }

    return db

def get_map_linkages():
    linkages = {}

    for filename in os.listdir("../map/src/"):
        if filename.endswith(".xml"):
            map_name = filename.replace(".xml", "").upper()
            xml_tree = ET.parse(f"../map/src/{filename}")
            linkages[map_name] = {}
            root = xml_tree.getroot()
            for child in root.iter():
                if child.tag == "Generators":
                    for element in child:
                        data = element.attrib
                        exit_id = int(data["entry"].split("Entry")[1])
                        dest_map = data["destMap"].upper()
                        dest_entry = int(data["destEntry"].split("Entry")[1])
                        linkages[map_name][exit_id] = {
                            "dest_map": dest_map,
                            "dest_entry": dest_entry,
                        }
    return linkages