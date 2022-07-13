"""
This module is used to modify entrances / loading zones. Depending on chosen
settings it can set pre-determined paths or randomize them.
"""
from worldgraph import adjust, check_unreachable_from_start

# Imports: Modify Bowser's Castle
from maps.graph_edges.bc_shorten.edges_kpa import \
    edges_kpa_add, edges_kpa_remove
from maps.graph_edges.bc_bossrush.edges_hos import \
    edges_hos_add, edges_hos_remove
from maps.graph_edges.bc_bossrush.edges_kpa import \
    edges_kpa_add    as edges_kpa_bossrush_add, \
    edges_kpa_remove as edges_kpa_bossrus_remove

# Imports: Glitched logic
from optionset import GlitchOptionSet
from maps.graph_edges.glitched_logic.early_ruins import \
    edges_sbk_add_laki, edges_sbk_add_ultraboots

from maps.graph_edges.glitched_logic.prologue_gel_early import \
    edges_kmr_add_prologue_gel_early

from maps.graph_edges.glitched_logic.odd_key_early import \
    edges_mac_odd_key_early
from maps.graph_edges.glitched_logic.blue_house_skip import \
    edges_mac_add_bhs
from maps.graph_edges.glitched_logic.bowless_toy_box import \
    edges_mac_add_bowless_toybox

from maps.graph_edges.glitched_logic.clippy_boots import \
    edges_tik_add_clippy_boots_metal_block_skip, edges_tik_add_clippy_boots_stone_block_skip
from maps.graph_edges.glitched_logic.enter_storeroom_without_key import \
    edges_mac_add_storeroom_without_key_hammer, edges_mac_add_storeroom_without_key_parakarry
from maps.graph_edges.glitched_logic.sushieless_toad_town_star_piece import \
    edges_mac_add_sushieless_starpiece
from maps.graph_edges.glitched_logic.whale_early import \
    edges_mac_add_whale_early_lzs

from maps.graph_edges.glitched_logic.island_pipe_blooper_skip import \
    edges_tik_add_island_pipe_blooper_skip
from maps.graph_edges.glitched_logic.parakaryless_sewer_star_piece import \
    edges_tik_add_parakarryless_sewer_star_piece
from maps.graph_edges.glitched_logic.sewer_blocks_without_ultra_boots import \
    edges_tik_add_sewer_blocks_without_ultra_boots

from maps.graph_edges.glitched_logic.kooperless_pleasant_path_star_piece import \
    edges_nok_add_kooperless_starpiece_clippy
from maps.graph_edges.glitched_logic.invisible_bridge_clip import \
    edges_nok_add_invisible_bridge_clip_laki, edges_nok_add_invisible_bridge_clip_lzs
from maps.graph_edges.glitched_logic.kooperless_pleasant_path_thunderbolt import \
    edges_nok_add_kooperless_thunderbolt

from maps.graph_edges.glitched_logic.bombetteless_kbf_fp_plus import \
    edges_nok_add_bombetteless_fp_plus_laki, edges_nok_add_bombetteless_fp_plus_lzs
from maps.graph_edges.glitched_logic.laki_jailbreak import \
    edges_trd_add_laki_jailbreak
from maps.graph_edges.glitched_logic.bombetteless_right_fortress_jail_key import \
    edges_trd_add_bombetteless_right_key


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


def get_glitched_logic(world_graph: dict, glitch_settings: GlitchOptionSet):
    """
    Returns the modified world graph itself for glitched logic, depending
    on settings chosen.
    """
    all_new_edges = []
    all_edges_to_remove = []

    # Early Ruins: Enter Dry Dry Ruins without Pulse Stone
    if glitch_settings.early_ruins_laki_jump["value"]:
        all_new_edges.extend(edges_sbk_add_laki)
    if glitch_settings.early_ruins_ultra_boots["value"]:
        all_new_edges.extend(edges_sbk_add_ultraboots)

    # Goomba Region
    if glitch_settings.prologue_gel_early["value"]:
        all_new_edges.extend(edges_kmr_add_prologue_gel_early)

    # Toad Town
    if glitch_settings.odd_key_early["value"]:
        all_new_edges.extend(edges_mac_odd_key_early)
    if glitch_settings.blue_house_skip["value"]:
        all_new_edges.extend(edges_mac_add_bhs)
    if glitch_settings.bowless_toy_box["value"]:
        all_new_edges.extend(edges_mac_add_bowless_toybox)
    if glitch_settings.early_storeroom_parakarry["value"]:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_parakarry)
    if glitch_settings.early_storeroom_hammer["value"]:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_hammer)
    if glitch_settings.whale_early["value"]:
        all_new_edges.extend(edges_mac_add_whale_early_lzs)
    if glitch_settings.sushiesless_toad_town_star_piece["value"]:
        all_new_edges.extend(edges_mac_add_sushieless_starpiece)
    
    # Toad Town Tunnels
    if glitch_settings.clippy_boots_stone_block_skip["value"]:
        all_new_edges.extend(edges_tik_add_clippy_boots_stone_block_skip)
    if glitch_settings.clippy_boots_metal_block_skip["value"]:
        all_new_edges.extend(edges_tik_add_clippy_boots_metal_block_skip)
    if glitch_settings.island_pipe_blooper_skip["value"]:
        all_new_edges.extend(edges_tik_add_island_pipe_blooper_skip)
    if glitch_settings.parakarryless_sewer_star_piece["value"]:
        all_new_edges.extend(edges_tik_add_parakarryless_sewer_star_piece)
    if glitch_settings.sewer_blocks_without_ultra_boots["value"]:
        all_new_edges.extend(edges_tik_add_sewer_blocks_without_ultra_boots)

    # Pleasant Path
    if glitch_settings.kooperless_pleasant_path_star_piece["value"]:
        all_new_edges.extend(edges_nok_add_kooperless_starpiece_clippy)
    if glitch_settings.invisible_bridge_clip_laki["value"]:
        all_new_edges.extend(edges_nok_add_invisible_bridge_clip_laki)
    if glitch_settings.invisible_bridge_clip_lzs["value"]:
        all_new_edges.extend(edges_nok_add_invisible_bridge_clip_lzs)
    if glitch_settings.kooperless_pleasant_path_thunderbolt["value"]:
        all_new_edges.extend(edges_nok_add_kooperless_thunderbolt)

    # Koopa Bros Fortress
    if glitch_settings.bombetteless_kbf_fp_plus_laki["value"]:
        all_new_edges.extend(edges_nok_add_bombetteless_fp_plus_laki)
    if glitch_settings.bombetteless_kbf_fp_plus_lzs["value"]:
        all_new_edges.extend(edges_nok_add_bombetteless_fp_plus_lzs)
    if glitch_settings.laki_jailbreak["value"]:
        all_new_edges.extend(edges_trd_add_laki_jailbreak)
    if glitch_settings.bombetteless_right_fortress_jail_key["value"]:
        all_new_edges.extend(edges_trd_add_bombetteless_right_key)
    print(all_new_edges)

    # Modify graph with all pending changes, if any
    if all_new_edges or all_edges_to_remove:
        world_graph, _ = adjust(
            world_graph,
            new_edges=all_new_edges,
            edges_to_remove=all_edges_to_remove
        )

    return world_graph
