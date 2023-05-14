from db.item import Item
from db.option import Option

from rando_enums.enum_options import (
    IncludeFavorsMode,
    IncludeLettersMode,
    RandomizeConsumablesMode,
    ItemTrapMode,
    RandomMoveCosts,
    HiddenBlockMode,
    StartingBoots,
    StartingHammer,
    MerlowRewardPricing,
    MusicRandomizationType
)

class OptionSet:
    def __init__(self):
        """ Load Defaults from DB """
        # General
        self.blocks_match_content = get_option_keyvalue_dict("BlocksMatchContent")
        self.hidden_block_mode = get_option_keyvalue_dict("HiddenBlockMode")
        self.allow_physics_glitches = get_option_keyvalue_dict("AllowPhysicsGlitches")
        self.badge_synergy = get_option_keyvalue_dict("BadgeSynergy")

        # QOL
        self.always_speedyspin = get_option_keyvalue_dict("AlwaysSpeedySpin")
        self.always_ispy = get_option_keyvalue_dict("AlwaysISpy")
        self.always_peekaboo = get_option_keyvalue_dict("AlwaysPeekaboo")
        self.shorten_cutscenes = get_option_keyvalue_dict("ShortenCutscenes")
        self.fast_text_skip = get_option_keyvalue_dict("FastTextSkip")
        self.skip_epilogue = get_option_keyvalue_dict("SkipEpilogue")
        self.peachcastle_return_pipe = get_option_keyvalue_dict("PeachCastleReturnPipe")
        self.foliage_item_hints = get_option_keyvalue_dict("FoliageItemHints")
        self.hiddenpanel_visibility = get_option_keyvalue_dict("HiddenPanelVisibility")

        # Difficulty and Enemies
        self.shuffle_chapter_difficulty = False
        self.progressive_scaling = get_option_keyvalue_dict("ProgressiveScaling")

        self.challenge_mode = get_option_keyvalue_dict("ChallengeMode")
        self.cap_enemy_xp = get_option_keyvalue_dict("CapEnemyXP")
        self.xp_multiplier = get_option_keyvalue_dict("XPMultiplier")
        self.damage_x2 = get_option_keyvalue_dict("DoubleDamage")
        self.damage_x4 = get_option_keyvalue_dict("QuadrupleDamage")
        self.ohko = get_option_keyvalue_dict("OHKO")
        self.no_save_blocks = get_option_keyvalue_dict("NoSaveBlocks")
        self.no_heart_blocks = get_option_keyvalue_dict("NoHeartBlocks")
        self.no_healing_items = get_option_keyvalue_dict("NoHealingItems")

        self.random_formations = get_option_keyvalue_dict("RandomFormations")

        # Custom Seed / Planned Seed / "Plandomizer"
        self.custom_seed = False

        # Item Placement
        self.shuffle_items = get_option_keyvalue_dict("ShuffleItems")
        self.include_coins_overworld = True
        self.include_coins_blocks = True
        self.include_coins_foliage = True
        self.include_coins_favors = False
        self.include_shops = get_option_keyvalue_dict("IncludeShops")
        self.progression_on_rowf = True
        self.progression_on_merlow = True
        self.include_panels = get_option_keyvalue_dict("IncludePanels")
        self.include_favors_mode = IncludeFavorsMode.NOT_RANDOMIZED
        self.include_letters_mode = IncludeLettersMode.NOT_RANDOMIZED
        self.include_radiotradeevent = False
        self.include_dojo = False
        self.keyitems_outside_dungeon = True
        self.keyitems_outside_chapter = True # "Keysanity" # false -> NYI

        # Item Pool Modification
        self.gear_shuffle_mode = get_option_keyvalue_dict("GearShuffleMode")
        self.add_item_pouches = False
        self.randomize_consumable_mode = RandomizeConsumablesMode.OFF
        self.item_quality = 100
        self.itemtrap_mode = ItemTrapMode.OFF

        # Map Check Tracker (auto-set, not changeable via settings)
        self.map_tracker_check_bits = get_option_keyvalue_dict("EnabledCheckBits")
        self.map_tracker_shop_bits = get_option_keyvalue_dict("EnabledShopBits")

        # Item Misc
        self.cook_without_fryingpan = get_option_keyvalue_dict("CookWithoutFryingPan")
        self.merlow_reward_pricing = MerlowRewardPricing.NORMAL
        self.ripcheato_items_in_logic = 6
        self.allow_itemhints = True
        self.mystery_settings = MysteryOptionSet()

        # Starting setup
        self.starting_map = get_option_keyvalue_dict("StartingMap") # mac_00 Entry 4
        self.starting_level = get_option_keyvalue_dict("StartingLevel")
        self.starting_maxhp = get_option_keyvalue_dict("StartingMaxHP")
        self.starting_maxfp = get_option_keyvalue_dict("StartingMaxFP")
        self.starting_maxbp = get_option_keyvalue_dict("StartingMaxBP")
        self.starting_starpower = get_option_keyvalue_dict("StartingStarPower")
        self.starting_boots = get_option_keyvalue_dict("StartingBoots")
        self.starting_hammer = get_option_keyvalue_dict("StartingHammer")
        self.starting_coins = get_option_keyvalue_dict("StartingCoins")

        self.random_starting_items = False
        self.random_starting_items_min = 0
        self.random_starting_items_max = 16
        self.starting_item_0 = get_option_keyvalue_dict("StartingItem0")
        self.starting_item_1 = get_option_keyvalue_dict("StartingItem1")
        self.starting_item_2 = get_option_keyvalue_dict("StartingItem2")
        self.starting_item_3 = get_option_keyvalue_dict("StartingItem3")
        self.starting_item_4 = get_option_keyvalue_dict("StartingItem4")
        self.starting_item_5 = get_option_keyvalue_dict("StartingItem5")
        self.starting_item_6 = get_option_keyvalue_dict("StartingItem6")
        self.starting_item_7 = get_option_keyvalue_dict("StartingItem7")
        self.starting_item_8 = get_option_keyvalue_dict("StartingItem8")
        self.starting_item_9 = get_option_keyvalue_dict("StartingItem9")
        self.starting_item_A = get_option_keyvalue_dict("StartingItemA")
        self.starting_item_B = get_option_keyvalue_dict("StartingItemB")
        self.starting_item_C = get_option_keyvalue_dict("StartingItemC")
        self.starting_item_D = get_option_keyvalue_dict("StartingItemD")
        self.starting_item_E = get_option_keyvalue_dict("StartingItemE")
        self.starting_item_F = get_option_keyvalue_dict("StartingItemF")

        # Partners
        self.starting_partners = ["Goombario"]
        self.start_with_goombario = get_option_keyvalue_dict("StartWithGoombario")
        self.start_with_kooper = get_option_keyvalue_dict("StartWithKooper")
        self.start_with_bombette = get_option_keyvalue_dict("StartWithBombette")
        self.start_with_parakarry = get_option_keyvalue_dict("StartWithParakarry")
        self.start_with_bow = get_option_keyvalue_dict("StartWithBow")
        self.start_with_watt = get_option_keyvalue_dict("StartWithWatt")
        self.start_with_sushie = get_option_keyvalue_dict("StartWithSushie")
        self.start_with_lakilester = get_option_keyvalue_dict("StartWithLakilester")

        self.partners_in_default_locations = True
        self.partners_always_usable = get_option_keyvalue_dict("PartnersAlwaysUsable")
        self.random_partners = False
        self.random_partners_min = 1
        self.random_partners_max = 1

        # Pre-opened areas
        self.magical_seeds_required = get_option_keyvalue_dict("MagicalSeedsRequired")
        self.prologue_open = get_option_keyvalue_dict("PrologueOpen")
        self.bluehouse_open = get_option_keyvalue_dict("BlueHouseOpen")
        self.mtrugged_open = get_option_keyvalue_dict("MtRuggedOpen")
        self.toybox_open = get_option_keyvalue_dict("ToyboxOpen")
        self.whale_open = get_option_keyvalue_dict("WhaleOpen")
        self.ch7_bridge_visible = get_option_keyvalue_dict("Ch7BridgeVisible")

        # Goal Settings
        self.starway_spirits_needed_count = get_option_keyvalue_dict("StarWaySpiritsNeededCnt")
        self.bowsers_castle_mode = get_option_keyvalue_dict("BowsersCastleMode")
        self.star_hunt = get_option_keyvalue_dict("StarHunt")
        self.star_hunt_required = get_option_keyvalue_dict("StarHuntRequired")
        self.star_hunt_total = get_option_keyvalue_dict("StarHuntTotal")
        self.star_hunt_ends_game = get_option_keyvalue_dict("StarHuntEndsGame")

        # Entrance Shuffle
        self.shuffle_dungeon_rooms = get_option_keyvalue_dict("ShuffleDungeonRooms")
        self.shuffle_dungeon_entrances = get_option_keyvalue_dict("ShuffleDungeonEntrances")
        self.shuffle_entrances_by_all = get_option_keyvalue_dict("ShuffleEntrancesByAll")
        self.match_entrance_type = get_option_keyvalue_dict("MatchEntranceTypes")
        self.random_oneway_entrances = False # NYI
        self.unpaired_entrances = False # NYI

        # Costs of Moves and Badges
        self.random_badges_bp = RandomMoveCosts.VANILLA
        self.random_badges_fp = RandomMoveCosts.VANILLA
        self.random_partner_fp = RandomMoveCosts.VANILLA
        self.random_starpower_sp = RandomMoveCosts.VANILLA

        # Misc Gameplay Randomization
        self.shuffle_blocks = False

        # Quizmo Quizzes
        self.random_quiz = get_option_keyvalue_dict("RandomQuiz")
        self.quizmo_always_appears = get_option_keyvalue_dict("QuizmoAlwaysAppears")
        self.skip_quiz = get_option_keyvalue_dict("SkipQuiz")

        # Spoilerlog
        self.write_spoilerlog = True

        # Cosmetics
        self.color_a = get_option_keyvalue_dict("Box5ColorA")
        self.color_b = get_option_keyvalue_dict("Box5ColorB")
        self.coin_color = get_option_keyvalue_dict("CoinColor")
        self.random_coin_color = False

        self.palette_settings = PaletteOptionSet()

        # Audio
        self.shuffle_music = False
        self.shuffle_music_mode = MusicRandomizationType.MOOD
        self.shuffle_jingles = False

        # Joke options
        self.roman_numerals = get_option_keyvalue_dict("RomanNumerals")
        self.random_text = get_option_keyvalue_dict("RandomText")
        self.random_pitch = get_option_keyvalue_dict("RandomPitch")

        # Glitched Logic
        self.glitch_settings = GlitchOptionSet()


    def get_startitem_list(self) -> list:
        """Returns this OptionSet's starting items as list of Item objects."""
        starting_items = []

        for self_key, self_value in self.__dict__.items():
            if self_key.startswith("starting_item"):
                item_id = self_value.get("value")
                if item_id != 0:
                    item_obj = Item.get_or_none(Item.value == item_id)
                    if item_obj is not None:
                        # No double uniques
                        if (    item_obj.item_type in ["BADGE", "KEYITEM", "STARPIECE"]
                            and item_obj in starting_items
                        ):
                            continue
                        starting_items.append(Item.get(Item.value == item_id))

        return starting_items


    def update_options(self, options_dict=None):

        try:
            validate_options(options_dict)
        except ValueError as err:
            print(f"{err.args}: Settings file not provided.")
            raise
        except AssertionError as err:
            print(f"ERROR: Settings file includes invalid data.")
            raise

        # General
        if "BlocksMatchContent" in options_dict:
            self.blocks_match_content = options_dict.get("BlocksMatchContent")
        if "HiddenBlockMode" in options_dict:
            self.hidden_block_mode = options_dict.get("HiddenBlockMode")
        if "AllowPhysicsGlitches" in options_dict:
            self.allow_physics_glitches = options_dict.get("AllowPhysicsGlitches")
        if "BadgeSynergy" in options_dict:
            self.badge_synergy = options_dict.get("BadgeSynergy")

        # QOL
        if "AlwaysSpeedySpin" in options_dict:
            self.always_speedyspin = options_dict.get("AlwaysSpeedySpin")
        if "AlwaysISpy" in options_dict:
            self.always_ispy = options_dict.get("AlwaysISpy")
        if "AlwaysPeekaboo" in options_dict:
            self.always_peekaboo = options_dict.get("AlwaysPeekaboo")
        if "ShortenCutscenes" in options_dict:
            self.shorten_cutscenes = options_dict.get("ShortenCutscenes")
            self.fast_text_skip["value"] = self.shorten_cutscenes["value"]
        if "SkipEpilogue" in options_dict:
            self.skip_epilogue = options_dict.get("SkipEpilogue")
        if "PeachCastleReturnPipe" in options_dict:
            self.peachcastle_return_pipe = options_dict.get("PeachCastleReturnPipe")
        if "FoliageItemHints" in options_dict:
            self.foliage_item_hints = options_dict.get("FoliageItemHints")
        if "HiddenPanelVisibility" in options_dict:
            self.hiddenpanel_visibility = options_dict.get("HiddenPanelVisibility")

        # Difficulty and Enemies
        if "ShuffleChapterDifficulty" in options_dict:
            self.shuffle_chapter_difficulty = options_dict.get("ShuffleChapterDifficulty").get("value")
        if "ProgressiveScaling" in options_dict:
            self.progressive_scaling = options_dict.get("ProgressiveScaling")

        if "ChallengeMode" in options_dict:
            self.challenge_mode = options_dict.get("ChallengeMode")
        if "CapEnemyXP" in options_dict:
            self.cap_enemy_xp = options_dict.get("CapEnemyXP")
        if "XPMultiplier" in options_dict:
            options_dict["XPMultiplier"]["value"] = int(options_dict.get("XPMultiplier").get("value") * 2) # Will get divided by 2 in mod
            self.xp_multiplier = options_dict.get("XPMultiplier")
        if "DoubleDamage" in options_dict:
            self.damage_x2 = options_dict.get("DoubleDamage")
        if "QuadrupleDamage" in options_dict:
            self.damage_x4 = options_dict.get("QuadrupleDamage")
        if "OHKO" in options_dict:
            self.ohko = options_dict.get("OHKO")
        if "NoSaveBlocks" in options_dict:
            self.no_save_blocks = options_dict.get("NoSaveBlocks")
        if "NoHeartBlocks" in options_dict:
            self.no_heart_blocks = options_dict.get("NoHeartBlocks")
        if "NoHealingItems" in options_dict:
            self.no_healing_items = options_dict.get("NoHealingItems")

        if "RandomFormations" in options_dict:
            self.random_formations = options_dict.get("RandomFormations")

        # Custom Seed / Planned Seed / "Plandomizer"
        if "CustomSeed" in options_dict:
            self.custom_seed = options_dict.get("CustomSeed").get("value")

        # Item Placement
        if "ShuffleItems" in options_dict:
            self.shuffle_items = options_dict.get("ShuffleItems")
        if "IncludeCoinsOverworld" in options_dict:
            self.include_coins_overworld = options_dict.get("IncludeCoinsOverworld").get("value")
        if "IncludeCoinsBlocks" in options_dict:
            self.include_coins_blocks = options_dict.get("IncludeCoinsBlocks").get("value")
        if "IncludeCoinsFoliage" in options_dict:
            self.include_coins_foliage = options_dict.get("IncludeCoinsFoliage").get("value")
        if "IncludeCoinsFavors" in options_dict:
            self.include_coins_favors = options_dict.get("IncludeCoinsFavors").get("value")
        if "IncludeShops" in options_dict:
            self.include_shops = options_dict.get("IncludeShops")
        if "ProgressionOnRowf" in options_dict:
            self.progression_on_rowf = options_dict.get("ProgressionOnRowf").get("value")
        if "ProgressionOnMerlow" in options_dict:
            self.progression_on_merlow = options_dict.get("ProgressionOnMerlow").get("value")
        if "IncludePanels" in options_dict:
            self.include_panels = options_dict.get("IncludePanels")
        if "IncludeFavorsMode" in options_dict:
            self.include_favors_mode = options_dict.get("IncludeFavorsMode").get("value")
        if "IncludeLettersMode" in options_dict:
            self.include_letters_mode = options_dict.get("IncludeLettersMode").get("value")
        if "IncludeRadioTradeEvent" in options_dict:
            self.include_radiotradeevent = options_dict.get("IncludeRadioTradeEvent").get("value")
        if "IncludeDojo" in options_dict:
            self.include_dojo = options_dict.get("IncludeDojo").get("value")
        if "KeyitemsOutsideDungeon" in options_dict:
            self.keyitems_outside_dungeon = options_dict.get("KeyitemsOutsideDungeon").get("value")
        if "KeyitemsOutsideChapter" in options_dict:
            self.keyitems_outside_chapter = options_dict.get("KeyitemsOutsideChapter").get("value")

        # Item Pool Modification
        if "GearShuffleMode" in options_dict:
            self.gear_shuffle_mode = options_dict.get("GearShuffleMode")
        if "AddItemPouches" in options_dict:
            self.add_item_pouches = options_dict.get("AddItemPouches").get("value")
        if "RandomConsumableMode" in options_dict:
            self.randomize_consumable_mode = options_dict.get("RandomConsumableMode").get("value")
        if "ItemQuality" in options_dict:
            self.item_quality = options_dict.get("ItemQuality").get("value")
        if "ItemTrapMode" in options_dict:
            self.itemtrap_mode = options_dict.get("ItemTrapMode").get("value")

        # Map Check Tracker (static)
        #   0x1   # regular checks
        #   0x2   # gear
        #   0x4   # panels
        #   0x10  # overworld coins
        #   0x20  # block coins
        #   0x40  # favor coins
        #   0x80  # foliage coins
        #   0x100 # dojo
        #   0x200 # koot favors
        #   0x400 # radio trade event
        #   0x800 # letter delivery
        map_tracker_bits = 0x1 + 0x2
        if self.include_panels.get("value"):
            map_tracker_bits += 0x4
        if self.include_coins_overworld:
            map_tracker_bits += 0x10
        if self.include_coins_blocks:
            map_tracker_bits += 0x20
        if self.include_coins_favors:
            map_tracker_bits += 0x40
        if self.include_coins_foliage:
            map_tracker_bits += 0x80
        if self.include_dojo:
            map_tracker_bits += 0x100
        if self.include_favors_mode != IncludeFavorsMode.NOT_RANDOMIZED:
            map_tracker_bits += 0x200
        if self.include_radiotradeevent:
            map_tracker_bits += 0x400
        if self.include_letters_mode != IncludeLettersMode.NOT_RANDOMIZED:
            map_tracker_bits += 0x800
        self.map_tracker_check_bits["value"] = map_tracker_bits
        #self.map_tracker_shop_bits = 0xFFFF # static for now

        # Item Misc
        if "CookWithoutFryingPan" in options_dict:
            self.cook_without_fryingpan = options_dict.get("CookWithoutFryingPan")
        if "MerlowRewardPricing" in options_dict:
            self.merlow_reward_pricing = options_dict.get("MerlowRewardPricing").get("value")
        if "RipCheatoItemsInLogic" in options_dict:
            self.ripcheato_items_in_logic = options_dict.get("RipCheatoItemsInLogic").get("value")
        if "AllowItemHints" in options_dict:
            self.allow_itemhints = options_dict.get("AllowItemHints").get("value")
        if "RandomChoice" in options_dict:
            self.mystery_settings.mystery_random_choice = options_dict.get("RandomChoice")
        if "MysteryRandomPick" in options_dict:
            self.mystery_settings.mystery_random_pick = options_dict.get("MysteryRandomPick").get("value")
        if "ItemChoiceA" in options_dict:
            self.mystery_settings.mystery_itemA = options_dict.get("ItemChoiceA")
        if "ItemChoiceB" in options_dict:
            self.mystery_settings.mystery_itemB = options_dict.get("ItemChoiceB")
        if "ItemChoiceC" in options_dict:
            self.mystery_settings.mystery_itemC = options_dict.get("ItemChoiceC")
        if "ItemChoiceD" in options_dict:
            self.mystery_settings.mystery_itemD = options_dict.get("ItemChoiceD")
        if "ItemChoiceE" in options_dict:
            self.mystery_settings.mystery_itemE = options_dict.get("ItemChoiceE")
        if "ItemChoiceF" in options_dict:
            self.mystery_settings.mystery_itemF = options_dict.get("ItemChoiceF")
        if "ItemChoiceG" in options_dict:
            self.mystery_settings.mystery_itemG = options_dict.get("ItemChoiceG")

        # Starting setup
        if "StartingMap" in options_dict:
            self.starting_map = options_dict.get("StartingMap")
        if "StartingLevel" in options_dict:
            self.starting_level = options_dict.get("StartingLevel")
        if "StartingMaxHP" in options_dict:
            self.starting_maxhp = options_dict.get("StartingMaxHP")
        if "StartingMaxFP" in options_dict:
            self.starting_maxfp = options_dict.get("StartingMaxFP")
        if "StartingMaxBP" in options_dict:
            self.starting_maxbp = options_dict.get("StartingMaxBP")
        if "StartingStarPower" in options_dict:
            self.starting_starpower = options_dict.get("StartingStarPower")
        if "StartingBoots" in options_dict:
            self.starting_boots = options_dict.get("StartingBoots")
        if "StartingHammer" in options_dict:
            self.starting_hammer = options_dict.get("StartingHammer")
        if "StartingCoins" in options_dict:
            self.starting_coins = options_dict.get("StartingCoins")

        if "StartWithRandomItems" in options_dict:
            self.random_starting_items = options_dict.get("StartWithRandomItems").get("value")
        if "RandomItemsMin" in options_dict:
            self.random_starting_items_min = options_dict.get("RandomItemsMin").get("value")
        if "RandomItemsMax" in options_dict:
            self.random_starting_items_max = options_dict.get("RandomItemsMax").get("value")
        if "StartingItem0" in options_dict:
            self.starting_item_0 = options_dict.get("StartingItem0")
        if "StartingItem1" in options_dict:
            self.starting_item_1 = options_dict.get("StartingItem1")
        if "StartingItem2" in options_dict:
            self.starting_item_2 = options_dict.get("StartingItem2")
        if "StartingItem3" in options_dict:
            self.starting_item_3 = options_dict.get("StartingItem3")
        if "StartingItem4" in options_dict:
            self.starting_item_4 = options_dict.get("StartingItem4")
        if "StartingItem5" in options_dict:
            self.starting_item_5 = options_dict.get("StartingItem5")
        if "StartingItem6" in options_dict:
            self.starting_item_6 = options_dict.get("StartingItem6")
        if "StartingItem7" in options_dict:
            self.starting_item_7 = options_dict.get("StartingItem7")
        if "StartingItem8" in options_dict:
            self.starting_item_8 = options_dict.get("StartingItem8")
        if "StartingItem9" in options_dict:
            self.starting_item_9 = options_dict.get("StartingItem9")
        if "StartingItemA" in options_dict:
            self.starting_item_A = options_dict.get("StartingItemA")
        if "StartingItemB" in options_dict:
            self.starting_item_B = options_dict.get("StartingItemB")
        if "StartingItemC" in options_dict:
            self.starting_item_C = options_dict.get("StartingItemC")
        if "StartingItemD" in options_dict:
            self.starting_item_D = options_dict.get("StartingItemD")
        if "StartingItemE" in options_dict:
            self.starting_item_E = options_dict.get("StartingItemE")
        if "StartingItemF" in options_dict:
            self.starting_item_F = options_dict.get("StartingItemF")

        # Partners
        if "StartWithPartners" in options_dict:
            self.starting_partners.clear()
            for partner, start_with_partner in options_dict.get("StartWithPartners").get("value").items():
                if start_with_partner:
                    self.starting_partners.append(partner)
                if partner == "Goombario":
                    self.start_with_goombario["value"] = start_with_partner
                elif partner == "Kooper":
                    self.start_with_kooper["value"] = start_with_partner
                elif partner == "Bombette":
                    self.start_with_bombette["value"] = start_with_partner
                elif partner == "Parakarry":
                    self.start_with_parakarry["value"] = start_with_partner
                elif partner == "Bow":
                    self.start_with_bow["value"] = start_with_partner
                elif partner == "Watt":
                    self.start_with_watt["value"] = start_with_partner
                elif partner == "Sushie":
                    self.start_with_sushie["value"] = start_with_partner
                elif partner == "Lakilester":
                    self.start_with_lakilester["value"] = start_with_partner

        if "PartnersInDefaultLocations" in options_dict:
            self.partners_in_default_locations = options_dict.get("PartnersInDefaultLocations").get("value")
        if "PartnersAlwaysUsable" in options_dict:
            self.partners_always_usable = options_dict.get("PartnersAlwaysUsable")
        if "StartWithRandomPartners" in options_dict:
            self.random_partners = options_dict.get("StartWithRandomPartners").get("value")
        if "RandomPartnersMin" in options_dict:
            self.random_partners_min = options_dict.get("RandomPartnersMin").get("value")
        if "RandomPartnersMax" in options_dict:
            self.random_partners_max = options_dict.get("RandomPartnersMax").get("value")

        # Pre-opened areas
        if "MagicalSeedsRequired" in options_dict:
            self.magical_seeds_required = options_dict.get("MagicalSeedsRequired")
        if "PrologueOpen" in options_dict:
            self.prologue_open = options_dict.get("PrologueOpen")
        if "BlueHouseOpen" in options_dict:
            self.bluehouse_open = options_dict.get("BlueHouseOpen")
        if "MtRuggedOpen" in options_dict:
            self.mtrugged_open = options_dict.get("MtRuggedOpen")
        if "ToyboxOpen" in options_dict:
            self.toybox_open = options_dict.get("ToyboxOpen")
        if "WhaleOpen" in options_dict:
            self.whale_open = options_dict.get("WhaleOpen")
        if "Ch7BridgeVisible" in options_dict:
            self.ch7_bridge_visible = options_dict.get("Ch7BridgeVisible")

        # Goal Settings
        if "StarWaySpiritsNeededCnt" in options_dict:
            self.starway_spirits_needed_count = options_dict.get("StarWaySpiritsNeededCnt")
        if "BowsersCastleMode" in options_dict:
            self.bowsers_castle_mode = options_dict.get("BowsersCastleMode")
        if "StarHunt" in options_dict:
            self.star_hunt = options_dict.get("StarHunt")
        if "StarHuntRequired" in options_dict:
            self.star_hunt_required = options_dict.get("StarHuntRequired")
        if "StarHuntTotal" in options_dict:
            self.star_hunt_total = options_dict.get("StarHuntTotal")
        if "StarHuntEndsGame" in options_dict:
            self.star_hunt_ends_game = options_dict.get("StarHuntEndsGame")

        # Entrance Shuffle
        if "ShuffleDungeonRooms" in options_dict:
            self.shuffle_dungeon_rooms = options_dict.get("ShuffleDungeonRooms")
        if "ShuffleDungeonEntrances" in options_dict:
            self.shuffle_dungeon_entrances = options_dict.get("ShuffleDungeonEntrances")
        if "ShuffleEntrancesByAll" in options_dict:
            self.shuffle_entrances_by_all = options_dict.get("ShuffleEntrancesByAll")
        if "MatchEntranceTypes" in options_dict:
            self.match_entrance_type = options_dict.get("MatchEntranceTypes")
        if "RandomizeOnewayEntrances" in options_dict:
            self.random_oneway_entrances = options_dict.get("RandomizeOnewayEntrances").get("value")
        if "UnpairedEntrances" in options_dict:
            self.unpaired_entrances = options_dict.get("UnpairedEntrances").get("value")

        # Costs of Moves and Badges
        if "RandomBadgesBP" in options_dict:
            self.random_badges_bp = options_dict.get("RandomBadgesBP").get("value")
        if "RandomBadgesFP" in options_dict:
            self.random_badges_fp = options_dict.get("RandomBadgesFP").get("value")
        if "RandomPartnerFP" in options_dict:
            self.random_partner_fp = options_dict.get("RandomPartnerFP").get("value")
        if "RandomStarpowerSP" in options_dict:
            self.random_starpower_sp = options_dict.get("RandomStarpowerSP").get("value")

        # Misc Gameplay Randomization
        if "ShuffleBlocks" in options_dict:
            self.shuffle_blocks = options_dict.get("ShuffleBlocks").get("value")

        # Quizmo Quizzes
        if "RandomQuiz" in options_dict:
            self.random_quiz = options_dict.get("RandomQuiz")
        if "QuizmoAlwaysAppears" in options_dict:
            self.quizmo_always_appears = options_dict.get("QuizmoAlwaysAppears")
        if "SkipQuiz" in options_dict:
            self.skip_quiz = options_dict.get("SkipQuiz")

        # Spoilerlog
        if "WriteSpoilerLog" in options_dict:
            self.write_spoilerlog = options_dict.get("WriteSpoilerLog").get("value")

        # Cosmetics General
        if "Box5ColorA" in options_dict:
            self.color_a = options_dict.get("Box5ColorA")
        if "Box5ColorB" in options_dict:
            self.color_b = options_dict.get("Box5ColorB")
        if "CoinColor" in options_dict:
            self.coin_color = options_dict.get("CoinColor")
        if "RandomCoinColor" in options_dict:
            self.random_coin_color = options_dict.get("RandomCoinColor").get("value")

        # Cosmetics: Palette Settings
        if "MarioSetting" in options_dict:
            self.palette_settings.mario_setting = options_dict.get("MarioSetting").get("value")
        if "MarioSprite" in options_dict:
            self.palette_settings.mario_sprite = options_dict.get("MarioSprite").get("value")
        if "GoombarioSetting" in options_dict:
            self.palette_settings.goombario_setting = options_dict.get("GoombarioSetting").get("value")
        if "GoombarioSprite" in options_dict:
            self.palette_settings.goombario_sprite = options_dict.get("GoombarioSprite").get("value")
        if "KooperSetting" in options_dict:
            self.palette_settings.kooper_setting = options_dict.get("KooperSetting").get("value")
        if "KooperSprite" in options_dict:
            self.palette_settings.kooper_sprite = options_dict.get("KooperSprite").get("value")
        if "BombetteSetting" in options_dict:
            self.palette_settings.bombette_setting = options_dict.get("BombetteSetting").get("value")
        if "BombetteSprite" in options_dict:
            self.palette_settings.bombette_sprite = options_dict.get("BombetteSprite").get("value")
        if "ParakarrySetting" in options_dict:
            self.palette_settings.parakarry_setting = options_dict.get("ParakarrySetting").get("value")
        if "ParakarrySprite" in options_dict:
            self.palette_settings.parakarry_sprite = options_dict.get("ParakarrySprite").get("value")
        if "BowSetting" in options_dict:
            self.palette_settings.bow_setting = options_dict.get("BowSetting").get("value")
        if "BowSprite" in options_dict:
            self.palette_settings.bow_sprite = options_dict.get("BowSprite").get("value")
        if "WattSetting" in options_dict:
            self.palette_settings.watt_setting = options_dict.get("WattSetting").get("value")
        if "WattSprite" in options_dict:
            self.palette_settings.watt_sprite = options_dict.get("WattSprite").get("value")
        if "SushieSetting" in options_dict:
            self.palette_settings.sushie_setting = options_dict.get("SushieSetting").get("value")
        if "SushieSprite" in options_dict:
            self.palette_settings.sushie_sprite = options_dict.get("SushieSprite").get("value")
        if "LakilesterSetting" in options_dict:
            self.palette_settings.lakilester_setting = options_dict.get("LakilesterSetting").get("value")
        if "LakilesterSprite" in options_dict:
            self.palette_settings.lakilester_sprite = options_dict.get("LakilesterSprite").get("value")
        if "BossesSetting" in options_dict:
            self.palette_settings.bosses_setting = options_dict.get("BossesSetting").get("value")
        if "EnemiesSetting" in options_dict:
            self.palette_settings.enemies_setting = options_dict.get("EnemiesSetting").get("value")
        if "NPCSetting" in options_dict:
            self.palette_settings.npc_setting = options_dict.get("NPCSetting").get("value")
        if "HammerSetting" in options_dict:
            self.palette_settings.hammer_setting = options_dict.get("HammerSetting").get("value")

        # Audio options
        if "ShuffleMusic" in options_dict:
            self.shuffle_music = options_dict.get("ShuffleMusic").get("value")
        if "ShuffleMusicMode" in options_dict:
            self.shuffle_music_mode = options_dict.get("ShuffleMusicMode").get("value")
        if "ShuffleJingles" in options_dict:
            self.shuffle_jingles = options_dict.get("ShuffleJingles").get("value")

        # Joke options
        if "RomanNumerals" in options_dict:
            self.roman_numerals = options_dict.get("RomanNumerals")
        if "RandomText" in options_dict:
            self.random_text = options_dict.get("RandomText")
        if "RandomPitch" in options_dict:
            self.random_pitch = options_dict.get("RandomPitch")

        # Glitched Logic
        if "PrologueGelEarly" in options_dict:
            self.glitch_settings.prologue_gel_early = options_dict.get("PrologueGelEarly")
        if "ReverseGoombaKingBridge" in options_dict:
            self.glitch_settings.reverse_goomba_king_bridge = options_dict.get("ReverseGoombaKingBridge")
        if "GoombaVillageEntryFenceClip" in options_dict:
            self.glitch_settings.goomba_village_entry_fence_clip = options_dict.get("GoombaVillageEntryFenceClip")
        if "GoombaVillageNpcLureExit" in options_dict:
            self.glitch_settings.goomba_village_npc_lure_exit = options_dict.get("GoombaVillageNpcLureExit")
        if "HammerlessJrPlaygroundLaki" in options_dict:
            self.glitch_settings.hammerless_jr_playground_laki = options_dict.get("HammerlessJrPlaygroundLaki")
        if "GoombaVillageLakiExit" in options_dict:
            self.glitch_settings.goomba_village_laki_exit = options_dict.get("GoombaVillageLakiExit")
        if "PrologueSushieGlitchKsj" in options_dict:
            self.glitch_settings.prologue_sushie_glitch_ksj = options_dict.get("PrologueSushieGlitchKsj")
        if "PrologueSushieGlitchUltraBootsLaki" in options_dict:
            self.glitch_settings.prologue_sushie_glitch_ultra_boots_laki = options_dict.get("PrologueSushieGlitchUltraBootsLaki")

        if "OddKeyEarly" in options_dict:
            self.glitch_settings.odd_key_early = options_dict.get("OddKeyEarly")
        if "BlueHouseSkip" in options_dict:
            self.glitch_settings.blue_house_skip = options_dict.get("BlueHouseSkip")
        if "BlueHouseSkipLaki" in options_dict:
            self.glitch_settings.blue_house_skip_laki = options_dict.get("BlueHouseSkipLaki")
        if "BlueHouseSkipToadLure" in options_dict:
            self.glitch_settings.blue_house_skip_toad_lure = options_dict.get("BlueHouseSkipToadLure")
        if "BowlessToyBoxHammer" in options_dict:
            self.glitch_settings.bowless_toy_box_hammer = options_dict.get("BowlessToyBoxHammer")
        if "BowlessToyBoxHammerlessLure" in options_dict:
            self.glitch_settings.bowless_toy_box_hammerless_lure = options_dict.get("BowlessToyBoxHammerlessLure")
        if "EarlyStoreroomParakarry" in options_dict:
            self.glitch_settings.early_storeroom_parakarry = options_dict.get("EarlyStoreroomParakarry")
        if "EarlyStoreroomHammer" in options_dict:
            self.glitch_settings.early_storeroom_hammer = options_dict.get("EarlyStoreroomHammer")
        if "EarlyStoreroomHammerlessLure" in options_dict:
            self.glitch_settings.early_storeroom_hammerless_lure = options_dict.get("EarlyStoreroomHammerlessLure")
        if "WhaleEarly" in options_dict:
            self.glitch_settings.whale_early = options_dict.get("WhaleEarly")
        if "SushielessToadTownStarPiece" in options_dict:
            self.glitch_settings.sushiesless_toad_town_star_piece = options_dict.get("SushielessToadTownStarPiece")
        if "ToadTownSushieGlitch" in options_dict:
            self.glitch_settings.toad_town_sushie_glitch = options_dict.get("ToadTownSushieGlitch")

        if "ClippyBootsStoneBlockSkip" in options_dict:
            self.glitch_settings.clippy_boots_stone_block_skip = options_dict.get("ClippyBootsStoneBlockSkip")
        if "ClippyBootsMetalBlockSkip" in options_dict:
            self.glitch_settings.clippy_boots_metal_block_skip = options_dict.get("ClippyBootsMetalBlockSkip")
        if "IslandPipeBlooperSkip" in options_dict:
            self.glitch_settings.island_pipe_blooper_skip = options_dict.get("IslandPipeBlooperSkip")
        if "ParakarrylessSewerStarPiece" in options_dict:
            self.glitch_settings.parakarryless_sewer_star_piece = options_dict.get("ParakarrylessSewerStarPiece")
        if "SewerBlocksWithoutUltraBoots" in options_dict:
            self.glitch_settings.sewer_blocks_without_ultra_boots = options_dict.get("SewerBlocksWithoutUltraBoots")
        if "FirstBlockToShiverCityWithoutSuperBoots" in options_dict:
            self.glitch_settings.first_block_to_shiver_city_without_super_boots = options_dict.get("FirstBlockToShiverCityWithoutSuperBoots")
        if "BlocksToShiverCityWithKooperShellItemThrow" in options_dict:
            self.glitch_settings.blocks_to_shiver_city_kooper_shell_item_throw = options_dict.get("BlocksToShiverCityWithKooperShellItemThrow")
        if "SewerYellowBlockWithUltraBoots" in options_dict:
            self.glitch_settings.sewer_yellow_block_with_ultra_boots = options_dict.get("SewerYellowBlockWithUltraBoots")
        if "JumplessSewerShootingStar" in options_dict:
            self.glitch_settings.jumpless_sewer_shooting_star = options_dict.get("JumplessSewerShootingStar")

        if "KooperlessPleasantPathStarPiece" in options_dict:
            self.glitch_settings.kooperless_pleasant_path_star_piece = options_dict.get("KooperlessPleasantPathStarPiece")
        if "HammerlessPleasantPathBridgeUltraBootsParakarry" in options_dict:
            self.glitch_settings.hammerless_pleasant_path_bridge_ultra_boots_parakarry = options_dict.get("HammerlessPleasantPathBridgeUltraBootsParakarry")
        if "InvisibleBridgeClipLzs" in options_dict:
            self.glitch_settings.invisible_bridge_clip_lzs = options_dict.get("InvisibleBridgeClipLzs")
        if "InvisibleBridgeClipLaki" in options_dict:
            self.glitch_settings.invisible_bridge_clip_laki = options_dict.get("InvisibleBridgeClipLaki")
        if "KooperlessPleasantPathThunderBolt" in options_dict:
            self.glitch_settings.kooperless_pleasant_path_thunderbolt = options_dict.get("KooperlessPleasantPathThunderBolt")

        if "BombettelessKbfFpPlusLZS" in options_dict:
            self.glitch_settings.bombetteless_kbf_fp_plus_lzs = options_dict.get("BombettelessKbfFpPlusLZS")
        if "BombettelessKbfFpPlusLaki" in options_dict:
            self.glitch_settings.bombetteless_kbf_fp_plus_laki = options_dict.get("BombettelessKbfFpPlusLaki")
        if "LakiJailbreak" in options_dict:
            self.glitch_settings.laki_jailbreak = options_dict.get("LakiJailbreak")
        if "BombettelessRightFortressJailKey" in options_dict:
            self.glitch_settings.bombetteless_right_fortress_jail_key = options_dict.get("BombettelessRightFortressJailKey")
        if "WaterStaircaseSkip" in options_dict:
            self.glitch_settings.water_staircase_skip = options_dict.get("WaterStaircaseSkip")

        if "MtRuggedQuakeHammerAndLetterWithLaki" in options_dict:
            self.glitch_settings.mt_rugged_quake_hammer_and_letter_with_laki = options_dict.get("MtRuggedQuakeHammerAndLetterWithLaki")
        if "ParakarrylessMtRuggedSeed" in options_dict:
            self.glitch_settings.parakarryless_mt_rugged_seed = options_dict.get("ParakarrylessMtRuggedSeed")
        if "BuzzarGapSkipClippy" in options_dict:
            self.glitch_settings.buzzar_gap_skip_clippy = options_dict.get("BuzzarGapSkipClippy")
        if "ParakarrylessMtRuggedStarPiece" in options_dict:
            self.glitch_settings.parakarryless_mt_rugged_star_piece = options_dict.get("ParakarrylessMtRuggedStarPiece")
        if "MtRuggedCoinsWithKooper" in options_dict:
            self.glitch_settings.mt_rugged_coins_with_kooper = options_dict.get("MtRuggedCoinsWithKooper")
        if "MtRuggedStationJumplessClimbBombette" in options_dict:
            self.glitch_settings.mt_rugged_station_jumpless_climb_bombette = options_dict.get("MtRuggedStationJumplessClimbBombette")
        if "MtRuggedStationJumplessClimbLaki" in options_dict:
            self.glitch_settings.mt_rugged_station_jumpless_climb_laki = options_dict.get("MtRuggedStationJumplessClimbLaki")
        if "JumplessMtRuggedTrainPlatformParakarry" in options_dict:
            self.glitch_settings.jumpless_mt_rugged_train_platform_parakarry = options_dict.get("JumplessMtRuggedTrainPlatformParakarry")

        if "DesertBrickBlockItemWithParakarry" in options_dict:
            self.glitch_settings.desert_brick_block_item_with_parakarry = options_dict.get("DesertBrickBlockItemWithParakarry")
        if "EarlyRuinsLakiJump" in options_dict:
            self.glitch_settings.early_ruins_laki_jump = options_dict.get("EarlyRuinsLakiJump")
        if "EarlyRuinsUltraBoots" in options_dict:
            self.glitch_settings.early_ruins_ultra_boots = options_dict.get("EarlyRuinsUltraBoots")

        if "ArtifactJumpLaki" in options_dict:
            self.glitch_settings.artifact_jump_laki = options_dict.get("ArtifactJumpLaki")
        if "ArtifactJumpUltraBoots" in options_dict:
            self.glitch_settings.artifact_jump_ultra_boots = options_dict.get("ArtifactJumpUltraBoots")
        if "RuinsKeyLakiJump" in options_dict:
            self.glitch_settings.ruins_key_laki_jump = options_dict.get("RuinsKeyLakiJump")
        if "ParakarrylessSecondSandRoomUltraBoots" in options_dict:
            self.glitch_settings.parakarryless_second_sand_room_ultra_boots = options_dict.get("ParakarrylessSecondSandRoomUltraBoots")
        if "ParakarrylessSecondSandRoomNormalBoots" in options_dict:
            self.glitch_settings.parakarryless_second_sand_room_normal_boots = options_dict.get("ParakarrylessSecondSandRoomNormalBoots")
        if "ParakarrylessSuperHammerRoomUltraBoots" in options_dict:
            self.glitch_settings.parakarryless_super_hammer_room_ultra_boots = options_dict.get("ParakarrylessSuperHammerRoomUltraBoots")
        if "ParakarrylessSuperHammerRoomNormalBoots" in options_dict:
            self.glitch_settings.parakarryless_super_hammer_room_normal_boots = options_dict.get("ParakarrylessSuperHammerRoomNormalBoots")
        if "RuinsLocksSkipClippy" in options_dict:
            self.glitch_settings.ruins_locks_skip_clippy = options_dict.get("RuinsLocksSkipClippy")

        if "RecordSkipNoBombettePush" in options_dict:
            self.glitch_settings.record_skip_no_bombette_push = options_dict.get("RecordSkipNoBombettePush")
        if "RecordSkipBombettePush" in options_dict:
            self.glitch_settings.record_skip_bombette_push = options_dict.get("RecordSkipBombettePush")
        if "BoosPortraitWithKooper" in options_dict:
            self.glitch_settings.boos_portrait_with_kooper = options_dict.get("BoosPortraitWithKooper")
        if "BoosPortraitWithLaki" in options_dict:
            self.glitch_settings.boos_portrait_with_laki = options_dict.get("BoosPortraitWithLaki")
        if "JumplessMansionEntry" in options_dict:
            self.glitch_settings.jumpless_mansion_entry = options_dict.get("JumplessMansionEntry")

        if "GustyGulchGateSkipLZS" in options_dict:
            self.glitch_settings.gusty_gulch_gate_skip_lzs = options_dict.get("GustyGulchGateSkipLZS")
        if "GustyGulchGateSkipLaki" in options_dict:
            self.glitch_settings.gusty_gulch_gate_skip_laki = options_dict.get("GustyGulchGateSkipLaki")
        if "KooperlessGustyGulchDizzyDialJump" in options_dict:
            self.glitch_settings.kooperless_gusty_gulch_dizzy_dial_jump = options_dict.get("KooperlessGustyGulchDizzyDialJump")
        if "KooperlessGustyGulchDizzyDialLaki" in options_dict:
            self.glitch_settings.kooperless_gusty_gulch_dizzy_dial_laki = options_dict.get("KooperlessGustyGulchDizzyDialLaki")
        if "KooperlessGustyGulchDizzyDialParakarry" in options_dict:
            self.glitch_settings.kooperless_gusty_gulch_dizzy_dial_parakarry = options_dict.get("KooperlessGustyGulchDizzyDialParakarry")
        if "GustyGulchGapSkip" in options_dict:
            self.glitch_settings.gusty_gulch_gap_skip = options_dict.get("GustyGulchGapSkip")

        if "BowlessTubbasCastle" in options_dict:
            self.glitch_settings.bowless_tubbas_castle = options_dict.get("BowlessTubbasCastle")
        if "TubbasTableLakiJumpClock" in options_dict:
            self.glitch_settings.tubbas_table_laki_jump_clock = options_dict.get("TubbasTableLakiJumpClock")
        if "TubbasTableUltraBoots" in options_dict:
            self.glitch_settings.tubbas_table_ultra_boots = options_dict.get("TubbasTableUltraBoots")
        if "TubbasTableLakiJumpStudy" in options_dict:
            self.glitch_settings.tubbas_table_laki_jump_study = options_dict.get("TubbasTableLakiJumpStudy")
        if "TubbasCastleSuperBootsSkip" in options_dict:
            self.glitch_settings.tubbas_castle_super_boots_skip = options_dict.get("TubbasCastleSuperBootsSkip")
        if "ParakarrylessMegaRush" in options_dict:
            self.glitch_settings.parakarryless_mega_rush = options_dict.get("ParakarrylessMegaRush")

        if "ParakarrylessBlueBuildingStarPiece" in options_dict:
            self.glitch_settings.parakarryless_blue_building_star_piece = options_dict.get("ParakarrylessBlueBuildingStarPiece")
        if "GourmetGuySkipJump" in options_dict:
            self.glitch_settings.gourmet_guy_skip_jump = options_dict.get("GourmetGuySkipJump")
        if "GourmetGuySkipLaki" in options_dict:
            self.glitch_settings.gourmet_guy_skip_laki = options_dict.get("GourmetGuySkipLaki")
        if "GourmetGuySkipParakarry" in options_dict:
            self.glitch_settings.gourmet_guy_skip_parakarry = options_dict.get("GourmetGuySkipParakarry")
        if "BowlessGreenStation" in options_dict:
            self.glitch_settings.bowless_green_station = options_dict.get("BowlessGreenStation")
        if "KooperlessRedStationShootingStar" in options_dict:
            self.glitch_settings.kooperless_red_station_shooting_star = options_dict.get("KooperlessRedStationShootingStar")
        if "GearlessRedStationShootingStar" in options_dict:
            self.glitch_settings.gearless_red_station_shooting_star = options_dict.get("GearlessRedStationShootingStar")
        if "ParakarrylessBlueBlockCityGap" in options_dict:
            self.glitch_settings.parakarryless_blue_block_city_gap = options_dict.get("ParakarrylessBlueBlockCityGap")
        if "BlueSwitchSkipLaki" in options_dict:
            self.glitch_settings.blue_switch_skip_laki = options_dict.get("BlueSwitchSkipLaki")
        if "BlueSwitchSkipUltraBoots" in options_dict:
            self.glitch_settings.blue_switch_skip_ultra_boots = options_dict.get("BlueSwitchSkipUltraBoots")
        if "RedBarricadeSkip" in options_dict:
            self.glitch_settings.red_barricade_skip = options_dict.get("RedBarricadeSkip")
        if "HammerlessBlueStationLaki" in options_dict:
            self.glitch_settings.hammerless_blue_station_laki = options_dict.get("HammerlessBlueStationLaki")
        if "HammerlessPinkStationLaki" in options_dict:
            self.glitch_settings.hammerless_pink_station_laki = options_dict.get("HammerlessPinkStationLaki")

        if "RaphSkipEnglish" in options_dict:
            self.glitch_settings.raph_skip_english = options_dict.get("RaphSkipEnglish")
        if "RaphSkipParakarry" in options_dict:
            self.glitch_settings.raph_skip_parakarry = options_dict.get("RaphSkipParakarry")
        if "Ch5SushieGlitch" in options_dict:
            self.glitch_settings.ch5_sushie_glitch = options_dict.get("Ch5SushieGlitch")
        if "SushielessJungleStarpieceAndLetter" in options_dict:
            self.glitch_settings.sushieless_jungle_starpiece_and_letter = options_dict.get("SushielessJungleStarpieceAndLetter")
        if "JumplessDeepJungleLaki" in options_dict:
            self.glitch_settings.jumpless_deep_jungle_laki = options_dict.get("JumplessDeepJungleLaki")

        if "KooperlessLavalavaPowBlockParakarry" in options_dict:
            self.glitch_settings.kooperless_lavalava_pow_block_parakarry = options_dict.get("KooperlessLavalavaPowBlockParakarry")
        if "KooperlessLavalavaPowBlockSuperBoots" in options_dict:
            self.glitch_settings.kooperless_lavalava_pow_block_super_boots = options_dict.get("KooperlessLavalavaPowBlockSuperBoots")
        if "JumplessLavalavaPowBlock" in options_dict:
            self.glitch_settings.jumpless_lavalava_pow_block = options_dict.get("JumplessLavalavaPowBlock")
        if "UltraHammerSkip" in options_dict:
            self.glitch_settings.ultra_hammer_skip = options_dict.get("UltraHammerSkip")
        if "UltraHammerSkipLaki" in options_dict:
            self.glitch_settings.ultra_hammer_skip_laki = options_dict.get("UltraHammerSkipLaki")
        if "UltraHammerSkipSushie" in options_dict:
            self.glitch_settings.ultra_hammer_skip_sushie = options_dict.get("UltraHammerSkipSushie")
        if "Flarakarry" in options_dict:
            self.glitch_settings.flarakarry = options_dict.get("Flarakarry")
        if "ParakarrylessFlarakarryBombette" in options_dict:
            self.glitch_settings.parakarryless_flarakarry_bombette = options_dict.get("ParakarrylessFlarakarryBombette")
        if "ParakarrylessFlarakarryLaki" in options_dict:
            self.glitch_settings.parakarryless_flarakarry_laki = options_dict.get("ParakarrylessFlarakarryLaki")
        if "VolcanoSushieGlitch" in options_dict:
            self.glitch_settings.volcano_sushie_glitch = options_dict.get("VolcanoSushieGlitch")

        if "EarlyLakiLZS" in options_dict:
            self.glitch_settings.early_laki_lzs = options_dict.get("EarlyLakiLZS")
        if "EarlyLakiBombettePush" in options_dict:
            self.glitch_settings.early_laki_bombette_push = options_dict.get("EarlyLakiBombettePush")
        if "BombettelessMegaSmash" in options_dict:
            self.glitch_settings.bombetteless_mega_smash = options_dict.get("BombettelessMegaSmash")
        if "SunTowerSkip" in options_dict:
            self.glitch_settings.sun_tower_skip = options_dict.get("SunTowerSkip")
        if "YellowBerryGateSkipLZS" in options_dict:
            self.glitch_settings.yellow_berry_gate_skip_lzs = options_dict.get("YellowBerryGateSkipLZS")
        if "YellowBerryGateSkipLaki" in options_dict:
            self.glitch_settings.yellow_berry_gate_skip_laki = options_dict.get("YellowBerryGateSkipLaki")
        if "YellowBerryGateSkipBombettePush" in options_dict:
            self.glitch_settings.yellow_berry_gate_skip_bombette_push = options_dict.get("YellowBerryGateSkipBombettePush")
        if "RedBerryGateSkipBombettePush" in options_dict:
            self.glitch_settings.red_berry_gate_skip_bombette_push = options_dict.get("RedBerryGateSkipBombettePush")
        if "RedBerryGateSkipLaki" in options_dict:
            self.glitch_settings.red_berry_gate_skip_laki = options_dict.get("RedBerryGateSkipLaki")
        if "BlueBerryGateSkipBombettePush" in options_dict:
            self.glitch_settings.blue_berry_gate_skip_bombette_push = options_dict.get("BlueBerryGateSkipBombettePush")
        if "BlueBerryGateSkipLaki" in options_dict:
            self.glitch_settings.blue_berry_gate_skip_laki = options_dict.get("BlueBerryGateSkipLaki")
        if "BubbleBerryTreeLakiJump" in options_dict:
            self.glitch_settings.bubble_berry_tree_early_laki_jump = options_dict.get("BubbleBerryTreeLakiJump")
        if "BubbleBerryTreeUltraBoots" in options_dict:
            self.glitch_settings.bubble_berry_tree_early_ultra_boots = options_dict.get("BubbleBerryTreeUltraBoots")

        if "MurderSolvedEarlyLaki" in options_dict:
            self.glitch_settings.murder_solved_early_laki = options_dict.get("MurderSolvedEarlyLaki")
        if "MurderSolvedEarlyBombettePush" in options_dict:
            self.glitch_settings.murder_solved_early_bombette_push = options_dict.get("MurderSolvedEarlyBombettePush")
        if "Ch7SushieGlitch" in options_dict:
            self.glitch_settings.ch7_sushie_glitch = options_dict.get("Ch7SushieGlitch")
        if "StarStoneWithCh7SushieGlitch" in options_dict:
            self.glitch_settings.star_stone_with_ch7_sushie_glitch = options_dict.get("StarStoneWithCh7SushieGlitch")
        if "ShiverMountainHiddenBlockWithoutUltraBootsLaki" in options_dict:
            self.glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_laki = options_dict.get("ShiverMountainHiddenBlockWithoutUltraBootsLaki")
        if "ShiverMountainHiddenBlockWithoutUltraBootsNoLaki" in options_dict:
            self.glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_no_laki = options_dict.get("ShiverMountainHiddenBlockWithoutUltraBootsNoLaki")
        if "SnowmenSkipLaki" in options_dict:
            self.glitch_settings.snowmen_skip_laki = options_dict.get("SnowmenSkipLaki")
        if "ShiverMountainSwitchSkip" in options_dict:
            self.glitch_settings.shiver_mountain_switch_skip = options_dict.get("ShiverMountainSwitchSkip")
        if "SushielessWarehouseKeyBombette" in options_dict:
            self.glitch_settings.sushieless_warehouse_key_bombette = options_dict.get("SushielessWarehouseKeyBombette")
        if "SushielessWarehouseKeyKooper" in options_dict:
            self.glitch_settings.sushieless_warehouse_key_kooper = options_dict.get("SushielessWarehouseKeyKooper")

        if "MirrorClip" in options_dict:
            self.glitch_settings.mirror_clip = options_dict.get("MirrorClip")

        if "BowlessBowsersCastleBasement" in options_dict:
            self.glitch_settings.bowless_bowsers_castle_basement = options_dict.get("BowlessBowsersCastleBasement")
        if "FastFloodRoomKooper" in options_dict:
            self.glitch_settings.fast_flood_room_kooper = options_dict.get("FastFloodRoomKooper")
        if "FastFloodRoomBombetteUltraBoots" in options_dict:
            self.glitch_settings.fast_flood_room_bombette_ultra_boots = options_dict.get("FastFloodRoomBombetteUltraBoots")
        if "BombettelessBowsersCastleBasement" in options_dict:
            self.glitch_settings.bombetteless_bowsers_castle_basement = options_dict.get("BombettelessBowsersCastleBasement")

        if "BreakYellowBlocksWithSuperBoots" in options_dict:
            self.glitch_settings.break_yellow_blocks_with_super_boots = options_dict.get("BreakYellowBlocksWithSuperBoots")
        if "BreakStoneBlocksWithUltraBoots" in options_dict:
            self.glitch_settings.break_stone_blocks_with_ultra_boots = options_dict.get("BreakStoneBlocksWithUltraBoots")
        if "KnowsHiddenBlocks" in options_dict:
            self.glitch_settings.knows_hidden_blocks = options_dict.get("KnowsHiddenBlocks")
        if "KnowsPuzzleSolutions" in options_dict:
            self.glitch_settings.knows_puzzle_solutions = options_dict.get("KnowsPuzzleSolutions")
        if "ReachHighBlocksWithSuperBoots" in options_dict:
            self.glitch_settings.reach_high_blocks_with_super_boots = options_dict.get("ReachHighBlocksWithSuperBoots")


def validate_options(options_dict):
    if options_dict is None:
        raise ValueError

    def basic_assert(
        option_name:str,
        data_type:type # or tuple(type)
    ):
        try:
            if option_name in options_dict:
                assert isinstance(options_dict.get(option_name).get("value"), data_type)
        except AssertionError as err:
            print(
                f"{option_name}/{type(options_dict.get(option_name).get('value'))}: "\
                    f"Wrong data type, expected '{data_type}'."
            )
            raise

    # General
    basic_assert("BlocksMatchContent", bool)
    if "HiddenBlockMode" in options_dict:
        assert (    isinstance(options_dict.get("HiddenBlockMode").get("value"), int)
                and HiddenBlockMode.VANILLA <= options_dict.get("HiddenBlockMode").get("value") <= HiddenBlockMode.ALWAYS_VISIBLE)
    basic_assert("AllowPhysicsGlitches", bool)
    basic_assert("BadgeSynergy", bool)

    # QOL
    basic_assert("AlwaysSpeedySpin", bool)
    basic_assert("AlwaysISpy", bool)
    basic_assert("AlwaysPeekaboo", bool)
    basic_assert("ShortenCutscenes", bool)
    # ignore FastTextSkip
    basic_assert("SkipEpilogue", bool)
    basic_assert("PeachCastleReturnPipe", bool)
    basic_assert("FoliageItemHints", bool)
    basic_assert("HiddenPanelVisibility", int)

    # Difficulty and Enemies
    basic_assert("ShuffleChapterDifficulty", bool)
    basic_assert("ProgressiveScaling", bool)
    basic_assert("ChallengeMode", bool)
    basic_assert("CapEnemyXP", bool)
    basic_assert("XPMultiplier", (int,float))
    basic_assert("DoubleDamage", bool)
    basic_assert("QuadrupleDamage", bool)
    basic_assert("OHKO", bool)
    basic_assert("NoSaveBlocks", bool)
    basic_assert("NoHeartBlocks", bool)
    basic_assert("NoHealingItems", bool)

    basic_assert("RandomFormations", bool)

    # Custom Seed / Planned Seed / "Plandomizer"
    basic_assert("CustomSeed", bool)

    # Item Placement
    basic_assert("ShuffleItems", bool)
    basic_assert("IncludeCoinsOverworld", bool)
    basic_assert("IncludeCoinsBlocks", bool)
    basic_assert("IncludeCoinsFoliage", bool)
    basic_assert("IncludeCoinsFavors", bool)
    basic_assert("IncludeShops", bool)
    basic_assert("ProgressionOnRowf", bool)
    basic_assert("ProgressionOnMerlow", bool)
    basic_assert("IncludePanels", bool)
    basic_assert("IncludeFavorsMode", int)
    basic_assert("IncludeLettersMode", int)
    basic_assert("IncludeRadioTradeEvent", bool)
    basic_assert("IncludeDojo", bool)
    basic_assert("KeyitemsOutsideDungeon", bool)
    basic_assert("KeyitemsOutsideChapter", bool) #NYI

    # Item Pool Modification
    basic_assert("GearShuffleMode", int)
    basic_assert("AddItemPouches", bool)
    if "RandomConsumableMode" in options_dict:
        assert (    isinstance(options_dict.get("RandomConsumableMode").get("value"), int)
                and RandomizeConsumablesMode.OFF <= options_dict.get("RandomConsumableMode").get("value") <= RandomizeConsumablesMode.MYSTERY_ONLY
        )
    if "ItemQuality" in options_dict:
        assert (    isinstance(options_dict.get("ItemQuality").get("value"), int)
                and 25 <= options_dict.get("ItemQuality").get("value") <= 125
        )
    basic_assert("ItemTrapMode", int)

    # Item Misc
    basic_assert("CookWithoutFryingPan", bool)
    if "MerlowRewardPricing" in options_dict:
        assert (
            isinstance(options_dict.get("MerlowRewardPricing").get("value"), int)
        and MerlowRewardPricing.has_value(options_dict.get("MerlowRewardPricing").get("value"))
        )
    if "RipCheatoItemsInLogic" in options_dict:
        value = options_dict.get("RipCheatoItemsInLogic").get("value")
        assert (    isinstance(value, int)
                and 0 <= value <= 11
        )
    basic_assert("AllowItemHints", bool)
    # Mystery? item options
    basic_assert("RandomChoice", bool)
    basic_assert("MysteryRandomPick", bool)
    if "ItemChoiceA" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceA").get("value"), int)
            and 0x80 <= options_dict.get("ItemChoiceA").get("value") <= 0xDA
        )
    if "ItemChoiceB" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceB").get("value"), int)
            and 0x80 <= options_dict.get("ItemChoiceB").get("value") <= 0xDA
        )
    if "ItemChoiceC" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceC").get("value"), int)
            and 0x80 <= options_dict.get("ItemChoiceC").get("value") <= 0xDA
        )
    if "ItemChoiceD" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceD").get("value"), int)
            and 0x80 <= options_dict.get("ItemChoiceD").get("value") <= 0xDA
        )
    if "ItemChoiceE" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceE").get("value"), int)
            and 0x80 <= options_dict.get("ItemChoiceE").get("value") <= 0xDA
        )
    if "ItemChoiceF" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceF").get("value"), int)
            and 0x80 <= options_dict.get("ItemChoiceF").get("value") <= 0xDA
        )
    if "ItemChoiceG" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceG").get("value"), int)
            and 0x80 <= options_dict.get("ItemChoiceG").get("value") <= 0xDA
        )

    # Starting setup
    basic_assert("StartingMap", int)
    basic_assert("StartingLevel", int)
    basic_assert("StartingMaxHP", int)
    basic_assert("StartingMaxFP", int)
    basic_assert("StartingMaxBP", int)
    if "StartingStarPower" in options_dict:
        assert (    isinstance(options_dict.get("StartingStarPower").get("value"), int)
                and 0 <= options_dict.get("StartingStarPower").get("value") <= 7)
    if "StartingBoots" in options_dict:
        assert (    isinstance(options_dict.get("StartingBoots").get("value"), int)
                and StartingBoots.JUMPLESS <= options_dict.get("StartingBoots").get("value") <= StartingBoots.ULTRABOOTS)
        try:
            if (    "ShuffleItems" in options_dict
                and not options_dict.get("ShuffleItems").get("value")
            ):
                assert (StartingBoots.BOOTS <= options_dict.get("StartingBoots").get("value"))
        except AssertionError:
            raise ValueError(
                "No item shuffle but jumpless start is not a valid setting-combination!",
            )
    if "StartingHammer" in options_dict:
        assert (    isinstance(options_dict.get("StartingHammer").get("value"), int)
                and StartingHammer.HAMMERLESS <= options_dict.get("StartingHammer").get("value") <= StartingHammer.ULTRAHAMMER)
    if "StartingCoins" in options_dict:
        assert (    isinstance(options_dict.get("StartingCoins").get("value"), int)
                and 0 <= options_dict.get("StartingCoins").get("value") <= 999
        )

    basic_assert("StartWithRandomItems", bool)
    if "RandomItemsMin" in options_dict:
        assert (    isinstance(options_dict.get("RandomItemsMin").get("value"), int)
                and 0 <= options_dict.get("RandomItemsMin").get("value") <= 16
                and (   "RandomItemsMax" not in options_dict
                     or options_dict.get("RandomItemsMin").get("value") <=
                        options_dict.get("RandomItemsMax").get("value"))
        )
    if "RandomItemsMax" in options_dict:
        assert (    isinstance(options_dict.get("RandomItemsMax").get("value"), int)
                and 0 <= options_dict.get("RandomItemsMax").get("value") <= 16
                and (   "RandomItemsMin" not in options_dict
                     or options_dict.get("RandomItemsMax").get("value") <=
                        options_dict.get("RandomItemsMax").get("value"))
        )
    basic_assert("StartingItem0", int)
    basic_assert("StartingItem1", int)
    basic_assert("StartingItem2", int)
    basic_assert("StartingItem3", int)
    basic_assert("StartingItem4", int)
    basic_assert("StartingItem5", int)
    basic_assert("StartingItem6", int)
    basic_assert("StartingItem7", int)
    basic_assert("StartingItem8", int)
    basic_assert("StartingItem9", int)
    basic_assert("StartingItemA", int)
    basic_assert("StartingItemB", int)
    basic_assert("StartingItemC", int)
    basic_assert("StartingItemD", int)
    basic_assert("StartingItemE", int)
    basic_assert("StartingItemF", int)

    # Partners
    if "StartWithPartners" in options_dict:
        permitted_values = [
            "Goombario",
            "Kooper",
            "Bombette",
            "Parakarry",
            "Bow",
            "Watt",
            "Sushie",
            "Lakilester"
        ]
        assert (    isinstance(options_dict.get("StartWithPartners").get("value"), dict)
                and all(key in permitted_values for key in options_dict.get("StartWithPartners").get("value"))
                and all(isinstance(value, bool) for value in options_dict.get("StartWithPartners").get("value").values())
                and any(value for value in options_dict.get("StartWithPartners").get("value").values()))

    basic_assert("PartnersInDefaultLocations", bool)
    basic_assert("PartnersAlwaysUsable", bool)
    basic_assert("StartWithRandomPartners", bool)
    if "RandomPartnersMin" in options_dict:
        assert (    isinstance(options_dict.get("RandomPartnersMin").get("value"), int)
                and 1 <= options_dict.get("RandomPartnersMin").get("value") <= 8
                and (   "RandomPartnersMax" not in options_dict
                     or options_dict.get("RandomPartnersMin").get("value") <=
                        options_dict.get("RandomPartnersMax").get("value"))
        )
    if "RandomPartnersMax" in options_dict:
        assert (    isinstance(options_dict.get("RandomPartnersMax").get("value"), int)
                and 1 <= options_dict.get("RandomPartnersMax").get("value") <= 8
                and (   "RandomPartnersMin" not in options_dict
                     or options_dict.get("RandomPartnersMin").get("value") <=
                        options_dict.get("RandomPartnersMax").get("value"))
        )

    # Pre-opened areas
    basic_assert("MagicalSeedsRequired", int)
    basic_assert("PrologueOpen", bool)
    basic_assert("BlueHouseOpen", bool)
    basic_assert("MtRuggedOpen", bool)
    basic_assert("ToyboxOpen", bool)
    basic_assert("WhaleOpen", bool)
    basic_assert("Ch7BridgeVisible", bool)

    # Goal Settings
    if "StarWaySpiritsNeededCnt" in options_dict:
        assert (    isinstance(options_dict.get("StarWaySpiritsNeededCnt").get("value"), int)
                and -1 <= options_dict.get("StarWaySpiritsNeededCnt").get("value") <= 7)
    basic_assert("BowsersCastleMode", int)
    if "StarHunt" in options_dict:
        assert isinstance(options_dict.get("StarHunt").get("value"), bool)
        try:
            if (    "ShuffleItems" in options_dict
                and not options_dict.get("ShuffleItems").get("value")
            ):
                assert (options_dict.get("StarHunt").get("value") is False)
        except AssertionError:
            raise ValueError(
                "No item shuffle but star hunt is not a valid setting-combination!",
            )
    if "StarHuntRequired" in options_dict:
        assert (    isinstance(options_dict.get("StarHuntRequired").get("value"), int)
                and 0 <= options_dict.get("StarHuntRequired").get("value") <= 120
        )
    if "StarHuntTotal" in options_dict:
        assert (    isinstance(options_dict.get("StarHuntTotal").get("value"), int)
                and 0 <= options_dict.get("StarHuntTotal").get("value") <= 120
                and options_dict.get("StarHuntTotal").get("value") >= options_dict.get("StarHuntRequired").get("value")
        )
    basic_assert("StarHuntEndsGame", bool)

    # Entrance Shuffle
    basic_assert("ShuffleDungeonRooms", bool)
    basic_assert("ShuffleDungeonEntrances", bool)
    basic_assert("ShuffleEntrancesByAll", bool)
    basic_assert("MatchEntranceTypes", bool)
    basic_assert("RandomizeOnewayEntrances", bool)
    basic_assert("UnpairedEntrances", bool)

    # Costs of Moves and Badges
    basic_assert("RandomBadgesBP", int)
    basic_assert("RandomBadgesFP", int)
    basic_assert("RandomPartnerFP", int)
    basic_assert("RandomStarpowerSP", int)

    # Misc Gameplay Randomization
    basic_assert("ShuffleBlocks", bool)

    # Quizmo Quizzes
    basic_assert("RandomQuiz", bool)
    basic_assert("QuizmoAlwaysAppears", bool)
    basic_assert("SkipQuiz", bool)

    # Spoilerlog
    basic_assert("WriteSpoilerLog", bool)

    # Cosmetics
    if "Box5ColorA" in options_dict:
        assert (    isinstance(options_dict.get("Box5ColorA").get("value"), int)
                and 0 <= options_dict.get("Box5ColorA").get("value") <= 0xFFFFFFFF
        )
    if "Box5ColorB" in options_dict:
        assert (    isinstance(options_dict.get("Box5ColorB").get("value"), int)
                and 0 <= options_dict.get("Box5ColorB").get("value") <= 0xFFFFFFFF
        )
    if "CoinColor" in options_dict:
        assert (    isinstance(options_dict.get("CoinColor").get("value"), int)
                and 0 <= options_dict.get("CoinColor").get("value") <= 4
        )
    basic_assert("RandomCoinColor", bool)

    basic_assert("MarioSetting", int)
    basic_assert("MarioSprite", int)
    basic_assert("GoombarioSetting", int)
    basic_assert("GoombarioSprite", int)
    basic_assert("KooperSetting", int)
    basic_assert("KooperSprite", int)
    basic_assert("BombetteSetting", int)
    basic_assert("BombetteSprite", int)
    basic_assert("ParakarrySetting", int)
    basic_assert("ParakarrySprite", int)
    basic_assert("BowSetting", int)
    basic_assert("BowSprite", int)
    basic_assert("WattSetting", int)
    basic_assert("WattSprite", int)
    basic_assert("SushieSetting", int)
    basic_assert("SushieSprite", int)
    basic_assert("LakilesterSetting", int)
    basic_assert("LakilesterSprite", int)
    basic_assert("BossesSetting", int)
    basic_assert("EnemiesSetting", int)
    basic_assert("NPCSetting", int)
    basic_assert("HammerSetting", int)

    # Audio options
    basic_assert("ShuffleMusic", bool)
    if "ShuffleMusicMode" in options_dict:
        assert (    isinstance(options_dict.get("ShuffleMusicMode").get("value"), int)
                and 0 <= options_dict.get("ShuffleMusicMode").get("value") <= 2
        )
    basic_assert("ShuffleJingles", bool)

    # Joke options
    basic_assert("RomanNumerals", bool)
    basic_assert("RandomText", bool)
    basic_assert("RandomPitch", bool)

    # Glitched Logic
    basic_assert("PrologueGelEarly", bool)
    basic_assert("ReverseGoombaKingBridge", bool)
    basic_assert("GoombaVillageEntryFenceClip", bool)
    basic_assert("GoombaVillageNpcLureExit", bool)
    basic_assert("HammerlessJrPlaygroundLaki", bool)
    basic_assert("PrologueSushieGlitchKsj", bool)
    basic_assert("PrologueSushieGlitchUltraBootsLaki", bool)
    basic_assert("GoombaVillageLakiExit", bool)

    basic_assert("OddKeyEarly", bool)
    basic_assert("BlueHouseSkip", bool)
    basic_assert("BlueHouseSkipLaki", bool)
    basic_assert("BlueHouseSkipToadLure", bool)
    basic_assert("BowlessToyBoxHammer", bool)
    basic_assert("BowlessToyBoxHammerlessLure", bool)
    basic_assert("EarlyStoreroomParakarry", bool)
    basic_assert("EarlyStoreroomHammer", bool)
    basic_assert("EarlyStoreroomHammerlessLure", bool)
    basic_assert("WhaleEarly", bool)
    basic_assert("SushielessToadTownStarPiece", bool)
    basic_assert("ToadTownSushieGlitch", bool)

    basic_assert("ClippyBootsStoneBlockSkip", bool)
    basic_assert("ClippyBootsMetalBlockSkip", bool)
    basic_assert("IslandPipeBlooperSkip", bool)
    basic_assert("ParakarrylessSewerStarPiece", bool)
    basic_assert("SewerBlocksWithoutUltraBoots", bool)
    basic_assert("FirstBlockToShiverCityWithoutSuperBoots", bool)
    basic_assert("BlocksToShiverCityWithKooperShellItemThrow", bool)
    basic_assert("SewerYellowBlockWithUltraBoots", bool)
    basic_assert("JumplessSewerShootingStar", bool)

    basic_assert("KooperlessPleasantPathStarPiece", bool)
    basic_assert("HammerlessPleasantPathBridgeUltraBootsParakarry", bool)
    basic_assert("InvisibleBridgeClipLzs", bool)
    basic_assert("InvisibleBridgeClipLaki", bool)
    basic_assert("KooperlessPleasantPathThunderBolt", bool)

    basic_assert("BombettelessKbfFpPlusLZS", bool)
    basic_assert("BombettelessKbfFpPlusLaki", bool)
    basic_assert("LakiJailbreak", bool)
    basic_assert("BombettelessRightFortressJailKey", bool)
    basic_assert("WaterStaircaseSkip", bool)

    basic_assert("MtRuggedQuakeHammerAndLetterWithLaki", bool)
    basic_assert("ParakarrylessMtRuggedSeed", bool)
    basic_assert("BuzzarGapSkipClippy", bool)
    basic_assert("ParakarrylessMtRuggedStarPiece", bool)
    basic_assert("MtRuggedCoinsWithKooper", bool)
    basic_assert("MtRuggedStationJumplessClimbBombette", bool)
    basic_assert("MtRuggedStationJumplessClimbLaki", bool)
    basic_assert("JumplessMtRuggedTrainPlatformParakarry", bool)

    basic_assert("DesertBrickBlockItemWithParakarry", bool)
    basic_assert("EarlyRuinsLakiJump", bool)
    basic_assert("EarlyRuinsUltraBoots", bool)

    basic_assert("ArtifactJumpLaki", bool)
    basic_assert("ArtifactJumpUltraBoots", bool)
    basic_assert("RuinsKeyLakiJump", bool)
    basic_assert("ParakarrylessSecondSandRoomUltraBoots", bool)
    basic_assert("ParakarrylessSecondSandRoomNormalBoots", bool)
    basic_assert("ParakarrylessSuperHammerRoomUltraBoots", bool)
    basic_assert("ParakarrylessSuperHammerRoomNormalBoots", bool)
    basic_assert("RuinsLocksSkipClippy", bool)

    basic_assert("RecordSkipNoBombettePush", bool)
    basic_assert("RecordSkipBombettePush", bool)
    basic_assert("BoosPortraitWithKooper", bool)
    basic_assert("BoosPortraitWithLaki", bool)
    basic_assert("JumplessMansionEntry", bool)

    basic_assert("GustyGulchGateSkipLZS", bool)
    basic_assert("GustyGulchGateSkipLaki", bool)
    basic_assert("KooperlessGustyGulchDizzyDialJump", bool)
    basic_assert("KooperlessGustyGulchDizzyDialLaki", bool)
    basic_assert("KooperlessGustyGulchDizzyDialParakarry", bool)
    basic_assert("GustyGulchGapSkip", bool)

    basic_assert("BowlessTubbasCastle", bool)
    basic_assert("TubbasTableLakiJumpClock", bool)
    basic_assert("TubbasTableUltraBoots", bool)
    basic_assert("TubbasTableLakiJumpStudy", bool)
    basic_assert("TubbasCastleSuperBootsSkip", bool)
    basic_assert("ParakarrylessMegaRush", bool)

    basic_assert("ParakarrylessBlueBuildingStarPiece", bool)
    basic_assert("GourmetGuySkipJump", bool)
    basic_assert("GourmetGuySkipLaki", bool)
    basic_assert("GourmetGuySkipParakarry", bool)
    basic_assert("BowlessGreenStation", bool)
    basic_assert("KooperlessRedStationShootingStar", bool)
    basic_assert("GearlessRedStationShootingStar", bool)
    basic_assert("ParakarrylessBlueBlockCityGap", bool)
    basic_assert("BlueSwitchSkipLaki", bool)
    basic_assert("BlueSwitchSkipUltraBoots", bool)
    basic_assert("RedBarricadeSkip", bool)
    basic_assert("HammerlessBlueStationLaki", bool)
    basic_assert("HammerlessPinkStationLaki", bool)

    basic_assert("RaphSkipEnglish", bool)
    basic_assert("RaphSkipParakarry", bool)
    basic_assert("Ch5SushieGlitch", bool)
    basic_assert("SushielessJungleStarpieceAndLetter", bool)
    basic_assert("JumplessDeepJungleLaki", bool)

    basic_assert("KooperlessLavalavaPowBlockParakarry", bool)
    basic_assert("KooperlessLavalavaPowBlockSuperBoots", bool)
    basic_assert("JumplessLavalavaPowBlock", bool)
    basic_assert("UltraHammerSkip", bool)
    basic_assert("UltraHammerSkipLaki", bool)
    basic_assert("UltraHammerSkipSushie", bool)
    basic_assert("Flarakarry", bool)
    basic_assert("ParakarrylessFlarakarryBombette", bool)
    basic_assert("ParakarrylessFlarakarryLaki", bool)
    basic_assert("VolcanoSushieGlitch", bool)

    basic_assert("EarlyLakiLZS", bool)
    basic_assert("EarlyLakiBombettePush", bool)
    basic_assert("BombettelessMegaSmash", bool)
    basic_assert("SunTowerSkip", bool)
    basic_assert("YellowBerryGateSkipLZS", bool)
    basic_assert("YellowBerryGateSkipLaki", bool)
    basic_assert("YellowBerryGateSkipBombettePush", bool)
    basic_assert("RedBerryGateSkipBombettePush", bool)
    basic_assert("RedBerryGateSkipLaki", bool)
    basic_assert("BlueBerryGateSkipBombettePush", bool)
    basic_assert("BlueBerryGateSkipLaki", bool)
    basic_assert("BubbleBerryTreeLakiJump", bool)
    basic_assert("BubbleBerryTreeUltraBoots", bool)

    basic_assert("MurderSolvedEarlyLaki", bool)
    basic_assert("MurderSolvedEarlyBombettePush", bool)
    basic_assert("Ch7SushieGlitch", bool)
    basic_assert("StarStoneWithCh7SushieGlitch", bool)
    basic_assert("ShiverMountainHiddenBlockWithoutUltraBootsLaki", bool)
    basic_assert("ShiverMountainHiddenBlockWithoutUltraBootsNoLaki", bool)
    basic_assert("SnowmenSkipLaki", bool)
    basic_assert("ShiverMountainSwitchSkip", bool)
    basic_assert("SushielessWarehouseKeyBombette", bool)
    basic_assert("SushielessWarehouseKeyKooper", bool)

    basic_assert("MirrorClip", bool)

    basic_assert("BowlessBowsersCastleBasement", bool)
    basic_assert("FastFloodRoomKooper", bool)
    basic_assert("FastFloodRoomBombetteUltraBoots", bool)
    basic_assert("BombettelessBowsersCastleBasement", bool)

    basic_assert("BreakYellowBlocksWithSuperBoots", bool)
    basic_assert("BreakStoneBlocksWithUltraBoots", bool)
    basic_assert("KnowsHiddenBlocks", bool)
    basic_assert("KnowsPuzzleSolutions", bool)
    basic_assert("ReachHighBlocksWithSuperBoots", bool)


def get_option_keyvalue_dict(option_str):
    key = Option.get(Option.name == option_str).get_key()
    value = Option.get(Option.name == option_str).value

    return {"key": key, "value": value}


def populate_keys(data:dict):
    for option_str in data.copy():
        if Option.get_or_none(Option.name == option_str) is not None:
            data[option_str] = {
                "key": Option.get(Option.name == option_str).get_key(),
                "value": data[option_str]
            }
        else:
            data[option_str] = {"value": data[option_str]}


class PaletteOptionSet():
    def __init__(self):
        DEFAULT_PALETTE = 0

        self.mario_setting = DEFAULT_PALETTE
        self.mario_sprite = DEFAULT_PALETTE
        self.goombario_setting = DEFAULT_PALETTE
        self.goombario_sprite = DEFAULT_PALETTE
        self.kooper_setting = DEFAULT_PALETTE
        self.kooper_sprite = DEFAULT_PALETTE
        self.bombette_setting = DEFAULT_PALETTE
        self.bombette_sprite = DEFAULT_PALETTE
        self.parakarry_setting = DEFAULT_PALETTE
        self.parakarry_sprite = DEFAULT_PALETTE
        self.bow_setting = DEFAULT_PALETTE
        self.bow_sprite = DEFAULT_PALETTE
        self.watt_setting = DEFAULT_PALETTE
        self.watt_sprite = DEFAULT_PALETTE
        self.sushie_setting = DEFAULT_PALETTE
        self.sushie_sprite = DEFAULT_PALETTE
        self.lakilester_setting = DEFAULT_PALETTE
        self.lakilester_sprite = DEFAULT_PALETTE

        self.bosses_setting = DEFAULT_PALETTE
        self.enemies_setting = DEFAULT_PALETTE
        self.npc_setting = DEFAULT_PALETTE
        self.hammer_setting = DEFAULT_PALETTE


class MysteryOptionSet():
    def __init__(self):
        self.mystery_random_choice = get_option_keyvalue_dict("RandomChoice")
        self.mystery_random_pick = False
        self.mystery_itemA = get_option_keyvalue_dict("ItemChoiceA")
        self.mystery_itemB = get_option_keyvalue_dict("ItemChoiceB")
        self.mystery_itemC = get_option_keyvalue_dict("ItemChoiceC")
        self.mystery_itemD = get_option_keyvalue_dict("ItemChoiceD")
        self.mystery_itemE = get_option_keyvalue_dict("ItemChoiceE")
        self.mystery_itemF = get_option_keyvalue_dict("ItemChoiceF")
        self.mystery_itemG = get_option_keyvalue_dict("ItemChoiceG")


class GlitchOptionSet():
    def __init__(self):
        self.prologue_gel_early = False
        self.reverse_goomba_king_bridge = False
        self.goomba_village_entry_fence_clip = False
        self.goomba_village_npc_lure_exit = False
        self.hammerless_jr_playground_laki = False
        self.goomba_village_laki_exit = False
        self.prologue_sushie_glitch_ksj = False
        self.prologue_sushie_glitch_ultra_boots_laki = False

        self.odd_key_early = False
        self.blue_house_skip = False
        self.blue_house_skip_laki = False
        self.blue_house_skip_toad_lure = False
        self.bowless_toy_box_hammer = False
        self.bowless_toy_box_hammerless_lure = False
        self.early_storeroom_parakarry = False
        self.early_storeroom_hammer = False
        self.early_storeroom_hammerless_lure = False
        self.whale_early = False
        self.sushiesless_toad_town_star_piece = False
        self.toad_town_sushie_glitch = False

        self.clippy_boots_stone_block_skip = False
        self.clippy_boots_metal_block_skip = False
        self.island_pipe_blooper_skip = False
        self.parakarryless_sewer_star_piece = False
        self.sewer_blocks_without_ultra_boots = False
        self.first_block_to_shiver_city_without_super_boots = False
        self.blocks_to_shiver_city_kooper_shell_item_throw = False
        self.sewer_yellow_block_with_ultra_boots = False
        self.jumpless_sewer_shooting_star = False

        self.kooperless_pleasant_path_star_piece = False
        self.hammerless_pleasant_path_bridge_ultra_boots_parakarry = False
        self.invisible_bridge_clip_lzs = False
        self.invisible_bridge_clip_laki = False
        self.kooperless_pleasant_path_thunderbolt = False

        self.bombetteless_kbf_fp_plus_lzs = False
        self.bombetteless_kbf_fp_plus_laki = False
        self.laki_jailbreak = False
        self.bombetteless_right_fortress_jail_key = False
        self.water_staircase_skip = False

        self.mt_rugged_quake_hammer_and_letter_with_laki = False
        self.parakarryless_mt_rugged_seed = False
        self.buzzar_gap_skip_clippy = False
        self.mt_rugged_coins_with_kooper = False
        self.mt_rugged_station_jumpless_climb_bombette = False
        self.mt_rugged_station_jumpless_climb_laki = False
        self.jumpless_mt_rugged_train_platform_parakarry = False
        self.parakarryless_mt_rugged_star_piece = False
        self.desert_brick_block_item_with_parakarry = False
        self.early_ruins_laki_jump = False
        self.early_ruins_ultra_boots = False

        self.artifact_jump_laki = False
        self.artifact_jump_ultra_boots = False
        self.ruins_key_laki_jump = False
        self.parakarryless_second_sand_room_ultra_boots = False
        self.parakarryless_second_sand_room_normal_boots = False
        self.parakarryless_super_hammer_room_ultra_boots = False
        self.parakarryless_super_hammer_room_normal_boots = False
        self.ruins_locks_skip_clippy = False

        self.record_skip_no_bombette_push = False
        self.record_skip_bombette_push = False
        self.boos_portrait_with_kooper = False
        self.boos_portrait_with_laki = False
        self.jumpless_mansion_entry = False

        self.gusty_gulch_gate_skip_lzs = False
        self.gusty_gulch_gate_skip_laki = False
        self.kooperless_gusty_gulch_dizzy_dial_jump = False
        self.kooperless_gusty_gulch_dizzy_dial_laki = False
        self.kooperless_gusty_gulch_dizzy_dial_parakarry = False
        self.gusty_gulch_gap_skip = False

        self.bowless_tubbas_castle = False
        self.tubbas_table_laki_jump_clock = False
        self.tubbas_table_ultra_boots = False
        self.tubbas_table_laki_jump_study = False
        self.tubbas_castle_super_boots_skip = False
        self.parakarryless_mega_rush = False

        self.parakarryless_blue_building_star_piece = False
        self.gourmet_guy_skip_jump = False
        self.gourmet_guy_skip_laki = False
        self.gourmet_guy_skip_parakarry = False
        self.bowless_green_station = False
        self.kooperless_red_station_shooting_star = False
        self.gearless_red_station_shooting_star = False
        self.parakarryless_blue_block_city_gap = False
        self.blue_switch_skip_laki = False
        self.blue_switch_skip_ultra_boots = False
        self.red_barricade_skip = False
        self.hammerless_blue_station_laki = False
        self.hammerless_pink_station_laki = False

        self.raph_skip_english = False
        self.raph_skip_parakarry = False
        self.ch5_sushie_glitch = False
        self.sushieless_jungle_starpiece_and_letter = False
        self.jumpless_deep_jungle_laki = False
        self.kooperless_lavalava_pow_block_parakarry = False
        self.kooperless_lavalava_pow_block_super_boots = False
        self.jumpless_lavalava_pow_block = False
        self.ultra_hammer_skip = False
        self.ultra_hammer_skip_laki = False
        self.ultra_hammer_skip_sushie = False
        self.flarakarry = False
        self.parakarryless_flarakarry_bombette = False
        self.parakarryless_flarakarry_laki = False
        self.volcano_sushie_glitch = False

        self.early_laki_lzs = False
        self.early_laki_bombette_push = False
        self.bombetteless_mega_smash = False
        self.sun_tower_skip = False
        self.yellow_berry_gate_skip_lzs = False
        self.yellow_berry_gate_skip_laki = False
        self.yellow_berry_gate_skip_bombette_push = False
        self.red_berry_gate_skip_bombette_push = False
        self.red_berry_gate_skip_laki = False
        self.blue_berry_gate_skip_bombette_push = False
        self.blue_berry_gate_skip_laki = False
        self.bubble_berry_tree_early_laki_jump = False
        self.bubble_berry_tree_early_ultra_boots = False

        self.murder_solved_early_laki = False
        self.murder_solved_early_bombette_push = False
        self.ch7_sushie_glitch = False
        self.star_stone_with_ch7_sushie_glitch = False
        self.shiver_mountain_hidden_block_without_ultra_boots_laki = False
        self.shiver_mountain_hidden_block_without_ultra_boots_no_laki = False
        self.snowmen_skip_laki = False
        self.shiver_mountain_switch_skip = False
        self.sushieless_warehouse_key_bombette = False
        self.sushieless_warehouse_key_kooper = False

        self.mirror_clip = False

        self.bowless_bowsers_castle_basement = False
        self.fast_flood_room_kooper = False
        self.fast_flood_room_bombette_ultra_boots = False
        self.bombetteless_bowsers_castle_basement = False

        self.break_yellow_blocks_with_super_boots = False
        self.break_stone_blocks_with_ultra_boots = False
        self.knows_hidden_blocks = False
        self.knows_puzzle_solutions = False
        self.reach_high_blocks_with_super_boots = False
