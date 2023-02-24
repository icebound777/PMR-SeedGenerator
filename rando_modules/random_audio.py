"""
This module modifies the music in the ROM by pairing different song ids and
song variation ids to different songs and variations.
DBKey: A700(u8 song)(u8 variation)
DBValue: (s16 song)(s16 variation)
I.e. to map song 4, variation 1 to song F, variation 2 we'd have
A7000401 : 000F0002
"""
