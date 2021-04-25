import random
import sqlite3

from db.item import Item


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
    # Start with everything and take away things as we place items
    mario = {
        "partners": ["Goombario", "Kooper", "Bombette", "Parakarry", "Bow", "Watt", "Sushi", "Lakilester"],
        "items": [item for item in Item.select() if item.map_area.name != "Options" and item.item_type == "KEYITEM"],
        "boots": 2,
        "hammer": 2,
    }

    def update_state(item):
        for name,requirements in item.logic["requirements"].items():
            if name == "partners":
                for partner in requirements:
                    del mario["partners"][mario["partners"].index(partner)]
            if name == "items":
                for item in requirements:
                    if item in mario["items"]:
                        del mario["items"][mario["items"].index(item)]

    def valid(item):
        # If this item is already placed, it's not a valid option
        if item.placed:
            return False

        # Mario must have obtained these partners
        for partner in item.logic["requirements"].get("partners", []):
            if partner not in mario["partners"]:
                return False

        # Mario must have obtained these items
        for item in item.logic["requirements"].get("items", []):
            if item not in mario["items"]:
                return False
            
        # Mario must have an equal or greater boots value
        if item.logic["requirements"].get("boots", -1) > mario["boots"]:
            return False

        # Mario must have an equal or greater hammer value
        if item.logic["requirements"].get("hammer", -1) > mario["hammer"]:
            return False

        # Mario must have ability to flip starpiece panels
        if item.logic["requirements"].get("flip_panels", False):
            if mario["boots"] < 1 and mario["hammer"] < 2:
                return False

        return True

    key_items = [item for item in Item.select() if item.map_area.name != "Options" and item.item_type == "KEYITEM"]
    random.shuffle(key_items)

    # Place Key Items
    passes = 0
    while True:
        passes += 1
        app.processEvents()

        # Get a list of valid item slots based on our current state
        items = [item for item in filter(valid, Item.select())]
        random.shuffle(items)

        if len(key_items) == 0:
            break
        elif len(items) == 0:
            raise Exception("Ran out of item slots to place")

        # Place the next key item
        key_item = key_items.pop()
        item = items.pop()
        print(f"Items to place: {len(key_items)}. Placed: {item} -> ({key_item.item_name})")

        item.value = key_item.value
        item.item_type = key_item.item_type
        item.item_name = key_item.item_name
        item.placed = True
        item.save()

        # Update mario's state
        update_state(key_item)

    # Place non key items
    items = [item for item in Item.select() if item.map_area.name != "Options" and item.item_type != "KEYITEM" and item.placed != True]
    random.shuffle(items)
    passes = 0
    while True:
        passes += 1
        app.processEvents()

        # Get a list of valid item slots based on our current state
        item_slots = [item for item in filter(valid, Item.select())]
        random.shuffle(item_slots)

        if len(items) == 0:
            break
        elif len(item_slots) == 0:
            raise Exception("Ran out of item slots to place")

        # Place the next key item
        item = items.pop()
        item_slot = item_slots.pop()
        print(f"Items to place: {len(items)}. Placed: {item_slot} -> ({item.item_name})")

        item_slot.value = item.value
        item_slot.item_type = item.item_type
        item_slot.item_name = item.item_name
        item_slot.placed = True
        item_slot.save()

        # Update mario's state
        update_state(item)

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


    



        