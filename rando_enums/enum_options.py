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
