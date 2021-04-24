import random

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

def place_items():
    # Starting data. This should grow as we place items so more options become available.
    # TODO: Initialize this based on configuration options
    mario = {
        "partners": [],
        "items": [],
        "boots": 0,
        "hammer": 0,
    }

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

        return True

    passes = 0
    while True:
        # Get a list of valid item slots based on our current state
        items = [item for item in filter(valid, Item.select())]
        if len(items) > 0:
            passes += 1
            print(f"Pass #{passes}")
            input()
            for item in items:
                print(item)
        else:
            unplaced_items = Item.select().where(Item.placed == False)
            print("Unplaced Items:")
            for item in unplaced_items:
                print(item)



        