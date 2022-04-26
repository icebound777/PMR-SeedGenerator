from copy import deepcopy
import random

from itemhints import get_itemhints
from models.CoinPalette import CoinPalette
from optionset import OptionSet
from rando_modules.logic import place_items, get_item_spheres
from rando_modules.random_actor_stats import get_shuffled_chapter_difficulty
from rando_modules.modify_entrances import get_shorter_bowsercastle
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
    def __init__(self, rando_settings: OptionSet, seed_value = None) -> None:

        self.rando_settings = rando_settings
        self.starting_partners = []
        self.placed_items = []
        self.entrance_list = []
        self.enemy_stats = []
        self.chapter_changes = {}
        self.battle_formations = []
        self.move_costs = []
        self.coin_palette:CoinPalette = CoinPalette()
        self.palette_data = []
        self.quiz_list = []
        self.music_list = []

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
        
        self.init_starting_partners(self.rando_settings)
        self.init_starting_map(self.rando_settings)
        self.init_starting_items(self.rando_settings)

        # Item Placement
        for x in range(0, 5):  # try 5 times
            try:
                world_graph_copy = deepcopy(world_graph)
                for _, _ in place_items(item_placement= self.placed_items,
                                    algorithm=self.rando_settings.placement_algorithm,
                                    do_shuffle_items=self.rando_settings.shuffle_items["value"],
                                    do_randomize_coins=self.rando_settings.include_coins["value"],
                                    do_randomize_shops=self.rando_settings.include_shops["value"],
                                    do_randomize_panels=self.rando_settings.include_panels["value"],
                                    do_randomize_koopakoot=self.rando_settings.include_favors,
                                    do_randomize_letterchain=self.rando_settings.include_letterchain,
                                    do_randomize_dojo=self.rando_settings.include_dojo,
                                    item_scarcity=self.rando_settings.item_scarcity,
                                    itemtrap_mode=self.rando_settings.itemtrap_mode,
                                    starting_map_id=self.rando_settings.starting_map["value"],
                                    startwith_bluehouse_open=self.rando_settings.bluehouse_open["value"],
                                    startwith_flowergate_open=self.rando_settings.flowergate_open["value"],
                                    startwith_toybox_open=self.rando_settings.toybox_open["value"],
                                    startwith_whale_open=self.rando_settings.whale_open["value"],
                                    starting_partners=self.starting_partners,
                                    speedyspin=self.rando_settings.always_speedyspin["value"],
                                    ispy=self.rando_settings.always_ispy["value"],
                                    peekaboo=self.rando_settings.always_peekaboo["value"],
                                    partners_always_usable=self.rando_settings.partners_always_usable["value"],
                                    partners_in_default_locations=self.rando_settings.partners_in_default_locations,
                                    hidden_block_mode=self.rando_settings.hidden_block_mode["value"],
                                    keyitems_outside_dungeon=self.rando_settings.keyitems_outside_dungeon,
                                    starting_items=self.starting_items,
                                    add_item_pouches=self.rando_settings.add_item_pouches,
                                    world_graph=world_graph_copy):
                    pass
                break

            except UnbeatableSeedError as err:
                print(f"Failed to place items! Fail count: {x+1}")

        # Modify Mystery? item
        self.rando_settings.mystery_settings = get_random_mystery(self.rando_settings.mystery_settings)

        # Make everything inexpensive
        #set_cheap_shopitems(placed_items)
        #self.placed_items = get_alpha_prices(self.placed_items)

        # Modify entrances if needed
        if self.rando_settings.shorten_bowsers_castle["value"]:
            self.entrance_list = get_shorter_bowsercastle()

        # Randomize chapter difficulty / enemy stats if needed
        self.enemy_stats, self.chapter_changes = get_shuffled_chapter_difficulty(
            self.rando_settings.shuffle_chapter_difficulty,
            self.rando_settings.progressive_scaling.get("value")
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
            self.rando_settings.include_favors,
            self.rando_settings.include_letterchain,
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

        self.item_spheres_text = get_item_spheres(item_placement= self.placed_items,
                    starting_map_id=self.rando_settings.starting_map["value"],
                    startwith_bluehouse_open=self.rando_settings.bluehouse_open["value"],
                    startwith_flowergate_open=self.rando_settings.flowergate_open["value"],
                    startwith_toybox_open=self.rando_settings.toybox_open["value"],
                    startwith_whale_open=self.rando_settings.whale_open["value"],
                    starting_partners=self.starting_partners,
                    partners_always_usable=self.rando_settings.partners_always_usable["value"],
                    hidden_block_mode=self.rando_settings.hidden_block_mode["value"],
                    starting_items=self.starting_items,
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
        #Choose random starting map if necessary
        if rando_settings.starting_map["value"] == 0xFFFFFFFF:
            self.rando_settings.starting_map["value"] = random.choice(starting_maps)

    def init_starting_items(self, rando_settings):
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

        if rando_settings.random_starting_items:
            all_allowed_starting_items = allowed_starting_badges + allowed_starting_items + allowed_starting_key_items

            starting_items_amount = random.randint(rando_settings.random_starting_items_min, rando_settings.random_starting_items_max)
            self.starting_items = []

            for i in range(starting_items_amount):
                random_item_id = random.choice(all_allowed_starting_items)
                random_item_obj = Item.get_or_none(Item.value == random_item_id)
                if random_item_obj is not None:
                    # No double uniques
                    if (random_item_obj.item_type in ["BADGE", "KEYITEM", "STARPIECE"] and random_item_obj in self.starting_items):
                        continue

                    self.starting_items.append(random_item_obj)
                    starting_item_options[i]["value"] = random_item_id
        else:
            self.starting_items = self.rando_settings.get_startitem_list()
