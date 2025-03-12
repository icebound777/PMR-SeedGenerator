"""
This modules offers the randomization logic and takes care of actually
randomizing the game according to the settings chosen.
"""
import random
#import logging
from copy import deepcopy

from db.node import Node
from db.item import Item
from db.map_area import MapArea

from models.MarioInventory import MarioInventory
from models.options.LogicOptionSet import LogicOptionSet

from rando_enums.enum_options import (
    BowserCastleMode,
    GearShuffleMode,
    StartingBoots,
    StartingHammer,
    IncludeFavorsMode,
    IncludeLettersMode,
    PartnerUpgradeShuffle,
    MultiCoinBlockShuffle,
    PartnerShuffle,
    DojoShuffle,
)

from rando_modules.modify_itempool import (
    get_randomized_itempool,
    get_trapped_itempool,
)

from rando_modules.unbeatable_seed_error import UnbeatableSeedError
from rando_modules.unbeatable_plando_placement_error import (
    UnbeatablPlandoPlacementError,
)
from rando_modules.plando_settings_mismatch_error import (
    PlandoSettingsMismatchError,
)
from rando_modules.item_pool_too_small_error import ItemPoolTooSmallError

from metadata.itemlocation_replenish import replenishing_itemlocations
from metadata.itemlocation_special import (
    kootfavors_reward_locations,
    kootfavors_keyitem_locations,
    chainletter_giver_locations,
    chainletter_final_reward_location,
    simpleletter_locations,
    radio_trade_event_locations,
    dojo_locations,
    limited_by_item_areas,
    bush_tree_coin_locations,
    overworld_coin_locations,
    block_coin_locations,
    favor_coin_locations,
    superblock_locations,
    multicoinblock_locations,
)
from metadata.progression_items import (
    progression_miscitems as progression_miscitems_names,
    progression_items,
)
from metadata.item_exclusion import (
    exclude_due_to_settings,
    exclude_from_taycet_placement,
)
from metadata.item_general import taycet_items, progressive_badges
from metadata.node_exclusion import exclude_from_trap_placement
from metadata.partners_meta import all_partners

from metadata.verbose_area_names import verbose_area_names
from metadata.verbose_item_names import verbose_item_names
from metadata.verbose_item_locations import verbose_item_locations

def get_startingnode_id_from_startingmap_id(starting_map_id):
    """Returns the starting node id (e.g. "MAC_00/4") for a given map id."""
    # Extract entrance, map and area from map-hex
    starting_map_hex = hex(starting_map_id)[2:]
    starting_map_entrance_id = int(starting_map_hex[-1:], 16)
    starting_map_map_id = int(starting_map_hex[-4:-2], 16) if starting_map_hex[-4:-2] != "" else 0
    starting_map_area_id = int(starting_map_hex[-6:-4], 16) if starting_map_hex[-6:-4] != "" else 0

    # Get maparea from db
    starting_maparea = MapArea.get(  (MapArea.area_id == starting_map_area_id)
                                   & (MapArea.map_id  == starting_map_map_id))

    # Janky, temporary workaround for jumpless logic being unable to handle
    # starting from pipe entrances pointing upwards (can't re-enter by jumping)
    if starting_maparea.name == 'MAC_00':
        starting_map_entrance_id = 0

    # String concat maparea-name and entrance-id to node-id string
    starting_node_id = starting_maparea.name + "/" + str(starting_map_entrance_id)

    return starting_node_id


def is_itemlocation_replenishable(item_node):
    """
    Returns True if the location described by a given node is replenishable,
    that is, the item at this location can be acquired multiple times.
    """
    node_id = item_node.identifier
    return (node_id in replenishing_itemlocations)


def _get_random_taycet_item():
    """
    Randomly pick a Tayce T. item object chosen out of all allowed Tayce T.
    items.
    """
    random_taycet_item_value = random.choice([x for x in taycet_items if x not in exclude_from_taycet_placement])
    random_taycet_item = Item.get(Item.value == random_taycet_item_value)
    return random_taycet_item


def _depth_first_search(
    node_id:str,
    world_graph:dict,
    reachable_node_ids:set, # set() of str()
    reachable_item_nodes:dict, # dict of str() on Node
    non_traversable_edges:dict, # dict() of node_id to list(edge_id)
    mario:MarioInventory
):
    """
    Executes a DFS (depths first search) through the world graph, starting from
    a given node.
    If the given node is new, attempts to traverse all outgoing edges from
    said node.
    If all of an edge's requirements are fulfilled, adds edge's pseudoitems to
    Mario's inventory (if any), then attempts a recursive DFS of that edge's
    target node to further traverse the world graph.
    If an edge's requirements are not fulfilled, it is added to the list of
    reachable but not yet traversable edges.
    Returns whether or not one or more pseudoitems have been found during
    graph traversal.
    """
    #logging.debug("> DFS node %s", node_id)
    found_new_pseudoitems = False # bool

    # Node already visited? -> Return!
    node_checked_earlier = False # bool
    if node_id in reachable_node_ids:
        if node_id in non_traversable_edges:
            node_checked_earlier = True
        else:
            return found_new_pseudoitems, mario
    else:
        reachable_node_ids.add(node_id)
    #logging.debug("DFS node_checked_earlier %s", node_checked_earlier)

    # If the current node is an item node and thus not an entrance node,
    # add it to the list of reachable item nodes for later item placement
    is_item_node = world_graph[node_id]["node"].key_name_item is not None
    if is_item_node and not node_checked_earlier:
        reachable_item_nodes[node_id] = world_graph[node_id]["node"]

    if not node_checked_earlier:
        # Get all outgoing edges
        outgoing_edges = [edge["edge_id"] for edge in world_graph[node_id]["edge_list"]]
    else:
        # Get all formerly untraversable edges
        outgoing_edges = non_traversable_edges.pop(node_id)

    for edge_id in outgoing_edges:
        # Check if all requirements for edge traversal are fulfilled
        edge = world_graph["edge_index"][edge_id]
        if mario.requirements_fulfilled(edge.get("reqs")):
            #logging.debug("DFS edge requirements fullfilled %s", edge)
            # Add all pseudoitems provided by this edge to the inventory
            if edge.get("pseudoitems") is not None:
                mario.add(edge.get("pseudoitems"))
                found_new_pseudoitems = True

            # DFS from newly reachable node
            found_additional_pseudoitems, mario = _depth_first_search(
                edge["target_node_id"],
                world_graph,
                reachable_node_ids,
                reachable_item_nodes,
                non_traversable_edges,
                mario
            )
            found_new_pseudoitems = found_new_pseudoitems or found_additional_pseudoitems
        else:
            if node_id not in non_traversable_edges:
                non_traversable_edges[node_id] = []
            non_traversable_edges[node_id].append(edge_id)
    return found_new_pseudoitems, mario


def _find_new_nodes_and_edges(
    world_graph:dict,
    reachable_node_ids:set,
    reachable_item_nodes:dict,
    non_traversable_edges:dict, # dict() of node_id to list(edge_id)
    mario:MarioInventory
):
    """
    Try to traverse already found edges which could not be traversed before.
    This re-traversing is accomplished by calling DFS on each respective edge's
    origin node ("from-node").
    """
    while True:
        found_new_items = False

        # We require a copy here since we cannot iterate over a list and
        # at the same time possibly delete entries from it (see DFS)
        non_traversable_edges_cpy = non_traversable_edges.copy()

        # Re-traverse already found edges which could not be traversed before.
        for from_node_id in non_traversable_edges:
            found_additional_items, mario = _depth_first_search(
                from_node_id,
                world_graph,
                reachable_node_ids,
                reachable_item_nodes,
                non_traversable_edges_cpy,
                mario
            )
            found_new_items = found_new_items or found_additional_items
        non_traversable_edges = non_traversable_edges_cpy.copy()

        # Keep searching for new edges and nodes until we don't find any new
        # items which might open up even more edges and nodes
        if not found_new_items:
            break

    return (
        reachable_node_ids,
        reachable_item_nodes,
        non_traversable_edges,
        mario
    )


def get_items_to_exclude(
    logic_settings:LogicOptionSet,
    starting_partners:list,
    do_partner_upgrade_shuffle:bool=False
) -> list:
    """
    Returns a list of items that should not be placed or given to Mario at the
    start.
    """
    excluded_items = []

    if logic_settings.include_dojo != DojoShuffle.OFF:
        for item_name in exclude_due_to_settings["do_randomize_dojo"][logic_settings.include_dojo]:
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    for partner_string in starting_partners:
        partner_item = Item.get(Item.item_name == partner_string)
        excluded_items.append(partner_item)
    if logic_settings.bluehouse_open:
        for item_name in exclude_due_to_settings.get("startwith_bluehouse_open"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if logic_settings.foreverforest_open:
        for item_name in exclude_due_to_settings.get("startwith_forest_open"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if logic_settings.magical_seeds_required < 4:
        for item_name in (
            exclude_due_to_settings
                .get("magical_seeds_required")
                .get(logic_settings.magical_seeds_required)
        ):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if logic_settings.bowsers_castle_mode > BowserCastleMode.VANILLA:
        for item_name in exclude_due_to_settings.get("shorten_bowsers_castle"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if logic_settings.bowsers_castle_mode == BowserCastleMode.BOSSRUSH:
        for item_name in exclude_due_to_settings.get("boss_rush"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if logic_settings.always_speedyspin:
        for item_name in exclude_due_to_settings.get("always_speedyspin"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if logic_settings.always_ispy:
        for item_name in exclude_due_to_settings.get("always_ispy"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if logic_settings.always_peekaboo:
        for item_name in exclude_due_to_settings.get("always_peekaboo"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if logic_settings.progressive_badges:
        for item_name in exclude_due_to_settings.get("do_progressive_badges"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if logic_settings.gear_shuffle_mode >= GearShuffleMode.GEAR_LOCATION_SHUFFLE:
        if logic_settings.starting_hammer == StartingHammer.ULTRAHAMMER:
            item = Item.get(Item.item_name == "HammerProxy3")
            excluded_items.append(item)
        if logic_settings.starting_hammer >= StartingHammer.SUPERHAMMER:
            item = Item.get(Item.item_name == "HammerProxy2")
            excluded_items.append(item)
        if logic_settings.starting_hammer >= StartingHammer.HAMMER:
            item = Item.get(Item.item_name == "HammerProxy1")
            excluded_items.append(item)
        if logic_settings.starting_boots == StartingBoots.ULTRABOOTS:
            item = Item.get(Item.item_name == "BootsProxy3")
            excluded_items.append(item)
        if logic_settings.starting_boots >= StartingBoots.SUPERBOOTS:
            item = Item.get(Item.item_name == "BootsProxy2")
            excluded_items.append(item)
        if logic_settings.starting_boots >= StartingBoots.BOOTS:
            item = Item.get(Item.item_name == "BootsProxy1")
            excluded_items.append(item)
    if do_partner_upgrade_shuffle:
        for item_name in exclude_due_to_settings.get("partner_upgrade_shuffle"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)

    return excluded_items


def _generate_item_pools(
    world_graph,
    pool_progression_items:list,
    pool_misc_progression_items:list,
    pool_other_items:list,
    all_item_nodes:list,
    logic_settings:LogicOptionSet,
    starting_items:list,
    starting_partners:list,
    do_partner_upgrade_shuffle:bool,
    plando_item_placement: dict[str | Item] | None,
    plando_traps_placed: int,
    plando_item_placeholders: dict[str, str],
    plando_trap_placeholders: list[str],
) -> tuple[list[Item], dict[str, Item], dict[str, Item]]:
    """
    Generates item pools for items to be shuffled (depending on chosen
    settings this may exclude certain items). The item pools generated are
    pool_progression_items (keyitems that influence progression),
    pool_misc_progression_items (non-keyitems that influence progression) and
    pool_other_items (every other item). Additionally marks item nodes that
    shall not be randomized as already filled.
    """
    if plando_item_placement is None:
        plando_item_placement = dict()
    items_plandod: int = 0

    pool_coins_only = []
    pool_illogical_consumables = []
    pool_badges = []

    items_to_remove_from_pools: list[Item] = []

    def add_to_correct_itempool(
        new_item: Item,
    ):
        if (    new_item.progression
            and new_item.item_type != 'ITEM'
        ):
            pool_progression_items.append(new_item)
        else:
            if (    new_item.item_name in progression_miscitems_names
                and new_item not in pool_misc_progression_items
            ):
                # Since progression misc items have to be placed in
                # replenishable locations, we only need one of each
                prog_misc_item = new_item
                prog_misc_item.progression = True
                pool_misc_progression_items.append(prog_misc_item)
            else:
                if new_item.item_type == "COIN":
                    pool_coins_only.append(new_item)
                elif new_item.item_type == "ITEM":
                    pool_illogical_consumables.append(new_item)
                elif new_item.item_type == "BADGE":
                    pool_badges.append(new_item)
                else:
                    pool_other_items.append(new_item)

    # Pre-fill nodes that are not to be randomized
    all_plando_locations = (
        list(plando_item_placement.keys())
      + list(plando_item_placeholders.keys())
      + plando_trap_placeholders
    )
    for node_id in world_graph:
        if node_id == "edge_index":
            continue
        current_node = world_graph[node_id]["node"]
        is_item_node = current_node.key_name_item
        if is_item_node: # and current_node not in all_item_nodes:

            current_node_id = current_node.identifier

            # Check the randomization settings. If something is not supposed
            # to be randomized, mark location as filled by setting its
            # current_item value
            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in overworld_coin_locations
                and not logic_settings.include_coins_overworld
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Shuffle Overworld Coins\" setting being turned off"
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in block_coin_locations
                and not logic_settings.include_coins_blocks
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Shuffle Coin Blocks\" setting being turned off"
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in bush_tree_coin_locations
                and not logic_settings.include_coins_foliage
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Shuffle Foliage Coins\" setting being turned off"
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in favor_coin_locations
                and not logic_settings.include_coins_favors
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Shuffle Favor Coins\" setting being turned off"
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item.startswith("Shop")
                and not logic_settings.include_shops
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Shopsanity\" setting being turned off"
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item == "HiddenPanel"
                and not logic_settings.include_panels
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Include Hidden Panels\" setting being turned off"
                    )
                current_node.current_item = Item.get(Item.item_name == "StarPiece")
                if (logic_settings.include_shops and logic_settings.progression_on_merlow):
                    current_node.current_item.progression = True
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in kootfavors_reward_locations
                and logic_settings.include_favors_mode == IncludeFavorsMode.NOT_RANDOMIZED
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Koopa Koot Favors\" setting set to \"Vanilla\""
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in kootfavors_keyitem_locations
                and logic_settings.include_favors_mode <= IncludeFavorsMode.RND_REWARD_VANILLA_KEYITEMS
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Koopa Koot Favors\" setting not set to \"Full Shuffle\""
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in chainletter_giver_locations
                and logic_settings.include_letters_mode < IncludeLettersMode.FULL_SHUFFLE
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Letter Delivery Rewards\" setting not set to \"Full Shuffle\""
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id == chainletter_final_reward_location
                and logic_settings.include_letters_mode < IncludeLettersMode.RANDOM_CHAIN_REWARD
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Letter Delivery Rewards\" setting set to \"Vanilla\""
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in simpleletter_locations
                and logic_settings.include_letters_mode < IncludeLettersMode.SIMPLE_LETTERS
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Letter Delivery Rewards\" setting set to \"Vanilla\""
                    )
                current_node.current_item = Item.get(Item.item_name == "StarPiece")
                all_item_nodes.append(current_node)
                continue

            if (    not logic_settings.include_radiotradeevent
                and current_node_id in radio_trade_event_locations
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Trading Event\" setting being turned off"
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in dojo_locations[5] # all dojo locations
                and current_node_id not in dojo_locations[logic_settings.include_dojo]
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Dojo Rewards\" setting being set too low"
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id == "MAC_02/GiftD"
                and logic_settings.foreverforest_open
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Open Forever Forest\" setting being turned on"
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item == "Partner"
                and logic_settings.partner_shuffle == PartnerShuffle.VANILLA
                and current_node.vanilla_item.item_name not in starting_partners
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Partner Shuffle\" setting being set to \"Vanilla\""
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in multicoinblock_locations
                and logic_settings.multicoin_block_shuffle == MultiCoinBlockShuffle.OFF
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Multi Coin Block Shuffle\" setting being set to \"Off\""
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in superblock_locations
                and logic_settings.partner_upgrade_shuffle == PartnerUpgradeShuffle.OFF
                and logic_settings.multicoin_block_shuffle == MultiCoinBlockShuffle.OFF
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Partner Upgrade Shuffle\" setting being set to \"Off\""
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    logic_settings.gear_shuffle_mode == GearShuffleMode.VANILLA
                and current_node.vanilla_item.item_type == "GEAR"
                and (   current_node.identifier != "KMR_04/Bush7_Drop1"
                     or logic_settings.starting_hammer == StartingHammer.HAMMERLESS)
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Gear Shuffle\" setting being set to \"Vanilla\""
                    )
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    logic_settings.gear_shuffle_mode == GearShuffleMode.VANILLA
                and current_node.identifier == "KMR_04/Bush7_Drop1"
            ):
                if current_node_id in all_plando_locations:
                    raise PlandoSettingsMismatchError(
                        "Plandomizer error: An item location is plando'd which clashes "\
                        "with the \"Gear Shuffle\" setting being set to \"Vanilla\""
                    )
                # special casing so the hammer bush is never empty but also
                # never holds required items or badges
                current_node.current_item = _get_random_taycet_item()
                all_item_nodes.append(current_node)
                continue

            if (    not logic_settings.randomize_puzzles
                and current_node.identifier in [
                        "DRO_01/ShopItemB",
                        "DRO_01/ShopItemD",
                        "DRO_01/ShopItemE"
                    ]
            ):
                # no plando exception necessary, because handled by OptionSet.py
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    not logic_settings.shuffle_starbeam
                and current_node.identifier == "HOS_05/GiftA"
            ):
                # no plando exception necessary, because handled by OptionSet.py
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if current_node_id in plando_item_placement:
                item_to_shuffle = current_node.vanilla_item
                if (    item_to_shuffle.item_type == "STARPIECE"
                    and logic_settings.include_shops
                    and logic_settings.progression_on_merlow
                ):
                    item_to_shuffle.progression = True
                add_to_correct_itempool(item_to_shuffle)
                current_node.current_item = plando_item_placement[current_node_id]
                if (    plando_item_placement[current_node_id].item_name in progression_miscitems_names
                    and is_itemlocation_replenishable(current_node)
                ):
                    current_node.current_item.progression = True
                all_item_nodes.append(current_node)
                items_to_remove_from_pools.append(plando_item_placement[current_node_id])
                items_plandod += 1
                continue

            # Check all remaining nodes for items to add to the pools
            all_item_nodes.append(current_node)

            # Special casing for hammer bush during gear location shuffle w/o
            # hammerless: add modified "gear" Tayce T item to gear locations
            if (    current_node.identifier == "KMR_04/Bush7_Drop1"
                and logic_settings.starting_hammer != StartingHammer.HAMMERLESS
                and logic_settings.gear_shuffle_mode == GearShuffleMode.GEAR_LOCATION_SHUFFLE
            ):
                modified_taycet = _get_random_taycet_item()
                modified_taycet.item_type = "GEAR"
                pool_progression_items.append(modified_taycet)
                continue

            # Item shall be randomized: Add it to the correct item pool
            item_to_shuffle = current_node.vanilla_item
            if (    item_to_shuffle.item_type == "STARPIECE"
                and logic_settings.include_shops
                and logic_settings.progression_on_merlow
            ):
                item_to_shuffle.progression = True
            add_to_correct_itempool(item_to_shuffle)


    target_itempool_size = (
        len(pool_progression_items)
        + len(pool_misc_progression_items)
        + len(pool_coins_only)
        + len(pool_illogical_consumables)
        + len(pool_badges)
        + len(pool_other_items)
        - items_plandod
    )

    # Make sure that every vanilla badge is in the item pool, regardless of
    # chosen settings
    for vanilla_badge in (
        Item
        .select()
        .where(Item.item_type == "BADGE")
        .where(Item.unused == False)
        .where(Item.unplaceable == False)
        .where(~(Item.item_name % "*Proxy*"))
    ):
        if (    vanilla_badge not in pool_badges
            and vanilla_badge not in pool_progression_items
        ):
            pool_badges.append(vanilla_badge)

    # Add Power Stars, if needed
    if logic_settings.star_hunt_total > 0:
        stars_added = 0
        for power_star_item in (
            Item
            .select()
            .where(
                Item.item_name % "PowerStar*"
            )
        ):
            if stars_added >= logic_settings.star_hunt_total:
                break

            pool_progression_items.append(power_star_item)
            stars_added += 1

    # Add Item Pouches, if needed
    if logic_settings.add_item_pouches:
        pouch_items = [
            Item.get(Item.item_name == "PouchA"),
            Item.get(Item.item_name == "PouchB"),
            Item.get(Item.item_name == "PouchC"),
            Item.get(Item.item_name == "PouchD"),
            Item.get(Item.item_name == "PouchE"),
        ]

        pool_other_items.extend(pouch_items)

    # Add unused badge duplicates, if needed
    if logic_settings.add_unused_badge_duplicates:
        unused_badge_duplicates = []
        for item in Item.select().where(Item.unused_duplicates == True):
            unused_badge_duplicates.append(item)

        pool_badges.extend(unused_badge_duplicates)

    # Add beta items, if needed
    if logic_settings.add_beta_items:
        beta_items = []
        for item in Item.select().where(Item.unused_duplicates == False).where(Item.unused == True):
            beta_items.append(item)

        pool_badges.extend(beta_items)

    # Add progressive badges, if needed
    if logic_settings.progressive_badges:
        new_badges = []
        for item in Item.select().where(Item.item_name.in_(progressive_badges)):
            new_badges.append(item)

        pool_badges.extend(new_badges)

    # If we start jumpless, add a progressive boots item to the item pool
    if logic_settings.starting_boots == StartingBoots.JUMPLESS:
        new_boots = Item.get(Item.item_name == "BootsProxy1")

        pool_progression_items.append(new_boots)

    # If we shuffle partner upgrades, add upgrade items to the item pool
    if do_partner_upgrade_shuffle:
        for item in (Item
                     .select()
                     .where(Item.item_type == "PARTNERUPGRADE")
                     .where(Item.unplaceable != 1)
                     .where(Item.item_name != "GenericUpgrade")
        ):
            pool_other_items.append(item)

    # Adjust item pools based on settings
    items_to_remove_from_pools.extend(get_items_to_exclude(
        logic_settings,
        starting_partners,
        do_partner_upgrade_shuffle
    ))
    items_to_remove_from_pools.extend(starting_items)

    while items_to_remove_from_pools:
        item = items_to_remove_from_pools.pop()
        if item in pool_progression_items:
            pool_progression_items.remove(item)
            continue
        if item in pool_misc_progression_items and item.progression:
            pool_misc_progression_items.remove(item)
            continue
        if item in pool_badges:
            pool_badges.remove(item)
            continue
        if item in pool_other_items:
            pool_other_items.remove(item)
            continue
        if item in pool_coins_only:
            pool_coins_only.remove(item)
            continue
        if item in pool_illogical_consumables:
            pool_illogical_consumables.remove(item)
            continue
        #if not item.is_trapped():
        #    print(f"Attempted to remove {item} from item pools, but no pool holds such item.")
    # If we have set a badge pool limit and exceed that, remove random badges
    # until that condition is satisfied
    if len(pool_badges) > logic_settings.badge_pool_limit:
        random.shuffle(pool_badges)
        while len(pool_badges) > logic_settings.badge_pool_limit:
            pool_badges.pop()

    # If the item pool is the wrong size now, fix it by filling up or clearing
    # out items
    cur_itempool_size = (
        len(pool_progression_items)
        + len(pool_misc_progression_items)
        + len(pool_coins_only)
        + len(pool_illogical_consumables)
        + len(pool_badges)
        + len(pool_other_items)
    )

    while target_itempool_size > cur_itempool_size:
        pool_illogical_consumables.append(_get_random_taycet_item())
        cur_itempool_size += 1

    if target_itempool_size < cur_itempool_size:
        random.shuffle(pool_illogical_consumables)
        while target_itempool_size < cur_itempool_size:
            if len(pool_coins_only) > 20 or len(pool_illogical_consumables) == 0:
                trashable_items = pool_coins_only
            else:
                trashable_items = pool_illogical_consumables
            try:
                trashable_items.pop()
                cur_itempool_size -= 1
            except IndexError:
                raise ItemPoolTooSmallError()

    # Randomize consumables if needed
    pool_illogical_consumables = get_randomized_itempool(
        pool_illogical_consumables,
        logic_settings.randomize_consumable_mode,
        logic_settings.item_quality,
        logic_settings.add_beta_items,
    )

    # Swap plandomizer placeholders for concrete items
    # "Consumable"s and "NonProgression" should be randomly picked from
    # pool_illogical_consumables and pool_illogical_consumables+pool_badges
    # respectively, while traps should be handled by get_trapped_itempool
    resolved_item_placeholders: dict[str, Item] = dict()
    if len(plando_item_placeholders) > 0:
        for node_id, placeholder in plando_item_placeholders.items():
            possible_items = deepcopy(pool_illogical_consumables)
            if placeholder == "NonProgression":
                possible_items.extend(deepcopy(pool_badges))
                possible_items.extend(deepcopy(pool_coins_only))

            if len(possible_items) > 0:
                resolved_placeholder = deepcopy(random.choice(possible_items))
            else:
                resolved_placeholder = _get_random_taycet_item()
            resolved_item_placeholders[node_id] = resolved_placeholder

            if resolved_placeholder in pool_illogical_consumables:
                pool_illogical_consumables.remove(resolved_placeholder)
            elif resolved_placeholder in pool_badges:
                pool_badges.remove(resolved_placeholder)
            elif resolved_placeholder in pool_coins_only:
                pool_coins_only.remove(resolved_placeholder)

    # Re-join the non-required items into one array
    pool_other_items.extend(pool_coins_only)
    pool_other_items.extend(pool_illogical_consumables)
    pool_other_items.extend(pool_badges)

    pool_other_items, resolved_trap_placeholders = get_trapped_itempool(
        itempool = pool_other_items,
        trap_mode = logic_settings.itemtrap_mode,
        randomize_favors_mode = logic_settings.include_favors_mode,
        do_randomize_dojo = logic_settings.include_dojo,
        keyitems_outside_dungeon = logic_settings.keyitems_outside_dungeon,
        power_star_hunt = (logic_settings.star_hunt_total > 0),
        add_beta_items = logic_settings.add_beta_items,
        do_partner_upgrade_shuffle = do_partner_upgrade_shuffle,
        already_placed_traps_count = plando_traps_placed,
        plando_trap_placeholders = plando_trap_placeholders,
    )

    return pool_other_items, resolved_item_placeholders, resolved_trap_placeholders


def find_available_nodes(
    world_graph,
    starting_node_id,
    mario
):
    reachable_node_ids = set()
    non_traversable_edges = dict()

    reachable_node_ids.add(starting_node_id)
    non_traversable_edges[starting_node_id] = [
        edge["edge_id"] for edge in world_graph[starting_node_id]["edge_list"]
    ]

    empty_reachables = find_empty_reachable_nodes(
        world_graph,
        reachable_node_ids,
        non_traversable_edges,
        mario
    )

    return empty_reachables


def find_empty_reachable_nodes(
    world_graph:dict,
    reachable_node_ids:set,
    non_traversable_edges:dict, # dict of node_id to list(edge_id)
    mario:MarioInventory
):
    """
    Try to traverse already found edges which could not be traversed before.
    This re-traversing is accomplished by calling DFS on each respective edge's
    origin node ("from-node").
    """
    #logging.debug("++++ find_empty_reachable_nodes called")
    reachable_item_nodes = {} # < hmmm
    filled_item_node_ids = set()
    empty_item_nodes = [] # [] of Node
    checked_item_node_ids = set() # set() of str()
    while True:
        found_new_items = False

        # Re-traverse already found edges which could not be traversed before.
        for from_node_id in set(non_traversable_edges):
            found_additional_items, mario = _depth_first_search(
                from_node_id,
                world_graph,
                reachable_node_ids,
                reachable_item_nodes,
                non_traversable_edges,
                mario
            )
            found_new_items = found_new_items or found_additional_items

        # Check if an item node is reachable which already has an item placed.
        for node_id in (reachable_item_nodes.keys() - checked_item_node_ids):
            item_node = reachable_item_nodes[node_id]
            current_item = item_node.current_item
            if current_item:
                if current_item.progression:
                    mario.add(current_item.item_name)
                    found_new_items = True
                filled_item_node_ids.add(node_id)

            checked_item_node_ids.add(node_id)

        # Keep searching for new edges and nodes until we don't find any new
        # items which might open up even more edges and nodes
        if not found_new_items:
            break

    for node_id, item_node in sorted(reachable_item_nodes.items()):
        if node_id not in filled_item_node_ids:
            empty_item_nodes.append(item_node)

    return empty_item_nodes


def _algo_assumed_fill(
    item_placement,
    logic_settings:LogicOptionSet,
    starting_partners,
    hidden_block_mode:int,
    starting_items:list,
    world_graph,
    plando_item_placement: dict[str | Item] | None,
    plando_traps_placed: int,
    plando_item_placeholders: dict[str, str],
    plando_trap_placeholders: list[str],
    is_progression_plandod: bool,
):

    # Declare and init additional data structures
    ## Data structures for graph traversal
    all_item_nodes = []
    ## Data structures for item pool
    pool_progression_items = []
    pool_other_items = []
    pool_misc_progression_items = []

    # Clean out plando'd locations for item placeholders and trap placeholders
    # which aren't actually part of the world graph (e.g. BowserCastleMode)
    remove_from_placeholders: list[str] = []
    for node_id in plando_item_placeholders:
        if node_id not in world_graph:
            remove_from_placeholders.append(node_id)
    for node_id in remove_from_placeholders:
        plando_item_placeholders.pop(node_id)
    remove_from_placeholders: list[str] = []
    for node_id in plando_trap_placeholders:
        if node_id not in world_graph:
            remove_from_placeholders.append(node_id)
    for node_id in remove_from_placeholders:
        plando_trap_placeholders.pop(node_id)

    # Generate item pool
    print("Generating item pool...")
    pool_other_items, resolved_item_placeholders, resolved_trap_placeholders = _generate_item_pools(
        world_graph,
        pool_progression_items,
        pool_misc_progression_items,
        pool_other_items,
        all_item_nodes,
        logic_settings,
        starting_items,
        starting_partners,
        (logic_settings.partner_upgrade_shuffle != PartnerUpgradeShuffle.OFF),
        plando_item_placement,
        plando_traps_placed,
        plando_item_placeholders,
        plando_trap_placeholders,
    )

    # Pre-place plando'd generic placeholder items "Consumable",
    # "NonProgression", and "TRAP", which have been resolved to actual items
    for node_id, item_obj in resolved_item_placeholders.items():
        world_graph[node_id]["node"].current_item = item_obj
    for node_id, item_obj in resolved_trap_placeholders.items():
        world_graph[node_id]["node"].current_item = item_obj


    starting_node_id = get_startingnode_id_from_startingmap_id(
        logic_settings.starting_map,
    )

    # If we have any items plando'd that can influence progression in any way:
    # Run a sanity pre-check of the world graph with all not plando'd items
    # as starting items, just to make sure the plando isn't impossible to begin
    # with
    if is_progression_plandod:
        all_progression_yet_to_be_placed: list = []
        all_progression_yet_to_be_placed.extend(pool_progression_items)
        all_progression_yet_to_be_placed.extend(pool_misc_progression_items)

        mario = MarioInventory(
            logic_settings.starting_boots,
            logic_settings.starting_hammer,
            starting_partners,
            starting_items,
            logic_settings.partners_always_usable,
            logic_settings.hidden_block_mode,
            logic_settings.magical_seeds_required,
            logic_settings.prologue_open,
            logic_settings.bluehouse_open,
            logic_settings.mtrugged_open,
            logic_settings.foreverforest_open,
            logic_settings.toybox_open,
            logic_settings.whale_open,
            logic_settings.ch7_bridge_visible,
            logic_settings.always_speedyspin,
            logic_settings.cook_without_fryingpan,
            vanilla_start=False,
        )
        for item in all_progression_yet_to_be_placed:
            mario.add(item.item_name)

        # Find reachable nodes within the world graph
        _ = find_available_nodes(
            world_graph,
            starting_node_id,
            mario
        )

        if "YOUWIN" not in mario.items:
            unreachable_items: list = list()
            for location, unreachable_item in [
                (location, item.item_name) for location, item in plando_item_placement.items()
                if     item.item_name not in mario.items
                   and item.item_name not in mario.partners
                   and item.item_name not in mario.boots
                   and item.item_name not in mario.hammer
                   and item.item_name not in mario.starpieces
                   and item.item_name not in mario.powerstars
                   and item.progression
                   and not item.is_trapped()
            ]:
                loc_area = verbose_area_names[location[:3]]
                loc_map = Node.get(Node.identifier == location).map_area.verbose_name
                verbose_location = verbose_item_locations[location.split("/")[0]][location.split("/")[1]]
                verbose_location = verbose_location.replace("'", "")
                unreachable_items.append((
                    f"{loc_area}: {loc_map} - {verbose_location}",
                    unreachable_item
                ))
            raise UnbeatablPlandoPlacementError(
                "Plandomizer error: Could not build beatable seed! "
                f"Progression logically unreachable: {unreachable_items}"
            )

    if logic_settings.randomize_puzzles and logic_settings.include_shops:
        # Check which slots are pre-filled, if any
        filled_slots: list[str] = list()
        shop_code_candidates: set[str] = set()

        shop_array = ["ShopItemA","ShopItemB","ShopItemC","ShopItemD","ShopItemE","ShopItemF"]
        for slot_id in shop_array:
            slot_item = world_graph[f"DRO_01/{slot_id}"]["node"].current_item
            if slot_item is not None:
                filled_slots.append(slot_id)
                if slot_item.item_type in ["ITEM","COIN"] and slot_item.base_price <= 10:
                    shop_code_candidates.add(slot_item.item_name)
        missing_code_candidates_cnt: int = (3 - len(shop_code_candidates))

        if (    len(filled_slots) < 6 # there are slots left to fill
            and len(shop_code_candidates) < 3 # we don't have 3 elligible consumables yet
            and len(filled_slots) + missing_code_candidates_cnt <= 6
            # do we even have enough slots left to get to 3 consumables
        ):
            # Force at least 3 different non-uniques into the Dry Dry Outpost shop
            # which are at least somewhat affordable
            affordable_nonuniques = set([
                x for x in pool_other_items
                if    (x.item_type == "ITEM" and x.base_price <= 10 and x.value <= 0xFF)
                #      consumable                affordable             not the berry keys
                   or x.item_type == "COIN"
            ])
            unique_nonuniques = sorted(list(dict.fromkeys(affordable_nonuniques)))

            manual_shop_fill_count: int = 0
            if len(unique_nonuniques) < missing_code_candidates_cnt:
                # We might have to place progression consumables here if the item
                # pool is too small, for example during "mystery only"
                try:
                    unique_nonuniques.extend(
                        random.sample(
                            pool_misc_progression_items,
                            k=missing_code_candidates_cnt - len(unique_nonuniques)
                        )
                    )
                except ValueError:
                    # Plando has already placed any item we could have as part of
                    # the shop code, so we have to fill it with more items out
                    # of thin air
                    if len(unique_nonuniques) < missing_code_candidates_cnt:
                        unique_nonuniques.append(Item.get(Item.item_name == "StinkyHerb"))
                        manual_shop_fill_count += 1
                    if len(unique_nonuniques) < missing_code_candidates_cnt:
                        unique_nonuniques.append(Item.get(Item.item_name == "Pebble"))
                        manual_shop_fill_count += 1
                    if len(unique_nonuniques) < missing_code_candidates_cnt:
                        unique_nonuniques.append(Item.get(Item.item_name == "Mistake"))
                        manual_shop_fill_count += 1

            shop_code_items = random.sample(unique_nonuniques, k=missing_code_candidates_cnt)
            for i, shop_code_item in enumerate(shop_code_items):
                # check if some of the consumables are relevant to progression
                # if so, then remove them from the misc progression instead
                try:
                    if shop_code_item in pool_misc_progression_items:
                        pool_misc_progression_items.remove(shop_code_item)
                        shop_code_items[i].progression = True
                    else:
                        pool_other_items.remove(shop_code_item)
                except ValueError:
                    if manual_shop_fill_count > 0:
                        manual_shop_fill_count -= 1
                    else:
                        raise

            # avoid item object references
            copied_shop_code_items = []
            for item in shop_code_items:
                copied_shop_code_items.append(deepcopy(item))

            # place into random dro shop slots
            shop_slot_ids = random.sample(
                population=[x for x in shop_array if world_graph[f"DRO_01/{x}"]["node"].current_item is None],
                k=missing_code_candidates_cnt
            )
            while shop_slot_ids:
                slot_id = shop_slot_ids.pop()
                shop_code_item = copied_shop_code_items.pop()
                world_graph[f"DRO_01/{slot_id}"]["node"].current_item = shop_code_item


    # Place CoinBag items into MultiCoinBlock locations if necessary
    candidate_locations = multicoinblock_locations.copy()
    candidate_locations.extend(superblock_locations.copy())
    # Remove locations that may have a partner upgrade item placed by
    # the PartnerUpgradeShuffle.OFF option
    candidate_locations = [
        x for x in candidate_locations
        if world_graph[x]["node"].current_item is None
    ]
    if logic_settings.multicoin_block_shuffle == MultiCoinBlockShuffle.SHUFFLE:
        coinbag_itemobj = Item.get(Item.item_name == "CoinBag")
        while coinbag_itemobj in pool_other_items:
            random_block_location = random.choice(candidate_locations)
            world_graph[random_block_location]["node"].current_item = coinbag_itemobj
            candidate_locations.remove(random_block_location)
            pool_other_items.remove(coinbag_itemobj)
    if logic_settings.multicoin_block_shuffle >= MultiCoinBlockShuffle.SHUFFLE:
        # If PartnerUpgradeShuffle is turned off, we now need to also place
        # the GenericUpgrade items into the remaining random block locations.
        # If PartnerUpgradeShuffle is not turned off, then we don't have
        # any GenericUpgrade items to place within the item pool
        genericupgrade_itemobj = Item.get(Item.item_name == "GenericUpgrade")
        while genericupgrade_itemobj in pool_other_items:
            random_block_location = random.choice(candidate_locations)
            world_graph[random_block_location]["node"].current_item = genericupgrade_itemobj
            candidate_locations.remove(random_block_location)
            pool_other_items.remove(genericupgrade_itemobj)

    # Place Partner Upgrade items into random block locations if necessary:
    if logic_settings.partner_upgrade_shuffle == PartnerUpgradeShuffle.SUPERBLOCKLOCATIONS:
        candidate_locations = multicoinblock_locations.copy()
        candidate_locations.extend(superblock_locations.copy())
        # Remove locations that may have a CoinBag item placed by
        # the MultiCoinBlockShuffle.SHUFFLE option
        candidate_locations = [
            x for x in candidate_locations
            if world_graph[x]["node"].current_item is None
        ]
        partner_upgrades = [
            x for x in pool_other_items
            if     x.item_type == "PARTNERUPGRADE"
               and x.item_name != "GenericUpgrade"
               and not x.is_trapped()
        ]
        random.shuffle(partner_upgrades)
        while partner_upgrades:
            random_block_location = random.choice(candidate_locations)
            partner_upgrade_itemobj = partner_upgrades.pop()
            world_graph[random_block_location]["node"].current_item = partner_upgrade_itemobj
            candidate_locations.remove(random_block_location)
            pool_other_items.remove(partner_upgrade_itemobj)


    print("Placing progression items...")
    #Place progression items, both key and replenishable
    pool_combined_progression_items = pool_progression_items + pool_misc_progression_items
    random.shuffle(pool_combined_progression_items)

    dungeon_restricted_items = {}
    if not logic_settings.keyitems_outside_dungeon:
        for dungeon in limited_by_item_areas:
            for itemlist in limited_by_item_areas[dungeon].values():
                for item in itemlist:
                    assert item not in dungeon_restricted_items
                    dungeon_restricted_items[item] = dungeon
        pool_combined_progression_items.sort(key=lambda x: x.item_name in dungeon_restricted_items.keys())

    if (   logic_settings.gear_shuffle_mode == GearShuffleMode.GEAR_LOCATION_SHUFFLE
        or logic_settings.starting_hammer == StartingHammer.HAMMERLESS
        or logic_settings.starting_boots == StartingBoots.JUMPLESS
    ):
        pool_combined_progression_items.sort(key=lambda x: x.item_type == "GEAR")

    if logic_settings.partner_shuffle == PartnerShuffle.SHUFFLED:
        pool_combined_progression_items.sort(
            key = lambda x: x.item_name in all_partners
        )

    while pool_combined_progression_items:
        item = pool_combined_progression_items.pop()
        mario = MarioInventory(
            logic_settings.starting_boots,
            logic_settings.starting_hammer,
            starting_partners,
            starting_items,
            logic_settings.partners_always_usable,
            logic_settings.hidden_block_mode,
            logic_settings.magical_seeds_required,
            logic_settings.prologue_open,
            logic_settings.bluehouse_open,
            logic_settings.mtrugged_open,
            logic_settings.foreverforest_open,
            logic_settings.toybox_open,
            logic_settings.whale_open,
            logic_settings.ch7_bridge_visible,
            logic_settings.always_speedyspin,
            logic_settings.cook_without_fryingpan,
            vanilla_start=False
        )

        for item_ in pool_combined_progression_items:
            mario.add(item_.item_name)

        candidate_locations = find_available_nodes(
            world_graph,
            starting_node_id,
            mario
        )

        if item.item_name in progression_miscitems_names:
            candidate_locations = [node for node in candidate_locations if is_itemlocation_replenishable(node)]

        if item.item_name in dungeon_restricted_items:
            dungeon = dungeon_restricted_items[item.item_name]
            candidate_locations = [
                node for node in candidate_locations
                if (    node.identifier[:3] == dungeon
                    and node.identifier != "TRD_00/ChestB" # not chest on Koopa Fortress ledge
                )
            ]
            dungeon_restricted_items.pop(item.item_name)

        if logic_settings.partner_shuffle == PartnerShuffle.SHUFFLED:
            if item.item_type == "PARTNER":
                candidate_locations = [
                    node for node in candidate_locations
                    if node.vanilla_item.item_type == "PARTNER"
                ]
            else:
                candidate_locations = [
                    node for node in candidate_locations
                    if node.vanilla_item.item_type != "PARTNER"
                ]

        if logic_settings.gear_shuffle_mode == GearShuffleMode.GEAR_LOCATION_SHUFFLE:
            # Note: Boots 1 (Jumpless start) has to be placed elsewhere, as all
            # gear locations are unreachable otherwise
            if item.item_type == "GEAR" and item.item_name != "BootsProxy1":
                candidate_locations = [node for node in candidate_locations if node.vanilla_item.item_type == "GEAR"]
            else:
                candidate_locations = [node for node in candidate_locations if node.vanilla_item.item_type != "GEAR"]


        if len(candidate_locations) == 0:
            raise UnbeatableSeedError("Failed to generate a beatable seed")

        placement_location = random.choice(candidate_locations)
        placement_location.current_item = item

    # Place all remaining items into still empty item nodes
    print("Placing Miscellaneous Items ...")
    random.shuffle(pool_other_items)

    # Sort so shop nodes are in front to make sure those are filled with
    # non-traps
    all_item_nodes.sort(key=lambda x: x.is_shop(), reverse=True)

    for item_node in all_item_nodes:
        if item_node.current_item:
            continue
        item_node_id = item_node.identifier

        if (    item_node_id == "KMR_06/ItemA"
            and (   logic_settings.include_coins_overworld
                 or logic_settings.include_coins_blocks
                 or logic_settings.include_coins_foliage
                 or logic_settings.include_coins_favors)
        ):
            # Do not put coin on the Goomba Road sign due to glitchy graphics
            item_index = -1
            for i_item, item in enumerate(pool_other_items):
                if item.item_name != "Coin":
                    item_index = i_item
                    break

            if item_index == -1:
                # No non-coin item in item-pool: Just place a Mushroom
                pool_other_items.pop()
                random_item = Item.get(Item.item_name == "Mushroom")
            else:
                random_item = pool_other_items.pop(item_index)

            item_node.current_item = random_item
            #logging.debug("%s: %s", item_node_id, random_item.item_name)

        else:
            # Place random remaining item here
            try:
                random_item = pool_other_items.pop()

                if "Shop" in item_node_id or item_node_id in exclude_from_trap_placement:
                    # Do not put item traps into shops or underwater -> it breaks otherwise!
                    while random_item.is_trapped():
                        pool_other_items.insert(0, random_item)
                        random_item = pool_other_items.pop()

                item_node.current_item = random_item
                #logging.debug("%s: %s", item_node_id, random_item.item_name)

            except ValueError as err:
                #logging.warning("pool_other_items size: %d", len(pool_other_items))
                #raise
                item_node.current_item = item_node.vanilla_item
                #logging.warning("%s", item_node_id)

    # "Return" list of modified item nodes
    item_placement.extend([node for node in all_item_nodes if node.current_item])


def get_item_spheres(
    item_placement,
    logic_settings:LogicOptionSet,
    starting_partners,
    hidden_block_mode:int,
    starting_items:list,
    world_graph,
) -> dict:
    """
    Builds and returns a dictionary containing progression spheres and their
    items, showing a possible way of tracing a playthrough.
    """

    # Declare and init additional data structures
    ## Data structures for graph traversal
    reachable_node_ids = set()
    reachable_item_nodes = {}
    non_traversable_edges = dict()
    ## Data structure for sphere information
    spheres_dict = dict()

    print("Gathering Item Spheres Data")

    # Set node to start graph traversal from
    starting_node_id = get_startingnode_id_from_startingmap_id(
        logic_settings.starting_map,
    )

    # Find initially reachable nodes within the world graph
    non_traversable_edges[starting_node_id] = [
        edge["edge_id"] for edge in world_graph[starting_node_id]["edge_list"]
    ]

    reachable_node_ids.add(starting_node_id)

    vanilla_start = (
            starting_node_id == "KMR_02/1"
        and not logic_settings.shuffle_items
        and logic_settings.starting_hammer == StartingHammer.HAMMERLESS
        and "Bombette" not in starting_partners
        and not logic_settings.partners_always_usable
    )

    # Init Mario Inventory
    mario = MarioInventory(
        logic_settings.starting_boots,
        logic_settings.starting_hammer,
        starting_partners,
        starting_items,
        logic_settings.partners_always_usable,
        logic_settings.hidden_block_mode,
        logic_settings.magical_seeds_required,
        logic_settings.prologue_open,
        logic_settings.bluehouse_open,
        logic_settings.mtrugged_open,
        logic_settings.foreverforest_open,
        logic_settings.toybox_open,
        logic_settings.whale_open,
        logic_settings.ch7_bridge_visible,
        logic_settings.always_speedyspin,
        logic_settings.cook_without_fryingpan,
        vanilla_start
    )

    # Add starting items
    spheres_dict["starting_items"] = []

    for item in mario.item_history:
        item_suffix = ""
        item = item[1:] # Remove the trailing + from items in initial mario history
        if item in progression_items.values() or item in progression_miscitems_names:
            item_suffix = "*"

        spheres_dict["starting_items"].append(f"{item}{item_suffix}")

    if logic_settings.starting_boots == StartingBoots.ULTRABOOTS:
        spheres_dict["starting_items"].append("ProgressiveBoots*")
    if logic_settings.starting_boots >= StartingBoots.SUPERBOOTS:
        spheres_dict["starting_items"].append("ProgressiveBoots*")
    if logic_settings.starting_boots >= StartingBoots.BOOTS:
        spheres_dict["starting_items"].append("ProgressiveBoots*")

    if logic_settings.starting_hammer == StartingHammer.ULTRAHAMMER:
        spheres_dict["starting_items"].append("ProgressiveHammer*")
    if logic_settings.starting_hammer >= StartingHammer.SUPERHAMMER:
        spheres_dict["starting_items"].append("ProgressiveHammer*")
    if logic_settings.starting_hammer >= StartingHammer.HAMMER:
        spheres_dict["starting_items"].append("ProgressiveHammer*")

    # Scan spheres
    item_placement_map = {}
    for n in item_placement:
        item_placement_map[n.identifier] = n

    cur_sphere = 0
    while item_placement_map:
        (
            reachable_node_ids,
            reachable_item_nodes,
            non_traversable_edges,
            mario
        ) = _find_new_nodes_and_edges(
            world_graph,
            reachable_node_ids,
            reachable_item_nodes,
            non_traversable_edges,
            mario
        )

        if reachable_item_nodes:
            item_spheres_text = f"sphere_{cur_sphere}"
            nodes_to_print = list(reachable_item_nodes.values())
        else:
            item_spheres_text = "unreachable_in_logic"
            nodes_to_print = list(item_placement_map.values())

        nodes_to_print.sort(key=lambda node: \
            (node.map_area.area_id, node.map_area.map_id, node.identifier)
        )

        for node in nodes_to_print:
            if item_spheres_text not in spheres_dict:
                spheres_dict[item_spheres_text] = dict()

            item = item_placement_map.pop(node.identifier).current_item

            area = verbose_area_names[node.map_area.name[:3]]
            area = area.replace("'", "")
            map = (node.map_area.verbose_name)
            map = map.replace("'", "")
            item_location = verbose_item_locations[node.map_area.name][node.key_name_item]
            item_location = item_location.replace("'", "")

            if area not in spheres_dict[item_spheres_text]:
                spheres_dict[item_spheres_text][area] = dict()
            area_dict = spheres_dict[item_spheres_text][area]

            full_location = f"{map} - {item_location}"
            if item.item_name in verbose_item_names:
                item_name = verbose_item_names[item.item_name]
            elif (    item.item_name == "CoinBag"
                  and (   node.identifier in superblock_locations
                       or node.identifier in multicoinblock_locations)
            ):
                # CoinBag in random block location turns that location into a
                # MultiCoinBlock
                item_name = "MultiCoinBlock"
            else:
                item_name = item.item_name

            if item.is_trapped():
                item_name = f"TRAP ({item_name})"
            else:
                item_suffix = ""
                if item.item_type != "ITEM" or is_itemlocation_replenishable(node):
                    if (    f"+{item.item_name}" not in mario.item_history
                        and (   item.item_name in progression_items.values()
                             or item.item_name in progression_miscitems_names
                             or item.item_type == 'GEAR'
                             or item.item_type == 'POWERSTAR')
                    ):
                        item_suffix = "*"
                    mario.add(item.item_name)

                item_name = f"{item_name}{item_suffix}"

            area_dict[full_location] = item_name

        reachable_item_nodes.clear()
        cur_sphere += 1

    assert "YOUWIN" in mario.items

    return spheres_dict


def place_items(
    item_placement,
    logic_settings:LogicOptionSet,
    starting_partners,
    hidden_block_mode:int,
    starting_items:list,
    plando_item_placeholders: dict[str, str],
    plando_trap_placeholders: list[str],
    world_graph = None,
    plando_item_placement: dict[str, Item] | None = None,
    plando_traps_placed: int = 0,
    is_progression_plandod: bool = False,
):
    """Places items into item locations according to chosen settings."""
    #level = logging.INFO
    #fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    #logging.basicConfig(level=level, format=fmt)

    if not logic_settings.shuffle_items:
        # Place items in their vanilla locations
        for node in Node.select().where(Node.key_name_item.is_null(False)):
            node.current_item = node.vanilla_item
            item_placement.append(node)
            # Also write the DRO shop items into the world graph, otherwise
            # "random puzzles" won't work
            if node.identifier in [
                "DRO_01/ShopItemA", "DRO_01/ShopItemB", "DRO_01/ShopItemC",
                "DRO_01/ShopItemD", "DRO_01/ShopItemE", "DRO_01/ShopItemF"
            ]:
                world_graph[node.identifier]["node"].current_item = node.vanilla_item
    else:
        # Place items in a backward fill, ensuring a maximally deep fill.
        _algo_assumed_fill(
            item_placement,
            logic_settings,
            starting_partners,
            hidden_block_mode,
            starting_items,
            world_graph,
            plando_item_placement,
            plando_traps_placed,
            plando_item_placeholders,
            plando_trap_placeholders,
            is_progression_plandod,
        )
