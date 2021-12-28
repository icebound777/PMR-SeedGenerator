"""
This module modifies the music in the ROM by pairing different song ids and
song variation ids to different songs and variations.
DBKey: A700(u8 song)(u8 variation)
DBValue: (s16 song)(s16 variation)
I.e. to map song 4, variation 1 to song F, variation 2 we'd have
A7000401 : 000F0002
"""

def get_turned_off_music():
    """
    Returns a list of tuples where the first value holds the dbkey for a song
    and the second value is -1, which mutes the song.
    """
    music_list = []

    for song_id in range(0, 0x97):
        db_key = 0xA7000000 + (song_id << 8)
        music_list.append((int(db_key), 0xFFFF0000))

    return music_list
