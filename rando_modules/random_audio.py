"""
This module modifies the music in the ROM by pairing different song ids and
song variation ids to different songs and variations.
DBKey: A700(u8 song)(u8 variation)
DBValue: (s16 song)(s16 variation)
I.e. to map song 4, variation 1 to song F, variation 2 we'd have
A7000401 : 000F0002
"""
from copy import deepcopy
import random

from rando_enums.enum_options import MusicRandomizationType
from rando_enums.enum_types import SongType
from metadata.song_data import SongData, song_data_array

def get_randomized_audio(
    randomize_bgm:bool,
    randomize_by:MusicRandomizationType,
    randomize_jingles:bool
) -> list:
    dbkey_base = 0xA7000000
    db_data = []

    def get_song_default_tuple(songdata:SongData) -> tuple:
        return (
            dbkey_base | (songdata.song_id << 8) | songdata.variation_id,
            0xFFFFFFFF
        )

    if randomize_bgm:
        bgms = [x for x in song_data_array if x.loops]
        categorized_lists = {}

        if randomize_by == MusicRandomizationType.MOOD:
            for songdata in bgms:
                if songdata.mood not in categorized_lists:
                    categorized_lists[songdata.mood] = []
                categorized_lists[songdata.mood].append(songdata)
        elif randomize_by == MusicRandomizationType.TYPE:
            for songdata in bgms:
                if songdata.type not in categorized_lists:
                    categorized_lists[songdata.type] = []
                categorized_lists[songdata.type].append(songdata)
        elif randomize_by == MusicRandomizationType.FULL:
            categorized_lists["all"] = bgms
        for song_category in categorized_lists:
            work_array = deepcopy(categorized_lists[song_category])
            for songdata in categorized_lists[song_category]:
                dbkey = dbkey_base | (songdata.song_id << 8) | songdata.variation_id
                random_choice = random.randint(0, len(work_array) - 1)
                new_song = work_array.pop(random_choice)
                dbvalue = (new_song.song_id << 16) | new_song.variation_id
                db_data.append((dbkey, dbvalue))
                #print(f"before {songdata.song_name}/{songdata.variation_name}, after {new_song.song_name}/{new_song.variation_name}")
                #print(f"{hex(dbkey)}/{hex(dbvalue)}")
    else:
        for songdata in song_data_array:
            if songdata.loops:
                db_data.append(get_song_default_tuple(songdata))

    if randomize_jingles:
        jingles = [x for x in song_data_array if x.type == SongType.JINGLE]
        work_array = deepcopy(jingles)
        for jingle in jingles:
            dbkey = dbkey_base | (jingle.song_id << 8) | jingle.variation_id
            random_choice = random.randint(0, len(work_array) - 1)
            new_song = work_array.pop(random_choice)
            dbvalue = (new_song.song_id << 16) | new_song.variation_id
            db_data.append((dbkey, dbvalue))
            #print(f"before {jingle.song_name}/{jingle.variation_name}, after {new_song.song_name}/{new_song.variation_name}")
            #print(f"{hex(dbkey)}/{hex(dbvalue)}")

    else:
        for songdata in [x for x in song_data_array if x.type == SongType.JINGLE]:
            db_data.append(get_song_default_tuple(songdata))

    return db_data
