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
        db_chapters_keysvalues: dict[int, tuple[int, int]] = dict()

        for battle in Battle.select():
            key, value = battle.get_key(), battle.vanilla_battle_id

            battle_group = get_battle_group(value)
            chapter = get_battle_chapter(battle_group)
            assert(chapter is not None)

            db_chapters_keysvalues[chapter] = (key, value)

        chapters: list[int] = list(db_chapters_keysvalues.keys())
        random.shuffle(chapters)
        for chapter, boss in enumerate(iterable=chapters, start=1):
            boss_chapter_map[boss] = chapter
        for boss, chapter in boss_chapter_map.items():
            battles_setup.append(
                (db_chapters_keysvalues[chapter][0], db_chapters_keysvalues[boss][1])
            )

    return battles_setup, boss_chapter_map
