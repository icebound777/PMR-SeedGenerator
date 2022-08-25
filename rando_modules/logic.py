"""
This modules offers the randomization logic and takes care of actually randomizing
the game according to the settings chosen.
"""
import random
from copy import deepcopy
import logging
from collections import defaultdict

from db.node import Node
from db.item import Item
from db.map_area import MapArea
from worldgraph \
    import generate as generate_world_graph,\
           get_area_nodes,\
           get_area_edges,\
           hashabledict
from rando_modules.random_shop_prices import get_shop_price

from rando_modules.simulate import Mario

from rando_modules.modify_itempool \
    import get_scarcitied_itempool,\
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
    mario:Mario
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
                mario.add_to_inventory(edge.get("pseudoitems"))
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
    mario:Mario
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
                mario.add_to_inventory(current_item_name)
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



def _init_mario_inventory(
    starting_partners:list,
    starting_items:list,
    starting_boots:int,
    starting_hammer:int,
    partners_always_usable:bool,
    hidden_block_mode:int,
    startwith_bluehouse_open:bool,
    magical_seeds_required:int,
    startwith_toybox_open:bool,
    startwith_whale_open:bool,
    cook_without_fryingpan:bool,
    startwith_speedyspin: bool
) -> Mario:
    """
    Initializes Mario's starting inventory.
    This includes partners (for considering their overworld abilities during
    world graph traversal), equipment, as well as additional pseudoitems
    based on chosen settings.
    Starting equipment irrelevant to world graph traversal (such as Lucky Star,
    starting coins) is ignored.
    """
    mario = Mario()

    mario.add_to_inventory(starting_partners)
    if partners_always_usable:
        mario.add_to_inventory(all_partners_imp)
        mario.add_to_inventory("RF_PartnersAlwaysUsable")

    if starting_boots == 2:
        mario.add_to_inventory("BootsProxy3")
    if starting_boots in [1,2]:
        mario.add_to_inventory("BootsProxy2")
    if starting_boots in [0,1,2]:
        mario.add_to_inventory("BootsProxy1")
    if starting_hammer == 2:
        mario.add_to_inventory("HammerProxy3")
    if starting_hammer in [1,2]:
        mario.add_to_inventory("HammerProxy2")
    if starting_hammer in [0,1,2]:
        mario.add_to_inventory("HammerProxy1")

    for item in starting_items:
        mario.add_to_inventory(item.item_name)

    if hidden_block_mode == 3:
        # hidden blocks always visible
        mario.add_to_inventory("RF_HiddenBlocksVisible")

    if startwith_bluehouse_open:
        mario.add_to_inventory("GF_MAC02_UnlockedHouse")
    if startwith_toybox_open:
        mario.add_to_inventory("RF_ToyboxOpen")
    if startwith_whale_open:
        mario.add_to_inventory("RF_CanRideWhale")
    if cook_without_fryingpan:
        mario.add_to_inventory("RF_CanCook")
    if magical_seeds_required == 3:
        mario.add_to_inventory("RF_MagicalSeed1")
    elif magical_seeds_required == 2:
        mario.add_to_inventory(["RF_MagicalSeed1", "RF_MagicalSeed2"])
    elif magical_seeds_required == 1:
        mario.add_to_inventory(["RF_MagicalSeed1", "RF_MagicalSeed2", "RF_MagicalSeed3"])
    elif magical_seeds_required == 0:
        mario.add_to_inventory(["RF_MagicalSeed1", "RF_MagicalSeed2", "RF_MagicalSeed3", "RF_MagicalSeed4"])

    if startwith_speedyspin:
        mario.add_to_inventory("SpeedySpin")

    return mario


def _get_limit_items_to_dungeons(
    all_item_nodes,
    partners_always_usable:bool,
    partners_in_default_locations,
    starting_items:list,
    starting_boots:int,
    starting_hammer:int,
    starting_partners:list,
    hidden_block_mode:int,
    bowsers_castle_mode:int,
    start_with_speedyspin: bool
):
    """
    Logically places progression items into their 'dungeons', then returns a
    list of the affected item nodes, as well as lists for items places and items
    overwritten in those nodes.
    """
    modified_nodes = []
    items_placed = []
    items_overwritten = []

    areas_to_limit = [
        "TRD",
        "ISK",
        "DGB",
        "OMO",
        #"KZN",
        "FLO",
        "PRA",
    ]

    if bowsers_castle_mode == 0:
        areas_to_limit.append("KPA")

    additional_edges = {
        "TRD": [ 
            # Fortress Exterior Exit Bottom Left
            # -> Fortress Exterior Exit Top Left
            {
                "from": {"map": "TRD_00", "id": 0},
                "to":   {"map": "TRD_00", "id": 4},
                "reqs": [["Bombette"]]
            },
            # Fortress Exterior Exit Top Left
            # -> Fortress Exterior Exit Bottom Left
            {
                "from": {"map": "TRD_00", "id": 4},
                "to":   {"map": "TRD_00", "id": 0},
                "reqs": []
            }
        ],
    }

    remove_edges = {
        "TRD": [
            # Fortress Exterior Exit Bottom Left
            # -> Path to Fortress 2 Exit Bottom Right
            {
                "from": {"map": "TRD_00", "id": 0},
                "to":   {"map": "NOK_15", "id": 1},
                "reqs": []
            },
            # Fortress Exterior Exit Top Left
            # -> Path to Fortress 2 Exit Top Right
            {
                "from": {"map": "TRD_00", "id": 4},
                "to":   {"map": "NOK_15", "id": 2},
                "reqs": []
            },
        ],
        "ISK": [
            # Entrance Exit Left
            # -> N3W1 Ruins Entrance Enter Ruins
            {
                "from": {"map": "ISK_01", "id": 0},
                "to":   {"map": "SBK_02", "id": 4},
                "reqs": []
            },
        ],
        "DGB": [
            # Escape Scene Exit Left
            # -> Wasteland Ascent 2 Exit East
            {
                "from": {"map": "DGB_00", "id": 0},
                "to":   {"map": "ARN_04", "id": 1},
                "reqs": []
            },
        ],
        "OMO": [
            # BLU Station Spring to Toad Town
            # -> Residental District Toybox Spring
            {
                "from": {"map": "OMO_03", "id": 4},
                "to":   {"map": "MAC_04", "id": 2},
                "reqs": []
            },
        ],
        #"KZN": [],
        "FLO": [
            # Center Tree Door
            # -> Plaza District Flower Door
            {
                "from": {"map": "FLO_00", "id": 0},
                "to":   {"map": "MAC_01", "id": 5},
                "reqs": []
            },
        ],
        "PRA": [
            # Entrance Exit West
            # -> Shiver Mountain Peaks Exit East
            {
                "from": {"map": "PRA_01", "id": 0},
                "to":   {"map": "SAM_10", "id": 1},
                "reqs": []
            },
        ],
        "KPA": [
            # Ship Enter/Exit Scenes Leave Hangar To Starhaven
            # -> Riding Star Ship Scene Fly To Bowser's Castle
            {
                "from": {"map": "KPA_60",  "id": 4},
                "to":   {"map": "HOS_20",  "id": 2},
                "reqs": []
            },
            # Exit to Peach's Castle Door Top Right
            # -> Hijacked Castle Entrance Door West
            {
                "from": {"map": "KPA_121", "id": 1},
                "to":   {"map": "OSR_02",  "id": 0},
                "reqs": []
            },
        ],
    }

    starting_node_ids = {
        "TRD": "TRD_00/0",
        "ISK": "ISK_01/0",
        "DGB": "DGB_00/0",
        "OMO": "OMO_03/4",
        #"KZN": "",
        "FLO": "FLO_00/0",
        "PRA": "PRA_01/0",
        "KPA": "KPA_60/4",
    }

    additional_starting_items = {
        "DGB": ["EQUIPMENT_Boots_Progressive_2"],
        "OMO": ["MF_Ch4_CanThrowInTrain", "RF_CanVisitTayceT", "RF_CanVisitRussT"],
        "FLO": ["EQUIPMENT_Boots_Progressive_2"],
        "PRA": ["EQUIPMENT_Boots_Progressive_2"],
    }

    all_partners = all_partners_imp.copy()

    # If partners are forced into their default locations, then we have to
    # place key items with those partners considered unavailable
    exclude_starting_partners = {
        "TRD": "Bombette",
        "OMO": "Watt",
        "FLO": "Lakilester"
    }

    limited_filled_item_nodes = deepcopy(all_item_nodes)

    for area_name in areas_to_limit:
        # Build small world graph only encompassing the current area
        area_nodes = get_area_nodes(area_name)
        area_edges = get_area_edges(area_name)
        if area_name in additional_edges:
            area_edges.extend([hashabledict(x) for x in additional_edges.get(area_name)])
        if area_name in remove_edges:
            cleaned_area_edges = [x for x in area_edges if x not in remove_edges.get(area_name)]
            area_edges = cleaned_area_edges
        cur_area_graph = generate_world_graph(area_nodes,area_edges)
        if (partners_in_default_locations
        and area_name in exclude_starting_partners
        and exclude_starting_partners.get(area_name) not in starting_partners
        ):
            # place partners manually into their nodes, so they can be found
            # by the _find_new_nodes_and_edges call and added to inventory
            for node_id in cur_area_graph:
                if cur_area_graph[node_id]["node"].key_name_item == "Partner":
                    cur_area_graph[node_id]["node"].current_item = cur_area_graph[node_id]["node"].vanilla_item
                    list_index = -1
                    for filled_node in limited_filled_item_nodes:
                        if node_id == filled_node.identifier:
                            list_index = limited_filled_item_nodes.index(filled_node)
                    if list_index == -1:
                        raise ValueError
                    limited_filled_item_nodes.pop(list_index)


        # Prepare data structures
        pool_progression_items = []
        pool_misc_progression_items = []
        reachable_node_ids = set()
        reachable_item_nodes = {}
        non_traversable_edges = defaultdict(set)

        cur_items_placed = []
        cur_items_overwritten = []

        # Prepare item pools for current area
        for item_type in limited_by_item_areas.get(area_name):
            if item_type == "keys":
                for item in limited_by_item_areas.get(area_name).get(item_type):
                    pool_progression_items.append(Item.get(Item.item_name == item))
            if item_type == "misc":
                for item in limited_by_item_areas.get(area_name).get(item_type):
                    pool_misc_progression_items.append(Item.get(Item.item_name == item))

        # Remove items Mario starts with from the progression key items.
        # Don't touch misc progression items, as Mario might waste those.
        for item in starting_items:
            if item in pool_progression_items:
                pool_progression_items.remove(item)

        # Set node to start graph traversal from
        starting_node_id = starting_node_ids.get(area_name)

        # Find initially reachable nodes within the world graph
        for edge in cur_area_graph.get(starting_node_id).get("edge_list"):
            non_traversable_edges[starting_node_id].add(edge)

        # Reset Mario's inventory
        if partners_in_default_locations:
            almost_all_partners = [x for x in all_partners if x != exclude_starting_partners.get(area_name) or x in starting_partners]
            mario = _init_mario_inventory(
                almost_all_partners,
                starting_items,
                starting_boots,
                starting_hammer,
                partners_always_usable,
                hidden_block_mode,
                False,
                False,
                False,
                False,
                start_with_speedyspin
            )
        else:
            mario = _init_mario_inventory(
                all_partners,
                starting_items,
                starting_boots,
                starting_hammer,
                partners_always_usable,
                hidden_block_mode,
                False,
                False,
                False,
                False,
                start_with_speedyspin
            )
        if area_name in additional_starting_items:
            mario.add_to_inventory(additional_starting_items[area_name])

        # Find initially reachable nodes
        pool_misc_progression_items,    \
            _,                          \
            reachable_node_ids,         \
            reachable_item_nodes,       \
            non_traversable_edges,      \
            limited_filled_item_nodes,  \
            mario = \
            _find_new_nodes_and_edges(pool_misc_progression_items,
                                      None,
                                      cur_area_graph,
                                      reachable_node_ids,
                                      reachable_item_nodes,
                                      non_traversable_edges,
                                      limited_filled_item_nodes,
                                      mario)

        successfully_placed = False
        while not successfully_placed:
            pool_progression_items_try = pool_progression_items.copy()
            pool_misc_progression_items_try = pool_misc_progression_items.copy()
            reachable_node_ids_try = reachable_node_ids.copy()
            reachable_item_nodes_try = deepcopy(reachable_item_nodes)
            limited_filled_item_nodes_try = limited_filled_item_nodes.copy()
            non_traversable_edges_try = non_traversable_edges.copy()
            cur_area_graph_try = deepcopy(cur_area_graph)
            try:
                limited_filled_item_nodes_try,\
                cur_items_placed,             \
                cur_items_overwritten, mario = place_progression_items(
                    mario,
                    pool_progression_items_try,
                    pool_misc_progression_items_try,
                    None,
                    True,
                    reachable_node_ids_try,
                    reachable_item_nodes_try,
                    limited_filled_item_nodes_try,
                    non_traversable_edges_try,
                    cur_area_graph_try
                )
                successfully_placed = True
                limited_filled_item_nodes = limited_filled_item_nodes_try.copy()
            except IndexError:
                # Items were placed in a way that makes the seed unbeatable,
                # so we have to clear the lists and retry
                cur_items_placed = []
                cur_items_overwritten = []
                # Reset Mario's inventory
                if partners_in_default_locations:
                    almost_all_partners = [x for x in all_partners if x != exclude_starting_partners.get(area_name) or x in starting_partners]
                    mario = _init_mario_inventory(
                        almost_all_partners,
                        starting_items,
                        starting_boots,
                        starting_hammer,
                        partners_always_usable,
                        hidden_block_mode,
                        False,
                        False,
                        False,
                        False,
                        start_with_speedyspin
                    )
                else:
                    mario = _init_mario_inventory(
                        all_partners,
                        starting_items,
                        starting_boots,
                        starting_hammer,
                        partners_always_usable,
                        hidden_block_mode,
                        False,
                        False,
                        False,
                        False,
                        start_with_speedyspin
                    )

        items_placed.extend(cur_items_placed)
        items_overwritten.extend(cur_items_overwritten)

        area_goals = {
            "TRD": [[{"starspirits": 1}]],
            "ISK": [[{"starspirits": 1}]],
            "DGB": [["MysticalKey"]],
            "OMO": [[{"starspirits": 1}]],
            "KZN": [[{"starspirits": 1}]],
            "FLO": [[{"starspirits": 1}]],
            "PRA": [[{"starspirits": 1}]],
            "KPA": lambda: "KPA_121/1" in reachable_node_ids_try,
        }

        if area_name == "KPA":
            assert area_goals[area_name]()
        else:
            assert mario.requirements_fulfilled(area_goals[area_name])

    all_item_node_ids = [node.identifier for node in all_item_nodes]
    modified_nodes = [node for node in limited_filled_item_nodes if node.identifier not in all_item_node_ids]

    return modified_nodes, items_placed, items_overwritten


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
        if starting_hammer in [1,2]:
            item = Item.get(Item.item_name == "HammerProxy2")
            excluded_items.append(item)
        if starting_hammer in [0,1,2]:
            item = Item.get(Item.item_name == "HammerProxy1")
            excluded_items.append(item)
        if starting_boots == 2:
            item = Item.get(Item.item_name == "BootsProxy3")
            excluded_items.append(item)
        if starting_boots in [1,2]:
            item = Item.get(Item.item_name == "BootsProxy2")
            excluded_items.append(item)
        if starting_boots in [0,1,2]:
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
    item_scarcity:int,
    itemtrap_mode:int,
    startwith_bluehouse_open:bool,
    magical_seeds_required:int,
    keyitems_outside_dungeon:bool,
    partners_always_usable:bool,
    partners_in_default_locations:bool,
    always_speedyspin,
    always_ispy,
    always_peekaboo,
    hidden_block_mode:int,
    starting_partners:list,
    starting_items:list,
    starting_boots:int,
    starting_hammer:int,
    add_item_pouches:bool,
    bowsers_castle_mode:int,
    algorithm
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
                and current_node.identifier != "KMR_04/Bush7_Drop1"
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


    # Pre-fill 'dungeon' nodes if keyitems are limited to there
    items_to_remove_from_pools = []
    items_to_add_to_pools = []
    pre_filled_dungeon_nodes = []
    pre_filled_node_ids = []
    if not keyitems_outside_dungeon and algorithm == "ForwardFill":
        pre_filled_dungeon_nodes,\
            items_to_remove_from_pools,\
            items_to_add_to_pools = _get_limit_items_to_dungeons(
                    all_item_nodes,
                    partners_always_usable,
                    partners_in_default_locations,
                    starting_items,
                    starting_boots,
                    starting_hammer,
                    starting_partners,
                    hidden_block_mode,
                    bowsers_castle_mode
                )
        for node in pre_filled_dungeon_nodes:
            pre_filled_node_ids.append(node.identifier)

    # Check all remaining nodes for items to add to the pools
    all_item_nodes_ids = {node.identifier for node in all_item_nodes}
    for node_id in world_graph.keys():
        current_node = world_graph[node_id]["node"]
        is_item_node = current_node.key_name_item
        if is_item_node and node_id not in all_item_nodes_ids:
            all_item_nodes.append(current_node)
            all_item_nodes_ids.add(node_id)

            # Set current item to the one set during dungeon pre-fill
            if node_id in pre_filled_node_ids:
                node_index = pre_filled_node_ids.index(node_id)
                current_node.current_item = pre_filled_dungeon_nodes[node_index].current_item
                continue

            # Special casing for hammer bush during gear location shuffle w/o
            # hammerless: add modified "gear" Tayce T item to gear locations
            if (    current_node.identifier == "KMR_04/Bush7_Drop1"
                and starting_hammer != 0xFF
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

    items_to_remove_from_pools.extend(
        get_items_to_exclude(
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
    ))
    items_to_remove_from_pools.extend(starting_items)

    for item in items_to_add_to_pools:
        if item.progression:
            pool_progression_items.append(item)
        else:
            if (    item.item_name in progression_miscitems_names
                and item not in pool_misc_progression_items
            ):
                # Since progression misc items have to be placed in
                # replenishable locations, we only need one of each
                pool_misc_progression_items.append(item)
            else:
                pool_other_items.append(item)

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

    pool_other_items = get_scarcitied_itempool(pool_other_items, item_scarcity)

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
        mario.add_to_inventory(random_item.item_name)
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


#@deprecated
def _algo_forward_fill(
    item_placement,
    do_randomize_coins,
    do_randomize_shops,
    do_randomize_panels,
    randomize_favors_mode:int,
    randomize_letters_mode:int,
    do_randomize_radiotrade:bool,
    do_randomize_dojo,
    gear_shuffle_mode,
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
    reachable_node_ids = set()
    reachable_item_nodes = {}
    non_traversable_edges = defaultdict(set)
    ## Data structures for item pool
    pool_progression_items = []
    pool_other_items = []
    pool_misc_progression_items = []
    filled_item_nodes = []

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
        item_scarcity,
        itemtrap_mode,
        startwith_bluehouse_open,
        magical_seeds_required,
        keyitems_outside_dungeon,
        partners_always_usable,
        partners_in_default_locations,
        speedyspin,
        ispy,
        peekaboo,
        hidden_block_mode,
        starting_partners,
        starting_items,
        starting_boots,
        starting_hammer,
        add_item_pouches,
        bowsers_castle_mode,
        algorithm
    )

    print("Initialize Mario's starting inventory...")
    mario = _init_mario_inventory(
        starting_partners,
        starting_items,
        starting_boots,
        starting_hammer,
        partners_always_usable,
        hidden_block_mode,
        startwith_bluehouse_open,
        magical_seeds_required,
        startwith_toybox_open,
        startwith_whale_open,
        cook_without_fryingpan,
        speedyspin
    )

    # Set node to start graph traversal from
    starting_node_id = get_startingnode_id_from_startingmap_id(starting_map_id)
    print(f'Starting map: {starting_node_id}')

    # Find initially reachable nodes within the world graph
    for edge in world_graph.get(starting_node_id).get("edge_list"):
        non_traversable_edges[starting_node_id].add(edge)
    reachable_node_ids.add(starting_node_id)
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

    # Place items influencing progression, giving misc. items priority for
    # repleneshing item locations
    print("Placing Progression Items ...")
    successfully_placed = False
    while not successfully_placed:
        try:
            pool_progression_items_try = pool_progression_items.copy()
            pool_misc_progression_items_try = pool_misc_progression_items.copy()
            pool_other_items_try = pool_other_items.copy()
            reachable_node_ids_try = reachable_node_ids.copy()
            reachable_item_nodes_try = deepcopy(reachable_item_nodes)
            filled_item_nodes_try = filled_item_nodes.copy()
            non_traversable_edges_try = non_traversable_edges.copy()
            world_graph_try = deepcopy(world_graph)

            non_traversable_edges_try, _, _, mario = place_progression_items(
                mario,
                pool_progression_items_try,
                pool_misc_progression_items_try,
                pool_other_items_try,
                do_randomize_shops,
                reachable_node_ids_try,
                reachable_item_nodes_try,
                filled_item_nodes_try,
                non_traversable_edges_try,
                world_graph_try
            )
            successfully_placed = True
            pool_other_items = pool_other_items_try.copy()
            filled_item_nodes = filled_item_nodes_try.copy()
            world_graph = world_graph_try.copy()

        except IndexError:
            # Items were placed in a way that makes the seed unbeatable,
            # so we have to clear the lists and retry
            mario = _init_mario_inventory(
                starting_partners,
                starting_items,
                starting_boots,
                starting_hammer,
                partners_always_usable,
                hidden_block_mode,
                startwith_bluehouse_open,
                magical_seeds_required,
                startwith_toybox_open,
                startwith_whale_open,
                speedyspin
            )
            logging.info("Progression placement fail, retrying ...")

    # Mark all unreachable nodes, which hold pre-filled items, as filled
    for item_node in all_item_nodes:
        if item_node.current_item and item_node.identifier not in [x.identifier for x in filled_item_nodes]:
            filled_item_nodes.append(item_node)

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
        and item_node_id not in [node.identifier for node in filled_item_nodes]
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
            filled_item_nodes.append(item_node)
            logging.debug(
                "%s: %s",
                item_node_id,
                random_item.item_name
            )
            continue

        if item_node_id not in [node.identifier for node in filled_item_nodes]:
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
                filled_item_nodes.append(item_node)
                logging.debug(
                    "%s: %s",
                    item_node_id,
                    random_item.item_name
                )
            except ValueError as err:
                logging.warning(
                    "filled_item_nodes size: %d",
                    len(filled_item_nodes)
                )
                logging.warning(
                    "pool_other_items size: %d",
                    len(pool_other_items)
                )
                logging.warning(
                    "nodes left: %d",
                    {len([item_node_id not in [node.identifier for node in filled_item_nodes]])}
                )
                #raise
                item_node.current_item = item_node.vanilla_item
                logging.warning("%s", item_node_id)

    if "YOUWIN" in mario.items:
        print("Seed verification: Beatable! Yay!")
    else:
        raise UnbeatableSeedError("Seed verification: Not beatable! Booo!")

    # "Return" list of modified item nodes
    item_placement.extend(filled_item_nodes)

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
    mario:Mario
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
                mario.add_to_inventory(current_item.item_name)
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
        item_scarcity,
        itemtrap_mode,
        startwith_bluehouse_open,
        magical_seeds_required,
        keyitems_outside_dungeon,
        partners_always_usable,
        partners_in_default_locations,
        speedyspin,
        ispy,
        peekaboo,
        hidden_block_mode,
        starting_partners,
        starting_items,
        starting_boots,
        starting_hammer,
        add_item_pouches,
        bowsers_castle_mode,
        algorithm
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
        mario = _init_mario_inventory(
            starting_partners,
            starting_items,
            starting_boots,
            starting_hammer,
            partners_always_usable,
            hidden_block_mode,
            startwith_bluehouse_open,
            magical_seeds_required,
            startwith_toybox_open,
            startwith_whale_open,
            cook_without_fryingpan,
            speedyspin
        )

        for item_ in pool_combined_progression_items:
            mario.add_to_inventory(item_.item_name)

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

    mario = _init_mario_inventory(
        starting_partners,
        starting_items,
        starting_boots,
        starting_hammer,
        partners_always_usable,
        hidden_block_mode,
        startwith_bluehouse_open,
        magical_seeds_required,
        startwith_toybox_open,
        startwith_whale_open,
        cook_without_fryingpan,
        startwith_speedyspin
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
                    mario.add_to_inventory(item.item_name)

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

    elif algorithm == "ForwardFill":
        # Place items in accessible locations first, then expand accessible
        # locations by unlocked locations
        _algo_forward_fill(
            item_placement,
            do_randomize_coins,
            do_randomize_shops,
            do_randomize_panels,
            randomize_favors_mode,
            randomize_letters_mode,
            do_randomize_radiotrade,
            do_randomize_dojo,
            gear_shuffle_mode,
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
