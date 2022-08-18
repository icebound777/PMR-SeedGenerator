from db.item import Item
from db.option import Option

from models.KeyValuePair import KeyValuePair

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
                item_id = self_value.value
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
            self.shuffle_chapter_difficulty = options_dict.get("ShuffleChapterDifficulty").value
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
            if self.starting_boots.value == -1:
                self.starting_boots.value = 0xFF
        if "StartingHammer" in options_dict:
            self.starting_hammer = options_dict.get("StartingHammer")
            if self.starting_hammer.value == -1:
                self.starting_hammer.value = 0xFF

        if "StartWithRandomItems" in options_dict:
            self.random_starting_items = options_dict.get("StartWithRandomItems").value
        if "RandomItemsMin" in options_dict:
            self.random_starting_items_min = options_dict.get("RandomItemsMin").value
        if "RandomItemsMax" in options_dict:
            self.random_starting_items_max = options_dict.get("RandomItemsMax").value
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
            self.include_favors_mode = options_dict.get("IncludeFavorsMode").value
        if "IncludeLettersMode" in options_dict:
            self.include_letters_mode = options_dict.get("IncludeLettersMode").value
        if "IncludeRadioTradeEvent" in options_dict:
            self.include_radiotradeevent = options_dict.get("IncludeRadioTradeEvent").value
        if "IncludeDojo" in options_dict:
            self.include_dojo = options_dict.get("IncludeDojo").value
        if "GearShuffleMode" in options_dict:
            self.gear_shuffle_mode = options_dict.get("GearShuffleMode")
        if "ItemScarcity" in options_dict:
            self.item_scarcity = options_dict.get("ItemScarcity").value
        if "AddItemPouches" in options_dict:
            self.add_item_pouches = options_dict.get("AddItemPouches").value
        if "PlacementAlgorithm" in options_dict:
            self.placement_algorithm = options_dict.get("PlacementAlgorithm").value
        if "PlacementLogic" in options_dict:
            self.placement_logic = options_dict.get("PlacementLogic").value
        if "KeyitemsOutsideDungeon" in options_dict:
            self.keyitems_outside_dungeon = options_dict.get("KeyitemsOutsideDungeon").value
        if "KeyitemsOutsideChapter" in options_dict:
            self.keyitems_outside_chapter = options_dict.get("KeyitemsOutsideChapter").value
        if "AllowItemHints" in options_dict:
            self.allow_itemhints = options_dict.get("AllowItemHints").value
        if "ItemTrapMode" in options_dict:
            self.itemtrap_mode = options_dict.get("ItemTrapMode").value
        # Mystery? item options
        if "RandomChoice" in options_dict:
            self.mystery_settings.mystery_random_choice = options_dict.get("RandomChoice")
        if "MysteryRandomPick" in options_dict:
            self.mystery_settings.mystery_random_pick = options_dict.get("MysteryRandomPick").value
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
            self.shuffle_blocks = options_dict.get("ShuffleBlocks").value

        # Moves and Badges
        if "RandomBadgesBP" in options_dict:
            self.random_badges_bp = options_dict.get("RandomBadgesBP").value
        if "RandomBadgesFP" in options_dict:
            self.random_badges_fp = options_dict.get("RandomBadgesFP").value
        if "RandomPartnerFP" in options_dict:
            self.random_partner_fp = options_dict.get("RandomPartnerFP").value
        if "RandomStarpowerSP" in options_dict:
            self.random_starpower_sp = options_dict.get("RandomStarpowerSP").value

        # Entrance related
        if "BowsersCastleMode" in options_dict:
            self.bowsers_castle_mode = options_dict.get("BowsersCastleMode")
        if "RandomizeOnewayEntrances" in options_dict:
            self.random_oneway_entrances = options_dict.get("RandomizeOnewayEntrances").value
        if "UnpairedEntrances" in options_dict:
            self.unpaired_entrances = options_dict.get("UnpairedEntrances").value

        # Partner related
        if "PartnersInDefaultLocations" in options_dict:
            self.partners_in_default_locations = options_dict.get("PartnersInDefaultLocations").value
        if "PartnersAlwaysUsable" in options_dict:
            self.partners_always_usable = options_dict.get("PartnersAlwaysUsable")
        if "StartWithRandomPartners" in options_dict:
            self.random_partners = options_dict.get("StartWithRandomPartners").value
        if "RandomPartnersMin" in options_dict:
            self.random_partners_min = options_dict.get("RandomPartnersMin").value
        if "RandomPartnersMax" in options_dict:
            self.random_partners_max = options_dict.get("RandomPartnersMax").value
        if "StartWithPartners" in options_dict:
            self.starting_partners.clear()
            for partner, start_with_partner in options_dict.get("StartWithPartners").value.items():
                if start_with_partner:
                    self.starting_partners.append(partner)
                if partner == "Goombario":
                    self.start_with_goombario.value = start_with_partner
                elif partner == "Kooper":
                    self.start_with_kooper.value = start_with_partner
                elif partner == "Bombette":
                    self.start_with_bombette.value = start_with_partner
                elif partner == "Parakarry":
                    self.start_with_parakarry.value = start_with_partner
                elif partner == "Bow":
                    self.start_with_bow.value = start_with_partner
                elif partner == "Watt":
                    self.start_with_watt.value = start_with_partner
                elif partner == "Sushie":
                    self.start_with_sushie.value = start_with_partner
                elif partner == "Lakilester":
                    self.start_with_lakilester.value = start_with_partner

        # Spoilerlog
        if "WriteSpoilerLog" in options_dict:
            self.write_spoilerlog = options_dict.get("WriteSpoilerLog").value
        if "PrettySpoilerlog" in options_dict:
            self.pretty_spoilerlog = options_dict.get("PrettySpoilerlog").value

        # Cosmetics / Palettes
        if "RomanNumerals" in options_dict:
            self.roman_numerals = options_dict.get("RomanNumerals")
        if "RandomText" in options_dict:
            self.random_text = options_dict.get("RandomText")
        if "CoinColor" in options_dict:
            self.coin_color = options_dict.get("CoinColor")
        if "RandomCoinColor" in options_dict:
            self.random_coin_color = options_dict.get("RandomCoinColor").value
        if "Box5ColorA" in options_dict:
            self.color_a = options_dict.get("Box5ColorA")
        if "Box5ColorB" in options_dict:
            self.color_b = options_dict.get("Box5ColorB")

        if "MarioSetting" in options_dict:
            self.palette_settings.mario_setting = options_dict.get("MarioSetting").value
        if "MarioSprite" in options_dict:
            self.palette_settings.mario_sprite = options_dict.get("MarioSprite").value
        if "GoombarioSetting" in options_dict:
            self.palette_settings.goombario_setting = options_dict.get("GoombarioSetting").value
        if "GoombarioSprite" in options_dict:
            self.palette_settings.goombario_sprite = options_dict.get("GoombarioSprite").value
        if "KooperSetting" in options_dict:
            self.palette_settings.kooper_setting = options_dict.get("KooperSetting").value
        if "KooperSprite" in options_dict:
            self.palette_settings.kooper_sprite = options_dict.get("KooperSprite").value
        if "BombetteSetting" in options_dict:
            self.palette_settings.bombette_setting = options_dict.get("BombetteSetting").value
        if "BombetteSprite" in options_dict:
            self.palette_settings.bombette_sprite = options_dict.get("BombetteSprite").value
        if "ParakarrySetting" in options_dict:
            self.palette_settings.parakarry_setting = options_dict.get("ParakarrySetting").value
        if "ParakarrySprite" in options_dict:
            self.palette_settings.parakarry_sprite = options_dict.get("ParakarrySprite").value
        if "BowSetting" in options_dict:
            self.palette_settings.bow_setting = options_dict.get("BowSetting").value
        if "BowSprite" in options_dict:
            self.palette_settings.bow_sprite = options_dict.get("BowSprite").value
        if "WattSetting" in options_dict:
            self.palette_settings.watt_setting = options_dict.get("WattSetting").value
        if "WattSprite" in options_dict:
            self.palette_settings.watt_sprite = options_dict.get("WattSprite").value
        if "SushieSetting" in options_dict:
            self.palette_settings.sushie_setting = options_dict.get("SushieSetting").value
        if "SushieSprite" in options_dict:
            self.palette_settings.sushie_sprite = options_dict.get("SushieSprite").value
        #if "LakilesterSetting" in options_dict:
        #    self.palette_settings.lakilester_setting = options_dict.get("LakilesterSetting").value
        #if "LakilesterSprite" in options_dict:
        #    self.palette_settings.lakilester_sprite = options_dict.get("LakilesterSprite").value
        if "BossesSetting" in options_dict:
            self.palette_settings.bosses_setting = options_dict.get("BossesSetting").value
        if "EnemiesSetting" in options_dict:
            self.palette_settings.enemies_setting = options_dict.get("EnemiesSetting").value
        if "NPCSetting" in options_dict:
            self.palette_settings.npc_setting = options_dict.get("NPCSetting").value

        # Glitched Logic
        if "PrologueGelEarly" in options_dict:
            self.glitch_settings.prologue_gel_early = options_dict.get("PrologueGelEarly").value

        if "OddKeyEarly" in options_dict:
            self.glitch_settings.odd_key_early = options_dict.get("OddKeyEarly").value
        if "BlueHouseSkip" in options_dict:
            self.glitch_settings.blue_house_skip = options_dict.get("BlueHouseSkip").value
        if "BlueHouseSkipLaki" in options_dict:
            self.glitch_settings.blue_house_skip_laki = options_dict.get("BlueHouseSkipLaki").value
        if "BlueHouseSkipToadLure" in options_dict:
            self.glitch_settings.blue_house_skip_toad_lure = options_dict.get("BlueHouseSkipToadLure").value
        if "BowlessToyBox" in options_dict:
            self.glitch_settings.bowless_toy_box = options_dict.get("BowlessToyBox").value
        if "EarlyStoreroomParakarry" in options_dict:
            self.glitch_settings.early_storeroom_parakarry = options_dict.get("EarlyStoreroomParakarry").value
        if "EarlyStoreroomHammer" in options_dict:
            self.glitch_settings.early_storeroom_hammer = options_dict.get("EarlyStoreroomHammer").value
        if "WhaleEarly" in options_dict:
            self.glitch_settings.whale_early = options_dict.get("WhaleEarly").value
        if "SushielessToadTownStarPiece" in options_dict:
            self.glitch_settings.sushiesless_toad_town_star_piece = options_dict.get("SushielessToadTownStarPiece").value

        if "ClippyBootsStoneBlockSkip" in options_dict:
            self.glitch_settings.clippy_boots_stone_block_skip = options_dict.get("ClippyBootsStoneBlockSkip").value
        if "ClippyBootsMetalBlockSkip" in options_dict:
            self.glitch_settings.clippy_boots_metal_block_skip = options_dict.get("ClippyBootsMetalBlockSkip").value
        if "IslandPipeBlooperSkip" in options_dict:
            self.glitch_settings.island_pipe_blooper_skip = options_dict.get("IslandPipeBlooperSkip").value
        if "ParakarrylessSewerStarPiece" in options_dict:
            self.glitch_settings.parakarryless_sewer_star_piece = options_dict.get("ParakarrylessSewerStarPiece").value
        if "SewerBlocksWithoutUltraBoots" in options_dict:
            self.glitch_settings.sewer_blocks_without_ultra_boots = options_dict.get("SewerBlocksWithoutUltraBoots").value

        if "KooperlessPleasantPathStarPiece" in options_dict:
            self.glitch_settings.kooperless_pleasant_path_star_piece = options_dict.get("KooperlessPleasantPathStarPiece").value
        if "InvisibleBridgeClipLzs" in options_dict:
            self.glitch_settings.invisible_bridge_clip_lzs = options_dict.get("InvisibleBridgeClipLzs").value
        if "InvisibleBridgeClipLaki" in options_dict:
            self.glitch_settings.invisible_bridge_clip_laki = options_dict.get("InvisibleBridgeClipLaki").value
        if "KooperlessPleasantPathThunderBolt" in options_dict:
            self.glitch_settings.kooperless_pleasant_path_thunderbolt = options_dict.get("KooperlessPleasantPathThunderBolt").value

        if "BombettelessKbfFpPlusLZS" in options_dict:
            self.glitch_settings.bombetteless_kbf_fp_plus_lzs = options_dict.get("BombettelessKbfFpPlusLZS").value
        if "BombettelessKbfFpPlusLaki" in options_dict:
            self.glitch_settings.bombetteless_kbf_fp_plus_laki = options_dict.get("BombettelessKbfFpPlusLaki").value
        if "LakiJailbreak" in options_dict:
            self.glitch_settings.laki_jailbreak = options_dict.get("LakiJailbreak").value
        if "BombettelessRightFortressJailKey" in options_dict:
            self.glitch_settings.bombetteless_right_fortress_jail_key = options_dict.get("BombettelessRightFortressJailKey").value

        if "MtRuggedQuakeHammerAndLetterWithLaki" in options_dict:
            self.glitch_settings.mt_rugged_quake_hammer_and_letter_with_laki = options_dict.get("MtRuggedQuakeHammerAndLetterWithLaki").value
        if "ParakarrylessMtRuggedSeed" in options_dict:
            self.glitch_settings.parakarryless_mt_rugged_seed = options_dict.get("ParakarrylessMtRuggedSeed").value
        if "BuzzarGapSkipClippy" in options_dict:
            self.glitch_settings.buzzar_gap_skip_clippy = options_dict.get("BuzzarGapSkipClippy").value
        if "ParakarrylessMtRuggedStarPiece" in options_dict:
            self.glitch_settings.parakarryless_mt_rugged_star_piece = options_dict.get("ParakarrylessMtRuggedStarPiece").value

        if "DesertBrickBlockItemWithParakarry" in options_dict:
            self.glitch_settings.desert_brick_block_item_with_parakarry = options_dict.get("DesertBrickBlockItemWithParakarry").value
        if "EarlyRuinsLakiJump" in options_dict:
            self.glitch_settings.early_ruins_laki_jump = options_dict.get("EarlyRuinsLakiJump").value
        if "EarlyRuinsUltraBoots" in options_dict:
            self.glitch_settings.early_ruins_ultra_boots = options_dict.get("EarlyRuinsUltraBoots").value

        if "ArtifactJump" in options_dict:
            self.glitch_settings.artifact_jump = options_dict.get("ArtifactJump").value
        if "RuinsKeyLakiJump" in options_dict:
            self.glitch_settings.ruins_key_laki_jump = options_dict.get("RuinsKeyLakiJump").value
        if "ParakarrylessSecondSandRoomUltraBoots" in options_dict:
            self.glitch_settings.parakarryless_second_sand_room_ultra_boots = options_dict.get("ParakarrylessSecondSandRoomUltraBoots").value
        if "ParakarrylessSecondSandRoomNormalBoots" in options_dict:
            self.glitch_settings.parakarryless_second_sand_room_normal_boots = options_dict.get("ParakarrylessSecondSandRoomNormalBoots").value
        if "ParakarrylessSuperHammerRoomUltraBoots" in options_dict:
            self.glitch_settings.parakarryless_super_hammer_room_ultra_boots = options_dict.get("ParakarrylessSuperHammerRoomUltraBoots").value
        if "ParakarrylessSuperHammerRoomNormalBoots" in options_dict:
            self.glitch_settings.parakarryless_super_hammer_room_normal_boots = options_dict.get("ParakarrylessSuperHammerRoomNormalBoots").value
        if "RuinsLocksSkipClippy" in options_dict:
            self.glitch_settings.ruins_locks_skip_clippy = options_dict.get("RuinsLocksSkipClippy").value

        if "RecordSkipNoBombettePush" in options_dict:
            self.glitch_settings.record_skip_no_bombette_push = options_dict.get("RecordSkipNoBombettePush").value
        if "RecordSkipBombettePush" in options_dict:
            self.glitch_settings.record_skip_bombette_push = options_dict.get("RecordSkipBombettePush").value
        if "BoosPortraitWithKooper" in options_dict:
            self.glitch_settings.boos_portrait_with_kooper = options_dict.get("BoosPortraitWithKooper").value
        if "BoosPortraitWithLaki" in options_dict:
            self.glitch_settings.boos_portrait_with_laki = options_dict.get("BoosPortraitWithLaki").value
            
        if "GustyGulchGateSkipLZS" in options_dict:
            self.glitch_settings.gusty_gulch_gate_skip_lzs = options_dict.get("GustyGulchGateSkipLZS").value
        if "KooperlessGustyGulchDizzyDialJump" in options_dict:
            self.glitch_settings.kooperless_gusty_gulch_dizzy_dial_jump = options_dict.get("KooperlessGustyGulchDizzyDialJump").value
        if "KooperlessGustyGulchDizzyDialLaki" in options_dict:
            self.glitch_settings.kooperless_gusty_gulch_dizzy_dial_laki = options_dict.get("KooperlessGustyGulchDizzyDialLaki").value
        if "KooperlessGustyGulchDizzyDialParakarry" in options_dict:
            self.glitch_settings.kooperless_gusty_gulch_dizzy_dial_parakarry = options_dict.get("KooperlessGustyGulchDizzyDialParakarry").value
        if "GustyGulchGapSkip" in options_dict:
            self.glitch_settings.gusty_gulch_gap_skip = options_dict.get("GustyGulchGapSkip").value

        if "BowlessTubbasCastle" in options_dict:
            self.glitch_settings.bowless_tubbas_castle = options_dict.get("BowlessTubbasCastle").value
        if "TubbasTableLakiJump" in options_dict:
            self.glitch_settings.tubbas_table_laki_jump = options_dict.get("TubbasTableLakiJump").value
        if "TubbasCastleSuperBootsSkip" in options_dict:
            self.glitch_settings.tubbas_castle_super_boots_skip = options_dict.get("TubbasCastleSuperBootsSkip").value
        if "ParakarrylessMegaRush" in options_dict:
            self.glitch_settings.parakarryless_mega_rush = options_dict.get("ParakarrylessMegaRush").value

        if "ParakarrylessBlueBuildingStarPiece" in options_dict:
            self.glitch_settings.parakarryless_blue_building_star_piece = options_dict.get("ParakarrylessBlueBuildingStarPiece").value
        if "GourmetGuySkipJump" in options_dict:
            self.glitch_settings.gourmet_guy_skip_jump = options_dict.get("GourmetGuySkipJump").value
        if "GourmetGuySkipLaki" in options_dict:
            self.glitch_settings.gourmet_guy_skip_laki = options_dict.get("GourmetGuySkipLaki").value
        if "GourmetGuySkipParakarry" in options_dict:
            self.glitch_settings.gourmet_guy_skip_parakarry = options_dict.get("GourmetGuySkipParakarry").value
        if "BowlessGreenStation" in options_dict:
            self.glitch_settings.bowless_green_station = options_dict.get("BowlessGreenStation").value
        if "KooperlessRedStationShootingStar" in options_dict:
            self.glitch_settings.kooperless_red_station_shooting_star = options_dict.get("KooperlessRedStationShootingStar").value

        if "RaphSkipEnglish" in options_dict:
            self.glitch_settings.raph_skip_english = options_dict.get("RaphSkipEnglish").value
        if "Ch5SushieGlitch" in options_dict:
            self.glitch_settings.ch5_sushie_glitch = options_dict.get("Ch5SushieGlitch").value

        if "KooperlessLavalavaPowBlock" in options_dict:
            self.glitch_settings.kooperless_lavalava_pow_block = options_dict.get("KooperlessLavalavaPowBlock").value
        if "UltraHammerSkip" in options_dict:
            self.glitch_settings.ultra_hammer_skip = options_dict.get("UltraHammerSkip").value
        if "Flarakarry" in options_dict:
            self.glitch_settings.flarakarry = options_dict.get("Flarakarry").value
        if "ParakarrylessFlarakarryBombette" in options_dict:
            self.glitch_settings.parakarryless_flarakarry_bombette = options_dict.get("ParakarrylessFlarakarryBombette").value
        if "ParakarrylessFlarakarryLaki" in options_dict:
            self.glitch_settings.parakarryless_flarakarry_laki = options_dict.get("ParakarrylessFlarakarryLaki").value

        if "EarlyLakiLZS" in options_dict:
            self.glitch_settings.early_laki_lzs = options_dict.get("EarlyLakiLZS").value
        if "EarlyLakiBombettePush" in options_dict:
            self.glitch_settings.early_laki_bombette_push = options_dict.get("EarlyLakiBombettePush").value
        if "BombettelessMegaSmash" in options_dict:
            self.glitch_settings.bombetteless_mega_smash = options_dict.get("BombettelessMegaSmash").value
        if "SunTowerSkip" in options_dict:
            self.glitch_settings.sun_tower_skip = options_dict.get("SunTowerSkip").value
        if "YellowBerryGateSkipLZS" in options_dict:
            self.glitch_settings.yellow_berry_gate_skip_lzs = options_dict.get("YellowBerryGateSkipLZS").value
        if "YellowBerryGateSkipLaki" in options_dict:
            self.glitch_settings.yellow_berry_gate_skip_laki = options_dict.get("YellowBerryGateSkipLaki").value
        if "YellowBerryGateSkipBombettePush" in options_dict:
            self.glitch_settings.yellow_berry_gate_skip_bombette_push = options_dict.get("YellowBerryGateSkipBombettePush").value
        if "RedBerryGateSkipBombettePush" in options_dict:
            self.glitch_settings.red_berry_gate_skip_bombette_push = options_dict.get("RedBerryGateSkipBombettePush").value
        if "RedBerryGateSkipLaki" in options_dict:
            self.glitch_settings.red_berry_gate_skip_laki = options_dict.get("RedBerryGateSkipLaki").value
        if "BlueBerryGateSkipBombettePush" in options_dict:
            self.glitch_settings.blue_berry_gate_skip_bombette_push = options_dict.get("BlueBerryGateSkipBombettePush").value
        if "BlueBerryGateSkipLaki" in options_dict:
            self.glitch_settings.blue_berry_gate_skip_laki = options_dict.get("BlueBerryGateSkipLaki").value
        if "BubbleBerryTreeLakiJump" in options_dict:
            self.glitch_settings.bubble_berry_tree_laki_jump = options_dict.get("BubbleBerryTreeLakiJump").value

        if "MurderSolvedEarlyLaki" in options_dict:
            self.glitch_settings.murder_solved_early_laki = options_dict.get("MurderSolvedEarlyLaki").value
        if "MurderSolvedEarlyBombettePush" in options_dict:
            self.glitch_settings.murder_solved_early_bombette_push = options_dict.get("MurderSolvedEarlyBombettePush").value
        if "Ch7SushieGlitch" in options_dict:
            self.glitch_settings.ch7_sushie_glitch = options_dict.get("Ch7SushieGlitch").value
        if "ShiverMountainHiddenBlockWithoutUltraBootsLaki" in options_dict:
            self.glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_laki = options_dict.get("ShiverMountainHiddenBlockWithoutUltraBootsLaki").value
        if "ShiverMountainHiddenBlockWithoutUltraBootsNoLaki" in options_dict:
            self.glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_no_laki = options_dict.get("ShiverMountainHiddenBlockWithoutUltraBootsNoLaki").value

        if "MirrorClip" in options_dict:
            self.glitch_settings.mirror_clip = options_dict.get("MirrorClip").value

        if "BowlessBowsersCastleBasement" in options_dict:
            self.glitch_settings.bowless_bowsers_castle_basement = options_dict.get("BowlessBowsersCastleBasement").value
        if "FastFloodRoomKooper" in options_dict:
            self.glitch_settings.fast_flood_room_kooper = options_dict.get("FastFloodRoomKooper").value
        if "FastFloodRoomBombetteUltraBoots" in options_dict:
            self.glitch_settings.fast_flood_room_bombette_ultra_boots = options_dict.get("FastFloodRoomBombetteUltraBoots").value

        if "BreakYellowBlocksWithSuperBoots" in options_dict:
            self.glitch_settings.break_yellow_blocks_with_super_boots = options_dict.get("BreakYellowBlocksWithSuperBoots").value
        if "BreakMetalBlocksWithUltraBoots" in options_dict:
            self.glitch_settings.break_metal_blocks_with_ultra_boots = options_dict.get("BreakMetalBlocksWithUltraBoots").value
        if "KnowsHiddenBlocks" in options_dict:
            self.glitch_settings.knows_hidden_blocks = options_dict.get("KnowsHiddenBlocks").value
        if "KnowsPuzzleSolutions" in options_dict:
            self.glitch_settings.knows_puzzle_solutions = options_dict.get("KnowsPuzzleSolutions").value
              
        # Audio
        if "RandomPitch" in options_dict:
            self.random_pitch = options_dict.get("RandomPitch")


def validate_options(options_dict):
    if options_dict is None:
        raise ValueError

    # General
    if "StartingCoins" in options_dict:
        assert (isinstance(options_dict.get("StartingCoins").value, int)
            and 0 <= options_dict.get("StartingCoins").value <= 999
        )
    if "ShortenCutscenes" in options_dict:
        assert isinstance(options_dict.get("ShortenCutscenes").value, bool)
    if "MagicalSeedsRequired" in options_dict:
        assert isinstance(options_dict.get("MagicalSeedsRequired").value, int)
    if "BlueHouseOpen" in options_dict:
        assert isinstance(options_dict.get("BlueHouseOpen").value, bool)
    if "BlocksMatchContent" in options_dict:
        assert isinstance(options_dict.get("BlocksMatchContent").value, bool)
    if "SkipQuiz" in options_dict:
        assert isinstance(options_dict.get("SkipQuiz").value, bool)
    if "ChallengeMode" in options_dict:
        assert isinstance(options_dict.get("ChallengeMode").value, bool)
    if "CapEnemyXP" in options_dict:
        assert isinstance(options_dict.get("CapEnemyXP").value, bool)
    if "NoXP" in options_dict:
        assert isinstance(options_dict.get("NoXP").value, bool)
    if "DoubleDamage" in options_dict:
        assert isinstance(options_dict.get("DoubleDamage").value, bool)
    if "QuadrupleDamage" in options_dict:
        assert isinstance(options_dict.get("QuadrupleDamage").value, bool)
    if "OHKO" in options_dict:
        assert isinstance(options_dict.get("OHKO").value, bool)
    if "NoSaveBlocks" in options_dict:
        assert isinstance(options_dict.get("NoSaveBlocks").value, bool)
    if "NoHeartBlocks" in options_dict:
        assert isinstance(options_dict.get("NoHeartBlocks").value, bool)
    if "NoHealingItems" in options_dict:
        assert isinstance(options_dict.get("NoHealingItems").value, bool)

    # Item related
    if "ShuffleItems" in options_dict:
        assert isinstance(options_dict.get("ShuffleItems").value, bool)
    if "IncludeCoins" in options_dict:
        assert isinstance(options_dict.get("IncludeCoins").value, bool)
    if "IncludeShops" in options_dict:
        assert isinstance(options_dict.get("IncludeShops").value, bool)
    if "IncludePanels" in options_dict:
        assert isinstance(options_dict.get("IncludePanels").value, bool)

    # Entrance related
    if "ShuffleEntrances" in options_dict:
        assert isinstance(options_dict.get("ShuffleEntrances").value, bool)
    if "ShuffleEntrancesByArea" in options_dict:
        assert isinstance(options_dict.get("ShuffleEntrancesByArea").value, bool)
    if "ShuffleEntrancesByAll" in options_dict:
        assert isinstance(options_dict.get("ShuffleEntrancesByAll").value, bool)
    if "MatchEntranceTypes" in options_dict:
        assert isinstance(options_dict.get("MatchEntranceTypes").value, bool)

    # Settings unavailable in the GUI
    # General
    if "RandomQuiz" in options_dict:
        assert isinstance(options_dict.get("RandomQuiz").value, bool)
    if "QuizmoAlwaysAppears" in options_dict:
        assert isinstance(options_dict.get("QuizmoAlwaysAppears").value, bool)
    if "ShuffleChapterDifficulty" in options_dict:
        assert isinstance(options_dict.get("ShuffleChapterDifficulty").value, bool)
    if "RandomFormations" in options_dict:
        assert isinstance(options_dict.get("RandomFormations").value, bool)
    if "ProgressiveScaling" in options_dict:
        assert isinstance(options_dict.get("ProgressiveScaling").value, bool)
    if "ToyboxOpen" in options_dict:
        assert isinstance(options_dict.get("ToyboxOpen").value, bool)
    if "WhaleOpen" in options_dict:
        assert isinstance(options_dict.get("WhaleOpen").value, bool)
    if "AlwaysSpeedySpin" in options_dict:
        assert isinstance(options_dict.get("AlwaysSpeedySpin").value, bool)
    if "AlwaysISpy" in options_dict:
        assert isinstance(options_dict.get("AlwaysISpy").value, bool)
    if "AlwaysPeekaboo" in options_dict:
        assert isinstance(options_dict.get("AlwaysPeekaboo").value, bool)
    if "HiddenBlockMode" in options_dict:
        assert (    isinstance(options_dict.get("HiddenBlockMode").value, int)
                and 0 <= options_dict.get("HiddenBlockMode").value <= 3)
    if "AllowPhysicsGlitches" in options_dict:
        assert isinstance(options_dict.get("AllowPhysicsGlitches").value, bool)
    if "SkipEpilogue" in options_dict:
        assert isinstance(options_dict.get("SkipEpilogue").value, bool)
    if "StarWaySpiritsNeeded" in options_dict:
        assert (    isinstance(options_dict.get("StarWaySpiritsNeeded").value, int)
                and 0 <= options_dict.get("StarWaySpiritsNeeded").value <= 7)
    if "PeachCastleReturnPipe" in options_dict:
        assert isinstance(options_dict.get("PeachCastleReturnPipe").value, bool)
    if "FoliageItemHints" in options_dict:
        assert isinstance(options_dict.get("FoliageItemHints").value, bool)
    if "HiddenPanelVisibility" in options_dict:
        assert isinstance(options_dict.get("HiddenPanelVisibility").value, int)

    # Starting setup
    if "StartingMap" in options_dict:
        assert isinstance(options_dict.get("StartingMap").value, int)
    if "StartingLevel" in options_dict:
        assert isinstance(options_dict.get("StartingLevel").value, int)
    if "StartingMaxHP" in options_dict:
        assert isinstance(options_dict.get("StartingMaxHP").value, int)
    if "StartingMaxFP" in options_dict:
        assert isinstance(options_dict.get("StartingMaxFP").value, int)
    if "StartingMaxBP" in options_dict:
        assert isinstance(options_dict.get("StartingMaxBP").value, int)
    if "StartingStarPower" in options_dict:
        assert (    isinstance(options_dict.get("StartingStarPower").value, int)
                and 0 <= options_dict.get("StartingStarPower").value <= 7)
    if "StartingBoots" in options_dict:
        try:
            assert (    isinstance(options_dict.get("StartingBoots").value, int)
                    and 0 <= options_dict.get("StartingBoots").value <= 2)
        except AssertionError:
            print("Preset Error: Jumpless start Not Yet Implemented in logic!")
            raise
    if "StartingHammer" in options_dict:
        assert (    isinstance(options_dict.get("StartingHammer").value, int)
                and -1 <= options_dict.get("StartingHammer").value <= 2)

    if "StartWithRandomItems" in options_dict:
        assert isinstance(options_dict.get("StartWithRandomItems").value, bool)
    if "RandomItemsMin" in options_dict:
        assert (isinstance(options_dict.get("RandomItemsMin").value, int)
            and 0 <= options_dict.get("RandomItemsMin").value <= 16
            and ("RandomItemsMax" not in options_dict
              or options_dict.get("RandomItemsMin").value <= 
                 options_dict.get("RandomItemsMax").value)
        )
    if "RandomItemsMax" in options_dict:
        assert (isinstance(options_dict.get("RandomItemsMax").value, int)
            and 0 <= options_dict.get("RandomItemsMax").value <= 16
            and ("RandomItemsMin" not in options_dict
              or options_dict.get("RandomItemsMax").value <= 
                 options_dict.get("RandomItemsMax").value)
        )
    if "StartingItem0" in options_dict:
        assert isinstance(options_dict.get("StartingItem0").value, int)
    if "StartingItem1" in options_dict:
        assert isinstance(options_dict.get("StartingItem1").value, int)
    if "StartingItem2" in options_dict:
        assert isinstance(options_dict.get("StartingItem2").value, int)
    if "StartingItem3" in options_dict:
        assert isinstance(options_dict.get("StartingItem3").value, int)
    if "StartingItem4" in options_dict:
        assert isinstance(options_dict.get("StartingItem4").value, int)
    if "StartingItem5" in options_dict:
        assert isinstance(options_dict.get("StartingItem5").value, int)
    if "StartingItem6" in options_dict:
        assert isinstance(options_dict.get("StartingItem6").value, int)
    if "StartingItem7" in options_dict:
        assert isinstance(options_dict.get("StartingItem7").value, int)
    if "StartingItem8" in options_dict:
        assert isinstance(options_dict.get("StartingItem8").value, int)
    if "StartingItem9" in options_dict:
        assert isinstance(options_dict.get("StartingItem9").value, int)
    if "StartingItemA" in options_dict:
        assert isinstance(options_dict.get("StartingItemA").value, int)
    if "StartingItemB" in options_dict:
        assert isinstance(options_dict.get("StartingItemB").value, int)
    if "StartingItemC" in options_dict:
        assert isinstance(options_dict.get("StartingItemC").value, int)
    if "StartingItemD" in options_dict:
        assert isinstance(options_dict.get("StartingItemD").value, int)
    if "StartingItemE" in options_dict:
        assert isinstance(options_dict.get("StartingItemE").value, int)
    if "StartingItemF" in options_dict:
        assert isinstance(options_dict.get("StartingItemF").value, int)

    # Item related
    if "IncludeFavorsMode" in options_dict:
        assert isinstance(options_dict.get("IncludeFavorsMode").value, int)
    if "IncludeLettersMode" in options_dict:
        assert isinstance(options_dict.get("IncludeLettersMode").value, int)
    if "IncludeRadioTradeEvent" in options_dict:
        assert isinstance(options_dict.get("IncludeRadioTradeEvent").value, bool)
    if "IncludeDojo" in options_dict:
        assert isinstance(options_dict.get("IncludeDojo").value, bool)
    if "GearShuffleMode" in options_dict:
        assert isinstance(options_dict.get("GearShuffleMode").value, int)
    if "ItemScarcity" in options_dict:
        assert (isinstance(options_dict.get("ItemScarcity").value, int)
            and 0 <= options_dict.get("ItemScarcity").value <= 5
        )
    if "AddItemPouches" in options_dict:
        assert isinstance(options_dict.get("AddItemPouches").value, bool)
    if "PlacementAlgorithm" in options_dict:
        assert (isinstance(options_dict.get("PlacementAlgorithm").value, str)
            and options_dict.get("PlacementAlgorithm").value in [
                "ForwardFill",
                #"WeightedForwardFill", # NYI
                "AssumedFill",
                "CustomSeed"
            ]
        )
    if "PlacementLogic" in options_dict:
        assert (isinstance(options_dict.get("PlacementLogic").value, str)
            and options_dict.get("PlacementLogic").value in [
                "NoGlitches",
                #"Glitches", # NYI
                "NoLogic"
            ]
        )
    if "KeyitemsOutsideDungeon" in options_dict:
        assert isinstance(options_dict.get("KeyitemsOutsideDungeon").value, bool)
    if "KeyitemsOutsideChapter" in options_dict:
        assert isinstance(options_dict.get("KeyitemsOutsideChapter").value, bool)
    if "AllowItemHints" in options_dict:
        assert isinstance(options_dict.get("AllowItemHints").value, bool)
    if "ItemTrapMode" in options_dict:
        assert isinstance(options_dict.get("ItemTrapMode").value, int)
    # Mystery? item options
    if "RandomChoice" in options_dict:
        assert isinstance(options_dict.get("RandomChoice").value, bool)
    if "MysteryRandomPick" in options_dict:
        assert isinstance(options_dict.get("MysteryRandomPick").value, bool)
    if "ItemChoiceA" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceA").value, int)
            and 0x80 <= options_dict.get("ItemChoiceA").value <= 0xDA
        )
    if "ItemChoiceB" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceB").value, int)
            and 0x80 <= options_dict.get("ItemChoiceB").value <= 0xDA
        )
    if "ItemChoiceC" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceC").value, int)
            and 0x80 <= options_dict.get("ItemChoiceC").value <= 0xDA
        )
    if "ItemChoiceD" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceD").value, int)
            and 0x80 <= options_dict.get("ItemChoiceD").value <= 0xDA
        )
    if "ItemChoiceE" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceE").value, int)
            and 0x80 <= options_dict.get("ItemChoiceE").value <= 0xDA
        )
    if "ItemChoiceF" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceF").value, int)
            and 0x80 <= options_dict.get("ItemChoiceF").value <= 0xDA
        )
    if "ItemChoiceG" in options_dict:
        assert (isinstance(options_dict.get("ItemChoiceG").value, int)
            and 0x80 <= options_dict.get("ItemChoiceG").value <= 0xDA
        )

    # Blocks related
    if "ShuffleBlocks" in options_dict:
        assert isinstance(options_dict.get("ShuffleBlocks").value, bool)

    # Moves and Badges
    if "RandomBadgesBP" in options_dict:
        assert isinstance(options_dict.get("RandomBadgesBP").value, int)
    if "RandomBadgesFP" in options_dict:
        assert isinstance(options_dict.get("RandomBadgesFP").value, int)
    if "RandomPartnerFP" in options_dict:
        assert isinstance(options_dict.get("RandomPartnerFP").value, int)
    if "RandomStarpowerSP" in options_dict:
        assert isinstance(options_dict.get("RandomStarpowerSP").value, int)

    # Entrance related
    if "BowsersCastleMode" in options_dict:
        assert isinstance(options_dict.get("BowsersCastleMode").value, int)
    if "RandomizeOnewayEntrances" in options_dict:
        assert isinstance(options_dict.get("RandomizeOnewayEntrances").value, bool)
    if "UnpairedEntrances" in options_dict:
        assert isinstance(options_dict.get("UnpairedEntrances").value, bool)

    # Partner related
    if "PartnersInDefaultLocations" in options_dict:
        assert isinstance(options_dict.get("PartnersInDefaultLocations").value, bool)
    if "PartnersAlwaysUsable" in options_dict:
        assert isinstance(options_dict.get("PartnersAlwaysUsable").value, bool)
    if "StartWithRandomPartners" in options_dict:
        assert isinstance(options_dict.get("StartWithRandomPartners").value, bool)
    if "RandomPartnersMin" in options_dict:
        assert (isinstance(options_dict.get("RandomPartnersMin").value, int)
            and 1 <= options_dict.get("RandomPartnersMin").value <= 8
            and ("RandomPartnersMax" not in options_dict
              or options_dict.get("RandomPartnersMin").value <= 
                 options_dict.get("RandomPartnersMax").value)
        )
    if "RandomPartnersMax" in options_dict:
        assert (isinstance(options_dict.get("RandomPartnersMax").value, int)
            and 1 <= options_dict.get("RandomPartnersMax").value <= 8
            and ("RandomPartnersMin" not in options_dict
              or options_dict.get("RandomPartnersMin").value <= 
                 options_dict.get("RandomPartnersMax").value)
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
        assert (isinstance(options_dict.get("StartWithPartners").value, dict)
            and all(key in permitted_values for key in options_dict.get("StartWithPartners").value)
            and all(isinstance(value, bool) for value in options_dict.get("StartWithPartners").value.values())
            and any(value for value in options_dict.get("StartWithPartners").value.values()))

    # Spoilerlog
    if "WriteSpoilerLog" in options_dict:
        assert isinstance(options_dict.get("WriteSpoilerLog").value, bool)
    if "PrettySpoilerlog" in options_dict:
        assert isinstance(options_dict.get("PrettySpoilerlog").value, bool)

    # Cosmetics / Palettes
    if "RomanNumerals" in options_dict:
        assert isinstance(options_dict.get("RomanNumerals").value, bool)
    if "RandomText" in options_dict:
        assert isinstance(options_dict.get("RandomText").value, bool)
    if "CoinColor" in options_dict:
        assert (isinstance(options_dict.get("CoinColor").value, int)
            and 0 <= options_dict.get("CoinColor").value <= 4
        )
    if "RandomCoinColor" in options_dict:
        assert isinstance(options_dict.get("RandomCoinColor").value, bool)
    if "Box5ColorA" in options_dict:
        assert (isinstance(options_dict.get("Box5ColorA").value, int)
            and 0 <= options_dict.get("Box5ColorA").value <= 0xFFFFFFFF
        )
    if "Box5ColorB" in options_dict:
        assert (isinstance(options_dict.get("Box5ColorB").value, int)
            and 0 <= options_dict.get("Box5ColorB").value <= 0xFFFFFFFF
        )

    if "MarioSetting" in options_dict:
        assert isinstance(options_dict.get("MarioSetting").value, int)
    if "MarioSprite" in options_dict:
        assert isinstance(options_dict.get("MarioSprite").value, int)
    if "GoombarioSetting" in options_dict:
        assert isinstance(options_dict.get("GoombarioSetting").value, int)
    if "GoombarioSprite" in options_dict:
        assert isinstance(options_dict.get("GoombarioSprite").value, int)
    if "KooperSetting" in options_dict:
        assert isinstance(options_dict.get("KooperSetting").value, int)
    if "KooperSprite" in options_dict:
        assert isinstance(options_dict.get("KooperSprite").value, int)
    if "BombetteSetting" in options_dict:
        assert isinstance(options_dict.get("BombetteSetting").value, int)
    if "BombetteSprite" in options_dict:
        assert isinstance(options_dict.get("BombetteSprite").value, int)
    #if "ParakarrySetting" in options_dict:
    #    assert isinstance(options_dict.get("ParakarrySetting").value, int)
    #if "ParakarrySprite" in options_dict:
    #    assert isinstance(options_dict.get("ParakarrySprite").value, int)
    if "BowSetting" in options_dict:
        assert isinstance(options_dict.get("BowSetting").value, int)
    if "BowSprite" in options_dict:
        assert isinstance(options_dict.get("BowSprite").value, int)
    #if "WattSetting" in options_dict:
    #    assert isinstance(options_dict.get("WattSetting").value, int)
    #if "WattSprite" in options_dict:
    #    assert isinstance(options_dict.get("WattSprite").value, int)
    #if "SushieSetting" in options_dict:
    #    assert isinstance(options_dict.get("SushieSetting").value, int)
    #if "SushieSprite" in options_dict:
    #    assert isinstance(options_dict.get("SushieSprite").value, int)
    #if "LakilesterSetting" in options_dict:
    #    assert isinstance(options_dict.get("LakilesterSetting").value, int)
    #if "LakilesterSprite" in options_dict:
    #    assert isinstance(options_dict.get("LakilesterSprite").value, int)
    if "BossesSetting" in options_dict:
        assert isinstance(options_dict.get("BossesSetting").value, int)
    if "EnemiesSetting" in options_dict:
        assert isinstance(options_dict.get("EnemiesSetting").value, int)
    if "NPCSetting" in options_dict:
        assert isinstance(options_dict.get("NPCSetting").value, int)

    # Glitched Logic
    if "PrologueGelEarly" in options_dict:
        assert isinstance(options_dict.get("PrologueGelEarly").value, bool)

    if "OddKeyEarly" in options_dict:
        assert isinstance(options_dict.get("OddKeyEarly").value, bool)
    if "BlueHouseSkip" in options_dict:
        assert isinstance(options_dict.get("BlueHouseSkip").value, bool)
    if "BlueHouseSkipLaki" in options_dict:
        assert isinstance(options_dict.get("BlueHouseSkipLaki").value, bool)
    if "BlueHouseSkipToadLure" in options_dict:
        assert isinstance(options_dict.get("BlueHouseSkipToadLure").value, bool)
    if "BowlessToyBox" in options_dict:
        assert isinstance(options_dict.get("BowlessToyBox").value, bool)
    if "EarlyStoreroomParakarry" in options_dict:
        assert isinstance(options_dict.get("EarlyStoreroomParakarry").value, bool)
    if "EarlyStoreroomHammer" in options_dict:
        assert isinstance(options_dict.get("EarlyStoreroomHammer").value, bool)
    if "WhaleEarly" in options_dict:
        assert isinstance(options_dict.get("WhaleEarly").value, bool)
    if "SushielessToadTownStarPiece" in options_dict:
        assert isinstance(options_dict.get("SushielessToadTownStarPiece").value, bool)

    if "ClippyBootsStoneBlockSkip" in options_dict:
        assert isinstance(options_dict.get("ClippyBootsStoneBlockSkip").value, bool)
    if "ClippyBootsMetalBlockSkip" in options_dict:
        assert isinstance(options_dict.get("ClippyBootsMetalBlockSkip").value, bool)
    if "IslandPipeBlooperSkip" in options_dict:
        assert isinstance(options_dict.get("IslandPipeBlooperSkip").value, bool)
    if "ParakarrylessSewerStarPiece" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSewerStarPiece").value, bool)
    if "SewerBlocksWithoutUltraBoots" in options_dict:
        assert isinstance(options_dict.get("SewerBlocksWithoutUltraBoots").value, bool)

    if "KooperlessPleasantPathStarPiece" in options_dict:
        assert isinstance(options_dict.get("KooperlessPleasantPathStarPiece").value, bool)
    if "InvisibleBridgeClipLzs" in options_dict:
        assert isinstance(options_dict.get("InvisibleBridgeClipLzs").value, bool)
    if "InvisibleBridgeClipLaki" in options_dict:
        assert isinstance(options_dict.get("InvisibleBridgeClipLaki").value, bool)
    if "KooperlessPleasantPathThunderBolt" in options_dict:
        assert isinstance(options_dict.get("KooperlessPleasantPathThunderBolt").value, bool)

    if "BombettelessKbfFpPlusLZS" in options_dict:
        assert isinstance(options_dict.get("BombettelessKbfFpPlusLZS").value, bool)
    if "BombettelessKbfFpPlusLaki" in options_dict:
        assert isinstance(options_dict.get("BombettelessKbfFpPlusLaki").value, bool)
    if "LakiJailbreak" in options_dict:
        assert isinstance(options_dict.get("LakiJailbreak").value, bool)
    if "BombettelessRightFortressJailKey" in options_dict:
        assert isinstance(options_dict.get("BombettelessRightFortressJailKey").value, bool)

    if "MtRuggedQuakeHammerAndLetterWithLaki" in options_dict:
        assert isinstance(options_dict.get("MtRuggedQuakeHammerAndLetterWithLaki").value, bool)
    if "ParakarrylessMtRuggedSeed" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessMtRuggedSeed").value, bool)
    if "BuzzarGapSkipClippy" in options_dict:
        assert isinstance(options_dict.get("BuzzarGapSkipClippy").value, bool)
    if "ParakarrylessMtRuggedStarPiece" in options_dict:
       assert isinstance(options_dict.get("ParakarrylessMtRuggedStarPiece").value, bool)

    if "DesertBrickBlockItemWithParakarry" in options_dict:
        assert isinstance(options_dict.get("DesertBrickBlockItemWithParakarry").value, bool)
    if "EarlyRuinsLakiJump" in options_dict:
        assert isinstance(options_dict.get("EarlyRuinsLakiJump").value, bool)
    if "EarlyRuinsUltraBoots" in options_dict:
        assert isinstance(options_dict.get("EarlyRuinsUltraBoots").value, bool)

    if "ArtifactJump" in options_dict:
        assert isinstance(options_dict.get("ArtifactJump").value, bool)
    if "RuinsKeyLakiJump" in options_dict:
        assert isinstance(options_dict.get("RuinsKeyLakiJump").value, bool)
    if "ParakarrylessSecondSandRoomUltraBoots" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSecondSandRoomUltraBoots").value, bool)
    if "ParakarrylessSecondSandRoomNormalBoots" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSecondSandRoomNormalBoots").value, bool)
    if "ParakarrylessSuperHammerRoomUltraBoots" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSuperHammerRoomUltraBoots").value, bool)
    if "ParakarrylessSuperHammerRoomNormalBoots" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessSuperHammerRoomNormalBoots").value, bool)
    if "RuinsLocksSkipClippy" in options_dict:
        assert isinstance(options_dict.get("RuinsLocksSkipClippy").value, bool)

    if "RecordSkipNoBombettePush" in options_dict:
        assert isinstance(options_dict.get("RecordSkipNoBombettePush").value, bool)
    if "RecordSkipBombettePush" in options_dict:
        assert isinstance(options_dict.get("RecordSkipBombettePush").value, bool)
    if "BoosPortraitWithKooper" in options_dict:
        assert isinstance(options_dict.get("BoosPortraitWithKooper").value, bool)
    if "BoosPortraitWithLaki" in options_dict:
        assert isinstance(options_dict.get("BoosPortraitWithLaki").value, bool)
        
    if "GustyGulchGateSkipLZS" in options_dict:
        assert isinstance(options_dict.get("GustyGulchGateSkipLZS").value, bool)
    if "KooperlessGustyGulchDizzyDialJump" in options_dict:
        assert isinstance(options_dict.get("KooperlessGustyGulchDizzyDialJump").value, bool)
    if "KooperlessGustyGulchDizzyDialLaki" in options_dict:
        assert isinstance(options_dict.get("KooperlessGustyGulchDizzyDialLaki").value, bool)
    if "KooperlessGustyGulchDizzyDialParakarry" in options_dict:
        assert isinstance(options_dict.get("KooperlessGustyGulchDizzyDialParakarry").value, bool)
    if "GustyGulchGapSkip" in options_dict:
        assert isinstance(options_dict.get("GustyGulchGapSkip").value, bool)

    if "BowlessTubbasCastle" in options_dict:
        assert isinstance(options_dict.get("BowlessTubbasCastle").value, bool)
    if "TubbasTableLakiJump" in options_dict:
        assert isinstance(options_dict.get("TubbasTableLakiJump").value, bool)
    if "TubbasCastleSuperBootsSkip" in options_dict:
        assert isinstance(options_dict.get("TubbasCastleSuperBootsSkip").value, bool)
    if "ParakarrylessMegaRush" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessMegaRush").value, bool)

    if "ParakarrylessBlueBuildingStarPiece" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessBlueBuildingStarPiece").value, bool)
    if "GourmetGuySkipJump" in options_dict:
        assert isinstance(options_dict.get("GourmetGuySkipJump").value, bool)
    if "GourmetGuySkipLaki" in options_dict:
        assert isinstance(options_dict.get("GourmetGuySkipLaki").value, bool)
    if "GourmetGuySkipParakarry" in options_dict:
        assert isinstance(options_dict.get("GourmetGuySkipParakarry").value, bool)
    if "BowlessGreenStation" in options_dict:
        assert isinstance(options_dict.get("BowlessGreenStation").value, bool)
    if "KooperlessRedStationShootingStar" in options_dict:
        assert isinstance(options_dict.get("KooperlessRedStationShootingStar").value, bool)

    if "RaphSkipEnglish" in options_dict:
        assert isinstance(options_dict.get("RaphSkipEnglish").value, bool)
    if "Ch5SushieGlitch" in options_dict:
        assert isinstance(options_dict.get("Ch5SushieGlitch").value, bool)

    if "KooperlessLavalavaPowBlock" in options_dict:
        assert isinstance(options_dict.get("KooperlessLavalavaPowBlock").value, bool)
    if "UltraHammerSkip" in options_dict:
        assert isinstance(options_dict.get("UltraHammerSkip").value, bool)
    if "Flarakarry" in options_dict:
        assert isinstance(options_dict.get("Flarakarry").value, bool)
    if "ParakarrylessFlarakarryBombette" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessFlarakarryBombette").value, bool)
    if "ParakarrylessFlarakarryLaki" in options_dict:
        assert isinstance(options_dict.get("ParakarrylessFlarakarryLaki").value, bool)

    if "EarlyLakiLZS" in options_dict:
        assert isinstance(options_dict.get("EarlyLakiLZS").value, bool)
    if "EarlyLakiBombettePush" in options_dict:
        assert isinstance(options_dict.get("EarlyLakiBombettePush").value, bool)
    if "BombettelessMegaSmash" in options_dict:
        assert isinstance(options_dict.get("BombettelessMegaSmash").value, bool)
    if "SunTowerSkip" in options_dict:
        assert isinstance(options_dict.get("SunTowerSkip").value, bool)
    if "YellowBerryGateSkipLZS" in options_dict:
        assert isinstance(options_dict.get("YellowBerryGateSkipLZS").value, bool)
    if "YellowBerryGateSkipLaki" in options_dict:
        assert isinstance(options_dict.get("YellowBerryGateSkipLaki").value, bool)
    if "YellowBerryGateSkipBombettePush" in options_dict:
        assert isinstance(options_dict.get("YellowBerryGateSkipBombettePush").value, bool)
    if "RedBerryGateSkipBombettePush" in options_dict:
        assert isinstance(options_dict.get("RedBerryGateSkipBombettePush").value, bool)
    if "RedBerryGateSkipLaki" in options_dict:
        assert isinstance(options_dict.get("RedBerryGateSkipLaki").value, bool)
    if "BlueBerryGateSkipBombettePush" in options_dict:
        assert isinstance(options_dict.get("BlueBerryGateSkipBombettePush").value, bool)
    if "BlueBerryGateSkipLaki" in options_dict:
        assert isinstance(options_dict.get("BlueBerryGateSkipLaki").value, bool)
    if "BubbleBerryTreeLakiJump" in options_dict:
        assert isinstance(options_dict.get("BubbleBerryTreeLakiJump").value, bool)

    if "MurderSolvedEarlyLaki" in options_dict:
        assert isinstance(options_dict.get("MurderSolvedEarlyLaki").value, bool)
    if "MurderSolvedEarlyBombettePush" in options_dict:
        assert isinstance(options_dict.get("MurderSolvedEarlyBombettePush").value, bool)
    if "Ch7SushieGlitch" in options_dict:
        assert isinstance(options_dict.get("Ch7SushieGlitch").value, bool)
    if "ShiverMountainHiddenBlockWithoutUltraBootsLaki" in options_dict:
        assert isinstance(options_dict.get("ShiverMountainHiddenBlockWithoutUltraBootsLaki").value, bool)
    if "ShiverMountainHiddenBlockWithoutUltraBootsNoLaki" in options_dict:
        assert isinstance(options_dict.get("ShiverMountainHiddenBlockWithoutUltraBootsNoLaki").value, bool)

    if "MirrorClip" in options_dict:
        assert isinstance(options_dict.get("MirrorClip").value, bool)

    if "BowlessBowsersCastleBasement" in options_dict:
        assert isinstance(options_dict.get("BowlessBowsersCastleBasement").value, bool)
    if "FastFloodRoomKooper" in options_dict:
        assert isinstance(options_dict.get("FastFloodRoomKooper").value, bool)
    if "FastFloodRoomBombetteUltraBoots" in options_dict:
        assert isinstance(options_dict.get("FastFloodRoomBombetteUltraBoots").value, bool)

    if "BreakYellowBlocksWithSuperBoots" in options_dict:
        assert isinstance(options_dict.get("BreakYellowBlocksWithSuperBoots").value, bool)
    if "BreakMetalBlocksWithUltraBoots" in options_dict:
        assert isinstance(options_dict.get("BreakMetalBlocksWithUltraBoots").value, bool)
    if "KnowsHiddenBlocks" in options_dict:
        assert isinstance(options_dict.get("KnowsHiddenBlocks").value, bool)
    if "KnowsPuzzleSolutions" in options_dict:
        assert isinstance(options_dict.get("KnowsPuzzleSolutions").value, bool)

    # Audio
    if "RandomPitch" in options_dict:
        assert isinstance(options_dict.get("RandomPitch").value, bool)


def get_option_keyvalue_dict(option_str):
    key = Option.get(Option.name == option_str).get_key()
    value = Option.get(Option.name == option_str).value

    return KeyValuePair(key, value)


def populate_keys(data:dict):

    for option_str in data.copy():
        if Option.get_or_none(Option.name == option_str) is not None:
            data[option_str] = KeyValuePair(
                Option.get(Option.name == option_str).get_key(),
                data[option_str]
            )
        else:
            data[option_str] = KeyValuePair(None, data[option_str])

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
            self.odd_key_early = False
            self.blue_house_skip = False
            self.blue_house_skip_laki = False
            self.blue_house_skip_toad_lure = False
            self.bowless_toy_box = False
            self.early_storeroom_parakarry = False
            self.early_storeroom_hammer = False
            self.whale_early = False
            self.sushiesless_toad_town_star_piece = False

            self.clippy_boots_stone_block_skip = False
            self.clippy_boots_metal_block_skip = False
            self.island_pipe_blooper_skip = False
            self.parakarryless_sewer_star_piece = False
            self.sewer_blocks_without_ultra_boots = False

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

            self.raph_skip_english = False
            self.ch5_sushie_glitch = False
            self.kooperless_lavalava_pow_block = False
            self.ultra_hammer_skip = False
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
