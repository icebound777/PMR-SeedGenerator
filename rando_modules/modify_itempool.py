import math
import random

from db.item import Item
from db.node import Node

from rando_enums.enum_options import \
    IncludeFavorsMode,\
    RandomizeConsumablesMode

from metadata.item_exclusion import exclude_due_to_settings
from metadata.item_scores import item_scores
from metadata.itemlocation_special import \
    kootfavors_reward_locations, \
    kootfavors_keyitem_locations, \
    limited_by_item_areas

def get_random_consumables(n:int) -> list:
    """
    Returns a list of n items, with categories similar to vanilla distribution
    """
    weights = {
        "battle": 50,
        "heal": 45,
        "taycet": 5,
    }
    item_weights = [weights[item["type"]] for item in item_scores]

    new_items = []
    for _ in range(n):
        item, = random.choices(item_scores, item_weights) 
        new_items.append(item)

    return new_items

def balance_consumables(items, target_score):
    """
    Modifies a list of consumables until its score is close enough to the target score
    """
    new_items = items.copy()
    pool_score = sum([item["score"] for item in new_items])
   
    lowest_item = item_scores[0]
    lowest_score = lowest_item["score"]
    highest_item = item_scores[len(item_scores)-1]
    highest_score = highest_item["score"]
    score_diff = math.ceil((highest_score - lowest_score) / 2)

    # Randomly adjust the items to bring closer to target score
    while pool_score < target_score - score_diff or pool_score > target_score + score_diff:
        if pool_score < target_score:
            # Upgrade an item
            item_weights = [highest_score - item["score"] for item in new_items]
            i, = random.choices([i for i in range(len(new_items))], item_weights)
            old_item = new_items[i]
            legal_items = [item for item in item_scores if item["score"] > old_item["score"] and item["type"] == old_item["type"]]
        else:
            # Downgrade an item
            item_weights = [item["score"] - lowest_score for item in new_items]
            i, = random.choices([i for i in range(len(new_items))], item_weights)
            old_item = new_items[i]
            legal_items = [item for item in item_scores if item["score"] < old_item["score"] and item["type"] == old_item["type"]]

        # If there's no legal items to upgrade/downgrade to, try again
        if len(legal_items) == 0:
            continue

        new_item = random.choice(legal_items)
        pool_score += new_item["score"] - old_item["score"]
        new_items[i] = new_item

    return new_items

def get_randomized_itempool(itempool:list, consumable_mode:int, scarcity:int) -> list:
    """
    Returns a randomized general item pool according to consumable mode
    Balanced random mode creates an item pool that has a value equal
    to the input pool's value, multiplied by the scarcity percentage
    """
    # Consumable mode:
    # 0: vanilla (no scarcity)
    # 1: full random (no scarcity)
    # 2: balanced random (scarcity applies)
    # 3: mystery only (no scarcity)

    # vanilla
    if consumable_mode == RandomizeConsumablesMode.OFF:
        return itempool

    def is_consumable(item_obj):
        item_name = item_obj.item_name
        item_score_obj = next((x for x in item_scores if x.get("name") == item_name), None)
        return item_score_obj != None

    kept_items = [x for x in itempool if not is_consumable(x)]
    removed_items = [x for x in itempool if is_consumable(x)]
    target_count = len(removed_items)

    # Random or Balanced Random
    if (consumable_mode == RandomizeConsumablesMode.FULL_RANDOM
        or consumable_mode == RandomizeConsumablesMode.BALANCED_RANDOM):
        # Generate fully random pool
        new_items = get_random_consumables(target_count)

        # Balance according to scarcity factor
        if consumable_mode == RandomizeConsumablesMode.BALANCED_RANDOM:
            target_score = 0
            for item_obj in removed_items:
                target_score += next(item["score"] for item in item_scores if item["name"] == item_obj.item_name)

            # Multiply score by the scarcity factor
            target_score = math.floor(target_score * (scarcity / 100))
            new_items = balance_consumables(new_items, target_score)
        
        # Convert from scored dict entries to proper item_obj list
        new_items = [Item.get(Item.item_name == item["name"]) for item in new_items]

    # Mystery only
    elif consumable_mode == RandomizeConsumablesMode.MYSTERY_ONLY:
        mystery_item = Item.get(Item.item_name == "Mystery")
        new_items = [mystery_item] * target_count

    new_itempool = kept_items + new_items
    assert(len(itempool) == len(new_itempool))
    return new_itempool

def get_trapped_itempool(
    itempool:list,
    trap_mode:int,
    randomize_favors_mode:int,
    do_randomize_dojo:bool,
    keyitems_outside_dungeon:bool
) -> list:
    """
    Modifies and returns a given item pool after placing trap items.
    This swaps out consumable items with trap items, which do not actually give
    the item to Mario, and instead damage him and make him drop coins.
    The items need not necessarily look like consumables, and can use the
    sprites of badges, key items and others instead.
    """
    # Trap mode:
    # 0: no traps
    # 1: sparse
    # 2: moderate
    # 3: plenty

    if trap_mode == 0:
        return itempool

    if trap_mode == 1:
        max_traps = 15
    elif trap_mode == 2:
        max_traps = 35
    else:
        max_traps = 80

    koot_items = {"rewards": [], "keyitems": []}
    for item_node in Node.select().where(Node.vanilla_item.is_null(False)):
        if item_node.identifier in kootfavors_reward_locations:
            koot_items["rewards"].append(item_node.vanilla_item.item_name)
        if item_node.identifier in kootfavors_keyitem_locations:
            koot_items["keyitems"].append(item_node.vanilla_item.item_name)

    trap_flag = 0x2000
    new_itempool = []
    fakeable_items = []
    dungeon_items = []
    for item in (Item
                 .select()
                 .where(Item.item_type.in_(["KEYITEM","PARTNER","BADGE","GEAR"]))
    ):
        if item.unused or item.unplaceable:
            continue
        if (not do_randomize_dojo
        and item.item_name in exclude_due_to_settings.get("do_randomize_dojo")
        ):
            continue
        if (    randomize_favors_mode < IncludeFavorsMode.RND_REWARD_VANILLA_KEYITEMS
            and item.item_name in koot_items["rewards"]
        ):
            continue
        if (    randomize_favors_mode < IncludeFavorsMode.FULL_SHUFFLE
            and item.item_name in koot_items["keyitems"]
        ):
            continue
        if not keyitems_outside_dungeon:
            # If no wild keys then don't use them for traps
            if not dungeon_items:
                for area_key_dict in limited_by_item_areas.values():
                    for key_list in area_key_dict.values():
                        dungeon_items.extend(key_list)
            if item.item_name in dungeon_items:
                continue

        fakeable_items.append(item)

    # Bias towards placing UltraStone traps, as requested by clover
    item_ultrastone = Item.get(Item.item_name == 'UltraStone')
    fakeable_items.extend([item_ultrastone] * 9)

    cnt_traps = 0
    shuffled_pool = itempool.copy()
    random.shuffle(shuffled_pool)

    for item_obj in shuffled_pool:
        if item_obj.item_type != "ITEM" or cnt_traps >= max_traps:
            new_itempool.append(item_obj)
        else:
            new_trapitem = random.choice(fakeable_items)
            new_trapitem.value = new_trapitem.value | trap_flag
            new_itempool.append(new_trapitem)
            cnt_traps += 1

    return new_itempool
