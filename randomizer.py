"""General setup and supportive functionalities for the randomizer."""
import io
import os
import shutil
import sys
import getopt
import hashlib
import time
import json
import yaml
from yaml.loader import SafeLoader

from enums import create_enums
from models.WebSeedResponse import WebSeedResponse
from random_seed import RandomSeed
from table import Table
from parse import gather_keys, gather_values
from calculate_crc import recalculate_crcs

from optionset import OptionSet, populate_keys

from spoilerlog import write_spoiler_log
from db.option          import create_options
from db.map_meta        import create_mapmeta
from db.item            import create_items
from db.node            import create_nodes
from db.actor           import create_actors
from db.actor_params    import create_actor_params
from db.actor_attribute import create_actor_attributes
from db.move            import create_moves
from db.quiz            import create_quizzes
from db.palette         import create_palettes
from rando_modules.random_partners import get_rnd_starting_partners


BASE_MOD_VERSION = "0.10.0 (beta)"
BASE_MOD_MD5 = "10785ABD05C36F4C6EEF27A80AE03642"
BASE_MOD_DEBUG_MD5 = "C053A221D28ABE44C7919C580887D8F2"
VERSION_STRING = f"Seed Generator for Paper Mario 64 Randomizer mod {BASE_MOD_VERSION}"


def init_randomizer(rebuild_database=False):
    """Deals with the initialization of data required for the randomizer to work."""
    
    # Build database from scratch if needed
    if rebuild_database:
        # Create enums from ./globals/enum/
        create_enums()
        gather_keys()
        gather_values()
        create_options()
        create_mapmeta()
        create_items()
        create_nodes()
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
    seed=int(hashlib.md5().hexdigest()[0:8], 16),
    edit_seed="0x0123456789ABCDEF"
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
    rom_table.info["seed"] = seed
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
        with open(os.path.abspath(__file__ + "/../debug/log.txt"), "a", encoding="utf-8") as log:
            #log.write("ITEM CHANGES:\n\n")

            for _,pair in enumerate(table_data):
                key_int = pair["key"].to_bytes(4, byteorder="big")
                value_int = pair["value"].to_bytes(4, byteorder="big")
                file.write(key_int)
                file.write(value_int)
                log.write(f'{hex(pair["key"])}: {hex(pair["value"])}\n')

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
    seed=int(hashlib.md5().hexdigest()[0:8], 16),
    edit_seed="0x0123456789ABCDEF"
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
    rom_table.info["seed"] = seed
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
    patchOperations += ((2).to_bytes(1, byteorder="big")) # 2 means final seek, no more FILE SEEK (0) after this point
    patchOperations += (rom_table.info["address"] + rom_table.info["header_size"]).to_bytes(4, byteorder="big")

    for _,pair in enumerate(table_data):
        key_int = pair["key"].to_bytes(4, byteorder="big")
        value_int = pair["value"].to_bytes(4, byteorder="big")
        
        patchOperations += (key_int)
        patchOperations += (value_int)

        #log += (f'{hex(pair["key"])}: {hex(pair["value"])}\n')

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


    return patchOperations


def web_randomizer(jsonSettings, world_graph):
    timer_start = time.perf_counter()

    data = json.loads(jsonSettings)

    rando_settings = OptionSet()
    populate_keys(data)
    rando_settings.update_options(data)

    init_randomizer(rebuild_database=False)

    random_seed = RandomSeed(rando_settings)
    random_seed.generate(world_graph)

    # Write data to ROM
    operations = write_data_to_array(
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
        seed=random_seed.seed_value
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
        spheres_text=random_seed.item_spheres_text
    )

    timer_end = time.perf_counter()
    print(f'Seed generated in {round(timer_end - timer_start, 2)}s')
    return WebSeedResponse(random_seed.seed_value, patch_file, spoiler_log_file)
    


def main_randomizer(args):
    """
    Main randomizer module, used for controlling the randomizer from the
    commandline. Calling this forgoes using the GUI.
    """
    timer_start = time.perf_counter()

    target_modfile = ""
    spoilerlog_file_path = ""
    rando_outputfile = ""

    rando_settings = None
    rando_seed = None

    # Get arguments from cmd
    argv = sys.argv[1:]
    try:
        opts, args = getopt.gnu_getopt(
            argv,
            'hc:t:s:rv',
            ['help', 'config-file=', 'targetmod=', 'spoilerlog=', 'rebuild-db', 'version']
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

            # Config file for rando
            if opt in ["-c", "--config-file"]:
                with open(arg, "r", encoding="utf-8") as file:
                    if arg[arg.rfind(".") + 1:] == "json":
                        data = json.load(file)
                    elif arg[arg.rfind(".") + 1:] == "yaml":
                        data = yaml.load(file, Loader=SafeLoader)
                rando_settings = OptionSet()
                if "SeedValue" in data:
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
                spoilerlog_file_path = arg

        for arg in args:
            # Output modded and randomized file
            rando_outputfile = arg
            break

    except getopt.GetoptError:
        print_usage()
        raise

    if rando_settings is None:
        with open(os.path.abspath(__file__ + "/../default_settings.yaml"), "r", encoding="utf-8") as file:
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
    write_data_to_rom(
        target_modfile=target_modfile,
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
        seed=random_seed.seed_value
    )

    # Write sorted spoiler log
    if rando_settings.write_spoilerlog:
        write_spoiler_log(
            random_seed.placed_items,
            random_chapter_difficulty=random_seed.chapter_changes,
            settings=rando_settings,
            spoilerlog_file=spoilerlog_file_path,
            spheres_text=random_seed.item_spheres_text
        )

    timer_end = time.perf_counter()
    print(f'Seed generated in {round(timer_end - timer_start, 2)}s')


if __name__ == "__main__":
    main_randomizer(sys.argv[1:])
