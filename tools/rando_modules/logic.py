"""
This modules offers the randomization logic and takes care of actually randomizing
the game according to the settings chosen.
"""
import random
import logging
import json

from db.node import Node
from db.item import Item
from db.map_area import MapArea
from worldgraph import generate as generate_world_graph, get_node_identifier
from rando_modules.simulate import add_to_inventory, clear_inventory, has_item
from custom_seed import validate_seed

from metadata.itemlocation_replenish import replenishing_itemlocations
from metadata.progression_items import progression_miscitems as progression_miscitems_names


def get_startingnode_id_from_startingmap_id(starting_map_id):
    """Returns the starting node id (e.g. "MAC_00/4") for a given map id."""
    # Extract entrance, map and area from map-hex
    starting_map_hex = hex(starting_map_id)[2:]
    starting_map_entrance_id = starting_map_hex[-1:]
    starting_map_map_id = starting_map_hex[-4:-2] if starting_map_hex[-4:-2] != "" else 0
    starting_map_area_id = starting_map_hex[-6:-4] if starting_map_hex[-6:-4] != "" else 0

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


def _algo_custom_seed(item_placement):
    """
    Places items into item_placement dict according to provided custom_seed
    file.
    """
    try:
        #TODO: seed_path as function argument
        seed_path = "./custom_seed.json"
        is_valid = validate_seed(seed_path)
        if is_valid:
            with open(seed_path, "r", encoding="utf-8") as custom_seed_file:
                custom_items = json.load(custom_seed_file)
        #TODO: handle invalid seed: GUI message?
    except FileNotFoundError as err:
        print(f"{err.args}: Custom Seed file \'{seed_path}\' cannot be read.")
        raise

    for node in Node.select().where(Node.key_name_item.is_null(False)):
        new_item = Item.get(Item.item_name == \
                            custom_items.get(node.map_area.name).get(node.key_name_item))
        node.current_item = new_item
        item_placement.append(node)


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
            if current_item and item_node not in filled_item_nodes:
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
                    #print(f"Considered item placed: {node_id}: {current_item}")

                filled_item_nodes.append(item_node)
                #print(f"Unrandom: {node_id}: {current_item.item_name}")
        
        # Keep searching for new edges and nodes until we don't find any new
        # items which might open up even more edges and nodes
        if not found_new_items:
            break
    logging.debug(f"non_traversable_edges after after {non_traversable_edges}")
    logging.debug("---- _find_new_nodes_and_edges end")
    return pool_misc_progression_items, reachable_node_ids, reachable_item_nodes, non_traversable_edges, filled_item_nodes



def _init_mario_inventory(
    starting_partners,
    startwith_bluehouse_open,
    startwith_flowergate_open
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
    add_to_inventory(["PARTNER_Goombario","PARTNER_Kooper","PARTNER_Bombette",
                      "PARTNER_Parakarry","PARTNER_Bow","PARTNER_Watt",
                      "PARTNER_Sushie","PARTNER_Lakilester"])
    # add_to_inventory(starting_partners) # the above are logic partners (abilities)
    add_to_inventory("EQUIPMENT_Hammer_Progressive")

    if startwith_bluehouse_open:
        add_to_inventory("GF_MAC02_UnlockedHouse")
    if startwith_flowergate_open:
        add_to_inventory("RF_Ch6_FlowerGateOpen")


def _generate_item_pools(
    world_graph,
    pool_progression_items,
    pool_misc_progression_items,
    pool_other_items,
    all_item_nodes,
    do_randomize_coins,
    do_randomize_shops,
    do_randomize_panels,
):
    """
    Generates item pools for items to be shuffled (depending on chosen
    settings this may exclude certain items). The item pools generated are
    pool_progression_items (keyitems that influence progression),
    pool_misc_progression_items (non-keyitems that influence progression) and
    pool_other_items (every other item). Additionally marks item nodes that
    shall not be randomized as already filled.
    """
    for node_id in world_graph.keys():
        is_item_node = world_graph.get(node_id).get("node").key_name_item
        if is_item_node:
            current_node = world_graph.get(node_id).get("node")
            all_item_nodes.append(current_node)

            # Check the randomization settings. If something is not supposed
            # to be randomized, mark location as filled by setting its
            # current_item value
            if (    current_node.vanilla_item.item_name == "Coin"
                and not do_randomize_coins
            ):
                current_node.current_item = current_node.vanilla_item
                continue

            if (    current_node.key_name_item.startswith("Shop")
                and not do_randomize_shops
            ):
                current_node.current_item = current_node.vanilla_item
                continue

            if (    current_node.key_name_item == "HiddenPanel"
                and not do_randomize_panels
            ):
                current_node.current_item = current_node.vanilla_item
                continue

            # Item shall be randomized: Add it to the correct item pool
            if current_node.vanilla_item.progression:
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


def _algo_forward_fill(
    item_placement,
    do_randomize_coins,
    do_randomize_shops,
    do_randomize_panels,
    starting_map_id,
    startwith_bluehouse_open,
    startwith_flowergate_open,
    starting_partners
):
    print("Initialize Mario's starting inventory...")
    _init_mario_inventory(
        starting_partners, startwith_bluehouse_open, startwith_flowergate_open
    )

    # Prepare world graph
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
    _generate_item_pools(world_graph,
                         pool_progression_items,
                         pool_misc_progression_items,
                         pool_other_items,
                         all_item_nodes,
                         do_randomize_coins,
                         do_randomize_shops,
                         do_randomize_panels)
    #print(f"Size pool_progression_items: {len(pool_progression_items)}")
    #print(f"Size pool_misc_progression_items: {len(pool_misc_progression_items)}")
    #print(f"Size pool_other_items: {len(pool_other_items)}")

    # Set node to start graph traversal from
    starting_node_id = get_startingnode_id_from_startingmap_id(starting_map_id)
    print(f'Starting map: {starting_node_id}')

    # Find initially reachable nodes within the world graph
    for edge in world_graph.get(starting_node_id).get("edge_list"):
        non_traversable_edges.append(edge)
    reachable_node_ids.append(starting_node_id)
    pool_misc_progression_items, \
    reachable_node_ids, \
    reachable_item_nodes, \
    non_traversable_edges, \
    filled_item_nodes = \
    _find_new_nodes_and_edges(pool_misc_progression_items,
                              world_graph,
                              reachable_node_ids,
                              reachable_item_nodes,
                              non_traversable_edges,
                              filled_item_nodes)

    # Place items influencing progression, giving misc. items priority for
    # repleneshing item locations
    print("Placing Progression Items ...")
    while pool_progression_items or pool_misc_progression_items:

        # Pick random reachable item node
        while True:
            random_node_key = random.choice(list(reachable_item_nodes.keys()))
            random_node = reachable_item_nodes.pop(random_node_key)
            if random_node not in filled_item_nodes:
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
        filled_item_nodes.append(random_node)
        print(f"{get_node_identifier(random_node)}: {random_item.item_name}")

        #print(f"{get_node_identifier(random_node)}: {random_item.item_name}")

        pool_misc_progression_items, \
        reachable_node_ids, \
        reachable_item_nodes, \
        non_traversable_edges, \
        filled_item_nodes = \
        _find_new_nodes_and_edges(pool_misc_progression_items,
                                  world_graph,
                                  reachable_node_ids,
                                  reachable_item_nodes,
                                  non_traversable_edges,
                                  filled_item_nodes)
        logging.debug(f"non_traversable_edges after _find_new_nodes_and_edges {non_traversable_edges}")
    logging.debug("non_traversable_edges after progression:")
    for edge in non_traversable_edges:
        logging.debug(edge)

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
                filled_item_nodes.append(item_node)
                print(f"{get_node_identifier(item_node)}: {random_item.item_name}")
            except ValueError as err:
                print(f"filled_item_nodes size: {len(filled_item_nodes)}")
                print(f"pool_other_items size: {len(pool_other_items)}")
                print(f"nodes left: {len([item_node_id not in [get_node_identifier(node) for node in filled_item_nodes]])}")
                #raise
                item_node.current_item = item_node.vanilla_item
                print(f"{item_node_id}")

    if has_item("YOUWIN"):
        print("Beatable! Yay!")
    else:
        print("Not beatable! Booo!")

    # "Return" list of modified item nodes
    item_placement.extend(filled_item_nodes)
    


def place_items(item_placement, algorithm, do_shuffle_items, do_randomize_coins,
  do_randomize_shops, do_randomize_panels, starting_map_id,
  startwith_bluehouse_open, startwith_flowergate_open, starting_partners=None
):
    """Places items into item locations according to chosen settings."""

    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    if algorithm == "CustomSeed":
        # Place items according to custom seed
        _algo_custom_seed(item_placement)

    elif not do_shuffle_items:
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
            starting_map_id,
            startwith_bluehouse_open,
            startwith_flowergate_open,
            starting_partners
        )

    yield ("Generating Log", int(100 * 1))
