import random
import sqlite3

from db.itemlocation import ItemLocation
from db.item import Item

from progression.chy_objects import requirements


def place_items(app, isShuffle, algorithm):
    """Places items into item locations according to the given algorithm."""

    # Generate item pool
    item_pool = []

    # Place items into item location
    if algorithm == "vanilla":
        # Place items in their vanilla locations
        None # NYI # TODO

    elif algorithm == "random_fill":
        # Place items 100% randomly without any logic attached. Check for solvability afterwards, retry if necessary
        for itemlocation in ItemLocation.select():
            item_pool.append(itemlocation.vanilla_item)
        
        for itemlocation in ItemLocation.select():
            # Place random items
            itemlocation.current_item = item_pool.pop(random.randint(0,len(item_pool) - 1))
            itemlocation.save()
            
        # Check for solvability
        # TODO

    elif algorithm == "forward_fill":
        def is_location_reachable(location, mario_inventory):
            is_reachable = True
            for requirement_group in requirements.get(location.map_area).get(location.key_name):
                is_reachable = len([req for req in requirement_group if req not in mario_inventory]) == 0
                if is_reachable:
                    break
            return is_reachable
        
        # Place items in accessible locations first, then expand accessible locations by unlocked locations

        mario_inventory = ['Hammer', 'Goombario']
        
        # Fetch all locations and their items from the database
        all_locations = []
        for itemlocation in ItemLocation.select():
            all_locations.append(itemlocation)
            item_pool.append(itemlocation.vanilla_item)

        # 
        progression_items = []
        other_items = []
        for item in item_pool:
            if item.progression:
                progression_items.append(item)
            else:
                other_items.append(item)

        filled_locations = []
        
        # Place all progression items first to guarantee the seed to be beatable
        while len(progression_items) > 0:
            # find all reachable locations that are not in filled-locations
            reachable_locations = []
            for location in [location for location in all_locations not in filled_locations]:
                if is_location_reachable(location, mario_inventory):
                    reachable_locations.append(location)
            # pop random reachable location
            random_location = reachable_locations.pop(random.randint(0,len(reachable_locations) - 1))
            # pop random item from progression-itempool
            random_item = progression_items.pop(random.randint(0,len(progression_items) - 1))
            # place item into location and mark location as filled
            random_location.current_item = random_item
            filled_locations.append(random_location)
            # place item into mario_inventory
            mario_inventory.append(random_item.item_name)
            # workaround for specific requirements not being actual items
            add_hammer_boots_flags()
        
        # Place all remaining items
        for location in [location for location in all_locations not in filled_locations]:
            # pop random item from non progression items
            random_item = other_items.pop(random.randint(0,len(other_items) - 1))
            # place item into location
            location.current_item = random_item
            filled_locations.append(location)

        # TODO make sure to recategorize mundane items that can be progression items before placing

        # Write new items to db
        for itemlocation in ItemLocation.select():
            # Find location that corresponds to the current db row
            for filled_location in filled_locations:
                if (filled_location.map_area == itemlocation.map_area
                    and filled_location.key_name == itemlocation.key_name):
                    current_location = filled_location
                    break
            # Place item and save row
            itemlocation.current_item = current_location.current_item
            itemlocation.save()

    elif algorithm == "assumed_fill":
        # Start with all items in inventory, remove an item and try to place it at a reachable location
        None # NYI # TODO
    
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
            key_name = tablerow['key_name']
            area_id = tablerow['area_id']
            map_id = tablerow['map_id']
            index = tablerow['index']

            itemlocation = ItemLocation.get(ItemLocation.area_id==area_id, ItemLocation.map_id==map_id, ItemLocation.index==index)
            print(f"{itemlocation}")
            file.write(f"[{itemlocation.map_area.name}] ({itemlocation.map_area.verbose_name}): {itemlocation.key_name} - {itemlocation.vanilla_item.item_name} -> {itemlocation.current_item.item_name}\n")
            app.processEvents()