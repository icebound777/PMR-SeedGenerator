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
from maps.graph_edges.gear_location_shuffle.edges_isk import \
    edges_isk_add    as edges_isk_gls_add, \
    edges_isk_remove as edges_isk_gls_remove
from maps.graph_edges.gear_location_shuffle.edges_kzn import \
    edges_kzn_add    as edges_kzn_gls_add, \
    edges_kzn_remove as edges_kzn_gls_remove
from maps.graph_edges.gear_location_shuffle.edges_tik import \
    edges_tik_add    as edges_tik_gls_add, \
    edges_tik_remove as edges_tik_gls_remove
from worldgraph import adjust, check_unreachable_from_start

# Imports: Glitched logic
from optionset import GlitchOptionSet

# Glitched Logic - Prologue
from maps.graph_edges.glitched_logic.kmr_prologue_gel_early import \
    edges_kmr_add_prologue_gel_early

# Glitched Logic - Toad Town
from maps.graph_edges.glitched_logic.mac_odd_key_early import \
    edges_mac_odd_key_early
from maps.graph_edges.glitched_logic.mac_blue_house_skip import \
    edges_mac_add_bhs_jump, edges_mac_add_bhs_laki, edges_mac_add_bhs_toad_lure
from maps.graph_edges.glitched_logic.mac_bowless_toy_box import \
    edges_mac_add_bowless_toybox
from maps.graph_edges.glitched_logic.mac_enter_storeroom_without_key import \
    edges_mac_add_storeroom_without_key_hammer, edges_mac_add_storeroom_without_key_parakarry
from maps.graph_edges.glitched_logic.mac_sushieless_toad_town_star_piece import \
    edges_mac_add_sushieless_starpiece
from maps.graph_edges.glitched_logic.mac_whale_early import \
    edges_mac_add_whale_early_lzs

# Glitched Logic - Toad Town Tunnels
from maps.graph_edges.glitched_logic.tik_island_pipe_blooper_skip import \
    edges_tik_add_island_pipe_blooper_skip
from maps.graph_edges.glitched_logic.tik_parakarryless_sewer_star_piece import \
    edges_tik_add_parakarryless_sewer_star_piece
from maps.graph_edges.glitched_logic.tik_sewer_blocks_without_ultra_boots import \
    edges_tik_add_sewer_blocks_without_ultra_boots
from maps.graph_edges.glitched_logic.tik_clippy_boots import \
    edges_tik_add_clippy_boots_metal_block_skip, edges_tik_add_clippy_boots_stone_block_skip

# Glitched Logic - Pleasant Path
from maps.graph_edges.glitched_logic.nok_kooperless_pleasant_path_star_piece import \
    edges_nok_add_kooperless_starpiece_clippy
from maps.graph_edges.glitched_logic.nok_invisible_bridge_clip import \
    edges_nok_add_invisible_bridge_clip_laki, edges_nok_add_invisible_bridge_clip_lzs
from maps.graph_edges.glitched_logic.nok_kooperless_pleasant_path_thunderbolt import \
    edges_nok_add_kooperless_thunderbolt

# Glitched Logic - Koopa Bros Fortress
from maps.graph_edges.glitched_logic.nok_bombetteless_kbf_fp_plus import \
    edges_nok_add_bombetteless_fp_plus_laki, edges_nok_add_bombetteless_fp_plus_lzs
from maps.graph_edges.glitched_logic.trd_laki_jailbreak import \
    edges_trd_add_laki_jailbreak
from maps.graph_edges.glitched_logic.trd_bombetteless_right_fortress_jail_key import \
    edges_trd_add_bombetteless_right_key

# Glitched Logic - Mt.Rugged
from maps.graph_edges.glitched_logic.mt_rugged_quake_hammer_and_letter_laki import \
    edges_iwa_add_quake_hammer_and_letter_laki
from maps.graph_edges.glitched_logic.iwa_parakarryless_mt_rugged_seed import \
    edges_iwa_add_parakarryless_mt_rugged_seed
from maps.graph_edges.glitched_logic.iwa_parakarryless_mt_rugged_star_piece import \
    edges_iwa_add_parakarryless_star_piece_laki
from maps.graph_edges.glitched_logic.iwa_buzzar_gap_skip import \
    edges_iwa_add_buzzar_gap_skip_clippy

# Glitched Logic - Dry Dry Desert
from maps.graph_edges.glitched_logic.sbk_desert_brick_block_item_with_parakarry import \
    edges_sbk_add_desert_brick_block_item_parakarry
from maps.graph_edges.glitched_logic.sbk_early_ruins import \
    edges_sbk_add_laki, edges_sbk_add_ultraboots

# Glitched Logic - Dry Dry Ruins
from maps.graph_edges.glitched_logic.isk_artifact_jump import \
    edges_isk_add_artifact_jump_laki
from maps.graph_edges.glitched_logic.isk_ruins_key_laki_jump import \
    edges_isk_add_ruins_key_laki_jump
from maps.graph_edges.glitched_logic.isk_parakarryless_second_sand_room import \
    edges_isk_add_parakarryless_second_sand_room_normal_boots, \
    edges_isk_add_parakarryless_second_sand_room_ultra_boots
from maps.graph_edges.glitched_logic.isk_parakarryless_super_hammer_room import \
    edges_isk_add_parakarryless_super_hammer_room_normal_boots, edges_isk_add_parakarryless_super_hammer_room_ultra_boots
from maps.graph_edges.glitched_logic.isk_ruins_locks_skip import \
    edges_isk_add_ruins_locks_skip_clippy

# Glitched Logic - Boo's Mansion
from maps.graph_edges.glitched_logic.obk_record_skip import \
    edges_obk_add_record_skip_bombette_push, edges_obk_add_record_skip_spin_jump
from maps.graph_edges.glitched_logic.obk_parakarryless_boos_portrait import \
    edges_obk_add_boo_portrait_kooper, edges_obk_add_boo_portrait_laki
    
# Glitched Logic - Gusty Gulch
from maps.graph_edges.glitched_logic.mim_gusty_gulch_gate_skip import \
    edges_mim_add_gusty_gulch_gate_skip_lzs
from maps.graph_edges.glitched_logic.arn_gusty_gulch_gap_skip import \
    edges_arn_add_gusty_gulch_gap_skip_jump
from maps.graph_edges.glitched_logic.arn_kooperless_gusty_gulch_dizzy_dial import \
    edges_arn_add_gusty_gulch_dizzy_dial_jump, edges_arn_add_gusty_gulch_dizzy_dial_laki, edges_arn_add_gusty_gulch_dizzy_dial_parakarry

# Glitched Logic - Tubba's Castle
from maps.graph_edges.glitched_logic.dgb_bowless_tubbas_castle import \
    edges_dgb_add_bowless_tubbas_castle
from maps.graph_edges.glitched_logic.dgb_tubbas_table_laki_jump import \
    edges_dgb_add_tubbas_table_laki_jump
from maps.graph_edges.glitched_logic.dgb_tubba_castle_super_boots_skip import \
    edges_dgb_add_tubbas_castle_super_boots_skip_laki
from maps.graph_edges.glitched_logic.dgb_parakarryless_mega_rush import \
    edges_dgb_add_parakarryless_mega_rush

# Glitched Logic - Toy Box
from maps.graph_edges.glitched_logic.omo_gourmet_guy_skip import \
    edges_omo_add_gourmet_guy_skip_jump, edges_omo_add_gourmet_guy_skip_laki, edges_omo_add_gourmet_guy_skip_parakarry
from maps.graph_edges.glitched_logic.omo_parakarryless_blue_station_star_piece import \
    edges_omo_add_parakarryless_blue_station_star_piece
from maps.graph_edges.glitched_logic.omo_bowless_green_station import \
    edges_omo_add_bowless_green_station_laki
from maps.graph_edges.glitched_logic.omo_kooperless_red_station_shooting_star import \
    edges_omo_add_red_station_shooting_star_parakarry

# Glitched Logic - Jade Jungle
from maps.graph_edges.glitched_logic.jan_raph_skip_english import \
    edges_jan_add_raph_skip_english
from maps.graph_edges.glitched_logic.jan_kzn_ch5_sushie_glitch import \
    edges_jan_kzn_add_ch5_sushie_glitch

# Glitched Logic - Mt. Lavalava
from maps.graph_edges.glitched_logic.kzn_kooperless_lavalava_pow_block import \
    edges_kzn_add_kooperless_pow_block_parakarry
from maps.graph_edges.glitched_logic.kzn_ultra_hammer_skip import \
    edges_kzn_add_ultra_hammer_skip
from maps.graph_edges.glitched_logic.kzn_flarakarry import \
    edges_kzn_add_flarakarry_bombette, edges_kzn_add_flarakarry_laki, edges_kzn_add_flarakarry_parakarry

# Glitched Logic - Flower Fields
from maps.graph_edges.glitched_logic.flo_early_lakilester import \
    edges_flo_add_early_lakilester_bombette_push, edges_flo_add_early_lakilester_without_bombette
from maps.graph_edges.glitched_logic.flo_bombetteless_mega_smash import \
    edges_flo_add_bombetteless_mega_smash
from maps.graph_edges.glitched_logic.flo_sun_tower_skip import \
    edges_flo_add_sun_tower_skip_lzs
from maps.graph_edges.glitched_logic.flo_yellow_berry_gate_skip import \
    edges_flo_add_yellow_berry_gate_skip_bombette_push, edges_flo_add_yellow_berry_gate_skip_laki, edges_flo_add_yellow_berry_gate_skip_lzs
from maps.graph_edges.glitched_logic.flo_red_berry_gate_skip import \
    edges_flo_add_red_berry_gate_skip_bombette_push, edges_flo_add_red_berry_gate_skip_laki
from maps.graph_edges.glitched_logic.flo_blue_berry_gate_skip import \
    edges_flo_add_blue_berry_gate_skip_bombette_push, edges_flo_add_blue_berry_gate_skip_laki
from maps.graph_edges.glitched_logic.flo_bubble_berry_tree_laki_jump import \
    edges_flo_add_bubble_berry_tree_laki

# Glitched Logic - Shiver Region
from maps.graph_edges.glitched_logic.sam_murder_solved_early import \
    edges_sam_add_murder_solved_early_laki, edges_sam_add_murder_solved_early_bombette_push
from maps.graph_edges.glitched_logic.sam_ch7_sushie_glitch import \
    edges_sam_add_ch7_sushie_glitch
from maps.graph_edges.glitched_logic.sam_shiver_mtn_hidden_block_without_ultra_boots import \
    edges_sam_add_shiver_mountain_hidden_block_normal_throw, edges_sam_add_shiver_mountain_hidden_block_laki_throw

# Glitched Logic - Crystal Palace
from maps.graph_edges.glitched_logic.pra_mirror_clip import \
    edges_pra_add_mirror_clip_laki

# Glitched Logic - Bowser's Castle
from maps.graph_edges.glitched_logic.kpa_bowless_bowsers_castle_basement import \
    edges_kpa_add_bowless_bowsers_castle_basement_laki
from maps.graph_edges.glitched_logic.kpa_fast_flood_room import \
    edges_kpa_add_fast_flood_room_bombette_ultra_boots, edges_kpa_add_fast_flood_room_kooper

# Glitched Logic - Global
from maps.graph_edges.glitched_logic.global_break_stone_blocks_with_ultra_boots import \
    edges_kmr_tik_isk_add_break_stone_blocks_ultra_boots
from maps.graph_edges.glitched_logic.kmr_break_yellow_blocks_with_super_boots import \
    edges_kmr_add_break_yellow_blocks_super_boots
from maps.graph_edges.glitched_logic.global_knows_puzzle_solutions import \
    edges_global_knows_puzzle_solutions

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

def get_gear_location_shuffle(world_graph: dict, gear_shuffle_mode: int):
    """
    Returns the modified world graph itself for Gear Location Shuffle and Full Shuffle,
    which removes dynamic hammer block logic.
    """
    all_new_edges = []
    all_edges_to_remove = []

    all_new_edges.extend(edges_isk_gls_add)
    all_new_edges.extend(edges_kzn_gls_add)
    all_edges_to_remove.extend(edges_isk_gls_remove)
    all_edges_to_remove.extend(edges_kzn_gls_remove)

    # The blocks are the same for isk and kzn and all non-vanilla modes, but only GLS modifies tik
    if gear_shuffle_mode == 1:
        all_new_edges.extend(edges_tik_gls_add)
        all_edges_to_remove.extend(edges_tik_gls_remove)

    world_graph, _ = adjust(
        world_graph,
        new_edges=all_new_edges,
        edges_to_remove=all_edges_to_remove
    )

    return world_graph


def get_glitched_logic(world_graph: dict, glitch_settings: GlitchOptionSet, bowsers_castle_mode: int):
    """
    Returns the modified world graph itself for glitched logic, depending
    on settings chosen.
    """
    all_new_edges = []
    all_edges_to_remove = []

    # Goomba Region
    if glitch_settings.prologue_gel_early:
        all_new_edges.extend(edges_kmr_add_prologue_gel_early)

    # Toad Town
    if glitch_settings.odd_key_early:
        all_new_edges.extend(edges_mac_odd_key_early)
    if glitch_settings.blue_house_skip:
        all_new_edges.extend(edges_mac_add_bhs_jump)
    if glitch_settings.blue_house_skip_laki:
        all_new_edges.extend(edges_mac_add_bhs_laki)
    if glitch_settings.blue_house_skip_toad_lure:
        all_new_edges.extend(edges_mac_add_bhs_toad_lure)
    if glitch_settings.bowless_toy_box:
        all_new_edges.extend(edges_mac_add_bowless_toybox)
    if glitch_settings.early_storeroom_parakarry:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_parakarry)
    if glitch_settings.early_storeroom_hammer:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_hammer)
    if glitch_settings.whale_early:
        all_new_edges.extend(edges_mac_add_whale_early_lzs)
    if glitch_settings.sushiesless_toad_town_star_piece:
        all_new_edges.extend(edges_mac_add_sushieless_starpiece)
    
    # Toad Town Tunnels
    if glitch_settings.clippy_boots_stone_block_skip:
        all_new_edges.extend(edges_tik_add_clippy_boots_stone_block_skip)
    if glitch_settings.clippy_boots_metal_block_skip:
        all_new_edges.extend(edges_tik_add_clippy_boots_metal_block_skip)
    if glitch_settings.island_pipe_blooper_skip:
        all_new_edges.extend(edges_tik_add_island_pipe_blooper_skip)
    if glitch_settings.parakarryless_sewer_star_piece:
        all_new_edges.extend(edges_tik_add_parakarryless_sewer_star_piece)
    if glitch_settings.sewer_blocks_without_ultra_boots:
        all_new_edges.extend(edges_tik_add_sewer_blocks_without_ultra_boots)

    # Pleasant Path
    if glitch_settings.kooperless_pleasant_path_star_piece:
        all_new_edges.extend(edges_nok_add_kooperless_starpiece_clippy)
    if glitch_settings.invisible_bridge_clip_laki:
        all_new_edges.extend(edges_nok_add_invisible_bridge_clip_laki)
    if glitch_settings.invisible_bridge_clip_lzs:
        all_new_edges.extend(edges_nok_add_invisible_bridge_clip_lzs)
    if glitch_settings.kooperless_pleasant_path_thunderbolt:
        all_new_edges.extend(edges_nok_add_kooperless_thunderbolt)

    # Koopa Bros Fortress
    if glitch_settings.bombetteless_kbf_fp_plus_laki:
        all_new_edges.extend(edges_nok_add_bombetteless_fp_plus_laki)
    if glitch_settings.bombetteless_kbf_fp_plus_lzs:
        all_new_edges.extend(edges_nok_add_bombetteless_fp_plus_lzs)
    if glitch_settings.laki_jailbreak:
        all_new_edges.extend(edges_trd_add_laki_jailbreak)
    if glitch_settings.bombetteless_right_fortress_jail_key:
        all_new_edges.extend(edges_trd_add_bombetteless_right_key)

    # Mt. Rugged
    if glitch_settings.mt_rugged_quake_hammer_and_letter_with_laki:
        all_new_edges.extend(edges_iwa_add_quake_hammer_and_letter_laki)
    if glitch_settings.parakarryless_mt_rugged_seed:
        all_new_edges.extend(edges_iwa_add_parakarryless_mt_rugged_seed)
    if glitch_settings.parakarryless_mt_rugged_star_piece:
        all_new_edges.extend(edges_iwa_add_parakarryless_star_piece_laki)
    if glitch_settings.buzzar_gap_skip_clippy:
        all_new_edges.extend(edges_iwa_add_buzzar_gap_skip_clippy)

    # Dry Dry Desert
    if glitch_settings.early_ruins_laki_jump:
        all_new_edges.extend(edges_sbk_add_laki)
    if glitch_settings.early_ruins_ultra_boots:
        all_new_edges.extend(edges_sbk_add_ultraboots)
    if glitch_settings.desert_brick_block_item_with_parakarry:
        all_new_edges.extend(edges_sbk_add_desert_brick_block_item_parakarry)

    # Dry Dry Ruins
    if glitch_settings.artifact_jump:
        all_new_edges.extend(edges_isk_add_artifact_jump_laki)
    if glitch_settings.parakarryless_second_sand_room_normal_boots:
        all_new_edges.extend(edges_isk_add_parakarryless_second_sand_room_normal_boots)
    if glitch_settings.parakarryless_second_sand_room_ultra_boots:
        all_new_edges.extend(edges_isk_add_parakarryless_second_sand_room_ultra_boots)
    if glitch_settings.parakarryless_super_hammer_room_normal_boots:
        all_new_edges.extend(edges_isk_add_parakarryless_super_hammer_room_normal_boots)
    if glitch_settings.parakarryless_super_hammer_room_ultra_boots:
        all_new_edges.extend(edges_isk_add_parakarryless_super_hammer_room_ultra_boots)
    if glitch_settings.ruins_key_laki_jump:
        all_new_edges.extend(edges_isk_add_ruins_key_laki_jump)
    if glitch_settings.ruins_locks_skip_clippy:
        all_new_edges.extend(edges_isk_add_ruins_locks_skip_clippy)

    # Boo's Mansion
    if glitch_settings.record_skip_bombette_push:
        all_new_edges.extend(edges_obk_add_record_skip_bombette_push)
    if glitch_settings.record_skip_no_bombette_push:
        all_new_edges.extend(edges_obk_add_record_skip_spin_jump)
    if glitch_settings.boos_portrait_with_kooper:
        all_new_edges.extend(edges_obk_add_boo_portrait_kooper)
    if glitch_settings.boos_portrait_with_laki:
        all_new_edges.extend(edges_obk_add_boo_portrait_laki)

    # Gusty Gulch
    if glitch_settings.gusty_gulch_gate_skip_lzs:
        all_new_edges.extend(edges_mim_add_gusty_gulch_gate_skip_lzs)
    if glitch_settings.kooperless_gusty_gulch_dizzy_dial_jump:
        all_new_edges.extend(edges_arn_add_gusty_gulch_dizzy_dial_jump)
    if glitch_settings.kooperless_gusty_gulch_dizzy_dial_laki:
        all_new_edges.extend(edges_arn_add_gusty_gulch_dizzy_dial_laki)
    if glitch_settings.kooperless_gusty_gulch_dizzy_dial_parakarry:
        all_new_edges.extend(edges_arn_add_gusty_gulch_dizzy_dial_parakarry)
    if glitch_settings.gusty_gulch_gap_skip:
        all_new_edges.extend(edges_arn_add_gusty_gulch_gap_skip_jump)

    # Tubba's Castle
    if glitch_settings.bowless_tubbas_castle:
        all_new_edges.extend(edges_dgb_add_bowless_tubbas_castle)
    if glitch_settings.tubbas_table_laki_jump:
        all_new_edges.extend(edges_dgb_add_tubbas_table_laki_jump)
    if glitch_settings.tubbas_castle_super_boots_skip:
        all_new_edges.extend(edges_dgb_add_tubbas_castle_super_boots_skip_laki)
    if glitch_settings.parakarryless_mega_rush:
        all_new_edges.extend(edges_dgb_add_parakarryless_mega_rush)

    # Toy Box
    if glitch_settings.parakarryless_blue_building_star_piece:
        all_new_edges.extend(edges_omo_add_parakarryless_blue_station_star_piece)
    if glitch_settings.gourmet_guy_skip_jump:
        all_new_edges.extend(edges_omo_add_gourmet_guy_skip_jump)
    if glitch_settings.gourmet_guy_skip_laki:
        all_new_edges.extend(edges_omo_add_gourmet_guy_skip_laki)
    if glitch_settings.gourmet_guy_skip_parakarry:
        all_new_edges.extend(edges_omo_add_gourmet_guy_skip_parakarry)
    if glitch_settings.bowless_green_station:
        all_new_edges.extend(edges_omo_add_bowless_green_station_laki)
    if glitch_settings.kooperless_red_station_shooting_star:
        all_new_edges.extend(edges_omo_add_red_station_shooting_star_parakarry)

    # Jade Jungle
    if glitch_settings.raph_skip_english:
        all_new_edges.extend(edges_jan_add_raph_skip_english)
    if glitch_settings.ch5_sushie_glitch:
        all_new_edges.extend(edges_jan_kzn_add_ch5_sushie_glitch)

    # Mt. Lavalava
    if glitch_settings.kooperless_lavalava_pow_block:
        all_new_edges.extend(edges_kzn_add_kooperless_pow_block_parakarry)
    if glitch_settings.ultra_hammer_skip:
        all_new_edges.extend(edges_kzn_add_ultra_hammer_skip)
    if glitch_settings.flarakarry:
        all_new_edges.extend(edges_kzn_add_flarakarry_parakarry)
    if glitch_settings.parakarryless_flarakarry_bombette:
        all_new_edges.extend(edges_kzn_add_flarakarry_bombette)
    if glitch_settings.parakarryless_flarakarry_laki:
        all_new_edges.extend(edges_kzn_add_flarakarry_laki)

    # Flower Fields
    if glitch_settings.early_laki_lzs:
        all_new_edges.extend(edges_flo_add_early_lakilester_without_bombette)
    if glitch_settings.early_laki_bombette_push:
        all_new_edges.extend(edges_flo_add_early_lakilester_bombette_push)
    if glitch_settings.bombetteless_mega_smash:
        all_new_edges.extend(edges_flo_add_bombetteless_mega_smash)
    if glitch_settings.sun_tower_skip:
        all_new_edges.extend(edges_flo_add_sun_tower_skip_lzs)
    if glitch_settings.yellow_berry_gate_skip_bombette_push:
        all_new_edges.extend(edges_flo_add_yellow_berry_gate_skip_bombette_push)
    if glitch_settings.yellow_berry_gate_skip_laki:
        all_new_edges.extend(edges_flo_add_yellow_berry_gate_skip_laki)
    if glitch_settings.yellow_berry_gate_skip_lzs:
        all_new_edges.extend(edges_flo_add_yellow_berry_gate_skip_lzs)
    if glitch_settings.red_berry_gate_skip_bombette_push:
        all_new_edges.extend(edges_flo_add_red_berry_gate_skip_bombette_push)
    if glitch_settings.red_berry_gate_skip_laki:
        all_new_edges.extend(edges_flo_add_red_berry_gate_skip_laki)
    if glitch_settings.blue_berry_gate_skip_bombette_push:
        all_new_edges.extend(edges_flo_add_blue_berry_gate_skip_bombette_push)
    if glitch_settings.blue_berry_gate_skip_laki:
        all_new_edges.extend(edges_flo_add_blue_berry_gate_skip_laki)
    if glitch_settings.bubble_berry_tree_laki_jump:
        all_new_edges.extend(edges_flo_add_bubble_berry_tree_laki)

    # Shiver Region
    if glitch_settings.murder_solved_early_bombette_push:
        all_new_edges.extend(edges_sam_add_murder_solved_early_bombette_push)
    if glitch_settings.murder_solved_early_laki:
        all_new_edges.extend(edges_sam_add_murder_solved_early_laki)
    if glitch_settings.ch7_sushie_glitch:
        all_new_edges.extend(edges_sam_add_ch7_sushie_glitch)
    if glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_laki:
        all_new_edges.extend(edges_sam_add_shiver_mountain_hidden_block_laki_throw)
    if glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_no_laki:
        all_new_edges.extend(edges_sam_add_shiver_mountain_hidden_block_normal_throw)

    # Crystal Palace
    if glitch_settings.mirror_clip:
        all_new_edges.extend(edges_pra_add_mirror_clip_laki)

    # Bowser's Castle
    if bowsers_castle_mode == 0: # Only modify kpa graph if vanilla castle
        if glitch_settings.bowless_bowsers_castle_basement:
            all_new_edges.extend(edges_kpa_add_bowless_bowsers_castle_basement_laki)
        if glitch_settings.fast_flood_room_kooper:
            all_new_edges.extend(edges_kpa_add_fast_flood_room_kooper)
        if glitch_settings.fast_flood_room_bombette_ultra_boots:
            all_new_edges.extend(edges_kpa_add_fast_flood_room_bombette_ultra_boots)

    # Global
    if glitch_settings.break_metal_blocks_with_ultra_boots:
        all_new_edges.extend(edges_kmr_tik_isk_add_break_stone_blocks_ultra_boots)
    if glitch_settings.break_yellow_blocks_with_super_boots:
        all_new_edges.extend(edges_kmr_add_break_yellow_blocks_super_boots)
    if glitch_settings.knows_puzzle_solutions:
        all_new_edges.extend(edges_global_knows_puzzle_solutions)

    # Modify graph with all pending changes, if any
    if all_new_edges or all_edges_to_remove:
        world_graph, _ = adjust(
            world_graph,
            new_edges=all_new_edges,
            edges_to_remove=all_edges_to_remove
        )

    return world_graph
