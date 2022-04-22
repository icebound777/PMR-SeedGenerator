"""This module handles creation of item hints for Merluvlee to offer Mario."""
from metadata.item_source_types import item_source_types as source_types
from metadata.itemlocation_special \
    import kootfavors_locations,\
           chainletter_giver_locations,\
           limited_by_item_areas

def get_itemhints(
    allow_itemhints:bool,
    placed_items:list,
    starting_partners:list,
    partners_in_default_locations:bool,
    do_randomize_shops:bool,
    do_randomize_panels:bool,
    do_randomize_koopakoot:bool,
    do_randomize_letterchain:bool,
    keyitems_outside_dungeon:bool
):
    """
    Returns a list of item hint lists for a given list of item nodes.
    Each item hint list contains the item id and a reference word describing
    the area, map and item source type.
    """
    if not allow_itemhints:
        return [[0x00000000, 0xFFFFFFFF]]

    itemhints = []
    limited_keyitems = []
    for area in limited_by_item_areas:
        for item_type in limited_by_item_areas.get(area):
            limited_keyitems.extend(limited_by_item_areas[area][item_type])
    interesting_keyitems = [
        "UltraStone",
        "PulseStone",
        "CrystalPalaceKey",
        "RedKey",
        "BlueKey",
        "LunarStone",
        "PyramidStone",
        "DiamondStone",
        "BooWeight",
        "BooPortrait",
        "ToyTrain",
        "StoreroomKey",
        "JadeRaven",
        "MagicalSeed1",
        "MagicalSeed2",
        "MagicalSeed3",
        "MagicalSeed4",
        "MagicalBean",
        "FertileSoil",
        "MiracleWater",
        "WarehouseKey",
        "SnowmanBucket",
        "SnowmanScarf",
        "StarStone",
        "KoopaFortressKeyA",
        "KoopaFortressKeyB",
        "KoopaFortressKeyC",
        "KoopaFortressKeyD",
        "RuinsKeyA",
        "RuinsKeyB",
        "RuinsKeyC",
        "RuinsKeyD",
        "TubbaCastleKeyA",
        "TubbaCastleKeyB",
        "TubbaCastleKeyC",
        "BowserCastleKeyA",
        "BowserCastleKeyB",
        "BowserCastleKeyC",
        "BowserCastleKeyD",
        "BowserCastleKeyE",
    ]

    interesting_badges = [
        "PowerPlusA",
        "PowerPlusB",
        "DodgeMaster",
        "PowerBounce",
        "DoubleDip",
        "QuickChange",
        "AllorNothing",
        "SlowGo", # :D
        "MegaRush",
        "DefendPlusA",
        "Berserker", # :D
        "MegaQuake",
        "SJumpChg",
        "PowerRush",
        "SpeedySpin",
        "DamageDodgeA",
        "DamageDodgeB",
        "AttackFXC", # :D
    ]
    
    all_partners = [
        "Goombario",
        "Kooper",
        "Bombette",
        "Parakarry",
        "Bow",
        "Watt",
        "Sushie",
        "Lakilester",
    ]

    # The hints table is build by pairing an item id with a word describing
    # a map and a item source type (like 'given by npc' or 'in block')
    for item_node in placed_items:
        if item_node.current_item.item_type in ["KEYITEM","BADGE","STARPIECE","PARTNER"]:
            # Skip current item hint if not randomized
            if (    item_node.key_name_item.startswith("Shop")
                and not do_randomize_shops
            ):
                continue
            if (    item_node.key_name_item == "HiddenPanel"
                and not do_randomize_panels
            ):
                continue
            if (    item_node.identifier in kootfavors_locations
                and not do_randomize_koopakoot
            ):
                continue
            if (    item_node.identifier in chainletter_giver_locations
                and not do_randomize_letterchain
            ):
                continue
            if (    item_node.current_item.item_name in limited_keyitems
                and not keyitems_outside_dungeon
            ):
                continue
            # Skip partner if default location or starting partner
            if (    item_node.current_item.item_name in all_partners
                and (   item_node.current_item.item_name in starting_partners
                     or partners_in_default_locations)
            ):
                continue

            # Skip current non-partner item unless it is interesting in any way
            if (    item_node.current_item.item_type in ["KEYITEM","BADGE"]
                and item_node.current_item.item_name not in interesting_keyitems
                and item_node.current_item.item_name not in interesting_badges
            ):
                continue

            cur_area_id = item_node.map_area.area_id
            cur_map_id = item_node.map_area.map_id
            cur_map_name = item_node.map_area.name
            cur_keyname = item_node.key_name_item

            item_id = item_node.current_item.value
            item_source_id = source_types.get(cur_map_name).get(cur_keyname)
            if item_source_id is None:
                print(f"item_source_id is None: {cur_map_name}:{cur_keyname}")
                raise TypeError
            #print(f"{cur_map_name=}; {cur_keyname=}")

            hint_word_1 = item_id
            hint_word_2 = (
                  cur_area_id << 24
                | cur_map_id  << 16
                | item_source_id  <<  8
            )

            itemhints.append([hint_word_1, hint_word_2])

    # Terminate hint table
    itemhints.append([0x00000000, 0xFFFFFFFF])

    return itemhints
