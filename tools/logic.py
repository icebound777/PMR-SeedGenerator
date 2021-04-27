import random
import sqlite3

from enums import Enums
from db.item import Item, ItemRelation
from db.map_area import MapArea


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
    partners = ["Goombario", "Kooper", "Bombette", "Parakarry", "Bow", "Watt", "Sushi", "Lakilester"]
    items = [
        item for item in items if item.item_type not in ["PARTNER", "PANEL", "PARTNER_REQUIRED", "NOTHING"]
    ]
    if by_type:
        items = [
            item for item in items
            if item.item_type == by_type
        ]

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
        "coins": 0,
        "star_pieces": 0,
        "progression_level": 0,
    }

    def display_state():
        print("    Items: " + ", ".join(mario["items"]))
        print("    Partners: " + ", ".join(mario["partners"]))
        print(f"    Hammer: {mario['hammer']}, Boots: {mario['boots']}, Star Pieces: {mario['star_pieces']}, Coins: {mario['coins']}")

    # Testing
    mario["partners"].add("Kooper")
    # mario["items"].append("FortressKey")

    """
    # Force a FortressKey to be placed here
    item = (
        Item.select()
        .join(MapArea, on=(Item.map_area == MapArea.id))
        .where(Item.index == 2, MapArea.name == "NOK_12")
        .get()
    )
    item.item_type = "KEYITEM"
    item.item_name = "FortressKey"
    item.value = Enums.get("Item")["FortressKey"]
    item.save()
    """

    chapter_relations = {i: ItemRelation.select().where(ItemRelation.chapter == i).order_by(ItemRelation.level, ItemRelation.id.asc()) for i in range(0, 9)}

    for chapter,relations in chapter_relations.items():
        print(f"CHAPTER {chapter}")
        unobtainable = set()
        can_continue = True
        for relation in relations:
            if not can_continue:
                unobtainable.add(relation)
            elif relation.valid(mario):
                if relation.level > mario["progression_level"]:
                    mario["progression_level"] = relation.level

                if relation.dest.item_type == "PARTNER":
                    mario["partners"].add(relation.dest.item_name)
                    print(f"OBTAINED PARTNER: {relation.dest.item_name} - {relation.comment}")
                elif relation.dest.item_type in ["ITEM", "KEYITEM", "BADGE"]:
                    mario["items"].append(relation.dest.item_name)
                    print(f"OBTAINED {relation.dest.item_type}: {relation.dest.item_name} - {relation.comment} ({relation.dest.map_area.name})")
                elif relation.dest.item_type == "STARPIECE":
                    mario["star_pieces"] += 1
                    print(f"OBTAINED STARPIECE - {relation.comment} ({relation.dest.map_area.name})")
                elif relation.dest.item_type == "COIN":
                    mario["coins"] += 1
                    print(f"OBTAINED COIN - {relation.comment} ({relation.dest.map_area.name})")

                if relation.src.original_item_type == "KEYITEM":
                    mario["items"].remove(relation.src.original_item_name)
                    print(f"USED {relation.src.original_item_name} - {relation.comment} ({relation.dest.map_area.name})")
            elif relation.level > mario["progression_level"]:
                unobtainable.add(relation)
                can_continue = False
                print(f"REACHED ROADBLOCK: {relation.comment}")
            else:
                unobtainable.add(relation)
        attainable = sorted(set(relations).difference(unobtainable), key=lambda relation: (relation.level, relation.id))
        print("Valid:\n - " + "\n - ".join([str(relation) for relation in attainable]))
        display_state()

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


    



        