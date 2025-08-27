"""This module handles creation of item hints for Merluvlee to offer Mario."""
from rando_enums.enum_options import (
    IncludeFavorsMode,
    IncludeLettersMode,
    PartnerShuffle,
    SpiritShuffleMode,
)

from metadata.item_source_types import item_source_types as source_types
from metadata.itemlocation_special import (
    kootfavors_reward_locations,
    kootfavors_keyitem_locations,
    chainletter_giver_locations,
    chainletter_final_reward_location,
    simpleletter_locations,
    limited_by_item_areas,
)
from metadata.partners_meta import all_partners

def get_itemhints(
    allow_itemhints:bool,
    placed_items:list,
    starting_partners:list,
    partner_shuffle:PartnerShuffle,
    do_randomize_shops:bool,
    do_randomize_panels:bool,
    favors_mode:int,
    randomize_letters_mode:int,
    keyitems_outside_dungeon:bool,
    forever_forest_open:bool,
    spirit_shuffle_mode:SpiritShuffleMode,
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
    uninteresting_keyitems = [
        "PrisonKeyA",
        "PrisonKeyB",
        "FirstDegreeCard",
        "SecondDegreeCard",
        "ThirdDegreeCard",
        "FourthDegreeCard",
        "Diploma",
        "MysteryNote",
        "SilverCredit",
        "GoldCredit",
    ]

    interesting_badges = [
        "PowerPlusA",
        "PowerPlusB",
        "DodgeMaster",
        "PowerBounce",
        "DoubleDip",
        "QuickChange",
        "AllorNothing",
        "MegaRush",
        "DefendPlusA",
        "Berserker",
        "MegaQuake",
        "SJumpChg",
        "PowerRush",
        "SpeedySpin",
        "DamageDodgeA",
        "DamageDodgeB",
    ]

    # The hints table is build by pairing an item id with a word describing
    # a map and a item source type (like 'given by npc' or 'in block')
    for item_node in placed_items:
        if item_node.current_item.item_type in ["KEYITEM","BADGE","STARPIECE","PARTNER","STARSPIRIT"]:
            # Skip current item hint if not randomized
            if (    item_node.key_name_item.startswith("Shop")
                and not do_randomize_shops
            ):
                continue
            if (    item_node.key_name_item == "HiddenPanel"
                and not do_randomize_panels
            ):
                continue
            if (    item_node.identifier in kootfavors_reward_locations
                and favors_mode < IncludeFavorsMode.RND_REWARD_VANILLA_KEYITEMS
            ):
                continue
            if (    item_node.identifier in kootfavors_keyitem_locations
                and favors_mode < IncludeFavorsMode.FULL_SHUFFLE
            ):
                continue
            if (    item_node.identifier in chainletter_giver_locations
                and randomize_letters_mode < IncludeLettersMode.FULL_SHUFFLE
            ):
                continue
            if (    item_node.identifier == chainletter_final_reward_location
                and randomize_letters_mode < IncludeLettersMode.RANDOM_CHAIN_REWARD
            ):
                continue
            if (    item_node.identifier in simpleletter_locations
                and randomize_letters_mode < IncludeLettersMode.SIMPLE_LETTERS
            ):
                continue
            if (    item_node.identifier == "MAC_02/GiftD"
                and forever_forest_open
            ):
                continue
            if (    item_node.current_item.item_name in limited_keyitems
                and not keyitems_outside_dungeon
            ):
                continue
            # Skip partner if default location or starting partner
            if (    item_node.current_item.item_name in all_partners
                and (   item_node.current_item.item_name in starting_partners
                     or partner_shuffle != PartnerShuffle.VANILLA)
            ):
                continue

            # Skip current non-partner item unless it is interesting in any way
            if (   (    item_node.current_item.item_type == "BADGE"
                    and item_node.current_item.item_name not in interesting_badges)
                or (    item_node.current_item.item_type == "KEYITEM"
                    and item_node.current_item.item_name in uninteresting_keyitems)
                or item_node.current_item.is_trapped()
            ):
                continue

            # Skip Star Spirits if not randomized
            if (    item_node.current_item.item_type == "STARSPIRIT"
                and spirit_shuffle_mode == SpiritShuffleMode.VANILLA
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
