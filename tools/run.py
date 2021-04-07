import re
import os
import json
import random
import configparser

from parse import get_debault_db, get_table_info, create_db, get_entrances
from enums import Enums
from starrod import sr_dump, sr_copy, sr_compile


# Read configuration data
config = configparser.ConfigParser()
config.read("./config.ini")
sr_path = config.get("starrod", "path")
seed_str = config.get("options", "seed")

# Initialize Random Seed
seed = hash(seed_str) & 0xFFFFFFFF
random.seed(seed)

# Create enums. They are tracked by the Enums class. E.g:
# item_id = Enums.get("Item")["UltraShroom"] -> 142
# item_str = Enums.get("Item")[142] --> UltraShroom
enums = {}
for name in os.listdir("../globals/enum/"):
    name = name.split(".")[0]
    Enums(f"../globals/enum/{name}.enum")

# Ensure we've dumped a ROM, copied its contents to the mod folder, and compiled it
# sr_dump(sr_path, console=False)
# sr_copy(sr_path, console=False)
# sr_compile(sr_path, console=False)

# Parse through the mod contents to obtain various data
entrances = get_entrances()
table_info = get_table_info()
default_db = get_debault_db()
db = create_db(default_db)

db["Options"]["InitialCoins"]["value"] = 999

for table in db:
    for name,data in db[table].items():
        if data["enum_type"] == "Item":
            data["value"] = Enums.get("Item").get_random(item_type="BADGE")

# Create a sorted list of key:value pairs to be written into the ROM
table_data = []
for table,data in db.items():
    for _,pair in data.items():
        table_data.append(pair)

# Update table info with variable data
table_info["num_entries"] = len(table_data)
table_info["seed"] = seed

# Write data to log file
with open("./debug/log.txt", "w") as log:
    log.write("OPTIONS:\n\n")
    log.write(f"Seed: 0x{seed:0X} \"{seed_str}\"\n")
    for name,data in db["Options"].items():
        log.write(f"{name:20}: {data['value']}\n")
    log.write("\n")

# Modify the table data in the ROM
with open("../out/PM64.z64", "r+b") as file:

    # Write the header
    file.seek(table_info["address"])
    file.write(table_info["magic_value"].to_bytes(4, byteorder="big"))
    file.write(table_info["header_size"].to_bytes(4, byteorder="big"))
    file.write(table_info["num_entries"].to_bytes(4, byteorder="big"))
    file.write(table_info["seed"].to_bytes(4, byteorder="big"))

    # Write table data and generate log file
    file.seek(table_info["address"] + table_info["header_size"])
    with open("./debug/log.txt", "a") as log:
        log.write("ITEM CHANGES:\n\n")

        for pair in table_data:
            key_int = pair["key"].to_bytes(4, byteorder="big")
            value_int = pair["value"].to_bytes(4, byteorder="big")
            file.write(key_int)
            file.write(value_int)
            if enum_type := pair.get("enum_type"):
                if enum_type == "Item":
                    column_left = f"[{pair['table']}][{pair['attribute']}]"
                    original_item_id = default_db[pair["table"]][pair['attribute']]["value"]
                    original_item = Enums.get("Item")[original_item_id]
                    column_right = f"{original_item} -> {Enums.get('Item')[pair['value']]}"
                    log_statement = f"{column_left:25} : {column_right}"
                    print(log_statement)
                    log.write(log_statement + "\n")

# Dump the data we used for randomization
with open("./debug/entrances.json", "w") as file:
    json.dump(entrances, file, indent=4)
with open("./debug/default_db.json", "w") as file:
    json.dump(default_db, file, indent=4)
with open("./debug/db.json", "w") as file:
    json.dump(db, file, indent=4)
