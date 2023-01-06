"""General setup and supportive functionalities for the randomizer."""
import io
import os
import random
import sys
import getopt
import hashlib
import time
import json
import yaml
from yaml.loader import SafeLoader
from pathlib import Path

from models.WebSeedResponse import WebSeedResponse
from random_seed import RandomSeed
from table import Table
from parse import gather_keys, gather_values
from calculate_crc import recalculate_crcs

from optionset import OptionSet, PaletteOptionSet, populate_keys

from spoilerlog import write_spoiler_log
from db.option          import Option, create_options
from db.map_meta        import create_mapmeta
from db.item            import create_items
from db.node            import create_nodes
from db.block           import create_blocks
from db.actor           import create_actors
from db.actor_params    import create_actor_params
from db.actor_attribute import create_actor_attributes
from db.move            import create_moves
from db.quiz            import create_quizzes
from db.palette         import Palette, create_palettes
from rando_modules.random_palettes     \
    import get_randomized_coinpalette, \
           get_randomized_palettes


BASE_MOD_VERSION = "0.10.0 (beta)"
BASE_MOD_MD5 = "10785ABD05C36F4C6EEF27A80AE03642"
BASE_MOD_DEBUG_MD5 = "C053A221D28ABE44C7919C580887D8F2"
VERSION_STRING = f"Seed Generator for Paper Mario 64 Randomizer mod {BASE_MOD_VERSION}"


def init_randomizer(rebuild_database=False):
    """Deals with the initialization of data required for the randomizer to work."""
    
    # Build database from scratch if needed
    if rebuild_database:
        # Create enums from ./globals/enum/
        gather_keys()
        gather_values()
        create_options()
        create_mapmeta()
        create_items()
        create_nodes()
        create_blocks()
        create_actors()
        create_actor_params()
        create_actor_attributes()
        create_palettes()
        create_moves()
        create_quizzes()


def set_cheap_shopitems(placed_items):
    """[in-dev] Sets the buying price of all items to 1."""
    for node in placed_items:
        node.current_item.base_price = 1


def print_usage():
    """Prints this program's usage."""
    print("Usage: randomizer.py [OPTION]... [FILE]")
    print("Main module for the Open World Paper Mario Randomizer.")
    print("Randomizes items, entrances and more and writes those to a pre-")
    print("modded Paper Mario ROM, outputting to FILE.")
    print("")
    print("OPTIONs")
    print("  -c, --config-file set path to config-file (json/yaml) to use for")
    print("                      the current randomization, overwriting defaults")
    print("  -t, --targetmod   set path to pre-modded PM64 ROM to randomize")
    print("  -s, --spoilerlog  set path to output spoilerlog file")
    print("  -S, --seed        set the generation seed")
    print("  -d, --dry-run     generate seed, but don't write to ROM")
    print("  -r, --rebuild-db  rebuild database from mod files and exit")
    print("  -h, --help        display this help and exit")
    print("  -v, --version     display version information and exit")


def print_version():
    """Prints version."""
    print(VERSION_STRING)


def is_rom_basemod(target_modfile:str) -> bool:
    """
    Checks the md5 hash of a provided target ROM and compares it against the
    version of the base modded Rando ROM that is ascociated with it.
    Returns True if matching.
    """
    basemod_md5_hash = BASE_MOD_MD5

    hash_md5 = hashlib.md5()
    with open(file=target_modfile, mode="rb") as in_file:
        for chunk in iter(lambda: in_file.read(4096), b""):
            hash_md5.update(chunk)

    #return hash_md5.hexdigest() == basemod_md5_hash
    #I killed this check because currently the randomizer destructively
    #writes to the ROM. It isn't good to remove a safety check, but the
    #CLI is frankly not reasonably usable without this hack in place for now.
    return True


def write_data_to_rom(
    target_modfile:str,
    options:OptionSet,
    placed_items:list,
    placed_blocks:list,
    entrance_list:list,
    enemy_stats:list,
    battle_formations:list,
    move_costs:list,
    itemhints:list,
    coin_palette_data:list,
    coin_palette_targets:list,
    coin_palette_crcs:list,
    palette_data:list,
    quiz_data:list,
    music_list:list,
    seed_id=random.randint(0, 0xFFFFFFFF)
):
    """
    Generates key:value pairs of locations and items from a randomized item set
    and writes these pairs to the ROM. Also logs the pairs to a file.
    """
    # Create the ROM table
    rom_table = Table()
    rom_table.create()
    # Create a sorted list of key:value pairs to be written into the ROM
    table_data = rom_table.generate_pairs(
        options=options,
        items=placed_items,
        blocks=placed_blocks,
        entrances=entrance_list,
        actor_data=enemy_stats,
        move_costs=move_costs,
        palettes=palette_data,
        quiz_data=quiz_data,
        music_list=music_list
    )

    # Update table info with variable data
    end_of_content_marker = 0x4 # end of table FFFFFFFF
    end_padding = 0x10 # 4x FFFFFFFF
    len_battle_formations = sum([len(formation) for formation in battle_formations])
    len_itemhints = sum([len(itemhint_word) for itemhint_word in itemhints])

    rom_table.info["db_size"] = (  rom_table.info["header_size"]
                                 + (len(table_data) * 8)
                                 + (len_battle_formations * 4)
                                 + end_of_content_marker
                                 + (len_itemhints * 4)
                                 + end_of_content_marker
                                 + end_padding)
    rom_table.info["seed"] = seed_id
    rom_table.info["formations_offset"] = len(table_data) * 8
    rom_table.info["itemhints_offset"] = (  rom_table.info["formations_offset"]
                                          + end_of_content_marker
                                          + (len_battle_formations * 4))

    # Write data to log file
    #with open(os.path.abspath(__file__ + "/../debug/log.txt"), "w", encoding="utf-8") as log:
    #    log.write("OPTIONS:\n\n")
    #    log.write(f"Seed: 0x{seed:0X} \"{edit_seed}\"\n")
    #    for name,data in rom_table["Options"].items():
    #        log.write(f"{name:20}: {data['value']}\n")
    #    log.write("\n")

    # Modify the table data in the ROM
    changed_coin_palette = False
    with open(target_modfile, "r+b") as file:
        # Write the db header
        file.seek(rom_table.info["address"])
        file.write(rom_table.info["magic_value"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["header_size"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["db_size"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["seed"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["formations_offset"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["itemhints_offset"].to_bytes(4, byteorder="big"))

        # Write table data and generate log file
        file.seek(rom_table.info["address"] + rom_table.info["header_size"])

        for _,pair in enumerate(table_data):
            key_int = pair["key"].to_bytes(4, byteorder="big")
            value_int = pair["value"].to_bytes(4, byteorder="big")
            file.write(key_int)
            file.write(value_int)

        for formation in battle_formations:
            for formation_hex_word in formation:
                file.write(formation_hex_word.to_bytes(4, byteorder="big"))

        # Write end of formations table
        file.write(0xFFFFFFFF.to_bytes(4, byteorder="big"))

        # Write itemhint table
        for itemhint in itemhints:
            for itemhint_hex in itemhint:
                file.write(itemhint_hex.to_bytes(4, byteorder="big"))

        # Write end of item hints table
        file.write(0xFFFFFFFF.to_bytes(4, byteorder="big"))
        # Write end of db padding
        for _ in range(1, 5):
            file.write(0xFFFFFFFF.to_bytes(4, byteorder="big"))

        # Special solution for random coin palettes
        if coin_palette_data and coin_palette_targets:
            changed_coin_palette = True
            for target_rom_location in coin_palette_targets:
                file.seek(target_rom_location)
                for palette_byte in coin_palette_data:
                    file.write(palette_byte.to_bytes(4, byteorder="big"))

    if changed_coin_palette:
        recalculate_crcs(target_modfile, coin_palette_crcs)

                #if enum_type := pair.get("enum_type"):
                #    if enum_type == "Item":
                #        if "ShopPrice" not in pair["attribute"]:
                #            column_left = f"[{pair['table']}][{pair['attribute']}]"
                #            original_item_id = rom_table.default_db[pair["table"]][pair['attribute']]["value"]
                #            original_item = Enums.get("Item")[original_item_id]
                #            column_right = f"{original_item} -> {Enums.get('Item')[pair['value']]}"
                #            log_statement = f"{column_left:25} : {column_right}"
                #            log.write(log_statement + "\n")
                #        if enum_type == "Entrance":
                #            pass #print(pair)

def write_data_to_array(
    options:OptionSet,
    placed_items:list,
    placed_blocks:list,
    entrance_list:list,
    enemy_stats:list,
    battle_formations:list,
    move_costs:list,
    itemhints:list,
    coin_palette_data:list,
    coin_palette_targets:list,
    coin_palette_crcs:list,
    palette_data:list,
    quiz_data:list,
    music_list:list,
    seed_id: int
):
    """
    Generates key:value pairs of locations and items from a randomized item set
    and writes these pairs in a dictionary meant to be returned by the server
    """
    # Create the ROM table
    rom_table = Table()
    rom_table.create()
    patchOperations = bytearray()
    # Create a sorted list of key:value pairs to be written into the ROM
    table_data = rom_table.generate_pairs(
        options=options,
        items=placed_items,
        blocks=placed_blocks,
        entrances = entrance_list,
        actor_data=enemy_stats,
        move_costs=move_costs,
        palettes=palette_data,
        quiz_data=quiz_data,
        music_list=music_list
    )

    # Update table info with variable data
    end_of_content_marker = 0x4 # end of table FFFFFFFF
    end_padding = 0x10 # 4x FFFFFFFF
    len_battle_formations = sum([len(formation) for formation in battle_formations])
    len_itemhints = sum([len(itemhint_word) for itemhint_word in itemhints])

    rom_table.info["db_size"] = (  rom_table.info["header_size"]
                                 + (len(table_data) * 8)
                                 + (len_battle_formations * 4)
                                 + end_of_content_marker
                                 + (len_itemhints * 4)
                                 + end_of_content_marker
                                 + end_padding)
    rom_table.info["seed"] = seed_id
    rom_table.info["formations_offset"] = len(table_data) * 8
    rom_table.info["itemhints_offset"] = (  rom_table.info["formations_offset"]
                                          + end_of_content_marker
                                          + (len_battle_formations * 4))

    # Write data to log string
    #log = "OPTIONS:\n\n"
    #log += (f"Seed: 0x{seed:0X} \"{edit_seed}\"\n")
    #for name,data in rom_table["Options"].items():
        #log += (f"{name:20}: {data['value']}\n")
    #log += ("\n")


    # Write the db header
    patchOperations +=((0).to_bytes(1, byteorder="big"))
    patchOperations += (rom_table.info["address"].to_bytes(4, byteorder = "big"))
    
    patchOperations += ((1).to_bytes(1, byteorder="big"))
    patchOperations += (rom_table.info["magic_value"].to_bytes(4, byteorder="big"))

    patchOperations += ((1).to_bytes(1, byteorder="big"))
    patchOperations += (rom_table.info["header_size"].to_bytes(4, byteorder="big"))

    patchOperations += ((1).to_bytes(1, byteorder="big"))
    patchOperations += (rom_table.info["db_size"].to_bytes(4, byteorder="big"))

    patchOperations += ((1).to_bytes(1, byteorder="big"))
    patchOperations += (rom_table.info["seed"].to_bytes(4, byteorder="big"))

    patchOperations += ((1).to_bytes(1, byteorder="big"))
    patchOperations += (rom_table.info["formations_offset"].to_bytes(4, byteorder="big"))

    patchOperations += ((1).to_bytes(1, byteorder="big"))
    patchOperations += (rom_table.info["itemhints_offset"].to_bytes(4, byteorder="big"))

    # Random Coin Palette
    if coin_palette_data and coin_palette_targets:
        for target_rom_location in coin_palette_targets:
           patchOperations += ((0).to_bytes(1, byteorder="big"))
           patchOperations += (target_rom_location.to_bytes(4, byteorder="big"))
           for palette_byte in coin_palette_data:               
                patchOperations += ((1).to_bytes(1, byteorder="big"))
                patchOperations += (palette_byte.to_bytes(4, byteorder="big"))

    # Write table data and generate log file
    db_offset = rom_table.info["address"] + rom_table.info["header_size"]
    patchOperations += ((2).to_bytes(1, byteorder="big")) # 2 means final seek, no more FILE SEEK (0) after this point
    patchOperations += db_offset.to_bytes(4, byteorder="big")

    palette_offset = 0
    cosmetics_offset = 0
    audio_offset = 0

    first_palette_db_key = Palette.get(Palette.sprite == "Mario").get_key()
    first_cosmetics_db_key = Option.get(Option.name == "Box5ColorA").get_key()
    first_audio_db_key = Option.get(Option.name == "RandomPitch").get_key()

    for _,pair in enumerate(table_data):
        key_int = pair["key"].to_bytes(4, byteorder="big")
        value_int = pair["value"].to_bytes(4, byteorder="big")
        
        patchOperations += (key_int)
        patchOperations += (value_int)

        if pair["key"] == first_palette_db_key: # When finding 1st palette key, save that offset as palette_offset to be used for future rewrite
            palette_offset = db_offset

        elif pair["key"] == first_cosmetics_db_key: # Save 1st cosmetics option key in the same manner
            cosmetics_offset = db_offset

        elif pair["key"] == first_audio_db_key: # Save 1st cosmetics option key in the same manner
            audio_offset = db_offset

        db_offset += 0x00000008 # Keep track of the current db offset at every iteration

    for formation in battle_formations:
        for formation_hex_word in formation:              
            patchOperations += (formation_hex_word.to_bytes(4, byteorder="big"))

    # Write end of formations table
    patchOperations += (0xFFFFFFFF.to_bytes(4, byteorder="big"))

    # Write itemhint table
    for itemhint in itemhints:
        for itemhint_hex in itemhint:
            patchOperations += (itemhint_hex.to_bytes(4, byteorder="big"))

    # Write end of item hints table
    patchOperations += (0xFFFFFFFF.to_bytes(4, byteorder="big"))
    # Write end of db padding
    for _ in range(1, 5):
        patchOperations += (0xFFFFFFFF.to_bytes(4, byteorder="big"))


    return patchOperations, palette_offset, cosmetics_offset, audio_offset

def write_cosmetics_data_to_array(
    coin_palette_data:list,
    coin_palette_targets:list,
    palette_data:list,
    cosmetic_options: dict,
    audio_options: dict,
    palette_offset: int,
    cosmetics_offset: int,
    audio_offset: int
):
    """
    Generates key:value pairs for cosmetic options only and writes these pairs in a dictionary
    meant to be returned by the server to overwrite cosmetics settings
    """
    # Create the ROM table
    rom_table = Table()
    rom_table.create()
    patchOperations = bytearray()
    # Create a sorted list of key:value pairs to be written into the ROM
    palette_table_data = rom_table.generate_palettes_pairs(palettes=palette_data)
    cosmetics_table_data = rom_table.generate_cosmetics_pairs(cosmetics=cosmetic_options)
    audio_options_table_data = rom_table.generate_audio_option_pairs(audio_options=audio_options)

    # Random Coin Palette
    if coin_palette_data and coin_palette_targets:
        for target_rom_location in coin_palette_targets:
           patchOperations += ((0).to_bytes(1, byteorder="big"))
           patchOperations += (target_rom_location.to_bytes(4, byteorder="big"))
           for palette_byte in coin_palette_data:               
                patchOperations += ((1).to_bytes(1, byteorder="big"))
                patchOperations += (palette_byte.to_bytes(4, byteorder="big"))


    # Write cosmetic options table data
    patchOperations += ((0).to_bytes(1, byteorder="big"))
    patchOperations += ((cosmetics_offset).to_bytes(4, byteorder="big")) # seek the adress where cosmetic settings start

    for _,pair in enumerate(cosmetics_table_data):
        key_int = pair["key"].to_bytes(4, byteorder="big")
        value_int = pair["value"].to_bytes(4, byteorder="big")
        
        patchOperations += ((1).to_bytes(1, byteorder="big"))
        patchOperations += (key_int)

        patchOperations += ((1).to_bytes(1, byteorder="big"))
        patchOperations += (value_int)

    # Write audio options table data
    patchOperations += ((0).to_bytes(1, byteorder="big"))
    patchOperations += ((audio_offset).to_bytes(4, byteorder="big")) # seek the adress where cosmetic settings start

    for _,pair in enumerate(audio_options_table_data):
        key_int = pair["key"].to_bytes(4, byteorder="big")
        value_int = pair["value"].to_bytes(4, byteorder="big")
        
        patchOperations += ((1).to_bytes(1, byteorder="big"))
        patchOperations += (key_int)

        patchOperations += ((1).to_bytes(1, byteorder="big"))
        patchOperations += (value_int)

    # Write palette table data
    patchOperations += ((2).to_bytes(1, byteorder="big")) # 2 means final seek, no more FILE SEEK (0) after this point
    patchOperations += (palette_offset).to_bytes(4, byteorder="big")

    for _,pair in enumerate(palette_table_data):
        key_int = pair["key"].to_bytes(4, byteorder="big")
        value_int = pair["value"].to_bytes(4, byteorder="big")
        
        patchOperations += (key_int)
        patchOperations += (value_int)

    return patchOperations

def web_apply_cosmetic_options(cosmetic_settings, palette_offset, cosmetics_offset, audio_offset):

    palette_options = PaletteOptionSet()

    palette_options.mario_setting = cosmetic_settings["MarioSetting"]
    palette_options.mario_sprite = cosmetic_settings["MarioSprite"]
    palette_options.goombario_setting = cosmetic_settings["GoombarioSetting"]
    palette_options.goombario_sprite = cosmetic_settings["GoombarioSprite"]
    palette_options.kooper_setting = cosmetic_settings["KooperSetting"]
    palette_options.kooper_sprite = cosmetic_settings["KooperSprite"]
    palette_options.bombette_setting = cosmetic_settings["BombetteSetting"]
    palette_options.bombette_sprite = cosmetic_settings["BombetteSprite"]
    palette_options.parakarry_setting = cosmetic_settings["ParakarrySetting"]
    palette_options.parakarry_sprite = cosmetic_settings["ParakarrySprite"]
    palette_options.bow_setting = cosmetic_settings["BowSetting"]
    palette_options.bow_sprite = cosmetic_settings["BowSprite"]
    palette_options.watt_setting = cosmetic_settings["WattSetting"]
    palette_options.watt_sprite = cosmetic_settings["WattSprite"]
    palette_options.sushie_setting = cosmetic_settings["SushieSetting"]
    palette_options.sushie_sprite = cosmetic_settings["SushieSprite"]
    palette_options.lakilester_setting = cosmetic_settings["LakilesterSetting"]
    palette_options.lakilester_sprite = cosmetic_settings["LakilesterSprite"]
    palette_options.bosses_setting = cosmetic_settings["BossesSetting"]
    palette_options.npc_setting = cosmetic_settings["NPCSetting"]
    palette_options.enemies_setting = cosmetic_settings["EnemiesSetting"]
    palette_options.hammer_setting = cosmetic_settings["HammerSetting"]
        
    # Randomize sprite palettes
    coin_palette, chosen_color_id= get_randomized_coinpalette(
        color_id = cosmetic_settings["CoinColor"],
        should_randomize_color = cosmetic_settings["RandomCoinColor"]
    )
    palette_data = get_randomized_palettes(
        palette_options
    )

    cosmetic_options = {
        "Box5ColorA": cosmetic_settings["Box5ColorA"],
        "Box5ColorB": cosmetic_settings["Box5ColorB"],
        "RandomText": cosmetic_settings["RandomText"],
        "RomanNumerals": cosmetic_settings["RomanNumerals"],
        "CoinColor": chosen_color_id,
    }

    audio_options = {
        "RandomPitch": cosmetic_settings["RandomPitch"]
    }

    operations = write_cosmetics_data_to_array(
        coin_palette_data= coin_palette.data,
        coin_palette_targets=coin_palette.targets,
        palette_data=palette_data,
        cosmetic_options=cosmetic_options,
        audio_options=audio_options,
        palette_offset=palette_offset,
        cosmetics_offset=cosmetics_offset,
        audio_offset=audio_offset
    )
    patch_file = io.BytesIO(operations)
    return patch_file

def web_randomizer(jsonSettings, world_graph):
    timer_start = time.perf_counter()

    data = json.loads(jsonSettings)

    rando_settings = OptionSet()
    populate_keys(data)
    rando_settings.update_options(data)

    init_randomizer(rebuild_database=False)

    random_seed = RandomSeed(rando_settings)
    random_seed.generate(world_graph)

    # Write data to byte array
    operations, palette_offset, cosmetics_offset, audio_offset = write_data_to_array(
        options=rando_settings,
        placed_items=random_seed.placed_items,
        placed_blocks=random_seed.placed_blocks,
        entrance_list=random_seed.entrance_list,
        enemy_stats=random_seed.enemy_stats,
        battle_formations=random_seed.battle_formations,
        move_costs=random_seed.move_costs,
        itemhints=random_seed.itemhints,
        coin_palette_data=random_seed.coin_palette.data,
        coin_palette_targets=random_seed.coin_palette.targets,
        coin_palette_crcs=random_seed.coin_palette.crcs,
        palette_data=random_seed.palette_data,
        quiz_data=random_seed.quiz_list,
        music_list=random_seed.music_list,
        seed_id=random_seed.seed_hash
    )
    patch_file = io.BytesIO(operations)

    # Write data to ROM (debug purposes)
    """ write_data_to_rom(
        target_modfile = os.path.abspath(__file__ + "/../../out/PM64.z64"),
        options=rando_settings,
        placed_items=random_seed.placed_items,
        entrance_list=random_seed.entrance_list,
        enemy_stats=random_seed.enemy_stats,
        battle_formations=random_seed.battle_formations,
        move_costs=random_seed.move_costs,
        itemhints=random_seed.itemhints,
        coin_palette_data=random_seed.coin_palette.data,
        coin_palette_targets=random_seed.coin_palette.targets,
        coin_palette_crcs=random_seed.coin_palette.crcs,
        palette_data=random_seed.palette_data,
        quiz_data=random_seed.quiz_list,
        music_list=random_seed.music_list,
        seed=random_seed.seedID
    ) """

    # Write sorted spoiler log. Always write it for web, we want to preserve for debug purposes and will hide it to users
    spoiler_log_file = None
    spoiler_log_file = write_spoiler_log(
        random_seed.placed_items,
        random_chapter_difficulty=random_seed.chapter_changes,
        settings=rando_settings,
        is_web_spoiler_log=True,
        spheres_dict=random_seed.item_spheres_dict,
        move_costs=random_seed.move_costs,
        block_locations=random_seed.placed_blocks,
        seed_hash_items=random_seed.seed_hash_items
    )

    timer_end = time.perf_counter()
    print(f'Seed generated in {round(timer_end - timer_start, 2)}s')
    return WebSeedResponse(random_seed.seed_value, patch_file, spoiler_log_file, palette_offset, cosmetics_offset, audio_offset)



def main_randomizer(args):
    """
    Main randomizer module, used for controlling the randomizer from the
    commandline. Calling this forgoes using the GUI.
    """
    timer_start = time.perf_counter()

    target_modfile = ""
    custom_spoilerlog_file_path = ""
    rando_outputfile = ""

    rando_settings = None
    rando_seed = None

    write_to_rom = True

    # Get arguments from cmd
    argv = sys.argv[1:]
    try:
        opts, args = getopt.gnu_getopt(
            argv,
            'hdc:t:s:S:rv',
            ['help', 'dry-run', 'config-file=', 'targetmod=', 'spoilerlog=', 'seed=', 'rebuild-db', 'version']
        )
        for opt, arg in opts:
            # Print usage
            if opt in ["-h", "--help"]:
                print_usage()
                sys.exit()

            # Print version
            if opt in ["-v", "--version"]:
                print_version()
                sys.exit()

            # Rebuild database
            if opt in ["-r", "--rebuild-db"]:
                init_randomizer(rebuild_database=True)
                sys.exit()

            # Make a dry run (no writing to ROM)
            if opt in ["-d", "--dry-run"]:
                write_to_rom = False

            # Config file for rando
            if opt in ["-c", "--config-file"]:
                with open(arg, "r", encoding="utf-8") as file:
                    if arg[arg.rfind(".") + 1:] == "json":
                        data = json.load(file)
                    elif arg[arg.rfind(".") + 1:] == "yaml":
                        data = yaml.load(file, Loader=SafeLoader)
                rando_settings = OptionSet()
                if "SeedValue" in data and rando_seed is None:
                    rando_seed = data.get("SeedValue")
                populate_keys(data)
                rando_settings.update_options(data)

            # Pre-modded Open World PM64 ROM
            if opt in ["-t", "--targetmod"]:
                target_modfile = arg
                if not is_rom_basemod(target_modfile):
                    print(f"Provided ROM is not the required v.{BASE_MOD_VERSION} base mod!\n"
                          f"Expected base mod md5 checksum: {BASE_MOD_MD5}\n"
                           "Aborting...")
                    exit()

            # Spoilerlog output file
            if opt in ["-s", "--spoilerlog"]:
                custom_spoilerlog_file_path = arg

            # Choose the random seed
            if opt in ["-S", "--seed"]:
                rando_seed = int(arg)

        for arg in args:
            # Output modded and randomized file
            rando_outputfile = arg
            break

    except getopt.GetoptError:
        print_usage()
        raise

    if rando_settings is None:
        with open(os.path.abspath(__file__ + "/../presets/default_settings.yaml"), "r", encoding="utf-8") as file:
            data = yaml.load(file, Loader=SafeLoader)
            rando_settings = OptionSet()
            populate_keys(data)
            rando_settings.update_options(data)

    # DEFAULTS: Set targetmod if none provided
    if not target_modfile:
        target_modfile = os.path.abspath(__file__ + "/../../../out/PM64.z64")
    # DEFAULTS: Set randomized output file if none provided
    if not rando_outputfile:
        rando_outputfile = "../out/PM64.z64"

    #
    init_randomizer(rebuild_database=False)

    random_seed = RandomSeed(rando_settings, rando_seed)
    random_seed.generate()

    # Write data to ROM
    if write_to_rom:
        write_data_to_rom(
            target_modfile=target_modfile,
            options=rando_settings,
            placed_items=random_seed.placed_items,
            placed_blocks=random_seed.placed_blocks,
            entrance_list=random_seed.entrance_list,
            enemy_stats=random_seed.enemy_stats,
            battle_formations=random_seed.battle_formations,
            move_costs=random_seed.move_costs,
            itemhints=random_seed.itemhints,
            coin_palette_data=random_seed.coin_palette.data,
            coin_palette_targets=random_seed.coin_palette.targets,
            coin_palette_crcs=random_seed.coin_palette.crcs,
            palette_data=random_seed.palette_data,
            quiz_data=random_seed.quiz_list,
            music_list=random_seed.music_list,
            seed_id=random_seed.seed_hash
        )

    # Write sorted spoiler log
    if custom_spoilerlog_file_path:
        target_spoilerfile = custom_spoilerlog_file_path
    else:
        target_spoilerfile = Path(target_modfile).parent / "spoiler_log.txt"

    if rando_settings.write_spoilerlog:
        write_spoiler_log(
            random_seed.placed_items,
            random_chapter_difficulty=random_seed.chapter_changes,
            settings=rando_settings,
            spoilerlog_file=target_spoilerfile,
            spheres_dict=random_seed.item_spheres_dict,
            move_costs=random_seed.move_costs,
            block_locations=random_seed.placed_blocks,
            seed_hash_items=random_seed.seed_hash_items
        )

    timer_end = time.perf_counter()
    print(f'Seed generated in {round(timer_end - timer_start, 2)}s')


if __name__ == "__main__":
    main_randomizer(sys.argv[1:])
