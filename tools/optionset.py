from db.option import Option

class OptionSet:
    def __init__(self):
        """ Load Defaults from DB """
        # General
        self.initial_coins = Option.get(Option.name == "InitialCoins")
        self.replace_duplicate_keys = Option.get(Option.name == "ReplaceDuplicateKeys")
        self.duplicate_key_replacement = Option.get(Option.name == "DuplicateKeyReplacement")
        self.flowergate_open = Option.get(Option.name == "FlowerGateOpen")
        self.bluehouse_open = Option.get(Option.name == "BlueHouseOpen")
        self.blocks_match_content = Option.get(Option.name == "BlocksMatchContent")
        self.skip_quiz = Option.get(Option.name == "SkipQuiz")
        self.cap_enemy_xp = Option.get(Option.name == "CapEnemyXP")
        self.damage_x2 = Option.get(Option.name == "2xDamage")
        self.damage_x4 = Option.get(Option.name == "4xDamage")
        self.ohko = Option.get(Option.name == "OHKO")

        # Item related
        self.shuffle_items = Option.get(Option.name == "ShuffleItems")
        self.include_coins = Option.get(Option.name == "IncludeCoins")
        self.include_shops = Option.get(Option.name == "IncludeShops")
        self.include_panels = Option.get(Option.name == "IncludePanels")

        # Entrance related
        self.shuffle_entrances = Option.get(Option.name == "ShuffleEntrances")
        self.shuffle_entrances_by_area = Option.get(Option.name == "ShuffleEntrancesByArea")
        self.shuffle_entrances_by_all = Option.get(Option.name == "ShuffleEntrancesByAll")
        self.match_entrance_type = Option.get(Option.name == "MatchEntranceTypes")

        # Settings unavailable in the GUI
        # General
        self.starting_map = 0x00010104 # mac_00 Entry 4
        self.random_quiz = True # ?
        self.shuffle_chapter_difficulty = False

        # Item related
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

        # Spoiler log
        self.write_spoilerlog = True
        self.pretty_spoilerlog = True

        # Cosmetics
        self.color_a = 0xEBE677FF # Box5ColorA
        self.color_b = 0x8E5A25FF # Box5ColorB
        self.random_coin_palette = False

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
        if "InitialCoins" in options_dict:
            self.initial_coins.value = options_dict.get("InitialCoins")
            self.initial_coins.save()
        if "ReplaceDuplicateKeys" in options_dict:
            self.replace_duplicate_keys.value = options_dict.get("ReplaceDuplicateKeys")
            self.replace_duplicate_keys.save()
        if "DuplicateKeyReplacement" in options_dict:
            self.duplicate_key_replacement.value = options_dict.get("DuplicateKeyReplacement")
            self.duplicate_key_replacement.save()
        if "FlowerGateOpen" in options_dict:
            self.flowergate_open.value = options_dict.get("FlowerGateOpen")
            self.flowergate_open.save()
        if "BlueHouseOpen" in options_dict:
            self.bluehouse_open.value = options_dict.get("BlueHouseOpen")
            self.bluehouse_open.save()
        if "BlocksMatchContent" in options_dict:
            self.blocks_match_content.value = options_dict.get("BlocksMatchContent")
            self.blocks_match_content.save()
        if "SkipQuiz" in options_dict:
            self.skip_quiz.value = options_dict.get("SkipQuiz")
            self.skip_quiz.save()
        if "CapEnemyXP" in options_dict:
            self.cap_enemy_xp.value = options_dict.get("CapEnemyXP")
            self.cap_enemy_xp.save()
        if "2xDamage" in options_dict:
            self.damage_x2.value = options_dict.get("2xDamage")
            self.damage_x2.save()
        if "4xDamage" in options_dict:
            self.damage_x4.value = options_dict.get("4xDamage")
            self.damage_x4.save()
        if "OHKO" in options_dict:
            self.ohko.value = options_dict.get("OHKO")
            self.ohko.save()

        # Item related
        if "ShuffleItems" in options_dict:
            self.shuffle_items.value = options_dict.get("ShuffleItems")
            self.shuffle_items.save()
        if "IncludeCoins" in options_dict:
            self.include_coins.value = options_dict.get("IncludeCoins")
            self.include_coins.save()
        if "IncludeShops" in options_dict:
            self.include_shops.value = options_dict.get("IncludeShops")
            self.include_shops.save()
        if "IncludePanels" in options_dict:
            self.include_panels.value = options_dict.get("IncludePanels")
            self.include_panels.save()

        # Entrance related
        if "ShuffleEntrances" in options_dict:
            self.shuffle_entrances.value = options_dict.get("ShuffleEntrances")
            self.shuffle_entrances.save()
        if "ShuffleEntrancesByArea" in options_dict:
            self.shuffle_entrances_by_area.value = options_dict.get("ShuffleEntrancesByArea")
            self.shuffle_entrances_by_area.save()
        if "ShuffleEntrancesByAll" in options_dict:
            self.shuffle_entrances_by_all.value = options_dict.get("ShuffleEntrancesByAll")
            self.shuffle_entrances_by_all.save()
        if "MatchEntranceTypes" in options_dict:
            self.match_entrance_type.value = options_dict.get("MatchEntranceTypes")
            self.match_entrance_type.save()

        # Settings unavailable in the GUI
        # General
        if "StartingMap" in options_dict:
            self.starting_map = options_dict.get("StartingMap")
        if "RandomQuiz" in options_dict:
            self.random_quiz = options_dict.get("RandomQuiz")
        if "ShuffleChapterDifficulty" in options_dict:
            self.shuffle_chapter_difficulty = options_dict.get("ShuffleChapterDifficulty")

        # Item related
        if "PlacementAlgorithm" in options_dict:
            self.placement_algorithm = options_dict.get("PlacementAlgorithm")
        if "PlacementLogic" in options_dict:
            self.placement_logic = options_dict.get("PlacementLogic")
        if "KeyitemsOutsideArea" in options_dict:
            self.keyitems_outside_area = options_dict.get("KeyitemsOutsideArea")
        if "KeyitemsOutsideChapter" in options_dict:
            self.keyitems_outside_chapter = options_dict.get("KeyitemsOutsideChapter")

        # Moves and Badges
        if "ShuffleBadgesBP" in options_dict:
            self.shuffle_badges_bp = options_dict.get("ShuffleBadgesBP")
        if "ShuffleBadgesFP" in options_dict:
            self.shuffle_badges_fp = options_dict.get("ShuffleBadgesFP")
        if "ShufflePartnerFP" in options_dict:
            self.shuffle_partner_fp = options_dict.get("ShufflePartnerFP")
        if "ShuffleStarpowerSP" in options_dict:
            self.shuffle_starpower_sp = options_dict.get("ShuffleStarpowerSP")

        # Entrance related
        if "RandomizeOnewayEntrances" in options_dict:
            self.random_oneway_entrances = options_dict.get("RandomizeOnewayEntrances")
        if "UnpairedEntrances" in options_dict:
            self.unpaired_entrances = options_dict.get("UnpairedEntrances")

        # Partner related
        if "StartWithRandomPartners" in options_dict:
            self.random_partners = options_dict.get("StartWithRandomPartners")
        if "RandomPartnersMin" in options_dict:
            self.random_partners_min = options_dict.get("RandomPartnersMin")
        if "RandomPartnersMax" in options_dict:
            self.random_partners_max = options_dict.get("RandomPartnersMax")
        if "StartWithPartners" in options_dict:
            self.starting_partners.clear()
            for partner, start_with_partner in options_dict.get("StartWithPartners").items():
                if (start_with_partner):
                    self.starting_partners.append(f"PARTNER_{partner}")

        # Cosmetics / Palettes
        if "RandomCoinPalette" in options_dict:
            self.random_coin_palette = options_dict.get("RandomCoinPalette")


def validate_options(options_dict):
    if options_dict is None:
        raise ValueError

    # General
    if "InitialCoins" in options_dict:
        assert (isinstance(options_dict.get("InitialCoins"), int)
            and 0 <= options_dict.get("InitialCoins") <= 999
        )
    if "ReplaceDuplicateKeys" in options_dict:
        assert isinstance(options_dict.get("ReplaceDuplicateKeys"), bool)
    if "DuplicateKeyReplacement" in options_dict:
        assert isinstance(options_dict.get("DuplicateKeyReplacement"), int)
    if "FlowerGateOpen" in options_dict:
        assert isinstance(options_dict.get("FlowerGateOpen"), bool)
    if "BlueHouseOpen" in options_dict:
        assert isinstance(options_dict.get("BlueHouseOpen"), bool)
    if "BlocksMatchContent" in options_dict:
        assert isinstance(options_dict.get("BlocksMatchContent"), bool)
    if "SkipQuiz" in options_dict:
        assert isinstance(options_dict.get("SkipQuiz"), bool)
    if "CapEnemyXP" in options_dict:
        assert isinstance(options_dict.get("CapEnemyXP"), bool)
    if "2xDamage" in options_dict:
        assert isinstance(options_dict.get("2xDamage"), bool)
    if "4xDamage" in options_dict:
        assert isinstance(options_dict.get("4xDamage"), bool)
    if "OHKO" in options_dict:
        assert isinstance(options_dict.get("OHKO"), bool)

    # Item related
    if "ShuffleItems" in options_dict:
        assert isinstance(options_dict.get("ShuffleItems"), bool)
    if "IncludeCoins" in options_dict:
        assert isinstance(options_dict.get("IncludeCoins"), bool)
    if "IncludeShops" in options_dict:
        assert isinstance(options_dict.get("IncludeShops"), bool)
    if "IncludePanels" in options_dict:
        assert isinstance(options_dict.get("IncludePanels"), bool)

    # Entrance related
    if "ShuffleEntrances" in options_dict:
        assert isinstance(options_dict.get("ShuffleEntrances"), bool)
    if "ShuffleEntrancesByArea" in options_dict:
        assert isinstance(options_dict.get("ShuffleEntrancesByArea"), bool)
    if "ShuffleEntrancesByAll" in options_dict:
        assert isinstance(options_dict.get("ShuffleEntrancesByAll"), bool)
    if "MatchEntranceTypes" in options_dict:
        assert isinstance(options_dict.get("MatchEntranceTypes"), bool)

    # Settings unavailable in the GUI
    # General
    if "StartingMap" in options_dict:
        assert isinstance(options_dict.get("StartingMap"), int)
    if "RandomQuiz" in options_dict:
        assert isinstance(options_dict.get("RandomQuiz"), bool)
    if "ShuffleChapterDifficulty" in options_dict:
        assert isinstance(options_dict.get("ShuffleChapterDifficulty"), bool)

    # Item related
    if "PlacementAlgorithm" in options_dict:
        assert (isinstance(options_dict.get("PlacementAlgorithm"), str)
            and options_dict.get("PlacementAlgorithm") in [
                "ForwardFill",
                #"WeightedForwardFill", # NYI
                #"AssumedFill", # NYI
                "CustomSeed"
            ]
        )
    if "PlacementLogic" in options_dict:
        assert (isinstance(options_dict.get("PlacementLogic"), str)
            and options_dict.get("PlacementLogic") in [
                "NoGlitches",
                #"Glitches", # NYI
                "NoLogic"
            ]
        )
    if "KeyitemsOutsideArea" in options_dict:
        assert isinstance(options_dict.get("KeyitemsOutsideArea"), bool)
    if "KeyitemsOutsideChapter" in options_dict:
        assert isinstance(options_dict.get("KeyitemsOutsideChapter"), bool)

    # Moves and Badges
    if "ShuffleBadgesBP" in options_dict:
        assert isinstance(options_dict.get("ShuffleBadgesBP"), bool)
    if "ShuffleBadgesFP" in options_dict:
        assert isinstance(options_dict.get("ShuffleBadgesFP"), bool)
    if "ShufflePartnerFP" in options_dict:
        assert isinstance(options_dict.get("ShufflePartnerFP"), bool)
    if "ShuffleStarpowerSP" in options_dict:
        assert isinstance(options_dict.get("ShuffleStarpowerSP"), bool)

    # Entrance related
    if "RandomizeOnewayEntrances" in options_dict:
        assert isinstance(options_dict.get("RandomizeOnewayEntrances"), bool)
    if "UnpairedEntrances" in options_dict:
        assert isinstance(options_dict.get("UnpairedEntrances"), bool)

    # Partner related
    if "StartWithRandomPartners" in options_dict:
        assert isinstance(options_dict.get("StartWithRandomPartners"), bool)
    if "RandomPartnersMin" in options_dict:
        assert (isinstance(options_dict.get("RandomPartnersMin"), int)
            and 1 <= options_dict.get("RandomPartnersMin") <= 8
            and ("RandomPartnersMax" not in options_dict
              or options_dict.get("RandomPartnersMin") <= 
                 options_dict.get("RandomPartnersMax"))
        )
    if "RandomPartnersMax" in options_dict:
        assert (isinstance(options_dict.get("RandomPartnersMax"), int)
            and 1 <= options_dict.get("RandomPartnersMax") <= 8
            and ("RandomPartnersMin" not in options_dict
              or options_dict.get("RandomPartnersMin") <= 
                 options_dict.get("RandomPartnersMax"))
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
        assert (isinstance(options_dict.get("StartWithPartners"), dict)
            and all(key in permitted_values for key in options_dict.get("StartWithPartners"))
            and all(isinstance(value, bool) for value in options_dict.get("StartWithPartners").values())
            and any(value for value in options_dict.get("StartWithPartners").values()))

    # Cosmetics / Palettes
    if "RandomCoinPalette" in options_dict:
        assert isinstance(options_dict.get("RandomCoinPalette"), bool)
