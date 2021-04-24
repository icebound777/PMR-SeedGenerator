import random

from table import Table


def shuffle_pairs(pairs, by_type=None):
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

        rom_table = Table.instance
        rom_table["Entrance"][e1.map_name][e1.index]["value"] = e1.destination.get_key()
        rom_table["Entrance"][e2.map_name][e2.index]["value"] = e2.destination.get_key()
        rom_table["Entrance"][e3.map_name][e3.index]["value"] = e3.destination.get_key()
        rom_table["Entrance"][e4.map_name][e4.index]["value"] = e4.destination.get_key()

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

        
        