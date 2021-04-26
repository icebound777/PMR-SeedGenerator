import random
import sqlite3

from db.item import Item, ItemRelation


# WIP
progress = [
    # Chapter 0
    "MagicalSeed1",

    # Chapter 1
    "KoopersShell",
    "FortressKey",
    "FortressKey",
    "FortressKey",
    "FortressKey",

    # Chapter 2
    "MagicalSeed2",
    "PulseStone",
    "RuinsKey",
    "RuinsKey",
    "RuinsKey",
    "DiamondStone",
    "PyramidStone",
    "RuinsKey",
    "LunarStone",

    # Chapter 3
    "MagicalSeed3",
    "Weight",
    "Record",
    "BoosPortrait",
    "CastleKey1",
    "CastleKey2",
    #"CastleKey3",

    # Chapter 4
    # "Cake",
    # Technically need these if playing blind?
    # "Dictionary",
    # "MysteryNote",

    # Chapter 5
    "JadeRaven",
    "MagicalSeed4",

    # Chapter 6
    "MagicalBean",
    "CrystalBerry",
    "FertileSoil",
    "MiracleWater",
    "WaterStone",

    # Chapter 7
    "Bucket",
    "Scarf",
    "StarStone",
    "BlueKey",
    "RedKey",
    "PalaceKey",

    # Chapter 8
    "PrisonKey1",
]


def shuffle_entrances(pairs, by_type=None):
    if by_type:
        pairs = [pair for pair in pairs if pair["src"].entrance_type == by_type]

    if len(pairs) % 2 != 0:
        pairs = pairs[:-1]

    # Swap connections between one link with the next one
    random.shuffle(pairs)
    for i in range(0, len(pairs), 2):
        first = pairs[i]
        second = pairs[i+1]
        e1 = first["src"]
        e2 = first["src"].destination
        e3 = second["src"]
        e4 = second["src"].destination

        e1.destination = e3
        e2.destination = e4
        e3.destination = e1
        e4.destination = e2

        e1.save()
        e2.save()
        e3.save()
        e4.save()

def shuffle_items(items, by_type=None):
    if by_type:
        items = [item for item in items if item.item_type == by_type]

    if len(items) % 2 != 0:
        items = items[:-1]

    random.shuffle(items)
    for i in range(0, len(items), 2):
        first = items[i]
        second = items[i+1]
        first.swap(second)


def place_items(app):
    mario = {
        "partners": set(),
        "items": [],
        "boots": 0,
        "hammer": 0,
        "progression_level": 0,
    }

    ch1_relations = ItemRelation.select().where(ItemRelation.chapter == 1).order_by(ItemRelation.level, ItemRelation.id.asc())
    for relation in ch1_relations:
        if relation.valid(mario):
            print(f"Obtainable: {relation}")
        elif relation.level > mario["progression_level"]:
            print(f"Could not pass: {relation}. STOPPING.")
            break
        else:
            print(f"Could not get: {relation} (but can still progress further)")

    """
    # Compare randomized database with default and log the changes
    with open("./debug/item_placement.txt", "w") as file:
        connection = sqlite3.connect("default_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM item INNER JOIN maparea ON item.map_area_id = maparea.id WHERE maparea.name != 'Options'")
        for data in cursor.fetchall():
            map_name = data[15]
            key_name = data[6]
            item_name = data[9]
            area_id = data[1]
            map_id = data[2]
            index = data[3]
            key = (0xA1 << 24) | (area_id << 16) | (map_id << 8) | index

            item = Item.get(Item.area_id==area_id, Item.map_id==map_id, Item.index==index)
            file.write(f"[{item.map_area.name}] ({item.map_area.verbose_name}): {item.key_name} - {item_name} -> {item.item_name}\n")
            app.processEvents()
    """


    



        