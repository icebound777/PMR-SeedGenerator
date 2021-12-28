"""This module handles creation of item hints for Merluvlee to offer Mario."""
from metadata.item_source_types import item_source_types as source_types

def get_itemhints(placed_items:list):
    """
    Returns a list of item hint lists for a given list of item nodes.
    Each item hint list contains the item id and a reference word describing
    the area, map and item source type.
    """
    itemhints = []

    # The hints table is build by pairing an item id with a word describing
    # a map and a item source type (like 'given by npc' or 'in block')
    for item_node in placed_items:
        if item_node.current_item.item_type in ["KEYITEM","BADGE","STARPIECE"]:
            cur_area_id = item_node.map_area.area_id
            cur_map_id = item_node.map_area.map_id
            cur_map_name = item_node.map_area.name
            cur_keyname = item_node.key_name_item

            item_id = item_node.current_item.value
            item_source_id = source_types.get(cur_map_name).get(cur_keyname)
            print(f"{cur_map_name=}; {cur_keyname=}")

            hint_word_1 = item_id
            hint_word_2 = (
                  cur_area_id << 24
                | cur_map_id  << 16
                | item_source_id  <<  8
            )

            itemhints.append([hint_word_1, hint_word_2])

    return itemhints
