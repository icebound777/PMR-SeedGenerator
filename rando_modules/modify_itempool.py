import random
from math import ceil, floor

from db.item import Item
from db.node import Node

from metadata.item_general import \
    healing_items, \
    battle_items, \
    taycet_items
from metadata.item_exclusion import exclude_due_to_settings
from metadata.itemlocation_special import \
    kootfavors_reward_locations, \
    kootfavors_keyitem_locations, \
    limited_by_item_areas

TYPE_BATTLEITEM = 0
TYPE_HEALINGITEM = 1
TYPE_TAYCETITEM = 2

item_tiers = {
    0: 0x157, # Coin
    1: {
        TYPE_BATTLEITEM: [
            0x085, # Pebble
            0x086, # DustyHammer
        ],
        TYPE_HEALINGITEM: [
            0x089, # TastyTonic
            0x08D, # DriedShroom
            0x09C, # Lemon
            0x09D, # Lime
            0x0A5, # Goomnut
        ],
        TYPE_TAYCETITEM: [
            0x0C2, # Mistake
        ]
    },
    2: {
        TYPE_BATTLEITEM: [
            0x080, # FireFlower
            0x084, # ThunderBolt
            0x08B, # VoltShroom
            0x090, # POWBlock
            0x096, # Mystery
            0x0AC, # Coconut
        ],
        TYPE_HEALINGITEM: [
            0x08A, # Mushroom
            0x094, # Apple
            0x09B, # SuperSoda
            # 0x09E, # BlueBerry
            # 0x09F, # RedBerry
            # 0x0A0, # YellowBerry
            # 0x0A1, # BubbleBerry
            0x0A4, # HoneySyrup
            0x0A6, # KoopaLeaf
            0x0A7, # DriedPasta
            0x0A9, # StrangeLeaf
            0x0AB, # Egg
            0x0AE, # StinkyHerb
            0x0AF, # IcedPotato
        ],
        TYPE_TAYCETITEM: [
            0x0B0, # SpicySoup
            0x0B6, # FriedShroom
            0x0C3, # KoopaTea
        ],
    },
    3: {
        TYPE_BATTLEITEM: [
            0x081, # SnowmanDoll
            0x08F, # SleepySheep
            0x0C8, # EggMissile
        ],
        TYPE_HEALINGITEM: [
            0x08C, # SuperShroom
            0x0A3, # MapleSyrup
            0x0A8, # DriedFruit
            0x0AA, # CakeMix
            0x0AD, # Melon
        ],
        TYPE_TAYCETITEM: [
            0x0B1, # ApplePie
            0x0B5, # Koopasta
            0x0B7, # ShroomCake
            0x0B9, # HotShroom
            0x0BD, # BlandMeal
            0x0C1, # Cake
            0x0CA, # HoneyShroom
            0x0C4, # HoneySuper
            0x0C5, # MapleSuper
            0x0C7, # Spaghetti
            0x0C9, # FriedEgg
            0x0CB, # HoneyCandy
            0x0CD, # FirePop
            0x0CE, # LimeCandy
            0x0CF, # CocoPop
            0x0D0, # LemonCandy
            0x0D2, # StrangeCake
            0x0D3, # KookyCookie
            0x0D4, # FrozenFries
            0x0D5, # PotatoSalad
            0x0D6, # NuttyCake
            0x0D7, # MapleShroom
            0x0D8, # BoiledEgg
        ],
    },
    4: {
        TYPE_BATTLEITEM: [
            0x082, # ThunderRage
            0x083, # ShootingStar
            0x088, # StoneCap
            0x091, # HustleDrink
            0x092, # StopWatch
            0x097, # RepelGel
            0x098, # FrightJar
            0x09A, # DizzyDial
        ],
        TYPE_HEALINGITEM: [
            0x08E, # UltraShroom
            0x093, # WhackasBump
            0x095, # LifeShroom
            0x0A2, # JamminJelly
        ],
        TYPE_TAYCETITEM: [
            0x0B2, # HoneyUltra
            0x0B3, # MapleUltra
            0x0B4, # JellyUltra
            0x0B8, # ShroomSteak
            0x0BA, # SweetShroom
            0x0BB, # YummyMeal
            0x0BC, # HealthyJuice
            0x0BE, # DeluxeFeast
            0x0BF, # SpecialShake
            0x0C0, # BigCookie
            0x0C6, # JellySuper
            0x0CC, # ElectroPop
            0x0D1, # JellyPop
            0x0D9, # YoshiCookie
            0x0DA, # JellyShroom1
        ],
    },
}

def get_item_tier(item_id:int) -> int:
    """
    Gets the tier of an item by its id, or -1 if not assigned one
    """
    item_tier = -1

    # Fetch item tier of current item
    for tier, type_dict in item_tiers.items():
        if isinstance(type_dict, int) and tier == 0 and item_id == type_dict:
            item_tier = tier
            break
        if isinstance(type_dict, dict):
            for item_list in type_dict.values():
                if item_id in item_list:
                    item_tier = tier
                    break

    return item_tier


def get_random_item_by_tier(item_tier:int, item_type:int) -> int:
    """
    Returns the id of an item with the given tier and type, or of
    a lower tier if no item of that tier and type exists
    """
    new_item_id = 0
    # Search for item of given tier, or lower tier if none exists
    item_found = False
    while not item_found:
        if (item_tier >= 1
            and item_tiers.get(item_tier).get(item_type)
        ):
            new_item_id = random.choice(item_tiers.get(item_tier).get(item_type))
            item_found = True
        elif item_tier >= 1:
            item_tier = item_tier - 1
        else:
            # Reached tier 0: Coin only
            new_item_id = item_tiers.get(item_tier)
            item_found = True
    
    return new_item_id


def randomize_value_list(value_list:list, scarcity:int) -> list:
    """
    When given a list of number of items at each tier, returns a new list
    with the a value of the value of the original list, multiplied by the scarcity
    """
    # Score for each item tier
    tier_scores = [0, 2, 5, 11, 15]
    list_score = sum([tier_scores[i] * num for (i, num) in enumerate(value_list)])
    target_score = floor(list_score * scarcity / 100)
    # print(f'Input Score: {list_score} Target Score: {target_score}')

    new_value_list = value_list.copy()
    # Special case: scarcity too low, must add in coins to make up difference
    if target_score < sum(new_value_list) * tier_scores[1]:
        n = sum(value_list)
        new_value_list = [0] * len(item_tiers)
        list_score = 0
        # Add random items until exceeded score
        while list_score < target_score:
            a = random.randrange(10) + 1
            new_value_list[a] += 1
            list_score += tier_scores[a]
        # Fill the rest with coins (tier 0 item)
        new_value_list[0] = n - sum(new_value_list)
        return new_value_list

    # Special case: scarcity too high, fill with top tier items
    # This should never happen...
    if target_score > sum(new_value_list) * tier_scores[len(item_tiers) - 1]:
        n = sum(new_value_list)
        new_value_list = [0] * len(item_tiers)
        new_value_list[len(item_tiers) - 1] = n
        return new_value_list

    i = 0
    # Run at least 25 times to fuzz initial state
    # If it ever takes more than 1000 iterations, cut it off
    while i < 25 or i > 1000 or list_score != target_score:
        i += 1
        # Generate two random tiers
        a = random.randrange(len(item_tiers) - 1) + 1
        b = random.randrange(len(item_tiers) - 1) + 1
        if a == b:
            continue
        elif a > b:
            higher, lower = a, b
        else:
            higher, lower = b, a

        # If the score is too high,
        # add to the lower tier and subtract from the higher tier
        if list_score > target_score and new_value_list[higher] > 0:
            new_value_list[lower] += 1
            new_value_list[higher] -= 1
            list_score += tier_scores[lower] - tier_scores[higher]
        # If the score is too low,
        # add the to higher tier and subtract from the lower tier
        elif list_score <= target_score and new_value_list[lower] > 0:
            new_value_list[higher] += 1
            new_value_list[lower] -= 1
            list_score += tier_scores[higher] - tier_scores[lower]

    return new_value_list


def get_randomized_itempool(itempool:list, consumable_mode:int, scarcity:int) -> list:
    """
    Returns a randomized general item pool according to consumable mode
    Balanced random mode creates an item pool that has a value equal
    to the input pool's value, multiplied by the scarcity percentage
    """
    # Consumable mode:
    # 0: vanilla (no scarcity)
    # 1: balanced random (scarcity applies)
    # 2: full random (no scarcity)
    # 3: mystery only (no scarcity)

    if consumable_mode == 0:
        # vanilla
        return itempool
    elif consumable_mode == 1:
        # construct a new lists of item tier counts for balanced random
        # Handle battle and healing items seperately 
        base_battle_counts = [0] * len(item_tiers)
        base_healing_counts = [0] * len(item_tiers)
        for item_obj in itempool:
            item_id = item_obj.value
            item_tier = get_item_tier(item_id)
            # Only counting tiered items
            if item_tier > 0:
                if item_id in battle_items:
                    base_battle_counts[item_tier] += 1
                else:
                    base_healing_counts[item_tier] += 1

        target_battle_counts = randomize_value_list(base_battle_counts, scarcity)
        target_healing_counts = randomize_value_list(base_healing_counts, scarcity)
        # print(f"Scarcity: {scarcity}")
        # print(f"Battle Base:\t{base_battle_counts}")
        # print(f"Battle New:\t{target_battle_counts}")
        # print(f"Healing Base:\t{base_healing_counts}")
        # print(f"Healing New:\t{target_healing_counts}")

    # Construct a new item pool
    new_itempool = []
    for item_obj in itempool:
        # Only replace consumable items, not badges or anything else
        if item_obj.item_type != "ITEM":
            new_itempool.append(item_obj)
            continue
        
        # Balanced random
        if consumable_mode == 1:
            # handle battle items
            if sum(target_battle_counts) > 0:
                for tier, count in enumerate(target_battle_counts):
                    if count <= 0:
                        continue
                    else:
                        new_item_id = get_random_item_by_tier(tier, TYPE_BATTLEITEM)
                        target_battle_counts[tier] -= 1
                        break
            # handle healing items
            else:
                # 10% chance for healing items to be tayce t item
                new_item_type = TYPE_HEALINGITEM if random.randrange(10) != 0 else TYPE_TAYCETITEM
                for tier, count in enumerate(target_healing_counts):
                    if count <= 0:
                        continue
                    else:
                        new_item_id = get_random_item_by_tier(tier, new_item_type)
                        target_healing_counts[tier] -= 1
                        break

            new_item_obj = Item.get(Item.value == new_item_id)
        # Full random
        elif consumable_mode == 2:
            consumable_items = []
            consumable_items += healing_items
            consumable_items += battle_items
            consumable_items += taycet_items

            new_item_id = random.choice(consumable_items)
            new_item_obj = Item.get(Item.value == new_item_id)
        # Mystery only
        elif consumable_mode == 3: 
            new_item_obj = Item.get(Item.item_name == "Mystery")

        # print(f"Changed {item_obj} to {new_item_obj}")
        new_itempool.append(new_item_obj)

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
                 .where(Item.item_type.in_(["KEYITEM","PARTNER","BADGE"]))
    ):
        if item.unused or item.unplaceable:
            continue
        if (not do_randomize_dojo
        and item.item_name in exclude_due_to_settings.get("do_randomize_dojo")
        ):
            continue
        if (    randomize_favors_mode < 1
            and item.item_name in koot_items["rewards"]
        ):
            continue
        if (    randomize_favors_mode < 2
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
