import random
import sqlite3

from db.itemlocation import ItemLocation
from db.item import Item


def place_items(app, isShuffle, algorithm):
    """Places items into item locations according to the given algorithm."""

    # Generate item pool
    item_pool = []
    
    if isShuffle:
        for itemlocation in ItemLocation.select():
            current_item = itemlocation.vanilla_item
            item_pool.append(current_item)
    else:
        None # NYI

    # Place items into item location
    if algorithm == "vanilla":
        # Place items in their vanilla locations
        None # NYI

    elif algorithm == "random_fill":
        # Place items 100% randomly without any logic attached. Check for solvability afterwards, retry if necessary
        for itemlocation in ItemLocation.select():
            # Place random items
            itemlocation.current_item = item_pool.pop(random.randint(0,len(item_pool) - 1))
            itemlocation.save()
        # Check for solvability
        # NYI

    elif algorithm == "forward_fill":
        # Place items in accessible locations first, then expand accessible locations by unlocked locations
        None # NYI

    elif algorithm == "assumed_fill":
        # Start with all items in inventory, remove an item and try to place it at a reachable location
        None # NYI
    
    # Compare randomized database with default and log the changes
    with open("./debug/item_placement.txt", "w") as file:
        connection = sqlite3.connect("default_db.sqlite")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        select_statement = ("SELECT *\
                               FROM itemlocation\
                              INNER JOIN maparea\
                                 ON itemlocation.map_area_id = maparea.id")
        cursor.execute(select_statement)
        for tablerow in cursor.fetchall():
            #map_name = tablerow[15]
            key_name = tablerow['key_name']
            area_id = tablerow['area_id']
            map_id = tablerow['map_id']
            index = tablerow['index']
            #key = (0xA1 << 24) | (area_id << 16) | (map_id << 8) | index

            itemlocation = ItemLocation.get(ItemLocation.area_id==area_id, ItemLocation.map_id==map_id, ItemLocation.index==index)
            print(f"{itemlocation}")
            file.write(f"[{itemlocation.map_area.name}] ({itemlocation.map_area.verbose_name}): {itemlocation.key_name} - {itemlocation.vanilla_item.item_name} -> {itemlocation.current_item.item_name}\n")
            app.processEvents()