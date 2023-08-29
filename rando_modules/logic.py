"""
This modules offers the randomization logic and takes care of actually randomizing
the game according to the settings chosen.
"""
import random
#import logging

from db.node import Node
from db.item import Item
from db.map_area import MapArea

from models.MarioInventory import MarioInventory

from rando_enums.enum_options import \
    BowserCastleMode,\
    GearShuffleMode,\
    StartingBoots,\
    StartingHammer,\
    IncludeFavorsMode,\
    IncludeLettersMode

from rando_modules.modify_itempool \
    import get_randomized_itempool,\
           get_trapped_itempool

from rando_modules.unbeatable_seed_error import UnbeatableSeedError

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
    do_randomize_dojo:bool,
    starting_partners:list,
    startwith_bluehouse_open:bool,
    startwith_forest_open:bool,
    magical_seeds_required:int,
    bowsers_castle_mode:int,
    always_speedyspin:bool,
    always_ispy:bool,
    always_peekaboo:bool,
    do_progressive_badges:bool,
    gear_shuffle_mode:int,
    starting_hammer:int=-1,
    starting_boots:int=-1,
) -> list:
    """
    Returns a list of items that should not be placed or given to Mario at the
    start.
    """
    excluded_items = []

    if do_randomize_dojo:
        for item_name in exclude_due_to_settings.get("do_randomize_dojo"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    for partner_string in starting_partners:
        partner_item = Item.get(Item.item_name == partner_string)
        excluded_items.append(partner_item)
    if startwith_bluehouse_open:
        for item_name in exclude_due_to_settings.get("startwith_bluehouse_open"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if startwith_forest_open:
        for item_name in exclude_due_to_settings.get("startwith_forest_open"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if magical_seeds_required < 4:
        for item_name in exclude_due_to_settings.get("magical_seeds_required").get(magical_seeds_required):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if bowsers_castle_mode > BowserCastleMode.VANILLA:
        for item_name in exclude_due_to_settings.get("shorten_bowsers_castle"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if bowsers_castle_mode == BowserCastleMode.BOSSRUSH:
        for item_name in exclude_due_to_settings.get("boss_rush"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if always_speedyspin:
        for item_name in exclude_due_to_settings.get("always_speedyspin"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if always_ispy:
        for item_name in exclude_due_to_settings.get("always_ispy"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if always_peekaboo:
        for item_name in exclude_due_to_settings.get("always_peekaboo"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if do_progressive_badges:
        for item_name in exclude_due_to_settings.get("do_progressive_badges"):
            item = Item.get(Item.item_name == item_name)
            excluded_items.append(item)
    if gear_shuffle_mode >= GearShuffleMode.GEAR_LOCATION_SHUFFLE:
        if starting_hammer == StartingHammer.ULTRAHAMMER:
            item = Item.get(Item.item_name == "HammerProxy3")
            excluded_items.append(item)
        if starting_hammer >= StartingHammer.SUPERHAMMER:
            item = Item.get(Item.item_name == "HammerProxy2")
            excluded_items.append(item)
        if starting_hammer >= StartingHammer.HAMMER:
            item = Item.get(Item.item_name == "HammerProxy1")
            excluded_items.append(item)
        if starting_boots == StartingBoots.ULTRABOOTS:
            item = Item.get(Item.item_name == "BootsProxy3")
            excluded_items.append(item)
        if starting_boots >= StartingBoots.SUPERBOOTS:
            item = Item.get(Item.item_name == "BootsProxy2")
            excluded_items.append(item)
        if starting_boots >= StartingBoots.BOOTS:
            item = Item.get(Item.item_name == "BootsProxy1")
            excluded_items.append(item)

    return excluded_items


def _generate_item_pools(
    world_graph,
    pool_progression_items:list,
    pool_misc_progression_items:list,
    pool_other_items:list,
    all_item_nodes:list,
    shuffle_overworld_coins:bool,
    shuffle_block_coins:bool,
    shuffle_foliage_coins:bool,
    shuffle_favor_coins:bool,
    do_randomize_shops:bool,
    do_randomize_panels:bool,
    randomize_favors_mode:int,
    randomize_letters_mode:int,
    do_randomize_radiotrade:bool,
    do_randomize_dojo:bool,
    gear_shuffle_mode:int,
    randomize_consumable_mode:int,
    item_quality:int,
    itemtrap_mode:int,
    startwith_bluehouse_open:bool,
    startwith_forest_open:bool,
    magical_seeds_required:int,
    keyitems_outside_dungeon:bool,
    partners_in_default_locations:bool,
    always_speedyspin,
    always_ispy,
    always_peekaboo,
    starting_partners:list,
    starting_items:list,
    starting_boots:int,
    starting_hammer:int,
    add_item_pouches:bool,
    add_unused_badge_duplicates:bool,
    add_beta_items:bool,
    do_progressive_badges:bool,
    bowsers_castle_mode:int,
    star_hunt_stars:int
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
                and not shuffle_overworld_coins
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in block_coin_locations
                and not shuffle_block_coins
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in bush_tree_coin_locations
                and not shuffle_foliage_coins
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.vanilla_item.item_name == "Coin"
                and current_node_id in favor_coin_locations
                and not shuffle_favor_coins
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item.startswith("Shop")
                and not do_randomize_shops
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item == "HiddenPanel"
                and not do_randomize_panels
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in kootfavors_reward_locations
                and randomize_favors_mode == IncludeFavorsMode.NOT_RANDOMIZED
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in kootfavors_keyitem_locations
                and randomize_favors_mode <= IncludeFavorsMode.RND_REWARD_VANILLA_KEYITEMS
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in chainletter_giver_locations
                and randomize_letters_mode < IncludeLettersMode.FULL_SHUFFLE
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id == chainletter_final_reward_location
                and randomize_letters_mode < IncludeLettersMode.RANDOM_CHAIN_REWARD
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id in simpleletter_locations
                and randomize_letters_mode < IncludeLettersMode.SIMPLE_LETTERS
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    not do_randomize_radiotrade
                and current_node_id in radio_trade_event_locations
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (   current_node_id in dojo_locations
                and not do_randomize_dojo
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node_id == "MAC_02/GiftD"
                and startwith_forest_open
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    current_node.key_name_item == "Partner"
                and partners_in_default_locations
                and current_node.vanilla_item.item_name not in starting_partners
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    gear_shuffle_mode == GearShuffleMode.VANILLA
                and current_node.vanilla_item.item_type == "GEAR"
                and (   current_node.identifier != "KMR_04/Bush7_Drop1"
                     or starting_hammer == StartingHammer.HAMMERLESS)
            ):
                current_node.current_item = current_node.vanilla_item
                all_item_nodes.append(current_node)
                continue

            if (    gear_shuffle_mode == GearShuffleMode.VANILLA
                and current_node.identifier == "KMR_04/Bush7_Drop1"
            ):
                # special casing so the hammer bush is never empty but also
                # never holds required items or badges
                current_node.current_item = _get_random_taycet_item()
                all_item_nodes.append(current_node)
                continue


            # Check all remaining nodes for items to add to the pools
            all_item_nodes.append(current_node)

            # Special casing for hammer bush during gear location shuffle w/o
            # hammerless: add modified "gear" Tayce T item to gear locations
            if (    current_node.identifier == "KMR_04/Bush7_Drop1"
                and starting_hammer != StartingHammer.HAMMERLESS
                and gear_shuffle_mode == GearShuffleMode.GEAR_LOCATION_SHUFFLE
            ):
                modified_taycet = _get_random_taycet_item()
                modified_taycet.item_type = "GEAR"
                pool_progression_items.append(modified_taycet)
                continue

            # Item shall be randomized: Add it to the correct item pool
            if (current_node.vanilla_item.progression
            or (do_randomize_shops and "StarPiece" in current_node.vanilla_item.item_name)
            or current_node.vanilla_item.item_type == "GEAR"
            ):
                pool_progression_items.append(current_node.vanilla_item)
            else:
                if (    current_node.vanilla_item.item_name in progression_miscitems_names
                    and current_node.vanilla_item not in pool_misc_progression_items
                ):
                    # Since progression misc items have to be placed in
                    # replenishable locations, we only need one of each
                    pool_misc_progression_items.append(current_node.vanilla_item)
                else:
                    if current_node.vanilla_item.item_type == "COIN":
                        pool_coins_only.append(current_node.vanilla_item)
                    elif current_node.vanilla_item.item_type == "ITEM":
                        pool_illogical_consumables.append(current_node.vanilla_item)
                    else:
                        pool_other_items.append(current_node.vanilla_item)

    random.shuffle(pool_illogical_consumables)

    # Swap random consumables and coins for power stars, if needed
    if star_hunt_stars > 0:
        stars_added = 0
        for power_star_item in (
            Item
            .select()
            .where(
                Item.item_name % "PowerStar*"
            )
        ):
            if stars_added >= star_hunt_stars:
                break
            if len(pool_coins_only) > 20:
                trashable_items = pool_coins_only
            else:
                trashable_items = pool_illogical_consumables

            trashable_items.pop()
            pool_progression_items.append(power_star_item)
            stars_added += 1

    # Swap random consumables and coins for strange pouches if needed
    if add_item_pouches:
        pouch_items = [
            Item.get(Item.item_name == "PouchA"),
            Item.get(Item.item_name == "PouchB"),
            Item.get(Item.item_name == "PouchC"),
            Item.get(Item.item_name == "PouchD"),
            Item.get(Item.item_name == "PouchE"),
        ]

        cnt_items_removed = 0

        if len(pool_coins_only) > 20:
            trashable_items = pool_coins_only
        else:
            trashable_items = pool_illogical_consumables
        while cnt_items_removed < 5:
            trashable_items.pop()
            cnt_items_removed += 1

        pool_other_items.extend(pouch_items)

    # Swap random consumables and coins for unused badge duplicates, if needed
    if add_unused_badge_duplicates:
        unused_badge_duplicates = []
        for item in Item.select().where(Item.unused_duplicates == True):
            unused_badge_duplicates.append(item)

        for _ in unused_badge_duplicates:
            if len(pool_coins_only) > 20:
                trashable_items = pool_coins_only
            else:
                trashable_items = pool_illogical_consumables
            trashable_items.pop()

        pool_other_items.extend(unused_badge_duplicates)

    # Swap random consumables and coins for beta items, if needed
    if add_beta_items:
        beta_items = []
        for item in Item.select().where(Item.unused_duplicates == False).where(Item.unused == True):
            beta_items.append(item)

        for _ in beta_items:
            if len(pool_coins_only) > 20:
                trashable_items = pool_coins_only
            else:
                trashable_items = pool_illogical_consumables
            trashable_items.pop()

        pool_other_items.extend(beta_items)

    # Swap random consumables and coins for progressive badges, if needed
    if do_progressive_badges:
        new_badges = []
        for item in Item.select().where(Item.item_name.in_(progressive_badges)):
            new_badges.append(item)

        for _ in new_badges:
            if len(pool_coins_only) > 20:
                trashable_items = pool_coins_only
            else:
                trashable_items = pool_illogical_consumables
            trashable_items.pop()

        pool_other_items.extend(new_badges)

    # If we start jumpless, add a progressive boots item to the item pool
    if starting_boots == StartingBoots.JUMPLESS:
        new_boots = Item.get(Item.item_name == "BootsProxy1")
        if len(pool_coins_only) > 20:
            trashable_items = pool_coins_only
        else:
            trashable_items = pool_illogical_consumables
        trashable_items.pop()

        pool_progression_items.append(new_boots)

    # Re-join the non-required items into one array
    pool_other_items.extend(pool_coins_only)
    pool_other_items.extend(pool_illogical_consumables)

    # Adjust item pools based on settings
    goal_size_item_pool = len(pool_progression_items)      \
                        + len(pool_misc_progression_items) \
                        + len(pool_other_items)

    items_to_remove_from_pools = get_items_to_exclude(
        do_randomize_dojo,
        starting_partners,
        startwith_bluehouse_open,
        startwith_forest_open,
        magical_seeds_required,
        bowsers_castle_mode,
        always_speedyspin,
        always_ispy,
        always_peekaboo,
        do_progressive_badges,
        gear_shuffle_mode,
        starting_hammer,
        starting_boots
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
        if item in pool_other_items:
            pool_other_items.remove(item)
            continue
        #logging.info("Attempted to remove %s from item pools, but no pool holds such item.", item)

    # If the item pool is too small now, fill it back up
    cur_size_item_pool = len(pool_progression_items)      \
                       + len(pool_misc_progression_items) \
                       + len(pool_other_items)
    while goal_size_item_pool > cur_size_item_pool:
        pool_other_items.append(_get_random_taycet_item())
        cur_size_item_pool = len(pool_progression_items)      \
                           + len(pool_misc_progression_items) \
                           + len(pool_other_items)

    # Randomize consumables if needed
    pool_other_items = get_randomized_itempool(
        pool_other_items,
        randomize_consumable_mode,
        item_quality,
        add_beta_items
    )

    pool_other_items = get_trapped_itempool(
        pool_other_items,
        itemtrap_mode,
        randomize_favors_mode,
        do_randomize_dojo,
        keyitems_outside_dungeon,
        (star_hunt_stars > 0)
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

    empty_reachables, mario = find_empty_reachable_nodes(
        world_graph,
        reachable_node_ids,
        non_traversable_edges,
        mario
    )

    return empty_reachables, mario


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
        node_ids_to_check = set() # set() of str()
        for from_node_id in non_traversable_edges:
            node_ids_to_check.add(from_node_id)

        #logging.debug("%s", node_ids_to_check)
        for from_node_id in node_ids_to_check:
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

    return empty_item_nodes, mario


def _algo_assumed_fill(
    item_placement,
    shuffle_overworld_coins:bool,
    shuffle_block_coins:bool,
    shuffle_foliage_coins:bool,
    shuffle_favor_coins:bool,
    do_randomize_shops,
    do_randomize_panels,
    randomize_favors_mode:int,
    randomize_letters_mode:int,
    do_randomize_radiotrade:bool,
    do_randomize_dojo,
    gear_shuffle_mode:int,
    randomize_consumable_mode:int,
    item_quality,
    itemtrap_mode,
    starting_map_id,
    startwith_prologue_open:bool,
    startwith_bluehouse_open,
    startwith_mtrugged_open:bool,
    startwith_forest_open:bool,
    magical_seeds_required:int,
    startwith_toybox_open,
    startwith_whale_open,
    ch7_bridge_visible:bool,
    cook_without_fryingpan:bool,
    starting_partners,
    starting_boots,
    starting_hammer,
    speedyspin,
    ispy,
    peekaboo,
    partners_always_usable,
    partners_in_default_locations,
    hidden_block_mode:int,
    keyitems_outside_dungeon:bool,
    starting_items:list,
    add_item_pouches:bool,
    add_unused_badge_duplicates:bool,
    add_beta_items:bool,
    do_progressive_badges:bool,
    bowsers_castle_mode:int,
    star_hunt_stars:int,
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
        shuffle_overworld_coins,
        shuffle_block_coins,
        shuffle_foliage_coins,
        shuffle_favor_coins,
        do_randomize_shops,
        do_randomize_panels,
        randomize_favors_mode,
        randomize_letters_mode,
        do_randomize_radiotrade,
        do_randomize_dojo,
        gear_shuffle_mode,
        randomize_consumable_mode,
        item_quality,
        itemtrap_mode,
        startwith_bluehouse_open,
        startwith_forest_open,
        magical_seeds_required,
        keyitems_outside_dungeon,
        partners_in_default_locations,
        speedyspin,
        ispy,
        peekaboo,
        starting_partners,
        starting_items,
        starting_boots,
        starting_hammer,
        add_item_pouches,
        add_unused_badge_duplicates,
        add_beta_items,
        do_progressive_badges,
        bowsers_castle_mode,
        star_hunt_stars
    )

    starting_node_id = get_startingnode_id_from_startingmap_id(starting_map_id)

    print("Placing progression items...")
    #Place progression items, both key and replenishable
    pool_combined_progression_items = pool_progression_items + pool_misc_progression_items
    random.shuffle(pool_combined_progression_items)

    dungeon_restricted_items = {}
    if not keyitems_outside_dungeon:
        for dungeon in limited_by_item_areas:
            for itemlist in limited_by_item_areas[dungeon].values():
                for item in itemlist:
                    assert item not in dungeon_restricted_items
                    dungeon_restricted_items[item] = dungeon
        pool_combined_progression_items.sort(key=lambda x: x.item_name in dungeon_restricted_items.keys())

    if gear_shuffle_mode == GearShuffleMode.GEAR_LOCATION_SHUFFLE:
        pool_combined_progression_items.sort(key=lambda x: x.item_type == "GEAR")

    while pool_combined_progression_items:
        item = pool_combined_progression_items.pop()
        mario = MarioInventory(
            starting_boots,
            starting_hammer,
            starting_partners,
            starting_items,
            partners_always_usable,
            hidden_block_mode,
            magical_seeds_required,
            startwith_prologue_open,
            startwith_bluehouse_open,
            startwith_mtrugged_open,
            startwith_forest_open,
            startwith_toybox_open,
            startwith_whale_open,
            ch7_bridge_visible,
            speedyspin,
            cook_without_fryingpan,
            vanilla_start=False
        )

        for item_ in pool_combined_progression_items:
            mario.add(item_.item_name)

        candidate_locations, mario = find_available_nodes(
            world_graph,
            starting_node_id,
            mario
        )
        if item.item_name in progression_miscitems_names:
            candidate_locations = [node for node in candidate_locations if is_itemlocation_replenishable(node)]

        if item.item_name in dungeon_restricted_items:
            dungeon = dungeon_restricted_items[item.item_name]
            candidate_locations = [node for node in candidate_locations if node.identifier[:3] == dungeon]
            dungeon_restricted_items.pop(item.item_name)

        if gear_shuffle_mode == GearShuffleMode.GEAR_LOCATION_SHUFFLE:
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
            and (   shuffle_overworld_coins
                 or shuffle_block_coins
                 or shuffle_foliage_coins
                 or shuffle_favor_coins)
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
    starting_map_id,
    startwith_prologue_open:bool,
    startwith_bluehouse_open,
    startwith_mtrugged_open:bool,
    startwith_forest_open:bool,
    magical_seeds_required:int,
    startwith_toybox_open,
    startwith_whale_open,
    ch7_bridge_visible,
    cook_without_fryingpan:bool,
    starting_partners,
    starting_boots,
    starting_hammer,
    partners_always_usable,
    hidden_block_mode:int,
    starting_items:list,
    startwith_speedyspin,
    world_graph,
    shuffle_items:bool
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
    starting_node_id = get_startingnode_id_from_startingmap_id(starting_map_id)

    # Find initially reachable nodes within the world graph
    non_traversable_edges[starting_node_id] = [
        edge["edge_id"] for edge in world_graph[starting_node_id]["edge_list"]
    ]

    reachable_node_ids.add(starting_node_id)

    vanilla_start = (
            starting_node_id == "KMR_02/1"
        and not shuffle_items
        and starting_hammer == -1
        and "Bombette" not in starting_partners
        and not partners_always_usable
    )

    # Init Mario Inventory
    mario = MarioInventory(
        starting_boots,
        starting_hammer,
        starting_partners,
        starting_items,
        partners_always_usable,
        hidden_block_mode,
        magical_seeds_required,
        startwith_prologue_open,
        startwith_bluehouse_open,
        startwith_mtrugged_open,
        startwith_forest_open,
        startwith_toybox_open,
        startwith_whale_open,
        ch7_bridge_visible,
        startwith_speedyspin,
        cook_without_fryingpan,
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

    if starting_boots == 2:
        spheres_dict["starting_items"].append("ProgressiveBoots*")
    if starting_boots >= 1:
        spheres_dict["starting_items"].append("ProgressiveBoots*")
    if starting_boots >= 0:
        spheres_dict["starting_items"].append("ProgressiveBoots*")

    if starting_hammer == 2:
        spheres_dict["starting_items"].append("ProgressiveHammer*")
    if starting_hammer >= 1:
        spheres_dict["starting_items"].append("ProgressiveHammer*")
    if starting_hammer >= 0:
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
    do_custom_seed:bool,
    do_shuffle_items,
    shuffle_overworld_coins:bool,
    shuffle_block_coins:bool,
    shuffle_foliage_coins:bool,
    shuffle_favor_coins:bool,
    do_randomize_shops,
    do_randomize_panels,
    randomize_favors_mode:int,
    randomize_letters_mode:int,
    do_randomize_radiotrade:bool,
    do_randomize_dojo,
    gear_shuffle_mode:int,
    randomize_consumable_mode:int,
    item_quality,
    itemtrap_mode,
    starting_map_id,
    startwith_prologue_open:bool,
    startwith_bluehouse_open,
    startwith_mtrugged_open:bool,
    startwith_forest_open:bool,
    magical_seeds_required:int,
    startwith_toybox_open,
    startwith_whale_open,
    ch7_bridge_visible:bool,
    cook_without_fryingpan:bool,
    starting_partners,
    starting_boots,
    starting_hammer,
    speedyspin,
    ispy,
    peekaboo,
    partners_always_usable:bool,
    partners_in_default_locations,
    hidden_block_mode:int,
    keyitems_outside_dungeon:bool,
    starting_items:list,
    add_item_pouches:list,
    add_unused_badge_duplicates:bool,
    add_beta_items:bool,
    do_progressive_badges:bool,
    bowsers_castle_mode:int,
    star_hunt_stars:int,
    world_graph = None
):
    """Places items into item locations according to chosen settings."""
    #level = logging.INFO
    #fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    #logging.basicConfig(level=level, format=fmt)

    if not do_shuffle_items:
        # Place items in their vanilla locations
        for node in Node.select().where(Node.key_name_item.is_null(False)):
            node.current_item = node.vanilla_item
            item_placement.append(node)
    elif do_custom_seed:
        raise ValueError
    else:
        # Place items in a backward fill, ensuring a maximally deep fill.
        _algo_assumed_fill(
            item_placement,
            shuffle_overworld_coins,
            shuffle_block_coins,
            shuffle_foliage_coins,
            shuffle_favor_coins,
            do_randomize_shops,
            do_randomize_panels,
            randomize_favors_mode,
            randomize_letters_mode,
            do_randomize_radiotrade,
            do_randomize_dojo,
            gear_shuffle_mode,
            randomize_consumable_mode,
            item_quality,
            itemtrap_mode,
            starting_map_id,
            startwith_prologue_open,
            startwith_bluehouse_open,
            startwith_mtrugged_open,
            startwith_forest_open,
            magical_seeds_required,
            startwith_toybox_open,
            startwith_whale_open,
            ch7_bridge_visible,
            cook_without_fryingpan,
            starting_partners,
            starting_boots,
            starting_hammer,
            speedyspin,
            ispy,
            peekaboo,
            partners_always_usable,
            partners_in_default_locations,
            hidden_block_mode,
            keyitems_outside_dungeon,
            starting_items,
            add_item_pouches,
            add_unused_badge_duplicates,
            add_beta_items,
            do_progressive_badges,
            bowsers_castle_mode,
            star_hunt_stars,
            world_graph
        )
