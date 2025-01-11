"""
This modules offers the randomization logic and takes care of actually randomizing
the game according to the settings chosen.
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
    PartnerShuffle,
    DojoShuffle,
)

from rando_modules.modify_itempool \
    import get_randomized_itempool,\
           get_trapped_itempool

from rando_modules.unbeatable_seed_error import UnbeatableSeedError
from rando_modules.item_pool_too_small_error import ItemPoolTooSmallError

from metadata.itemlocation_replenish import replenishing_itemlocations
from metadata.itemlocation_special import \
    kootfavors_reward_locations,          \
    kootfavors_keyitem_locations,         \
    chainletter_giver_locations,          \
    chainletter_final_reward_location,    \
    simpleletter_locations,               \
    radio_trade_event_locations,          \
    dojo_locations,                       \
    limited_by_item_areas,                \
    bush_tree_coin_locations,             \
    overworld_coin_locations,             \
    block_coin_locations,                 \
    favor_coin_locations
from metadata.progression_items                                 \
    import progression_miscitems as progression_miscitems_names, \
           progression_items
from metadata.item_exclusion \
    import exclude_due_to_settings, exclude_from_taycet_placement
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
):
    """
    Generates item pools for items to be shuffled (depending on chosen
    settings this may exclude certain items). The item pools generated are
    pool_progression_items (keyitems that influence progression),
    pool_misc_progression_items (non-keyitems that influence progression) and
    pool_other_items (every other item). Additionally marks item nodes that
    shall not be randomized as already filled.
    """
    pool_coins_only = []
    pool_illogical_consumables = []
    pool_badges = []

    def add_to_correct_itempool(
        new_item: Item,
    ):
        if (new_item.progression
        or (logic_settings.include_shops and "StarPiece" in new_item.item_name)
        or new_item.item_type == "GEAR"
        ):
            pool_progression_items.append(new_item)
        else:
            if (    new_item.item_name in progression_miscitems_names
                and new_item not in pool_misc_progression_items
            ):
                # Since progression misc items have to be placed in
                # replenishable locations, we only need one of each
                pool_misc_progression_items.append(new_item)
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
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in block_coin_locations
                and not logic_settings.include_coins_blocks
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in bush_tree_coin_locations
                and not logic_settings.include_coins_foliage
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in favor_coin_locations
                and not logic_settings.include_coins_favors
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item.startswith("Shop")
                and not logic_settings.include_shops
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item == "HiddenPanel"
                and not logic_settings.include_panels
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in kootfavors_reward_locations
                and logic_settings.include_favors_mode == IncludeFavorsMode.NOT_RANDOMIZED
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in kootfavors_keyitem_locations
                and logic_settings.include_favors_mode <= IncludeFavorsMode.RND_REWARD_VANILLA_KEYITEMS
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in chainletter_giver_locations
                and logic_settings.include_letters_mode < IncludeLettersMode.FULL_SHUFFLE
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id == chainletter_final_reward_location
                and logic_settings.include_letters_mode < IncludeLettersMode.RANDOM_CHAIN_REWARD
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in simpleletter_locations
                and logic_settings.include_letters_mode < IncludeLettersMode.SIMPLE_LETTERS
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    not logic_settings.include_radiotradeevent
                and current_node_id in radio_trade_event_locations
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in dojo_locations[5] # all dojo locations
                and current_node_id not in dojo_locations[logic_settings.include_dojo]
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id == "MAC_02/GiftD"
                and logic_settings.foreverforest_open
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item == "Partner"
                and logic_settings.partner_shuffle == PartnerShuffle.VANILLA
                and current_node.vanilla_item.item_name not in starting_partners
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    logic_settings.gear_shuffle_mode == GearShuffleMode.VANILLA
                and current_node.vanilla_item.item_type == "GEAR"
                and (   current_node.identifier != "KMR_04/Bush7_Drop1"
                     or logic_settings.starting_hammer == StartingHammer.HAMMERLESS)
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    logic_settings.gear_shuffle_mode == GearShuffleMode.VANILLA
                and current_node.identifier == "KMR_04/Bush7_Drop1"
            ):
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
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    not logic_settings.shuffle_starbeam
                and current_node.identifier == "HOS_05/GiftA"
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
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
            add_to_correct_itempool(current_node.vanilla_item)


    target_itempool_size = (
        len(pool_progression_items)
        + len(pool_misc_progression_items)
        + len(pool_coins_only)
        + len(pool_illogical_consumables)
        + len(pool_badges)
        + len(pool_other_items)
    )

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
        for item in Item.select().where(Item.item_type == "PARTNERUPGRADE").where(Item.unplaceable != 1):
            pool_other_items.append(item)

    # Adjust item pools based on settings
    items_to_remove_from_pools = get_items_to_exclude(
        logic_settings,
        starting_partners,
        do_partner_upgrade_shuffle
    )
    items_to_remove_from_pools.extend(starting_items)

    while items_to_remove_from_pools:
        item = items_to_remove_from_pools.pop()
        if item in pool_progression_items:
            pool_progression_items.remove(item)
            continue
        if item in pool_misc_progression_items:
            pool_misc_progression_items.remove(item)
            continue
        if item in pool_badges:
            pool_badges.remove(item)
            continue
        if item in pool_other_items:
            pool_other_items.remove(item)
            continue
        #logging.info("Attempted to remove %s from item pools, but no pool holds such item.", item)

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
            if len(pool_coins_only) > 20:
                trashable_items = pool_coins_only
            else:
                trashable_items = pool_illogical_consumables
            try:
                trashable_items.pop()
                cur_itempool_size -= 1
            except IndexError:
                raise ItemPoolTooSmallError()

    # Re-join the non-required items into one array
    pool_other_items.extend(pool_coins_only)
    pool_other_items.extend(pool_illogical_consumables)
    pool_other_items.extend(pool_badges)

    # Randomize consumables if needed
    pool_other_items = get_randomized_itempool(
        pool_other_items,
        logic_settings.randomize_consumable_mode,
        logic_settings.item_quality,
        logic_settings.add_beta_items,
    )

    pool_other_items = get_trapped_itempool(
        itempool = pool_other_items,
        trap_mode = logic_settings.itemtrap_mode,
        randomize_favors_mode = logic_settings.include_favors_mode,
        do_randomize_dojo = logic_settings.include_dojo,
        keyitems_outside_dungeon = logic_settings.keyitems_outside_dungeon,
        power_star_hunt = (logic_settings.star_hunt_total > 0),
        add_beta_items = logic_settings.add_beta_items,
        do_partner_upgrade_shuffle = do_partner_upgrade_shuffle,
    )

    return pool_other_items


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
    world_graph
):

    # Declare and init additional data structures
    ## Data structures for graph traversal
    all_item_nodes = []
    ## Data structures for item pool
    pool_progression_items = []
    pool_other_items = []
    pool_misc_progression_items = []

    # Generate item pool
    print("Generating item pool...")
    pool_other_items = _generate_item_pools(
        world_graph,
        pool_progression_items,
        pool_misc_progression_items,
        pool_other_items,
        all_item_nodes,
        logic_settings,
        starting_items,
        starting_partners,
        (logic_settings.partner_upgrade_shuffle != PartnerUpgradeShuffle.OFF),
    )

    starting_node_id = get_startingnode_id_from_startingmap_id(
        logic_settings.starting_map,
    )

    if logic_settings.randomize_puzzles and logic_settings.include_shops:
        # Force at least 3 different non-uniques into the Dry Dry Outpost shop
        # which are at least somewhat affordable
        affordable_nonuniques = set([
            x for x in pool_other_items
            if    (x.item_type == "ITEM" and x.base_price <= 10 and x.value <= 0xFF)
            #      consumable                affordable             not the berry keys
               or x.item_type == "COIN"
        ])
        unique_nonuniques = sorted(list(dict.fromkeys(affordable_nonuniques)))

        if len(unique_nonuniques) < 3:
            # We might have to place progression consumables here if the item
            # pool is too small, for example during "mystery only"
            unique_nonuniques.extend(
                random.sample(
                    [
                        x for x in pool_misc_progression_items
                        if not ("Proxy") in x.item_name
                    ],
                    k=3-len(unique_nonuniques)
                )
            )

        shop_code_items = random.sample(unique_nonuniques, k=3)
        for shop_code_item in shop_code_items:
            # check if some of the consumables are relevant to progression
            # if so, then remove them from the misc progression instead
            if shop_code_item in pool_misc_progression_items:
                pool_misc_progression_items.remove(shop_code_item)
            else:
                pool_other_items.remove(shop_code_item)

        # avoid item object references
        copied_shop_code_items = []
        for item in shop_code_items:
            copied_shop_code_items.append(deepcopy(item))

        # place into random dro shop slots
        shop_slot_ids = random.sample(
            population=["ShopItemA","ShopItemB","ShopItemC","ShopItemD","ShopItemE","ShopItemF"],
            k=3
        )
        while shop_slot_ids:
            world_graph[f"DRO_01/{shop_slot_ids.pop()}"]["node"].current_item = copied_shop_code_items.pop()


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

    if logic_settings.partner_shuffle == PartnerShuffle.SHUFFLED:
        pool_combined_progression_items.sort(
            key = lambda x: x.item_name in all_partners
        )

    if (   logic_settings.gear_shuffle_mode == GearShuffleMode.GEAR_LOCATION_SHUFFLE
        or logic_settings.starting_hammer == StartingHammer.HAMMERLESS
        or logic_settings.starting_boots == StartingBoots.JUMPLESS
    ):
        pool_combined_progression_items.sort(key=lambda x: x.item_type == "GEAR")

    if logic_settings.partner_upgrade_shuffle == PartnerUpgradeShuffle.SUPERBLOCKLOCATIONS:
        # Special handling: non-progression which has to be placed first
        pool_upgrade_items = [
            item for item in pool_other_items
            if     item.item_type == "PARTNERUPGRADE"
               and not item.is_trapped()
        ]
        for upgrade in pool_upgrade_items:
            pool_other_items.remove(upgrade)

        random.shuffle(pool_upgrade_items)
        for item_node in all_item_nodes:
            if item_node.current_item:
                continue
            item_node_id = item_node.identifier
            if "RandomBlockItem" in item_node_id:
                item_node.current_item = pool_upgrade_items.pop()
            if not pool_upgrade_items:
                break


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
    world_graph = None
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
            world_graph
        )
