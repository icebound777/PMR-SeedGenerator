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
