"""
This module is used to modify entrances / loading zones dynamically.
In accordance to chosen settings entrances get randomly re-rerouted.
"""
import random
from copy import deepcopy

from db.map_area import MapArea
from db.node import Node

from worldgraph import adjust

from metadata.verbose_area_names import verbose_area_names

def shuffle_dungeon_entrances(
    world_graph:dict,
    starway_spirits_needed:int,
    shuffle_bowsers_castle:bool,
    write_spoilers:bool
) -> dict:
    if starway_spirits_needed > 6:
        shuffle_bowsers_castle = False

    dungeon_border_node_ids = [
        ("NOK_15/1", "TRD_00/0"), # Koopa Bros Fortress main
        #("NOK_15/2", "TRD_00/4"), # Koopa Bros Fortress chest ledge
        ("SBK_02/4", "ISK_01/0"), # Dry Dry Ruins
        ("ARN_04/1", "DGB_00/0"), # Tubba Blubbas Castle
        ("MAC_04/2", "OMO_03/4"), # Shy Guys Toybox
        ("JAN_22/2", "KZN_01/0"), # Mt. Lavalava
        ("MAC_01/5", "FLO_00/0"), # Flower Fields
        ("SAM_10/1", "PRA_01/0"), # Crystal Palace
    ]

    if shuffle_bowsers_castle:
        # determine Bowser Castle target entrance (due to BC mode this can vary)
        bc_node_id = "KPA_60/4"

        for edge in world_graph["HOS_20/2"]["edge_list"]:
            if edge.get("mapchange") is not None and edge["mapchange"]:
                bc_node_id = f"{edge['to']['map']}/{edge['to']['id']}"
                break

        dungeon_border_node_ids.append(
            ("HOS_20/2", bc_node_id) # Bowsers Castle
        )

    add_edges = []
    remove_edges = []

    spirit_warp_relinks = []

    outside_dungeon_node_ids = [i[0] for i in dungeon_border_node_ids]
    inside_dungeon_node_ids = [i[1] for i in dungeon_border_node_ids]

    for outside_node_id in outside_dungeon_node_ids:
        i = random.randint(0, len(inside_dungeon_node_ids) - 1)
        inside_node_id = inside_dungeon_node_ids.pop(i)

        if (outside_node_id, inside_node_id) not in dungeon_border_node_ids:
            # print(f"mod: {outside_node_id} -> {inside_node_id}")
            # find original edges
            for edge in world_graph[outside_node_id]["edge_list"]:
                if edge.get("mapchange") is not None and edge["mapchange"]:
                    remove_edges.append(deepcopy(edge))
                    new_edge = deepcopy(edge)
                    new_edge["to"]["map"] = inside_node_id[:-2]
                    new_edge["to"]["id"] = int(inside_node_id[-1:])
                    add_edges.append(new_edge)
            for edge in world_graph[inside_node_id]["edge_list"]:
                if edge.get("mapchange") is not None and edge["mapchange"]:
                    remove_edges.append(deepcopy(edge))
                    new_edge = deepcopy(edge)
                    new_target_map = outside_node_id[:-2]
                    new_target_id = int(outside_node_id[-1:])
                    new_edge["to"]["map"] = new_target_map
                    new_edge["to"]["id"] = new_target_id
                    add_edges.append(new_edge)
                    # modify star spirit warp target
                    orig_outside = None
                    for outside, inside in dungeon_border_node_ids:
                        if inside == inside_node_id:
                            orig_outside = outside[:-2]
                            break
                    # print(f"{orig_outside=}")
                    spirit_warp_entrance_data = (
                        MapArea.select(MapArea.area_id,
                                       MapArea.map_id,
                                       Node.entrance_id)
                               .join(Node)
                               .where(Node.entrance_type == "spirit-warp")
                               .where(MapArea.name == orig_outside)
                               .objects()
                               .get_or_none()
                    )
                    if spirit_warp_entrance_data is not None:
                        # a spirit warp target entrance exists (i.e. we're
                        # currently not linking tubbas castle or bowsers castle)
                        dbkey = (
                            (0xA3 << 24)
                          | (spirit_warp_entrance_data.area_id << 16)
                          | (spirit_warp_entrance_data.map_id  <<  8)
                          |  spirit_warp_entrance_data.entrance_id
                        )
                        new_target_map_data = (
                            MapArea.select(MapArea.area_id,
                                           MapArea.map_id,
                                           Node.entrance_id)
                                   .join(Node)
                                   .where(MapArea.name == new_target_map)
                                   .where(Node.entrance_id == new_target_id)
                                   .objects()
                                   .get()
                        )
                        dbvalue = (
                            (new_target_map_data.area_id << 16)
                          | (new_target_map_data.map_id  <<  8)
                          |  new_target_map_data.entrance_id
                        )
                        spirit_warp_relinks.append((dbkey, dbvalue))

        # else:
        #     print(f"van: {outside_node_id} -> {inside_node_id}")

    entrance_changes = []
    if add_edges and remove_edges:
        world_graph, entrance_changes = adjust(
            world_graph,
            new_edges=add_edges,
            edges_to_remove=remove_edges
        )
    entrance_changes.extend(spirit_warp_relinks)

    # spoiler log data
    spoilers = []
    pre_sort_spoilers = []
    if write_spoilers:
        for edge in add_edges:
            # verbose from-entrance
            area_name = verbose_area_names.get(edge["from"]["map"][:3]).replace("'", "")

            from_map_data = (
                MapArea.select(MapArea.verbose_name,
                               Node.entrance_name)
                       .join(Node)
                       .where(MapArea.name == edge["from"]["map"])
                       .where(Node.entrance_id == edge["from"]["id"])
                       .objects()
                       .get()
            )
            map_name_verbose = from_map_data.verbose_name
            entrance_verbose = from_map_data.entrance_name

            full_from_entrance = f"{area_name} - {map_name_verbose} - {entrance_verbose}"

            # verbose to-entrance
            area_name = verbose_area_names.get(edge["to"]["map"][:3]).replace("'", "")

            to_map_data = (
                MapArea.select(MapArea.verbose_name,
                               Node.entrance_name)
                       .join(Node)
                       .where(MapArea.name == edge["to"]["map"])
                       .where(Node.entrance_id == edge["to"]["id"])
                       .objects()
                       .get()
            )
            map_name_verbose = to_map_data.verbose_name
            entrance_verbose = to_map_data.entrance_name

            full_to_entrance = f"{area_name} - {map_name_verbose} - {entrance_verbose}"

            if (full_to_entrance, full_from_entrance) not in pre_sort_spoilers:
                pre_sort_spoilers.append((full_from_entrance,full_to_entrance))
            else:
                pre_sort_spoilers.remove((full_to_entrance, full_from_entrance))
                spoilers.append({
                    "entrance": full_to_entrance,
                    "exit": full_from_entrance,
                    "direction": "both"
                })
    for from_entrance, to_entrance in pre_sort_spoilers:
        spoilers.append({
            "entrance": from_entrance,
            "exit": to_entrance,
            "direction": "one-way"
        })

    return entrance_changes, world_graph, spoilers
