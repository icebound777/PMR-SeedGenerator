"""
This module is used to modify entrances / loading zones. Depending on chosen
settings it can set pre-determined paths or randomize them.
"""

from maps.graph_edges.bc_shorten.edges_kpa import \
    edges_kpa_add, edges_kpa_remove
from maps.graph_edges.bc_bossrush.edges_hos import \
    edges_hos_add, edges_hos_remove
from maps.graph_edges.bc_bossrush.edges_kpa import \
    edges_kpa_add    as edges_kpa_bossrush_add, \
    edges_kpa_remove as edges_kpa_bossrus_remove
from worldgraph import adjust, check_unreachable_from_start


def get_shorter_bowsercastle(world_graph: dict):
    """
    Returns a list of db data tuples representing modified entrances in Bowser's
    Castle to shorten it, as well as the corresponding adjusted world graph.
    """
    # Sets up the following connections:
    # kpa_50  (1)  <-> kpa_82  (0) (Hall to Guard Door 1 <-> Guard Door 2)
    # kpa_82  (1)  <-> kpa_32  (0) (Guard Door 2 <-> Lower Grand Hall)
    # kpa_51  (1)  <-> kpa_130 (0) (Hall to Water Puzzle <-> Bill Blaster Hall)
    # kpa_112 (1)  <-> kpa_61  (0) (Hidden Passage 1 <-> Battlement)
    # kpa_33  (2)  <-> kpa_102 (0) (Upper Grand Hall <-> Blue Fire Bridge)
    world_graph, kpa_entrance_modifications = adjust(
        world_graph,
        new_edges=edges_kpa_add,
        edges_to_remove=edges_kpa_remove
    )

    unreachable_node_ids = check_unreachable_from_start(world_graph, False)
    for node_id in unreachable_node_ids:
        world_graph.pop(node_id)

    return kpa_entrance_modifications, world_graph


def get_bowsercastle_bossrush(world_graph: dict):
    """
    Returns a list of db data tuples representing modified entrances in Bowser's
    Castle and Shooting Star Summit to skip straight to the Fake Peach Hallway
    for as boss rush.
    """
    # Sets up the following connection:
    # hos_20 (2) <-> kpa_53 (0) (Riding Star Ship Scene <-> Fake Peach Hallway)
    all_entrance_modifications = []

    world_graph, hos_entrance_modifications = adjust(
        world_graph,
        new_edges=edges_hos_add,
        edges_to_remove=edges_hos_remove
    )
    world_graph, kpa_entrance_modifications = adjust(
        world_graph,
        new_edges=edges_kpa_bossrush_add,
        edges_to_remove=edges_kpa_bossrus_remove
    )

    all_entrance_modifications.extend(hos_entrance_modifications)
    all_entrance_modifications.extend(kpa_entrance_modifications)

    unreachable_node_ids = check_unreachable_from_start(world_graph, False)
    for node_id in unreachable_node_ids:
        world_graph.pop(node_id)

    return all_entrance_modifications, world_graph
