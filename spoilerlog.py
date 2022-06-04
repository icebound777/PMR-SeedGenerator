import io
import os
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
    spheres_text = None
):
    """
    Outputs a log file listing the final locations of all items
    after randomization and randomized chapter difficulty
    """
    if not spoilerlog_file and not is_web_spoiler_log:
        spoilerlog_file = os.path.abspath(__file__ + "/../debug/item_placement.txt")
        

    sorted_by_key =  sorted(placed_items,  key=lambda node: node.key_name_item)
    sorted_by_map =  sorted(sorted_by_key, key=lambda node: node.map_area.map_id)
    sorted_by_area = sorted(sorted_by_map, key=lambda node: node.map_area.area_id)

    if is_web_spoiler_log:
        file = io.StringIO()
    else:
        file = open(spoilerlog_file, "w", encoding="utf-8")
    # Print chapter difficulties
    if random_chapter_difficulty and not settings.progressive_scaling["value"]:
        file.write("Modified Chapter Difficulty:")
        for old_chapter, new_chapter in random_chapter_difficulty.items():
            file.write(f"\nChapter {old_chapter} -> Chapter {new_chapter}")
        file.write("\n\n")

    # Print item locations
    if settings.pretty_spoilerlog:
        current_area_name = None
        for node in sorted_by_area:
            new_area_name = verbose_area_names.get(node.map_area.name[:3])
            if (current_area_name is None):
                file.write(f"{new_area_name}:\n")
            elif (new_area_name != current_area_name):
                file.write(f"\n{new_area_name}:\n")

            current_item_name = node.current_item.item_name
            map_verbose_name = node.map_area.verbose_name

            if current_item_name in verbose_item_names:
                current_item_name = verbose_item_names.get(current_item_name)
            if (    node.map_area.name in verbose_item_locations
                and node.key_name_item in verbose_item_locations.get(node.map_area.name)):
                item_location = (f"{map_verbose_name} - "
                                    f"{verbose_item_locations.get(node.map_area.name).get(node.key_name_item)}")
            else:
                item_location = f"{map_verbose_name} - {node.key_name_item}"

            if node.current_item.is_trapped():
                file.write(f"    ({item_location}): TRAP ({current_item_name})\n")
            else:
                file.write(f"    ({item_location}): {current_item_name}\n")
            current_area_name = verbose_area_names.get(node.map_area.name[:3])
    else:
        for node in sorted_by_area:
            file.write(f"[{node.map_area.name}] {node.key_name_item} - "
                        f"{node.current_item.item_name}\n")
    if(spheres_text):
        file.write(f'\n{spheres_text}')

    if is_web_spoiler_log:
        file.seek(0)
        return file
