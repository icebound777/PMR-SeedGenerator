import random

from models.CoinPalette import CoinPalette


"""Module for modifying sprite palettes"""

def get_randomized_coinpalette():
    """
    Choose and return a random color palette for coin sprites, and all locations
    in ROM where the palette needs to be written to.
    We do it this way, because
    "swapping these coin palettes at runtime is pretty ugly" -clover
    """

    target_rom_locations = [
        0x09A030,
        0x09A0D0,
        0x09A170,
        0x09A210,
        0x09A2B0,
        0x09A350,
        0x09A3F0,
        0x09A490,
        0x09A530,
        0x09A5D0,
        0x1FB9F0,
        0x1FBB30,
        0x1FBC70,
        0x1FBDB0,
        0x1FBEF0,
        0x1FC030,
        0x1FC170,
        0x1FC2B0,
        0x1FC3F0,
        0x1FC530
    ]

    all_coin_palettes = {}

    # byte data for gold palette (default)
    all_coin_palettes["palette_coin_gold"] = [
        0x294AE739,
        0xEED5E64F,
        0xE5CDDD49,
        0xBC49AB87,
        0x92C76A09,
        0xC4CB8289,
        0x00010001,
        0x00010001
    ]

    # byte data for red palette
    all_coin_palettes["palette_coin_red"] = [
        0x294AE739,
        0xEB15E24F,
        0xE18DD90B,
        0xB90DA8CD,
        0x90CF610F,
        0xC14D810F,
        0x00010001,
        0x00010001
    ]

    # byte data for blue palette
    all_coin_palettes["palette_coin_blue"] = [
        0x294AE739,
        0x653F4C7D,
        0x43BD32FB,
        0x327121AD,
        0x21252119,
        0x3AF3215D,
        0x00010001,
        0x00010001
    ]

    # byte data for purple palette
    all_coin_palettes["palette_coin_purple"] = [
        0x294AE739,
        0xCC75C2F5,
        0xAA739933,
        0x792B60E7,
        0x50E138D7,
        0x916D491D,
        0x00010001,
        0x00010001
    ]

    # byte data for silver palette
    all_coin_palettes["palette_coin_silver"] = [
        0x294AE739,
        0xC5F1B5AF,
        0xA52B9CA9,
        0x7BA3631B,
        0x5257294B,
        0x94654211,
        0x00010001,
        0x00010001
    ]

    all_coin_palette_crcs = {
        "palette_coin_gold": [
            0xD4C3F881,
            0xCB3B5A00
        ],
        "palette_coin_red": [
            0x2BCD223A,
            0x3CC7D7D5
        ],
        "palette_coin_blue": [
            0xEE094F68,
            0x421628A3
        ],
        "palette_coin_purple": [
            0xB99EDAC8,
            0x7E0C334A
        ],
        "palette_coin_silver": [
            0x82A4AB59,
            0xBF600802
        ]
    }

    # Choose random coin palette
    coin_palette_keys = [palette for palette in all_coin_palettes.keys()]
    random_palette = random.choice(coin_palette_keys)
    print(random_palette)

    return CoinPalette(all_coin_palettes.get(random_palette), \
           target_rom_locations, \
           None)
