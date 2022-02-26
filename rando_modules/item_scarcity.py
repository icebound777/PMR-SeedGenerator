import random
from math import ceil

from db.item import Item

def get_scarcitied_itempool(itempool:list, scarcity:int) -> list:
    scarcity_tiers = {
        0: [0x157], # Coin
        1: [
            0x085, # Pebble
            0x086, # DustyHammer
            0x089, # TastyTonic
            0x08D, # DriedShroom
            0x0C2, # Mistake
        ],
        2: [
            0x09C, # Lemon
            0x09D, # Lime
            0x0A6, # KoopaLeaf
            0x0AE, # StinkyHerb
            0x0AC, # Coconut
            0x0A5, # Goomnut
            0x0A0, # YellowBerry
            0x08A, # Mushroom
            0x094, # Apple
            0x09E, # BlueBerry
            0x09F, # RedBerry
            0x09B, # SuperSoda
            0x0A1, # BubbleBerry
            0x0A4, # HoneySyrup
            0x0B6, # FriedShroom
        ],
        3: [
            0x0AB, # Egg
            0x0AF, # IcedPotato
            0x090, # POWBlock
            0x0C3, # KoopaTea
            0x0A7, # DriedPasta
            0x08B, # VoltShroom
            0x0B0, # SpicySoup
        ],
        4: [
            0x096, # Mystery
            0x0AA, # CakeMix
            0x080, # FireFlower
            0x084, # ThunderBolt
            0x0D5, # PotatoSalad
            0x0D6, # NuttyCake
            0x0C7, # Spaghetti
            0x08C, # SuperShroom
            0x0C9, # FriedEgg
            0x0CA, # HoneyShroom
            0x0B5, # Koopasta
            0x0A3, # MapleSyrup
            0x0D8, # BoiledEgg
            0x0D2, # StrangeCake
        ],
        5: [
            0x0A9, # StrangeLeaf
            0x08F, # SleepySheep
            0x0A8, # DriedFruit
            0x081, # SnowmanDoll
            0x0AD, # Melon
            0x0C8, # EggMissile
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
        6: [
            0x098, # FrightJar
            0x09A, # DizzyDial
            0x082, # ThunderRage
            0x091, # HustleDrink
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
        7: [
            0x0BF, # SpecialShake
            0x0C0, # BigCookie
            0x088, # StoneCap
            0x095, # LifeShroom
            0x0BC, # HealthyJuice
            0x093, # WhackasBump
            0x0BA, # SweetShroom
        ],
        8: [
            0x092, # StopWatch
            0x083, # ShootingStar
            0x08E, # UltraShroom
            0x0A2, # JamminJelly
            0x0B2, # HoneyUltra
            0x0DA, # JellyShroom1
        ],
        9: [
            0x0B3, # MapleUltra
            0x0C6, # JellySuper
            0x0D1, # JellyPop
        ],
        10: [
            0x097, # RepelGel
            0x0BE, # DeluxeFeast
            0x0B4, # JellyUltra
        ]
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

    new_itempool = []

    for item_obj in itempool:
        item_id = item_obj.value
        scarcity_tier = -1

        # Fetch scarcity tier of current item
        for tier, itemlist in scarcity_tiers.items():
            if item_id in itemlist:
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
            new_item_id = random.choice(scarcity_tiers.get(new_scarcity_tier))
            new_item = Item.get(Item.value == new_item_id)
            new_itempool.append(new_item)
            #print(f"Changed {item_obj} to {new_item}")

    return new_itempool
