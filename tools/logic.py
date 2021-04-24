import random


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

        
        