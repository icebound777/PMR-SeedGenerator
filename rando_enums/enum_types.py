from enum import IntEnum, unique

@unique
class SongType(IntEnum):
    BATTLE = 0
    BOSS = 1
    EVENT = 2
    FIELDANDTOWN = 3
    JINGLE = 4

@unique
class SongMood(IntEnum):
    RELAXED = 0
    UPBEAT = 1
    SINISTER = 2
    CRISIS = 3
    BATTLE = 4
    BOSS = 5
