from copy import deepcopy
import random
import datetime

from rando_enums.enum_options import BowserCastleMode, GearShuffleMode

from itemhints import get_itemhints
from models.CoinPalette import CoinPalette
from optionset import OptionSet
from rando_modules.logic import \
    place_items,\
    get_item_spheres,\
    get_items_to_exclude
from rando_modules.random_blocks import get_block_placement
from rando_modules.random_actor_stats import get_shuffled_chapter_difficulty
from rando_modules.modify_entrances import \
    get_shorter_bowsercastle,\
    get_bowsercastle_bossrush,\
    get_gear_location_shuffle,\
    get_starhunt,\
    get_glitched_logic,\
    adjust_shop_logic
from rando_modules.random_entrances import shuffle_dungeon_entrances
from rando_modules.random_formations import get_random_formations
from rando_modules.random_movecosts import get_randomized_moves
from rando_modules.random_mystery import get_random_mystery
from rando_modules.random_palettes import \
    get_randomized_coinpalette,\
    get_randomized_palettes
from rando_modules.random_audio import get_randomized_audio
from rando_modules.random_partners import get_rnd_starting_partners
from rando_modules.random_quizzes import get_randomized_quizzes
from rando_modules.random_shop_prices import get_shop_price
from rando_modules.unbeatable_seed_error import UnbeatableSeedError
from worldgraph import \
    generate as generate_world_graph,\
    check_unreachable_from_start,\
    enrich_graph_data

from metadata.starting_maps import starting_maps
from metadata.starting_items import \
    allowed_starting_badges,\
    allowed_starting_items,\
    allowed_starting_key_items
from metadata.item_general import seed_hash_item_names

from db.item import Item

class RandomSeed:
    def __init__(self, rando_settings: OptionSet, seed_value=None) -> None:

        self.rando_settings = rando_settings
        self.starting_partners = []
        self.starting_items = []
        self.placed_items = []
        self.placed_blocks = []
        self.entrance_list = []
        self.enemy_stats = []
        self.chapter_changes = {}
        self.battle_formations = []
        self.move_costs = []
        self.coin_palette:CoinPalette = CoinPalette()
        self.palette_data = []
        self.quiz_list = []
        self.music_list = []
        self.item_spheres_dict = None
        self.spoilerlog_additions = {}

        if seed_value is None:
            self.seed_value = random.randint(0, 0xFFFFFFFF)
        else:
            self.seed_value = seed_value


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
                self.entrance_list = []
                self.spoilerlog_additions = {}

                # Modify entrances if needed
                maps_removed = False
                if self.rando_settings.bowsers_castle_mode["value"] == BowserCastleMode.SHORTEN:
                    self.entrance_list, modified_world_graph = get_shorter_bowsercastle(modified_world_graph)
                    maps_removed = True
                elif self.rando_settings.bowsers_castle_mode["value"] == BowserCastleMode.BOSSRUSH:
                    self.entrance_list, modified_world_graph = get_bowsercastle_bossrush(modified_world_graph)
                    maps_removed = True

                if self.rando_settings.star_hunt["value"]:
                    entrance_changes, modified_world_graph = get_starhunt(
                        modified_world_graph,
                        #self.rando_settings.star_hunt_required["value"],
                        self.rando_settings.star_hunt_total["value"],
                        self.rando_settings.star_hunt_ends_game["value"]
                    )
                    self.entrance_list.extend(entrance_changes)
                    if self.rando_settings.star_hunt_ends_game["value"]:
                        maps_removed = True

                if (    self.rando_settings.shuffle_dungeon_entrances["value"]
                    and self.rando_settings.shuffle_items["value"]
                ):
                    entrance_changes, modified_world_graph, spoilerlog_info = shuffle_dungeon_entrances(
                        modified_world_graph,
                        self.rando_settings.starway_spirits_needed_count["value"],
                        False,
                        self.rando_settings.write_spoilerlog
                    )
                    self.entrance_list.extend(entrance_changes)
                    if self.spoilerlog_additions.get("entrances") is None:
                        self.spoilerlog_additions["entrances"] = []
                    self.spoilerlog_additions["entrances"].extend(spoilerlog_info)

                # Cull unneeded data from world graph if access to maps was
                # removed
                if maps_removed:
                    unreachable_node_ids = check_unreachable_from_start(
                        modified_world_graph,
                        False
                    )
                    for node_id in unreachable_node_ids:
                        modified_world_graph.pop(node_id)

                # Adjust graph logic if needed
                if self.rando_settings.gear_shuffle_mode["value"] != GearShuffleMode.VANILLA:
                    modified_world_graph = get_gear_location_shuffle(
                        modified_world_graph,
                        self.rando_settings.gear_shuffle_mode["value"]
                    )
                modified_world_graph = adjust_shop_logic(
                    modified_world_graph,
                    self.rando_settings.progression_on_rowf,
                    self.rando_settings.progression_on_merlow,
                    self.rando_settings.ripcheato_items_in_logic
                )
                modified_world_graph = get_glitched_logic(
                    modified_world_graph,
                    self.rando_settings.glitch_settings,
                    self.rando_settings.bowsers_castle_mode["value"],
                    self.rando_settings.shuffle_dungeon_entrances["value"]
                )

                modified_world_graph = enrich_graph_data(modified_world_graph)

                # Adjust further settings
                hidden_block_mode = self.rando_settings.hidden_block_mode["value"]
                if self.rando_settings.glitch_settings.knows_hidden_blocks["value"]:
                    hidden_block_mode = 3 # Having this trick enabled is equivalent to mode 3, logic wise

                if self.rando_settings.starway_spirits_needed_count["value"] == -1:
                    self.rando_settings.starway_spirits_needed_count["value"] = random.randint(0,7)

                starting_chapter, starting_map_value = self.init_starting_map(self.rando_settings)
                self.init_starting_partners(self.rando_settings)

                # Pick seeds required for flower gate, if random
                if self.rando_settings.magical_seeds_required["value"] == 5:
                    magical_seeds_required = random.randint(0, 4)
                else:
                    magical_seeds_required = self.rando_settings.magical_seeds_required["value"]

                self.init_starting_items(
                    self.rando_settings,
                    magical_seeds_required
                )

                modified_world_graph_copy = deepcopy(modified_world_graph)

                # Item Placement
                place_items(
                    item_placement= self.placed_items,
                    do_custom_seed=self.rando_settings.custom_seed,
                    do_shuffle_items=self.rando_settings.shuffle_items["value"],
                    shuffle_overworld_coins=self.rando_settings.include_coins_overworld,
                    shuffle_block_coins=self.rando_settings.include_coins_blocks,
                    shuffle_foliage_coins=self.rando_settings.include_coins_foliage,
                    shuffle_favor_coins=self.rando_settings.include_coins_favors,
                    do_randomize_shops=self.rando_settings.include_shops["value"],
                    do_randomize_panels=self.rando_settings.include_panels["value"],
                    randomize_favors_mode=self.rando_settings.include_favors_mode,
                    randomize_letters_mode=self.rando_settings.include_letters_mode,
                    do_randomize_radiotrade=self.rando_settings.include_radiotradeevent,
                    do_randomize_dojo=self.rando_settings.include_dojo,
                    gear_shuffle_mode=self.rando_settings.gear_shuffle_mode["value"],
                    randomize_consumable_mode=self.rando_settings.randomize_consumable_mode,
                    item_quality=self.rando_settings.item_quality,
                    itemtrap_mode=self.rando_settings.itemtrap_mode,
                    starting_map_id=starting_map_value,
                    startwith_prologue_open=self.rando_settings.prologue_open["value"],
                    startwith_bluehouse_open=self.rando_settings.bluehouse_open["value"],
                    startwith_mtrugged_open=self.rando_settings.mtrugged_open["value"],
                    magical_seeds_required=magical_seeds_required,
                    startwith_toybox_open=self.rando_settings.toybox_open["value"],
                    startwith_whale_open=self.rando_settings.whale_open["value"],
                    ch7_bridge_visible=self.rando_settings.ch7_bridge_visible["value"],
                    cook_without_fryingpan=self.rando_settings.cook_without_fryingpan["value"],
                    starting_partners=self.starting_partners,
                    starting_boots=self.rando_settings.starting_boots["value"],
                    starting_hammer=self.rando_settings.starting_hammer["value"],
                    speedyspin=self.rando_settings.always_speedyspin["value"],
                    ispy=self.rando_settings.always_ispy["value"],
                    peekaboo=self.rando_settings.always_peekaboo["value"],
                    partners_always_usable=self.rando_settings.partners_always_usable["value"],
                    partners_in_default_locations=self.rando_settings.partners_in_default_locations,
                    hidden_block_mode=hidden_block_mode,
                    keyitems_outside_dungeon=self.rando_settings.keyitems_outside_dungeon,
                    starting_items=[x for x in self.starting_items if x.item_type != "ITEM"],
                    add_item_pouches=self.rando_settings.add_item_pouches,
                    bowsers_castle_mode=self.rando_settings.bowsers_castle_mode["value"],
                    star_hunt_stars=self.rando_settings.star_hunt_total["value"] if self.rando_settings.star_hunt["value"] else 0,
                    world_graph=modified_world_graph_copy
                )

                self.rando_settings.starting_map["value"] = starting_map_value # Overwrite starting map in case it was random at first
                self.rando_settings.magical_seeds_required["value"] = magical_seeds_required
                break

            except UnbeatableSeedError as err:
                print(f"Failed to place items! Fail count: {placement_attempt}")

        # Adjust item pricing
        for node in self.placed_items:
            if "Shop" in node.identifier:
                node.current_item.base_price = get_shop_price(
                    node,
                    self.rando_settings.include_shops["value"],
                    self.rando_settings.merlow_reward_pricing
                )

        # Modify Mystery? item
        self.rando_settings.mystery_settings = get_random_mystery(
            self.rando_settings.mystery_settings
        )

        # Make everything inexpensive
        #set_cheap_shopitems(placed_items)
        #self.placed_items = get_alpha_prices(self.placed_items)

        # Randomize blocks if needed
        self.placed_blocks = get_block_placement(
            self.rando_settings.shuffle_blocks
        )

        # Randomize chapter difficulty / enemy stats if needed
        self.enemy_stats, self.chapter_changes = get_shuffled_chapter_difficulty(
            self.rando_settings.shuffle_chapter_difficulty,
            self.rando_settings.progressive_scaling.get("value"),
            starting_chapter
        )

        # Randomize enemy battle formations
        if (   self.rando_settings.random_formations["value"]
            or self.rando_settings.progressive_scaling["value"]
        ):
            self.battle_formations = get_random_formations(
                self.chapter_changes,
                self.rando_settings.progressive_scaling["value"]
            )

        # Randomize move costs (FP/BP) if needed
        self.move_costs = get_randomized_moves(
            self.rando_settings.random_badges_bp,
            self.rando_settings.random_badges_fp,
            self.rando_settings.random_partner_fp,
            self.rando_settings.random_starpower_sp
        )

        # Build item hint db
        self.itemhints = get_itemhints(
            self.rando_settings.allow_itemhints,
            self.placed_items,
            self.starting_partners,
            self.rando_settings.partners_in_default_locations,
            self.rando_settings.include_shops["value"],
            self.rando_settings.include_panels["value"],
            self.rando_settings.include_favors_mode,
            self.rando_settings.include_letters_mode,
            self.rando_settings.keyitems_outside_dungeon
        )

        # Random quiz
        if self.rando_settings.random_quiz["value"]:
            self.quiz_list = get_randomized_quizzes()

        # Randomize sprite palettes
        (self.coin_palette,
         self.rando_settings.coin_color["value"]
        ) = get_randomized_coinpalette(
            color_id = self.rando_settings.coin_color["value"],
            should_randomize_color = self.rando_settings.random_coin_color
        )
        self.palette_data = get_randomized_palettes(
            self.rando_settings.palette_settings
        )

        # Music settings
        self.music_list = get_randomized_audio(
            randomize_bgm=self.rando_settings.shuffle_music,
            randomize_by=self.rando_settings.shuffle_music_mode,
            randomize_jingles=self.rando_settings.shuffle_jingles
        )

        # Determine item placement spheres
        self.item_spheres_dict = get_item_spheres(
            item_placement= self.placed_items,
            starting_map_id=self.rando_settings.starting_map["value"],
            startwith_prologue_open=self.rando_settings.prologue_open["value"],
            startwith_bluehouse_open=self.rando_settings.bluehouse_open["value"],
            startwith_mtrugged_open=self.rando_settings.mtrugged_open["value"],
            magical_seeds_required=self.rando_settings.magical_seeds_required["value"],
            startwith_toybox_open=self.rando_settings.toybox_open["value"],
            startwith_whale_open=self.rando_settings.whale_open["value"],
            ch7_bridge_visible=self.rando_settings.ch7_bridge_visible["value"],
            cook_without_fryingpan=self.rando_settings.cook_without_fryingpan["value"],
            starting_partners=self.starting_partners,
            starting_boots=self.rando_settings.starting_boots["value"],
            starting_hammer=self.rando_settings.starting_hammer["value"],
            partners_always_usable=self.rando_settings.partners_always_usable["value"],
            hidden_block_mode=hidden_block_mode,
            starting_items=[x for x in self.starting_items if x.item_type != "ITEM"],
            startwith_speedyspin=self.rando_settings.always_speedyspin["value"],
            world_graph=modified_world_graph
        )

        # Set up seed hash for the save select screen
        self.set_seed_hash()


    def init_starting_partners(self,rando_settings):
        # Choose random starting partners if necessary
        if rando_settings.random_partners:
            self.starting_partners = get_rnd_starting_partners(
                num_rnd_partners_min=rando_settings.random_partners_min,
                num_rnd_partners_max=rando_settings.random_partners_max,
                rando_settings=rando_settings
            )
        else:
            self.starting_partners = rando_settings.starting_partners


    def init_starting_map(self, rando_settings):
        """
        Initializes the starting map and returns its chapter number. If the
        starting map is to be chosen at random, pick from curated list.
        """
        starting_map_value = rando_settings.starting_map["value"]
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
        magical_seeds_needed:int
    ):
        """
        Initialize the starting items from either the chosen starting items or
        pick them randomly.
        """
        self.starting_items = []
        if rando_settings.random_starting_items:
            starting_item_options = [
                rando_settings.starting_item_0,
                rando_settings.starting_item_1,
                rando_settings.starting_item_2,
                rando_settings.starting_item_3,
                rando_settings.starting_item_4,
                rando_settings.starting_item_5,
                rando_settings.starting_item_6,
                rando_settings.starting_item_7,
                rando_settings.starting_item_8,
                rando_settings.starting_item_9,
                rando_settings.starting_item_A,
                rando_settings.starting_item_B,
                rando_settings.starting_item_C,
                rando_settings.starting_item_D,
                rando_settings.starting_item_E,
                rando_settings.starting_item_F
            ]

            # Set up allowed items
            all_allowed_starting_items = (
                allowed_starting_badges
              + allowed_starting_items
              + allowed_starting_key_items
            )
            excluded_items = get_items_to_exclude(
                do_randomize_dojo=rando_settings.include_dojo,
                starting_partners=self.starting_partners,
                startwith_bluehouse_open=rando_settings.bluehouse_open["value"],
                magical_seeds_required=magical_seeds_needed,
                bowsers_castle_mode=rando_settings.bowsers_castle_mode["value"],
                always_speedyspin=rando_settings.always_speedyspin["value"],
                always_ispy=rando_settings.always_ispy["value"],
                always_peekaboo=rando_settings.always_peekaboo["value"],
                gear_shuffle_mode=rando_settings.gear_shuffle_mode["value"]
            )
            for item_obj in excluded_items:
                if item_obj.value in all_allowed_starting_items:
                    all_allowed_starting_items.remove(item_obj.value)

            starting_items_amount = random.randint(
                rando_settings.random_starting_items_min,
                rando_settings.random_starting_items_max
            )

            for i in range(starting_items_amount):
                random_item_id = random.choice(all_allowed_starting_items)
                random_item_obj = Item.get_or_none(Item.value == random_item_id)
                if random_item_obj is not None:
                    # No double uniques
                    if (random_item_obj.item_type in ["BADGE", "KEYITEM", "STARPIECE"]
                    and random_item_obj in self.starting_items
                    ):
                        continue

                    self.starting_items.append(random_item_obj)
                    starting_item_options[i]["value"] = random_item_id
        else:
            self.starting_items = self.rando_settings.get_startitem_list()


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
