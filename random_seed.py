from copy import deepcopy
import random

from itemhints import get_itemhints
from models.CoinPalette import CoinPalette
from optionset import OptionSet
from rando_modules.logic import place_items, get_item_spheres, get_items_to_exclude
from rando_modules.random_blocks import get_block_placement
from rando_modules.random_actor_stats import get_shuffled_chapter_difficulty
from rando_modules.modify_entrances import \
    get_shorter_bowsercastle, get_bowsercastle_bossrush, get_gear_location_shuffle, get_glitched_logic
from rando_modules.random_formations import get_random_formations
from rando_modules.random_movecosts import get_randomized_moves
from rando_modules.random_mystery import get_random_mystery
from rando_modules.random_palettes     \
    import get_randomized_coinpalette, \
           get_randomized_palettes
from rando_modules.random_partners import get_rnd_starting_partners
from rando_modules.random_quizzes import get_randomized_quizzes
from rando_modules.unbeatable_seed_error import UnbeatableSeedError
from worldgraph import generate as generate_world_graph
from metadata.starting_maps import starting_maps
from metadata.starting_items import allowed_starting_badges, allowed_starting_items, allowed_starting_key_items
from db.item import Item

class RandomSeed:
    def __init__(self, rando_settings: OptionSet, seed_value=None) -> None:

        self.rando_settings = OptionSet()
        for setting_name, value in rando_settings.__dict__.items():
            self.rando_settings.__dict__[setting_name] = value["value"] if isinstance(value, dict) else value

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
        self.item_spheres_text = None

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

        # Modify entrances if needed
        if self.rando_settings.bowsers_castle_mode == 1:
            self.entrance_list, world_graph = get_shorter_bowsercastle(world_graph)
        elif self.rando_settings.bowsers_castle_mode == 2:
            self.entrance_list, world_graph = get_bowsercastle_bossrush(world_graph)
        if self.rando_settings.gear_shuffle_mode != 0:
            world_graph = get_gear_location_shuffle(world_graph, self.rando_settings.gear_shuffle_mode)

        # Adjust graph logic if needed
        world_graph = get_glitched_logic(world_graph, self.rando_settings.glitch_settings, self.rando_settings.bowsers_castle_mode)

        hidden_block_mode = self.rando_settings.hidden_block_mode
        if self.rando_settings.glitch_settings.knows_hidden_blocks:
            hidden_block_mode = 3 # Having this trick enabled is equivalent to mode 3, logic wise


        # Item Placement
        for placement_attempt in range(1, 11):  # try 10 times
            try:
                starting_chapter, starting_map_value = self.init_starting_map(self.rando_settings)
                self.init_starting_partners(self.rando_settings)
                self.init_starting_items(self.rando_settings)

                # Pick seeds required for flower gate, if random
                if self.rando_settings.magical_seeds_required == 5:
                    magical_seeds_required = random.randint(0, 4)
                else:
                    magical_seeds_required = self.rando_settings.magical_seeds_required

                world_graph_copy = deepcopy(world_graph)
                place_items(
                    item_placement= self.placed_items,
                    algorithm=self.rando_settings.placement_algorithm,
                    do_shuffle_items=self.rando_settings.shuffle_items,
                    do_randomize_coins=self.rando_settings.include_coins,
                    do_randomize_shops=self.rando_settings.include_shops,
                    do_randomize_panels=self.rando_settings.include_panels,
                    randomize_favors_mode=self.rando_settings.include_favors_mode,
                    randomize_letters_mode=self.rando_settings.include_letters_mode,
                    do_randomize_radiotrade=self.rando_settings.include_radiotradeevent,
                    do_randomize_dojo=self.rando_settings.include_dojo,
                    gear_shuffle_mode=self.rando_settings.gear_shuffle_mode,
                    item_scarcity=self.rando_settings.item_scarcity,
                    itemtrap_mode=self.rando_settings.itemtrap_mode,
                    starting_map_id=starting_map_value,
                    startwith_bluehouse_open=self.rando_settings.bluehouse_open,
                    magical_seeds_required=magical_seeds_required,
                    startwith_toybox_open=self.rando_settings.toybox_open,
                    startwith_whale_open=self.rando_settings.whale_open,
                    starting_partners=self.starting_partners,
                    starting_boots=self.rando_settings.starting_boots,
                    starting_hammer=self.rando_settings.starting_hammer,
                    speedyspin=self.rando_settings.always_speedyspin,
                    ispy=self.rando_settings.always_ispy,
                    peekaboo=self.rando_settings.always_peekaboo,
                    partners_always_usable=self.rando_settings.partners_always_usable,
                    partners_in_default_locations=self.rando_settings.partners_in_default_locations,
                    hidden_block_mode=hidden_block_mode,
                    keyitems_outside_dungeon=self.rando_settings.keyitems_outside_dungeon,
                    starting_items=[x for x in self.starting_items if x.item_type != "ITEM"],
                    add_item_pouches=self.rando_settings.add_item_pouches,
                    bowsers_castle_mode=self.rando_settings.bowsers_castle_mode,
                    world_graph=world_graph_copy
                )

                self.rando_settings.starting_map = starting_map_value # Overwrite starting map in case it was random at first
                self.rando_settings.magical_seeds_required = magical_seeds_required
                break

            except UnbeatableSeedError as err:
                print(f"Failed to place items! Fail count: {placement_attempt}")

        
        # Modify Mystery? item
        self.rando_settings.mystery_settings = get_random_mystery(
            self.rando_settings.mystery_settings
        )

        # Make everything inexpensive
        #set_cheap_shopitems(placed_items)
        #self.placed_items = get_alpha_prices(self.placed_items)

        # Randomize blocks if needed
        self.placed_blocks = get_block_placement(self.rando_settings.shuffle_blocks)

        # Randomize chapter difficulty / enemy stats if needed
        self.enemy_stats, self.chapter_changes = get_shuffled_chapter_difficulty(
            self.rando_settings.shuffle_chapter_difficulty,
            self.rando_settings.progressive_scaling,
            starting_chapter
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
            self.rando_settings.random_starpower_sp
        )

        # Build item hint db
        self.itemhints = get_itemhints(
            self.rando_settings.allow_itemhints,
            self.placed_items,
            self.starting_partners,
            self.rando_settings.partners_in_default_locations,
            self.rando_settings.include_shops,
            self.rando_settings.include_panels,
            self.rando_settings.include_favors_mode,
            self.rando_settings.include_letters_mode,
            self.rando_settings.keyitems_outside_dungeon
        )

        # Random quiz
        if self.rando_settings.random_quiz:
            self.quiz_list = get_randomized_quizzes()

        # Randomize sprite palettes
        (self.coin_palette,
         self.rando_settings.coin_color
        ) = get_randomized_coinpalette(
            color_id = self.rando_settings.coin_color,
            should_randomize_color = self.rando_settings.random_coin_color
        )
        self.palette_data = get_randomized_palettes(
            self.rando_settings.palette_settings
        )

        # Music settings

        # Determine item placement spheres
        self.item_spheres_text = get_item_spheres(
            item_placement= self.placed_items,
            starting_map_id=self.rando_settings.starting_map,
            startwith_bluehouse_open=self.rando_settings.bluehouse_open,
            magical_seeds_required=self.rando_settings.magical_seeds_required,
            startwith_toybox_open=self.rando_settings.toybox_open,
            startwith_whale_open=self.rando_settings.whale_open,
            starting_partners=self.starting_partners,
            starting_boots=self.rando_settings.starting_boots,
            starting_hammer=self.rando_settings.starting_hammer,
            partners_always_usable=self.rando_settings.partners_always_usable,
            hidden_block_mode=hidden_block_mode,
            starting_items=[x for x in self.starting_items if x.item_type != "ITEM"],
            startwith_speedyspin=self.rando_settings.always_speedyspin,
            world_graph=world_graph
        )


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
        starting_map_value = rando_settings.starting_map
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



    def init_starting_items(self, rando_settings:OptionSet):
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
                startwith_bluehouse_open=rando_settings.bluehouse_open,
                magical_seeds_required=rando_settings.magical_seeds_required,
                bowsers_castle_mode=rando_settings.bowsers_castle_mode,
                always_speedyspin=rando_settings.always_speedyspin,
                always_ispy=rando_settings.always_ispy,
                always_peekaboo=rando_settings.always_peekaboo,
                gear_shuffle_mode=rando_settings.gear_shuffle_mode,
                starting_hammer=None,
                starting_boots=None
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
                    starting_item_options[i] = random_item_id
        else:
            self.starting_items = self.rando_settings.get_startitem_list()
