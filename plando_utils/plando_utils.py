import re

from metadata.verbose_item_names import inverted_verbose_names
from metadata.verbose_item_locations import verbose_item_locations
from metadata.verbose_area_names import verbose_area_names

from metadata.partners_meta import all_partners

from plandomizer.plando_metadata import allowed_placeholders

from db.item import Item
from db.map_area import MapArea


class TransformedPlandoData():
    def __init__(self, plando_data: dict | None) -> None:
        self.partners_placed: list[str] = list()
        self.badges_placed: list[str] = list()
        self.keyitems_placed: list[str] = list()
        self.trap_count: int = 0
        self.magical_seeds_count: int = 0
        self.shop_prices: dict[str, int] = dict()
        self.item_placeholders: dict[str, str] = dict()
        self.trap_placeholders: list[str] = list()

        if plando_data is None:
            self.boss_battles: dict[int, int] | None = None
            self.required_spirits: list[int] | None = None
            self.difficulty: dict[int, int] | None = None
            self.move_costs: dict[str, dict[str, dict[str, int]]] | None = None
            self.item_placement: dict[str, Item] | None = None
            return

        self.boss_battles: dict[int, int] | None  = plando_data.get("boss_battles")
        self.required_spirits: list[int] | None = plando_data.get("required_spirits")
        self.difficulty: dict[int, int] | None = plando_data.get("difficulty")
        self.move_costs: dict[str, dict[str, dict[str, int]]] | None = plando_data.get("move_costs")

        self.item_placement: dict[str, Item] | None = dict()

        items_already_resolved: set[str] = set()


        def lookup_nodeid(area_str: str, location_str: str) -> str:
            verbose_map_name = location_str[:location_str.index(" - ")]
            verbose_location_name = location_str[location_str.index(" - ")+3:]

            if verbose_map_name in ["Ruined Castle Grounds","Hijacked Castle Entrance"]:
                area_str = "Peachs Castle Grounds"
            for k, v in verbose_area_names.items():
                if v.replace("'", "") == area_str:
                    area_key = k
                    break
            for map_area in MapArea.select():
                if map_area.verbose_name.replace("'","") != verbose_map_name:
                    continue
                if map_area.name.startswith(area_key):
                    if (   (    map_area.name == "KPA_10"
                            and verbose_location_name == "Defeat Koopatrol Reward")
                        or (    map_area.name == "KPA_11"
                            and verbose_location_name == "Yellow Block")
                    ):
                        continue

                    map_id = map_area.name
                    break

            map_location_dict = verbose_item_locations[map_id]
            for location_id, location_name in map_location_dict.items():
                if location_name.replace("'", "") == verbose_location_name:
                    key_name_item = location_id
                    break

            return f"{map_id}/{key_name_item}"


        def lookup_item(item_str: str) -> Item:
            item_name_plando: str = item_str
            item_is_trap: bool = False

            regex_match = re.match(r"TRAP \((.*)\)", item_name_plando)
            if regex_match is not None:
                item_is_trap = True
                item_name_plando = regex_match.group(1)

            if item_name_plando in inverted_verbose_names:
                if isinstance(inverted_verbose_names[item_name_plando], list):
                    if item_is_trap:
                        item_name_plando = inverted_verbose_names[item_name_plando][0]
                    else:
                        for unverbose_name in inverted_verbose_names[item_name_plando]:
                            if unverbose_name not in items_already_resolved:
                                item_name_plando = unverbose_name
                                break
                        else:
                            raise ValueError("Mismatch between plando and unverbose item names")
                else:
                    item_name_plando = inverted_verbose_names[item_name_plando]

            item_obj: Item | None = Item.get_or_none(Item.item_name == item_name_plando)

            if item_is_trap:
                item_obj.set_trapped()
            else:
                items_already_resolved.add(item_name_plando)

            return item_obj


        for area, arealocation_dict in plando_data["items"].items():
            for location, item_or_dict in arealocation_dict.items():
                # get location
                node_id = lookup_nodeid(area, location)
                # get item price, if shop
                if isinstance(item_or_dict, dict) and item_or_dict.get("price") is not None:
                    self.shop_prices[node_id] = item_or_dict["price"]
                # get item
                if isinstance(item_or_dict, str):
                    if item_or_dict in allowed_placeholders:
                        if item_or_dict == "TRAP":
                            self.trap_placeholders.append(node_id)
                            self.trap_count += 1
                        else:
                            self.item_placeholders[node_id] = item_or_dict
                        continue
                    else:
                        item_obj = lookup_item(item_or_dict)
                elif isinstance(item_or_dict, dict) and item_or_dict.get("item") is not None:
                    item_obj = lookup_item(item_or_dict["item"])
                else:
                    continue

                self.item_placement[node_id] = item_obj

                if item_obj.is_trapped():
                    self.trap_count += 1
                elif item_obj.item_name in all_partners:
                    self.partners_placed.append(item_obj.item_name)
                elif item_obj.item_type == "BADGE":
                    self.badges_placed.append(item_obj.item_name)
                elif item_obj.item_type in ["KEYITEM", "STARPIECE"]:
                    self.keyitems_placed.append(item_obj.item_name)

                    if item_obj.item_name.startswith("MagicalSeed"):
                        self.magical_seeds_count += 1
