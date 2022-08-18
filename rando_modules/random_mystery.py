import random

from db.item import Item
from optionset import MysteryOptionSet

def get_random_mystery(mystery_settings:MysteryOptionSet) -> MysteryOptionSet:
    # If Random Choice is on, then none of the other settings matter
    if mystery_settings.mystery_random_choice:
        return mystery_settings

    if mystery_settings.mystery_random_pick:
        # Set possible items the same as Random Choice (see Item_Mystery.bpat)
        possible_items = []
        chosen_items = []
        
        mystery_itemid = Item.get(Item.item_name == "Mystery").value

        possible_items.extend(4 * [Item.get(Item.item_name == "Mushroom").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "SuperShroom").value])
        possible_items.extend(1 * [Item.get(Item.item_name == "UltraShroom").value])
        possible_items.extend(4 * [Item.get(Item.item_name == "HoneySyrup").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "MapleSyrup").value])
        possible_items.extend(1 * [Item.get(Item.item_name == "JamminJelly").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "POWBlock").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "FireFlower").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "SnowmanDoll").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "ThunderRage").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "ShootingStar").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "Pebble").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "Coconut").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "ThunderBolt").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "EggMissile").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "SleepySheep").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "DizzyDial").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "StopWatch").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "VoltShroom").value])
        possible_items.extend(2 * [Item.get(Item.item_name == "StoneCap").value])
        possible_items.extend(1 * [Item.get(Item.item_name == "RepelGel").value])
        possible_items.extend(4 * [mystery_itemid])

        # We have 7 item slots to fill, with the first one having a hardcoded
        # double-chance of occuring
        while len(chosen_items) < 7:
            random_item = random.choice(possible_items)
            if not (random_item == mystery_itemid
                and len([x for x in chosen_items if x == mystery_itemid]) >= 4
            ):
                chosen_items.append(random_item)
            if chosen_items[0] == mystery_itemid:
                chosen_items.pop(0)

        mystery_settings.mystery_itemA = chosen_items[0]
        mystery_settings.mystery_itemB = chosen_items[1]
        mystery_settings.mystery_itemC = chosen_items[2]
        mystery_settings.mystery_itemD = chosen_items[3]
        mystery_settings.mystery_itemE = chosen_items[4]
        mystery_settings.mystery_itemF = chosen_items[5]
        mystery_settings.mystery_itemG = chosen_items[6]
        for itemthing in chosen_items:
            print(Item.get(Item.value == itemthing))
    else:
        # Set vanilla
        mystery_settings.mystery_itemA = Item.get(Item.item_name == "Mushroom").value
        mystery_settings.mystery_itemB = Item.get(Item.item_name == "SuperShroom").value
        mystery_settings.mystery_itemC = Item.get(Item.item_name == "FireFlower").value
        mystery_settings.mystery_itemD = Item.get(Item.item_name == "StoneCap").value
        mystery_settings.mystery_itemE = Item.get(Item.item_name == "DizzyDial").value
        mystery_settings.mystery_itemF = Item.get(Item.item_name == "ThunderRage").value
        mystery_settings.mystery_itemG = Item.get(Item.item_name == "Pebble").value

    return mystery_settings
