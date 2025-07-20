from models.options.option_utility import get_option_default_value

from metadata.area_name_mappings import area_name_id_map

from rando_enums.enum_options import (
    IncludeFavorsMode,
    IncludeLettersMode,
    RandomizeConsumablesMode,
    ItemTrapMode,
    PartnerShuffle,
    DojoShuffle,
    MultiCoinBlockShuffle,
    RequiredChapters,
    BowserDoorQuiz,
    KentCKoopa,
)

class LogicOptionSet():
    def __init__(self):
        # General
        self.hidden_block_mode = get_option_default_value("HiddenBlockMode")

        # QOL
        self.always_speedyspin = bool(get_option_default_value("AlwaysSpeedySpin"))
        self.always_ispy = bool(get_option_default_value("AlwaysISpy"))
        self.always_peekaboo = bool(get_option_default_value("AlwaysPeekaboo"))

        # Difficulty and Enemies
        self.boss_shuffle_mode = get_option_default_value("BossShuffleMode")

        # Item Placement
        self.shuffle_items = bool(get_option_default_value("ShuffleItems"))
        self.include_coins_overworld = True
        self.include_coins_blocks = True
        self.include_coins_foliage = True
        self.include_coins_favors = False
        self.include_shops = bool(get_option_default_value("IncludeShops"))
        self.progression_on_rowf = 5
        self.progression_on_merlow = True
        self.include_panels = bool(get_option_default_value("IncludePanels"))
        self.include_favors_mode = IncludeFavorsMode.NOT_RANDOMIZED
        self.include_letters_mode = IncludeLettersMode.NOT_RANDOMIZED
        self.include_radiotradeevent = False
        self.include_dojo = DojoShuffle.OFF
        self.keyitems_outside_dungeon = True
        self.keyitems_outside_chapter = True # "Keysanity" # false -> NYI

        # Item Pool Modification
        self.gear_shuffle_mode = get_option_default_value("GearShuffleMode")
        self.spirit_shuffle_mode = get_option_default_value("SpiritShuffleMode")
        self.add_item_pouches = False
        self.partner_upgrade_shuffle = get_option_default_value("PartnerUpgradeShuffle")
        self.add_unused_badge_duplicates = False
        self.add_beta_items = False
        self.progressive_badges = False
        self.badge_pool_limit = 128 # literal cap of Paper Mario
        self.randomize_consumable_mode = RandomizeConsumablesMode.OFF
        self.item_quality = 100
        self.itemtrap_mode = ItemTrapMode.OFF

        # Item Misc
        self.cook_without_fryingpan = bool(get_option_default_value("CookWithoutFryingPan"))
        self.ripcheato_items_in_logic = 6

        # Starting setup
        self.starting_map = get_option_default_value("StartingMap") # mac_00 Entry 4
        self.starting_boots = get_option_default_value("StartingBoots") #
        self.starting_hammer = get_option_default_value("StartingHammer") #

        self.random_starting_items = False
        self.random_starting_items_min = 0
        self.random_starting_items_max = 16
        self.starting_item_0 = get_option_default_value("StartingItem0")
        self.starting_item_1 = get_option_default_value("StartingItem1")
        self.starting_item_2 = get_option_default_value("StartingItem2")
        self.starting_item_3 = get_option_default_value("StartingItem3")
        self.starting_item_4 = get_option_default_value("StartingItem4")
        self.starting_item_5 = get_option_default_value("StartingItem5")
        self.starting_item_6 = get_option_default_value("StartingItem6")
        self.starting_item_7 = get_option_default_value("StartingItem7")
        self.starting_item_8 = get_option_default_value("StartingItem8")
        self.starting_item_9 = get_option_default_value("StartingItem9")
        self.starting_item_A = get_option_default_value("StartingItemA")
        self.starting_item_B = get_option_default_value("StartingItemB")
        self.starting_item_C = get_option_default_value("StartingItemC")
        self.starting_item_D = get_option_default_value("StartingItemD")
        self.starting_item_E = get_option_default_value("StartingItemE")
        self.starting_item_F = get_option_default_value("StartingItemF")

        # Partners
        self.starting_partners = ["Goombario"]
        self.start_with_goombario = bool(get_option_default_value("StartWithGoombario"))
        self.start_with_kooper = bool(get_option_default_value("StartWithKooper"))
        self.start_with_bombette = bool(get_option_default_value("StartWithBombette"))
        self.start_with_parakarry = bool(get_option_default_value("StartWithParakarry"))
        self.start_with_bow = bool(get_option_default_value("StartWithBow"))
        self.start_with_watt = bool(get_option_default_value("StartWithWatt"))
        self.start_with_sushie = bool(get_option_default_value("StartWithSushie"))
        self.start_with_lakilester = bool(get_option_default_value("StartWithLakilester"))

        self.partner_shuffle = PartnerShuffle.VANILLA
        self.partners_always_usable = bool(get_option_default_value("PartnersAlwaysUsable"))
        self.random_partners = False
        self.random_partners_min = 1
        self.random_partners_max = 1

        # Pre-opened areas
        self.magical_seeds_required = get_option_default_value("MagicalSeedsRequired")
        self.prologue_open = bool(get_option_default_value("PrologueOpen"))
        self.bluehouse_open = bool(get_option_default_value("BlueHouseOpen"))
        self.mtrugged_open = bool(get_option_default_value("MtRuggedOpen"))
        self.foreverforest_open = bool(get_option_default_value("ForeverForestOpen"))
        self.toybox_open = bool(get_option_default_value("ToyboxOpen"))
        self.whale_open = bool(get_option_default_value("WhaleOpen"))
        self.ch7_bridge_visible = bool(get_option_default_value("Ch7BridgeVisible"))

        # Goal Settings
        self.seed_goal = get_option_default_value("SeedGoal")
        self.bowsers_castle_mode = get_option_default_value("BowsersCastleMode")
        self.starway_spirits_needed_count = get_option_default_value("StarWaySpiritsNeededCnt")
        self.starway_chapters_needed_count = get_option_default_value("StarWayChaptersNeededCnt")
        self.starway_chapters_needed_encoded = get_option_default_value("StarWayChaptersNeededEnc")
        self.starway_powerstars_needed = get_option_default_value("StarWayPowerStarsNeeded")
        self.shuffle_starbeam = False
        self.starbeam_location = area_name_id_map["HOS"]
        self.starbeam_chapters_needed = get_option_default_value("StarBeamChaptersNeeded")
        self.starbeam_spirits_needed = get_option_default_value("StarBeamSpiritsNeeded")
        self.starbeam_powerstars_needed = get_option_default_value("StarBeamPowerStarsNeeded")
        self.star_hunt_total = get_option_default_value("StarHuntTotal")
        self.required_chapters = RequiredChapters.ANY

        # Entrance Shuffle
        self.shuffle_dungeon_rooms = bool(get_option_default_value("ShuffleDungeonRooms"))
        self.shuffle_dungeon_entrances = get_option_default_value("ShuffleDungeonEntrances")
        self.shuffle_entrances_by_all = bool(get_option_default_value("ShuffleEntrancesByAll"))
        self.match_entrance_type = bool(get_option_default_value("MatchEntranceTypes"))
        self.random_oneway_entrances = False # NYI
        self.unpaired_entrances = False # NYI

        # Misc Gameplay Randomization
        self.multicoin_block_shuffle = MultiCoinBlockShuffle.OFF
        self.randomize_puzzles = False
        self.bowserdoor_quiz = BowserDoorQuiz.DO_QUIZ
        self.kentckoopa = KentCKoopa.BLOCKS_PLEASANT_PATH
