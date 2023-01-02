import io
import json

from metadata.verbose_area_names import verbose_area_names
from metadata.verbose_item_names import verbose_item_names
from metadata.verbose_item_locations import verbose_item_locations

from optionset import OptionSet

def write_spoiler_log(
    placed_items:list,
    random_chapter_difficulty:dict=None,
    settings:OptionSet=False,
    spoilerlog_file:str=None,
    is_web_spoiler_log=False,
    spheres_dict:dict = None
):
    """
    Outputs a log file listing the final locations of all items
    after randomization and randomized chapter difficulty
    """
    spoiler_dict = dict()

    sorted_by_key =  sorted(placed_items,  key=lambda node: node.key_name_item)
    sorted_by_map =  sorted(sorted_by_key, key=lambda node: node.map_area.map_id)
    sorted_by_area = sorted(sorted_by_map, key=lambda node: node.map_area.area_id)

    # Add chapter difficulties
    if settings.progressive_scaling["value"]:
        spoiler_dict["difficulty"] = "progressive"
    else:
        spoiler_dict["difficulty"] = {}
        for old_chapter, new_chapter in random_chapter_difficulty.items():
            spoiler_dict["difficulty"][f"chapter {old_chapter}"] = new_chapter

    # Add item locations
    for node in sorted_by_area:
        area_name = verbose_area_names.get(node.map_area.name[:3])
        area_name = area_name.replace("'", "")
        current_item_name = node.current_item.item_name
        map_verbose_name = (node.map_area.verbose_name)
        map_verbose_name = map_verbose_name.replace("'", "")

        # Get verbose names for item and map
        if current_item_name in verbose_item_names:
            current_item_name = verbose_item_names.get(current_item_name)

        if (    node.map_area.name in verbose_item_locations
            and node.key_name_item in verbose_item_locations.get(node.map_area.name)):
            item_location = verbose_item_locations.get(node.map_area.name).get(node.key_name_item)
        else: # fallback for not-yet-verbose'd locations
            item_location = node.key_name_item
        item_location = item_location.replace("'", "")

        if node.current_item.is_trapped():
            current_item_name = f"TRAP ({current_item_name})"

        if area_name not in spoiler_dict:
            spoiler_dict[area_name] = {}
        spoiler_dict[area_name][f"{map_verbose_name} - {item_location}"] = \
            current_item_name

    # Add sphere log
    if(spheres_dict):
        spoiler_dict["sphere_log"] = spheres_dict

    # Output spoiler log
    if is_web_spoiler_log:
        file = io.StringIO()
        json.dump(spoiler_dict, file)
        file.seek(0)
        return file
    else:
        with open(spoilerlog_file, "w", encoding="utf-8") as file:
            json.dump(spoiler_dict, file, indent=4)
