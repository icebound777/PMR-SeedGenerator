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
        