from metadata.verbose_area_names import verbose_area_names
from metadata.verbose_item_names import verbose_item_names
from metadata.verbose_item_locations import verbose_item_locations

def write_spoiler_log(
    placed_items:list,
    random_chapter_difficulty:dict=None,
    do_pretty:bool=False,
    spoilerlog_file:str=None
):
    """
    Outputs a log file listing the final locations of all items
    after randomization and randomized chapter difficulty
    """
    if not spoilerlog_file:
        spoilerlog_file = "./debug/item_placement.txt"

    sorted_by_key =  sorted(placed_items,  key=lambda node: node.key_name_item)
    sorted_by_map =  sorted(sorted_by_key, key=lambda node: node.map_area.map_id)
    sorted_by_area = sorted(sorted_by_map, key=lambda node: node.map_area.area_id)
    with open(spoilerlog_file, "w", encoding="utf-8") as file:
        # Print item locations
        if do_pretty:
            current_area_name = None
            for node in sorted_by_area:
                new_area_name = verbose_area_names.get(node.map_area.name[:3])
                if (current_area_name is None):
                    file.write(f"{new_area_name}:\n")
                elif (new_area_name != current_area_name):
                    file.write(f"\n{new_area_name}:\n")

                current_item_name = node.current_item.item_name
                map_verbose_name = node.map_area.verbose_name

                if "de Lower Jail" in map_verbose_name: # map name fix
                    map_verbose_name = "Outside Lower Jail"
                if current_item_name in verbose_item_names:
                    current_item_name = verbose_item_names.get(current_item_name)
                if (    node.map_area.name in verbose_item_locations
                    and node.key_name_item in verbose_item_locations.get(node.map_area.name)):
                    item_location = (f"{map_verbose_name} - "
                                     f"{verbose_item_locations.get(node.map_area.name).get(node.key_name_item)}")
                else:
                    item_location = f"{map_verbose_name} - {node.key_name_item}"

                file.write(f"    ({item_location}): {current_item_name}\n")
                current_area_name = verbose_area_names.get(node.map_area.name[:3])
        else:
            for node in sorted_by_area:
                file.write(f"[{node.map_area.name}] {node.key_name_item} - "
                           f"{node.current_item.item_name}\n")
        
        # Print chapter difficulties
        if random_chapter_difficulty:
            file.write("\n\nModified Chapter Difficulty:")
            for old_chapter, new_chapter in random_chapter_difficulty.items():
                file.write(f"\nChapter {old_chapter} -> Chapter {new_chapter}")