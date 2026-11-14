"""
This module is used to modify entrances / loading zones within dungeon areas,
rearranging the maps of dungeons into new layouts.
"""
import random
from typing import Dict, List, Set

from db.map_area import MapArea
from db.node import Node

from metadata.area_name_mappings import chapter_dungeon_map

from worldgraph import adjust

def shuffle_dungeon_rooms(
    world_graph: Dict[str, Dict],
    required_chapters: List[int],
    limit_chapter_logic: bool,
    write_spoilers: bool,
) -> tuple[List, Dict, Dict]:
    entrance_changes: List = []

    dungeons_to_shuffle: List[int] = _get_dungeons_to_shuffle(
        limit_chapter_logic,
        required_chapters,
    )

    while dungeons_to_shuffle:
        cur_dungeon_number: int = dungeons_to_shuffle.pop()
        # Find all nodes for the dungeon
        cur_dungeon_nodes: List = _get_cur_dungeon_nodes(world_graph, cur_dungeon_number)
        print(f"{cur_dungeon_nodes=}")

        # Pick one main entrance at random.
        dungeon_entrance_node = _choose_dungeon_entrance(
            cur_dungeon_nodes,
        )

        exit


    spoilers: List = []
    if write_spoilers:
        None #todo

    return entrance_changes, world_graph, spoilers


def _get_dungeons_to_shuffle(
    limit_chapter_logic: bool,
    required_chapters: List[int],
) -> List[int]:
    if limit_chapter_logic and len(required_chapters) > 0:
        dungeons_to_shuffle = required_chapters.copy()
    else:
        #dungeons_to_shuffle = [1,2,3,4,5,6,7,8]
        dungeons_to_shuffle = [1,2,3,4,5,6,7]
    #return dungeons_to_shuffle
    return [1]


def _get_cur_dungeon_nodes(
    world_graph: Dict[str, Dict],
    cur_dungeon_number: int,
) -> List:
    cur_dungeon_nodes: List = list()

    for node_key in world_graph:
        if node_key.startswith(chapter_dungeon_map[cur_dungeon_number]):
            cur_node: Node = world_graph[node_key]["node"]
            if cur_node.entrance_id is not None and node_key != "TRD_00/4":
                cur_dungeon_nodes.append(world_graph[node_key])
                # now we have the node data and all outgoing edges
    return cur_dungeon_nodes


def _choose_dungeon_entrance(
    cur_dungeon_nodes: List,
) -> Dict:
    # The main criteria are:
    #  * Mario can leave the dungeon from there without any items
    #    -> so we never force warping to home if we get stuck in the dungeon
    #  * The room has more than one exit
    #    -> so the entrance is not an immediate dead end
    possible_entrance_nodes_ids: List[str] = []

    for cur_node in cur_dungeon_nodes:
        cur_node_edges: List[Dict[str, Dict[str, str | int] | List]] = cur_node["edge_list"]
        cur_map: str = _get_map_from_node_data(cur_node)

        if (    _can_mario_leave_itemless(cur_node_edges)
            and _room_has_more_than_one_exit(cur_dungeon_nodes, cur_map)
        ):
            possible_entrance_nodes_ids.append(cur_node["node"].identifier)

    print(f"{possible_entrance_nodes_ids=}")
    return random.choice(possible_entrance_nodes_ids)


def _can_mario_leave_itemless(
    edge_list: List[Dict[str, Dict[str, str | int] | List]]
) -> bool:
    return True


def _room_has_more_than_one_exit(cur_dungeon_nodes: List, cur_map: str) -> bool:
    return True


def _get_map_from_node_data(node_data: Dict) -> str:
    return node_data["node"].identifier.split("/")[0]
