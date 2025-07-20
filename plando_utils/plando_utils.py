import re

from models.options.OptionSet import OptionSet

from metadata.verbose_item_names import inverted_verbose_names
from metadata.verbose_item_locations import verbose_item_locations
from metadata.verbose_area_names import verbose_area_names

from metadata.partners_meta import all_partners

from rando_enums.enum_options import RequiredChapters, SeedGoal

from plandomizer.plando_metadata import (
    allowed_placeholders,
    rowf_badges,
    merlow_badges,
)

from rando_modules.plando_settings_mismatch_error import PlandoSettingsMismatchError

from db.item import Item
from db.map_area import MapArea


class TransformedPlandoData():
    def __init__(self, plando_data: dict | None) -> None:
        self.partners_placed: list[str] = list()
        self.badges_placed: list[str] = list()
        self.shop_badges_placed: bool = False
        self.keyitems_placed: list[str] = list()
        self.trap_count: int = 0
        self.magical_seeds_count: int = 0
        self.shop_prices: dict[str, int] = dict()
        self.item_placeholders: dict[str, str] = dict()
        self.trap_placeholders: list[str] = list()

        if plando_data is None:
            self.boss_battles: dict[int, int] | None = None
            self.required_chapters: list[int] | None = None
            self.difficulty: dict[int, int] | None = None
            self.move_costs: dict[str, dict[str, dict[str, int]]] | None = None
            self.item_placement: dict[str, Item] | None = None
            self.plando_active = False
            self.dungeon_entrances: dict[int, int] | None = None
            return

        self.boss_battles: dict[int, int] | None  = plando_data.get("boss_battles")
        self.required_chapters: list[int] | None = plando_data.get("required_chapters")
        self.difficulty: dict[int, int] | None = plando_data.get("difficulty")
        self.move_costs: dict[str, dict[str, dict[str, int]]] | None = plando_data.get("move_costs")
        self.dungeon_entrances: dict[int, int] | None = plando_data.get("dungeon_entrances")

        self.item_placement: dict[str, Item] | None = dict()

        self.plando_active = (
            (self.boss_battles is not None and len(self.boss_battles) > 0)
         or (self.required_chapters is not None and len(self.required_chapters) > 0)
         or (self.difficulty is not None and len(self.difficulty) > 0)
         or (self.move_costs is not None and len(self.move_costs) > 0)
         or (plando_data.get("items") is not None and len(plando_data.get("items")) > 0)
         or (self.dungeon_entrances is not None and len(self.dungeon_entrances) > 0)
        )

        if not plando_data.get("items"):
            return

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
                item_name: str = None
                if isinstance(item_or_dict, str):
                    item_name = item_or_dict
                elif isinstance(item_or_dict, dict) and item_or_dict.get("item") is not None:
                    item_name = item_or_dict["item"]
                if item_name is None:
                    continue

                if item_name in allowed_placeholders:
                    if item_name == "TRAP":
                        self.trap_placeholders.append(node_id)
                        self.trap_count += 1
                    else:
                        self.item_placeholders[node_id] = item_name
                    continue

                if item_name in rowf_badges or item_name in merlow_badges:
                    self.shop_badges_placed = True

                item_obj = lookup_item(item_name)

                self.item_placement[node_id] = item_obj

                if item_obj.is_trapped():
                    self.trap_count += 1
                elif item_obj.item_name in all_partners:
                    self.partners_placed.append(item_obj.item_name)
                elif item_obj.item_type == "BADGE":
                    self.badges_placed.append(item_obj.item_name)
                elif item_obj.item_type in ["KEYITEM", "STARPIECE", "GEAR"]:
                    self.keyitems_placed.append(item_obj.item_name)

                    if item_obj.item_name.startswith("MagicalSeed"):
                        self.magical_seeds_count += 1


    def verify_against_settings(self, rando_settings: OptionSet):
        """
        Run assertions on randomizer settings, to check if they clash with
        plandomizer data.
        """

        # Assert that we have Shop Shuffle active if we have plando'd
        # one of the shop badges
        if (    self.shop_badges_placed
            and not rando_settings.logic_settings.include_shops
        ):
            raise PlandoSettingsMismatchError(
                "Plandomizer error: Shop shuffle is turned off, but one or "\
                "more of the badges from Rowf's or Merlow's shops are plando'd"
            )

        # Assert that Required Chapters is not set to Limit Chapter Logic if
        # a chapter 8 entrance is plando'd
        if (    rando_settings.logic_settings.required_chapters == RequiredChapters.SPECIFIC_AND_LIMITCHAPTERLOGIC
            and self.dungeon_entrances is not None
            and (   8 in self.dungeon_entrances
                 or 8 in self.dungeon_entrances.values()
                )
        ):
            raise PlandoSettingsMismatchError(
                "Plandomizer error: Limit Chapter Logic is active, but "\
                "a chapter 8 dungeon entrance is set"
            )

        # Assert that if the seed goal is set to Open Star Way and Required
        # Chapters is active, none of the required chapters' dungeons are behind
        # Star Haven
        if (    rando_settings.logic_settings.seed_goal == SeedGoal.OPEN_STARWAY
            and self.dungeon_entrances is not None
            and self.required_chapters is not None
            and 8 in self.dungeon_entrances
            and self.dungeon_entrances[8] in self.required_chapters
        ):
            raise PlandoSettingsMismatchError(
                "Plandomizer error: The Seed Goal is Open Star Way, but "\
                "one of the chapters required to beat the game is connected "
                "to Star Haven"
            )

        # Assert that if Required Chapters is active in any way, none of
        # the required dungeons are behind Star Haven
        if (    self.dungeon_entrances is not None
            and self.required_chapters is not None
            and rando_settings.logic_settings.required_chapters != RequiredChapters.ANY
            and 8 in self.dungeon_entrances
            and any(
                    True for x in self.required_chapters
                    if x == self.dungeon_entrances[8]
                )
        ):
            raise PlandoSettingsMismatchError(
                "Plandomizer error: Required Chapters is set active, but one "\
                "of the required chapters is placed behind Star Haven"
            )

        # Assert that if Star Way requires 7 chapters to open, that no
        # chapter 8 connection is plando'd
        if (    self.dungeon_entrances is not None
            and rando_settings.logic_settings.starway_chapters_needed_count == 7
            and (   8 in self.dungeon_entrances
                 or 8 in self.dungeon_entrances.values()
                )
        ):
            raise PlandoSettingsMismatchError(
                "Plandomizer error: The number of chapters to open Star Way "\
                "is set to 7, but a chapter 8 dungeon connection is plando'd"
            )
