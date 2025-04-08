from enum import IntEnum, unique

@unique
class BowserCastleMode(IntEnum):
    VANILLA = 0
    SHORTEN = 1
    BOSSRUSH = 2

@unique
class HiddenBlockMode(IntEnum):
    VANILLA = 0
    WATT_OUT = 1
    WATT_ACQUIRED = 2
    ALWAYS_VISIBLE = 3

@unique
class StartingBoots(IntEnum):
    JUMPLESS = -1
    BOOTS = 0
    SUPERBOOTS = 1
    ULTRABOOTS = 2

@unique
class StartingHammer(IntEnum):
    HAMMERLESS = -1
    HAMMER = 0
    SUPERHAMMER = 1
    ULTRAHAMMER = 2

@unique
class IncludeFavorsMode(IntEnum):
    NOT_RANDOMIZED = 0
    RND_REWARD_VANILLA_KEYITEMS = 1
    FULL_SHUFFLE = 2

@unique
class IncludeLettersMode(IntEnum):
    NOT_RANDOMIZED = 0
    SIMPLE_LETTERS = 1
    RANDOM_CHAIN_REWARD = 2
    FULL_SHUFFLE = 3

@unique
class RandomizeConsumablesMode(IntEnum):
    OFF = 0
    FULL_RANDOM = 1
    BALANCED_RANDOM = 2
    MYSTERY_ONLY = 3

@unique
class ItemTrapMode(IntEnum):
    OFF = 0
    SPARSE = 1
    MODERATE = 2
    PLENTY = 3

@unique
class GearShuffleMode(IntEnum):
    VANILLA = 0
    GEAR_LOCATION_SHUFFLE = 1
    FULL_SHUFFLE = 2

@unique
class RandomMoveCosts(IntEnum):
    VANILLA = 0
    BALANCED_RANDOM = 1
    SHUFFLED = 2
    FULLY_RANDOM = 3

@unique
class RandomPalettes(IntEnum):
    DEFAULT_PALETTE = 0
    SELECT_PALETTE = 1
    RANDOM_PICK = 2
    RANDOM_PICK_NOT_VANILLA = 3
    ALWAYS_RANDOM = 4

@unique
class MusicRandomizationType(IntEnum):
    MOOD = 0
    TYPE = 1
    FULL = 2

@unique
class MerlowRewardPricing(IntEnum):
    CHEAP = 0
    NORMAL = 1

    @classmethod
    def has_value(cls, value):
        return (value in set(item.value for item in cls))

@unique
class PartnerUpgradeShuffle(IntEnum):
    OFF = 0
    SUPERBLOCKLOCATIONS = 1
    FULL = 2

@unique
class MultiCoinBlockShuffle(IntEnum):
    OFF = 0
    SHUFFLE = 1
    ANYWHERE = 2

@unique
class SeedGoal(IntEnum):
    DEFEAT_BOWSER = 0
    OPEN_STARWAY = 1

@unique
class DungeonEntranceShuffle(IntEnum):
    OFF = 0
    ONLY_SPIRIT_DUNGEONS = 1
    INCLUDE_BOWSERSCASTLE = 2

@unique
class PartnerShuffle(IntEnum):
    VANILLA = 0
    SHUFFLED = 1
    ANYWHERE = 2

@unique
class DojoShuffle(IntEnum):
    OFF = 0
    INCLUDE_CHAN = 1
    INCLUDE_LEE = 2
    INCLUDE_MASTER1 = 3
    INCLUDE_MASTER2 = 4
    INCLUDE_MASTER3 = 5

@unique
class BossShuffleMode(IntEnum):
    OFF = 0
    CHAPTER_BOSSES = 1

@unique
class RequiredSpirits(IntEnum):
    ANY = 0
    SPECIFIC = 1
    SPECIFIC_AND_LIMITCHAPTERLOGIC = 2

@unique
class BowserDoorQuiz(IntEnum):
    DO_QUIZ = 0
    ANTI_GUYS_UNIT = 1
    SKIP = 2

@unique
class KentCKoopa(IntEnum):
    BLOCKS_PLEASANT_PATH = 0
    MUST_FIGHT = 1
    ALREADY_PAID = 2
    ALREADY_DEFEATED = 3
