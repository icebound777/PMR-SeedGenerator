import random
from itemhints import get_itemhints
from models.CoinPalette import CoinPalette
from optionset import OptionSet
from rando_modules.logic import place_items
from rando_modules.random_actor_stats import get_shuffled_chapter_difficulty
from rando_modules.random_audio import get_turned_off_music
from rando_modules.random_formations import get_random_formations
from rando_modules.random_movecosts import get_randomized_moves
from rando_modules.random_palettes import get_randomized_coinpalette
from rando_modules.random_partners import get_rnd_starting_partners
from rando_modules.random_shop_prices import get_alpha_prices

class RandomSeed:
    def __init__(self, rando_settings: OptionSet) -> None:

        self.rando_settings = rando_settings
        self.starting_partners = []
        self.placed_items = []        
        self.enemy_stats = []
        self.chapter_changes = {}
        self.battle_formations = []
        self.move_costs = []
        self.coin_palette:CoinPalette = None        
        self.music_list = []
        self.seedID =  random.randint(0, 0xFFFFFFFF)    


    def generate(self):

        self.init_starting_partners(self.rando_settings)
        # Item Placement
        for _, _ in place_items(item_placement= self.placed_items,
                            algorithm=self.rando_settings.placement_algorithm,
                            do_shuffle_items=self.rando_settings.shuffle_items["value"],
                            do_randomize_coins=self.rando_settings.include_coins["value"],
                            do_randomize_shops=self.rando_settings.include_shops["value"],
                            do_randomize_panels=self.rando_settings.include_panels["value"],
                            do_randomize_koopakoot=self.rando_settings.include_favors,
                            do_randomize_letterchain=self.rando_settings.include_letterchain,
                            do_randomize_dojo=self.rando_settings.include_dojo,
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
                            keyitems_outside_dungeon=self.rando_settings.keyitems_outside_dungeon):
            pass

        # Make everything inexpensive
        #set_cheap_shopitems(placed_items)
        self.placed_items = get_alpha_prices(self.placed_items)

        # Randomize chapter difficulty / enemy stats if needed
        self.enemy_stats, self.chapter_changes = get_shuffled_chapter_difficulty(
            self.rando_settings.shuffle_chapter_difficulty
        )

        # Randomize enemy battle formations        
        if self.rando_settings.random_formations or self.rando_settings.progressive_scaling:
            self.battle_formations = get_random_formations(
                self.chapter_changes,
                self.rando_settings.progressive_scaling
            )

            # Randomize move costs (FP/BP) if needed
        
        if (
            self.rando_settings.shuffle_badges_bp
            or self.rando_settings.shuffle_badges_fp
            or self.rando_settings.shuffle_partner_fp
            or self.rando_settings.shuffle_starpower_sp
        ):
            self.move_costs = get_randomized_moves(
                self.rando_settings.shuffle_badges_bp,
                self.rando_settings.shuffle_badges_fp,
                self.rando_settings.shuffle_partner_fp,
                self.rando_settings.shuffle_starpower_sp
            )

        # Build item hint db
        self.itemhints = get_itemhints(
                self.placed_items,
                self.rando_settings.include_shops["value"],
                self.rando_settings.include_panels["value"],
                self.rando_settings.include_favors,
                self.rando_settings.include_letterchain,
                self.rando_settings.keyitems_outside_dungeon
            )

        # Randomize sprite palettes        
        if self.rando_settings.random_coin_palette:
            self.coin_palette = get_randomized_coinpalette()

        # Music settings        
        if self.rando_settings.turn_off_music:
            self.music_list = get_turned_off_music()

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