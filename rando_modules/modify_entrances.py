"""
This module is used to modify entrances / loading zones statically.
Pre-determined changes are done to the world graph and loading zones in
accordance to chosen settings.
"""
from copy import deepcopy

from worldgraph import adjust

from rando_modules.random_blocks import get_block_placement

from rando_enums.enum_options import (
    GearShuffleMode,
    BowserCastleMode,
    SeedGoal,
    BossShuffleMode,
)

# Imports: Modify Bowser's Castle
from maps.graph_edges.bc_shorten.edges_kpa import \
    edges_kpa_add, edges_kpa_remove
from maps.graph_edges.bc_bossrush.edges_hos import \
    edges_hos_add, edges_hos_remove
from maps.graph_edges.bc_bossrush.edges_kpa import \
    edges_kpa_add    as edges_kpa_bossrush_add, \
    edges_kpa_remove as edges_kpa_bossrush_remove
from maps.graph_edges.gear_location_shuffle.edges_isk import \
    edges_isk_add    as edges_isk_gls_add, \
    edges_isk_remove as edges_isk_gls_remove
from maps.graph_edges.gear_location_shuffle.edges_kzn import \
    edges_kzn_add    as edges_kzn_gls_add, \
    edges_kzn_remove as edges_kzn_gls_remove
from maps.graph_edges.gear_location_shuffle.edges_tik import \
    edges_tik_add    as edges_tik_gls_add, \
    edges_tik_remove as edges_tik_gls_remove

# Imports: Star Hunt
from maps.graph_edges.goal_openstarway.edges_hos import (
    edges_hos_goal_openstarway_add,
    edges_hos_goal_openstarway_remove
)

# Imports: Partner Upgrade Shuffle
from rando_enums.enum_types import BlockType
from maps.graph_edges.partner_upgrade_shuffle.edges_arn import edges_arn_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_dgb import edges_dgb_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_flo import edges_flo_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_isk import edges_isk_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_iwa import edges_iwa_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_jan import edges_jan_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_kmr import edges_kmr_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_kzn import edges_kzn_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_mac import edges_mac_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_nok import edges_nok_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_omo import edges_omo_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_pra import edges_pra_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_sam import edges_sam_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_sbk import edges_sbk_add_partnerupgrades
from maps.graph_edges.partner_upgrade_shuffle.edges_tik import edges_tik_add_partnerupgrades

# Imports: Battle Shuffle
from rando_modules.random_battles import get_boss_battles

# Imports: Glitched logic
from models.options.OptionSet import GlitchOptionSet

# Glitched Logic - Prologue
from maps.graph_edges.glitched_logic.kmr_prologue_gel_early import \
    edges_kmr_add_prologue_gel_early
from maps.graph_edges.glitched_logic.kmr_reverse_goomba_king_bridge import \
    edges_kmr_add_reverse_goomba_king_bridge
from maps.graph_edges.glitched_logic.kmr_goomba_village_entry_fence_clip import \
    edges_kmr_add_goomba_village_entry_fence_clip
from maps.graph_edges.glitched_logic.kmr_goomba_village_hammerless_exit import \
    edges_kmr_add_goomba_village_hammerless_exit_npc_lure, edges_kmr_add_goomba_village_hammerless_exit_laki
from maps.graph_edges.glitched_logic.kmr_hammerless_jr_playground_laki import \
    edges_kmr_add_hammerless_jr_playground_laki
from maps.graph_edges.glitched_logic.kmr_prologue_sushie_glitch import \
    edges_kmr_add_prologue_sushie_glitch_ksj, edges_kmr_add_prologue_sushie_glitch_common, edges_kmr_add_prologue_sushie_glitch_ultra_boots_laki

# Glitched Logic - Toad Town
from maps.graph_edges.glitched_logic.mac_odd_key_early import \
    edges_mac_odd_key_early
from maps.graph_edges.glitched_logic.mac_blue_house_skip import \
    edges_mac_add_bhs_jump, edges_mac_add_bhs_laki, edges_mac_add_bhs_toad_lure
from maps.graph_edges.glitched_logic.mac_bowless_toy_box import \
    edges_mac_add_bowless_toybox_hammer_lure, edges_mac_add_bowless_toybox_hammerless_lure
from maps.graph_edges.glitched_logic.mac_enter_storeroom_without_key import \
    edges_mac_add_storeroom_without_key_hammer, edges_mac_add_storeroom_without_key_parakarry, edges_mac_add_storeroom_without_key_hammerless_lure
from maps.graph_edges.glitched_logic.mac_sushieless_toad_town_star_piece import \
    edges_mac_add_sushieless_starpiece
from maps.graph_edges.glitched_logic.mac_whale_early import \
    edges_mac_add_whale_early_lzs
from maps.graph_edges.glitched_logic.mac_toad_town_sushie_glitch import \
    edges_mac_add_toad_town_sushie_glitch_gearless, edges_mac_add_toad_town_sushie_glitch_jump_or_hammer, edges_mac_add_toad_town_sushie_glitch_full_gear, edges_mac_add_toad_town_sushie_glitch

# Glitched Logic - Toad Town Tunnels
from maps.graph_edges.glitched_logic.tik_island_pipe_blooper_skip import \
    edges_tik_add_island_pipe_blooper_skip
from maps.graph_edges.glitched_logic.tik_parakarryless_sewer_star_piece import \
    edges_tik_add_parakarryless_sewer_star_piece
from maps.graph_edges.glitched_logic.tik_clippy_sewers_upgrade_block import \
    edges_tik_add_clippy_sewers_upgrade_block
from maps.graph_edges.glitched_logic.tik_sewer_blocks_without_ultra_boots import \
    edges_tik_add_sewer_blocks_without_ultra_boots
from maps.graph_edges.glitched_logic.tik_chapter_7_bridge_with_super_boots import \
    edges_tik_add_chapter_7_bridge_with_super_boots
from maps.graph_edges.glitched_logic.tik_clippy_boots import \
    edges_tik_add_clippy_boots_metal_block_skip, edges_tik_add_clippy_boots_stone_block_skip
from maps.graph_edges.glitched_logic.tik_first_block_to_shiver_city_without_super_boots import \
    edges_tik_add_first_block_to_shiver_city_witout_super_boots
from maps.graph_edges.glitched_logic.tik_blocks_to_shiver_city_kooper_shell_item_throw import \
    edges_tik_add_blocks_to_shiver_city_kooper_shell_item_throw
from maps.graph_edges.glitched_logic.tik_break_sewer_yellow_block_with_ultra_boots import \
    edges_tik_add_break_sewer_yellow_block_with_ultra_boots
from maps.graph_edges.glitched_logic.tik_jumpless_sewer_shooting_star import \
    edges_tik_add_jumpless_sewer_shooting_star_kooper

# Glitched Logic - Pleasant Path
from maps.graph_edges.glitched_logic.nok_kooperless_pleasant_path_star_piece import \
    edges_nok_add_kooperless_starpiece_clippy
from maps.graph_edges.glitched_logic.nok_hammerless_pleasant_path_bridge_skip import \
    edges_nok_add_hammerless_bridge_skip_ultra_boots_parakarry
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
from maps.graph_edges.glitched_logic.trd_water_staircase_skip import \
    edges_trd_add_water_staircase_skip

# Glitched Logic - Mt.Rugged
from maps.graph_edges.glitched_logic.iwa_mt_rugged_quake_hammer_and_letter_laki import \
    edges_iwa_add_quake_hammer_and_letter_laki
from maps.graph_edges.glitched_logic.iwa_parakarryless_mt_rugged_seed import \
    edges_iwa_add_parakarryless_mt_rugged_seed
from maps.graph_edges.glitched_logic.iwa_parakarryless_mt_rugged_seed_clippu import \
    edges_iwa_add_parakarryless_mt_rugged_seed_clippy
from maps.graph_edges.glitched_logic.iwa_parakarryless_mt_rugged_star_piece import \
    edges_iwa_add_parakarryless_star_piece_laki
from maps.graph_edges.glitched_logic.iwa_buzzar_gap_skip import \
    edges_iwa_add_buzzar_gap_skip_clippy
from maps.graph_edges.glitched_logic.iwa_mt_rugged_coins_with_kooper import \
    edges_iwa_add_mt_rugged_coins_with_kooper
from maps.graph_edges.glitched_logic.iwa_mt_rugged_station_jumpless_climb import \
    edges_iwa_add_mt_rugged_station_jumpless_climb_bombette, edges_iwa_add_mt_rugged_station_jumpless_climb_laki
from maps.graph_edges.glitched_logic.iwa_jumpless_mt_rugged_train_platform import \
    edges_iwa_add_jumpless_mt_rugged_train_platform_parakarry

# Glitched Logic - Dry Dry Desert
from maps.graph_edges.glitched_logic.sbk_desert_brick_block_item_with_parakarry import \
    edges_sbk_add_desert_brick_block_item_parakarry
from maps.graph_edges.glitched_logic.sbk_early_ruins import \
    edges_sbk_add_laki, edges_sbk_add_ultraboots

# Glitched Logic - Dry Dry Ruins
from maps.graph_edges.glitched_logic.isk_artifact_jump import \
    edges_isk_add_artifact_jump_laki, edges_isk_add_artifact_jump_ultra_boots
from maps.graph_edges.glitched_logic.isk_ruins_key_laki_jump import \
    edges_isk_add_ruins_key_laki_jump
from maps.graph_edges.glitched_logic.isk_parakarryless_second_sand_room import \
    edges_isk_add_parakarryless_second_sand_room_normal_boots, \
    edges_isk_add_parakarryless_second_sand_room_ultra_boots
from maps.graph_edges.glitched_logic.isk_parakarryless_super_hammer_room import \
    edges_isk_add_parakarryless_super_hammer_room_normal_boots, edges_isk_add_parakarryless_super_hammer_room_ultra_boots
from maps.graph_edges.glitched_logic.isk_ruins_locks_skip import \
    edges_isk_add_ruins_locks_skip_clippy
from maps.graph_edges.glitched_logic.isk_ruins_stone_skip import \
    edges_isk_add_ruins_stone_skip
from maps.graph_edges.glitched_logic.isk_ruins_puzzle_solution_early import \
    edges_isk_add_ruins_puzzle_solution_early

# Glitched Logic - Forever Forest
from maps.graph_edges.glitched_logic.mim_forever_forest_backwards import \
    edges_mim_add_forever_forest_backwards

# Glitched Logic - Boo's Mansion
from maps.graph_edges.glitched_logic.obk_record_skip import \
    edges_obk_add_record_skip_bombette_push, edges_obk_add_record_skip_spin_jump
from maps.graph_edges.glitched_logic.obk_parakarryless_boos_portrait import \
    edges_obk_add_boo_portrait_kooper, edges_obk_add_boo_portrait_laki
from maps.graph_edges.glitched_logic.mim_jumpless_mansion_entry import \
    edges_mim_add_jumpless_mansion_entry_parakarry

# Glitched Logic - Gusty Gulch
from maps.graph_edges.glitched_logic.mim_gusty_gulch_gate_skip import \
    edges_mim_add_gusty_gulch_gate_skip_lzs, edges_mim_add_gusty_gulch_gate_skip_laki
from maps.graph_edges.glitched_logic.arn_gusty_gulch_gap_skip import \
    edges_arn_add_gusty_gulch_gap_skip_jump
from maps.graph_edges.glitched_logic.arn_kooperless_gusty_gulch_dizzy_dial import \
    edges_arn_add_gusty_gulch_dizzy_dial_jump, edges_arn_add_gusty_gulch_dizzy_dial_laki, edges_arn_add_gusty_gulch_dizzy_dial_parakarry

# Glitched Logic - Tubba's Castle
from maps.graph_edges.glitched_logic.dgb_bowless_tubbas_castle import \
    edges_dgb_add_bowless_tubbas_castle
from maps.graph_edges.glitched_logic.dgb_tubbas_table_jump_clock import \
    edges_dgb_add_tubbas_table_clock_laki_jump,\
    edges_dgb_add_tubbas_table_clock_ultra_boots
from maps.graph_edges.glitched_logic.dgb_tubbas_table_jump_study import \
    edges_dgb_add_tubbas_table_laki_jump_study
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
from maps.graph_edges.glitched_logic.omo_clippy_green_station_coin_block import \
    edges_omo_clippy_green_station_coin_block
from maps.graph_edges.glitched_logic.omo_kooperless_red_station_shooting_star import \
    edges_omo_add_red_station_shooting_star_parakarry
from maps.graph_edges.glitched_logic.omo_gearless_red_station_shooting_star import \
    edges_omo_add_red_station_shooting_star_gearless
from maps.graph_edges.glitched_logic.omo_parakarryless_blue_block_city_gap import \
    edges_omo_add_parakarryless_blue_block_city_gap
from maps.graph_edges.glitched_logic.omo_blue_switch_skip import \
    edges_omo_add_blue_switch_skip_laki, edges_omo_add_blue_switch_skip_ultra_boots
from maps.graph_edges.glitched_logic.omo_red_barricade_skip import \
    edges_omo_add_red_barricade_skip
from maps.graph_edges.glitched_logic.omo_wattless_dark_room import \
    edges_omo_add_wattless_dark_room
from maps.graph_edges.glitched_logic.omo_hammerless_blue_station import \
    edges_omo_add_hammerless_blue_station_laki
from maps.graph_edges.glitched_logic.omo_hammerless_pink_station import \
    edges_omo_add_hammerless_pink_station_laki

# Glitched Logic - Jade Jungle
from maps.graph_edges.glitched_logic.jan_raph_skip_english import \
    edges_jan_add_raph_skip_english
from maps.graph_edges.glitched_logic.jan_raph_skip_parakarry import \
    edges_jan_add_raph_skip_parakarry
from maps.graph_edges.glitched_logic.jan_kzn_ch5_sushie_glitch import \
    edges_jan_kzn_add_ch5_sushie_glitch, edges_kzn_add_volcano_sushie_glitch, \
    edges_kzn_add_volcano_sushie_glitch_superboots, edges_kzn_add_volcano_sushie_glitch_goombario
from maps.graph_edges.glitched_logic.jan_sushieless_jungle_starpiece_and_letter import \
    edges_jan_add_sushieless_jungle_starpiece_and_letter_lzs
from maps.graph_edges.glitched_logic.jan_jumpless_deep_jungle import \
    edges_jan_add_jumpless_deep_jungle_laki

# Glitched Logic - Mt. Lavalava
from maps.graph_edges.glitched_logic.kzn_kooperless_lavalava_pow_block import \
    edges_kzn_add_kooperless_pow_block_parakarry, edges_kzn_add_kooperless_pow_block_super_boots
from maps.graph_edges.glitched_logic.kzn_jumpless_lavalava_pow_block import \
    edges_kzn_add_jumpless_pow_block_kooper
from maps.graph_edges.glitched_logic.kzn_ultra_hammer_skip import \
    edges_kzn_add_ultra_hammer_skip, edges_kzn_add_ultra_hammer_skip_laki, edges_kzn_add_ultra_hammer_skip_sushie
from maps.graph_edges.glitched_logic.kzn_flarakarry import \
    edges_kzn_add_flarakarry_laki, edges_kzn_add_flarakarry_parakarry

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
from maps.graph_edges.glitched_logic.flo_bubble_berry_tree_early import \
    edges_flo_add_bubble_berry_tree_early_laki, edges_flo_add_bubble_berry_tree_early_ultra_boots

# Glitched Logic - Shiver Region
from maps.graph_edges.glitched_logic.sam_murder_solved_early import \
    edges_sam_add_murder_solved_early_laki, edges_sam_add_murder_solved_early_bombette_push
from maps.graph_edges.glitched_logic.sam_ch7_sushie_glitch import \
    edges_sam_add_ch7_sushie_glitch, edges_sam_add_star_stone_with_ch7_sushie_glitch
from maps.graph_edges.glitched_logic.sam_shiver_mtn_hidden_block_without_ultra_boots import \
    edges_sam_add_shiver_mountain_hidden_block_normal_throw, edges_sam_add_shiver_mountain_hidden_block_laki_throw
from maps.graph_edges.glitched_logic.sam_snowmen_skip import \
    edges_sam_add_snowmen_skip_laki
from maps.graph_edges.glitched_logic.sam_shiver_mountain_switch_skip import \
    edges_sam_add_shiver_mountain_switch_skip
from maps.graph_edges.glitched_logic.sam_sushieless_warehouse_key import \
    edges_sam_add_sushieless_warehouse_key_bombette_push, edges_sam_add_sushieless_warehouse_key_kooper_ksj

# Glitched Logic - Crystal Palace
from maps.graph_edges.glitched_logic.pra_mirror_clip import \
    edges_pra_add_mirror_clip_laki
from maps.graph_edges.glitched_logic.pra_kooper_puzzle_skip import \
    edges_pra_add_kooper_puzzle_skip

# Glitched Logic - Bowser's Castle
from maps.graph_edges.glitched_logic.kpa_bowless_bowsers_castle_basement import \
    edges_kpa_add_bowless_bowsers_castle_basement_laki
from maps.graph_edges.glitched_logic.kpa_fast_flood_room import \
    edges_kpa_add_fast_flood_room_bombette_ultra_boots, edges_kpa_add_fast_flood_room_kooper
from maps.graph_edges.glitched_logic.kpa_bombetteless_bowsers_castle_basement import \
    edges_kpa_add_bombetteless_bowsers_castle_basement_laki

# Glitched Logic - Global
from maps.graph_edges.glitched_logic.global_break_stone_blocks_with_ultra_boots import \
    edges_kmr_tik_isk_add_break_stone_blocks_ultra_boots
from maps.graph_edges.glitched_logic.kmr_break_yellow_blocks_with_super_boots import \
    edges_kmr_add_break_yellow_blocks_super_boots
from maps.graph_edges.glitched_logic.global_knows_puzzle_solutions import \
    edges_global_knows_puzzle_solutions
from maps.graph_edges.glitched_logic.global_reach_high_blocks_with_super_boots import \
    edges_global_reach_high_blocks_with_super_boots


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

    return kpa_entrance_modifications, world_graph


def get_bowsercastle_bossrush(world_graph: dict):
    """
    Returns a list of db data tuples representing modified entrances in Bowser's
    Castle and Shooting Star Summit to skip straight to the Fake Peach Hallway
    for as boss rush.
    """
    # Sets up the following connection:
    # hos_20 (2) <-> kpa_53 (0) (Riding Star Ship Scene <-> Fake Peach Hallway)
    all_new_edges = []
    all_edges_to_remove = []
    entrance_modifications = []

    all_new_edges.extend(edges_hos_add)
    all_new_edges.extend(edges_kpa_bossrush_add)
    all_edges_to_remove.extend(edges_hos_remove)
    all_edges_to_remove.extend(edges_kpa_bossrush_remove)

    world_graph, entrance_modifications = adjust(
        world_graph,
        new_edges=all_new_edges,
        edges_to_remove=all_edges_to_remove
    )

    return entrance_modifications, world_graph


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
    if gear_shuffle_mode == GearShuffleMode.GEAR_LOCATION_SHUFFLE:
        all_new_edges.extend(edges_tik_gls_add)
        all_edges_to_remove.extend(edges_tik_gls_remove)

    world_graph, _ = adjust(
        world_graph,
        new_edges=all_new_edges,
        edges_to_remove=all_edges_to_remove
    )

    return world_graph


def get_partner_upgrade_shuffle(
    world_graph: dict,
    shuffle_blocks: bool,
    glitch_settings: GlitchOptionSet
) -> (dict, list):
    """
    Returns the modified world graph itself for Partner Upgrade Shuffle,
    with upgrades shuffled between SuperBlock locations and, if needed,
    MultiCoinBlock locations.
    """
    block_placement = get_block_placement(
        shuffle_blocks,
        supers_are_yellow=True
    )

    # handle upgrade block glitch logic first
    if glitch_settings.clippy_sewers_upgrade_block:
        edges_tik_add_partnerupgrades.extend(edges_tik_add_clippy_sewers_upgrade_block)
    if glitch_settings.clippy_green_station_coin_block:
        edges_omo_add_partnerupgrades.extend(edges_omo_clippy_green_station_coin_block)

    edges_partner_upgrade = []
    edges_partner_upgrade.extend(edges_arn_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_dgb_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_flo_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_isk_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_iwa_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_jan_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_kmr_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_kzn_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_mac_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_nok_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_omo_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_pra_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_sam_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_sbk_add_partnerupgrades)
    edges_partner_upgrade.extend(edges_tik_add_partnerupgrades)

    all_new_edges = []

    for block_dbkey, block_type in block_placement:
        if block_type == BlockType.YELLOW:
            # add relevant graph edge to new edges
            for cur_block_dbkey, edge in edges_partner_upgrade:
                if block_dbkey == cur_block_dbkey:
                    all_new_edges.append(edge)

    world_graph, _ = adjust(
        world_graph,
        new_edges=all_new_edges,
        edges_to_remove=[]
    )

    return world_graph, block_placement


def set_starway_requirements(
    world_graph: dict,
    spirits_needed: int,
    specific_spirits: list,
    powerstars_needed: int,
    seed_goal: SeedGoal
) -> dict:
    """
    Returns the modified world graph itself, modified to set the spirits
    required to enter Star Way.
    """
    added_requirements = []
    entrance_modifications = []

    # set number of spirits needed
    if spirits_needed > 0:
        added_requirements.append([{"starspirits": spirits_needed}])

    # set specific spirits, if required
    # the logic knows the spirits as "STARSPIRIT_X", where X is in 1-7
    for spirit_number in specific_spirits:
        added_requirements.append([f"STARSPIRIT_{spirit_number}"])

    if powerstars_needed > 0:
        added_requirements.append([{"powerstars": powerstars_needed}])

    if seed_goal == SeedGoal.OPEN_STARWAY:
        world_graph, entrance_modifications = adjust(
            world_graph,
            new_edges=edges_hos_goal_openstarway_add,
            edges_to_remove=edges_hos_goal_openstarway_remove
        )

    # find Star Way edge and modify its requirements
    for index, entrance in enumerate(world_graph["HOS_01/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "HOS_01"
            and entrance["to"]["id"] == 1
        ):
            world_graph["HOS_01/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            #print(world_graph["HOS_01/0"]["edge_list"][index]["reqs"])
            break

    # add requirements to chapter 8 jr. troopa and both bowser battles, so the
    # logic doesn't require going through them too early

    ## ch8 jr. troopa
    for index, entrance in enumerate(world_graph["KPA_83/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_83"
            and entrance["to"]["id"] == 1
        ):
            world_graph["KPA_83/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    for index, entrance in enumerate(world_graph["KPA_83/1"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_83"
            and entrance["to"]["id"] == 0
        ):
            world_graph["KPA_83/1"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## hallway bowser
    for index, entrance in enumerate(world_graph["KKJ_13/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KKJ_13"
            and entrance["to"]["id"] == 1
        ):
            world_graph["KKJ_13/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    for index, entrance in enumerate(world_graph["KKJ_13/1"]["edge_list"]):
        if (    entrance["to"]["map"] == "KKJ_13"
            and entrance["to"]["id"] == 0
        ):
            world_graph["KKJ_13/1"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## final bowser
    for index, entrance in enumerate(world_graph["KKJ_25/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KKJ_25"
            and entrance["to"]["id"] == 0
        ):
            world_graph["KKJ_25/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break

    # also add requirements to chapter 8 Koopatrol and lava switch battles, so
    # the logic doesn't require going through them too early
    # This is far from ideal, but an okay-ish temporary solution to having
    # to battle chapter 8 enemies way too early

    ## Koopatrol: Bowser Castle Key in lava room
    for index, entrance in enumerate(world_graph["KPA_11/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_11"
            and entrance["to"]["id"] == "ItemA"
        ):
            world_graph["KPA_11/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## Koopatrol: Prison 1
    for index, entrance in enumerate(world_graph["KPA_91/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_91"
            and entrance["to"]["id"] == "ItemA"
        ):
            world_graph["KPA_91/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## Koopatrol: Prison 2
    for index, entrance in enumerate(world_graph["KPA_95/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_95"
            and entrance["to"]["id"] == "ItemA"
        ):
            world_graph["KPA_95/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## Lava Control room battle
    for index, entrance in enumerate(world_graph["KPA_16/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_16"
            and entrance["to"]["id"] == 0
        ):
            world_graph["KPA_16/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break

    return entrance_modifications, world_graph


def set_starbeam_requirements(
    world_graph: dict,
    spirits_needed: int,
    powerstars_needed: int,
) -> dict:
    """
    Returns the modified world graph itself, modified to set the spirits
    and power stars required to collect the Star Beam item location.
    """
    added_requirements = []

    if spirits_needed > 0:
        added_requirements.append([{"starspirits": spirits_needed}])
    if powerstars_needed > 0:
        added_requirements.append([{"powerstars": powerstars_needed}])

    # find Star Beam edge and modify its requirements
    for index, entrance in enumerate(world_graph["HOS_05/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "HOS_05"
            and entrance["to"]["id"] == "GiftA"
        ):
            world_graph["HOS_05/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            #print(world_graph["HOS_05/0"]["edge_list"][index]["reqs"])
            break

    # add requirements to chapter 8 jr. troopa and both bowser battles, so the
    # logic doesn't require going through them too early.
    # this will add onto requirements placed by set_starway_requirements

    ## ch8 jr. troopa
    for index, entrance in enumerate(world_graph["KPA_83/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_83"
            and entrance["to"]["id"] == 1
        ):
            world_graph["KPA_83/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    for index, entrance in enumerate(world_graph["KPA_83/1"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_83"
            and entrance["to"]["id"] == 0
        ):
            world_graph["KPA_83/1"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## hallway bowser
    for index, entrance in enumerate(world_graph["KKJ_13/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KKJ_13"
            and entrance["to"]["id"] == 1
        ):
            world_graph["KKJ_13/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    for index, entrance in enumerate(world_graph["KKJ_13/1"]["edge_list"]):
        if (    entrance["to"]["map"] == "KKJ_13"
            and entrance["to"]["id"] == 0
        ):
            world_graph["KKJ_13/1"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## final bowser
    for index, entrance in enumerate(world_graph["KKJ_25/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KKJ_25"
            and entrance["to"]["id"] == 0
        ):
            world_graph["KKJ_25/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break

    # also add requirements to chapter 8 Koopatrol and lava switch battles, so
    # the logic doesn't require going through them too early
    # This is far from ideal, but an okay-ish temporary solution to having
    # to battle chapter 8 enemies way too early

    ## Koopatrol: Bowser Castle Key in lava room
    for index, entrance in enumerate(world_graph["KPA_11/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_11"
            and entrance["to"]["id"] == "ItemA"
        ):
            world_graph["KPA_11/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## Koopatrol: Prison 1
    for index, entrance in enumerate(world_graph["KPA_91/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_91"
            and entrance["to"]["id"] == "ItemA"
        ):
            world_graph["KPA_91/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## Koopatrol: Prison 2
    for index, entrance in enumerate(world_graph["KPA_95/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_95"
            and entrance["to"]["id"] == "ItemA"
        ):
            world_graph["KPA_95/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break
    ## Lava Control room battle
    for index, entrance in enumerate(world_graph["KPA_16/0"]["edge_list"]):
        if (    entrance["to"]["map"] == "KPA_16"
            and entrance["to"]["id"] == 0
        ):
            world_graph["KPA_16/0"]["edge_list"][index]["reqs"].extend(added_requirements)
            break

    return world_graph


def get_limited_chapter_logic(
    world_graph: dict,
    chosen_spirits: list,
    gear_shuffle_mode: GearShuffleMode
) -> dict:
    """
    Returns the modified world graph itself for specific spirits limiting
    chapter logic, which sets item locations in non-required chapters
    to be in logic only if Bowser can already be reached. This makes them
    effectively out of logic, but still allows the item placement to put
    some progression items outside of the required chapters.
    """
    chapter_areaname_map = {
        1: ["NOK","TRD"],
        2: ["IWA","SBK","DRO","ISK"],
        3: ["MIM","OBK","ARN","DGB"],
        4: ["OMO"],
        5: ["JAN","KZN"],
        6: ["FLO"],
        7: ["SAM","PRA"],
        8: ["KPA"]
    }
    out_of_logic_areas = []
    for chapter, area_list in chapter_areaname_map.items():
        if chapter not in chosen_spirits:
            out_of_logic_areas.extend(chapter_areaname_map[chapter])

    if gear_shuffle_mode == GearShuffleMode.FULL_SHUFFLE:
        for node_id in world_graph:
            if node_id[:3] in out_of_logic_areas:
                for index, edge in enumerate(world_graph[node_id]["edge_list"]):
                    if type(edge["to"]["id"]) is str: # is item location
                        world_graph[node_id]["edge_list"][index]["reqs"].extend([["YOUWIN"]])
    else:
        gear_node_ids = [
            # Hammer bush irrelevant here
            "ISK_09/BigChest", # SuperHammer
            "OBK_04/BigChest", # SuperBoots
            "KZN_07/BigChest"  # UltraHammer
            # UltraBoots irrelevant here
        ]
        for node_id in world_graph:
            if node_id[:3] in out_of_logic_areas:
                for index, edge in enumerate(world_graph[node_id]["edge_list"]):
                    if type(edge["to"]["id"]) is str: # is item location
                        if (f"{edge['to']['map']}/{edge['to']['id']}") not in gear_node_ids:
                            world_graph[node_id]["edge_list"][index]["reqs"].extend([["YOUWIN"]])

    # Remove logic from star spirits we do not need to rescue.
    # This is so Rowf doesn't require us to still save them.
    area_spiritnode_pairs = [
        ("TRD", "TRD_10/0"),
        ("ISK", "ISK_16/0"),
        ("ARN", "ARN_07/0"),
        ("OMO", "OMO_15/0"),
        ("JAN", "JAN_22/0"),
        ("FLO", "FLO_21/0"),
        ("PRA", "PRA_32/0")
    ]
    for pair in area_spiritnode_pairs:
        if pair[0] in out_of_logic_areas:
            for index, edge in enumerate(world_graph[pair[1]]["edge_list"]):
                if (   "pseudoitems" in edge
                    and any(True for x in edge["pseudoitems"] if x.startswith("STARSPIRIT_"))
                ):
                    world_graph[pair[1]]["edge_list"][index]["reqs"].extend([["YOUWIN"]])
                    break

    # Special case: block Kolorado's Camp in the desert if ch2 is out of logic
    kolorados_camp = ("SBK", "SBK_30/0")
    if kolorados_camp[0] in out_of_logic_areas:
        for index, edge in enumerate(world_graph[kolorados_camp[1]]["edge_list"]):
            if (   "pseudoitems" in edge
               and "RF_CanVisitDesertCamp" in edge["pseudoitems"]
            ):
                world_graph[kolorados_camp[1]]["edge_list"][index]["reqs"].extend([["YOUWIN"]])
                break

    return world_graph


def get_glitched_logic(
    world_graph: dict,
    glitch_settings: GlitchOptionSet,
    bowsers_castle_mode: int,
    shuffle_dungeon_entrances: bool
):
    """
    Returns the modified world graph itself for glitched logic, depending
    on settings chosen.
    """
    all_new_edges = []
    all_edges_to_remove = []

    # Goomba Region
    if glitch_settings.prologue_gel_early:
        all_new_edges.extend(edges_kmr_add_prologue_gel_early)
    if glitch_settings.reverse_goomba_king_bridge:
        all_new_edges.extend(edges_kmr_add_reverse_goomba_king_bridge)
    if glitch_settings.goomba_village_entry_fence_clip:
        all_new_edges.extend(edges_kmr_add_goomba_village_entry_fence_clip)
    if glitch_settings.goomba_village_npc_lure_exit:
        all_new_edges.extend(edges_kmr_add_goomba_village_hammerless_exit_npc_lure)
    if glitch_settings.goomba_village_laki_exit:
        all_new_edges.extend(edges_kmr_add_goomba_village_hammerless_exit_laki)
    if glitch_settings.hammerless_jr_playground_laki:
        all_new_edges.extend(edges_kmr_add_hammerless_jr_playground_laki)
    if glitch_settings.prologue_sushie_glitch_ksj:
        all_new_edges.extend(edges_kmr_add_prologue_sushie_glitch_ksj)
        all_new_edges.extend(edges_kmr_add_prologue_sushie_glitch_common)
    if glitch_settings.prologue_sushie_glitch_ultra_boots_laki:
        all_new_edges.extend(edges_kmr_add_prologue_sushie_glitch_ultra_boots_laki)
        all_new_edges.extend(edges_kmr_add_prologue_sushie_glitch_common)

    # Toad Town
    if glitch_settings.odd_key_early:
        all_new_edges.extend(edges_mac_odd_key_early)
    if glitch_settings.blue_house_skip:
        all_new_edges.extend(edges_mac_add_bhs_jump)
    if glitch_settings.blue_house_skip_laki:
        all_new_edges.extend(edges_mac_add_bhs_laki)
    if glitch_settings.blue_house_skip_toad_lure:
        all_new_edges.extend(edges_mac_add_bhs_toad_lure)
    if glitch_settings.bowless_toy_box_hammer:
        all_new_edges.extend(edges_mac_add_bowless_toybox_hammer_lure)
    if glitch_settings.bowless_toy_box_hammerless_lure:
        all_new_edges.extend(edges_mac_add_bowless_toybox_hammerless_lure)
    if glitch_settings.early_storeroom_parakarry:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_parakarry)
    if glitch_settings.early_storeroom_hammer:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_hammer)
    if glitch_settings.early_storeroom_hammerless_lure:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_hammerless_lure)
    if glitch_settings.whale_early:
        all_new_edges.extend(edges_mac_add_whale_early_lzs)
    if glitch_settings.sushiesless_toad_town_star_piece:
        all_new_edges.extend(edges_mac_add_sushieless_starpiece)
    if glitch_settings.toad_town_sushie_glitch_gearless:
        all_new_edges.extend(edges_mac_add_toad_town_sushie_glitch_gearless)
    if glitch_settings.toad_town_sushie_glitch:
        all_new_edges.extend(edges_mac_add_toad_town_sushie_glitch_jump_or_hammer)
    if glitch_settings.toad_town_sushie_glitch_full_gear:
        all_new_edges.extend(edges_mac_add_toad_town_sushie_glitch_full_gear)
    if glitch_settings.toad_town_sushie_glitch_gearless or glitch_settings.toad_town_sushie_glitch or glitch_settings.toad_town_sushie_glitch_full_gear:
        all_new_edges.extend(edges_mac_add_toad_town_sushie_glitch)

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
    if glitch_settings.chapter_7_bridge_with_super_boots:
        all_new_edges.extend(edges_tik_add_chapter_7_bridge_with_super_boots)
    if glitch_settings.first_block_to_shiver_city_without_super_boots:
        all_new_edges.extend(edges_tik_add_first_block_to_shiver_city_witout_super_boots)
    if glitch_settings.blocks_to_shiver_city_kooper_shell_item_throw:
        all_new_edges.extend(edges_tik_add_blocks_to_shiver_city_kooper_shell_item_throw)
    if glitch_settings.sewer_yellow_block_with_ultra_boots:
        all_new_edges.extend(edges_tik_add_break_sewer_yellow_block_with_ultra_boots)
    if glitch_settings.jumpless_sewer_shooting_star:
        all_new_edges.extend(edges_tik_add_jumpless_sewer_shooting_star_kooper)

    # Pleasant Path
    if glitch_settings.kooperless_pleasant_path_star_piece:
        all_new_edges.extend(edges_nok_add_kooperless_starpiece_clippy)
    if glitch_settings.hammerless_pleasant_path_bridge_ultra_boots_parakarry:
        all_new_edges.extend(edges_nok_add_hammerless_bridge_skip_ultra_boots_parakarry)
    if glitch_settings.invisible_bridge_clip_laki:
        all_new_edges.extend(edges_nok_add_invisible_bridge_clip_laki)
    if glitch_settings.invisible_bridge_clip_lzs:
        all_new_edges.extend(edges_nok_add_invisible_bridge_clip_lzs)
    if glitch_settings.kooperless_pleasant_path_thunderbolt:
        all_new_edges.extend(edges_nok_add_kooperless_thunderbolt)

    # Koopa Bros Fortress
    if glitch_settings.bombetteless_kbf_fp_plus_laki:
        all_new_edges.extend(edges_nok_add_bombetteless_fp_plus_laki)
    if glitch_settings.bombetteless_kbf_fp_plus_lzs and not shuffle_dungeon_entrances:
        all_new_edges.extend(edges_nok_add_bombetteless_fp_plus_lzs)
    if glitch_settings.laki_jailbreak:
        all_new_edges.extend(edges_trd_add_laki_jailbreak)
    if glitch_settings.bombetteless_right_fortress_jail_key:
        all_new_edges.extend(edges_trd_add_bombetteless_right_key)
    if glitch_settings.water_staircase_skip:
        all_new_edges.extend(edges_trd_add_water_staircase_skip)

    # Mt. Rugged
    if glitch_settings.mt_rugged_quake_hammer_and_letter_with_laki:
        all_new_edges.extend(edges_iwa_add_quake_hammer_and_letter_laki)
    if glitch_settings.parakarryless_mt_rugged_seed:
        all_new_edges.extend(edges_iwa_add_parakarryless_mt_rugged_seed)
    if glitch_settings.parakarryless_mt_rugged_seed_clippy:
        all_new_edges.extend(edges_iwa_add_parakarryless_mt_rugged_seed_clippy)
    if glitch_settings.parakarryless_mt_rugged_star_piece:
        all_new_edges.extend(edges_iwa_add_parakarryless_star_piece_laki)
    if glitch_settings.buzzar_gap_skip_clippy:
        all_new_edges.extend(edges_iwa_add_buzzar_gap_skip_clippy)
    if glitch_settings.mt_rugged_coins_with_kooper:
        all_new_edges.extend(edges_iwa_add_mt_rugged_coins_with_kooper)
    if glitch_settings.mt_rugged_station_jumpless_climb_bombette:
        all_new_edges.extend(edges_iwa_add_mt_rugged_station_jumpless_climb_bombette)
    if glitch_settings.mt_rugged_station_jumpless_climb_laki:
        all_new_edges.extend(edges_iwa_add_mt_rugged_station_jumpless_climb_laki)
    if glitch_settings.jumpless_mt_rugged_train_platform_parakarry:
        all_new_edges.extend(edges_iwa_add_jumpless_mt_rugged_train_platform_parakarry)

    # Dry Dry Desert
    if glitch_settings.early_ruins_laki_jump:
        all_new_edges.extend(edges_sbk_add_laki)
    if glitch_settings.early_ruins_ultra_boots:
        all_new_edges.extend(edges_sbk_add_ultraboots)
    if glitch_settings.desert_brick_block_item_with_parakarry:
        all_new_edges.extend(edges_sbk_add_desert_brick_block_item_parakarry)

    # Dry Dry Ruins
    if glitch_settings.artifact_jump_laki:
        all_new_edges.extend(edges_isk_add_artifact_jump_laki)
    if glitch_settings.artifact_jump_ultra_boots:
        all_new_edges.extend(edges_isk_add_artifact_jump_ultra_boots)
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
    if glitch_settings.ruins_puzzle_solution_early:
        all_new_edges.extend(edges_isk_add_ruins_puzzle_solution_early)
    if glitch_settings.ruins_stone_skip:
        all_new_edges.extend(edges_isk_add_ruins_stone_skip)

    # Forever Forest
    if glitch_settings.forever_forest_backwards:
        all_new_edges.extend(edges_mim_add_forever_forest_backwards)

    # Boo's Mansion
    if glitch_settings.record_skip_bombette_push:
        all_new_edges.extend(edges_obk_add_record_skip_bombette_push)
    if glitch_settings.record_skip_no_bombette_push:
        all_new_edges.extend(edges_obk_add_record_skip_spin_jump)
    if glitch_settings.boos_portrait_with_kooper:
        all_new_edges.extend(edges_obk_add_boo_portrait_kooper)
    if glitch_settings.boos_portrait_with_laki:
        all_new_edges.extend(edges_obk_add_boo_portrait_laki)
    if glitch_settings.jumpless_mansion_entry:
        all_new_edges.extend(edges_mim_add_jumpless_mansion_entry_parakarry)

    # Gusty Gulch
    if glitch_settings.gusty_gulch_gate_skip_lzs:
        all_new_edges.extend(edges_mim_add_gusty_gulch_gate_skip_lzs)
    if glitch_settings.gusty_gulch_gate_skip_laki:
        all_new_edges.extend(edges_mim_add_gusty_gulch_gate_skip_laki)
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
    if glitch_settings.tubbas_table_laki_jump_clock:
        all_new_edges.extend(edges_dgb_add_tubbas_table_clock_laki_jump)
    if glitch_settings.tubbas_table_ultra_boots:
        all_new_edges.extend(edges_dgb_add_tubbas_table_clock_ultra_boots)
    if glitch_settings.tubbas_table_laki_jump_study:
        all_new_edges.extend(edges_dgb_add_tubbas_table_laki_jump_study)
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
    if glitch_settings.gearless_red_station_shooting_star:
        all_new_edges.extend(edges_omo_add_red_station_shooting_star_gearless)
    if glitch_settings.parakarryless_blue_block_city_gap:
        all_new_edges.extend(edges_omo_add_parakarryless_blue_block_city_gap)
    if glitch_settings.blue_switch_skip_laki:
        all_new_edges.extend(edges_omo_add_blue_switch_skip_laki)
    if glitch_settings.blue_switch_skip_ultra_boots:
        all_new_edges.extend(edges_omo_add_blue_switch_skip_ultra_boots)
    if glitch_settings.red_barricade_skip:
        all_new_edges.extend(edges_omo_add_red_barricade_skip)
    if glitch_settings.wattless_dark_room:
        all_new_edges.extend(edges_omo_add_wattless_dark_room)
    if glitch_settings.hammerless_blue_station_laki:
        all_new_edges.extend(edges_omo_add_hammerless_blue_station_laki)
    if glitch_settings.hammerless_pink_station_laki:
        all_new_edges.extend(edges_omo_add_hammerless_pink_station_laki)

    # Jade Jungle
    if glitch_settings.raph_skip_english:
        all_new_edges.extend(edges_jan_add_raph_skip_english)
    if glitch_settings.raph_skip_parakarry:
        all_new_edges.extend(edges_jan_add_raph_skip_parakarry)
    if glitch_settings.ch5_sushie_glitch:
        all_new_edges.extend(edges_jan_kzn_add_ch5_sushie_glitch)
    if glitch_settings.sushieless_jungle_starpiece_and_letter:
        all_new_edges.extend(edges_jan_add_sushieless_jungle_starpiece_and_letter_lzs)
    if glitch_settings.jumpless_deep_jungle_laki:
        all_new_edges.extend(edges_jan_add_jumpless_deep_jungle_laki)

    # Mt. Lavalava
    if glitch_settings.kooperless_lavalava_pow_block_parakarry:
        all_new_edges.extend(edges_kzn_add_kooperless_pow_block_parakarry)
    if glitch_settings.kooperless_lavalava_pow_block_super_boots:
        all_new_edges.extend(edges_kzn_add_kooperless_pow_block_super_boots)
    if glitch_settings.jumpless_lavalava_pow_block:
        all_new_edges.extend(edges_kzn_add_jumpless_pow_block_kooper)
    if glitch_settings.ultra_hammer_skip:
        all_new_edges.extend(edges_kzn_add_ultra_hammer_skip)
    if glitch_settings.ultra_hammer_skip_laki:
        all_new_edges.extend(edges_kzn_add_ultra_hammer_skip_laki)
    if glitch_settings.ultra_hammer_skip_sushie:
        all_new_edges.extend(edges_kzn_add_ultra_hammer_skip_sushie)
    if glitch_settings.flarakarry:
        all_new_edges.extend(edges_kzn_add_flarakarry_parakarry)
    if glitch_settings.parakarryless_flarakarry_laki:
        all_new_edges.extend(edges_kzn_add_flarakarry_laki)
    if glitch_settings.volcano_sushie_glitch_superboots: # super boots save block storage
        all_new_edges.extend(edges_kzn_add_volcano_sushie_glitch_superboots)
    if glitch_settings.volcano_sushie_glitch_goombario: # tattle save block storage
        all_new_edges.extend(edges_kzn_add_volcano_sushie_glitch_goombario)
    if glitch_settings.volcano_sushie_glitch_superboots or glitch_settings.volcano_sushie_glitch_goombario:
        all_new_edges.extend(edges_kzn_add_volcano_sushie_glitch)

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
    if glitch_settings.bubble_berry_tree_early_laki_jump:
        all_new_edges.extend(edges_flo_add_bubble_berry_tree_early_laki)
    if glitch_settings.bubble_berry_tree_early_ultra_boots:
        all_new_edges.extend(edges_flo_add_bubble_berry_tree_early_ultra_boots)

    # Shiver Region
    if glitch_settings.murder_solved_early_bombette_push:
        all_new_edges.extend(edges_sam_add_murder_solved_early_bombette_push)
    if glitch_settings.murder_solved_early_laki:
        all_new_edges.extend(edges_sam_add_murder_solved_early_laki)
    if glitch_settings.ch7_sushie_glitch:
        all_new_edges.extend(edges_sam_add_ch7_sushie_glitch)
    if glitch_settings.star_stone_with_ch7_sushie_glitch:
        all_new_edges.extend(edges_sam_add_star_stone_with_ch7_sushie_glitch)
    if glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_laki:
        all_new_edges.extend(edges_sam_add_shiver_mountain_hidden_block_laki_throw)
    if glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_no_laki:
        all_new_edges.extend(edges_sam_add_shiver_mountain_hidden_block_normal_throw)
    if glitch_settings.snowmen_skip_laki:
        all_new_edges.extend(edges_sam_add_snowmen_skip_laki)
    if glitch_settings.shiver_mountain_switch_skip:
        all_new_edges.extend(edges_sam_add_shiver_mountain_switch_skip)
    if glitch_settings.sushieless_warehouse_key_bombette:
        all_new_edges.extend(edges_sam_add_sushieless_warehouse_key_bombette_push)
    if glitch_settings.sushieless_warehouse_key_kooper:
        all_new_edges.extend(edges_sam_add_sushieless_warehouse_key_kooper_ksj)

    # Crystal Palace
    if glitch_settings.mirror_clip:
        all_new_edges.extend(edges_pra_add_mirror_clip_laki)
    if glitch_settings.kooper_puzzle_skip:
        all_new_edges.extend(edges_pra_add_kooper_puzzle_skip)

    # Bowser's Castle
    if bowsers_castle_mode == BowserCastleMode.VANILLA:
        if glitch_settings.bowless_bowsers_castle_basement:
            all_new_edges.extend(edges_kpa_add_bowless_bowsers_castle_basement_laki)
        if glitch_settings.fast_flood_room_kooper:
            all_new_edges.extend(edges_kpa_add_fast_flood_room_kooper)
        if glitch_settings.fast_flood_room_bombette_ultra_boots:
            all_new_edges.extend(edges_kpa_add_fast_flood_room_bombette_ultra_boots)
        if glitch_settings.bombetteless_bowsers_castle_basement:
            all_new_edges.extend(edges_kpa_add_bombetteless_bowsers_castle_basement_laki)

    # Global
    if glitch_settings.break_stone_blocks_with_ultra_boots:
        all_new_edges.extend(edges_kmr_tik_isk_add_break_stone_blocks_ultra_boots)
    if glitch_settings.break_yellow_blocks_with_super_boots:
        all_new_edges.extend(edges_kmr_add_break_yellow_blocks_super_boots)
    if glitch_settings.knows_puzzle_solutions:
        all_new_edges.extend(edges_global_knows_puzzle_solutions)
    if glitch_settings.reach_high_blocks_with_super_boots:
        all_new_edges.extend(edges_global_reach_high_blocks_with_super_boots)

    #print(all_new_edges)

    # Modify graph with all pending changes, if any
    if all_new_edges or all_edges_to_remove:
        world_graph, _ = adjust(
            world_graph,
            new_edges=all_new_edges,
            edges_to_remove=all_edges_to_remove
        )

    return world_graph


def adjust_shop_logic(
    world_graph: dict,
    rowf_sets_in_logic:int,
    merlow_in_logic:bool,
    ripcheato_cnt_in_logic:int
):
    if rowf_sets_in_logic < 5:
        world_graph = _set_rowf_out_of_logic(world_graph, rowf_sets_in_logic)
    if not merlow_in_logic:
        world_graph = _set_merlow_out_of_logic(world_graph)

    world_graph = _adjust_rip_cheato_logic(world_graph, ripcheato_cnt_in_logic)

    return world_graph


def _set_rowf_out_of_logic(
    world_graph: dict,
    rowf_sets_in_logic: int
):
    remove_rowf_edges = []
    adjusted_rowf_edges = []

    if rowf_sets_in_logic == 4:
        nodeid_modify = "MAC_01/ShopBadgeK"
        exclude_edge_targets = [
            "ShopBadgeN"
        ]
    elif rowf_sets_in_logic == 3:
        nodeid_modify = "MAC_01/ShopBadgeH"
        exclude_edge_targets = [
            "ShopBadgeK"
        ]
    elif rowf_sets_in_logic == 2:
        nodeid_modify = "MAC_01/ShopBadgeE"
        exclude_edge_targets = [
            "ShopBadgeH"
        ]
    elif rowf_sets_in_logic == 1:
        nodeid_modify = "MAC_01/0"
        exclude_edge_targets = [
            "ShopBadgeE"
        ]
    else: # == 0
        nodeid_modify = "MAC_01/0"
        exclude_edge_targets = [
            "ShopBadgeA",
            "ShopBadgeB",
            "ShopBadgeC",
            "ShopBadgeD",
            "ShopBadgeE",
        ]

    for edge in world_graph[nodeid_modify]["edge_list"]:
        if (    isinstance(edge["to"]["id"], str)
            and any(True for x in exclude_edge_targets
                    if x == edge["to"]["id"]
            )
        ):
            remove_rowf_edges.append(deepcopy(edge))

            out_of_logic_edge = deepcopy(edge)
            out_of_logic_edge["reqs"] = [["RF_OutOfLogic"]]
            adjusted_rowf_edges.append(out_of_logic_edge)

    world_graph, _ = adjust(
        world_graph,
        new_edges=adjusted_rowf_edges,
        edges_to_remove=remove_rowf_edges
    )

    return world_graph


def _set_merlow_out_of_logic(world_graph:dict):
    remove_merlow_edges = []
    adjusted_merlow_edges = []

    for edge in world_graph["HOS_06/0"]["edge_list"]:
        if (    isinstance(edge["to"]["id"], str)
            and edge["to"]["id"] == "ShopRewardA"
        ):
            remove_merlow_edges.append(deepcopy(edge))

            out_of_logic_edge = deepcopy(edge)
            out_of_logic_edge["reqs"] = [["RF_OutOfLogic"]]
            adjusted_merlow_edges.append(out_of_logic_edge)
            break

    world_graph, _ = adjust(
        world_graph,
        new_edges=adjusted_merlow_edges,
        edges_to_remove=remove_merlow_edges
    )

    return world_graph


def _adjust_rip_cheato_logic(world_graph: dict, checks_in_logic:int):
    """
    Returns the modified world graph itself with adjusted item check logic for
    the 11 item checks of Rip Cheato.
    """
    base_cheato_edges = []
    base_cheato_edges.extend([deepcopy(edge) for edge in world_graph["TIK_15/1"]["edge_list"] if isinstance(edge["to"]["id"], str)])
    for x in "ABCDEFGHIJ":
        base_cheato_edges.extend(deepcopy([edge for edge in world_graph[f"TIK_15/Gift{x}"]["edge_list"]]))

    # late checks first to mark out of logic from the back of Cheato's item list
    base_cheato_edges.sort(key=lambda edge: edge["to"]["id"], reverse=True)

    checks_out_of_logic = len(base_cheato_edges) - checks_in_logic

    remove_cheato_edges = []
    adjusted_cheato_edges = []

    adjusted_edges_cnt = 0
    for edge in base_cheato_edges:
        if adjusted_edges_cnt >= checks_out_of_logic:
            break
        remove_cheato_edges.append(edge)
        new_edge = deepcopy(edge)
        new_edge["reqs"] = [["RF_OutOfLogic"]]
        adjusted_cheato_edges.append(new_edge)
        adjusted_edges_cnt += 1

    if adjusted_cheato_edges:
        world_graph, _ = adjust(
            world_graph,
            new_edges=adjusted_cheato_edges,
            edges_to_remove=remove_cheato_edges
        )

    return world_graph


def get_shuffled_battles(
    world_graph: dict,
    boss_shuffle_mode: BossShuffleMode
) -> tuple[dict, list[tuple[int, int]], dict[int, int]]:
    battles_setup, boss_chapter_map = get_boss_battles(boss_shuffle_mode)

    if boss_shuffle_mode != BossShuffleMode.OFF and boss_chapter_map[1] != 1:
        # boss shuffle is active, and Koopa Bros are placed outside of ch. 1:
        # move their battle logic to the other chapter

        boss_requirements: dict = {}
        adjusted_boss_edges: list = []
        remove_boss_edges: list = []

        # gather Koopa Bros boss edge and remove their battle logic
        for edge in world_graph["TRD_10/0"]["edge_list"]:
            if (edge["to"]["map"], edge["to"]["id"]) == ("TRD_10", 0):
                remove_boss_edges.append(deepcopy(edge))
                koopa_bros_requirements = deepcopy(edge["reqs"])

                new_edge = deepcopy(edge)
                new_edge["reqs"] = []
                adjusted_boss_edges.append(new_edge)

                break

        # gather boss edge of the new Koopa Bros location and add their
        # battle logic
        if boss_chapter_map[1] == 2:
            boss_node_id = "ISK_16/0"
            boss_edge_target = "ISK_16/0"
        elif boss_chapter_map[1] == 3:
            boss_node_id = "ARN_11/0"
            boss_edge_target = "ARN_11/0"
        elif boss_chapter_map[1] == 4:
            boss_node_id = "OMO_15/0"
            boss_edge_target = "OMO_15/0"
        elif boss_chapter_map[1] == 5:
            boss_node_id = "KZN_19/1"
            boss_edge_target = "KZN_19/2"
        elif boss_chapter_map[1] == 6:
            boss_node_id = "FLO_21/0"
            boss_edge_target = "FLO_21/0"
        elif boss_chapter_map[1] == 7:
            boss_node_id = "PRA_32/0"
            boss_edge_target = "PRA_32/0"
        else:
            raise ValueError(f"Boss Shuffle has placed no Koopa Bros!: {boss_chapter_map}")

        for edge in world_graph[boss_node_id]["edge_list"]:
            if (f"{edge['to']['map']}/{edge['to']['id']}") == boss_edge_target:
                remove_boss_edges.append(deepcopy(edge))

                new_edge = deepcopy(edge)
                new_edge["reqs"].extend(koopa_bros_requirements)
                adjusted_boss_edges.append(new_edge)

                break

        world_graph, _ = adjust(
            world_graph,
            new_edges=adjusted_boss_edges,
            edges_to_remove=remove_boss_edges
        )


    return world_graph, battles_setup, boss_chapter_map
