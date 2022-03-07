"""
This modules offers the randomization logic and takes care of actually randomizing
the game according to the settings chosen.
"""
import random
from copy import deepcopy
import logging

from db.node import Node
from db.item import Item
from db.map_area import MapArea
from worldgraph \
    import generate as generate_world_graph,\
           get_node_identifier,\
           get_area_nodes,\
           get_area_edges
from rando_modules.random_shop_prices import get_shop_price
from rando_modules.simulate        \
    import add_to_inventory,       \
           clear_inventory,        \
           has_item,               \
           require,                \
           has_parakarry_3_letters,\
           get_starpiece_count
from rando_modules.item_scarcity import get_scarcitied_itempool

from rando_modules.unbeatable_seed_error import UnbeatableSeedError

from metadata.itemlocation_replenish import replenishing_itemlocations
from metadata.itemlocation_special     \
    import kootfavors_locations,       \
           chainletter_giver_locations,\
           dojo_locations,             \
           limited_by_item_areas,      \
           bush_tree_coin_locations
from metadata.progression_items                                 \
    import progression_miscitems as progression_miscitems_names
from metadata.item_exclusion \
    import exclude_due_to_settings, exclude_from_taycet_placement
from metadata.item_general import taycet_items
from metadata.partners_meta import all_partners as all_partners_imp


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
    return edge.get("to").get("map") + "/" + str(edge.get("to").get("id"))


def get_edge_origin_node_id(edge):
    """Returns the node_id of a given edge's origin node in string format"""
    return edge.get("from").get("map") + "/" + str(edge.get("from").get("id"))


def is_itemlocation_replenishable(item_node):
    """
    Returns True if the location described by a given node is replenishable,
    that is, the item at this location can be acquired multiple times.
    """
    node_id = get_node_identifier(item_node)
    return (node_id in replenishing_itemlocations)


def _depth_first_search(
    node_id:str,
    world_graph:dict,
    reachable_node_ids:list,
    reachable_item_nodes:dict,
    non_traversable_edges:list
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
    logging.debug(f"> DFS node {node_id}")
    found_new_pseudoitems = False

    # Node already visited? -> Return!
    node_checked_earlier = False
    if node_id in reachable_node_ids:
        if any(    outgoing_edges in non_traversable_edges
               for outgoing_edges in world_graph.get(node_id).get("edge_list")):
            node_checked_earlier = True
        else:
            return found_new_pseudoitems
    else:
        reachable_node_ids.append(node_id)
    logging.debug(f"DFS node_checked_earlier {node_checked_earlier}")

    # If the current node is an item node and thus not an entrance node,
    # add it to the list of reachable item nodes for later item placement
    is_item_node = world_graph.get(node_id).get("node").key_name_item is not None
    if is_item_node and not node_checked_earlier:
        reachable_item_nodes[node_id] = world_graph.get(node_id).get("node")

    if not node_checked_earlier:
        # Get all outgoing edges
        outgoing_edges = world_graph.get(node_id).get("edge_list")
    else:
        # Get all formerly untraversable edges
        outgoing_edges = [edge for edge in non_traversable_edges
                               if get_edge_origin_node_id(edge) == node_id]
    logging.debug(f"DFS outgoing_edges {outgoing_edges}")
    for edge in outgoing_edges:
        # Check if all requirements for edge traversal are fulfilled
        if all([r() for r in edge.get("reqs")]):
            logging.debug(f"DFS edge requirements fullfilled {edge}")
            # Add all pseudoitems provided by this edge to the inventory
            if edge.get("pseudoitems") is not None:
                add_to_inventory(edge.get("pseudoitems"))
                found_new_pseudoitems = True

            while edge in non_traversable_edges:
                logging.debug(f"DFS remove edge from non_traversable_edges {edge}")
                logging.debug(f"non_traversable_edges before {non_traversable_edges}")
                non_traversable_edges.remove(edge)
                logging.debug(f"non_traversable_edges after {non_traversable_edges}")


            # If edge requires multiuse item, remove one applicable item from
            # our inventory
            ## handled as part of simulate.require, which is very janky and
            ## should be reworked

            # DFS from newly reachable node
            edge_target_node_id = get_edge_target_node_id(edge)
            found_new_pseudoitems = (   _depth_first_search(edge_target_node_id,
                                                            world_graph,
                                                            reachable_node_ids,
                                                            reachable_item_nodes,
                                                            non_traversable_edges)
                                     or found_new_pseudoitems)
        elif edge not in non_traversable_edges:
            logging.debug(f"DFS edge requirements not fullfilled {edge}")
            non_traversable_edges.append(edge)
        else:
            logging.debug(f"DFS edge requirements not fullfilled but already in non_traversable_edges {edge}")
    return found_new_pseudoitems


def _find_new_nodes_and_edges(
    pool_misc_progression_items:list,
    pool_other_items:list,
    world_graph:dict,
    reachable_node_ids:list,
    reachable_item_nodes:dict,
    non_traversable_edges:list,
    filled_item_nodes:list
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
        logging.debug(f"non_traversable_edges_cpy before {non_traversable_edges_cpy}")

        # Re-traverse already found edges which could not be traversed before.
        node_ids_to_check = []
        for edge in non_traversable_edges:
            # Generate list of unique node_ids to check to avoid multiple
            # checks of the same node
            from_node_id = get_edge_origin_node_id(edge)
            if from_node_id not in node_ids_to_check:
                node_ids_to_check.append(from_node_id)

        logging.debug(node_ids_to_check)
        for from_node_id in node_ids_to_check:
            found_new_items = (   _depth_first_search(from_node_id,
                                                      world_graph,
                                                      reachable_node_ids,
                                                      reachable_item_nodes,
                                                      non_traversable_edges_cpy)
                               or found_new_items)
        non_traversable_edges = non_traversable_edges_cpy.copy()
        logging.debug(f"non_traversable_edges_cpy after {non_traversable_edges_cpy}")
        logging.debug(f"non_traversable_edges after {non_traversable_edges}")

        # Check if an item node is reachable which already has an item placed.
        # Since nodes are usually removed from this dict the moment an item is
        # placed there, this can only be true for node which's item is not being
        # randomized (caused by turned off shop shuffle, coin shuffle or
        # hidden panel shuffle).
        # If this is the case add item to inventory and remove node
        for node_id, item_node in reachable_item_nodes.items():
            current_item = item_node.current_item
            if current_item and get_node_identifier(item_node) not in [get_node_identifier(x) for x in filled_item_nodes]:
                current_item_name = current_item.item_name
                add_to_inventory(current_item_name)
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
                logging.debug(f"Pre-filled: {node_id}: {current_item.item_name}")
        
        # Keep searching for new edges and nodes until we don't find any new
        # items which might open up even more edges and nodes
        if not found_new_items:
            break
    logging.debug(f"non_traversable_edges after after {non_traversable_edges}")
    logging.debug("---- _find_new_nodes_and_edges end")
    return pool_misc_progression_items, pool_other_items, reachable_node_ids, reachable_item_nodes, non_traversable_edges, filled_item_nodes



def _init_mario_inventory(
    starting_partners:list,
    starting_items:list,
    partners_always_usable:bool,
    hidden_block_mode:int,
    startwith_bluehouse_open:bool,
    startwith_flowergate_open:bool,
    startwith_toybox_open:bool,
    startwith_whale_open:bool
):
    """
    Initializes Mario's starting inventory.
    This includes partners (for considering their overworld abilities during
    world graph traversal), equipment, as well as additional pseudoitems
    based on chosen settings.
    Starting equipment irrelevant to world graph traversal (such as Lucky Star,
    starting coins) is ignored.
    """
    clear_inventory()
    partner_gettable_flags = {
        "Goombario": "RF_CanGetGoombario",
        "Kooper": "RF_CanGetKooper",
        "Bombette": "RF_CanGetBombette",
        "Parakarry": "RF_CanGetParakarry",
        "Bow": "RF_CanGetBow",
        "Watt": "RF_CanGetWatt",
        "Sushie": "RF_CanGetSushie",
        "Lakilester": "RF_CanGetLakilester",
    }

    if partners_always_usable:
        for partner in partner_gettable_flags.keys():
            add_to_inventory(partner)
    else:
        add_to_inventory(starting_partners)
    for partner in [x for x in partner_gettable_flags if x not in starting_partners]:
        add_to_inventory(partner_gettable_flags.get(partner))
    if "Bow" in starting_partners:
        add_to_inventory("RF_OpenedGustyGulch")

    add_to_inventory("EQUIPMENT_Hammer_Progressive")

    for item in starting_items:
        add_to_inventory(item.item_name)

    if hidden_block_mode == 3:
        # hidden blocks always visible
        add_to_inventory("RF_HiddenBlocksVisible")

    if startwith_bluehouse_open:
        add_to_inventory("GF_MAC02_UnlockedHouse")
    if startwith_flowergate_open:
        add_to_inventory("RF_Ch6_FlowerGateOpen")
    if startwith_toybox_open:
        add_to_inventory("RF_ToyboxOpen")
    if startwith_whale_open:
        add_to_inventory("RF_CanRideWhale")


def _get_limit_items_to_dungeons(
    all_item_nodes,
    partners_always_usable:bool,
    partners_in_default_locations,
    starting_items:list,
    hidden_block_mode:int
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
        "KPA",
    ]

    additional_edges = {
        "TRD": [ 
            # Fortress Exterior Exit Bottom Left
            # -> Fortress Exterior Exit Top Left
            {
                "from": {"map": "TRD_00", "id": 0},
                "to":   {"map": "TRD_00", "id": 4},
                "reqs": [require(partner="Bombette")]
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
            area_edges.extend(additional_edges.get(area_name))
        if area_name in remove_edges:
            cleaned_area_edges = [x for x in area_edges if x not in remove_edges.get(area_name)]
            area_edges = cleaned_area_edges
        cur_area_graph = generate_world_graph(area_nodes,area_edges)
        if partners_in_default_locations and area_name in exclude_starting_partners:
            # place partners manually into their nodes, so they can be found
            # by the _find_new_nodes_and_edges call and added to inventory
            for node_id in cur_area_graph:
                if cur_area_graph.get(node_id).get("node").key_name_item == "Partner":
                    cur_area_graph[node_id]["node"].current_item = cur_area_graph[node_id]["node"].vanilla_item
                    list_index = -1
                    for filled_node in limited_filled_item_nodes:
                        if node_id == get_node_identifier(filled_node):
                            list_index = limited_filled_item_nodes.index(filled_node)
                    if list_index == -1:
                        raise ValueError
                    limited_filled_item_nodes.pop(list_index)


        # Prepare data structures
        pool_progression_items = []
        pool_misc_progression_items = []
        reachable_node_ids = []
        reachable_item_nodes = {}
        non_traversable_edges = []

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
            non_traversable_edges.append(edge)

        # Reset Mario's inventory
        if partners_in_default_locations:
            almost_all_partners = [x for x in all_partners if x != exclude_starting_partners.get(area_name)]
            _init_mario_inventory(
                almost_all_partners,
                starting_items,
                partners_always_usable,
                hidden_block_mode,
                False,
                False,
                False,
                False
            )
        else:
            _init_mario_inventory(
                all_partners,
                starting_items,
                partners_always_usable,
                hidden_block_mode,
                False,
                False,
                False,
                False
            )
        add_to_inventory([
            "CrystalBerry",
            "WaterStone"
        ])

        # Find initially reachable nodes
        pool_misc_progression_items,    \
            _,                          \
            reachable_node_ids,         \
            reachable_item_nodes,       \
            non_traversable_edges,      \
            limited_filled_item_nodes = \
            _find_new_nodes_and_edges(pool_misc_progression_items,
                                      None,
                                      cur_area_graph,
                                      reachable_node_ids,
                                      reachable_item_nodes,
                                      non_traversable_edges,
                                      limited_filled_item_nodes)

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
                cur_items_overwritten = place_progression_items(
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
                    almost_all_partners = [x for x in all_partners if x != exclude_starting_partners.get(area_name)]
                    _init_mario_inventory(
                        almost_all_partners,
                        starting_items,
                        partners_always_usable,
                        hidden_block_mode,
                        False,
                        False,
                        False,
                        False
                    )
                else:
                    _init_mario_inventory(
                        all_partners,
                        starting_items,
                        partners_always_usable,
                        hidden_block_mode,
                        False,
                        False,
                        False,
                        False
                    )

        items_placed.extend(cur_items_placed)
        items_overwritten.extend(cur_items_overwritten)

    all_item_node_ids = [get_node_identifier(node) for node in all_item_nodes]
    modified_nodes = [node for node in limited_filled_item_nodes if get_node_identifier(node) not in all_item_node_ids]

    return modified_nodes, items_placed, items_overwritten


def _generate_item_pools(
    world_graph,
    pool_progression_items:list,
    pool_misc_progression_items:list,
    pool_other_items:list,
    all_item_nodes:list,
    do_randomize_coins:bool,
    do_randomize_shops:bool,
    do_randomize_panels:bool,
    do_randomize_koopakoot:bool,
    do_randomize_letterchain:bool,
    do_randomize_dojo:bool,
    item_scarcity:int,
    startwith_bluehouse_open:bool,
    startwith_flowergate_open:bool,
    keyitems_outside_dungeon:bool,
    partners_always_usable:bool,
    partners_in_default_locations:bool,
    start_with_kooper:bool,
    start_with_bow:bool,
    always_speedyspin,
    always_ispy,
    always_peekaboo,
    hidden_block_mode:int,
    starting_partners:list,
    starting_items:list
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
        current_node = world_graph.get(node_id).get("node")
        is_item_node = current_node.key_name_item
        if is_item_node: # and current_node not in all_item_nodes:

            current_node_id = get_node_identifier(current_node)

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

            if (    current_node_id in kootfavors_locations
                and not do_randomize_koopakoot
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in chainletter_giver_locations
                and not do_randomize_letterchain
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
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item == "Partner"
                and current_node.vanilla_item.item_name in starting_partners
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

    # Pre-fill 'dungeon' nodes if keyitems are limited to there
    items_to_remove_from_pools = []
    items_to_add_to_pools = []
    pre_filled_dungeon_nodes = []
    pre_filled_node_ids = []
    if not keyitems_outside_dungeon:
        pre_filled_dungeon_nodes,\
            items_to_remove_from_pools,\
            items_to_add_to_pools = _get_limit_items_to_dungeons(
                    all_item_nodes,
                    partners_always_usable,
                    partners_in_default_locations,
                    starting_items,
                    hidden_block_mode
                )
        for node in pre_filled_dungeon_nodes:
            pre_filled_node_ids.append(get_node_identifier(node))

    # Check all remaining nodes for items to add to the pools
    for node_id in world_graph.keys():
        current_node = world_graph.get(node_id).get("node")
        is_item_node = current_node.key_name_item
        if is_item_node and current_node not in all_item_nodes:
            all_item_nodes.append(current_node)

            # Set current item to the one set during dungeon pre-fill
            if node_id in pre_filled_node_ids:
                node_index = pre_filled_node_ids.index(node_id)
                current_node.current_item = pre_filled_dungeon_nodes[node_index].current_item
                continue

            # Item shall be randomized: Add it to the correct item pool
            if (current_node.vanilla_item.progression
            or (do_randomize_shops and "StarPiece" in current_node.vanilla_item.item_name)
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

    # Adjust item pools based on settings
    goal_size_item_pool = len(pool_progression_items)      \
                        + len(pool_misc_progression_items) \
                        + len(pool_other_items)

    if startwith_bluehouse_open:
        for item_name in exclude_due_to_settings.get("startwith_bluehouse_open"):
            item = Item.get(Item.item_name == item_name)
            items_to_remove_from_pools.append(item)
    if startwith_flowergate_open:
        for item_name in exclude_due_to_settings.get("startwith_flowergate_open"):
            item = Item.get(Item.item_name == item_name)
            items_to_remove_from_pools.append(item)
    if always_speedyspin:
        for item_name in exclude_due_to_settings.get("always_speedyspin"):
            item = Item.get(Item.item_name == item_name)
            items_to_remove_from_pools.append(item)
    if always_ispy:
        for item_name in exclude_due_to_settings.get("always_ispy"):
            item = Item.get(Item.item_name == item_name)
            items_to_remove_from_pools.append(item)
    if always_peekaboo:
        for item_name in exclude_due_to_settings.get("always_peekaboo"):
            item = Item.get(Item.item_name == item_name)
            items_to_remove_from_pools.append(item)
    if start_with_kooper:
        for item_name in exclude_due_to_settings.get("start_with_kooper"):
            item = Item.get(Item.item_name == item_name)
            items_to_remove_from_pools.append(item)
    if start_with_bow:
        for item_name in exclude_due_to_settings.get("start_with_bow"):
            item = Item.get(Item.item_name == item_name)
            items_to_remove_from_pools.append(item)
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
        logging.info(f"Attempted to remove {item} from item pools, but no pool"\
                      " holds such item.")

    # If the item pool is too small now, fill it back up
    cur_size_item_pool = len(pool_progression_items)      \
                       + len(pool_misc_progression_items) \
                       + len(pool_other_items)
    while goal_size_item_pool > cur_size_item_pool:
        random_taycet_item_value = random.choice([x for x in taycet_items if x not in exclude_from_taycet_placement])
        random_taycet_item = Item.get(Item.value == random_taycet_item_value)
        pool_other_items.append(random_taycet_item)
        cur_size_item_pool = len(pool_progression_items)      \
                           + len(pool_misc_progression_items) \
                           + len(pool_other_items)

    pool_other_items = get_scarcitied_itempool(pool_other_items, item_scarcity)

    return pool_other_items


def place_progression_items(
    pool_progression_items,
    pool_misc_progression_items,
    pool_other_items,
    do_randomize_shops,
    reachable_node_ids,
    reachable_item_nodes,
    filled_item_nodes,
    non_traversable_edges,
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
            if random_node_key not in [get_node_identifier(x) for x in filled_item_nodes]:
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
        add_to_inventory(random_item.item_name)
        items_placed.append(random_item)
        items_overwritten.append(random_node.vanilla_item)
        node_identifier = get_node_identifier(random_node)
        if "Shop" in node_identifier:
            random_node.current_item.base_price = get_shop_price(random_node, do_randomize_shops)
        filled_item_nodes.append(random_node)

        # Adjust item pools if necessary: Letters
        if (has_parakarry_3_letters()
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

        if (get_starpiece_count() >= 60
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
        filled_item_nodes = \
        _find_new_nodes_and_edges(pool_misc_progression_items,
                                  pool_other_items,
                                  world_graph,
                                  reachable_node_ids,
                                  reachable_item_nodes,
                                  non_traversable_edges,
                                  filled_item_nodes)
        logging.debug(f"non_traversable_edges after _find_new_nodes_and_edges {non_traversable_edges}")
    logging.debug("non_traversable_edges after progression:")
    for edge in non_traversable_edges:
        logging.debug(edge)

    return filled_item_nodes, items_placed, items_overwritten


def _algo_forward_fill(
    item_placement,
    do_randomize_coins,
    do_randomize_shops,
    do_randomize_panels,
    do_randomize_koopakoot,
    do_randomize_letterchain,
    do_randomize_dojo,
    item_scarcity,
    starting_map_id,
    startwith_bluehouse_open,
    startwith_flowergate_open,
    startwith_toybox_open,
    startwith_whale_open,
    starting_partners,
    speedyspin,
    ispy,
    peekaboo,
    partners_always_usable,
    partners_in_default_locations,
    hidden_block_mode:int,
    keyitems_outside_dungeon:bool,
    starting_items:list,
    world_graph = None
):
    # Prepare world graph if not provided
    if world_graph is None:
        print("Generating World Graph ...")
        world_graph = generate_world_graph(None, None)

    # Declare and init additional data structures
    ## Data structures for graph traversal
    all_item_nodes = []
    reachable_node_ids = []
    reachable_item_nodes = {}
    non_traversable_edges = []
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
        do_randomize_koopakoot,
        do_randomize_letterchain,
        do_randomize_dojo,
        item_scarcity,
        startwith_bluehouse_open,
        startwith_flowergate_open,
        keyitems_outside_dungeon,
        partners_always_usable,
        partners_in_default_locations,
        ("Kooper" in starting_partners),
        ("Bow" in starting_partners),
        speedyspin,
        ispy,
        peekaboo,
        hidden_block_mode,
        starting_partners,
        starting_items
    )

    print("Initialize Mario's starting inventory...")
    _init_mario_inventory(
        starting_partners,
        starting_items,
        partners_always_usable,
        hidden_block_mode,
        startwith_bluehouse_open,
        startwith_flowergate_open,
        startwith_toybox_open,
        startwith_whale_open
    )

    # Set node to start graph traversal from
    starting_node_id = get_startingnode_id_from_startingmap_id(starting_map_id)
    print(f'Starting map: {starting_node_id}')

    # Find initially reachable nodes within the world graph
    for edge in world_graph.get(starting_node_id).get("edge_list"):
        non_traversable_edges.append(edge)
    reachable_node_ids.append(starting_node_id)
    pool_misc_progression_items, \
    pool_other_items, \
    reachable_node_ids, \
    reachable_item_nodes, \
    non_traversable_edges, \
    filled_item_nodes = \
    _find_new_nodes_and_edges(pool_misc_progression_items,
                              pool_other_items,
                              world_graph,
                              reachable_node_ids,
                              reachable_item_nodes,
                              non_traversable_edges,
                              filled_item_nodes)

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
            non_traversable_edges_try, _, _ = place_progression_items(
                pool_progression_items_try,
                pool_misc_progression_items_try,
                pool_other_items_try,
                do_randomize_shops,
                reachable_node_ids_try,
                reachable_item_nodes_try,
                filled_item_nodes_try,
                non_traversable_edges_try,
                world_graph
            )
            successfully_placed = True
            pool_other_items = pool_other_items_try.copy()
            filled_item_nodes = filled_item_nodes_try.copy()

        except IndexError:
            # Items were placed in a way that makes the seed unbeatable,
            # so we have to clear the lists and retry
            logging.info(f"Progression placement fail, retrying ...")

    # Mark all unreachable nodes, which hold pre-filled items, as filled
    for item_node in all_item_nodes:
        if item_node.current_item and item_node not in filled_item_nodes:
            filled_item_nodes.append(item_node)

    # Place all remaining items into still empty item nodes
    print("Placing Miscellaneous Items ...")
    for item_node in all_item_nodes:
        item_node_id = get_node_identifier(item_node)

        if item_node_id not in [get_node_identifier(node) for node in filled_item_nodes]:
            # Place random remaining item here
            try:
                random_item_id = random.randint(0, len(pool_other_items) - 1)
                random_item = pool_other_items.pop(random_item_id)
                item_node.current_item = random_item
                if "Shop" in item_node_id:
                    item_node.current_item.base_price = get_shop_price(item_node, do_randomize_shops)
                filled_item_nodes.append(item_node)
                logging.debug(f"{item_node_id}: {random_item.item_name}")
            except ValueError as err:
                logging.warning(f"filled_item_nodes size: {len(filled_item_nodes)}")
                logging.warning(f"pool_other_items size: {len(pool_other_items)}")
                logging.warning(f"nodes left: {len([item_node_id not in [get_node_identifier(node) for node in filled_item_nodes]])}")
                #raise
                item_node.current_item = item_node.vanilla_item
                logging.warning(f"{item_node_id}")

    if has_item("YOUWIN"):
        print("Seed verification: Beatable! Yay!")
    else:
        raise UnbeatableSeedError("Seed verification: Not beatable! Booo!")

    # "Return" list of modified item nodes
    item_placement.extend(filled_item_nodes)
    


def place_items(
    item_placement,
    algorithm,
    do_shuffle_items,
    do_randomize_coins,
    do_randomize_shops,
    do_randomize_panels,
    do_randomize_koopakoot,
    do_randomize_letterchain,
    do_randomize_dojo,
    item_scarcity,
    starting_map_id,
    startwith_bluehouse_open,
    startwith_flowergate_open,
    startwith_toybox_open,
    startwith_whale_open,
    starting_partners,
    speedyspin,
    ispy,
    peekaboo,
    partners_always_usable:bool,
    partners_in_default_locations,
    hidden_block_mode:int,
    keyitems_outside_dungeon:bool,
    starting_items:list,
    world_graph = None
):
    """Places items into item locations according to chosen settings."""
    level = logging.INFO
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    cur_seed = random.random()
    print(f"Seed: {cur_seed}")
    random.seed(cur_seed)

    if not do_shuffle_items:
        # Place items in their vanilla locations
        for node in Node.select().where(Node.key_name_item.is_null(False)):
            node.current_item = node.vanilla_item
            item_placement.append(node)

    elif algorithm == "ForwardFill":
        # Place items in accessible locations first, then expand accessible
        # locations by unlocked locations
        _algo_forward_fill(
            item_placement,
            do_randomize_coins,
            do_randomize_shops,
            do_randomize_panels,
            do_randomize_koopakoot,
            do_randomize_letterchain,
            do_randomize_dojo,
            item_scarcity,
            starting_map_id,
            startwith_bluehouse_open,
            startwith_flowergate_open,
            startwith_toybox_open,
            startwith_whale_open,
            starting_partners,
            speedyspin,
            ispy,
            peekaboo,
            partners_always_usable,
            partners_in_default_locations,
            hidden_block_mode,
            keyitems_outside_dungeon,
            starting_items,
            world_graph
        )

    yield ("Generating Log", int(100 * 1))
