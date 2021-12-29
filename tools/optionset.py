from db.option import Option

class OptionSet:
    def __init__(self):
        """ Load Defaults from DB """
        # General
        self.starting_coins = get_option_keyvalue_dict("StartingCoins")
        self.replace_duplicate_keys = get_option_keyvalue_dict("ReplaceDuplicateKeys")
        self.duplicate_key_replacement = get_option_keyvalue_dict("DuplicateKeyReplacement")
        self.shorten_cutscenes = get_option_keyvalue_dict("ShortenCutscenes")
        self.flowergate_open = get_option_keyvalue_dict("FlowerGateOpen")
        self.bluehouse_open = get_option_keyvalue_dict("BlueHouseOpen")
        self.blocks_match_content = get_option_keyvalue_dict("BlocksMatchContent")
        self.skip_quiz = get_option_keyvalue_dict("SkipQuiz")
        self.cap_enemy_xp = get_option_keyvalue_dict("CapEnemyXP")
        self.damage_x2 = get_option_keyvalue_dict("2xDamage")
        self.damage_x4 = get_option_keyvalue_dict("4xDamage")
        self.ohko = get_option_keyvalue_dict("OHKO")

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
        self.shuffle_chapter_difficulty = False
        self.random_formations = get_option_keyvalue_dict("RandomFormations")

        # Starting setup
        self.starting_map = get_option_keyvalue_dict("StartingMap") # mac_00 Entry 4
        self.starting_level = get_option_keyvalue_dict("StartingLevel")
        self.starting_maxhp = get_option_keyvalue_dict("StartingMaxHP")
        self.starting_maxfp = get_option_keyvalue_dict("StartingMaxFP")
        self.starting_maxbp = get_option_keyvalue_dict("StartingMaxBP")

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
        self.include_favors = False
        self.include_letterchain = False
        self.placement_algorithm = "ForwardFill"
        self.placement_logic = "NoGlitches"
        self.keyitems_outside_area = True # False -> NYI
        self.keyitems_outside_chapter = True # "Keysanity" # false -> NYI

        # Moves and Badges
        self.shuffle_badges_bp = False
        self.shuffle_badges_fp = False
        self.shuffle_partner_fp = False
        self.shuffle_starpower_sp = False

        # Entrance related
        self.random_oneway_entrances = False # NYI
        self.unpaired_entrances = False # NYI

        # Partner related
        self.random_partners = False
        self.random_partners_min = 1
        self.random_partners_max = 1
        self.starting_partners = ["PARTNER_Goombario"]
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
        self.color_a = 0xEBE677FF # Box5ColorA
        self.color_b = 0x8E5A25FF # Box5ColorB
        self.random_coin_palette = False

        # Audio
        self.turn_off_music = False


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
        if "ReplaceDuplicateKeys" in options_dict:
            self.replace_duplicate_keys = options_dict.get("ReplaceDuplicateKeys")
        if "DuplicateKeyReplacement" in options_dict:
            self.duplicate_key_replacement = options_dict.get("DuplicateKeyReplacement")
        if "ShortenCutscenes" in options_dict:
            self.shorten_cutscenes = options_dict.get("ShortenCutscenes")
        if "FlowerGateOpen" in options_dict:
            self.flowergate_open = options_dict.get("FlowerGateOpen")
        if "BlueHouseOpen" in options_dict:
            self.bluehouse_open = options_dict.get("BlueHouseOpen")
        if "BlocksMatchContent" in options_dict:
            self.blocks_match_content = options_dict.get("BlocksMatchContent")
        if "SkipQuiz" in options_dict:
            self.skip_quiz = options_dict.get("SkipQuiz")
        if "CapEnemyXP" in options_dict:
            self.cap_enemy_xp = options_dict.get("CapEnemyXP")
        if "2xDamage" in options_dict:
            self.damage_x2 = options_dict.get("2xDamage")
        if "4xDamage" in options_dict:
            self.damage_x4 = options_dict.get("4xDamage")
        if "OHKO" in options_dict:
            self.ohko = options_dict.get("OHKO")

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
        if "ShuffleChapterDifficulty" in options_dict:
            self.shuffle_chapter_difficulty = options_dict.get("ShuffleChapterDifficulty").get("value")
        if "RandomFormations" in options_dict:
            self.random_formations = options_dict.get("RandomFormations")

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
        if "IncludeFavors" in options_dict:
            self.include_favors = options_dict.get("IncludeFavors").get("value")
        if "IncludeLetterChain" in options_dict:
            self.include_letterchain = options_dict.get("IncludeLetterChain").get("value")
        if "PlacementAlgorithm" in options_dict:
            self.placement_algorithm = options_dict.get("PlacementAlgorithm").get("value")
        if "PlacementLogic" in options_dict:
            self.placement_logic = options_dict.get("PlacementLogic").get("value")
        if "KeyitemsOutsideArea" in options_dict:
            self.keyitems_outside_area = options_dict.get("KeyitemsOutsideArea").get("value")
        if "KeyitemsOutsideChapter" in options_dict:
            self.keyitems_outside_chapter = options_dict.get("KeyitemsOutsideChapter").get("value")

        # Moves and Badges
        if "ShuffleBadgesBP" in options_dict:
            self.shuffle_badges_bp = options_dict.get("ShuffleBadgesBP").get("value")
        if "ShuffleBadgesFP" in options_dict:
            self.shuffle_badges_fp = options_dict.get("ShuffleBadgesFP").get("value")
        if "ShufflePartnerFP" in options_dict:
            self.shuffle_partner_fp = options_dict.get("ShufflePartnerFP").get("value")
        if "ShuffleStarpowerSP" in options_dict:
            self.shuffle_starpower_sp = options_dict.get("ShuffleStarpowerSP").get("value")

        # Entrance related
        if "RandomizeOnewayEntrances" in options_dict:
            self.random_oneway_entrances = options_dict.get("RandomizeOnewayEntrances").get("value")
        if "UnpairedEntrances" in options_dict:
            self.unpaired_entrances = options_dict.get("UnpairedEntrances").get("value")

        # Partner related
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
                    self.starting_partners.append(f"PARTNER_{partner}")
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
        if "RandomCoinPalette" in options_dict:
            self.random_coin_palette = options_dict.get("RandomCoinPalette").get("value")

        # Audio
        if "TurnOffMusic" in options_dict:
            self.turn_off_music = options_dict.get("TurnOffMusic").get("value")


def validate_options(options_dict):
    if options_dict is None:
        raise ValueError

    # General
    if "StartingCoins" in options_dict:
        assert (isinstance(options_dict.get("StartingCoins").get("value"), int)
            and 0 <= options_dict.get("StartingCoins").get("value") <= 999
        )
    if "ReplaceDuplicateKeys" in options_dict:
        assert isinstance(options_dict.get("ReplaceDuplicateKeys").get("value"), bool)
    if "DuplicateKeyReplacement" in options_dict:
        assert isinstance(options_dict.get("DuplicateKeyReplacement").get("value"), int)
    if "ShortenCutscenes" in options_dict:
        assert isinstance(options_dict.get("ShortenCutscenes").get("value"), bool)
    if "FlowerGateOpen" in options_dict:
        assert isinstance(options_dict.get("FlowerGateOpen").get("value"), bool)
    if "BlueHouseOpen" in options_dict:
        assert isinstance(options_dict.get("BlueHouseOpen").get("value"), bool)
    if "BlocksMatchContent" in options_dict:
        assert isinstance(options_dict.get("BlocksMatchContent").get("value"), bool)
    if "SkipQuiz" in options_dict:
        assert isinstance(options_dict.get("SkipQuiz").get("value"), bool)
    if "CapEnemyXP" in options_dict:
        assert isinstance(options_dict.get("CapEnemyXP").get("value"), bool)
    if "2xDamage" in options_dict:
        assert isinstance(options_dict.get("2xDamage").get("value"), bool)
    if "4xDamage" in options_dict:
        assert isinstance(options_dict.get("4xDamage").get("value"), bool)
    if "OHKO" in options_dict:
        assert isinstance(options_dict.get("OHKO").get("value"), bool)

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
    if "ShuffleChapterDifficulty" in options_dict:
        assert isinstance(options_dict.get("ShuffleChapterDifficulty").get("value"), bool)
    if "RandomFormations" in options_dict:
        assert isinstance(options_dict.get("RandomFormations").get("value"), bool)

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
    if "IncludeFavors" in options_dict:
        assert isinstance(options_dict.get("IncludeFavors").get("value"), bool)
    if "IncludeLetterChain" in options_dict:
        assert isinstance(options_dict.get("IncludeLetterChain").get("value"), bool)
    if "PlacementAlgorithm" in options_dict:
        assert (isinstance(options_dict.get("PlacementAlgorithm").get("value"), str)
            and options_dict.get("PlacementAlgorithm").get("value") in [
                "ForwardFill",
                #"WeightedForwardFill", # NYI
                #"AssumedFill", # NYI
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
    if "KeyitemsOutsideArea" in options_dict:
        assert isinstance(options_dict.get("KeyitemsOutsideArea").get("value"), bool)
    if "KeyitemsOutsideChapter" in options_dict:
        assert isinstance(options_dict.get("KeyitemsOutsideChapter").get("value"), bool)

    # Moves and Badges
    if "ShuffleBadgesBP" in options_dict:
        assert isinstance(options_dict.get("ShuffleBadgesBP").get("value"), bool)
    if "ShuffleBadgesFP" in options_dict:
        assert isinstance(options_dict.get("ShuffleBadgesFP").get("value"), bool)
    if "ShufflePartnerFP" in options_dict:
        assert isinstance(options_dict.get("ShufflePartnerFP").get("value"), bool)
    if "ShuffleStarpowerSP" in options_dict:
        assert isinstance(options_dict.get("ShuffleStarpowerSP").get("value"), bool)

    # Entrance related
    if "RandomizeOnewayEntrances" in options_dict:
        assert isinstance(options_dict.get("RandomizeOnewayEntrances").get("value"), bool)
    if "UnpairedEntrances" in options_dict:
        assert isinstance(options_dict.get("UnpairedEntrances").get("value"), bool)

    # Partner related
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
    if "RandomCoinPalette" in options_dict:
        assert isinstance(options_dict.get("RandomCoinPalette").get("value"), bool)

    # Audio
    if "TurnOffAudio" in options_dict:
        assert isinstance(options_dict.get("TurnOffMusic").get("value"), bool)


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
