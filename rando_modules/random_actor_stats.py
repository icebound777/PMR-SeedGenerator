import random

from db.actor_attribute import ActorAttribute
from db.actor_params import ActorParam

from metadata.formations_meta import bossactor_chapter_map

def get_shuffled_chapter_difficulty(
    shuffle_chapter_difficulty:bool,
    chapter_boss_map: dict[int, int], # e.g. chapter 1 -> General Guy, so {1: 4}
    progressive_scaling:bool,
    starting_chapter: int,
    plando_difficulty: dict[int, int] | None,
):
    # Load and reorganize actor param data into different format
    # format example:
    # "00_Goomba": {
    #     "Level": [5,8,10,13,15,18,20,23],
    #     "HP": [2,3,4,5,6,7,8],
    #     "DamageA": [1,2,2,3,3,4,4,5]
    #     "NativeChapter": 1
    # }
    all_enemy_stats = {}

    for actor_param in ActorParam.select():
        actor_name = actor_param.actor_name
        actor_native_chapter = actor_param.native_chapter
        actor_stat_name = actor_param.actor_stat_name
        actor_stat_values = [
            actor_param.chapter_1,
            actor_param.chapter_2,
            actor_param.chapter_3,
            actor_param.chapter_4,
            actor_param.chapter_5,
            actor_param.chapter_6,
            actor_param.chapter_7,
            actor_param.chapter_8,
        ]

        # add actor to all enemy stats
        if not actor_name in all_enemy_stats:
            all_enemy_stats[actor_name] = {}
            if (    actor_name in [x for x1 in bossactor_chapter_map.values() for x in x1]
                and actor_native_chapter in chapter_boss_map.values()
            ):
                # is boss
                flipped_chapter_boss_map = {}
                for chapter, boss in chapter_boss_map.items():
                    flipped_chapter_boss_map[boss] = chapter
                all_enemy_stats[actor_name]["NativeChapter"] = flipped_chapter_boss_map[actor_native_chapter]
            else:
                # is not boss
                all_enemy_stats[actor_name]["NativeChapter"] = actor_native_chapter

        all_enemy_stats[actor_name][actor_stat_name] = actor_stat_values

    # Randomly promote enemies to higher scaling
    _random_enemy_promotions(
        all_enemy_stats,
        shuffle_chapter_difficulty
    )

    # Pair chapter numbers with chapter difficulties
    chapter_dict = _assign_chapter_difficulties(
        shuffle_chapter_difficulty = shuffle_chapter_difficulty,
        starting_chapter = starting_chapter,
        plando_difficulty = plando_difficulty,
    )

    # Set enemy stats according to chapter difficulties
    new_enemy_stats = []
    for actor_attribute in ActorAttribute.select():
        dbkey = actor_attribute.get_key()
        actor_name = actor_attribute.actor_name
        actor_stat_name = actor_attribute.attribute
        if (
               actor_name not in all_enemy_stats
            or actor_stat_name not in all_enemy_stats[actor_name]
            or (not progressive_scaling and not shuffle_chapter_difficulty)
        ):
            # not supposed to be random, so write defaults
            value = actor_attribute.value
        else:
            native_chapter = all_enemy_stats[actor_name]["NativeChapter"]
            if native_chapter == -1:
                # Special case for Dojo / Kent
                native_chapter = 1
            value = int(all_enemy_stats[actor_name][actor_stat_name][chapter_dict.get(native_chapter) - 1])
            if all_enemy_stats[actor_name]["Promoted"]:
                value = int(all_enemy_stats[actor_name][actor_stat_name][chapter_dict.get(native_chapter) + 1])

        new_enemy_stats.append((dbkey, value))

    return new_enemy_stats, chapter_dict


def _assign_chapter_difficulties(
    shuffle_chapter_difficulty: bool,
    starting_chapter: int,
    plando_difficulty: dict[int, int] | None,
) -> dict[int, int]:
    """
    Pair chapter numbers with chapter difficulties according to given settings,
    and returns a dictionary representing these pairings.
    The values set here are of no relevance if chapter scaling is set to
    progressive.
    """
    chapter_difficulties = [1,2,3,4,5,6,7]
    chapter_dict: dict[int, int] = {}

    if not shuffle_chapter_difficulty:
        # Vanilla difficulty
        chapter_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}

        if plando_difficulty:
            for k, v in plando_difficulty.items():
                chapter_dict[k] = v

    elif shuffle_chapter_difficulty and not plando_difficulty:
        # Shuffle chapter difficulty, making sure the starting chapter is not
        # harder than ch3 difficulty
        random.shuffle(chapter_difficulties)

        for chapter_number, new_difficulty in enumerate(chapter_difficulties):
            chapter_dict[chapter_number + 1] = new_difficulty
        # Chapter 8 is never shuffled
        chapter_dict[8] = 8

        # Check if the chapter we are starting in is too high of a level: adjust it
        if starting_chapter != 0 and chapter_dict[starting_chapter] > 3:
            original_chapters = list(chapter_dict.keys())
            random.shuffle(original_chapters)
            for original_chapter in original_chapters:
                if chapter_dict[original_chapter] <= 3:
                    swap_chapter = chapter_dict[starting_chapter]
                    chapter_dict[starting_chapter] = chapter_dict[original_chapter]
                    chapter_dict[original_chapter] = swap_chapter
                    break

    elif shuffle_chapter_difficulty and plando_difficulty:
        # Force plando difficulty, then fill any remaining chapters with
        # difficulties that are not already set, if able
        if len(plando_difficulty) == 7:
            # All chapters plando'd
            chapter_dict = plando_difficulty
        else:
            # Not all chapters plando'd
            for x in plando_difficulty.values():
                if x in chapter_difficulties:
                    chapter_difficulties.remove(x)

            not_plandod_chapters = [
                x for x in range(1, 8)
                if x not in plando_difficulty.keys()
            ]

            # Check if the chapter we are starting in is not plando'd:
            # if it's not, and the plando has not already placed the
            # difficulties of 1, 2, and 3 anywhere, force one of those
            # difficulties into the starting chapter
            if (    starting_chapter != 0
                and starting_chapter not in plando_difficulty
                and any([x <= 3 for x in chapter_difficulties])
            ):
                starting_difficulty = random.choice([
                    x for x in chapter_difficulties
                    if x <= 3
                ])
                chapter_dict[starting_chapter] = starting_difficulty
                chapter_difficulties.remove(starting_difficulty)
                not_plandod_chapters.remove(starting_chapter)

            random.shuffle(chapter_difficulties)

            while not_plandod_chapters and chapter_difficulties:
                chapter_dict[not_plandod_chapters.pop()] = chapter_difficulties.pop()

            chapter_dict.update(plando_difficulty)

        # Chapter 8 is never shuffled
        chapter_dict[8] = 8

    return chapter_dict


def _random_enemy_promotions(
    all_enemy_stats: dict,
    shuffle_chapter_difficulty: bool
) -> None:
    """
    Randomly choose enemies to be promoted, that is to be scaled up by one
    chapter difficulty.
    """
    for actor_name in all_enemy_stats:
        if not shuffle_chapter_difficulty:
            all_enemy_stats[actor_name]["Promoted"] = False
        else:
            # Random chance for enemy promotion: 20%
            #all_enemy_stats[actor_name]["Promoted"] = (random.random() <= 0.2)
            all_enemy_stats[actor_name]["Promoted"] = False

    for actor_name in all_enemy_stats:
        if all_enemy_stats[actor_name]["Promoted"]:
            print(f"Promoted {actor_name}")
