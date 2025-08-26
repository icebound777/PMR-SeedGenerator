import os
import re
import json

import xml.dom.minidom

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
    A8 = Puzzles & Minigames
    A9 = Battles
    AA = RESERVED (see table.py unique itemID)
    AE = Static Map Mirroring (but we don't need them in the generator)
    AF = Quizzes
    """
    files = get_files("../../globals/patch")
    keys = {
        "items": {},
        "item_prices": {},
        "blocks": {},
        "move_costs": {},
        "actors": {},
        "entrances": {},
        "palettes": {},
        "options": {},
        "puzzles": {},
        "quizzes": {},
        "battles": {},
    }
    sprite_palette_counts = {}
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

                    if byte_id == 0xA1 and 0x40 <= value_id <= 0x4F:
                        name = key_info.split(":")[-1]
                        keys["blocks"][key] = {
                            "name": name,
                            "map_name": key_info.split(":")[0],
                            "byte_id": byte_id,
                            "area_id": area_id,
                            "map_id": map_id,
                            "value_id": value_id,
                        }
                    elif byte_id == 0xA1:
                        name = key_info.split(":")[-1]
                        if "ShopPrice" in name or "RewardAmount" in name:
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
                    elif byte_id == 0xA4:
                        sprite = key_info.split(":")[-1]
                        keys["palettes"][key] = {
                            "sprite": sprite
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
                    elif byte_id == 0xA8:
                        puzzle_name = key_info.split(":")[-1]
                        keys["puzzles"][key] = {
                            "puzzle": puzzle_name,
                            "index": (area_id << 16) | (map_id << 8) | value_id,
                        }
                    elif byte_id == 0xA9:
                        battle_name = key_info.split(":")[-1]
                        keys["battles"][key] = {
                            "name": battle_name,
                            "index": (area_id << 16) | (map_id << 8) | value_id,
                        }
                    elif byte_id == 0xAF:
                        name,attribute = key_info.split(":")
                        if name in ("Options", "Cosmetic", "Mystery"):
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
                elif match := re.match(r"#export\s*.PalCount:", line):
                    # Palette count per Sprite
                    data = line[match.end():]
                    match = re.match(r"(\S*)\s*(\S*)", data)
                    sprite, palette_count = match.group(1), match.group(2)
                    sprite_palette_counts[sprite] = palette_count
    for sprite, palette_count in sprite_palette_counts.items():
        for dbkey, sprite_dict in keys["palettes"].items():
            if sprite_dict["sprite"] == sprite:
                keys["palettes"][dbkey]["palette_count"] = int(palette_count.replace("`", ""))
    with open("./debug/keys.json", "w", encoding="utf-8") as file:
        json.dump(keys, file, indent=4)

def gather_values():
    item_list = {}
    items_doc = xml.dom.minidom.parse("../../globals/Items.xml")
    for item in items_doc.getElementsByTagName("Item"):
        item_name = item.getAttribute("name")
        item_value = int(item.getAttribute("index"), 16)
        item_list[item_name] = item_value

    def get_value(value, constants_dict: dict):
        if constants_dict and value in constants_dict:
            return get_value(constants_dict[value], None)

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
        except ValueError:
            pass
        else:
            return value

        # Items
        if value.startswith(".Item"):
            item = value.split(":")[-1]
            value = item_list[item]
            return value

        # Blocks
        if value.startswith(".BlockType"):
            # As per definition in RandomSuperBlocks.patch in base mod
            if "Multi" in value:
                value = 0
            elif "Super" in value:
                value = 1
            elif "Item" in value:
                value = 2
            else:
                raise ValueError
            return value

        # other Defines
        if value.startswith(".ColorMode"):
            # As per definition in RandomUI.patch in base mod
            if ":Fixed" in value:
                value = 0
            elif ":Random" in value:
                value = 1
            elif ":Animated" in value:
                value = 2
            else:
                raise ValueError
            return value

        if value.startswith(".Cutscenes"):
            # As per definition in DatabaseDefaults.patch in base mod
            if "Vanilla" in value:
                value = 0
            elif "Shortened" in value:
                value = 1
            elif "Minimal" in value:
                value = 2
            else:
                raise ValueError
            return value

        if value.startswith(".PanelHints"):
            # As per definition in DatabaseDefaults.patch in base mod
            if "Off" in value:
                value = 0
            elif "Vague" in value:
                value = 1
            elif "Concrete" in value:
                value = 2
            else:
                raise ValueError
            return value

        return None

    values = {
        "items": {},
        "item_prices": {},
        "blocks": {},
        "move_costs": {},
        "actors": {},
        "entrances": {},
        "palettes": {},
        "options": {},
        "puzzles": {},
        "quizzes": {},
        "battles": {},
    }

    file_path = "/../../../globals/patch/DatabaseDefaults.patch"
    db_constants = {}
    with open(os.path.abspath(__file__ + file_path), "r", encoding="utf-8") as file:
        for line in file:
            if match := re.match(r"#export\s(\S+)\s+(\S+)", line):
                db_constants[match.group(1)] = match.group(2)
                continue

            if match := re.match(r"\s*.DBKey:(\S*)\s*(\S*)", line):
                key_info = match.group(1)
                value = match.group(2)
                if "Options" in key_info or "Cosmetic" in key_info or "Mystery" in key_info:
                    name = key_info.split(":")[-1]
                    values["options"][name] = get_value(value, db_constants)
                elif "Puzzle" in key_info:
                    name = key_info.split(":")[-1]
                    values["puzzles"][name] = get_value(value, db_constants)
                elif "Quiz" in key_info:
                    name = key_info.split(":")[-1]
                    values["quizzes"][name] = get_value(value, db_constants)
                elif "Battle" in key_info:
                    name = key_info.split(":")[-1]
                    values["battles"][name] = get_value(value, db_constants)
                elif "Move" in key_info: # MoveBP:SpinSmash                 1`
                    name = key_info.split(":")[-1]
                    cost_type = key_info.split(":")[0][-2:]
                    if name not in values["move_costs"]:
                        values["move_costs"][name] = {}
                    values["move_costs"][name][cost_type] = get_value(value, db_constants)
                # Check for map name (which means it's an item, item price or block)
                elif match := re.match(r"([A-Z]{2,5}_\d+):(\S*)", key_info):
                    map_name = match.group(1)
                    key_name = match.group(2)
                    if "RandomBlock" in key_info and "Item" not in key_info:
                        if map_name not in values["blocks"]:
                            values["blocks"][map_name] = {}
                        values["blocks"][map_name][key_name] = get_value(value, db_constants)
                    elif "ShopPrice" in key_name or "RewardAmount" in key_name:
                        if map_name not in values["item_prices"]:
                            values["item_prices"][map_name] = {}
                        values["item_prices"][map_name][key_name] = get_value(value, db_constants)
                    else:
                        if map_name not in values["items"]:
                            values["items"][map_name] = {}
                        values["items"][map_name][key_name] = get_value(value, db_constants)
                # Check for actor data
                elif any(["HP" in key_info,
                          "Damage" in key_info,
                          "Level" in key_info,
                          "Increment" in key_info,
                          "Heal" in key_info]):
                    actor,attribute = key_info.split(":")
                    value = get_value(value, db_constants)
                    if actor not in values["actors"]:
                        values["actors"][actor] = {}
                    values["actors"][actor][attribute] = value

    file_path = "../../globals/patch/Actors.patch"
    with open(file_path, "r", encoding="utf-8") as file:
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
                                0xA6: "Move",
                                0xA8: "Puzzle",
                                0xA9: "Battle",
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
