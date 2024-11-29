import random

from db.actor_attribute import ActorAttribute
from db.actor_params import ActorParam

from metadata.formations_meta import bossactor_chapter_map

def get_shuffled_chapter_difficulty(
    shuffle_chapter_difficulty:bool,
    boss_chapter_map: dict[int, int], # e.g. General Guy -> chapter 1, so {4: 1}
    progressive_scaling:bool,
    starting_chapter:int
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
            if actor_name in [x for x1 in bossactor_chapter_map.values() for x in x1]:
                # is boss
                all_enemy_stats[actor_name]["NativeChapter"] = boss_chapter_map[actor_native_chapter]
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
        shuffle_chapter_difficulty,
        starting_chapter,
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
) -> dict[int, int]:
    """
    Pair chapter numbers with chapter difficulties according to given settings,
    and returns a dictionary representing these pairings.
    The values set here are of no relevance if chapter scaling is set to
    progressive.
    """
    chapter_dict: dict[int, int] = {}

    # Randomize chapter difficulties
    chapter_difficulties = [1,2,3,4,5,6,7]
    if shuffle_chapter_difficulty:
        random.shuffle(chapter_difficulties)

    # Assign difficulties to chapters
    chapter_dict = {}
    for chapter_number, new_difficulty in enumerate(chapter_difficulties):
        chapter_dict[chapter_number + 1] = new_difficulty
    # Chapter 8 is never shuffled
    chapter_dict[8] = 8

    if shuffle_chapter_difficulty:
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
