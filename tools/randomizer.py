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
from calculate_crc import recalculate_crcs

from optionset import OptionSet, populate_keys

from rando_modules.logic import place_items
from itemhints import get_itemhints
from spoilerlog import write_spoiler_log
from rando_modules.random_actor_stats import get_shuffled_chapter_difficulty
from rando_modules.random_formations import get_random_formations
from rando_modules.random_movecosts import get_randomized_moves
from rando_modules.random_palettes import get_randomized_coinpalette
from rando_modules.random_audio import get_turned_off_music

from db.option          import create_options
from db.item            import create_items
from db.node            import create_nodes
from db.actor           import create_actors
from db.actor_attribute import create_actor_attributes
from db.move            import create_moves
from db.quiz            import create_quizzes
from rando_modules.random_partners import get_rnd_starting_partners


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
        create_actors()
        create_actor_attributes()
        create_moves()
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


def write_data_to_rom(
    target_modfile:str,
    options:OptionSet,
    placed_items:list,
    enemy_stats:list,
    battle_formations:list,
    move_costs:list,
    itemhints:list,
    coin_palette_data:list,
    coin_palette_targets:list,
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
        actor_data=enemy_stats,
        move_costs=move_costs,
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
    with open("./debug/log.txt", "w", encoding="utf-8") as log:
        log.write("OPTIONS:\n\n")
        log.write(f"Seed: 0x{seed:0X} \"{edit_seed}\"\n")
        for name,data in rom_table["Options"].items():
            log.write(f"{name:20}: {data['value']}\n")
        log.write("\n")

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
        with open("./debug/log.txt", "a", encoding="utf-8") as log:
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
        recalculate_crcs(target_modfile)

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
                rando_settings = OptionSet()
                populate_keys(data)
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

    if rando_settings is None:
        rando_settings = OptionSet()

    # DEFAULTS: Set targetmod if none provided
    if not target_modfile:
        target_modfile = "../out/PM64.z64"
    # DEFAULTS: Set randomized output file if none provided
    if not rando_outputfile:
        rando_outputfile = "../out/PM64.z64"

    #
    init_randomizer(rebuild_database=False)

    # Choose random starting partners if necessary
    if rando_settings.random_partners:
        starting_partners = get_rnd_starting_partners(
            num_rnd_partners_min=rando_settings.random_partners_min,
            num_rnd_partners_max=rando_settings.random_partners_max,
            rando_settings=rando_settings
        )
    else:
        starting_partners = rando_settings.starting_partners

    # Item Placement
    placed_items = []
    for _, _ in place_items(item_placement=placed_items,
                            algorithm=rando_settings.placement_algorithm,
                            do_shuffle_items=rando_settings.shuffle_items["value"],
                            do_randomize_coins=rando_settings.include_coins["value"],
                            do_randomize_shops=rando_settings.include_shops["value"],
                            do_randomize_panels=rando_settings.include_panels["value"],
                            do_randomize_koopakoot=rando_settings.include_favors,
                            do_randomize_letterchain=rando_settings.include_letterchain,
                            do_randomize_dojo=rando_settings.include_dojo,
                            starting_map_id=rando_settings.starting_map["value"],
                            startwith_bluehouse_open=rando_settings.bluehouse_open["value"],
                            startwith_flowergate_open=rando_settings.flowergate_open["value"],
                            startwith_toybox_open=rando_settings.toybox_open["value"],
                            startwith_whale_open=rando_settings.whale_open["value"],
                            starting_partners=starting_partners,
                            speedyspin=rando_settings.always_speedyspin["value"],
                            ispy=rando_settings.always_ispy["value"],
                            peekaboo=rando_settings.always_peekaboo["value"],
                            partners_always_usable=rando_settings.partners_always_usable["value"],
                            partners_in_default_locations=rando_settings.partners_in_default_locations,
                            hidden_block_mode=rando_settings.hidden_block_mode["value"],
                            keyitems_outside_dungeon=rando_settings.keyitems_outside_dungeon):
        pass

    # Make everything inexpensive
    set_cheap_shopitems(placed_items)

    # Randomize chapter difficulty / enemy stats if needed
    enemy_stats = []
    chapter_changes = {}
    enemy_stats, chapter_changes = get_shuffled_chapter_difficulty(
        rando_settings.shuffle_chapter_difficulty
    )

    # Randomize enemy battle formations
    battle_formations = []
    if rando_settings.random_formations:
        battle_formations = get_random_formations(chapter_changes)

    # Randomize move costs (FP/BP) if needed
    move_costs = []
    if (
           rando_settings.shuffle_badges_bp
        or rando_settings.shuffle_badges_fp
        or rando_settings.shuffle_partner_fp
        or rando_settings.shuffle_starpower_sp
    ):
        move_costs = get_randomized_moves(
            rando_settings.shuffle_badges_bp,
            rando_settings.shuffle_badges_fp,
            rando_settings.shuffle_partner_fp,
            rando_settings.shuffle_starpower_sp
        )

    # Build item hint db
    itemhints = get_itemhints(
            placed_items,
            rando_settings.include_shops["value"],
            rando_settings.include_panels["value"],
            rando_settings.include_favors,
            rando_settings.include_letterchain,
            rando_settings.keyitems_outside_dungeon
        )

    # Randomize sprite palettes
    coin_palette_data = []
    coin_palette_targets = []
    if rando_settings.random_coin_palette:
        coin_palette_data, coin_palette_targets = get_randomized_coinpalette()

    # Music settings
    music_list = []
    if rando_settings.turn_off_music:
        music_list = get_turned_off_music()

    # Write data to ROM
    write_data_to_rom(
        target_modfile=target_modfile,
        options=rando_settings,
        placed_items=placed_items,
        enemy_stats=enemy_stats,
        battle_formations=battle_formations,
        move_costs=move_costs,
        itemhints=itemhints,
        coin_palette_data=coin_palette_data,
        coin_palette_targets=coin_palette_targets,
        music_list=music_list
    )

    # Write sorted spoiler log
    if rando_settings.write_spoilerlog:
        write_spoiler_log(
            placed_items,
            random_chapter_difficulty=chapter_changes,
            do_pretty=rando_settings.pretty_spoilerlog,
            spoilerlog_file=spoilerlog_file_path
        )

    timer_end = time.perf_counter()
    print(f'Seed generated in {round(timer_end - timer_start, 2)}s')


if __name__ == "__main__":
    main_randomizer()
