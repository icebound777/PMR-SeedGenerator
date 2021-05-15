import random
import sqlite3

from db.itemlocation import ItemLocation
from db.item import Item

from progression.hos_objects import requirements as requirements_hos
from progression.mac_objects import requirements as requirements_mac
from progression.tik_objects import requirements as requirements_tik
from progression.chapter_0.kmr_objects import requirements as requirements_kmr
from progression.chapter_1.nok_objects import requirements as requirements_nok
from progression.chapter_1.trd_objects import requirements as requirements_trd
from progression.chapter_2.iwa_objects import requirements as requirements_iwa
from progression.chapter_2.sbk_objects import requirements as requirements_sbk
from progression.chapter_2.dro_objects import requirements as requirements_dro
from progression.chapter_2.isk_objects import requirements as requirements_isk
from progression.chapter_3.mim_objects import requirements as requirements_mim
from progression.chapter_3.obk_objects import requirements as requirements_obk
from progression.chapter_3.arn_objects import requirements as requirements_arn
from progression.chapter_3.dgb_objects import requirements as requirements_dgb
from progression.chapter_4.omo_objects import requirements as requirements_omo
from progression.chapter_5.jan_objects import requirements as requirements_jan
from progression.chapter_5.kzn_objects import requirements as requirements_kzn
from progression.chapter_6.flo_objects import requirements as requirements_flo
from progression.chapter_7.sam_objects import requirements as requirements_sam
from progression.chapter_7.pra_objects import requirements as requirements_pra
from progression.chapter_8.kpa_objects import requirements as requirements_kpa
from progression.chapter_8.osr_objects import requirements as requirements_osr
from progression.chapter_8.kkj_objects import requirements as requirements_kkj

# import time


def place_items(app, isShuffle, algorithm):
    """Places items into item locations according to the given algorithm."""
    # timers = {}

    # Place items into item location
    if algorithm == "vanilla":
        # Place items in their vanilla locations
        for itemlocation in ItemLocation.select():
            itemlocation.current_item = itemlocation.vanilla_item
            itemlocation.save()

    elif algorithm == "random_fill":
        # Generate item pool
        item_pool = []

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
        # Place items in accessible locations first, then expand accessible locations by unlocked locations

        # timer_start = time.time()
        # timers['timer_start'] = timer_start
        def is_location_reachable(location, mario_inventory, requirements):
            is_reachable = True

            try:
                for requirement_group in requirements.get(location.map_area.name).get(location.key_name):
                    tmp_mario_inventory = mario_inventory[:]
                    list_requirement_group = list(requirement_group)

                    for requirement in list_requirement_group:
                        if requirement in tmp_mario_inventory:
                            list_requirement_group.remove(requirement)
                            tmp_mario_inventory.remove(requirement)

                    is_reachable = len(list_requirement_group) == 0
                    if is_reachable:
                        break
            except AttributeError:
                print("AttributeError: " + location.map_area.name + " " + location.key_name)
                raise
            return is_reachable

        # Generate item pool, requirements and starting inventory
        item_pool = []
        
        requirements = {}
        requirements |= (requirements_hos | requirements_mac | requirements_tik | requirements_kmr)
        requirements |= (requirements_nok | requirements_trd | requirements_iwa | requirements_sbk)
        requirements |= (requirements_dro | requirements_isk | requirements_mim | requirements_obk)
        requirements |= (requirements_arn | requirements_dgb | requirements_omo | requirements_jan)
        requirements |= (requirements_kzn | requirements_flo | requirements_sam | requirements_pra)
        requirements |= (requirements_kpa | requirements_osr | requirements_kkj)
        #print(len(requirements))
        
        mario_inventory = ['Hammer','SuperHammer','UltraHammer','SuperBoots','UltraBoots'
                           'Goombario', 'Kooper', 'Bombette', 'Parakarry', 'Bow', 'Watt', 'Sushie', 'Lakilester',
                           'p_OpenedToybox', 'p_PlacedToyTrain', 'p_PlacedRavenStatue',
                           'p_TalkedToRaphael', 'p_OpenedFlowerFields', 'p_PlantedBeanstalk']
        # timer_before_db = time.time()
        # timers['timer_before_db'] = timer_before_db

        # Fetch all locations and their items from the database
        all_locations = []
        for itemlocation in ItemLocation.select():
            all_locations.append(itemlocation)
            item_pool.append(itemlocation.vanilla_item)
        # timer_after_db = time.time()
        # timers['timer_after_db'] = timer_after_db

        # Order items into progression or non-progression groups
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
            # Find all reachable locations that are not in filled-locations
            reachable_locations = []
            for location in all_locations:
                if location not in filled_locations:
                    if is_location_reachable(location, mario_inventory, requirements):
                        reachable_locations.append(location)
            # Pop random reachable location
            random_location = reachable_locations.pop(random.randint(0,len(reachable_locations) - 1))
            # Pop random item from progression-itempool
            random_item = progression_items.pop(random.randint(0,len(progression_items) - 1))
            # Place item into location and mark location as filled
            random_location.current_item = random_item
            filled_locations.append(random_location)
            # Place item into mario_inventory
            mario_inventory.append(random_item.item_name)
            # Workaround for specific requirements not being actual items
            #add_hammer_boots_flags() #TODO
        
        # Place all remaining items
        for location in all_locations:
            if location not in filled_locations:
                # Pop random item from non progression items
                random_item = other_items.pop(random.randint(0,len(other_items) - 1))
                # Place item into location
                location.current_item = random_item
                filled_locations.append(location)
        # timer_after_random = time.time()
        # timers['timer_after_random'] = timer_after_random
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
        # timer_after_random_db = time.time()
        # timers['timer_after_random_db'] = timer_after_random_db
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
        
        # print("timer_before_db "       + format(timers.get('timer_start') - timers.get('timer_before_db')))
        # print("timer_after_db "        + format(timers.get('timer_start') - timers.get('timer_after_db')))
        # print("timer_after_random "    + format(timers.get('timer_start') - timers.get('timer_after_random')))
        # print("timer_after_random_db " + format(timers.get('timer_start') - timers.get('timer_after_random_db')))