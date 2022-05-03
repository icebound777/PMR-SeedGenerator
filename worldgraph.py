"""
This module represents a world graph. This graph maps item locations and the
connections between them to allow simulated traversal of the in-game world.
"""
#from peewee import *

from metadata.area_name_mappings import area_name_id_map, area_name_edges_map

from db.node import Node
from db.map_area import MapArea

from maps.graph_edges.edges_arn import edges_arn
from maps.graph_edges.edges_dgb import edges_dgb
from maps.graph_edges.edges_dro import edges_dro
from maps.graph_edges.edges_flo import edges_flo
from maps.graph_edges.edges_hos import edges_hos
from maps.graph_edges.edges_isk import edges_isk
from maps.graph_edges.edges_iwa import edges_iwa
from maps.graph_edges.edges_jan import edges_jan
from maps.graph_edges.edges_kgr import edges_kgr
from maps.graph_edges.edges_kkj import edges_kkj
from maps.graph_edges.edges_kmr import edges_kmr
from maps.graph_edges.edges_kpa import edges_kpa
from maps.graph_edges.edges_kzn import edges_kzn
from maps.graph_edges.edges_mac import edges_mac
from maps.graph_edges.edges_mgm import edges_mgm
from maps.graph_edges.edges_mim import edges_mim
from maps.graph_edges.edges_nok import edges_nok
from maps.graph_edges.edges_obk import edges_obk
from maps.graph_edges.edges_omo import edges_omo
from maps.graph_edges.edges_osr import edges_osr
from maps.graph_edges.edges_pra import edges_pra
from maps.graph_edges.edges_sam import edges_sam
from maps.graph_edges.edges_sbk import edges_sbk
from maps.graph_edges.edges_tik import edges_tik
from maps.graph_edges.edges_trd import edges_trd


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
    return [hashabledict(d) for d in all_edges]


def get_area_edges(area_shorthand:str):
    """Returns a list of all edges which are part of a given ingame area."""
    area_edges = []
    if area_shorthand in area_name_edges_map:
        area_edges.extend(area_name_edges_map.get(area_shorthand))
    else:
        raise KeyError

    return [hashabledict(d) for d in area_edges]


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
    check_unreachable_from_start(all_nodes, all_edges)

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


def check_unreachable_from_start(all_nodes, all_edges):
    """Check if theres any nodes unreachable from KMR_20/4 (Mario's House Green Pipe)"""
    print("Check if theres any nodes unreachable from KMR_20/4 (Mario's House Green Pipe) ...")

    # build world graph
    print("Generating world graph from nodes and edges ...")
    world_graph = generate(all_nodes, all_edges)

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
            print(f"{err.args}: Cannot find edges of {node_id}!")
            raise

    # traverse world graph
    print("Checking node reachability in world graph ...")
    depth_first_search("KMR_20/4")

    not_visited_node_ids = [id for id in world_graph.keys() if id not in visited_node_ids]

    if len(not_visited_node_ids) == 0:
        print("No unreachable nodes from KMR_20/4 found.")
    else:
        print(str(len(not_visited_node_ids)) + " unreachable nodes:")
        for node_id in not_visited_node_ids:
            print(node_id)


if __name__ == "__main__":
    check_graph()
