import csv
import random

from db.actor_attribute import ActorAttribute

def get_shuffled_chapter_difficulty(shuffle_chapter_difficulty):
    # Load enemy stats csv
    ENEMY_STATS_CSV_PATH = '../res/actor_params.csv'

    with open(ENEMY_STATS_CSV_PATH, mode="r", encoding="utf-8") as csv_file:
        file_lines = []
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            file_lines.append(row)

    # Reorganize loaded data into different format
    # format example:
    # "00_Goomba": {
    #     "Level": [3,5,8,10,13,15,18,20,23],
    #     "HP": [1,2,3,4,5,6,7,8],
    #     "DamageA": [1,1,2,2,3,3,4,4,5]
    #     "NativeChapter": 1
    # }
    KEY_CSV_ID = 0
    CH0_CSV_ID = 3
    NATIVE_CH_CSV_ID = 1

    all_enemy_stats = {}

    for row in file_lines[1:]:
        dbkey_name = row[KEY_CSV_ID]
        actor_name = dbkey_name[dbkey_name.index(":")+1:dbkey_name.rindex(":")]
        actor_native_chapter = row[NATIVE_CH_CSV_ID]
        actor_stat_name = dbkey_name[dbkey_name.rindex(":")+1:]
        # starting with ch0 here, so the list index equals chapter number later
        actor_stat_values = row[CH0_CSV_ID:]

        if not actor_name in all_enemy_stats:
            all_enemy_stats[actor_name] = {}
        all_enemy_stats[actor_name]["NativeChapter"] = int(actor_native_chapter)
        all_enemy_stats[actor_name][actor_stat_name] = actor_stat_values

    # Random chance for enemy promotion: 20%
    for actor_name in all_enemy_stats:
        if not shuffle_chapter_difficulty:
            all_enemy_stats[actor_name]["Promoted"] = False
        else:
            #all_enemy_stats[actor_name]["Promoted"] = (random.random() <= 0.2)
            all_enemy_stats[actor_name]["Promoted"] = False

    for actor_name in all_enemy_stats:
        if all_enemy_stats[actor_name]["Promoted"]:
            print(f"Promoted {actor_name}")

    # Randomize chapter order
    chapters_to_shuffle = [1,2,3,4,5,6,7]
    if shuffle_chapter_difficulty:
        random.shuffle(chapters_to_shuffle)

    chapter_dict = {}
    for old_chapter_number, new_chapter_number in enumerate(chapters_to_shuffle):
        chapter_dict[old_chapter_number + 1] = new_chapter_number
    # Chapter 8 is never shuffled
    chapter_dict[8] = 8

    new_enemy_stats = []

    for actor_attribute in ActorAttribute.select():
        dbkey = actor_attribute.get_key()
        actor_name = actor_attribute.actor_name
        actor_stat_name = actor_attribute.attribute
        if (
               actor_name not in all_enemy_stats
            or actor_stat_name not in all_enemy_stats[actor_name]
        ):
            # not supposed to be random, so write defaults
            value = actor_attribute.value
        else:
            native_chapter = all_enemy_stats[actor_name]["NativeChapter"]
            value = int(all_enemy_stats[actor_name][actor_stat_name][chapter_dict.get(native_chapter)])
            if all_enemy_stats[actor_name]["Promoted"]:
                value = int(all_enemy_stats[actor_name][actor_stat_name][chapter_dict.get(native_chapter) + 1])

        new_enemy_stats.append((dbkey, value))

    return new_enemy_stats, chapter_dict
