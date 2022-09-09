"""
This module represents a world graph. This graph maps item locations and the
connections between them to allow simulated traversal of the in-game world.
"""
from collections import defaultdict
from copy import deepcopy

from metadata.area_name_mappings import area_name_id_map, area_name_edges_map

from db.node import Node
from db.map_area import MapArea

from maps.graph_edges.base_graph.edges_arn import edges_arn
from maps.graph_edges.base_graph.edges_dgb import edges_dgb
from maps.graph_edges.base_graph.edges_dro import edges_dro
from maps.graph_edges.base_graph.edges_flo import edges_flo
from maps.graph_edges.base_graph.edges_hos import edges_hos
from maps.graph_edges.base_graph.edges_isk import edges_isk
from maps.graph_edges.base_graph.edges_iwa import edges_iwa
from maps.graph_edges.base_graph.edges_jan import edges_jan
from maps.graph_edges.base_graph.edges_kgr import edges_kgr
from maps.graph_edges.base_graph.edges_kkj import edges_kkj
from maps.graph_edges.base_graph.edges_kmr import edges_kmr
from maps.graph_edges.base_graph.edges_kpa import edges_kpa
from maps.graph_edges.base_graph.edges_kzn import edges_kzn
from maps.graph_edges.base_graph.edges_mac import edges_mac
from maps.graph_edges.base_graph.edges_mgm import edges_mgm
from maps.graph_edges.base_graph.edges_mim import edges_mim
from maps.graph_edges.base_graph.edges_nok import edges_nok
from maps.graph_edges.base_graph.edges_obk import edges_obk
from maps.graph_edges.base_graph.edges_omo import edges_omo
from maps.graph_edges.base_graph.edges_osr import edges_osr
from maps.graph_edges.base_graph.edges_pra import edges_pra
from maps.graph_edges.base_graph.edges_sam import edges_sam
from maps.graph_edges.base_graph.edges_sbk import edges_sbk
from maps.graph_edges.base_graph.edges_tik import edges_tik
from maps.graph_edges.base_graph.edges_trd import edges_trd

from models.MarioInventory import MarioInventory

from rando_modules.logic import \
    get_edge_origin_node_id,\
    get_edge_target_node_id,\
    get_startingnode_id_from_startingmap_id


class hashabledict(dict):
    def __init__(self, d):
        super().__init__(d)
        self._hash = hash(str(self))

    def __hash__(self):
        return self._hash

def print_node_info(node):
    """Print a node's map name and its entrance_id or item key, depending on the node"""
    entrancenode_string = str(node.entrance_id) + "/" \
                        + node.entrance_name if node.entrance_id else ''
    itemnode_string = node.key_name_item + "/" \
                    + node.vanilla_item.item_name if node.key_name_item else ''
    print(f"{node.map_area.name} - {entrancenode_string}{itemnode_string}")

def get_all_nodes():
    """Returns a list of all item and entrance nodes"""
    all_nodes = []
    for node in (Node
                .select(
                    Node.map_area, Node.entrance_id, Node.entrance_type,
                    Node.entrance_name, Node.key_name_item,
                    Node.key_name_price, Node.item_source_type,
                    Node.vanilla_item, Node.current_item,
                    Node.vanilla_price, Node.item_index, Node.price_index,
                    Node.identifier
                )
                .join(MapArea)
                .order_by(MapArea.area_id, MapArea.map_id)
    ):
        all_nodes.append(node)
    return all_nodes


def get_area_nodes(area_shorthand:str):
    """Generates and returns a list of all nodes for a given ingame area."""
    area_nodes = []
    if area_shorthand in area_name_id_map:
        cur_area_id = area_name_id_map.get(area_shorthand)
        for node in (Node
                     .select(
                         Node.map_area, Node.entrance_id, Node.entrance_type,
                         Node.entrance_name, Node.key_name_item,
                         Node.key_name_price, Node.item_source_type,
                         Node.vanilla_item, Node.current_item,
                         Node.vanilla_price, Node.item_index, Node.price_index,
                         Node.identifier
                     )
                     .join(MapArea)
                     .where(MapArea.area_id == cur_area_id)):
            area_nodes.append(node)
    else:
        raise KeyError
    
    return area_nodes


def get_all_edges():
    """Returns a list of all edges"""
    all_edges = []
    all_edges.extend(edges_arn)
    all_edges.extend(edges_dgb)
    all_edges.extend(edges_dro)
    all_edges.extend(edges_flo)
    all_edges.extend(edges_hos)
    all_edges.extend(edges_isk)
    all_edges.extend(edges_iwa)
    all_edges.extend(edges_jan)
    all_edges.extend(edges_kgr)
    all_edges.extend(edges_kkj)
    all_edges.extend(edges_kmr)
    all_edges.extend(edges_kpa)
    all_edges.extend(edges_kzn)
    all_edges.extend(edges_mac)
    all_edges.extend(edges_mgm)
    all_edges.extend(edges_mim)
    all_edges.extend(edges_nok)
    all_edges.extend(edges_obk)
    all_edges.extend(edges_omo)
    all_edges.extend(edges_osr)
    all_edges.extend(edges_pra)
    all_edges.extend(edges_sam)
    all_edges.extend(edges_sbk)
    all_edges.extend(edges_tik)
    all_edges.extend(edges_trd)

    hashabledicts = []
    for d in all_edges:
        d["mapchange"] = d["from"]["map"] != d["to"]["map"]
        hashabledicts.append(hashabledict(d))

    return hashabledicts


def get_area_edges(area_shorthand:str):
    """Returns a list of all edges which are part of a given ingame area."""
    area_edges = []
    if area_shorthand in area_name_edges_map:
        area_edges.extend(area_name_edges_map.get(area_shorthand))
    else:
        raise KeyError

    hashabledicts = []
    for d in area_edges:
        d["mapchange"] = d["from"]["map"] != d["to"]["map"]
        hashabledicts.append(hashabledict(d))

    return hashabledicts


def generate(node_list, edge_list):
    """
    Generates and returns a world graph dictionary with nodes' node_ids in string form as keys and
    a list of neighboring nodes' node_ids in string form as values.
    """
    if not node_list or len(node_list) == 0:
        node_list = get_all_nodes()
    if not edge_list or len(edge_list) == 0:
        edge_list = get_all_edges()
    world_graph = {}

    for node in node_list:
        world_graph[node.identifier] = {}
        world_graph[node.identifier]["node"] = node
        world_graph[node.identifier]["edge_list"] = []

        edge_list_cpy = edge_list.copy()
        for edge in edge_list:
            if edge.get("from").get("map") == node.map_area.name:
                if edge.get("to").get("map") is None:
                    # This edge exists for completeness' sake only and has no use inside the graph
                    pass
                elif (   edge.get("from").get("id") == node.entrance_id
                      or edge.get("from").get("id") == node.key_name_item):
                    world_graph[node.identifier]["edge_list"].append(edge)
                    if not node.map_area.name.startswith("PRA_02"):
                        edge_list_cpy.remove(edge)
        edge_list = edge_list_cpy

    return world_graph


def adjust(world_graph, new_edges=None, edges_to_remove=None):
    """
    Adjusts and returns a modified world graph depending on given edge list
    parameters.
    """
    if new_edges is None:
        new_edges = []
    if edges_to_remove is None:
        edges_to_remove = []

    edge_adjustments = {}
    db_data = []
    db_data_dict = {}

    # Add new edges to graph nodes
    for new_edge in [hashabledict(x) for x in new_edges]:
        origin_map_name = new_edge["from"]["map"]
        origin_entrance_id = new_edge["from"]["id"]
        destination_map_name = new_edge["to"]["map"]
        destination_entrance_id = new_edge["to"]["id"]

        node_id = f"{origin_map_name}/{origin_entrance_id}"
        if node_id not in edge_adjustments:
            edge_adjustments[node_id] = []
        edge_adjustments[node_id].append(new_edge)

        # Map changes are implicitly True unless specified otherwise
        is_mapchange = new_edge.get("mapchange")
        if is_mapchange is None:
            is_mapchange = True

        # If the edge symbolizes a map change, gather ROM db data to write
        if (isinstance(origin_entrance_id, int)
        and isinstance(destination_entrance_id, int)
        and is_mapchange
        ):
            for old_edge in world_graph[node_id]["edge_list"]:
                if (
                    old_edge["from"]["map"] == origin_map_name
                and old_edge["from"]["id"]  == origin_entrance_id
                ):
                    old_target_map_info = old_edge["to"]
                    break
            old_target_map_data = (
                MapArea.select(MapArea.area_id,
                               MapArea.map_id,
                               Node.entrance_id)
                       .join(Node)
                       .where(MapArea.name == old_target_map_info["map"])
                       .where(Node.entrance_id == old_target_map_info["id"])
                       .objects()
                       .get()
            )
            db_key = (0xA3 << 24) \
                   | (old_target_map_data.area_id << 16) \
                   | (old_target_map_data.map_id  <<  8) \
                   |  old_target_map_data.entrance_id

            new_target_map_data = (
                MapArea.select(MapArea.area_id,
                               MapArea.map_id,
                               Node.entrance_id)
                       .join(Node)
                       .where(MapArea.name == destination_map_name)
                       .where(Node.entrance_id == destination_entrance_id)
                       .objects()
                       .get()
            )
            db_value = (new_target_map_data.area_id << 16) \
                     | (new_target_map_data.map_id  <<  8) \
                     |  new_target_map_data.entrance_id

            db_data_dict[db_key]= db_value

    # Remove old edges from graph nodes
    for old_edge in [hashabledict(x) for x in edges_to_remove]:
        node_id = f"{old_edge['from']['map']}/{old_edge['from']['id']}"
        stripped_edge_list = world_graph[node_id]["edge_list"]
        for i, strip_edge in enumerate(stripped_edge_list):
            if (
                strip_edge["from"] == old_edge["from"]
            and strip_edge["to"] == old_edge["to"]
            ):
                stripped_edge_list.pop(i)
                break
        world_graph[node_id]["edge_list"] = stripped_edge_list

    # Add new edges to graph nodes
    for node_id, adjustment_list in edge_adjustments.items():
        world_graph[node_id]["edge_list"].extend(adjustment_list)

    # Prepare tuples for entrance rando db-entries
    for dbkey, dbvalue in db_data_dict.items():
        db_data.append((dbkey, dbvalue))

    return world_graph, db_data


def recalculate_multikeys(world_graph:dict, starting_map_id:int):
    """
    Given a starting map id within the given world graph, recalculate the keys
    required for each path blocked by a varying amount of the same key type
    ("multikeys").
    Does not recalculate required star spirits or star pieces.
    """
    # Check if the starting node is actually part of the world graph
    node_identifier = get_startingnode_id_from_startingmap_id(starting_map_id)

    if not node_identifier in world_graph:
        raise ValueError(
            "Provided node is not part of the provided world graph",
            node_identifier
        )

    # Prepare datastructures and functions for world graph traversal
    keys_required = {}
    inventory = MarioInventory(
        starting_boots=2,
        starting_hammer=2,
        partners_always_usable=True,
        hidden_block_mode=2,
        startwith_bluehouse_open=True,
        magical_seeds_required=0,
        startwith_toybox_open=True,
        startwith_whale_open=True,
        startwith_speedyspin=True
    )

    def _depth_first_search(
        node_id:str,
        world_graph:dict,
        reachable_node_ids:set,
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

        if not node_checked_earlier:
            # Get all outgoing edges
            outgoing_edges = world_graph[node_id]["edge_list"]
        else:
            # Get all formerly untraversable edges
            outgoing_edges = non_traversable_edges.pop(node_id)

        for edge in outgoing_edges:
            # Check if all requirements for edge traversal are fulfilled
            if mario.requirements_fulfilled(edge.get("reqs")):
                # Add all pseudoitems provided by this edge to the inventory
                if edge.get("pseudoitems") is not None:
                    mario.add(edge.get("pseudoitems"))
                    found_new_pseudoitems = True

                while edge in non_traversable_edges[node_id]:
                    non_traversable_edges[node_id].remove(edge)

                # DFS from newly reachable node
                edge_target_node_id = get_edge_target_node_id(edge)
                found_additional_pseudoitems, mario = _depth_first_search(
                    edge_target_node_id,
                    world_graph,
                    reachable_node_ids,
                    non_traversable_edges,
                    mario
                )
                found_new_pseudoitems = found_new_pseudoitems or found_additional_pseudoitems
            else:
                non_traversable_edges[node_id].add(edge)
        return found_new_pseudoitems, mario

    def _find_new_nodes_and_edges(
        world_graph:dict,
        reachable_node_ids:set,
        non_traversable_edges:defaultdict, #(set)
        local_inventory:MarioInventory
    ):
        """
        Try to traverse already found edges which could not be traversed before.
        This re-traversing is accomplished by calling DFS on each respective edge's
        origin node ("from-node").
        """
        while True:
            found_new_items = False

            # We require a copy here since we cannot iterate over a list and
            # at the same time possibly delete entries from it (see DFS)
            non_traversable_edges_cpy = non_traversable_edges.copy()

            # Re-traverse already found edges which could not be traversed before.
            node_ids_to_check = []
            for edges in non_traversable_edges.values():
                for edge in edges:
                    # Generate list of unique node_ids to check to avoid multiple
                    # checks of the same node
                    from_node_id = get_edge_origin_node_id(edge)
                    if from_node_id not in node_ids_to_check:
                        node_ids_to_check.append(from_node_id)

            for from_node_id in node_ids_to_check:
                found_additional_items, local_inventory = _depth_first_search(
                    from_node_id,
                    world_graph,
                    reachable_node_ids,
                    non_traversable_edges_cpy,
                    local_inventory
                )
                found_new_items = found_new_items or found_additional_items
            non_traversable_edges = non_traversable_edges_cpy.copy()

            # Keep searching for new edges and nodes until we don't find any new
            # items which might open up even more edges and nodes
            if not found_new_items:
                break
        return reachable_node_ids, non_traversable_edges, local_inventory

    # Add all items to the inventory except for the multikeys
    key_list = ["KoopaFortress","Ruins","TubbaCastle","BowserCastle"]
    for key in key_list:
        keys_required[f"{key}Key"] = 0
    for node_id in world_graph.keys():
        node = world_graph[node_id]["node"]
        if node.vanilla_item:
            item = node.vanilla_item.item_name
            if not any(item.startswith(x) for x in key_list):
                inventory.add(item)

    # Search graph without keys
    reachable_node_ids = set()
    reachable_node_ids.add(node_identifier)
    non_traversable_edges = defaultdict(set)
    non_traversable_edges[node_identifier] = set()
    for edge in world_graph.get(node_identifier).get("edge_list"):
        non_traversable_edges[node_identifier].add(edge)

    original_edges = []
    modified_edges = []
    while non_traversable_edges:
        current_key_edges = []

        reachable_node_ids, non_traversable_edges, inventory = \
        _find_new_nodes_and_edges(
            world_graph,
            reachable_node_ids,
            non_traversable_edges,
            inventory
        )

        # Check if we were blocked by one of the missing keys and note that down
        for node, edge_set in non_traversable_edges.items():
            for edge in edge_set:
                found_key = False
                for req_group in edge["reqs"]:
                    for req in req_group:
                        if isinstance(req, dict):
                            for key in req.keys():
                                if any(key.startswith(x) for x in key_list):
                                    keys_required[key] += 1
                                    found_key = True
                if found_key:
                    original_edges.append(edge)
                    current_key_edges.append(edge)

        # Add multikeys to inventory depending on number of encountered blockers
        for key, count in keys_required.items():
            inventory.add([f"{key}{x}" for x in range(1, count + 1)])
            # Search encountered multikey edges and add them (modified to hold
            # the newly calculated key count) to a new list
            for cur_edge in current_key_edges:
                for org_edge in original_edges:
                    if cur_edge == org_edge:
                        for i, cur_req_grp in enumerate(cur_edge["reqs"]):
                            for j, cur_req in enumerate(cur_req_grp):
                                if isinstance(cur_req, dict) and cur_req.get(key) is not None:
                                    mod_edge = deepcopy(cur_edge)
                                    mod_edge["reqs"][i][j][key] = count
                                    modified_edges.append(mod_edge)

        # Some clean-up of the non_traversable_edges dict
        remove_edges = []
        for key, value in non_traversable_edges.items():
            # Clear out empty data
            if not value:
                remove_edges.append(key)
            # Clear out edges that can never be traversed
            elif all([any(y in [['RF_Missable'], ['RF_OutOfLogic']] for y in x["reqs"]) for x in value]):
                remove_edges.append(key)
        for edge in remove_edges:
            non_traversable_edges.pop(edge)

    # Remove unneeded edge data
    for entry in original_edges:
        if entry.get("origin_node_id") is not None:
            entry.pop("origin_node_id")
        if entry.get("target_node_id") is not None:
            entry.pop("target_node_id")
    for entry in modified_edges:
        if entry.get("origin_node_id") is not None:
            entry.pop("origin_node_id")
        if entry.get("target_node_id") is not None:
            entry.pop("target_node_id")

    # Remove un-changing edges from sets
    remove_edges = []
    for entry in original_edges:
        if entry in modified_edges:
            remove_edges.append(entry)
    for entry in remove_edges:
        original_edges.remove(entry)
        modified_edges.remove(entry)

    # Adjust graph if needed
    if original_edges or modified_edges:
        world_graph, _ = adjust(
            world_graph,
            new_edges=modified_edges,
            edges_to_remove=original_edges
        )

    return world_graph


def check_graph():
    """
    Generate world graph from default entrance links and edges, then run a few validation checks
    """
    print("Loading world graph nodes and edges ...")

    all_nodes = get_all_nodes()
    print(str(len(all_nodes)) + " nodes loaded.")

    all_edges = get_all_edges()
    print(str(len(all_edges)) + " edges loaded.")
    print()

    # Check for nodes without atleast one outbound edge
    check_unleavable_nodes(all_nodes, all_edges)

    # Check if nodes exist that are unreachable (not targets of any edges)
    check_unreachable_nodes(all_nodes, all_edges)

    # Check if edges exist that reference non-existing nodes
    check_nullnode_reference(all_nodes, all_edges)

    # Check if theres any nodes unreachable from KMR_20/4 (Mario's House Green Pipe)
    print("Generating world graph from nodes and edges ...")
    graph = generate(all_nodes, all_edges)
    check_unreachable_from_start(graph, True)

    print("Done.")


def check_unleavable_nodes(all_nodes, all_edges):
    """Check for nodes without atleast one outbound edge."""
    print("Check for nodes without atleast one outbound edge ...")
    unleavable_nodes = []

    for node in all_nodes:
        leaving_edge_found = False
        for edge in all_edges:
            if edge.get("from").get("map") == node.map_area.name:
                if (   edge.get("from").get("id") == node.entrance_id
                    or edge.get("from").get("id") == node.key_name_item):
                    if edge.get("to").get("map") is not None:
                        leaving_edge_found = True
                        break
        if not leaving_edge_found:
            unleavable_nodes.append(node)

    if len(unleavable_nodes) == 0:
        print("No unleavable nodes found.")
    else:
        print(str(len(unleavable_nodes)) + " unleavable nodes found:")
        for node in unleavable_nodes:
            print_node_info(node)

    print()


def check_unreachable_nodes(all_nodes, all_edges):
    """Check if nodes exist that are unreachable (not targets of any edges)"""
    print("Check for unreachable nodes ...")
    unreachable_nodes = []

    for node in all_nodes:
        edge_target_found = False
        for edge in all_edges:
            if edge.get("to").get("map") == node.map_area.name:
                if (   edge.get("to").get("id") == node.entrance_id
                    or edge.get("to").get("id") == node.key_name_item):
                    edge_target_found = True
                    break
        if not edge_target_found:
            unreachable_nodes.append(node)

    if len(unreachable_nodes) == 0:
        print("No unreachable nodes found.")
    else:
        print(str(len(unreachable_nodes)) + " unreachable nodes found:")
        for node in unreachable_nodes:
            print_node_info(node)

    print()


def check_nullnode_reference(all_nodes, all_edges):
    """Check if edges exist that reference non-existing nodes"""
    print("Check for edges that reference non-existing nodes ...")
    invalid_origin_edges = []
    invalid_target_edges = []

    for edge in all_edges:
        edge_origin_found = False
        edge_target_found = False
        for node in all_nodes:
            if edge.get("from").get("map") == node.map_area.name:
                if (   edge.get("from").get("id") == node.entrance_id
                    or edge.get("from").get("id") == node.key_name_item):
                    edge_origin_found = True
                    if edge_origin_found and edge_target_found:
                        break
            if edge.get("to").get("map") == node.map_area.name:
                if (   edge.get("to").get("id") == node.entrance_id
                    or edge.get("to").get("id") == node.key_name_item):
                    edge_target_found = True
                    if edge_origin_found and edge_target_found:
                        break
        if not edge_origin_found:
            invalid_origin_edges.append(edge)
        if not edge_target_found:
            invalid_target_edges.append(edge)

    if len(invalid_origin_edges) == 0:
        print("No edges with non-existing origin nodes found.")
    else:
        print(str(len(invalid_origin_edges)) + " edges with invalid origin nodes found:")
        for edge in invalid_origin_edges:
            print(edge)

    print()

    if len(invalid_target_edges) == 0:
        print("No edges with non-existing target nodes found.")
    else:
        print(str(len(invalid_target_edges)) + " edges with invalid target nodes found:")
        for edge in invalid_target_edges:
            print(edge)

    print()


def check_unreachable_from_start(world_graph:dict, do_print:bool) -> list:
    """Check if theres any nodes unreachable from KMR_20/4 (Mario's House Green Pipe)"""
    # build world graph
    if do_print:
        print("Check if theres any nodes unreachable from KMR_20/4 (Mario's House Green Pipe) ...")

    # prepare datastructures for world graph traversal
    visited_node_ids = []

    def depth_first_search(node_id):
        if node_id in visited_node_ids:
            return
        visited_node_ids.append(node_id)

        try:
            outgoing_edges = world_graph.get(node_id).get("edge_list")
            for edge in outgoing_edges:
                depth_first_search(edge.get("to").get("map") + "/" + str(edge.get("to").get("id")))
        except AttributeError as err:
            if do_print:
                print(f"{err.args}: Cannot find edges of {node_id}!")
            raise

    # traverse world graph
    if do_print:
        print("Checking node reachability in world graph ...")
    depth_first_search("KMR_20/4")

    not_visited_node_ids = [id for id in world_graph.keys() if id not in visited_node_ids]

    if do_print:
        if len(not_visited_node_ids) == 0:
            print("No unreachable nodes from KMR_20/4 found.")
        else:
            print(str(len(not_visited_node_ids)) + " unreachable nodes:")
            for node_id in not_visited_node_ids:
                print(node_id)

    return not_visited_node_ids


if __name__ == "__main__":
    check_graph()
