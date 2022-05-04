"""
This module is used to modify entrances / loading zones. Depending on chosen
settings it can set pre-determined paths or randomize them.
"""

from maps.graph_edges.shorten_bc.edges_kpa \
    import edges_kpa_add, edges_kpa_remove
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
