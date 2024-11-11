"""
This module can modify which battleID gets loaded instead of the original
battle, allowing for shuffling encounters.
"""

import random

from db.battle import Battle

from metadata.formations_meta import chapter_battle_mapping
from rando_enums.enum_options import BossShuffleMode


def get_boss_battles(
    boss_shuffle_mode: BossShuffleMode
) -> tuple[list[tuple[int, int]], dict[int, int]]:
    def get_battle_group(battle: int) -> int:
        # battles have two bytes, the upper byte signifies the battle group
        # to load, the lower byte the id within that group
        return battle >> 8
    def get_battle_chapter(battle_group: int) -> int | None:
        for chapter, battle_group_list in chapter_battle_mapping.items():
            if battle_group in [int(x, 16) for x in battle_group_list]:
                return chapter
        return None

    battles_setup: List[Tuple[int, int]] = []

    if boss_shuffle_mode == BossShuffleMode.OFF:
        for battle in Battle.select():
            battles_setup.append((battle.get_key(), battle.vanilla_battle_id))
        boss_chapter_map = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7} # default
    elif boss_shuffle_mode == BossShuffleMode.CHAPTER_BOSSES:
        db_keys_and_chapters: list = []
        db_values_and_chapters: List[Tuple[int, int]] = []

        for battle in Battle.select():
            key, value = battle.get_key(), battle.vanilla_battle_id

            battle_group = get_battle_group(value)
            chapter = get_battle_chapter(battle_group)
            assert(chapter is not None)

            db_keys_and_chapters.append((key, chapter))
            db_values_and_chapters.append((value, chapter))

        random.shuffle(db_values_and_chapters)

        battles_setup: List[Tuple[int, int]] = list(zip(
            [x[0] for x in db_keys_and_chapters], [x[0] for x in db_values_and_chapters]
        ))
        boss_chapter_map: Dict[int, int] = dict(zip(
            [x[1] for x in db_values_and_chapters], [x[1] for x in db_keys_and_chapters]
        )) # e.g. General Guy appears in chapter 1, so (4, 1)


    return battles_setup, boss_chapter_map
