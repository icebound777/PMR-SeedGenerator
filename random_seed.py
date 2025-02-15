from copy import deepcopy
import random
import datetime

from metadata.area_name_mappings import area_name_id_map

from rando_enums.enum_options import (
    BowserCastleMode,
    GearShuffleMode,
    PartnerUpgradeShuffle,
    DungeonEntranceShuffle,
)

from itemhints import get_itemhints
from models.CoinPalette import CoinPalette
from models.options.OptionSet import OptionSet
from models.options.LogicOptionSet import LogicOptionSet
from rando_modules.logic import \
    place_items,\
    get_item_spheres,\
    get_items_to_exclude
from rando_modules.random_blocks import get_block_placement
from rando_modules.random_actor_stats import get_shuffled_chapter_difficulty
from rando_modules.modify_entrances import get_shuffled_battles
from rando_modules.modify_entrances import (
    get_shorter_bowsercastle,
    get_bowsercastle_bossrush,
    get_gear_location_shuffle,
    get_partner_upgrade_shuffle,
    get_glitched_logic,
    adjust_shop_logic,
    set_starway_requirements,
    set_starbeam_requirements,
    get_limited_chapter_logic
)
from rando_modules.random_entrances import shuffle_dungeon_entrances
from rando_modules.random_formations import get_random_formations
from rando_modules.random_map_mirroring import get_mirrored_map_list
from rando_modules.random_stat_distribution import generate_random_stats
from rando_modules.random_movecosts import get_randomized_moves
from rando_modules.random_mystery import get_random_mystery
from rando_modules.random_palettes import \
    get_randomized_coinpalette,\
    get_randomized_palettes
from rando_modules.random_audio import get_randomized_audio
from rando_modules.random_partners import get_rnd_starting_partners
from rando_modules.random_puzzles_minigames import get_puzzles_minigames, get_dro_shop_items
from rando_modules.random_quizzes import get_randomized_quizzes
from rando_modules.random_shop_prices import get_shop_price
from rando_modules.unbeatable_seed_error import UnbeatableSeedError
from rando_modules.unbeatable_plando_placement_error import UnbeatablPlandoPlacementError
from rando_modules.plando_settings_mismatch_error import PlandoSettingsMismatchError
from worldgraph import \
    generate as generate_world_graph,\
    check_unreachable_from_start,\
    enrich_graph_data

from rando_enums.enum_ingame import StarSpirits
from metadata.starting_maps import starting_maps
from metadata.starting_items import \
    allowed_starting_badges,\
    allowed_starting_items,\
    allowed_starting_key_items
from metadata.item_general import seed_hash_item_names

from plando_utils.plando_utils import TransformedPlandoData

from db.item import Item

class RandomSeed:
    def __init__(
        self,
        rando_settings: OptionSet,
        seed_value: int = None,
        plando_data: dict = None
    ) -> None:

        self.rando_settings = rando_settings
        self.starting_partners = []
        self.starting_items = []
        self.placed_items = []
        self.placed_blocks = []
        self.entrance_list = []
        self.enemy_stats = []
        self.battles = []
        self.chapter_changes = {}
        self.battle_formations = []
        self.move_costs = []
        self.coin_palette:CoinPalette = CoinPalette()
        self.palette_data = []
        self.static_map_mirroring = []
        self.quiz_list = []
        self.music_list = []
        self.puzzle_minigame_data = []
        self.item_spheres_dict = None
        self.spoilerlog_additions = {}
        self.plando_data: TransformedPlandoData = TransformedPlandoData(
            plando_data
        )

        if seed_value is None:
            self.seed_value = random.randint(0, 0xFFFFFFFF)
        else:
            self.seed_value = seed_value

        self.rando_settings.plando_active = self.plando_data.plando_active


    def generate(self, world_graph = None):

        print(f"Seed: {self.seed_value}")
        random.seed(self.seed_value)

        # Prepare world graph if not provided
        if world_graph is None:
            print("Generating World Graph ...")
            world_graph = generate_world_graph(None, None)

        # Generation attempt
        for placement_attempt in range(1, 11):  # try 10 times
            try:
                modified_world_graph = deepcopy(world_graph)
                self.placed_items = []
                self.entrance_list = []
                self.placed_blocks = []
                self.battles = []
                self.spoilerlog_additions = {}
                self.item_spheres_dict = None
                dc_rando_settings = deepcopy(self.rando_settings)
                logic_settings = dc_rando_settings.logic_settings

                # Choose values for options that are set to "random"
                if logic_settings.magical_seeds_required == -1:
                    logic_settings.magical_seeds_required = random.randint(
                        self.plando_data.magical_seeds_count,
                        4
                    )
                elif self.plando_data.magical_seeds_count > logic_settings.magical_seeds_required:
                    logic_settings.magical_seeds_required = self.plando_data.magical_seeds_count

                if logic_settings.starway_spirits_needed_count == -1:
                    # note: don't roll zero here
                    logic_settings.starway_spirits_needed_count = random.randint(1, 7)

                if logic_settings.starbeam_spirits_needed == -1:
                    # note: don't roll zero here
                    logic_settings.starbeam_spirits_needed = random.randint(1, 7)

                if logic_settings.star_hunt_total == -1:
                    min_total_stars = max([
                        logic_settings.starway_powerstars_needed,
                        logic_settings.starbeam_powerstars_needed,
                    ])
                    if min_total_stars == -1:
                        min_total_stars = 1
                    logic_settings.star_hunt_total = random.randint(
                        min_total_stars,
                        120
                    )
                if logic_settings.star_hunt_total == 0:
                    logic_settings.starway_powerstars_needed = 0
                elif logic_settings.starway_powerstars_needed == -1:
                    logic_settings.starway_powerstars_needed = random.randint(
                        1,
                        logic_settings.star_hunt_total
                    )
                if logic_settings.star_hunt_total == 0:
                    logic_settings.starbeam_powerstars_needed = 0
                elif logic_settings.starbeam_powerstars_needed == -1:
                    logic_settings.starbeam_powerstars_needed = random.randint(
                        int(logic_settings.starway_powerstars_needed * 0.7) + 1,
                        logic_settings.star_hunt_total
                    )

                # Unset settings that become meaningless due to other settings
                if logic_settings.starway_spirits_needed_count in [0, 7]:
                    logic_settings.require_specific_spirits = False
                    logic_settings.limit_chapter_logic = False

                # Select required star spirits
                chosen_spirits = []
                all_spirits = [
                    StarSpirits.ELDSTAR,
                    StarSpirits.MAMAR,
                    StarSpirits.SKOLAR,
                    StarSpirits.MUSKULAR,
                    StarSpirits.MISSTAR,
                    StarSpirits.KLEVAR,
                    StarSpirits.KALMAR,
                ]
                plando_required_spirits: list[int] | None = self.plando_data.required_spirits
                if (    logic_settings.require_specific_spirits
                    and 0 < logic_settings.starway_spirits_needed_count < 7
                    and (plando_required_spirits is None or len(plando_required_spirits) < 7)
                ):
                    # Set spirits
                    if plando_required_spirits is not None:
                        chosen_spirits.extend(plando_required_spirits)
                    if len(chosen_spirits) < logic_settings.starway_spirits_needed_count:
                        all_spirits = list(set(all_spirits) - set(chosen_spirits))
                        for _ in range(logic_settings.starway_spirits_needed_count - len(chosen_spirits)):
                            rnd_spirit = random.randint(0, len(all_spirits) - 1)
                            chosen_spirits.append(all_spirits.pop(rnd_spirit))
                    # Encode set spirits
                    encoded_spirits = 0
                    for spirit in chosen_spirits:
                        encoded_spirits = encoded_spirits | (1 << (spirit - 1))
                    logic_settings.starway_spirits_needed_encoded = encoded_spirits

                    chosen_spirits.sort()
                    if self.spoilerlog_additions.get("required_spirits") is None:
                        self.spoilerlog_additions["required_spirits"] = []
                    self.spoilerlog_additions["required_spirits"].extend(chosen_spirits)

                # Modify entrances if needed
                entrance_changes = []
                if logic_settings.bowsers_castle_mode == BowserCastleMode.SHORTEN:
                    entrance_changes, modified_world_graph = get_shorter_bowsercastle(
                        modified_world_graph
                    )
                elif logic_settings.bowsers_castle_mode == BowserCastleMode.BOSSRUSH:
                    entrance_changes, modified_world_graph = get_bowsercastle_bossrush(
                        modified_world_graph
                    )
                if entrance_changes:
                    self.extend_entrances(entrance_changes)

                if (    logic_settings.shuffle_dungeon_entrances
                    and logic_settings.shuffle_items
                ):
                    entrance_changes, modified_world_graph, spoilerlog_info = shuffle_dungeon_entrances(
                        world_graph = modified_world_graph,
                        starway_spirits_needed_count = logic_settings.starway_spirits_needed_count,
                        required_star_spirits = chosen_spirits,
                        limit_chapter_logic = logic_settings.limit_chapter_logic,
                        shuffle_bowsers_castle = (
                            logic_settings.shuffle_dungeon_entrances == DungeonEntranceShuffle.INCLUDE_BOWSERSCASTLE
                        ),
                        write_spoilers = dc_rando_settings.write_spoilerlog,
                    )
                    self.extend_entrances(entrance_changes)
                    if self.spoilerlog_additions.get("entrances") is None:
                        self.spoilerlog_additions["entrances"] = []
                    self.spoilerlog_additions["entrances"].extend(spoilerlog_info)

                # Set up partner upgrade shuffle if needed
                if logic_settings.partner_upgrade_shuffle != PartnerUpgradeShuffle.OFF:
                    modified_world_graph, self.placed_blocks = get_partner_upgrade_shuffle(
                        modified_world_graph,
                        logic_settings.shuffle_blocks,
                        dc_rando_settings.glitch_settings
                    )

                # Adjust graph logic if needed
                if logic_settings.gear_shuffle_mode != GearShuffleMode.VANILLA:
                    modified_world_graph = get_gear_location_shuffle(
                        modified_world_graph,
                        logic_settings.gear_shuffle_mode
                    )

                modified_world_graph = adjust_shop_logic(
                    modified_world_graph,
                    logic_settings.progression_on_rowf,
                    logic_settings.progression_on_merlow,
                    logic_settings.ripcheato_items_in_logic
                )

                # Randomize battles if needed
                modified_world_graph, self.battles, chapter_boss_map = get_shuffled_battles(
                    modified_world_graph,
                    logic_settings.boss_shuffle_mode,
                    self.plando_data.boss_battles,
                )
                self.spoilerlog_additions["boss_battles"] = chapter_boss_map

                # Set up trick & glitch logic
                modified_world_graph = get_glitched_logic(
                    modified_world_graph,
                    dc_rando_settings.glitch_settings,
                    logic_settings.bowsers_castle_mode,
                    logic_settings.shuffle_dungeon_entrances
                )

                ## Setup star spirits, power stars, and relevant logic
                if (   logic_settings.starbeam_spirits_needed > 0
                    or logic_settings.starbeam_powerstars_needed > 0
                ):
                    modified_world_graph = set_starbeam_requirements(
                        world_graph=modified_world_graph,
                        spirits_needed=logic_settings.starbeam_spirits_needed,
                        powerstars_needed=logic_settings.starbeam_powerstars_needed
                    )

                entrance_changes, modified_world_graph = set_starway_requirements(
                    world_graph=modified_world_graph,
                    spirits_needed=logic_settings.starway_spirits_needed_count,
                    specific_spirits=chosen_spirits,
                    powerstars_needed=( # don't expect all, but also don't bottleneck
                        logic_settings.star_hunt_total
                      - int(  (  logic_settings.star_hunt_total
                               - logic_settings.starway_powerstars_needed
                              )
                            / 2
                        )
                    ),
                    seed_goal=logic_settings.seed_goal
                )
                if entrance_changes:
                    self.extend_entrances(entrance_changes)

                if logic_settings.limit_chapter_logic:
                    modified_world_graph = get_limited_chapter_logic(
                        modified_world_graph,
                        chosen_spirits,
                        logic_settings.gear_shuffle_mode
                    )

                # Cull unneeded data from world graph if access to maps was
                # removed
                unreachable_node_ids = check_unreachable_from_start(
                    modified_world_graph,
                    False
                )
                for node_id in unreachable_node_ids:
                    modified_world_graph.pop(node_id)

                modified_world_graph = enrich_graph_data(modified_world_graph)

                # Adjust further settings
                hidden_block_mode = logic_settings.hidden_block_mode
                if dc_rando_settings.glitch_settings.knows_hidden_blocks:
                    # Having this trick enabled is equivalent to mode 3, logic wise
                    hidden_block_mode = 3

                starting_chapter, logic_settings.starting_map = self.init_starting_map(
                    dc_rando_settings
                )
                self.init_starting_partners(
                    logic_settings,
                    self.plando_data.partners_placed,
                )

                self.init_starting_items(
                    dc_rando_settings,
                    self.plando_data.keyitems_placed,
                    self.plando_data.badges_placed,
                )

                # Item Placement
                place_items(
                    item_placement=self.placed_items,
                    logic_settings=logic_settings,
                    starting_partners=self.starting_partners,
                    hidden_block_mode=hidden_block_mode,
                    starting_items=[x for x in self.starting_items if x.item_type != "ITEM"],
                    plando_item_placeholders=self.plando_data.item_placeholders,
                    plando_trap_placeholders=self.plando_data.trap_placeholders,
                    world_graph=modified_world_graph,
                    plando_item_placement=self.plando_data.item_placement,
                    plando_traps_placed=self.plando_data.trap_count,
                    is_progression_plandod = (len(self.plando_data.keyitems_placed) > 0),
                )

                # Determine item placement spheres
                self.item_spheres_dict = get_item_spheres(
                    item_placement= self.placed_items,
                    logic_settings = logic_settings,
                    starting_partners=self.starting_partners,
                    hidden_block_mode=hidden_block_mode,
                    starting_items=[x for x in self.starting_items if x.item_type != "ITEM"],
                    world_graph=modified_world_graph,
                )

                self.rando_settings = dc_rando_settings
                logic_settings = self.rando_settings.logic_settings

                break

            except UnbeatablPlandoPlacementError:
                # Item placement in plandomizer prohibits logical seed
                # completion, so just raise w/o trying 10 times
                raise
            except PlandoSettingsMismatchError:
                # Item placement in plandomizer clashes with chosen settings,
                # so just raise w/o trying 10 times
                raise
            except UnbeatableSeedError:
                print(f"Failed to place items! Fail count: {placement_attempt}")
                if placement_attempt == 10:
                    raise
            except AssertionError:
                print(f"Failed to build beatable world! Fail count: {placement_attempt}")
                if placement_attempt == 10:
                    raise

        # Write ingame hint area for star beam, if shuffled
        if logic_settings.shuffle_starbeam:
            for node_id in modified_world_graph:
                cur_node = modified_world_graph[node_id].get("node")
                if (    cur_node # check for edge_index
                    and cur_node.current_item
                    and cur_node.current_item.item_name == "StarBeam"
                ):
                    if cur_node.map_area.area_id == area_name_id_map["OSR"]:
                        # Either Muss T. or the hidden block in front of the
                        # Peach's Castle entrance. Let's rebind those to
                        # Toad Town and Peach's Castle respectively
                        if cur_node.map_area.map_id == 1:
                            logic_settings.starbeam_location = area_name_id_map["MAC"]
                        else:
                            logic_settings.starbeam_location = area_name_id_map["KKJ"]
                    else:
                        logic_settings.starbeam_location = cur_node.map_area.area_id
                    break

        # Setup puzzles and minigames
        # (have to set up the Dry Dry Outpost shop puzzles before item prices
        # get adjusted)
        self.puzzle_minigame_data, spoilerlog_info = get_puzzles_minigames(
            logic_settings.randomize_puzzles,
            get_dro_shop_items(modified_world_graph)
        )
        self.spoilerlog_additions["puzzle_solutions"] = spoilerlog_info

        # Adjust item pricing
        for node in self.placed_items:
            if "Shop" in node.identifier:
                node.current_item.base_price = get_shop_price(
                    node,
                    logic_settings.include_shops,
                    self.rando_settings.merlow_reward_pricing,
                    logic_settings.star_hunt_total,
                    self.plando_data.shop_prices,
                )

        # Modify Mystery? item
        self.rando_settings.mystery_settings = get_random_mystery(
            self.rando_settings.mystery_settings
        )

        # Randomize blocks if needed and not already done logically
        if not self.placed_blocks:
            self.placed_blocks = get_block_placement(
                logic_settings.shuffle_blocks,
                supers_are_yellow=False
            )

        # Randomize stat distribution if needed
        if self.rando_settings.random_starting_stats_level >= 0:
            self.rando_settings.starting_level, \
            self.rando_settings.starting_maxhp, \
            self.rando_settings.starting_maxfp, \
            self.rando_settings.starting_maxbp = generate_random_stats(
                self.rando_settings.random_starting_stats_level
            )

        # Randomize chapter difficulty / enemy stats if needed
        self.enemy_stats, self.chapter_changes = get_shuffled_chapter_difficulty(
            self.rando_settings.shuffle_chapter_difficulty,
            chapter_boss_map,
            self.rando_settings.progressive_scaling,
            starting_chapter,
            self.plando_data.difficulty,
        )

        # Randomize enemy battle formations
        if (   self.rando_settings.random_formations
            or self.rando_settings.progressive_scaling
        ):
            self.battle_formations = get_random_formations(
                self.chapter_changes,
                self.rando_settings.progressive_scaling
            )

        # Randomize move costs (FP/BP) if needed
        self.move_costs = get_randomized_moves(
            self.rando_settings.random_badges_bp,
            self.rando_settings.random_badges_fp,
            self.rando_settings.random_partner_fp,
            self.rando_settings.random_starpower_sp,
            self.plando_data.move_costs,
        )

        # Build item hint db
        self.itemhints = get_itemhints(
            self.rando_settings.allow_itemhints,
            self.placed_items,
            self.starting_partners,
            logic_settings.partner_shuffle,
            logic_settings.include_shops,
            logic_settings.include_panels,
            logic_settings.include_favors_mode,
            logic_settings.include_letters_mode,
            logic_settings.keyitems_outside_dungeon,
        )

        # Random quiz
        if self.rando_settings.random_quiz:
            self.quiz_list = get_randomized_quizzes()

        # Randomize sprite palettes
        (
            self.coin_palette,
            self.rando_settings.coin_color
        ) = get_randomized_coinpalette(
            color_id = self.rando_settings.coin_color,
            should_randomize_color = self.rando_settings.random_coin_color
        )
        self.palette_data = get_randomized_palettes(
            self.rando_settings.palette_settings
        )

        # Randomize map mirroring
        if self.rando_settings.static_mirroring:
            self.static_map_mirroring = get_mirrored_map_list()

        # Music settings
        self.music_list = get_randomized_audio(
            randomize_bgm=self.rando_settings.shuffle_music,
            randomize_by=self.rando_settings.shuffle_music_mode,
            randomize_jingles=self.rando_settings.shuffle_jingles
        )

        # Set up seed hash for the save select screen
        self.set_seed_hash()


    def init_starting_partners(
        self,
        logic_settings:LogicOptionSet,
        plandod_partners: list[str],
    ):
        # Choose random starting partners if necessary
        if logic_settings.random_partners:
            self.starting_partners = get_rnd_starting_partners(
                num_rnd_partners_min=logic_settings.random_partners_min,
                num_rnd_partners_max=logic_settings.random_partners_max,
                logic_settings=logic_settings,
                plandod_partners=plandod_partners,
            )
        else:
            if (any([
                    True for x in logic_settings.starting_partners
                    if x in plandod_partners
                ])
            ):
                raise ValueError(
                    "ERROR: Chosen starting partners: Cannot start the seed with "\
                    "these partners, because one or more of them is already "\
                    "placed by the plandomizer!"
                )
            self.starting_partners = logic_settings.starting_partners


    def init_starting_map(
        self,
        rando_settings:OptionSet
    ):
        """
        Initializes the starting map and returns its chapter number. If the
        starting map is to be chosen at random, pick from curated list.
        """
        starting_map_value = rando_settings.logic_settings.starting_map
        start_chapter = None
        if starting_map_value == 0xFFFFFFFF:
            # Pick random starting location
            start_chapter = random.choice(list(starting_maps.keys()))
            starting_map_value = starting_maps[start_chapter]
        else:
            # Attempt to detect starting chapter value
            for chapter_number, start_location in starting_maps.items():
                if starting_map_value == start_location:
                    start_chapter = chapter_number
                    break
            else:
                start_chapter = 0

        return start_chapter, starting_map_value


    def init_starting_items(
        self,
        rando_settings:OptionSet,
        plando_keyitems: list[str],
        plando_badges: list[str],
    ):
        """
        Initialize the starting items from either the chosen starting items or
        pick them randomly.
        """
        self.starting_items = []
        if rando_settings.logic_settings.random_starting_items:
            starting_item_options = [0 for _ in range(16)]

            # Set up allowed items
            all_allowed_starting_items = []
            all_allowed_starting_items.extend(allowed_starting_badges)
            all_allowed_starting_items.extend(allowed_starting_items)
            all_allowed_starting_items.extend(allowed_starting_key_items)

            # Exclude items that are already placed by the plandomizer
            for keyitem_str in plando_keyitems:
                keyitem_obj = Item.get(Item.item_name == keyitem_str)
                if keyitem_obj.value in all_allowed_starting_items:
                    all_allowed_starting_items.remove(keyitem_obj.value)
            for badge_str in plando_badges:
                badge_obj = Item.get(Item.item_name == badge_str)
                if badge_obj.value in all_allowed_starting_items:
                    all_allowed_starting_items.remove(badge_obj.value)

            excluded_items = get_items_to_exclude(
                logic_settings=rando_settings.logic_settings,
                starting_partners=self.starting_partners,
                do_partner_upgrade_shuffle=(rando_settings.logic_settings.partner_upgrade_shuffle != PartnerUpgradeShuffle.OFF)
            )
            for item_obj in excluded_items:
                if item_obj.value in all_allowed_starting_items:
                    all_allowed_starting_items.remove(item_obj.value)

            starting_items_amount = random.randint(
                rando_settings.logic_settings.random_starting_items_min,
                rando_settings.logic_settings.random_starting_items_max
            )

            for i in range(starting_items_amount):
                random_item_id = random.choice(all_allowed_starting_items)
                random_item_obj = Item.get_or_none(Item.value == random_item_id)
                if random_item_obj is not None:
                    # No double uniques
                    if (    random_item_obj.item_type in ["BADGE", "KEYITEM", "STARPIECE"]
                        and random_item_obj in self.starting_items
                    ):
                        continue

                    self.starting_items.append(random_item_obj)
                    starting_item_options[i] = random_item_id

            rando_settings.logic_settings.starting_item_0 = starting_item_options[0]
            rando_settings.logic_settings.starting_item_1 = starting_item_options[1]
            rando_settings.logic_settings.starting_item_2 = starting_item_options[2]
            rando_settings.logic_settings.starting_item_3 = starting_item_options[3]
            rando_settings.logic_settings.starting_item_4 = starting_item_options[4]
            rando_settings.logic_settings.starting_item_5 = starting_item_options[5]
            rando_settings.logic_settings.starting_item_6 = starting_item_options[6]
            rando_settings.logic_settings.starting_item_7 = starting_item_options[7]
            rando_settings.logic_settings.starting_item_8 = starting_item_options[8]
            rando_settings.logic_settings.starting_item_9 = starting_item_options[9]
            rando_settings.logic_settings.starting_item_A = starting_item_options[10]
            rando_settings.logic_settings.starting_item_B = starting_item_options[11]
            rando_settings.logic_settings.starting_item_C = starting_item_options[12]
            rando_settings.logic_settings.starting_item_D = starting_item_options[13]
            rando_settings.logic_settings.starting_item_E = starting_item_options[14]
            rando_settings.logic_settings.starting_item_F = starting_item_options[15]
        else:
            if (any([
                    True for x in self.rando_settings.get_startitem_list()
                    if x.item_name in plando_keyitems or x.item_name in plando_badges
                ])
            ):
                raise ValueError(
                    "ERROR: Chosen starting items: Cannot start the seed with "\
                    "these items, because one or more of them are already "\
                    "placed by the plandomizer!"
                )
            self.starting_items = self.rando_settings.get_startitem_list()


    def extend_entrances(
        self,
        entrance_changes: list[tuple[int, int]]
    ) -> None:
        """
        Extends the seed's entrance modifications.
        If entrance randomization, or static entrance changes like Shorten BC,
        results in modifying the same entrance multiple times, then we have
        to handle these changes in a specific way.
        While the worldgraph can handle modification of this kind, the new
        entrance links to be written to the ROM cannot resolve these entrance
        link chains themselves.
        Here we have to check for entrances getting modified multiple times
        and adjust the links accordingly.
        Example:
            in vanilla, LZ 1 leads to Entrance A.
            We now re-link this connection, so LZ 1 leads to Entrance B.
                (this writes "EntranceA: EntranceB" to the ROM, as in
                "anything that, in vanilla, goes to EntranceA now goes to
                EntranceB")
            We now re-link this connection again, so LZ 1 leads to Entrance C.
                (this writes "EntranceB: EntranceC" to the ROM)
            However, "EntranceB: EntranceC" is wrong as far as the ROM is
            concerned, and the only entrance link written to ROM
            should be "EntranceA: EntranceC", because the ROM cannot resolve
            entrance link chains.
        """
        if len(self.entrance_list) == 0:
            self.entrance_list.extend(entrance_changes)
        else:
            chain_extensions: dict[int, tuple[int, int]] = {}
            new_changes: list[tuple[int, int]] = []

            # iterate over all new entrance changes:
            # if they want to modify an entrance that has not been modified
            # before, then we just add them to the list of changes.
            # if they want to modify an entrance that has already been
            # re-linked, then we have to resolve such a link chain by changing
            # the existing entrance link, instead of adding to the link list.
            for tup in entrance_changes:
                found_existing_link: bool = False
                for i, entrance_change_tup in enumerate(self.entrance_list):
                    if tup[0] & 0xFFFFFF == entrance_change_tup[1]:
                        chain_extensions[i] = tup
                        found_existing_link = True
                        break
                if not found_existing_link:
                    new_changes.append(tup)

            for entrance_index, extension_tup in chain_extensions.items():
                self.entrance_list[entrance_index] = (
                    self.entrance_list[entrance_index][0], extension_tup[1]
                )
            self.entrance_list.extend(new_changes)


    def set_seed_hash(self) -> tuple():
        """
        Randomly selects 4 items and their indices for displaying an item icon
        hash representing the seeded game on the save select screen.
        NOTE: This function resets the internally used random seeding, so
        after calling this don't do other seed dependent calls to the random
        module anymore!
        """
        random.seed()

        seed_hash = 0
        seed_hash_items = []

        for i in range(4):
            random_index = random.randint(0, 0xFF)
            seed_hash = seed_hash + (random_index << (8 * i))

            hash_item_name = seed_hash_item_names[random_index]
            seed_hash_items.append(hash_item_name)

        seed_hash_items.reverse()

        self.seed_hash = seed_hash
        self.seed_hash_items = seed_hash_items
