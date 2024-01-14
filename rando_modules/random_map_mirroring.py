"""
This module is used to set up visual mirroring of maps in a static way.
Specific Maps can be chosen to always be mirrored, always be not mirrored, or
always be 50/50 within this module.
For maps which are not set here, the chosen value for the "Mirror Mode" setting
is used as a fallback, so either "none mirrored", "all mirrored" or
"50/50 chance to mirror".
"""
import random

from db.map_area import MapArea

from metadata.area_name_mappings import area_name_id_map

def get_mirrored_map_list() -> list:
    map_list = []

    # Have one in three seeds have one fully mirrored area
    fully_mirrored_area = -1
    if random.randint(0, 2) == 1:
        area_id_name_map = {v: k for k, v in area_name_id_map.items()}
        fully_mirrored_area = random.choice(list(area_id_name_map.keys()))

    # Choose to mirror maps (fully mirrored area or 40% chance to mirror any map)
    for ingame_map in (
        MapArea
        .select(MapArea.area_id, MapArea.map_id)
    ):
        if ingame_map.area_id == fully_mirrored_area or random.randint(1, 10) <= 4:
            db_key = (0xAE << 24) + (ingame_map.area_id << 16) + (ingame_map.map_id << 8)

            map_list.append((db_key, 1))

    return map_list
