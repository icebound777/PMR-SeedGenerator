import os
import re
import json

from enums import Enums, enum_int, create_enums
from utility import get_files


def gather_keys():
    """
    Gather a list of ALL keys under the ../globals/patch/ directory
    AF = Options
    A1 = Items
    A2 = Actors
    A3 = Entrances
    A4 = Palettes
    A5 = 
    A6 = Moves (cost FP/BP)
    AA = RESERVED (see table.py unique itemID)
    AF = Quizzes
    """
    files = get_files("../../globals/patch")
    keys = {
        "items": {},
        "item_prices": {},
        "move_costs": {},
        "actors": {},
        "entrances": {},
        "palettes": {},
        "options": {},
        "quizzes": {},
    }
    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as file:
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
                            "actor_id": map_id,
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
                    elif byte_id == 0xA6:
                        cost_type,move = key_info.split(":")
                        keys["move_costs"][key] = {
                            "name": move,
                            "cost_type": cost_type,
                            "byte_id": byte_id,
                            "area_id": area_id,
                            "map_id": map_id,
                            "value_id": value_id,
                        }
                    elif byte_id == 0xAF:
                        name,attribute = key_info.split(":")
                        if name in ("Options", "Cosmetic"):
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
    with open("./debug/keys.json", "w", encoding="utf-8") as file:
        json.dump(keys, file, indent=4)

def gather_values():
    def get_value(value):
        # Booleans
        if value == ".True":
            return True
        if value == ".False":
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

        return None

    create_enums()

    values = {
        "items": {},
        "item_prices": {},
        "move_costs": {},
        "actors": {},
        "entrances": {},
        "palettes": {},
        "options": {},
        "quizzes": {},
    }
    with open(os.path.abspath(__file__ + "/../../../globals/patch/DatabaseDefaults.patch"), "r", encoding="utf-8") as file:
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
                elif "Move" in key_info: # MoveBP:SpinSmash                 1`
                    name = key_info.split(":")[-1]
                    cost_type = key_info.split(":")[0][-2:]
                    if name not in values["move_costs"]:
                        values["move_costs"][name] = {}
                    values["move_costs"][name][cost_type] = get_value(value)
                # Check for map name (which means it's an item or item price)
                elif match := re.match(r"([A-Z]{2,5}_\d+):(\S*)", key_info):
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
                # Check for actor data
                elif any(["HP" in key_info,
                          "Damage" in key_info,
                          "Level" in key_info,
                          "Increment" in key_info]):
                    actor,attribute = key_info.split(":")
                    value = get_value(value)
                    if actor not in values["actors"]:
                        values["actors"][actor] = {}
                    values["actors"][actor][attribute] = value

    with open("../../globals/patch/Actors.patch", "r", encoding="utf-8") as file:
        for line in file:
            if match := re.match(r"#export\s*.ActorPtr:", line):
                data = line[match.end():]
                match = re.match(r"(\S*)\s*(\S*)", data)
                actor, pointer = match.group(1), match.group(2)
                if actor not in values["actors"]:
                    values["actors"][actor] = {}
                values["actors"][actor]["Pointer"] = int(pointer, base=16)

    with open("./debug/values.json", "w", encoding="utf-8") as file:
        json.dump(values, file, indent=4)

def get_default_table():
    # Get general data
    db = {}
    with open(os.path.abspath(__file__ + "/../../globals/patch/DatabaseDefaults.patch"), "r", encoding="utf-8") as file:
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
    with open(os.path.abspath(__file__ + "/../../globals/patch/RandomEntrances.patch"), "r", encoding="utf-8") as file:
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
        "db_size": 0,
        "seed": 0xDEADBEEF,
        "address": 0x1D00000,
        "formations_offset": 0,
        "itemhints_offset": 0,
    }

    return table_info


def create_table(default_table):

    def get_keys(db, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                if match := re.match(r"#export\s*.DBKey:(\S*):(\S*)\s*(\S*)", line):
                    table = match.group(1)
                    attribute = match.group(2)
                    key = int(match.group(3), 16)
                    if table not in db:
                        db[table] = {}

                    if data := default_table.get(table, {}).get(attribute):
                        default_value = data["value"]
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
                                0xA6: "Move"
                            }.get((key & 0xFF000000) >> 24)
                        }
    db = {}
    get_keys(db, os.path.abspath(__file__ + "/../../globals/patch/DatabaseKeys.patch"))
    get_keys(db, os.path.abspath(__file__ + "/../../globals/patch/generated/keys.patch"))

    db["Entrance"] = {}
    for map_name,entrance_data in default_table["Entrance"].items():
        db["Entrance"][map_name] = {}
        for entrance,data in entrance_data.items():
            db_key = (data["byte_id"] << 24) \
                   | (data["area"] << 16) \
                   | (data["map"] << 8) \
                   | data["entry"]
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
                    0xA6: "Move"
                }.get((db_key & 0xFF000000) >> 24)
            }

    return db
