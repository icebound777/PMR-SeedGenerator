"""Module for modifying sprite palettes"""
import random

from models.CoinPalette import CoinPalette
from db.palette import Palette

from optionset import PaletteOptionSet
from metadata.palettes_meta import \
    mario_n_partner_sprite_names, \
    boss_sprite_names, \
    enemy_sprite_names



def get_randomized_coinpalette(color_id:int, should_randomize_color:bool):
    """
    Choose and return a color palette for coin sprites in accordance to chosen
    settings, as well as all locations in ROM where the palette needs to be
    written to.
    We do it this way, because
    "swapping these coin palettes at runtime is pretty ugly" (-clover)
    """
    COIN_COLOR_GOLD   = 0
    COIN_COLOR_RED    = 1
    COIN_COLOR_BLUE   = 2
    COIN_COLOR_PURPLE = 3
    COIN_COLOR_SILVER = 4

    # byte data for gold palette (default)
    palette_coin_gold = [
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
    palette_coin_red = [
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
    palette_coin_blue = [
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
    palette_coin_purple = [
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
    palette_coin_silver = [
        0x294AE739,
        0xC5F1B5AF,
        0xA52B9CA9,
        0x7BA3631B,
        0x5257294B,
        0x94654211,
        0x00010001,
        0x00010001
    ]

    coin_color_palettes = {
        COIN_COLOR_GOLD  : palette_coin_gold,
        COIN_COLOR_RED   : palette_coin_red,
        COIN_COLOR_BLUE  : palette_coin_blue,
        COIN_COLOR_PURPLE: palette_coin_purple,
        COIN_COLOR_SILVER: palette_coin_silver,
    }

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

    # temp. unused
    all_coin_palette_crcs = {
        COIN_COLOR_GOLD: [
            0xD4C3F881,
            0xCB3B5A00
        ],
        COIN_COLOR_RED: [
            0x2BCD223A,
            0x3CC7D7D5
        ],
        COIN_COLOR_BLUE: [
            0xEE094F68,
            0x421628A3
        ],
        COIN_COLOR_PURPLE: [
            0xB99EDAC8,
            0x7E0C334A
        ],
        COIN_COLOR_SILVER: [
            0x82A4AB59,
            0xBF600802
        ]
    }

    if should_randomize_color:
        # Choose random coin palette, ignoring given color id
        coin_color_keys = [color_id for color_id in coin_color_palettes.keys()]
        chosen_color_id = random.choice(coin_color_keys)
    else:
        chosen_color_id = color_id

    return CoinPalette(
        coin_color_palettes.get(chosen_color_id),
        target_rom_locations,
        None
    ), \
    chosen_color_id


def get_randomized_palettes(palette_settings:PaletteOptionSet) -> list:
    DEFAULT_PALETTE = 0
    SELECT_PALETTE = 1
    RANDOM_PICK = 2
    RANDOM_NOT_VANILLA = 3
    ALWAYS_RANDOM = 4
    PALETTEVALUE_ALWAYS_RANDOM = 0xFFFFFFFF

    palettes_data = []
    all_palettes = []
    all_palettes.append(("Mario", palette_settings.mario_setting, palette_settings.mario_sprite))
    all_palettes.append(("01_0_Goombario", palette_settings.goombario_setting, palette_settings.goombario_sprite))
    all_palettes.append(("02_0_Kooper", palette_settings.kooper_setting, palette_settings.kooper_sprite))
    all_palettes.append(("03_0_Bombette", palette_settings.bombette_setting, palette_settings.bombette_sprite))
    all_palettes.append(("04_0_Parakarry", palette_settings.parakarry_setting, palette_settings.parakarry_sprite))
    all_palettes.append(("05_0_Bow", palette_settings.bow_setting, palette_settings.bow_sprite))
    all_palettes.append(("06_0_Watt", palette_settings.watt_setting, palette_settings.watt_sprite))
    all_palettes.append(("07_0_Sushie", palette_settings.sushie_setting, palette_settings.sushie_sprite))
    #all_palettes.append(("08_0_Lakilester", palette_settings.lakilester_setting, palette_settings.lakilester_sprite))

    # Selectable palettes
    for palette_tuple in all_palettes:
        cur_sprite_name = palette_tuple[0]
        cur_setting = palette_tuple[1]
        cur_sprite = palette_tuple[2]
        palette_info = Palette.get(Palette.sprite == cur_sprite_name)
        palette_count = palette_info.palette_count

        if (cur_setting == SELECT_PALETTE
        and ((    cur_sprite_name == "Mario" # Player sprite special case, see *
              and 0 <= cur_sprite < palette_count)
          or (    cur_sprite_name != "Mario"
              and 0 <= cur_sprite <= palette_count))
        ):
            chosen_palette = cur_sprite
        elif cur_setting == RANDOM_PICK or cur_setting == RANDOM_NOT_VANILLA:
            if cur_sprite_name == "Mario":
                # Player sprite special case, see *
                chosen_palette = random.randrange(abs(RANDOM_NOT_VANILLA - cur_setting - 1), palette_count)
            else:
                chosen_palette = random.randrange(abs(RANDOM_NOT_VANILLA - cur_setting - 1), palette_count + 1)
        elif cur_setting == ALWAYS_RANDOM:
            chosen_palette = PALETTEVALUE_ALWAYS_RANDOM
        else:
            chosen_palette = DEFAULT_PALETTE

        palettes_data.append((palette_info.dbkey, chosen_palette))

    # Bosses, enemies and general NPC palettes
    for palette_info in Palette.select():
        if palette_info.sprite in mario_n_partner_sprite_names:
            continue

        if palette_info.sprite in boss_sprite_names:
            if palette_settings.bosses_setting == RANDOM_PICK or palette_settings.bosses_setting == RANDOM_NOT_VANILLA:
                palette_count = palette_info.palette_count
                chosen_palette = random.randrange(abs(RANDOM_NOT_VANILLA - palette_settings.bosses_setting - 1), palette_count + 1)
            elif palette_settings.bosses_setting == ALWAYS_RANDOM:
                chosen_palette = PALETTEVALUE_ALWAYS_RANDOM
            else:
                chosen_palette = DEFAULT_PALETTE
            palettes_data.append((palette_info.dbkey, chosen_palette))
        elif palette_info.sprite in enemy_sprite_names:
            if palette_settings.enemies_setting == RANDOM_PICK or palette_settings.enemies_setting == RANDOM_NOT_VANILLA:
                palette_count = palette_info.palette_count
                chosen_palette = random.randrange(abs(RANDOM_NOT_VANILLA - palette_settings.enemies_setting - 1), palette_count + 1)
            elif palette_settings.enemies_setting == ALWAYS_RANDOM:
                chosen_palette = PALETTEVALUE_ALWAYS_RANDOM
            else:
                chosen_palette = DEFAULT_PALETTE
            palettes_data.append((palette_info.dbkey, chosen_palette))
        else:
            if palette_settings.npc_setting == RANDOM_PICK or palette_settings.npc_setting == RANDOM_NOT_VANILLA:
                palette_count = palette_info.palette_count
                if palette_info.sprite == "Peach":
                    # Player sprite special case, see *
                    chosen_palette = random.randrange(abs(RANDOM_NOT_VANILLA - palette_settings.npc_setting - 1), palette_count)
                else:
                    chosen_palette = random.randrange(0, palette_count + 1)
            elif palette_settings.npc_setting == ALWAYS_RANDOM:
                chosen_palette = PALETTEVALUE_ALWAYS_RANDOM
            else:
                chosen_palette = DEFAULT_PALETTE
            palettes_data.append((palette_info.dbkey, chosen_palette))

    # * For technical reasons, the palette_count of player sprites, that is
    #   Mario and Peach, is off by one. This is due to our coding for player
    #   sprites making the default palette for player sprites unusable, so
    #   palette #0 (normally the default) for those is technically counted as
    #   custom palette.
    #   This is not the case for any other sprite, where a palette count of,
    #   say, 3 means 3 additional palettes in addition to the default sprite.
    #   The palette count for player sprites includes the default palette.

    return palettes_data
