"""Module for modifying sprite palettes"""
import random

from models.CoinPalette import CoinPalette
from db.palette import Palette

from rando_enums.enum_options import RandomPalettes

from models.options.OptionSet import PaletteOptionSet
from metadata.palettes_meta import (
    mario_n_partner_sprite_names,
    boss_sprite_names,
    enemy_sprite_names,
    hammer_sprite_names,
    special_vanilla_palette_ids
)



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
    """
    Set up and return a list of dbkey/value pairs for sprite palette changes,
    according to given settings.
    Each dbkey is associated with one sprite, which in turn has at least two
    color palettes (vanilla palette + at least 1 custom one). If a sprite
    is not found in the dbkeys, then we don't provide custom palettes for it
    yet.
    Some color palettes are shared among several sprites (like for toads,
    toadettes, dryites, or shy guys).
    If a sprite is to be left vanilla, then we have to determine the vanilla
    sprite id first using a local function. The affected sprites have their
    vanilla sprite id encoded in the sprite name.
    """
    def get_vanilla_palette_id(sprite_name: str) -> int:
        if sprite_name not in special_vanilla_palette_ids:
            return 0
        else:
            return int(sprite_name[3:4])


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
    all_palettes.append(("08_0_Lakilester", palette_settings.lakilester_setting, palette_settings.lakilester_sprite))

    # Selectable palettes
    for palette_tuple in all_palettes:
        cur_sprite_name = palette_tuple[0]
        cur_setting = palette_tuple[1]
        cur_sprite = palette_tuple[2]
        palette_info = Palette.get(Palette.sprite == cur_sprite_name)
        palette_count = palette_info.palette_count

        if (    cur_setting == RandomPalettes.SELECT_PALETTE
            and 0 <= cur_sprite < palette_count
        ):
            chosen_palette = cur_sprite
        elif cur_setting == RandomPalettes.RANDOM_PICK:
            chosen_palette = random.randrange(0, palette_count)
        elif cur_setting == RandomPalettes.RANDOM_PICK_NOT_VANILLA:
            chosen_palette = random.randrange(1, palette_count)
        elif cur_setting == RandomPalettes.ALWAYS_RANDOM:
            chosen_palette = PALETTEVALUE_ALWAYS_RANDOM
        else:
            chosen_palette = get_vanilla_palette_id(palette_info.sprite)
        palettes_data.append((palette_info.dbkey, chosen_palette))

    # Bosses, enemies and general NPC palettes
    for palette_info in Palette.select():
        if palette_info.sprite in mario_n_partner_sprite_names:
            continue

        if palette_info.sprite in boss_sprite_names:
            cur_setting = palette_settings.bosses_setting
        elif palette_info.sprite in enemy_sprite_names:
            cur_setting = palette_settings.enemies_setting
        elif palette_info.sprite in hammer_sprite_names:
            cur_setting = palette_settings.hammer_setting
        else: # other NPC settings
            cur_setting = palette_settings.npc_setting

        if cur_setting == RandomPalettes.RANDOM_PICK:
            palette_count = palette_info.palette_count
            chosen_palette = random.randrange(0, palette_count)
        elif cur_setting == RandomPalettes.RANDOM_PICK_NOT_VANILLA:
            palette_count = palette_info.palette_count
            chosen_palette = random.randrange(1, palette_count)
        elif cur_setting == RandomPalettes.ALWAYS_RANDOM:
            chosen_palette = PALETTEVALUE_ALWAYS_RANDOM
        else:
            chosen_palette = get_vanilla_palette_id(palette_info.sprite)
        palettes_data.append((palette_info.dbkey, chosen_palette))

    return palettes_data
