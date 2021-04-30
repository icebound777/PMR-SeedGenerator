import random
import sqlite3

from enums import Enums
from db.item import Item
from db.map_area import MapArea

from simulate import simulate_gameplay


# Items in order of requirement to progress
required_items = [
    # Chapter 1
    "FortressKey",
    "FortressKey",
    "FortressKey",
    "FortressKey",

    # Chapter 2
    "PulseStone",
    "RuinsKey",
    "RuinsKey",
    "RuinsKey",
    "DiamondStone",
    "PyramidStone",
    "RuinsKey",
    "LunarStone",

    # Chapter 3
    "Weight",
    "Record",
    "BoosPortrait",
    "CastleKey1",
    "CastleKey1",

    # TODO

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
    extracted = []

    mario = None
    placed_items = []
    overflow = 0
    for key_item in required_items:

        mario,activated = simulate_gameplay(app, mario=mario)

        valid_slots = []
        for node in activated:
            if node.item_received:
                item = (Item.select()
                    .join(MapArea, on=(Item.map_area == MapArea.id))
                    .where(MapArea.name == node.map_name, Item.original_item_name == node.item_received, Item.index == node.index).select()
                    .get()
                )
                if not item.placed and item not in valid_slots:
                    valid_slots.append(item)

        if len(valid_slots) > 0:
            item = random.choice(valid_slots)
            extracted.append(item.item_name)

            placed_items.append((key_item, item))
            item.item_name = key_item
            item.item_type = "KEYITEM"
            item.value = Enums.get("Item")[key_item]
            item.placed = True
            item.save()

            mario.items = set([(received_item, i) for i,(received_item,_) in enumerate(placed_items)])
            mario.partners = {"Goombario", "Kooper"}
        else:
            overflow += 1

    mario = None
    for extracted_item in extracted:

        mario,activated = simulate_gameplay(app, mario=mario)

        valid_slots = []
        for node in activated:
            if node.item_received:
                item = (Item.select()
                    .join(MapArea, on=(Item.map_area == MapArea.id))
                    .where(MapArea.name == node.map_name, Item.original_item_name == node.item_received, Item.index == node.index).select()
                    .get()
                )
                if not item.placed and item not in valid_slots:
                    valid_slots.append(item)

        if len(valid_slots) > 0:
            item = random.choice(valid_slots)
            extracted.append(item.item_name)

            placed_items.append((extracted_item, item))
            item.item_name = extracted_item
            item.item_type = Item.get_type(Enums.get("Item")[extracted_item])
            item.value = Enums.get("Item")[extracted_item]
            item.placed = True
            item.save()

            mario.items = set([(received_item, i) for i,(received_item,_) in enumerate(placed_items)])
            mario.partners = {"Goombario", "Kooper"}
        else:
            overflow += 1

    print("Items Extracted:")
    for e in extracted:
        print("    " + str(e))

    print(f"Items Placed ({len(placed_items)}):")
    for received_item,item in placed_items:
        print(f"    {received_item} in {item}")
    
    if overflow > 0:
        print(f"WARNING: Couldn't find space for {overflow} items")

    # Compare randomized database with default and log the changes
    with open("./debug/item_placement.txt", "w") as file:
        connection = sqlite3.connect("default_db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM item INNER JOIN maparea ON item.map_area_id = maparea.id")
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


    



        