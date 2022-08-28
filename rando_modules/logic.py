"""
This modules offers the randomization logic and takes care of actually randomizing
the game according to the settings chosen.
"""
import random
import logging
from collections import defaultdict

from db.node import Node
from db.item import Item
from db.map_area import MapArea
from rando_modules.random_shop_prices import get_shop_price

from models.MarioInventory import MarioInventory

from rando_modules.modify_itempool \
    import get_randomized_itempool,\
           get_trapped_itempool

from rando_modules.unbeatable_seed_error import UnbeatableSeedError

from metadata.itemlocation_replenish import replenishing_itemlocations
from metadata.itemlocation_special import \
    kootfavors_reward_locations,          \
    kootfavors_keyitem_locations,         \
    chainletter_giver_locations,          \
    chainletter_final_reward_location,    \
    simpleletter_locations,               \
    radio_trade_event_locations,          \
    dojo_locations,                       \
    limited_by_item_areas,                \
    bush_tree_coin_locations
from metadata.progression_items                                 \
    import progression_miscitems as progression_miscitems_names, \
           progression_items
from metadata.item_exclusion \
    import exclude_due_to_settings, exclude_from_taycet_placement
from metadata.item_general import taycet_items
from metadata.partners_meta import all_partners as all_partners_imp
from metadata.node_exclusion import exclude_from_trap_placement

from metadata.verbose_area_names import verbose_area_names
from metadata.verbose_item_names import verbose_item_names
from metadata.verbose_item_locations import verbose_item_locations

def get_startingnode_id_from_startingmap_id(starting_map_id):
    """Returns the starting node id (e.g. "MAC_00/4") for a given map id."""
    # Extract entrance, map and area from map-hex
    starting_map_hex = hex(starting_map_id)[2:]
    starting_map_entrance_id = int(starting_map_hex[-1:], 16)
    starting_map_map_id = int(starting_map_hex[-4:-2], 16) if starting_map_hex[-4:-2] != "" else 0
    starting_map_area_id = int(starting_map_hex[-6:-4], 16) if starting_map_hex[-6:-4] != "" else 0

    # Get maparea from db
    starting_maparea = MapArea.get(  (MapArea.area_id == starting_map_area_id)
                                   & (MapArea.map_id  == starting_map_map_id))

    # String concat maparea-name and entrance-id to node-id string
    starting_node_id = starting_maparea.name + "/" + str(starting_map_entrance_id)

    return starting_node_id


def get_edge_target_node_id(edge):
    """Returns the node_id of a given edge's target node in string format"""
    if "target_node_id" not in edge:
        edge["target_node_id"] = f'{edge["to"]["map"]}/{edge["to"]["id"]}'
    return edge["target_node_id"]


def get_edge_origin_node_id(edge):
    """Returns the node_id of a given edge's origin node in string format"""
    if "origin_node_id" not in edge:
        edge["origin_node_id"] = f'{edge["from"]["map"]}/{edge["from"]["id"]}'
    return edge["origin_node_id"]


def is_itemlocation_replenishable(item_node):
    """
    Returns True if the location described by a given node is replenishable,
    that is, the item at this location can be acquired multiple times.
    """
    node_id = item_node.identifier
    return (node_id in replenishing_itemlocations)


def _get_random_taycet_item():
    """
    Randomly pick a Tayce T. item object chosen out of all allowed Tayce T.
    items.
    """
    random_taycet_item_value = random.choice([x for x in taycet_items if x not in exclude_from_taycet_placement])
    random_taycet_item = Item.get(Item.value == random_taycet_item_value)
    return random_taycet_item


def _depth_first_search(
    node_id:str,
    world_graph:dict,
    reachable_node_ids:set,
    reachable_item_nodes:dict,
    non_traversable_edges:defaultdict, #(set)
    mario:MarioInventory
):
    """
    Executes a DFS (depths first search) through the world graph, starting from
    a given node.
    If the given node is new, attempts to traverse all outgoing edges from
    said node.
    If all of an edge's requirements are fulfilled, adds edge's pseudoitems to
    Mario's inventory (if any), then attempts a recursive DFS of that edge's
    target node to further traverse the world graph.
    If an edge's requirements are not fulfilled, it is added to the list of
    reachable but not yet traversable edges.
    Returns whether or not one or more pseudoitems have been found during
    graph traversal.
    """
    #logging.debug("> DFS node %s", node_id)
    found_new_pseudoitems = False

    # Node already visited? -> Return!
    node_checked_earlier = False
    if node_id in reachable_node_ids:
        if non_traversable_edges[node_id]:
            node_checked_earlier = True
        else:
            return found_new_pseudoitems, mario
    else:
        reachable_node_ids.add(node_id)
    #logging.debug("DFS node_checked_earlier %s", node_checked_earlier)

    # If the current node is an item node and thus not an entrance node,
    # add it to the list of reachable item nodes for later item placement
    is_item_node = world_graph[node_id]["node"].key_name_item is not None
    if is_item_node and not node_checked_earlier:
        reachable_item_nodes[node_id] = world_graph[node_id]["node"]

    if not node_checked_earlier:
        # Get all outgoing edges
        outgoing_edges = world_graph[node_id]["edge_list"]
    else:
        # Get all formerly untraversable edges
        outgoing_edges = non_traversable_edges.pop(node_id)
    #logging.debug("DFS outgoing_edges %s", outgoing_edges)

    for edge in outgoing_edges:
        # Check if all requirements for edge traversal are fulfilled
        if mario.requirements_fulfilled(edge.get("reqs")):
            #logging.debug("DFS edge requirements fullfilled %s", edge)
            # Add all pseudoitems provided by this edge to the inventory
            if edge.get("pseudoitems") is not None:
                mario.add(edge.get("pseudoitems"))
                found_new_pseudoitems = True

            while edge in non_traversable_edges[node_id]:
                #logging.debug("DFS remove edge from non_traversable_edges %s",edge)
                #logging.debug("non_traversable_edges[node_id] before %s", non_traversable_edges[node_id])
                non_traversable_edges[node_id].remove(edge)
                #logging.debug("non_traversable_edges[node_id] after %s", non_traversable_edges[node_id])

            # DFS from newly reachable node
            edge_target_node_id = get_edge_target_node_id(edge)
            found_additional_pseudoitems, mario = _depth_first_search(
                edge_target_node_id,
                world_graph,
                reachable_node_ids,
                reachable_item_nodes,
                non_traversable_edges,
                mario
            )
            found_new_pseudoitems = found_new_pseudoitems or found_additional_pseudoitems
        else:
            non_traversable_edges[node_id].add(edge)
    return found_new_pseudoitems, mario


def _find_new_nodes_and_edges(
    pool_misc_progression_items:list,
    pool_other_items:list,
    world_graph:dict,
    reachable_node_ids:set,
    reachable_item_nodes:dict,
    non_traversable_edges:defaultdict, #(set)
    filled_item_nodes:list,
    mario:MarioInventory
):
    """
    Try to traverse already found edges which could not be traversed before.
    This re-traversing is accomplished by calling DFS on each respective edge's
    origin node ("from-node").
    """
    logging.debug("++++ _find_new_nodes_and_edges called")
    while True:
        found_new_items = False

        # We require a copy here since we cannot iterate over a list and
        # at the same time possibly delete entries from it (see DFS)
        non_traversable_edges_cpy = non_traversable_edges.copy()
        logging.debug(
            "non_traversable_edges_cpy before %s",
            non_traversable_edges_cpy.values()
        )

        # Re-traverse already found edges which could not be traversed before.
        node_ids_to_check = []
        for edges in non_traversable_edges.values():
            for edge in edges:
                # Generate list of unique node_ids to check to avoid multiple
                # checks of the same node
                from_node_id = get_edge_origin_node_id(edge)
                if from_node_id not in node_ids_to_check:
                    node_ids_to_check.append(from_node_id)

        logging.debug("%s", node_ids_to_check)
        for from_node_id in node_ids_to_check:
            found_additional_items, mario = _depth_first_search(
                from_node_id,
                world_graph,
                reachable_node_ids,
                reachable_item_nodes,
                non_traversable_edges_cpy,
                mario
            )
            found_new_items = found_new_items or found_additional_items
        non_traversable_edges = non_traversable_edges_cpy.copy()
        logging.debug(
            "non_traversable_edges_cpy after %s",
            non_traversable_edges_cpy.values()
        )
        logging.debug(
            "non_traversable_edges after %s",
            non_traversable_edges.values()
        )

        # Check if an item node is reachable which already has an item placed.
        # Since nodes are usually removed from this dict the moment an item is
        # placed there, this can only be true for node which's item is not being
        # randomized (caused by turned off shop shuffle, coin shuffle or
        # hidden panel shuffle).
        # If this is the case add item to inventory and remove node
        for node_id, item_node in reachable_item_nodes.items():
            current_item = item_node.current_item
            if current_item and item_node.identifier not in [x.identifier for x in filled_item_nodes]:
                current_item_name = current_item.item_name
                mario.add(current_item_name)
                found_new_items = True

                # Special case: Item location is replenishable, holds a misc.
                # item influencing progression and this type of item is yet to
                # be placed anywhere:
                # Consider item placed
                if (    is_itemlocation_replenishable(item_node)
                    and current_item in pool_misc_progression_items
                ):
                    pool_misc_progression_items.remove(current_item)
                    pool_other_items.append(current_item)

                filled_item_nodes.append(item_node)
                logging.debug(
                    "Pre-filled: %s: %s",
                    node_id,
                    current_item.item_name
                )
        
        # Keep searching for new edges and nodes until we don't find any new
        # items which might open up even more edges and nodes
        if not found_new_items:
            break
    logging.debug("non_traversable_edges after after %s", non_traversable_edges)
    logging.debug("---- _find_new_nodes_and_edges end")
    return pool_misc_progression_items, pool_other_items, reachable_node_ids, reachable_item_nodes, non_traversable_edges, filled_item_nodes, mario


def get_items_to_exclude(
    do_randomize_dojo:bool,
    starting_partners:list,
    startwith_bluehouse_open:bool,
    magical_seeds_required:int,
    bowsers_castle_mode:int,
    always_speedyspin:bool,
    always_ispy:bool,
    always_peekaboo:bool,
    gear_shuffle_mode:int,
    starting_hammer:int,
    starting_boots:int
) -> list:
    """
    Returns a list of items that should not be placed or given to Mario at the
    start.
    """
    excluded_items = []

    if do_randomize_dojo:
        for item_name in exclude_due_to_settings.get("do_randomize_dojo"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    for partner_string in starting_partners:
        partner_item = Item.get(Item.item_name == partner_string)
        excluded_items.append(partner_item)
    if startwith_bluehouse_open:
        for item_name in exclude_due_to_settings.get("startwith_bluehouse_open"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if magical_seeds_required < 4:
        for item_name in exclude_due_to_settings.get("magical_seeds_required").get(magical_seeds_required):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if bowsers_castle_mode > 0:
        for item_name in exclude_due_to_settings.get("shorten_bowsers_castle"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if always_speedyspin:
        for item_name in exclude_due_to_settings.get("always_speedyspin"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if always_ispy:
        for item_name in exclude_due_to_settings.get("always_ispy"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if always_peekaboo:
        for item_name in exclude_due_to_settings.get("always_peekaboo"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if gear_shuffle_mode >= 1:
        if starting_hammer == 2:
            item = Item.get(Item.item_name == "HammerProxy3")
            excluded_items.append(item)
        if starting_hammer >= 1:
            item = Item.get(Item.item_name == "HammerProxy2")
            excluded_items.append(item)
        if starting_hammer >= 0:
            item = Item.get(Item.item_name == "HammerProxy1")
            excluded_items.append(item)
        if starting_boots == 2:
            item = Item.get(Item.item_name == "BootsProxy3")
            excluded_items.append(item)
        if starting_boots >= 1:
            item = Item.get(Item.item_name == "BootsProxy2")
            excluded_items.append(item)
        if starting_boots >= 0:
            item = Item.get(Item.item_name == "BootsProxy1")
            excluded_items.append(item)

    return excluded_items


def _generate_item_pools(
    world_graph,
    pool_progression_items:list,
    pool_misc_progression_items:list,
    pool_other_items:list,
    all_item_nodes:list,
    do_randomize_coins:bool,
    do_randomize_shops:bool,
    do_randomize_panels:bool,
    randomize_favors_mode:int,
    randomize_letters_mode:int,
    do_randomize_radiotrade:bool,
    do_randomize_dojo:bool,
    gear_shuffle_mode:int,
    randomize_consumable_mode:int,
    item_scarcity:int,
    itemtrap_mode:int,
    startwith_bluehouse_open:bool,
    magical_seeds_required:int,
    keyitems_outside_dungeon:bool,
    partners_in_default_locations:bool,
    always_speedyspin,
    always_ispy,
    always_peekaboo,
    starting_partners:list,
    starting_items:list,
    starting_boots:int,
    starting_hammer:int,
    add_item_pouches:bool,
    bowsers_castle_mode:int
):
    """
    Generates item pools for items to be shuffled (depending on chosen
    settings this may exclude certain items). The item pools generated are
    pool_progression_items (keyitems that influence progression),
    pool_misc_progression_items (non-keyitems that influence progression) and
    pool_other_items (every other item). Additionally marks item nodes that
    shall not be randomized as already filled.
    """

    # Pre-fill nodes that are not to be randomized
    for node_id in world_graph.keys():
        current_node = world_graph[node_id]["node"]
        is_item_node = current_node.key_name_item
        if is_item_node: # and current_node not in all_item_nodes:

            current_node_id = current_node.identifier

            # temp. don't rando coins in trees or bushes
            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in bush_tree_coin_locations
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            # Check the randomization settings. If something is not supposed
            # to be randomized, mark location as filled by setting its
            # current_item value
            if (    current_node.vanilla_item.item_name == "Coin"
                and not do_randomize_coins
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item.startswith("Shop")
                and not do_randomize_shops
            ):
                current_node.current_item = current_node.vanilla_item
                current_node.current_item.base_price = get_shop_price(
                    current_node,
                    do_randomize_shops
                )
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item == "HiddenPanel"
                and not do_randomize_panels
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in kootfavors_reward_locations
                and randomize_favors_mode < 1
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in kootfavors_keyitem_locations
                and randomize_favors_mode < 2
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in chainletter_giver_locations
                and randomize_letters_mode < 3
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id == chainletter_final_reward_location
                and randomize_letters_mode < 2
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in simpleletter_locations
                and randomize_letters_mode < 1
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    not do_randomize_radiotrade
                and current_node_id in radio_trade_event_locations
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (   current_node_id in dojo_locations
                and not do_randomize_dojo
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item == "Partner"
                and partners_in_default_locations
                and current_node.vanilla_item.item_name not in starting_partners
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    gear_shuffle_mode not in [1,2]
                and current_node.vanilla_item.item_type == "GEAR"
                and (   current_node.identifier != "KMR_04/Bush7_Drop1"
                     or starting_hammer == -1)
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    gear_shuffle_mode not in [1,2]
                and current_node.identifier == "KMR_04/Bush7_Drop1"
            ):
                # special casing so the hammer bush is never empty but also
                # never holds required items or badges
                current_node.current_item = _get_random_taycet_item()
                all_item_nodes.append(current_node)
                continue


    # Check all remaining nodes for items to add to the pools
    all_item_nodes_ids = {node.identifier for node in all_item_nodes}
    for node_id in world_graph.keys():
        current_node = world_graph[node_id]["node"]
        is_item_node = current_node.key_name_item
        if is_item_node and node_id not in all_item_nodes_ids:
            all_item_nodes.append(current_node)
            all_item_nodes_ids.add(node_id)

            # Special casing for hammer bush during gear location shuffle w/o
            # hammerless: add modified "gear" Tayce T item to gear locations
            if (    current_node.identifier == "KMR_04/Bush7_Drop1"
                and starting_hammer != -1
                and gear_shuffle_mode == 1
            ):
                modified_taycet = _get_random_taycet_item()
                modified_taycet.item_type = "GEAR"
                pool_progression_items.append(modified_taycet)
                continue

            # Item shall be randomized: Add it to the correct item pool
            if (current_node.vanilla_item.progression
            or (do_randomize_shops and "StarPiece" in current_node.vanilla_item.item_name)
            or current_node.vanilla_item.item_type == "GEAR"
            ):
                pool_progression_items.append(current_node.vanilla_item)
            else:
                if (    current_node.vanilla_item.item_name in progression_miscitems_names
                    and current_node.vanilla_item not in pool_misc_progression_items
                ):
                    # Since progression misc items have to be placed in
                    # replenishable locations, we only need one of each
                    pool_misc_progression_items.append(current_node.vanilla_item)
                else:
                    pool_other_items.append(current_node.vanilla_item)

    # Swap random consumables for strange pouches if needed
    if add_item_pouches:
        pouch_items = [
            Item.get(Item.item_name == "PouchA"),
            Item.get(Item.item_name == "PouchB"),
            Item.get(Item.item_name == "PouchC"),
            Item.get(Item.item_name == "PouchD"),
            Item.get(Item.item_name == "PouchE"),
        ]

        cnt_items_removed = 0
        while True:
            rnd_index = random.randint(0, len(pool_other_items) - 1)
            rnd_item = pool_other_items.pop(rnd_index)
            if rnd_item.item_type == "ITEM":
                cnt_items_removed += 1
            else:
                pool_other_items.append(rnd_item)
            if cnt_items_removed == 5:
                break
        pool_other_items.extend(pouch_items)

    # If we start jumpless, add a progressive boots item to the item pool
    if starting_boots == 0xFF:
        new_boots = Item.get(Item.item_name == "BootsProxy1")
        while True:
            rnd_index = random.randint(0, len(pool_other_items) - 1)
            rnd_item = pool_other_items.pop(rnd_index)
            if rnd_item.item_type == "ITEM":
                break
            else:
                pool_other_items.append(rnd_item)
        pool_other_items.extend(new_boots)


    # Adjust item pools based on settings
    goal_size_item_pool = len(pool_progression_items)      \
                        + len(pool_misc_progression_items) \
                        + len(pool_other_items)

    items_to_remove_from_pools = get_items_to_exclude(
        do_randomize_dojo,
        starting_partners,
        startwith_bluehouse_open,
        magical_seeds_required,
        bowsers_castle_mode,
        always_speedyspin,
        always_ispy,
        always_peekaboo,
        gear_shuffle_mode,
        starting_hammer,
        starting_boots
    )
    items_to_remove_from_pools.extend(starting_items)

    while items_to_remove_from_pools:
        item = items_to_remove_from_pools.pop()
        if item in pool_progression_items:
            pool_progression_items.remove(item)
            continue
        if item in pool_misc_progression_items:
            pool_misc_progression_items.remove(item)
            continue
        if item in pool_other_items:
            pool_other_items.remove(item)
            continue
        logging.info(
            "Attempted to remove %s from item pools, but no pool"\
            " holds such item.",
            item
        )

    # If the item pool is too small now, fill it back up
    cur_size_item_pool = len(pool_progression_items)      \
                       + len(pool_misc_progression_items) \
                       + len(pool_other_items)
    while goal_size_item_pool > cur_size_item_pool:
        pool_other_items.append(_get_random_taycet_item())
        cur_size_item_pool = len(pool_progression_items)      \
                           + len(pool_misc_progression_items) \
                           + len(pool_other_items)

    # Randomize consumables if needed
    pool_other_items = get_randomized_itempool(pool_other_items, randomize_consumable_mode, item_scarcity)

    pool_other_items = get_trapped_itempool(
        pool_other_items,
        itemtrap_mode,
        randomize_favors_mode,
        do_randomize_dojo,
        keyitems_outside_dungeon
    )

    return pool_other_items


def place_progression_items(
    mario,
    pool_progression_items,
    pool_misc_progression_items,
    pool_other_items,
    do_randomize_shops,
    reachable_node_ids,
    reachable_item_nodes,
    filled_item_nodes,
    non_traversable_edges:defaultdict, #(set)
    world_graph
):
    if pool_other_items is None:
        pool_other_items = []
    items_placed = []
    items_overwritten = []
    if pool_other_items is None:
        pool_other_items = []

    starpieces = []
    if any(["StarPiece" in x.item_name for x in pool_progression_items]):
        print(f"Removing StarPieces temporarily ...")
        for item in [x for x in pool_progression_items if "StarPiece" in x.item_name]:
            starpieces.append(item)
        for item in starpieces:
            pool_progression_items.remove(item)

    size_prog_items = len(pool_progression_items)

    while pool_progression_items or pool_misc_progression_items:
        # Pick random reachable item node
        while True:
            random_node_key = random.choice(list(reachable_item_nodes.keys()))
            random_node = reachable_item_nodes.pop(random_node_key)
            if random_node_key not in [x.identifier for x in filled_item_nodes]:
                if not pool_progression_items:
                    # All keyitems already placed, search for replenish node
                    # for remaining misc items
                    if is_itemlocation_replenishable(random_node):
                        # Suitable replenishable node found
                        break
                else:
                    # Suitable Node found
                    break

        # If item node is replenishable and we have misc. items still to place,
        # then pick misc. item, otherwise any item will do
        if (    is_itemlocation_replenishable(random_node)
            and pool_misc_progression_items
        ):
            random_item_id = random.randint(0, len(pool_misc_progression_items) - 1)
            random_item = pool_misc_progression_items.pop(random_item_id)
        else:
            random_item_id = random.randint(0, len(pool_progression_items) - 1)
            random_item = pool_progression_items.pop(random_item_id)

        # Put chosen item into the randomly chosen item node, add item to
        # inventory, then check for newly reachable item nodes
        random_node.current_item = random_item
        mario.add(random_item.item_name)
        items_placed.append(random_item)
        items_overwritten.append(random_node.vanilla_item)
        node_identifier = random_node.identifier
        if "Shop" in node_identifier:
            random_node.current_item.base_price = get_shop_price(random_node, do_randomize_shops)
        filled_item_nodes.append(random_node)

        # Adjust item pools if necessary: Letters
        if (mario.has_parakarry_letters()
        and any(item.item_name.find("Letter") != -1 for item in pool_progression_items)
        ):
            print("Removing Letters from progressive pool ...")
            transfer_letters = []
            for item in pool_progression_items:
                if item.item_name.find("Letter") != -1:
                    transfer_letters.append(item)
            for item in transfer_letters:
                pool_progression_items.remove(item)
                pool_other_items.append(item)

        # Adjust item pools if necessary: StarPieces
        if (len(starpieces) > 0
        and size_prog_items / (len(pool_progression_items) + 1) > 1.5
        ):
            print(f"Adding removed StarPieces back ...")
            pool_progression_items.extend(starpieces)
            starpieces.clear()

        if (mario.starpiece_count >= 60
        and any(item.item_name.find("StarPiece") != -1 for item in pool_progression_items)
        ):
            print("Removing StarPieces from progressive pool ...")
            transfer_starpieces = []
            for item in pool_progression_items:
                if item.item_name.find("StarPiece") != -1:
                    transfer_starpieces.append(item)
            for item in transfer_starpieces:
                pool_progression_items.remove(item)
                pool_other_items.append(item)

        pool_misc_progression_items, \
        pool_other_items, \
        reachable_node_ids, \
        reachable_item_nodes, \
        non_traversable_edges, \
        filled_item_nodes, \
        mario = \
        _find_new_nodes_and_edges(pool_misc_progression_items,
                                  pool_other_items,
                                  world_graph,
                                  reachable_node_ids,
                                  reachable_item_nodes,
                                  non_traversable_edges,
                                  filled_item_nodes,
                                  mario)
        logging.debug(
            "non_traversable_edges after _find_new_nodes_and_edges %s",
            non_traversable_edges
        )
    logging.debug("non_traversable_edges after progression:")
    if logging.root.level == logging.DEBUG:
        for edge in non_traversable_edges:
            logging.debug("%s", edge)

    return filled_item_nodes, items_placed, items_overwritten, mario


def find_available_nodes(
    world_graph,
    starting_node_id,
    mario
):
    reachable_node_ids = set()
    reachable_item_nodes = {}
    non_traversable_edges = defaultdict(set)
    filled_item_node_ids = set()

    reachable_node_ids.add(starting_node_id)
    for edge in world_graph[starting_node_id]["edge_list"]:
        non_traversable_edges[starting_node_id].add(edge)

    empty_reachables, mario = find_empty_reachable_nodes(
        world_graph,
        reachable_node_ids,
        reachable_item_nodes,
        non_traversable_edges,
        filled_item_node_ids,
        mario
    )

    return empty_reachables, mario


def find_empty_reachable_nodes(
    world_graph:dict,
    reachable_node_ids:set,
    reachable_item_nodes:dict,
    non_traversable_edges:defaultdict,
    filled_item_node_ids:set,
    mario:MarioInventory
):
    """
    Try to traverse already found edges which could not be traversed before.
    This re-traversing is accomplished by calling DFS on each respective edge's
    origin node ("from-node").
    """
    logging.debug("++++ find_empty_reachable_nodes called")
    empty_item_nodes = []
    checked_item_node_ids = set()
    while True:
        found_new_items = False

        # Re-traverse already found edges which could not be traversed before.
        node_ids_to_check = set()
        for from_node_id, edges in non_traversable_edges.items():
            if edges:
                node_ids_to_check.add(from_node_id)

        logging.debug("%s", node_ids_to_check)
        for from_node_id in node_ids_to_check:
            found_additional_items, mario = _depth_first_search(
                from_node_id,
                world_graph,
                reachable_node_ids,
                reachable_item_nodes,
                non_traversable_edges,
                mario
            )
            found_new_items = found_new_items or found_additional_items

        # Check if an item node is reachable which already has an item placed.
        for node_id in (reachable_item_nodes.keys() - checked_item_node_ids):
            item_node = reachable_item_nodes[node_id]
            current_item = item_node.current_item
            if current_item:
                mario.add(current_item.item_name)
                found_new_items = True
                filled_item_node_ids.add(node_id)

            checked_item_node_ids.add(node_id)

        # Keep searching for new edges and nodes until we don't find any new
        # items which might open up even more edges and nodes
        if not found_new_items:
            break

    for node_id, item_node in sorted(reachable_item_nodes.items()):
        if node_id not in filled_item_node_ids:
            empty_item_nodes.append(item_node)

    return empty_item_nodes, mario


def _algo_assumed_fill(
    item_placement,
    do_randomize_coins,
    do_randomize_shops,
    do_randomize_panels,
    randomize_favors_mode:int,
    randomize_letters_mode:int,
    do_randomize_radiotrade:bool,
    do_randomize_dojo,
    gear_shuffle_mode:int,
    randomize_consumable_mode:int,
    item_scarcity,
    itemtrap_mode,
    starting_map_id,
    startwith_bluehouse_open,
    magical_seeds_required:int,
    startwith_toybox_open,
    startwith_whale_open,
    cook_without_fryingpan:bool,
    starting_partners,
    starting_boots,
    starting_hammer,
    speedyspin,
    ispy,
    peekaboo,
    partners_always_usable,
    partners_in_default_locations,
    hidden_block_mode:int,
    keyitems_outside_dungeon:bool,
    starting_items:list,
    add_item_pouches:bool,
    bowsers_castle_mode:int,
    world_graph,
    algorithm
):

    # Declare and init additional data structures
    ## Data structures for graph traversal
    all_item_nodes = []
    ## Data structures for item pool
    pool_progression_items = []
    pool_other_items = []
    pool_misc_progression_items = []
    filled_item_node_ids = set()

    # Generate item pool
    print("Generating item pool...")
    pool_other_items = _generate_item_pools(
        world_graph,
        pool_progression_items,
        pool_misc_progression_items,
        pool_other_items,
        all_item_nodes,
        do_randomize_coins,
        do_randomize_shops,
        do_randomize_panels,
        randomize_favors_mode,
        randomize_letters_mode,
        do_randomize_radiotrade,
        do_randomize_dojo,
        gear_shuffle_mode,
        randomize_consumable_mode,
        item_scarcity,
        itemtrap_mode,
        startwith_bluehouse_open,
        magical_seeds_required,
        keyitems_outside_dungeon,
        partners_in_default_locations,
        speedyspin,
        ispy,
        peekaboo,
        starting_partners,
        starting_items,
        starting_boots,
        starting_hammer,
        add_item_pouches,
        bowsers_castle_mode
    )

    starting_node_id = get_startingnode_id_from_startingmap_id(starting_map_id)

    print("Placing progression items...")
    #Place progression items, both key and replenishable
    pool_combined_progression_items = pool_progression_items + pool_misc_progression_items
    random.shuffle(pool_combined_progression_items)

    dungeon_restricted_items = {}
    if not keyitems_outside_dungeon:
        for dungeon in limited_by_item_areas:
            for itemlist in limited_by_item_areas[dungeon].values():
                for item in itemlist:
                    assert item not in dungeon_restricted_items
                    dungeon_restricted_items[item] = dungeon

    if gear_shuffle_mode == 1: # gear location shuffle
        pool_combined_progression_items.sort(key=lambda x: x.item_type == "GEAR")
    pool_combined_progression_items.sort(key=lambda x: x.item_name in dungeon_restricted_items.keys())

    while pool_combined_progression_items:
        item = pool_combined_progression_items.pop()
        mario = MarioInventory(
            starting_boots,
            starting_hammer,
            starting_partners,
            starting_items,
            partners_always_usable,
            hidden_block_mode,
            magical_seeds_required,
            startwith_bluehouse_open,
            startwith_toybox_open,
            startwith_whale_open,
            speedyspin,
            cook_without_fryingpan
        )

        for item_ in pool_combined_progression_items:
            mario.add(item_.item_name)

        candidate_locations, mario = find_available_nodes(
            world_graph,
            starting_node_id,
            mario
        )
        if item.item_name in progression_miscitems_names:
            candidate_locations = [node for node in candidate_locations if is_itemlocation_replenishable(node)]

        if item.item_name in dungeon_restricted_items:
            dungeon = dungeon_restricted_items[item.item_name]
            candidate_locations = [node for node in candidate_locations if node.map_area.name[:3] == dungeon]
            dungeon_restricted_items.pop(item.item_name)

        if gear_shuffle_mode == 1:
            # Gear Location Shuffle
            if item.item_type == "GEAR":
                candidate_locations = [node for node in candidate_locations if node.vanilla_item.item_type == "GEAR"]
            else:
                candidate_locations = [node for node in candidate_locations if node.vanilla_item.item_type != "GEAR"]


        if len(candidate_locations) == 0:
            raise UnbeatableSeedError("Failed to generate a beatable seed")

        placement_location = random.choice(candidate_locations)
        placement_location.current_item = item
        node_identifier = placement_location.identifier

        if "Shop" in node_identifier:
            placement_location.current_item.base_price = get_shop_price(placement_location, do_randomize_shops)

    # Mark all unreachable nodes, which hold pre-filled items, as filled
    for item_node in all_item_nodes:
        if item_node.current_item:
            filled_item_node_ids.add(item_node.identifier)

    # Place all remaining items into still empty item nodes
    print("Placing Miscellaneous Items ...")
    random.shuffle(pool_other_items)

    # Sort so shop nodes are in front to make sure those are filled with
    # non-traps
    all_item_nodes.sort(key=lambda x: x.is_shop(), reverse=True)

    for item_node in all_item_nodes:
        item_node_id = item_node.identifier

        if (item_node_id == "KMR_06/ItemA"
        and do_randomize_coins
        and item_node_id not in filled_item_node_ids
        ):
            # Do not put coin on the Goomba Road sign due to glitchy graphics
            item_index = -1
            for i_item, item in enumerate(pool_other_items):
                if item.item_name != "Coin":
                    item_index = i_item

            if item_index == -1:
                # No non-coin item in item-pool: Just place a Mushroom
                pool_other_items.pop()
                random_item = Item.get(Item.item_name == "Mushroom")
            else:
                random_item = pool_other_items.pop(item_index)

            item_node.current_item = random_item
            filled_item_node_ids.add(item_node_id)
            logging.debug(
                "%s: %s",
                item_node_id,
                random_item.item_name
            )
            continue

        if item_node_id not in filled_item_node_ids:
            # Place random remaining item here
            try:
                random_item_id = random.randint(0, len(pool_other_items) - 1)
                random_item = pool_other_items.pop(random_item_id)

                if "Shop" in item_node_id or item_node_id in exclude_from_trap_placement:
                    # Do not put item traps into shops or underwater -> it breaks otherwise!
                    while random_item.is_trapped():
                        pool_other_items.append(random_item)
                        random_item_id = random.randint(0, len(pool_other_items) - 1)
                        random_item = pool_other_items.pop(random_item_id)

                item_node.current_item = random_item

                if "Shop" in item_node_id:
                    item_node.current_item.base_price = get_shop_price(item_node, do_randomize_shops)

                filled_item_node_ids.add(item_node_id)
                logging.debug(
                    "%s: %s",
                    item_node_id,
                    random_item.item_name
                )

            except ValueError as err:
                logging.warning(
                    "filled_item_node_ids size: %d",
                    len(filled_item_node_ids)
                )
                logging.warning(
                    "pool_other_items size: %d",
                    len(pool_other_items)
                )
                logging.warning(
                    "nodes left: %d",
                    len([item_node_id not in filled_item_node_ids])
                )
                #raise
                item_node.current_item = item_node.vanilla_item
                logging.warning("%s", item_node_id)

    # "Return" list of modified item nodes
    item_placement.extend([node for node in all_item_nodes if node.current_item])


def get_item_spheres(
    item_placement,
    starting_map_id,
    startwith_bluehouse_open,
    magical_seeds_required:int,
    startwith_toybox_open,
    startwith_whale_open,
    cook_without_fryingpan:bool,
    starting_partners,
    starting_boots,
    starting_hammer,
    partners_always_usable,
    hidden_block_mode:int,
    starting_items:list,
    startwith_speedyspin,
    world_graph
):

    # Declare and init additional data structures
    ## Data structures for graph traversal
    reachable_node_ids = set()
    reachable_item_nodes = {}
    non_traversable_edges = defaultdict(set)
    ## Data structures for item pool
    pool_other_items = []
    pool_misc_progression_items = []
    filled_item_nodes = set()

    print("Writing Item Spheres")

    mario = MarioInventory(
        starting_boots,
        starting_hammer,
        starting_partners,
        starting_items,
        partners_always_usable,
        hidden_block_mode,
        magical_seeds_required,
        startwith_bluehouse_open,
        startwith_toybox_open,
        startwith_whale_open,
        startwith_speedyspin,
        cook_without_fryingpan
    )

    # Set node to start graph traversal from
    starting_node_id = get_startingnode_id_from_startingmap_id(starting_map_id)

    # Find initially reachable nodes within the world graph
    for edge in world_graph.get(starting_node_id).get("edge_list"):
        non_traversable_edges[starting_node_id].add(edge)

    reachable_node_ids.add(starting_node_id)

    item_spheres_text = "Starting Items:\n"
    item_placement_map = {}
    mario_item_history = mario.item_history

    for n in item_placement:
        item_placement_map[n.identifier] = n

    for item in mario_item_history:
        item_suffix = ""
        item = item[1:] # Remove the trailing + from items in initial mario history
        if item in progression_items.values() or item in progression_miscitems_names:
            item_suffix = "*"

        item_spheres_text += f'    ((Start) Mario\'s inventory): {item}{item_suffix}\n'

    sphere = 0
    while item_placement_map:
        pool_misc_progression_items, \
        pool_other_items, \
        reachable_node_ids, \
        reachable_item_nodes, \
        non_traversable_edges, \
        filled_item_nodes, \
        mario = \
        _find_new_nodes_and_edges(pool_misc_progression_items,
                                  pool_other_items,
                                  world_graph,
                                  reachable_node_ids,
                                  reachable_item_nodes,
                                  non_traversable_edges,
                                  filled_item_nodes,
                                  mario)

        item_spheres_text += '\n'
        if reachable_item_nodes:
            item_spheres_text += f'Sphere {sphere}:\n'
            nodes_to_print = list(reachable_item_nodes.values())
        else:
            item_spheres_text += f'Unreachable In Logic:\n'
            nodes_to_print = list(item_placement_map.values())

        nodes_to_print.sort(key=lambda node: (node.map_area.area_id, node.map_area.map_id, node.identifier))

        for node in nodes_to_print:
            item = item_placement_map.pop(node.identifier).current_item
            node_long_name = f'({verbose_area_names[node.map_area.name[:3]]}) {node.map_area.verbose_name} - {verbose_item_locations[node.map_area.name][node.key_name_item]}'
            item_verbose_name = verbose_item_names[item.item_name] if item.item_name in verbose_item_names else item.item_name

            item_suffix = ""
            if item.is_trapped():
                item_spheres_text += f'    ({node_long_name}): TRAP ({item_verbose_name})\n'
            else:
                if item.item_type != "ITEM" or is_itemlocation_replenishable(node):
                    if f"+{item.item_name}" not in mario_item_history and (item.item_name in progression_items.values() or item.item_name in progression_miscitems_names or item.item_type == 'GEAR'):
                        item_suffix = "*"
                    mario.add(item.item_name)

                item_spheres_text += f'    ({node_long_name}): {item_verbose_name}{item_suffix}\n'
        reachable_item_nodes.clear()
        sphere += 1

    assert "YOUWIN" in mario.items
    return item_spheres_text


def place_items(
    item_placement,
    algorithm,
    do_shuffle_items,
    do_randomize_coins,
    do_randomize_shops,
    do_randomize_panels,
    randomize_favors_mode:int,
    randomize_letters_mode:int,
    do_randomize_radiotrade:bool,
    do_randomize_dojo,
    gear_shuffle_mode:int,
    randomize_consumable_mode:int,
    item_scarcity,
    itemtrap_mode,
    starting_map_id,
    startwith_bluehouse_open,
    magical_seeds_required:int,
    startwith_toybox_open,
    startwith_whale_open,
    cook_without_fryingpan:bool,
    starting_partners,
    starting_boots,
    starting_hammer,
    speedyspin,
    ispy,
    peekaboo,
    partners_always_usable:bool,
    partners_in_default_locations,
    hidden_block_mode:int,
    keyitems_outside_dungeon:bool,
    starting_items:list,
    add_item_pouches:list,
    bowsers_castle_mode:int,
    world_graph = None
):
    """Places items into item locations according to chosen settings."""
    level = logging.INFO
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    if not do_shuffle_items:
        # Place items in their vanilla locations
        for node in Node.select().where(Node.key_name_item.is_null(False)):
            node.current_item = node.vanilla_item
            node.current_item.base_price = get_shop_price(
                node,
                do_randomize_shops=False
            )
            item_placement.append(node)
    elif algorithm == "AssumedFill":
        # Place items in a backward fill, ensuring a maximally deep fill.
        _algo_assumed_fill(
            item_placement,
            do_randomize_coins,
            do_randomize_shops,
            do_randomize_panels,
            randomize_favors_mode,
            randomize_letters_mode,
            do_randomize_radiotrade,
            do_randomize_dojo,
            gear_shuffle_mode,
            randomize_consumable_mode,
            item_scarcity,
            itemtrap_mode,
            starting_map_id,
            startwith_bluehouse_open,
            magical_seeds_required,
            startwith_toybox_open,
            startwith_whale_open,
            cook_without_fryingpan,
            starting_partners,
            starting_boots,
            starting_hammer,
            speedyspin,
            ispy,
            peekaboo,
            partners_always_usable,
            partners_in_default_locations,
            hidden_block_mode,
            keyitems_outside_dungeon,
            starting_items,
            add_item_pouches,
            bowsers_castle_mode,
            world_graph,
            algorithm
        )
