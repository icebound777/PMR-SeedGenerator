import random


# Work in Progress / Proof of Concept
# Probably not correct, should delete and approach differently
def shuffle_entrances(db):
    entrance_list = []
    mapping = {}
    for map_name,data in db["Entrance"].items():
        for entrance,pair in data.items():
            entrance_list.append(pair)
            mapping[pair["key"]] = {
                "value": pair["value"],
                "map_name": map_name,
                "entrance": entrance,
            }

    keys = [key for key in mapping.keys()]
    random.shuffle(keys)
    mapping = dict(zip(keys, mapping.values()))
    
    for key,data in mapping.items():
        db["Entrance"][data["map_name"]][data["entrance"]] = {
            "key": db["Entrance"][data["map_name"]][data["entrance"]]["key"],
            "value": key & 0x00FFFFFF,
            "enum_type": "Entrance",
            "map_name": data["map_name"],
            "entrance": data["entrance"],
        }

    return db

def shuffle_links(links, rom_table):
     # Swap connections between one link with the next one
    for i in range(0, len(links), 2):
        link = links[i]
        next_link = links[i+1]

        src_map1,src_exit1 = link["src"]
        src_map1 = src_map1.upper()
        dest_map1,dest_exit1 = link["dest"]
        dest_map1 = dest_map1.upper()

        src_map2,src_exit2 = next_link["src"]
        src_map2 = src_map2.upper()
        dest_map2,dest_exit2 = next_link["dest"]
        dest_map2 = dest_map2.upper()

        src_1 = rom_table["Entrance"][src_map1][src_exit1]
        dest_1 = rom_table["Entrance"][dest_map1][dest_exit1]
        src_2 = rom_table["Entrance"][src_map2][src_exit2]
        dest_2 = rom_table["Entrance"][dest_map2][dest_exit2]

        src_value1 = src_1["value"]
        dest_value1 = dest_1["value"]
        src_value2 = src_2["value"]
        dest_value2 = dest_2["value"]

        # Swapped values:
        src_1["value"] = src_value2
        dest_1["value"] = dest_value2
        src_2["value"] = src_value1
        dest_2["value"] = dest_value1

def shuffle_pipes(links, rom_table):
    pipe_links = [link for link in filter(lambda link: link["type"]=="pipe", links)]
    random.shuffle(pipe_links)

    # If we don't have an even number, trim the last one
    if len(pipe_links) % 2 != 0:
        pipe_links = pipe_links[:-1]

    shuffle_links(pipe_links, rom_table)

def shuffle_doors(links, rom_table):
    door_links = [link for link in filter(lambda link: link["type"]=="door", links)]
    random.shuffle(door_links)

    # If we don't have an even number, trim the last one
    if len(door_links) % 2 != 0:
        door_links = door_links[:-1]

    shuffle_links(door_links, rom_table)

def shuffle_paths(links, rom_table):
    path_links = [link for link in filter(lambda link: link["type"]=="ground", links)]
    random.shuffle(path_links)

    # If we don't have an even number, trim the last one
    if len(path_links) % 2 != 0:
        path_links = path_links[:-1]

    shuffle_links(path_links, rom_table)

   