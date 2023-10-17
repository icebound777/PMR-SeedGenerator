"""
This module can modify the placement of different block types within the world.
"""

import random

from db.block import Block

from rando_enums.enum_types import BlockType


def get_block_placement(
    shuffle_blocks:bool,
    supers_are_yellow:bool
):
    block_placement = []

    if not shuffle_blocks:
        for block in Block.select():
            if block.vanilla_type == BlockType.SUPER and supers_are_yellow:
                block_placement.append((block.get_key(), BlockType.YELLOW))
            else:
                block_placement.append((block.get_key(), block.vanilla_type))
    else:
        db_keys = {}
        db_values = {}
        for block in Block.select():
            key = block.get_key()
            area_id = (key & 0xFF0000) >> 16
            if area_id not in db_keys:
                db_keys[area_id] = [key]
            else:
                db_keys[area_id].append(key)

            if block.vanilla_type == BlockType.SUPER and supers_are_yellow:
                block_type = BlockType.YELLOW
            else:
                block_type = block.vanilla_type

            if block_type not in db_values:
                db_values[block_type] = 1
            else:
                db_values[block_type] = db_values[block_type] + 1

        block_type_supers = BlockType.SUPER if not supers_are_yellow else BlockType.YELLOW

        while (block_type_supers in db_values) and db_keys:
            # Choose random area, then random db key / block spawn in that area
            area_id = random.choice(list(db_keys))
            db_key = random.choice(db_keys[area_id])
            db_keys[area_id].remove(db_key)
            if not db_keys[area_id]:
                db_keys.pop(area_id)

            block_placement.append((db_key, block_type_supers))

            db_values[block_type_supers] = db_values[block_type_supers] - 1
            if db_values[block_type_supers] == 0:
                db_values.pop(block_type_supers)

    return block_placement
