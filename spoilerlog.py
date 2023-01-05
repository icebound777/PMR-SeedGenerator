import io
import json

from db.move import Move
from db.map_area import MapArea

from rando_enums.enum_types import BlockType

from metadata.partners_meta import partner_moves
from metadata.verbose_area_names import verbose_area_names
from metadata.verbose_item_names import verbose_item_names
from metadata.verbose_item_locations import verbose_item_locations

from optionset import OptionSet

def write_spoiler_log(
    placed_items:list,
    random_chapter_difficulty:dict=None,
    settings:OptionSet=False,
    spoilerlog_file:str=None,
    is_web_spoiler_log=False,
    spheres_dict:dict=None,
    move_costs:list=None,
    block_locations:list=None
):
    """
    Outputs a log file listing the final locations of all items
    after randomization and randomized chapter difficulty
    """
    spoiler_dict = dict()

    sorted_by_key =  sorted(placed_items,  key=lambda node: node.key_name_item)
    sorted_by_map =  sorted(sorted_by_key, key=lambda node: node.map_area.map_id)
    sorted_by_area = sorted(sorted_by_map, key=lambda node: node.map_area.area_id)

    # Add chapter difficulties
    if settings.progressive_scaling["value"]:
        spoiler_dict["difficulty"] = "progressive"
    else:
        spoiler_dict["difficulty"] = dict()
        for old_chapter, new_chapter in random_chapter_difficulty.items():
            spoiler_dict["difficulty"][f"chapter {old_chapter}"] = new_chapter

    # Add item locations
    for node in sorted_by_area:
        area_name = verbose_area_names.get(node.map_area.name[:3])
        area_name = area_name.replace("'", "")
        current_item_name = node.current_item.item_name
        map_verbose_name = (node.map_area.verbose_name)
        map_verbose_name = map_verbose_name.replace("'", "")

        # Get verbose names for map and item
        if (    node.map_area.name in verbose_item_locations
            and node.key_name_item in verbose_item_locations.get(node.map_area.name)):
            item_location = verbose_item_locations.get(node.map_area.name).get(node.key_name_item)
        else: # fallback for not-yet-verbose'd locations
            item_location = node.key_name_item
        item_location = item_location.replace("'", "")

        if current_item_name in verbose_item_names:
            current_item_name = verbose_item_names.get(current_item_name)
        if node.current_item.is_trapped():
            current_item_name = f"TRAP ({current_item_name})"
        if node.is_shop():
            # Add shop price
            price = node.current_item.base_price
            currency = "coins"
            if "HOS_06" in node.identifier and "Shop" in node.identifier:
                currency = "sp"
            current_item_name = f"{current_item_name} ({price} {currency})"

        if area_name not in spoiler_dict:
            spoiler_dict[area_name] = dict()
        spoiler_dict[area_name][f"{map_verbose_name} - {item_location}"] = \
            current_item_name

    # Add sphere log
    if(spheres_dict):
        spoiler_dict["sphere_log"] = spheres_dict

    # Add move costs
    def get_partner_by_move(move_name) -> str:
        partner_name = ""
        for partner, move_list in partner_moves.items():
            if move_name in move_list:
                partner_name = partner
        return partner_name


    def add_move_cost(spoilers:dict, move:Move, cost:int):
        cur_move_type = move.move_type.lower()
        cur_move_name = move.move_name
        if cur_move_name.startswith("ChillOut"):
            # Trim "ChillOutMove" and "ChillOutBadge"
            cur_move_name = "ChillOut"

        if cur_move_type not in spoilers:
            spoilers[cur_move_type] = dict()
        if (    cur_move_name not in spoilers[cur_move_type]
            and cur_move_type != "partner"
        ):
            spoilers[cur_move_type][cur_move_name] = dict()

        cost_type = move.cost_type
        if cur_move_type == "starpower":
            cost_type = "SP"

        if cur_move_type == "partner":
            current_partner = get_partner_by_move(cur_move_name)
            if current_partner not in spoilers[cur_move_type]:
                spoilers[cur_move_type][current_partner] = dict()
            spoilers[cur_move_type][current_partner][cur_move_name] = cost
        else:
            spoilers[cur_move_type][cur_move_name][cost_type] = cost


    spoiler_dict["move_costs"] = dict()
    ## fetch default move costs
    for move in Move.select().order_by(Move.cost_type):
        current_cost = move.cost_value

        add_move_cost(spoiler_dict["move_costs"], move, current_cost)

    if move_costs is not None and move_costs:
        ## adjust edited move costs
        for move_key, move_cost in move_costs:
            item_id = move_key & 0xFF
            move = (
                Move.select(Move.move_name,
                            Move.move_type,
                            Move.cost_type)
                    .where(Move.index == item_id)
                    .get()
            )

            current_cost = move_cost

            add_move_cost(spoiler_dict["move_costs"], move, current_cost)

    ## order badges alphabetically
    badge_names = list(spoiler_dict["move_costs"]["badge"].keys())
    badge_names.sort()
    badges_ordered = dict()
    for key in badge_names:
        badges_ordered[key] = spoiler_dict["move_costs"]["badge"][key]
    spoiler_dict["move_costs"]["badge"] = badges_ordered

    ## manually order partners
    partners_ordered = dict()
    partners_ordered["Goombario"] = spoiler_dict["move_costs"]["partner"]["Goombario"]
    partners_ordered["Kooper"] = spoiler_dict["move_costs"]["partner"]["Kooper"]
    partners_ordered["Bombette"] = spoiler_dict["move_costs"]["partner"]["Bombette"]
    partners_ordered["Parakarry"] = spoiler_dict["move_costs"]["partner"]["Parakarry"]
    partners_ordered["Bow"] = spoiler_dict["move_costs"]["partner"]["Bow"]
    partners_ordered["Watt"] = spoiler_dict["move_costs"]["partner"]["Watt"]
    partners_ordered["Sushie"] = spoiler_dict["move_costs"]["partner"]["Sushie"]
    partners_ordered["Lakilester"] = spoiler_dict["move_costs"]["partner"]["Lakilester"]

    spoiler_dict["move_costs"]["partner"] = partners_ordered

    # Add super block locations
    block_dict = dict()
    block_locations.sort(key=lambda x: x[0])
    for location_key, block_type in block_locations:
        if block_type == BlockType.SUPER:
            # resolve location
            area_id = (location_key & 0xFF0000) >> 16
            map_id = (location_key & 0xFF00) >> 8
            map_area = (
                MapArea.select(MapArea.name, MapArea.verbose_name)
                    .where(MapArea.area_id == area_id)
                    .where(MapArea.map_id == map_id)
                    .get()
            )
            cur_map_name, cur_verbose_map = map_area.name, map_area.verbose_name
            cur_verbose_area = verbose_area_names.get(cur_map_name[:3])

            cur_verbose_map = cur_verbose_map.replace("'", "")
            cur_verbose_area = cur_verbose_area.replace("'", "")

            if cur_verbose_area not in block_dict:
                block_dict[cur_verbose_area] = []
            block_dict[cur_verbose_area].append(cur_verbose_map)

    spoiler_dict["superblocks"] = block_dict

    # Output spoiler log
    if is_web_spoiler_log:
        file = io.StringIO()
        json.dump(spoiler_dict, file)
        file.seek(0)
        return file
    else:
        with open(spoilerlog_file, "w", encoding="utf-8") as file:
            json.dump(spoiler_dict, file, indent=4)
