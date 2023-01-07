from enum import IntEnum, unique

@unique
class BlockType(IntEnum):
    MULTICOIN = 0
    SUPER = 1
