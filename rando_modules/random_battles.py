"""
This module can modify which battleID gets loaded instead of the original
battle, allowing for shuffling encounters.
"""

import random

from db.battle import Battle

from metadata.formations_meta import chapter_battle_mapping
from rando_enums.enum_options import BossShuffleMode


def get_boss_battles(
    boss_shuffle_mode: BossShuffleMode,
    plando_battles: dict | None,
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

    battles_setup: list[tuple[int, int]] = []
    chapter_boss_map: dict[int, int] = dict()
    db_chapters_keysvalues: dict[int, tuple[int, int]] = dict()

    for battle in Battle.select():
        key, value = battle.get_key(), battle.vanilla_battle_id

        battle_group = get_battle_group(value)
        chapter = get_battle_chapter(battle_group)
        assert(chapter is not None)

        db_chapters_keysvalues[chapter] = (key, value)

    if plando_battles is not None and len(plando_battles) == 7:
        chapter_boss_map = plando_battles
    elif boss_shuffle_mode == BossShuffleMode.OFF:
        chapter_boss_map = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7} # default
        if plando_battles is not None:
            chapter_boss_map.update(plando_battles)
    elif boss_shuffle_mode == BossShuffleMode.CHAPTER_BOSSES:
        chapters: list[int] = list(db_chapters_keysvalues.keys())
        # chapters = [1,2,3,4,5,6,7]

        if plando_battles:
            # plando_battles = {1: 3, 2: 7} Tubba in TRD, CK in ISK
            for x in plando_battles:
                # x = [1,2]
                if x in chapters:
                    chapters.remove(x)
                    # chapters = [3,4,5,6,7]

            not_plandod_bosses = [
                x for x in range(1, 8)
                if x not in plando_battles.values()
            ]
            # not_plandod_bosses = [1,2,4,5,6]

            random.shuffle(chapters)
            # chapters = [6,3,7,4,5]

            while not_plandod_bosses and chapters:
                chapter_boss_map[chapters.pop()] = not_plandod_bosses.pop()
                # chapter_boss_map = {
                #     5: 6,
                #     4: 5,
                #     7: 4,
                #     3: 2,
                #     6: 1
                # }

            chapter_boss_map.update(plando_battles)
            # chapter_boss_map = {
            #     5: 6,
            #     4: 5,
            #     7: 4,
            #     3: 2,
            #     6: 1,
            #     1: 3,
            #     2: 7
            # }

        else:
            random.shuffle(chapters)
            # chapters = [4,3,5,7,2,1,6]

            for chapter, boss in enumerate(iterable=chapters, start=1):
            # chapter, boss = (1, 4) (2, 3), (3,5), (4,7), (5,2), (6,1), (7,6)
                chapter_boss_map[chapter] = boss
                # chapter_boss_map = {
                #     1: 4,
                #     2: 3,
                #     3: 5,
                #     4: 7,
                #     5: 2,
                #     6: 1,
                #     7: 6,
                # }

    for chapter, boss in chapter_boss_map.items():
        battles_setup.append(
            (db_chapters_keysvalues[chapter][0], db_chapters_keysvalues[boss][1])
        )
        # battles_setup = [
        #     (db_chapters_keysvalues[1].dbkey, db_chapters_keysvalues[4].dbvalue)
        #     (db_chapters_keysvalues[2].dbkey, db_chapters_keysvalues[3].dbvalue)
        #     (db_chapters_keysvalues[3].dbkey, db_chapters_keysvalues[5].dbvalue)
        #     (db_chapters_keysvalues[4].dbkey, db_chapters_keysvalues[7].dbvalue)
        #     (db_chapters_keysvalues[5].dbkey, db_chapters_keysvalues[2].dbvalue)
        #     (db_chapters_keysvalues[6].dbkey, db_chapters_keysvalues[1].dbvalue)
        #     (db_chapters_keysvalues[7].dbkey, db_chapters_keysvalues[6].dbvalue)
        # ]

    return battles_setup, chapter_boss_map
