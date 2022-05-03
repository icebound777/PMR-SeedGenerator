import random
from math import ceil

from db.item import Item
from db.node import Node

from metadata.item_exclusion import exclude_due_to_settings
from metadata.itemlocation_special import kootfavors_locations

def get_scarcitied_itempool(itempool:list, scarcity:int) -> list:
    """
    Modifies and returns a given item pool for scarcity of consumables.
    This swaps out items with weaker ones, according to the chosen scarcity
    intensity.
    """
    TYPE_BATTLEITEM = 0
    TYPE_HEALINGITEM = 1
    TYPE_TAYCETITEM = 2

    scarcity_tiers = {
        0: 0x157, # Coin
        1: {
            TYPE_BATTLEITEM: [
                0x085, # Pebble
                0x086, # DustyHammer
            ],
            TYPE_HEALINGITEM: [
                0x089, # TastyTonic
                0x08D, # DriedShroom
            ],
            TYPE_TAYCETITEM: [
                0x0C2, # Mistake
            ]
        },
        2: {
            TYPE_BATTLEITEM: [
                0x0AC, # Coconut
            ],
            TYPE_HEALINGITEM: [
                0x09C, # Lemon
                0x09D, # Lime
                0x0A6, # KoopaLeaf
                0x0AE, # StinkyHerb
                0x0A5, # Goomnut
                0x0A0, # YellowBerry
                0x08A, # Mushroom
                0x094, # Apple
                0x09E, # BlueBerry
                0x09F, # RedBerry
                0x09B, # SuperSoda
                0x0A1, # BubbleBerry
                0x0A4, # HoneySyrup
            ],
            TYPE_TAYCETITEM: [
                0x0B6, # FriedShroom
            ],
        },
        3: {
            TYPE_BATTLEITEM: [
                0x090, # POWBlock
                0x08B, # VoltShroom
            ],
            TYPE_HEALINGITEM: [
                0x0AB, # Egg
                0x0A7, # DriedPasta
                0x0AF, # IcedPotato
            ],
            TYPE_TAYCETITEM: [
                0x0C3, # KoopaTea
                0x0B0, # SpicySoup
            ],
        },
        4: {
            TYPE_BATTLEITEM: [
                0x096, # Mystery
                0x080, # FireFlower
                0x084, # ThunderBolt
            ],
            TYPE_HEALINGITEM: [
                0x0AA, # CakeMix
                0x08C, # SuperShroom
                0x0CA, # HoneyShroom
                0x0A3, # MapleSyrup
            ],
            TYPE_TAYCETITEM: [
                0x0D5, # PotatoSalad
                0x0D6, # NuttyCake
                0x0C7, # Spaghetti
                0x0C9, # FriedEgg
                0x0B5, # Koopasta
                0x0D8, # BoiledEgg
                0x0D2, # StrangeCake
            ],
        },
        5: {
            TYPE_BATTLEITEM: [
                0x081, # SnowmanDoll
                0x08F, # SleepySheep
                0x0C8, # EggMissile
            ],
            TYPE_HEALINGITEM: [
                0x0A9, # StrangeLeaf
                0x0A8, # DriedFruit
                0x0AD, # Melon
            ],
            TYPE_TAYCETITEM: [
                0x0BD, # BlandMeal
                0x0C1, # Cake
                0x0CF, # CocoPop
                0x0D4, # FrozenFries
                0x0C4, # HoneySuper
                0x0B7, # ShroomCake
                0x0CD, # FirePop
                0x0D7, # MapleShroom
                0x0C5, # MapleSuper
            ],
        },
        6: {
            TYPE_BATTLEITEM: [
                0x082, # ThunderRage
                0x091, # HustleDrink
                0x098, # FrightJar
                0x09A, # DizzyDial
            ],
            TYPE_HEALINGITEM: [

            ],
            TYPE_TAYCETITEM: [
                0x0B1, # ApplePie
                0x0D3, # KookyCookie
                0x0B9, # HotShroom
                0x0D0, # LemonCandy
                0x0CB, # HoneyCandy
                0x0CE, # LimeCandy
                0x0BB, # YummyMeal
                0x0D9, # YoshiCookie
                0x0CC, # ElectroPop
                0x0B8, # ShroomSteak
            ],
        },
        7: {
            TYPE_BATTLEITEM: [
                0x088, # StoneCap
            ],
            TYPE_HEALINGITEM: [
                0x095, # LifeShroom
                0x093, # WhackasBump
            ],
            TYPE_TAYCETITEM: [
                0x0BF, # SpecialShake
                0x0C0, # BigCookie
                0x0BC, # HealthyJuice
                0x0BA, # SweetShroom
            ],
        },
        8: {
            TYPE_BATTLEITEM: [
                0x092, # StopWatch
                0x083, # ShootingStar
            ],
            TYPE_HEALINGITEM: [
                0x08E, # UltraShroom
                0x0A2, # JamminJelly
            ],
            TYPE_TAYCETITEM: [
                0x0B2, # HoneyUltra
                0x0DA, # JellyShroom1
            ],
        },
        9: {
            TYPE_BATTLEITEM: [

            ],
            TYPE_HEALINGITEM: [

            ],
            TYPE_TAYCETITEM: [
                0x0B3, # MapleUltra
                0x0C6, # JellySuper
                0x0D1, # JellyPop
            ],
        },
        10: {
            TYPE_BATTLEITEM: [
                0x097, # RepelGel
            ],
            TYPE_HEALINGITEM: [

            ],
            TYPE_TAYCETITEM: [
                0x0B4, # JellyUltra
                0x0BE, # DeluxeFeast
            ],
        },
    }

    # item scarcity:
    # when placing a non-essential item, have a chance to replace the item with
    # another from a lower item tier according to...
    #
    # 0    vanilla
    # 1    30% chance to divide tier by 2
    # 2    40% chance to divide tier by 2, 10% chance to divide tier by 3
    # 3    50% chance to divide tier by 2, 20% chance to divide tier by 3
    # 4    60% chance to divide tier by 2, 40% chance to divide tier by 3
    # 5    100% chance to divide tier by 3
    #
    # Also choose an item by type:
    # battle items    40% chance
    # healing items   35% chance
    # Tayce T. items  25% chance
    #
    # If no item of the chosen type exists in the chosen tier, retry with lower
    # tier. If tier 0 is reached this way, pick randomly

    # setting: {chance in %: divider}
    scarcity_factors = {
        0: {100: 1},
        1: { 70: 1,
             30: 2},
        2: { 50: 1,
             40: 2,
             10: 3},
        3: { 30: 1,
             50: 2,
             20: 3},
        4: { 60: 2,
             40: 3},
        5: {100: 3}
    }

    # item type: {chance in %}
    itemtype_chances = {
        TYPE_BATTLEITEM: 40,
        TYPE_HEALINGITEM: 35,
        TYPE_TAYCETITEM: 25
    }

    new_itempool = []

    for item_obj in itempool:
        item_id = item_obj.value
        scarcity_tier = -1

        # Fetch scarcity tier of current item
        for tier, type_dict in scarcity_tiers.items():
            if isinstance(type_dict, int) and tier == 0 and item_id == type_dict:
                scarcity_tier = tier
                break
            if isinstance(type_dict, dict):
                for item_list in type_dict.values():
                    if item_id in item_list:
                        scarcity_tier = tier
                        break

        # If current item is not in scarcity list, or we're doing vanilla
        # scarcity, skip replacing it
        if scarcity_tier == -1 or scarcity == 0:
            new_itempool.append(item_obj)
            #print(f"Kept {item_obj}")
            continue

        # Choose random new scarcity tier for current item
        rnd_value = random.random() * 100
        probability_count = 0
        for chance, divider in scarcity_factors.get(scarcity).items():
            probability_count += chance
            if rnd_value <= probability_count:
                tier_divider = divider
                break
        new_scarcity_tier = ceil(scarcity_tier / tier_divider)

        # Get new item if scarcity changed
        if scarcity_tier == new_scarcity_tier:
            new_itempool.append(item_obj)
            #print(f"Kept {item_obj}")
        else:
            # Determine item type to pick
            rnd_value = random.random() * 100
            probability_count = 0
            chosen_type = TYPE_BATTLEITEM # default
            for item_type, chance in itemtype_chances.items():
                probability_count += chance
                if rnd_value <= probability_count:
                    chosen_type = item_type
                    break

            # Search for lower tier item of the chosen item type
            item_found = False
            new_item_id = 0
            while not item_found:
                if (new_scarcity_tier >= 1
                and scarcity_tiers.get(new_scarcity_tier).get(chosen_type)
                ):
                    new_item_id = random.choice(scarcity_tiers.get(new_scarcity_tier).get(chosen_type))
                    item_found = True
                elif new_scarcity_tier >= 1:
                    new_scarcity_tier = new_scarcity_tier - 1
                else:
                    # Reached tier 0: Coin only
                    new_item_id = scarcity_tiers.get(new_scarcity_tier)
                    item_found = True

            # Add item
            new_item = Item.get(Item.value == new_item_id)
            new_itempool.append(new_item)

            #print(f"Changed {item_obj} to {new_item}")

    return new_itempool


def get_trapped_itempool(
    itempool:list,
    trap_mode:int,
    do_randomize_koopakoot:bool,
    do_randomize_dojo:bool
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
    # 1: sparce
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

    koot_items = []
    for item_node in Node.select().where(Node.vanilla_item.is_null(False)):
        if item_node.identifier in kootfavors_locations:
            koot_items.append(item_node.vanilla_item.item_name)

    trap_flag = 0x2000
    new_itempool = []
    fakeable_items = []
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
        if (not do_randomize_koopakoot
        and item.item_name in koot_items
        ):
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
