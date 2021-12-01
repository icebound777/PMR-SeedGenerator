"""General setup and supportive functionalities for the randomizer."""
import shutil
import sys
import getopt
import hashlib
import time
import json
import yaml
from yaml.loader import SafeLoader

from enums import create_enums
from table import Table
from parse import gather_keys, gather_values

from logic import place_items
from spoilerlog import write_spoiler_log
from optionset import OptionSet

from db.option          import create_options
from db.item            import create_items
from db.node            import create_nodes
from db.actor_attribute import create_actor_attributes
from db.quiz            import create_quizzes


VERSION = "Randomizer 0.1 for Open World Paper Mario mod 0.1"


def init_randomizer(rebuild_database=False):
    """Deals with the initialization of data required for the randomizer to work."""
    # Create enums from ./globals/enum/
    create_enums()

    # Build database from scratch if needed
    if rebuild_database:
        work_db_name = "db.sqlite"
        default_db_name = "default_db.sqlite"

        gather_keys()
        gather_values()
        create_options()
        create_items()
        create_nodes()
        create_actor_attributes()
        create_quizzes()
        shutil.copy(work_db_name, default_db_name)


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
    print(VERSION)


def write_itemdata_to_rom(
    placed_items,
    target_modfile,
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
    table_data = rom_table.generate_pairs(items=placed_items)

    # Update table info with variable data
    rom_table.info["db_size"] = (  rom_table.info["header_size"]
                                 + (len(table_data) * 8)
                                 + 8
                                 + 16)
    rom_table.info["seed"] = seed
    rom_table.info["formations_offset"] = (  rom_table.info["header_size"]
                                           + (len(table_data) * 8))

    # Write data to log file
    with open("./debug/log.txt", "w", encoding="utf-8") as log:
        log.write("OPTIONS:\n\n")
        log.write(f"Seed: 0x{seed:0X} \"{edit_seed}\"\n")
        for name,data in rom_table["Options"].items():
            log.write(f"{name:20}: {data['value']}\n")
        log.write("\n")

    # Modify the table data in the ROM
    with open(target_modfile, "r+b") as file:
        # Write the header
        file.seek(rom_table.info["address"])
        file.write(rom_table.info["magic_value"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["header_size"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["db_size"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["seed"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["formations_offset"].to_bytes(4, byteorder="big"))

        # Write table data and generate log file
        file.seek(rom_table.info["address"] + rom_table.info["header_size"])
        with open("./debug/log.txt", "a", encoding="utf-8") as log:
            #log.write("ITEM CHANGES:\n\n")

            for _,pair in enumerate(table_data):
                key_int = pair["key"].to_bytes(4, byteorder="big")
                value_int = pair["value"].to_bytes(4, byteorder="big")
                file.write(key_int)
                file.write(value_int)
                log.write(f'{hex(pair["key"])}: {hex(pair["value"])}\n')
            
            # Write empty random formations table (for now)
            file.write(0xFFFFFFFF.to_bytes(4, byteorder="big"))

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


def main_randomizer():
    """
    Main randomizer module, used for controlling the randomizer from the
    commandline. Calling this forgoes using the GUI.
    """
    timer_start = time.perf_counter()

    rando_settings = OptionSet()
    target_modfile = ""
    spoilerlog_file_path = ""
    rando_outputfile = ""

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
                rando_settings.update_options(data)

            # Pre-modded Open World PM64 ROM
            if opt in ["-t", "--targetmod"]:
                target_modfile = arg

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

    # DEFAULTS: Load settings if none provided
    #if not rando_settings:
    #    with open("default_settings.yaml", "r", encoding="utf-8") as file:
    #        rando_settings = yaml.load(file, Loader=SafeLoader)
    # DEFAULTS: Set targetmod if none provided
    if not target_modfile:
        target_modfile = "../out/PM64.z64"
    # DEFAULTS: Set randomized output file if none provided
    if not rando_outputfile:
        rando_outputfile = "../out/PM64.z64"

    #
    init_randomizer(rebuild_database=False)

    # Item Placement
    placed_items = []
    for _, _ in place_items(item_placement=placed_items,
                            algorithm=rando_settings.placement_algorithm,
                            do_shuffle_items=rando_settings.shuffle_items.value,
                            do_randomize_coins=rando_settings.include_coins.value,
                            do_randomize_shops=rando_settings.include_shops.value,
                            do_randomize_panels=rando_settings.include_panels.value,
                            starting_map_id=rando_settings.starting_map,
                            startwith_bluehouse_open=rando_settings.bluehouse_open.value,
                            startwith_flowergate_open=rando_settings.flowergate_open.value,
                            starting_partners=rando_settings.starting_partners):
        pass

    # Make everything inexpensive
    set_cheap_shopitems(placed_items)

    # Write item data to ROM
    write_itemdata_to_rom(placed_items, target_modfile)

    # Write sorted spoiler log
    if rando_settings.write_spoilerlog:
        write_spoiler_log(
            placed_items,
            do_pretty=rando_settings.pretty_spoilerlog,
            spoilerlog_file=spoilerlog_file_path
        )

    timer_end = time.perf_counter()
    print(f'Seed generated in {round(timer_end - timer_start, 2)}s')


if __name__ == "__main__":
    main_randomizer()
