import random
import sqlite3
import json

from db.node import Node
from db.item import Item
from db.map_area import MapArea
from db.option import Option
from worldgraph import generate as generate_world_graph, get_node_identifier
from simulate import Mario, add_to_inventory
from custom_seed import validate_seed


def remove_items_from_randomization(item_types, world_graph, filled_item_nodes, pool_other_items):
    # Mark vanilla item nodes as filled
    items_to_remove = {}
    for key in world_graph.keys():
        node = world_graph.get(key).get("node")
        if (    node.key_name_item is not None
            and (   ("Shops" in item_types and node.key_name_item.startswith("ShopItem"))
                 or ("Coins" in item_types and node.vanilla_item.item_name == "Coin")
                 or ("Panels" in item_types and node.key_name_item == "HiddenPanel"))):
            filled_item_nodes.append(node)
            if items_to_remove.get(node.vanilla_item.item_name) is None:
                items_to_remove[node.vanilla_item.item_name] = 1
            else:
                items_to_remove[node.vanilla_item.item_name] = items_to_remove.get(node.vanilla_item.item_name) + 1
    # Remove items from item pool
    i = 0
    while i < len(pool_other_items):
        cur_item = pool_other_items[i].item_name
        if items_to_remove.get(cur_item) is not None and items_to_remove.get(cur_item) > 0:
            pool_other_items.pop(i)
            items_to_remove[cur_item] = items_to_remove[cur_item] - 1
        else:
            i += 1


def place_items(app, isShuffle, algorithm, item_placement):
    """Places items into item locations according to chosen settings."""

    do_custom_seed = False #NYI
    do_shuffle_items = Option.get(Option.name == "ShuffleItems").value

    if do_custom_seed:
        # Place items according to custom seed
        try:
            seed_path = "./custom_seed.json"
            is_valid = validate_seed(seed_path)
            if is_valid:
                with open(seed_path, "r") as custom_seed_file:
                    custom_items = json.load(custom_seed_file)
            #TODO: handle invalid seed: GUI message?
        except FileNotFoundError as err:
            print(f"{err.args}: Custom Seed file \'{seed_path}\' cannot be read.")
            raise

        for node in Node.select().where(Node.key_name_item.is_null(False)):
            new_item = Item.get(Item.item_name == custom_items.get(node.map_area.name).get(node.key_name_item))
            node.current_item = new_item
            item_placement.append(node)

    elif not do_shuffle_items:
        # Place items in their vanilla locations
        for node in Node.select().where(Node.key_name_item.is_null(False)):
            node.current_item = node.vanilla_item
            item_placement.append(node)

    elif algorithm == "forward_fill":
        # Place items in accessible locations first, then expand accessible locations by unlocked locations
        
        # Prepare Mario's starting inventory
        mario = Mario()
        add_to_inventory(["PARTNER_Goombario","PARTNER_Kooper","PARTNER_Bombette","PARTNER_Parakarry",
                          "PARTNER_Bow","PARTNER_Watt","PARTNER_Sushie","PARTNER_Lakilester"])
        add_to_inventory("EQUIPMENT_Hammer_Progressive")

        startwith_bluehouse_open = Option.get(Option.name == "BlueHouseOpen").value
        if startwith_bluehouse_open:
            add_to_inventory("GF_MAC02_UnlockedHouse")
            #TODO maybe remove OddKey from itempool?
        startwith_flowergate_open = Option.get(Option.name == "FlowerGateOpen").value
        if startwith_flowergate_open:
            add_to_inventory("RF_Ch6_FlowerGateOpen")
            #TODO maybe remove MagicalSeeds from itempool?

        # Prepare world graph
        print("Generating World Graph ...")
        world_graph = generate_world_graph()

        # Prepare datastructures
        reachable_nodes = []
        reachable_item_nodes = {}
        non_traversable_edges = []
        filled_item_nodes = []

        def depth_first_search(node_id):
            if node_id in reachable_nodes:
                return
            reachable_nodes.append(node_id)
            if world_graph.get(node_id).get("node").key_name_item is not None:
                reachable_item_nodes[node_id] = world_graph.get(node_id).get("node")

            outgoing_edges = world_graph.get(node_id).get("edge_list")
            for edge in outgoing_edges:
                try:
                    if all([r() for r in edge.get("reqs")]):
                        if edge.get("pseudoitems") is not None:
                            pseudoitem_acquired = add_to_inventory(edge.get("pseudoitems"))
                        depth_first_search(edge.get("to").get("map") + "/" + str(edge.get("to").get("id")))
                    elif edge not in non_traversable_edges:
                        non_traversable_edges.append(edge)
                except TypeError as err:
                    print(f"{err.args}: {edge}")
                    raise

        # Generate item pools
        print("Generating Item Pool ...")
        pool_progression_items = []
        pool_other_items = []
        all_item_nodes = []

        for node_id in world_graph.keys():
            if world_graph.get(node_id).get("node").key_name_item:
                cur_node = world_graph.get(node_id).get("node")
                all_item_nodes.append(cur_node)
                if cur_node.vanilla_item.progression:
                    pool_progression_items.append(cur_node.vanilla_item)
                else:
                    pool_other_items.append(cur_node.vanilla_item)
        
        # Check if items and nodes need to be excluded from randomization based on settings
        dont_randomize = []
        # Randomize coins?
        do_randomize_coins = Option.get(Option.name == "IncludeCoins").value
        if not do_randomize_coins:
            dont_randomize.append("Coins")
        # Randomize shops?
        do_randomize_shops = Option.get(Option.name == "IncludeShops").value
        if not do_randomize_shops:
            dont_randomize.append("Shops")
        # Randomize hidden panels?
        do_randomize_panels = Option.get(Option.name == "IncludePanels").value
        if not do_randomize_panels:
            dont_randomize.append("Panels")

        if len(dont_randomize) > 0:
            remove_items_from_randomization(dont_randomize, world_graph, filled_item_nodes, pool_other_items)
        
        # Set node to start graph traversal from
        starting_map_hex = hex(Option.get(Option.name == "StartingMap").value)[2:]
        starting_map_entrance_id = starting_map_hex[-1:]
        starting_map_map_id = starting_map_hex[-4:-2] if starting_map_hex[-4:-2] != "" else 0
        starting_map_area_id = starting_map_hex[-6:-4] if starting_map_hex[-6:-4] != "" else 0

        starting_maparea = MapArea.get(  (MapArea.area_id == starting_map_area_id)
                                       & (MapArea.map_id  == starting_map_map_id))

        starting_node_id = starting_maparea.name + "/" + str(starting_map_entrance_id)
        
        # Find initially reachable nodes
        print("Placing Progression Items ...")
        reachable_nodes = []
        reachable_item_nodes = {}

        def find_reachable_nodes(non_traversable_edges):
            # Check for newly available nodes and add those to reachable_nodes
            while True:
                pseudoitem_acquired = False
                non_traversable_edges_tmp = non_traversable_edges.copy()
                non_traversable_edges.clear()
                for non_traversable_edge in non_traversable_edges_tmp:
                    from_node_id = (  non_traversable_edge.get("from").get("map")
                                    + "/" 
                                    + str(non_traversable_edge.get("from").get("id")))
                    # remove edge's from-node from reachable_nodes, or else DFS won't do anything
                    i = 0
                    while i < len(reachable_nodes):
                        cur_node_id = reachable_nodes[i]
                        if cur_node_id == from_node_id:
                            reachable_nodes.pop(i)
                            break
                        else:
                            i += 1
                    # DFS from edge's from-node
                    depth_first_search(from_node_id)
                # If we find atleast one pseudo-item (partner, upgrade, flag, koopa koot favor), then
                # we have to check for reachable_nodes repeatedly until no new pseudoitems are found
                if not pseudoitem_acquired:
                    break

        depth_first_search(starting_node_id)
        find_reachable_nodes(non_traversable_edges)

        # Place all items that influence progression and re-traverse formerly locked parts of the graph
        while len(pool_progression_items) > 0:

            # Pick random progression_item and place it into random reachable and unfilled item node
            while True:
                random_node = reachable_item_nodes.pop(random.choice(list(reachable_item_nodes.keys())))
                if random_node not in filled_item_nodes:
                    break
            random_item = pool_progression_items.pop(random.randint(0, len(pool_progression_items) - 1))
            random_node.current_item = random_item
            filled_item_nodes.append(random_node)

            # Add placed progression_item into mario's inventory
            add_to_inventory(random_item.item_name)

            find_reachable_nodes(non_traversable_edges)
        
        # Place all remaining items
        print("Placing Miscellaneous Items ...")
        for item_node in all_item_nodes:
            item_node_id = get_node_identifier(item_node)

            if item_node_id not in [get_node_identifier(node) for node in filled_item_nodes]:
                print(item_node_id)
                random_item = pool_other_items.pop(random.randint(0, len(pool_other_items) - 1))
                item_node.current_item = random_item
                filled_item_nodes.append(item_node)

        item_placement.extend(filled_item_nodes)

    elif algorithm == "assumed_fill":
        # Start with all items in inventory, remove an item and try to place it at a reachable location
        None # NYI # TODO

    yield ("Generating Log", int(100 * 1))
