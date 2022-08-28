from db.item import Item
from db.option import Option
from db.palette import Palette

class OptionSet:
    def __init__(self):
        """ Load Defaults from DB """
        # General
        self.starting_coins = get_option_keyvalue_dict("StartingCoins")
        self.shorten_cutscenes = get_option_keyvalue_dict("ShortenCutscenes")
        self.magical_seeds_required = get_option_keyvalue_dict("MagicalSeedsRequired")
        self.bluehouse_open = get_option_keyvalue_dict("BlueHouseOpen")
        self.blocks_match_content = get_option_keyvalue_dict("BlocksMatchContent")
        self.skip_quiz = get_option_keyvalue_dict("SkipQuiz")
        self.challenge_mode = get_option_keyvalue_dict("ChallengeMode")
        self.cap_enemy_xp = get_option_keyvalue_dict("CapEnemyXP")
        self.no_xp = get_option_keyvalue_dict("NoXP")
        self.damage_x2 = get_option_keyvalue_dict("DoubleDamage")
        self.damage_x4 = get_option_keyvalue_dict("QuadrupleDamage")
        self.ohko = get_option_keyvalue_dict("OHKO")
        self.no_save_blocks = get_option_keyvalue_dict("NoSaveBlocks")
        self.no_heart_blocks = get_option_keyvalue_dict("NoHeartBlocks")
        self.no_healing_items = get_option_keyvalue_dict("NoHealingItems")

        # Item related
        self.shuffle_items = get_option_keyvalue_dict("ShuffleItems")
        self.include_coins = get_option_keyvalue_dict("IncludeCoins")
        self.include_shops = get_option_keyvalue_dict("IncludeShops")
        self.include_panels = get_option_keyvalue_dict("IncludePanels")

        # Entrance related
        self.shuffle_entrances = get_option_keyvalue_dict("ShuffleEntrances")
        self.shuffle_entrances_by_area = get_option_keyvalue_dict("ShuffleEntrancesByArea")
        self.shuffle_entrances_by_all = get_option_keyvalue_dict("ShuffleEntrancesByAll")
        self.match_entrance_type = get_option_keyvalue_dict("MatchEntranceTypes")

        # Settings unavailable in the GUI
        # General
        self.random_quiz = get_option_keyvalue_dict("RandomQuiz")
        self.quizmo_always_appears = get_option_keyvalue_dict("QuizmoAlwaysAppears")
        self.shuffle_chapter_difficulty = False
        self.progressive_scaling = get_option_keyvalue_dict("ProgressiveScaling")
        self.random_formations = get_option_keyvalue_dict("RandomFormations")
        self.toybox_open = get_option_keyvalue_dict("ToyboxOpen")
        self.whale_open = get_option_keyvalue_dict("WhaleOpen")
        self.always_speedyspin = get_option_keyvalue_dict("AlwaysSpeedySpin")
        self.always_ispy = get_option_keyvalue_dict("AlwaysISpy")
        self.always_peekaboo = get_option_keyvalue_dict("AlwaysPeekaboo")
        self.hidden_block_mode = get_option_keyvalue_dict("HiddenBlockMode")
        self.skip_epilogue = get_option_keyvalue_dict("SkipEpilogue")
        self.allow_physics_glitches = get_option_keyvalue_dict("AllowPhysicsGlitches")
        self.starway_spirits_needed = get_option_keyvalue_dict("StarWaySpiritsNeeded")
        self.peachcastle_return_pipe = get_option_keyvalue_dict("PeachCastleReturnPipe")
        self.foliage_item_hints = get_option_keyvalue_dict("FoliageItemHints")
        self.hiddenpanel_visibility = get_option_keyvalue_dict("HiddenPanelVisibility")

        # Starting setup
        self.starting_map = get_option_keyvalue_dict("StartingMap") # mac_00 Entry 4
        self.starting_level = get_option_keyvalue_dict("StartingLevel")
        self.starting_maxhp = get_option_keyvalue_dict("StartingMaxHP")
        self.starting_maxfp = get_option_keyvalue_dict("StartingMaxFP")
        self.starting_maxbp = get_option_keyvalue_dict("StartingMaxBP")
        self.starting_starpower = get_option_keyvalue_dict("StartingStarPower")
        self.starting_boots = get_option_keyvalue_dict("StartingBoots")
        self.starting_hammer = get_option_keyvalue_dict("StartingHammer")

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

        # Item related
        self.include_favors_mode = 0
        self.include_letters_mode = 0
        self.include_radiotradeevent = False
        self.include_dojo = False
        self.gear_shuffle_mode = get_option_keyvalue_dict("GearShuffleMode")
        self.item_scarcity = 0
        self.add_item_pouches = False
        self.placement_algorithm = "ForwardFill"
        self.placement_logic = "NoGlitches"
        self.keyitems_outside_dungeon = True # False -> NYI
        self.keyitems_outside_chapter = True # "Keysanity" # false -> NYI
        self.allow_itemhints = True
        self.itemtrap_mode = 0
        # Mystery? item options
        self.mystery_settings = MysteryOptionSet()

        # Blocks related
        self.shuffle_blocks = False

        # Moves and Badges
        self.random_badges_bp = 0
        self.random_badges_fp = 0
        self.random_partner_fp = 0
        self.random_starpower_sp = 0

        # Entrance related
        self.bowsers_castle_mode = get_option_keyvalue_dict("BowsersCastleMode")
        self.random_oneway_entrances = False # NYI
        self.unpaired_entrances = False # NYI

        # Partner related
        self.partners_in_default_locations = True
        self.partners_always_usable = get_option_keyvalue_dict("PartnersAlwaysUsable")
        self.random_partners = False
        self.random_partners_min = 1
        self.random_partners_max = 1
        self.starting_partners = ["Goombario"]
        self.start_with_goombario = get_option_keyvalue_dict("StartWithGoombario")
        self.start_with_kooper = get_option_keyvalue_dict("StartWithKooper")
        self.start_with_bombette = get_option_keyvalue_dict("StartWithBombette")
        self.start_with_parakarry = get_option_keyvalue_dict("StartWithParakarry")
        self.start_with_bow = get_option_keyvalue_dict("StartWithBow")
        self.start_with_watt = get_option_keyvalue_dict("StartWithWatt")
        self.start_with_sushie = get_option_keyvalue_dict("StartWithSushie")
        self.start_with_lakilester = get_option_keyvalue_dict("StartWithLakilester")

        # Spoilerlog
        self.write_spoilerlog = True
        self.pretty_spoilerlog = True

        # Cosmetics
        self.color_a = get_option_keyvalue_dict("Box5ColorA")
        self.color_b = get_option_keyvalue_dict("Box5ColorB")
        self.roman_numerals = get_option_keyvalue_dict("RomanNumerals")
        self.random_text = get_option_keyvalue_dict("RandomText")
        self.coin_color = get_option_keyvalue_dict("CoinColor")
        self.random_coin_color = False

        self.palette_settings = PaletteOptionSet()

        # Glitched logic options
        self.glitch_settings = GlitchOptionSet()

        # Audio
        self.random_pitch = get_option_keyvalue_dict("RandomPitch")


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
                        if (item_obj.item_type in ["BADGE", "KEYITEM", "STARPIECE"]
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
            print(f"{err.args}: Settings file includes invalid data.")
            raise

        # General
        if "StartingCoins" in options_dict:
            self.starting_coins = options_dict.get("StartingCoins")
        if "ShortenCutscenes" in options_dict:
            self.shorten_cutscenes = options_dict.get("ShortenCutscenes")
        if "MagicalSeedsRequired" in options_dict:
            self.magical_seeds_required = options_dict.get("MagicalSeedsRequired")
        if "BlueHouseOpen" in options_dict:
            self.bluehouse_open = options_dict.get("BlueHouseOpen")
        if "BlocksMatchContent" in options_dict:
            self.blocks_match_content = options_dict.get("BlocksMatchContent")
        if "SkipQuiz" in options_dict:
            self.skip_quiz = options_dict.get("SkipQuiz")
        if "ChallengeMode" in options_dict:
            self.challenge_mode = options_dict.get("ChallengeMode")
        if "CapEnemyXP" in options_dict:
            self.cap_enemy_xp = options_dict.get("CapEnemyXP")
        if "NoXP" in options_dict:
            self.no_xp = options_dict.get("NoXP")
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

        # Item related
        if "ShuffleItems" in options_dict:
            self.shuffle_items = options_dict.get("ShuffleItems")
        if "IncludeCoins" in options_dict:
            self.include_coins = options_dict.get("IncludeCoins")
        if "IncludeShops" in options_dict:
            self.include_shops = options_dict.get("IncludeShops")
        if "IncludePanels" in options_dict:
            self.include_panels = options_dict.get("IncludePanels")

        # Entrance related
        if "ShuffleEntrances" in options_dict:
            self.shuffle_entrances = options_dict.get("ShuffleEntrances")
        if "ShuffleEntrancesByArea" in options_dict:
            self.shuffle_entrances_by_area = options_dict.get("ShuffleEntrancesByArea")
        if "ShuffleEntrancesByAll" in options_dict:
            self.shuffle_entrances_by_all = options_dict.get("ShuffleEntrancesByAll")
        if "MatchEntranceTypes" in options_dict:
            self.match_entrance_type = options_dict.get("MatchEntranceTypes")

        # Settings unavailable in the GUI
        # General
        if "RandomQuiz" in options_dict:
            self.random_quiz = options_dict.get("RandomQuiz")
        if "QuizmoAlwaysAppears" in options_dict:
            self.quizmo_always_appears = options_dict.get("QuizmoAlwaysAppears")
        if "ShuffleChapterDifficulty" in options_dict:
            self.shuffle_chapter_difficulty = options_dict.get("ShuffleChapterDifficulty").get("value")
        if "ProgressiveScaling" in options_dict:
            self.progressive_scaling = options_dict.get("ProgressiveScaling")
        if "RandomFormations" in options_dict:
            self.random_formations = options_dict.get("RandomFormations")
        if "ToyboxOpen" in options_dict:
            self.toybox_open = options_dict.get("ToyboxOpen")
        if "WhaleOpen" in options_dict:
            self.whale_open = options_dict.get("WhaleOpen")
        if "AlwaysSpeedySpin" in options_dict:
            self.always_speedyspin = options_dict.get("AlwaysSpeedySpin")
        if "AlwaysISpy" in options_dict:
            self.always_ispy = options_dict.get("AlwaysISpy")
        if "AlwaysPeekaboo" in options_dict:
            self.always_peekaboo = options_dict.get("AlwaysPeekaboo")
        if "HiddenBlockMode" in options_dict:
            self.hidden_block_mode = options_dict.get("HiddenBlockMode")
        if "SkipEpilogue" in options_dict:
            self.skip_epilogue = options_dict.get("SkipEpilogue")
        if "AllowPhysicsGlitches" in options_dict:
            self.allow_physics_glitches = options_dict.get("AllowPhysicsGlitches")
        if "StarWaySpiritsNeeded" in options_dict:
            self.starway_spirits_needed = options_dict.get("StarWaySpiritsNeeded")
        if "PeachCastleReturnPipe" in options_dict:
            self.peachcastle_return_pipe = options_dict.get("PeachCastleReturnPipe")
        if "FoliageItemHints" in options_dict:
            self.foliage_item_hints = options_dict.get("FoliageItemHints")
        if "HiddenPanelVisibility" in options_dict:
            self.hiddenpanel_visibility = options_dict.get("HiddenPanelVisibility")

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
            if self.starting_boots.get("value") == -1:
                self.starting_boots["value"] = 0xFF
        if "StartingHammer" in options_dict:
            self.starting_hammer = options_dict.get("StartingHammer")
            if self.starting_hammer.get("value") == -1:
                self.starting_hammer["value"] = 0xFF

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

        # Item related
        if "IncludeFavorsMode" in options_dict:
            self.include_favors_mode = options_dict.get("IncludeFavorsMode").get("value")
        if "IncludeLettersMode" in options_dict:
            self.include_letters_mode = options_dict.get("IncludeLettersMode").get("value")
        if "IncludeRadioTradeEvent" in options_dict:
            self.include_radiotradeevent = options_dict.get("IncludeRadioTradeEvent").get("value")
        if "IncludeDojo" in options_dict:
            self.include_dojo = options_dict.get("IncludeDojo").get("value")
        if "GearShuffleMode" in options_dict:
            self.gear_shuffle_mode = options_dict.get("GearShuffleMode")
        if "ItemScarcity" in options_dict:
            self.item_scarcity = options_dict.get("ItemScarcity").get("value")
        if "AddItemPouches" in options_dict:
            self.add_item_pouches = options_dict.get("AddItemPouches").get("value")
        if "PlacementAlgorithm" in options_dict:
            self.placement_algorithm = options_dict.get("PlacementAlgorithm").get("value")
        if "PlacementLogic" in options_dict:
            self.placement_logic = options_dict.get("PlacementLogic").get("value")
        if "KeyitemsOutsideDungeon" in options_dict:
            self.keyitems_outside_dungeon = options_dict.get("KeyitemsOutsideDungeon").get("value")
        if "KeyitemsOutsideChapter" in options_dict:
            self.keyitems_outside_chapter = options_dict.get("KeyitemsOutsideChapter").get("value")
        if "AllowItemHints" in options_dict:
            self.allow_itemhints = options_dict.get("AllowItemHints").get("value")
        if "ItemTrapMode" in options_dict:
            self.itemtrap_mode = options_dict.get("ItemTrapMode").get("value")
        # Mystery? item options
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

        # Blocks related
        if "ShuffleBlocks" in options_dict:
            self.shuffle_blocks = options_dict.get("ShuffleBlocks").get("value")

        # Moves and Badges
        if "RandomBadgesBP" in options_dict:
            self.random_badges_bp = options_dict.get("RandomBadgesBP").get("value")
        if "RandomBadgesFP" in options_dict:
            self.random_badges_fp = options_dict.get("RandomBadgesFP").get("value")
        if "RandomPartnerFP" in options_dict:
            self.random_partner_fp = options_dict.get("RandomPartnerFP").get("value")
        if "RandomStarpowerSP" in options_dict:
            self.random_starpower_sp = options_dict.get("RandomStarpowerSP").get("value")

        # Entrance related
        if "BowsersCastleMode" in options_dict:
            self.bowsers_castle_mode = options_dict.get("BowsersCastleMode")
        if "RandomizeOnewayEntrances" in options_dict:
            self.random_oneway_entrances = options_dict.get("RandomizeOnewayEntrances").get("value")
        if "UnpairedEntrances" in options_dict:
            self.unpaired_entrances = options_dict.get("UnpairedEntrances").get("value")

        # Partner related
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

        # Spoilerlog
        if "WriteSpoilerLog" in options_dict:
            self.write_spoilerlog = options_dict.get("WriteSpoilerLog").get("value")
        if "PrettySpoilerlog" in options_dict:
            self.pretty_spoilerlog = options_dict.get("PrettySpoilerlog").get("value")

        # Cosmetics / Palettes
        if "RomanNumerals" in options_dict:
            self.roman_numerals = options_dict.get("RomanNumerals")
        if "RandomText" in options_dict:
            self.random_text = options_dict.get("RandomText")
        if "CoinColor" in options_dict:
            self.coin_color = options_dict.get("CoinColor")
        if "RandomCoinColor" in options_dict:
            self.random_coin_color = options_dict.get("RandomCoinColor").get("value")
        if "Box5ColorA" in options_dict:
            self.color_a = options_dict.get("Box5ColorA")
        if "Box5ColorB" in options_dict:
            self.color_b = options_dict.get("Box5ColorB")

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
        #if "LakilesterSetting" in options_dict:
        #    self.palette_settings.lakilester_setting = options_dict.get("LakilesterSetting").get("value")
        #if "LakilesterSprite" in options_dict:
        #    self.palette_settings.lakilester_sprite = options_dict.get("LakilesterSprite").get("value")
        if "BossesSetting" in options_dict:
            self.palette_settings.bosses_setting = options_dict.get("BossesSetting").get("value")
        if "EnemiesSetting" in options_dict:
            self.palette_settings.enemies_setting = options_dict.get("EnemiesSetting").get("value")
        if "NPCSetting" in options_dict:
            self.palette_settings.npc_setting = options_dict.get("NPCSetting").get("value")

        # Glitched Logic
        if "PrologueGelEarly" in options_dict:
            self.glitch_settings.prologue_gel_early = options_dict.get("PrologueGelEarly")
        if "ReverseGoombaKingBridge" in options_dict:
            self.glitch_settings.reverse_goomba_king_bridge = options_dict.get("ReverseGoombaKingBridge")
        if "GoombaVillageEntryFenceClip" in options_dict:
            self.glitch_settings.goomba_village_entry_fence_clip = options_dict.get("GoombaVillageEntryFenceClip")
        if "GoombaVillageSuperBootsExit" in options_dict:
            self.glitch_settings.goomba_village_super_boots_exit = options_dict.get("GoombaVillageSuperBootsExit")
        if "HammerlessJrPlaygroundLaki" in options_dict:
            self.glitch_settings.hammerless_jr_playground_laki = options_dict.get("HammerlessJrPlaygroundLaki")
        if "GoombaVillageLakiExit" in options_dict:
            self.glitch_settings.goomba_village_laki_exit = options_dict.get("GoombaVillageLakiExit")

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
        if "BowlessToyBoxParakarry" in options_dict:
            self.glitch_settings.bowless_toy_box_parakarry = options_dict.get("BowlessToyBoxParakarry")
        if "BowlessToyBoxUltraBoots" in options_dict:
            self.glitch_settings.bowless_toy_box_ultra_boots = options_dict.get("BowlessToyBoxUltraBoots")
        if "EarlyStoreroomParakarry" in options_dict:
            self.glitch_settings.early_storeroom_parakarry = options_dict.get("EarlyStoreroomParakarry")
        if "EarlyStoreroomHammer" in options_dict:
            self.glitch_settings.early_storeroom_hammer = options_dict.get("EarlyStoreroomHammer")
        if "EarlyStoreroomUltraBoots" in options_dict:
            self.glitch_settings.early_storeroom_ultra_boots = options_dict.get("EarlyStoreroomUltraBoots")
        if "WhaleEarly" in options_dict:
            self.glitch_settings.whale_early = options_dict.get("WhaleEarly")
        if "SushielessToadTownStarPiece" in options_dict:
            self.glitch_settings.sushiesless_toad_town_star_piece = options_dict.get("SushielessToadTownStarPiece")

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

        if "KooperlessPleasantPathStarPiece" in options_dict:
            self.glitch_settings.kooperless_pleasant_path_star_piece = options_dict.get("KooperlessPleasantPathStarPiece")
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

        if "DesertBrickBlockItemWithParakarry" in options_dict:
            self.glitch_settings.desert_brick_block_item_with_parakarry = options_dict.get("DesertBrickBlockItemWithParakarry")
        if "EarlyRuinsLakiJump" in options_dict:
            self.glitch_settings.early_ruins_laki_jump = options_dict.get("EarlyRuinsLakiJump")
        if "EarlyRuinsUltraBoots" in options_dict:
            self.glitch_settings.early_ruins_ultra_boots = options_dict.get("EarlyRuinsUltraBoots")

        if "ArtifactJump" in options_dict:
            self.glitch_settings.artifact_jump = options_dict.get("ArtifactJump")
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
        if "TubbasTableLakiJump" in options_dict:
            self.glitch_settings.tubbas_table_laki_jump = options_dict.get("TubbasTableLakiJump")
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
        if "ParakarrylessBlueBlockCityGap" in options_dict:
            self.glitch_settings.parakarryless_blue_block_city_gap = options_dict.get("ParakarrylessBlueBlockCityGap")
        if "BlueSwitchSkip" in options_dict:
            self.glitch_settings.blue_switch_skip = options_dict.get("BlueSwitchSkip")
        if "RedBarricadeSkip" in options_dict:
            self.glitch_settings.red_barricade_skip = options_dict.get("RedBarricadeSkip")

        if "RaphSkipEnglish" in options_dict:
            self.glitch_settings.raph_skip_english = options_dict.get("RaphSkipEnglish")
        if "Ch5SushieGlitch" in options_dict:
            self.glitch_settings.ch5_sushie_glitch = options_dict.get("Ch5SushieGlitch")

        if "KooperlessLavalavaPowBlock" in options_dict:
            self.glitch_settings.kooperless_lavalava_pow_block = options_dict.get("KooperlessLavalavaPowBlock")
        if "UltraHammerSkip" in options_dict:
            self.glitch_settings.ultra_hammer_skip = options_dict.get("UltraHammerSkip")
        if "UltraHammerSkipLaki" in options_dict:
            self.glitch_settings.ultra_hammer_skip_laki = options_dict.get("UltraHammerSkipLaki")
        if "Flarakarry" in options_dict:
            self.glitch_settings.flarakarry = options_dict.get("Flarakarry")
        if "ParakarrylessFlarakarryBombette" in options_dict:
            self.glitch_settings.parakarryless_flarakarry_bombette = options_dict.get("ParakarrylessFlarakarryBombette")
        if "ParakarrylessFlarakarryLaki" in options_dict:
            self.glitch_settings.parakarryless_flarakarry_laki = options_dict.get("ParakarrylessFlarakarryLaki")

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
            self.glitch_settings.bubble_berry_tree_laki_jump = options_dict.get("BubbleBerryTreeLakiJump")

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

        if "MirrorClip" in options_dict:
            self.glitch_settings.mirror_clip = options_dict.get("MirrorClip")

        if "BowlessBowsersCastleBasement" in options_dict:
            self.glitch_settings.bowless_bowsers_castle_basement = options_dict.get("BowlessBowsersCastleBasement")
        if "FastFloodRoomKooper" in options_dict:
            self.glitch_settings.fast_flood_room_kooper = options_dict.get("FastFloodRoomKooper")
        if "FastFloodRoomBombetteUltraBoots" in options_dict:
            self.glitch_settings.fast_flood_room_bombette_ultra_boots = options_dict.get("FastFloodRoomBombetteUltraBoots")

        if "BreakYellowBlocksWithSuperBoots" in options_dict:
            self.glitch_settings.break_yellow_blocks_with_super_boots = options_dict.get("BreakYellowBlocksWithSuperBoots")
        if "BreakMetalBlocksWithUltraBoots" in options_dict:
            self.glitch_settings.break_metal_blocks_with_ultra_boots = options_dict.get("BreakMetalBlocksWithUltraBoots")
        if "KnowsHiddenBlocks" in options_dict:
            self.glitch_settings.knows_hidden_blocks = options_dict.get("KnowsHiddenBlocks")
        if "KnowsPuzzleSolutions" in options_dict:
            self.glitch_settings.knows_puzzle_solutions = options_dict.get("KnowsPuzzleSolutions")
        if "ReachHighBlocksWithSuperBoots" in options_dict:
            self.glitch_settings.reach_high_blocks_with_super_boots = options_dict.get("ReachHighBlocksWithSuperBoots")
              
        # Audio
        if "RandomPitch" in options_dict:
            self.random_pitch = options_dict.get("RandomPitch")


def validate_options(options_dict):
    if options_dict is None:
        raise ValueError

    # General
    if "StartingCoins" in options_dict:
        assert (isinstance(options_dict.get("StartingCoins").get("value"), int)
            and 0 <= options_dict.get("StartingCoins").get("value") <= 999
        )
    if "ShortenCutscenes" in options_dict:
        assert isinstance(options_dict.get("ShortenCutscenes").get("value"), bool)
    if "MagicalSeedsRequired" in options_dict:
        assert isinstance(options_dict.get("MagicalSeedsRequired").get("value"), int)
    if "BlueHouseOpen" in options_dict:
        assert isinstance(options_dict.get("BlueHouseOpen").get("value"), bool)
    if "BlocksMatchContent" in options_dict:
        assert isinstance(options_dict.get("BlocksMatchContent").get("value"), bool)
    if "SkipQuiz" in options_dict:
        assert isinstance(options_dict.get("SkipQuiz").get("value"), bool)
    if "ChallengeMode" in options_dict:
        assert isinstance(options_dict.get("ChallengeMode").get("value"), bool)
    if "CapEnemyXP" in options_dict:
        assert isinstance(options_dict.get("CapEnemyXP").get("value"), bool)
    if "NoXP" in options_dict:
        assert isinstance(options_dict.get("NoXP").get("value"), bool)
    if "DoubleDamage" in options_dict:
        assert isinstance(options_dict.get("DoubleDamage").get("value"), bool)
    if "QuadrupleDamage" in options_dict:
        assert isinstance(options_dict.get("QuadrupleDamage").get("value"), bool)
    if "OHKO" in options_dict:
        assert isinstance(options_dict.get("OHKO").get("value"), bool)
    if "NoSaveBlocks" in options_dict:
        assert isinstance(options_dict.get("NoSaveBlocks").get("value"), bool)
    if "NoHeartBlocks" in options_dict:
        assert isinstance(options_dict.get("NoHeartBlocks").get("value"), bool)
    if "NoHealingItems" in options_dict:
        assert isinstance(options_dict.get("NoHealingItems").get("value"), bool)

    # Item related
    if "ShuffleItems" in options_dict:
        assert isinstance(options_dict.get("ShuffleItems").get("value"), bool)
    if "IncludeCoins" in options_dict:
        assert isinstance(options_dict.get("IncludeCoins").get("value"), bool)
    if "IncludeShops" in options_dict:
        assert isinstance(options_dict.get("IncludeShops").get("value"), bool)
    if "IncludePanels" in options_dict:
        assert isinstance(options_dict.get("IncludePanels").get("value"), bool)

    # Entrance related
    if "ShuffleEntrances" in options_dict:
        assert isinstance(options_dict.get("ShuffleEntrances").get("value"), bool)
    if "ShuffleEntrancesByArea" in options_dict:
        assert isinstance(options_dict.get("ShuffleEntrancesByArea").get("value"), bool)
    if "ShuffleEntrancesByAll" in options_dict:
        assert isinstance(options_dict.get("ShuffleEntrancesByAll").get("value"), bool)
    if "MatchEntranceTypes" in options_dict:
        assert isinstance(options_dict.get("MatchEntranceTypes").get("value"), bool)

    # Settings unavailable in the GUI
    # General
    if "RandomQuiz" in options_dict:
        assert isinstance(options_dict.get("RandomQuiz").get("value"), bool)
    if "QuizmoAlwaysAppears" in options_dict:
        assert isinstance(options_dict.get("QuizmoAlwaysAppears").get("value"), bool)
    if "ShuffleChapterDifficulty" in options_dict:
        assert isinstance(options_dict.get("ShuffleChapterDifficulty").get("value"), bool)
    if "RandomFormations" in options_dict:
        assert isinstance(options_dict.get("RandomFormations").get("value"), bool)
    if "ProgressiveScaling" in options_dict:
        assert isinstance(options_dict.get("ProgressiveScaling").get("value"), bool)
    if "ToyboxOpen" in options_dict:
        assert isinstance(options_dict.get("ToyboxOpen").get("value"), bool)
    if "WhaleOpen" in options_dict:
        assert isinstance(options_dict.get("WhaleOpen").get("value"), bool)
    if "AlwaysSpeedySpin" in options_dict:
        assert isinstance(options_dict.get("AlwaysSpeedySpin").get("value"), bool)
    if "AlwaysISpy" in options_dict:
        assert isinstance(options_dict.get("AlwaysISpy").get("value"), bool)
    if "AlwaysPeekaboo" in options_dict:
        assert isinstance(options_dict.get("AlwaysPeekaboo").get("value"), bool)
    if "HiddenBlockMode" in options_dict:
        assert (    isinstance(options_dict.get("HiddenBlockMode").get("value"), int)
                and 0 <= options_dict.get("HiddenBlockMode").get("value") <= 3)
    if "AllowPhysicsGlitches" in options_dict:
        assert isinstance(options_dict.get("AllowPhysicsGlitches").get("value"), bool)
    if "SkipEpilogue" in options_dict:
        assert isinstance(options_dict.get("SkipEpilogue").get("value"), bool)
    if "StarWaySpiritsNeeded" in options_dict:
        assert (    isinstance(options_dict.get("StarWaySpiritsNeeded").get("value"), int)
                and 0 <= options_dict.get("StarWaySpiritsNeeded").get("value") <= 7)
    if "PeachCastleReturnPipe" in options_dict:
        assert isinstance(options_dict.get("PeachCastleReturnPipe").get("value"), bool)
    if "FoliageItemHints" in options_dict:
        assert isinstance(options_dict.get("FoliageItemHints").get("value"), bool)
    if "HiddenPanelVisibility" in options_dict:
        assert isinstance(options_dict.get("HiddenPanelVisibility").get("value"), int)

    # Starting setup
    if "StartingMap" in options_dict:
        assert isinstance(options_dict.get("StartingMap").get("value"), int)
    if "StartingLevel" in options_dict:
        assert isinstance(options_dict.get("StartingLevel").get("value"), int)
    if "StartingMaxHP" in options_dict:
        assert isinstance(options_dict.get("StartingMaxHP").get("value"), int)
    if "StartingMaxFP" in options_dict:
        assert isinstance(options_dict.get("StartingMaxFP").get("value"), int)
    if "StartingMaxBP" in options_dict:
        assert isinstance(options_dict.get("StartingMaxBP").get("value"), int)
    if "StartingStarPower" in options_dict:
        assert (    isinstance(options_dict.get("StartingStarPower").get("value"), int)
                and 0 <= options_dict.get("StartingStarPower").get("value") <= 7)
    if "StartingBoots" in options_dict:
        try:
            assert (    isinstance(options_dict.get("StartingBoots").get("value"), int)
                    and 0 <= options_dict.get("StartingBoots").get("value") <= 2)
        except AssertionError:
            print("Preset Error: Jumpless start Not Yet Implemented in logic!")
            raise
    if "StartingHammer" in options_dict:
        assert (    isinstance(options_dict.get("StartingHammer").get("value"), int)
                and -1 <= options_dict.get("StartingHammer").get("value") <= 2)

    if "StartWithRandomItems" in options_dict:
        assert isinstance(options_dict.get("StartWithRandomItems").get("value"), bool)
    if "RandomItemsMin" in options_dict:
        assert (isinstance(options_dict.get("RandomItemsMin").get("value"), int)
            and 0 <= options_dict.get("RandomItemsMin").get("value") <= 16
            and ("RandomItemsMax" not in options_dict
              or options_dict.get("RandomItemsMin").get("value") <= 
                 options_dict.get("RandomItemsMax").get("value"))
        )
    if "RandomItemsMax" in options_dict:
        assert (isinstance(options_dict.get("RandomItemsMax").get("value"), int)
            and 0 <= options_dict.get("RandomItemsMax").get("value") <= 16
            and ("RandomItemsMin" not in options_dict
              or options_dict.get("RandomItemsMax").get("value") <= 
                 options_dict.get("RandomItemsMax").get("value"))
        )
    if "StartingItem0" in options_dict:
        assert isinstance(options_dict.get("StartingItem0").get("value"), int)
    if "StartingItem1" in options_dict:
        assert isinstance(options_dict.get("StartingItem1").get("value"), int)
    if "StartingItem2" in options_dict:
        assert isinstance(options_dict.get("StartingItem2").get("value"), int)
    if "StartingItem3" in options_dict:
        assert isinstance(options_dict.get("StartingItem3").get("value"), int)
    if "StartingItem4" in options_dict:
        assert isinstance(options_dict.get("StartingItem4").get("value"), int)
    if "StartingItem5" in options_dict:
        assert isinstance(options_dict.get("StartingItem5").get("value"), int)
    if "StartingItem6" in options_dict:
        assert isinstance(options_dict.get("StartingItem6").get("value"), int)
    if "StartingItem7" in options_dict:
        assert isinstance(options_dict.get("StartingItem7").get("value"), int)
    if "StartingItem8" in options_dict:
        assert isinstance(options_dict.get("StartingItem8").get("value"), int)
    if "StartingItem9" in options_dict:
        assert isinstance(options_dict.get("StartingItem9").get("value"), int)
    if "StartingItemA" in options_dict:
        assert isinstance(options_dict.get("StartingItemA").get("value"), int)
    if "StartingItemB" in options_dict:
        assert isinstance(options_dict.get("StartingItemB").get("value"), int)
    if "StartingItemC" in options_dict:
        assert isinstance(options_dict.get("StartingItemC").get("value"), int)
    if "StartingItemD" in options_dict:
        assert isinstance(options_dict.get("StartingItemD").get("value"), int)
    if "StartingItemE" in options_dict:
        assert isinstance(options_dict.get("StartingItemE").get("value"), int)
    if "StartingItemF" in options_dict:
        assert isinstance(options_dict.get("StartingItemF").get("value"), int)

    # Item related
    if "IncludeFavorsMode" in options_dict:
        assert isinstance(options_dict.get("IncludeFavorsMode").get("value"), int)
    if "IncludeLettersMode" in options_dict:
        assert isinstance(options_dict.get("IncludeLettersMode").get("value"), int)
    if "IncludeRadioTradeEvent" in options_dict:
        assert isinstance(options_dict.get("IncludeRadioTradeEvent").get("value"), bool)
    if "IncludeDojo" in options_dict:
        assert isinstance(options_dict.get("IncludeDojo").get("value"), bool)
    if "GearShuffleMode" in options_dict:
        assert isinstance(options_dict.get("GearShuffleMode").get("value"), int)
    if "ItemScarcity" in options_dict:
        assert (isinstance(options_dict.get("ItemScarcity").get("value"), int)
            and 0 <= options_dict.get("ItemScarcity").get("value") <= 5
        )
    if "AddItemPouches" in options_dict:
        assert isinstance(options_dict.get("AddItemPouches").get("value"), bool)
    if "PlacementAlgorithm" in options_dict:
        assert (isinstance(options_dict.get("PlacementAlgorithm").get("value"), str)
            and options_dict.get("PlacementAlgorithm").get("value") in [
                "ForwardFill",
                #"WeightedForwardFill", # NYI
                "AssumedFill",
                "CustomSeed"
            ]
        )
    if "PlacementLogic" in options_dict:
        assert (isinstance(options_dict.get("PlacementLogic").get("value"), str)
            and options_dict.get("PlacementLogic").get("value") in [
                "NoGlitches",
                #"Glitches", # NYI
                "NoLogic"
            ]
        )
    if "KeyitemsOutsideDungeon" in options_dict:
        assert isinstance(options_dict.get("KeyitemsOutsideDungeon").get("value"), bool)
    if "KeyitemsOutsideChapter" in options_dict:
        assert isinstance(options_dict.get("KeyitemsOutsideChapter").get("value"), bool)
    if "AllowItemHints" in options_dict:
        assert isinstance(options_dict.get("AllowItemHints").get("value"), bool)
    if "ItemTrapMode" in options_dict:
        assert isinstance(options_dict.get("ItemTrapMode").get("value"), int)
    # Mystery? item options
    if "RandomChoice" in options_dict:
        assert isinstance(options_dict.get("RandomChoice").get("value"), bool)
    if "MysteryRandomPick" in options_dict:
        assert isinstance(options_dict.get("MysteryRandomPick").get("value"), bool)
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

    # Blocks related
    if "ShuffleBlocks" in options_dict:
        assert isinstance(options_dict.get("ShuffleBlocks").get("value"), bool)

    # Moves and Badges
    if "RandomBadgesBP" in options_dict:
        assert isinstance(options_dict.get("RandomBadgesBP").get("value"), int)
    if "RandomBadgesFP" in options_dict:
        assert isinstance(options_dict.get("RandomBadgesFP").get("value"), int)
    if "RandomPartnerFP" in options_dict:
        assert isinstance(options_dict.get("RandomPartnerFP").get("value"), int)
    if "RandomStarpowerSP" in options_dict:
        assert isinstance(options_dict.get("RandomStarpowerSP").get("value"), int)

    # Entrance related
    if "BowsersCastleMode" in options_dict:
        assert isinstance(options_dict.get("BowsersCastleMode").get("value"), int)
    if "RandomizeOnewayEntrances" in options_dict:
        assert isinstance(options_dict.get("RandomizeOnewayEntrances").get("value"), bool)
    if "UnpairedEntrances" in options_dict:
        assert isinstance(options_dict.get("UnpairedEntrances").get("value"), bool)

    # Partner related
    if "PartnersInDefaultLocations" in options_dict:
        assert isinstance(options_dict.get("PartnersInDefaultLocations").get("value"), bool)
    if "PartnersAlwaysUsable" in options_dict:
        assert isinstance(options_dict.get("PartnersAlwaysUsable").get("value"), bool)
    if "StartWithRandomPartners" in options_dict:
        assert isinstance(options_dict.get("StartWithRandomPartners").get("value"), bool)
    if "RandomPartnersMin" in options_dict:
        assert (isinstance(options_dict.get("RandomPartnersMin").get("value"), int)
            and 1 <= options_dict.get("RandomPartnersMin").get("value") <= 8
            and ("RandomPartnersMax" not in options_dict
              or options_dict.get("RandomPartnersMin").get("value") <= 
                 options_dict.get("RandomPartnersMax").get("value"))
        )
    if "RandomPartnersMax" in options_dict:
        assert (isinstance(options_dict.get("RandomPartnersMax").get("value"), int)
            and 1 <= options_dict.get("RandomPartnersMax").get("value") <= 8
            and ("RandomPartnersMin" not in options_dict
              or options_dict.get("RandomPartnersMin").get("value") <= 
                 options_dict.get("RandomPartnersMax").get("value"))
        )
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
        assert (isinstance(options_dict.get("StartWithPartners").get("value"), dict)
            and all(key in permitted_values for key in options_dict.get("StartWithPartners").get("value"))
            and all(isinstance(value, bool) for value in options_dict.get("StartWithPartners").get("value").values())
            and any(value for value in options_dict.get("StartWithPartners").get("value").values()))

    # Spoilerlog
    if "WriteSpoilerLog" in options_dict:
        assert isinstance(options_dict.get("WriteSpoilerLog").get("value"), bool)
    if "PrettySpoilerlog" in options_dict:
        assert isinstance(options_dict.get("PrettySpoilerlog").get("value"), bool)

    # Cosmetics / Palettes
    if "RomanNumerals" in options_dict:
        assert isinstance(options_dict.get("RomanNumerals").get("value"), bool)
    if "RandomText" in options_dict:
        assert isinstance(options_dict.get("RandomText").get("value"), bool)
    if "CoinColor" in options_dict:
        assert (isinstance(options_dict.get("CoinColor").get("value"), int)
            and 0 <= options_dict.get("CoinColor").get("value") <= 4
        )
    if "RandomCoinColor" in options_dict:
        assert isinstance(options_dict.get("RandomCoinColor").get("value"), bool)
    if "Box5ColorA" in options_dict:
        assert (isinstance(options_dict.get("Box5ColorA").get("value"), int)
            and 0 <= options_dict.get("Box5ColorA").get("value") <= 0xFFFFFFFF
        )
    if "Box5ColorB" in options_dict:
        assert (isinstance(options_dict.get("Box5ColorB").get("value"), int)
            and 0 <= options_dict.get("Box5ColorB").get("value") <= 0xFFFFFFFF
        )

    if "MarioSetting" in options_dict:
        assert isinstance(options_dict.get("MarioSetting").get("value"), int)
    if "MarioSprite" in options_dict:
        assert isinstance(options_dict.get("MarioSprite").get("value"), int)
    if "GoombarioSetting" in options_dict:
        assert isinstance(options_dict.get("GoombarioSetting").get("value"), int)
    if "GoombarioSprite" in options_dict:
        assert isinstance(options_dict.get("GoombarioSprite").get("value"), int)
    if "KooperSetting" in options_dict:
        assert isinstance(options_dict.get("KooperSetting").get("value"), int)
    if "KooperSprite" in options_dict:
        assert isinstance(options_dict.get("KooperSprite").get("value"), int)
    if "BombetteSetting" in options_dict:
        assert isinstance(options_dict.get("BombetteSetting").get("value"), int)
    if "BombetteSprite" in options_dict:
        assert isinstance(options_dict.get("BombetteSprite").get("value"), int)
    #if "ParakarrySetting" in options_dict:
    #    assert isinstance(options_dict.get("ParakarrySetting").get("value"), int)
    #if "ParakarrySprite" in options_dict:
    #    assert isinstance(options_dict.get("ParakarrySprite").get("value"), int)
    if "BowSetting" in options_dict:
        assert isinstance(options_dict.get("BowSetting").get("value"), int)
    if "BowSprite" in options_dict:
        assert isinstance(options_dict.get("BowSprite").get("value"), int)
    #if "WattSetting" in options_dict:
    #    assert isinstance(options_dict.get("WattSetting").get("value"), int)
    #if "WattSprite" in options_dict:
    #    assert isinstance(options_dict.get("WattSprite").get("value"), int)
    #if "SushieSetting" in options_dict:
    #    assert isinstance(options_dict.get("SushieSetting").get("value"), int)
    #if "SushieSprite" in options_dict:
    #    assert isinstance(options_dict.get("SushieSprite").get("value"), int)
    #if "LakilesterSetting" in options_dict:
    #    assert isinstance(options_dict.get("LakilesterSetting").get("value"), int)
    #if "LakilesterSprite" in options_dict:
    #    assert isinstance(options_dict.get("LakilesterSprite").get("value"), int)
    if "BossesSetting" in options_dict:
        assert isinstance(options_dict.get("BossesSetting").get("value"), int)
    if "EnemiesSetting" in options_dict:
        assert isinstance(options_dict.get("EnemiesSetting").get("value"), int)
    if "NPCSetting" in options_dict:
        assert isinstance(options_dict.get("NPCSetting").get("value"), int)

    # Glitched Logic
    if "PrologueGelEarly" in options_dict:
        assert isinstance(options_dict.get("PrologueGelEarly").get("value"), bool)
    if "ReverseGoombaKingBridge" in options_dict:
        assert isinstance(options_dict.get("ReverseGoombaKingBridge").get("value"), bool)
    if "GoombaVillageEntryFenceClip" in options_dict:
        assert isinstance(options_dict.get("GoombaVillageEntryFenceClip").get("value"), bool)
    if "GoombaVillageSuperBootsExit" in options_dict:
        assert isinstance(options_dict.get("GoombaVillageSuperBootsExit").get("value"), bool)
    if "HammerlessJrPlaygroundLaki" in options_dict:
        assert isinstance(options_dict.get("HammerlessJrPlaygroundLaki").get("value"), bool)
    if "GoombaVillageLakiExit" in options_dict:
        assert isinstance(options_dict.get("GoombaVillageLakiExit").get("value"), bool)

    if "OddKeyEarly" in options_dict:
        assert isinstance(options_dict.get("OddKeyEarly").get("value"), bool)
    if "BlueHouseSkip" in options_dict:
        assert isinstance(options_dict.get("BlueHouseSkip").get("value"), bool)
    if "BlueHouseSkipLaki" in options_dict:
        assert isinstance(options_dict.get("BlueHouseSkipLaki").get("value"), bool)
    if "BlueHouseSkipToadLure" in options_dict:
        assert isinstance(options_dict.get("BlueHouseSkipToadLure").get("value"), bool)
    if "BowlessToyBoxHammer" in options_dict:
        assert isinstance(options_dict.get("BowlessToyBoxHammer").get("value"), bool)
    if "BowlessToyBoxParakarry" in options_dict:
        assert isinstance(options_dict.get("BowlessToyBoxParakarry").get("value"), bool)
    if "BowlessToyBoxUltraBoots" in options_dict:
        assert isinstance(options_dict.get("BowlessToyBoxUltraBoots").get("value"), bool)
    if "EarlyStoreroomParakarry" in options_dict:
        assert isinstance(options_dict.get("EarlyStoreroomParakarry").get("value"), bool)
    if "EarlyStoreroomHammer" in options_dict:
        assert isinstance(options_dict.get("EarlyStoreroomHammer").get("value"), bool)
    if "EarlyStoreroomUltraBoots" in options_dict:
        assert isinstance(options_dict.get("EarlyStoreroomUltraBoots").get("value"), bool)
    if "WhaleEarly" in options_dict:
        assert isinstance(options_dict.get("WhaleEarly").get("value"), bool)
    if "SushielessToadTownStarPiece" in options_dict:
        assert isinstance(options_dict.get("SushielessToadTownStarPiece").get("value"), bool)

    if "ClippyBootsStoneBlockSkip" in options_dict:
        assert isinstance(options_dict.get("ClippyBootsStoneBlockSkip").get("value"), bool)
    if "ClippyBootsMetalBlockSkip" in options_dict:
        assert isinstance(options_dict.get("ClippyBootsMetalBlockSkip").get("value"), bool)
    if "IslandPipeBlooperSkip" in options_dict:
        assert isinstance(options_dict.get("IslandPipeBlooperSkip").get("value"), bool)
    if "ParakarrylessSewerStarPiece" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSewerStarPiece").get("value"), bool)
    if "SewerBlocksWithoutUltraBoots" in options_dict:
        assert isinstance(options_dict.get("SewerBlocksWithoutUltraBoots").get("value"), bool)
    if "FirstBlockToShiverCityWithoutSuperBoots" in options_dict:
        assert isinstance(options_dict.get("FirstBlockToShiverCityWithoutSuperBoots").get("value"), bool)
    if "BlocksToShiverCityWithKooperShellItemThrow" in options_dict:
        assert isinstance(options_dict.get("BlocksToShiverCityWithKooperShellItemThrow").get("value"), bool)

    if "KooperlessPleasantPathStarPiece" in options_dict:
        assert isinstance(options_dict.get("KooperlessPleasantPathStarPiece").get("value"), bool)
    if "InvisibleBridgeClipLzs" in options_dict:
        assert isinstance(options_dict.get("InvisibleBridgeClipLzs").get("value"), bool)
    if "InvisibleBridgeClipLaki" in options_dict:
        assert isinstance(options_dict.get("InvisibleBridgeClipLaki").get("value"), bool)
    if "KooperlessPleasantPathThunderBolt" in options_dict:
        assert isinstance(options_dict.get("KooperlessPleasantPathThunderBolt").get("value"), bool)

    if "BombettelessKbfFpPlusLZS" in options_dict:
        assert isinstance(options_dict.get("BombettelessKbfFpPlusLZS").get("value"), bool)
    if "BombettelessKbfFpPlusLaki" in options_dict:
        assert isinstance(options_dict.get("BombettelessKbfFpPlusLaki").get("value"), bool)
    if "LakiJailbreak" in options_dict:
        assert isinstance(options_dict.get("LakiJailbreak").get("value"), bool)
    if "BombettelessRightFortressJailKey" in options_dict:
        assert isinstance(options_dict.get("BombettelessRightFortressJailKey").get("value"), bool)
    if "WaterStaircaseSkip" in options_dict:
        assert isinstance(options_dict.get("WaterStaircaseSkip").get("value"), bool)

    if "MtRuggedQuakeHammerAndLetterWithLaki" in options_dict:
        assert isinstance(options_dict.get("MtRuggedQuakeHammerAndLetterWithLaki").get("value"), bool)
    if "ParakarrylessMtRuggedSeed" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessMtRuggedSeed").get("value"), bool)
    if "BuzzarGapSkipClippy" in options_dict:
        assert isinstance(options_dict.get("BuzzarGapSkipClippy").get("value"), bool)
    if "ParakarrylessMtRuggedStarPiece" in options_dict:
       assert isinstance(options_dict.get("ParakarrylessMtRuggedStarPiece").get("value"), bool)
    if "MtRuggedCoinsWithKooper" in options_dict:
       assert isinstance(options_dict.get("MtRuggedCoinsWithKooper").get("value"), bool)

    if "DesertBrickBlockItemWithParakarry" in options_dict:
        assert isinstance(options_dict.get("DesertBrickBlockItemWithParakarry").get("value"), bool)
    if "EarlyRuinsLakiJump" in options_dict:
        assert isinstance(options_dict.get("EarlyRuinsLakiJump").get("value"), bool)
    if "EarlyRuinsUltraBoots" in options_dict:
        assert isinstance(options_dict.get("EarlyRuinsUltraBoots").get("value"), bool)

    if "ArtifactJump" in options_dict:
        assert isinstance(options_dict.get("ArtifactJump").get("value"), bool)
    if "RuinsKeyLakiJump" in options_dict:
        assert isinstance(options_dict.get("RuinsKeyLakiJump").get("value"), bool)
    if "ParakarrylessSecondSandRoomUltraBoots" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSecondSandRoomUltraBoots").get("value"), bool)
    if "ParakarrylessSecondSandRoomNormalBoots" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSecondSandRoomNormalBoots").get("value"), bool)
    if "ParakarrylessSuperHammerRoomUltraBoots" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSuperHammerRoomUltraBoots").get("value"), bool)
    if "ParakarrylessSuperHammerRoomNormalBoots" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSuperHammerRoomNormalBoots").get("value"), bool)
    if "RuinsLocksSkipClippy" in options_dict:
        assert isinstance(options_dict.get("RuinsLocksSkipClippy").get("value"), bool)

    if "RecordSkipNoBombettePush" in options_dict:
        assert isinstance(options_dict.get("RecordSkipNoBombettePush").get("value"), bool)
    if "RecordSkipBombettePush" in options_dict:
        assert isinstance(options_dict.get("RecordSkipBombettePush").get("value"), bool)
    if "BoosPortraitWithKooper" in options_dict:
        assert isinstance(options_dict.get("BoosPortraitWithKooper").get("value"), bool)
    if "BoosPortraitWithLaki" in options_dict:
        assert isinstance(options_dict.get("BoosPortraitWithLaki").get("value"), bool)
        
    if "GustyGulchGateSkipLZS" in options_dict:
        assert isinstance(options_dict.get("GustyGulchGateSkipLZS").get("value"), bool)
    if "GustyGulchGateSkipLaki" in options_dict:
        assert isinstance(options_dict.get("GustyGulchGateSkipLaki").get("value"), bool)
    if "KooperlessGustyGulchDizzyDialJump" in options_dict:
        assert isinstance(options_dict.get("KooperlessGustyGulchDizzyDialJump").get("value"), bool)
    if "KooperlessGustyGulchDizzyDialLaki" in options_dict:
        assert isinstance(options_dict.get("KooperlessGustyGulchDizzyDialLaki").get("value"), bool)
    if "KooperlessGustyGulchDizzyDialParakarry" in options_dict:
        assert isinstance(options_dict.get("KooperlessGustyGulchDizzyDialParakarry").get("value"), bool)
    if "GustyGulchGapSkip" in options_dict:
        assert isinstance(options_dict.get("GustyGulchGapSkip").get("value"), bool)

    if "BowlessTubbasCastle" in options_dict:
        assert isinstance(options_dict.get("BowlessTubbasCastle").get("value"), bool)
    if "TubbasTableLakiJump" in options_dict:
        assert isinstance(options_dict.get("TubbasTableLakiJump").get("value"), bool)
    if "TubbasCastleSuperBootsSkip" in options_dict:
        assert isinstance(options_dict.get("TubbasCastleSuperBootsSkip").get("value"), bool)
    if "ParakarrylessMegaRush" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessMegaRush").get("value"), bool)

    if "ParakarrylessBlueBuildingStarPiece" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessBlueBuildingStarPiece").get("value"), bool)
    if "GourmetGuySkipJump" in options_dict:
        assert isinstance(options_dict.get("GourmetGuySkipJump").get("value"), bool)
    if "GourmetGuySkipLaki" in options_dict:
        assert isinstance(options_dict.get("GourmetGuySkipLaki").get("value"), bool)
    if "GourmetGuySkipParakarry" in options_dict:
        assert isinstance(options_dict.get("GourmetGuySkipParakarry").get("value"), bool)
    if "BowlessGreenStation" in options_dict:
        assert isinstance(options_dict.get("BowlessGreenStation").get("value"), bool)
    if "KooperlessRedStationShootingStar" in options_dict:
        assert isinstance(options_dict.get("KooperlessRedStationShootingStar").get("value"), bool)
    if "ParakarrylessBlueBlockCityGap" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessBlueBlockCityGap").get("value"), bool)
    if "BlueSwitchSkip" in options_dict:
        assert isinstance(options_dict.get("BlueSwitchSkip").get("value"), bool)
    if "RedBarricadeSkip" in options_dict:
        assert isinstance(options_dict.get("RedBarricadeSkip").get("value"), bool)

    if "RaphSkipEnglish" in options_dict:
        assert isinstance(options_dict.get("RaphSkipEnglish").get("value"), bool)
    if "Ch5SushieGlitch" in options_dict:
        assert isinstance(options_dict.get("Ch5SushieGlitch").get("value"), bool)

    if "KooperlessLavalavaPowBlock" in options_dict:
        assert isinstance(options_dict.get("KooperlessLavalavaPowBlock").get("value"), bool)
    if "UltraHammerSkip" in options_dict:
        assert isinstance(options_dict.get("UltraHammerSkip").get("value"), bool)
    if "UltraHammerSkipLaki" in options_dict:
        assert isinstance(options_dict.get("UltraHammerSkip").get("value"), bool)
    if "Flarakarry" in options_dict:
        assert isinstance(options_dict.get("Flarakarry").get("value"), bool)
    if "ParakarrylessFlarakarryBombette" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessFlarakarryBombette").get("value"), bool)
    if "ParakarrylessFlarakarryLaki" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessFlarakarryLaki").get("value"), bool)

    if "EarlyLakiLZS" in options_dict:
        assert isinstance(options_dict.get("EarlyLakiLZS").get("value"), bool)
    if "EarlyLakiBombettePush" in options_dict:
        assert isinstance(options_dict.get("EarlyLakiBombettePush").get("value"), bool)
    if "BombettelessMegaSmash" in options_dict:
        assert isinstance(options_dict.get("BombettelessMegaSmash").get("value"), bool)
    if "SunTowerSkip" in options_dict:
        assert isinstance(options_dict.get("SunTowerSkip").get("value"), bool)
    if "YellowBerryGateSkipLZS" in options_dict:
        assert isinstance(options_dict.get("YellowBerryGateSkipLZS").get("value"), bool)
    if "YellowBerryGateSkipLaki" in options_dict:
        assert isinstance(options_dict.get("YellowBerryGateSkipLaki").get("value"), bool)
    if "YellowBerryGateSkipBombettePush" in options_dict:
        assert isinstance(options_dict.get("YellowBerryGateSkipBombettePush").get("value"), bool)
    if "RedBerryGateSkipBombettePush" in options_dict:
        assert isinstance(options_dict.get("RedBerryGateSkipBombettePush").get("value"), bool)
    if "RedBerryGateSkipLaki" in options_dict:
        assert isinstance(options_dict.get("RedBerryGateSkipLaki").get("value"), bool)
    if "BlueBerryGateSkipBombettePush" in options_dict:
        assert isinstance(options_dict.get("BlueBerryGateSkipBombettePush").get("value"), bool)
    if "BlueBerryGateSkipLaki" in options_dict:
        assert isinstance(options_dict.get("BlueBerryGateSkipLaki").get("value"), bool)
    if "BubbleBerryTreeLakiJump" in options_dict:
        assert isinstance(options_dict.get("BubbleBerryTreeLakiJump").get("value"), bool)

    if "MurderSolvedEarlyLaki" in options_dict:
        assert isinstance(options_dict.get("MurderSolvedEarlyLaki").get("value"), bool)
    if "MurderSolvedEarlyBombettePush" in options_dict:
        assert isinstance(options_dict.get("MurderSolvedEarlyBombettePush").get("value"), bool)
    if "Ch7SushieGlitch" in options_dict:
        assert isinstance(options_dict.get("Ch7SushieGlitch").get("value"), bool)
    if "StarStoneWithCh7SushieGlitch" in options_dict:
        assert isinstance(options_dict.get("StarStoneWithCh7SushieGlitch").get("value"), bool)
    if "ShiverMountainHiddenBlockWithoutUltraBootsLaki" in options_dict:
        assert isinstance(options_dict.get("ShiverMountainHiddenBlockWithoutUltraBootsLaki").get("value"), bool)
    if "ShiverMountainHiddenBlockWithoutUltraBootsNoLaki" in options_dict:
        assert isinstance(options_dict.get("ShiverMountainHiddenBlockWithoutUltraBootsNoLaki").get("value"), bool)

    if "MirrorClip" in options_dict:
        assert isinstance(options_dict.get("MirrorClip").get("value"), bool)

    if "BowlessBowsersCastleBasement" in options_dict:
        assert isinstance(options_dict.get("BowlessBowsersCastleBasement").get("value"), bool)
    if "FastFloodRoomKooper" in options_dict:
        assert isinstance(options_dict.get("FastFloodRoomKooper").get("value"), bool)
    if "FastFloodRoomBombetteUltraBoots" in options_dict:
        assert isinstance(options_dict.get("FastFloodRoomBombetteUltraBoots").get("value"), bool)

    if "BreakYellowBlocksWithSuperBoots" in options_dict:
        assert isinstance(options_dict.get("BreakYellowBlocksWithSuperBoots").get("value"), bool)
    if "BreakMetalBlocksWithUltraBoots" in options_dict:
        assert isinstance(options_dict.get("BreakMetalBlocksWithUltraBoots").get("value"), bool)
    if "KnowsHiddenBlocks" in options_dict:
        assert isinstance(options_dict.get("KnowsHiddenBlocks").get("value"), bool)
    if "KnowsPuzzleSolutions" in options_dict:
        assert isinstance(options_dict.get("KnowsPuzzleSolutions").get("value"), bool)
    if "ReachHighBlocksWithSuperBoots" in options_dict:
        assert isinstance(options_dict.get("ReachHighBlocksWithSuperBoots").get("value"), bool)

    # Audio
    if "RandomPitch" in options_dict:
        assert isinstance(options_dict.get("RandomPitch").get("value"), bool)


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
        #self.lakilester_setting = DEFAULT_PALETTE
        #self.lakilester_sprite = DEFAULT_PALETTE
        self.bosses_setting = DEFAULT_PALETTE
        self.enemies_setting = DEFAULT_PALETTE
        self.npc_setting = DEFAULT_PALETTE


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
            self.goomba_village_super_boots_exit = False
            self.hammerless_jr_playground_laki = False
            self.goomba_village_laki_exit = False

            self.odd_key_early = False
            self.blue_house_skip = False
            self.blue_house_skip_laki = False
            self.blue_house_skip_toad_lure = False
            self.bowless_toy_box_hammer = False
            self.bowless_toy_box_parakarry = False
            self.bowless_toy_box_ultra_boots = False
            self.early_storeroom_parakarry = False
            self.early_storeroom_hammer = False
            self.early_storeroom_ultra_boots = False
            self.whale_early = False
            self.sushiesless_toad_town_star_piece = False

            self.clippy_boots_stone_block_skip = False
            self.clippy_boots_metal_block_skip = False
            self.island_pipe_blooper_skip = False
            self.parakarryless_sewer_star_piece = False
            self.sewer_blocks_without_ultra_boots = False
            self.first_block_to_shiver_city_without_super_boots = False
            self.blocks_to_shiver_city_kooper_shell_item_throw = False

            self.kooperless_pleasant_path_star_piece = False
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
            self.parakarryless_mt_rugged_star_piece = False
            self.desert_brick_block_item_with_parakarry = False
            self.early_ruins_laki_jump = False
            self.early_ruins_ultra_boots = False

            self.artifact_jump = False
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
            
            self.gusty_gulch_gate_skip_lzs = False
            self.gusty_gulch_gate_skip_laki = False
            self.kooperless_gusty_gulch_dizzy_dial_jump = False
            self.kooperless_gusty_gulch_dizzy_dial_laki = False
            self.kooperless_gusty_gulch_dizzy_dial_parakarry = False
            self.gusty_gulch_gap_skip = False

            self.bowless_tubbas_castle = False
            self.tubbas_table_laki_jump = False
            self.tubbas_castle_super_boots_skip = False
            self.parakarryless_mega_rush = False

            self.parakarryless_blue_building_star_piece = False
            self.gourmet_guy_skip_jump = False
            self.gourmet_guy_skip_laki = False
            self.gourmet_guy_skip_parakarry = False
            self.bowless_green_station = False
            self.kooperless_red_station_shooting_star = False
            self.parakarryless_blue_block_city_gap = False
            self.blue_switch_skip = False
            self.red_barricade_skip = False

            self.raph_skip_english = False
            self.ch5_sushie_glitch = False
            self.kooperless_lavalava_pow_block = False
            self.ultra_hammer_skip = False
            self.ultra_hammer_skip_laki = False
            self.flarakarry = False
            self.parakarryless_flarakarry_bombette = False
            self.parakarryless_flarakarry_laki = False

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
            self.bubble_berry_tree_laki_jump = False

            self.murder_solved_early_laki = False
            self.murder_solved_early_bombette_push = False
            self.ch7_sushie_glitch = False
            self.star_stone_with_ch7_sushie_glitch = False
            self.shiver_mountain_hidden_block_without_ultra_boots_laki = False
            self.shiver_mountain_hidden_block_without_ultra_boots_no_laki = False

            self.mirror_clip = False

            self.bowless_bowsers_castle_basement = False
            self.fast_flood_room_kooper = False
            self.fast_flood_room_bombette_ultra_boots = False

            self.break_yellow_blocks_with_super_boots = False
            self.break_metal_blocks_with_ultra_boots = False
            self.knows_hidden_blocks = False
            self.knows_puzzle_solutions = False
            self.reach_high_blocks_with_super_boots = False
