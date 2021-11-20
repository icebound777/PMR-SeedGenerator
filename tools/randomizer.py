"""General setup and supportive functionalities for the randomizer."""
import shutil
import sys
import hashlib
import time
import yaml
from yaml.loader import SafeLoader

from enums import create_enums
from table import Table
from parse import gather_keys, gather_values

from logic import place_items

from db.option          import create_options
from db.item            import create_items
from db.node            import create_nodes
from db.actor_attribute import create_actor_attributes
from db.quiz            import create_quizzes


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
        sys.exit()


def set_cheap_shopitems(placed_items):
    """[in-dev] Sets the buying price of all items to 1."""
    for node in placed_items:
        node.current_item.base_price = 1


def write_itemdata_to_rom(placed_items, seed=int(hashlib.md5().hexdigest()[0:8], 16), edit_seed="0x0123456789ABCDEF"):
    """
    Generates key:value pairs of locations and items from randomized item set
    and writes these pairs to the ROM. Also logs the pairs to a file.
    """
    # Create the ROM table
    rom_table = Table()
    rom_table.create()

    # Create a sorted list of key:value pairs to be written into the ROM
    table_data = rom_table.generate_pairs(items=placed_items)

    # Update table info with variable data
    rom_table.info["num_entries"] = len(table_data)
    rom_table.info["seed"] = seed

    # Write data to log file
    with open("./debug/log.txt", "w", encoding="utf-8") as log:
        log.write("OPTIONS:\n\n")
        log.write(f"Seed: 0x{seed:0X} \"{edit_seed}\"\n")
        for name,data in rom_table["Options"].items():
            log.write(f"{name:20}: {data['value']}\n")
        log.write("\n")

    # Modify the table data in the ROM
    with open("../out/PM64.z64", "r+b") as file:
        # Write the header
        file.seek(rom_table.info["address"])
        file.write(rom_table.info["magic_value"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["header_size"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["num_entries"].to_bytes(4, byteorder="big"))
        file.write(rom_table.info["seed"].to_bytes(4, byteorder="big"))

        # Write table data and generate log file
        file.seek(rom_table.info["address"] + rom_table.info["header_size"])
        with open("./debug/log.txt", "a", encoding="utf-8") as log:
            #log.write("ITEM CHANGES:\n\n")

            for _,pair in enumerate(table_data):
                key_int = pair["key"].to_bytes(4, byteorder="big")
                value_int = pair["value"].to_bytes(4, byteorder="big")
                file.write(key_int)
                file.write(value_int)

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


def write_spoiler_log(placed_items):
    """Outputs a log file listing the final locations of all items after randomization."""
    sorted_by_key =  sorted(placed_items,  key=lambda node: node.key_name_item)
    sorted_by_map =  sorted(sorted_by_key, key=lambda node: node.map_area.map_id)
    sorted_by_area = sorted(sorted_by_map, key=lambda node: node.map_area.area_id)
    with open("./debug/item_placement.txt", "w",encoding='utf-8') as file:
        for node in sorted_by_area:
            file.write(f"[{node.map_area.name}] ({node.map_area.verbose_name}): "
                       f"{node.key_name_item} - {node.vanilla_item.item_name} -> "
                       f"{node.current_item.item_name}\n")

def main_randomizer():
    timer_start = time.perf_counter()

    # Load settings
    rando_settings = {}
    with open("default_settings.yaml", "r", encoding="utf-8") as file:
        rando_settings = yaml.load(file, Loader=SafeLoader)

    #
    init_randomizer(rebuild_database=False)

    # Item Placement
    placed_items = []
    for _, _ in place_items(item_placement=placed_items,
                            algorithm=rando_settings.get("PlacementAlgorithm"),
                            do_shuffle_items=rando_settings.get("ShuffleItems"),
                            do_randomize_coins=rando_settings.get("IncludeCoins"),
                            do_randomize_shops=rando_settings.get("IncludeShops"),
                            do_randomize_panels=rando_settings.get("IncludePanels"),
                            starting_map_id=rando_settings.get("StartingMap"),
                            startwith_bluehouse_open=rando_settings.get("BlueHouseOpen")):
        pass

    # Make everything inexpensive
    set_cheap_shopitems(placed_items)

    # Write item data to ROM
    write_itemdata_to_rom(placed_items)

    # Write sorted spoiler log
    write_spoiler_log(placed_items)
    
    timer_end = time.perf_counter()
    print(f'Seed generated in {round(timer_end - timer_start, 2)}s')


if __name__ == "__main__":
    main_randomizer()
