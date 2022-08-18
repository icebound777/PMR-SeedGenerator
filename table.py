from parse import get_default_table, create_table, get_table_info

from db.option import Option
from db.actor_attribute import ActorAttribute
from db.quiz import Quiz
from optionset import MysteryOptionSet

from models.KeyValuePair import KeyValuePair


class Table:
    instance = None
    default_db = {}
    db = {}
    info = {}

    def __init__(self):
        if Table.instance is None:
            Table.instance = self
        else:
            self = Table.instance

    def __getitem__(self, key):
        return self.db[key]

    def generate_pairs(self, **kwargs):
        table_data = []

        # Options
        options = kwargs.get("options")

        for option_data in options.__dict__.values():
            if isinstance(option_data, KeyValuePair) and option_data.key:
                table_data.append(option_data)

            if isinstance(option_data, MysteryOptionSet):
                for mystery_option in option_data.__dict__.values():
                    if isinstance(mystery_option, dict) and mystery_option.key:
                        table_data.append(mystery_option)

        # temp fix for multiworld
        table_data.append(
            KeyValuePair(
                0xAF050000,
                0x00000000
            )
        )

        # more temp fixes because we push half implemented features
        table_data.append(
            KeyValuePair(
                0xAF02000B,
                0x00000000
            )
        )
        table_data.append(
            KeyValuePair(
                0xAF060505,
                0x00000000
            )
        )

        # Quizzes
        quizzes = kwargs.get("quiz_data")

        for key, value in quizzes:
            table_data.append(KeyValuePair(key, value))

        # Items
        placed_items = kwargs.get("items")
        for node in placed_items:
            if node.key_name_item is not None and node.current_item is not None:
                table_data.append(KeyValuePair(node.get_item_key(), node.current_item.value))
                # Generate a ROM table pair that describes where a unique itemID
				# resides in the game using areaID and mapID
                if node.current_item.item_type in [
                    "KEYITEM",
                    "BADGE",
                    "STARPIECE",
                    "PARTNER"
                ]:
                    table_data.append(
                        KeyValuePair(
                            (0xAA << 24) | (node.current_item.value),
                            (node.map_area.area_id << 8) | (node.map_area.map_id)
                        )
                    )

            # Item Prices
            if (    node.key_name_price is not None
                and (   node.key_name_price.startswith("ShopPrice")
                     or node.key_name_price.startswith("RewardAmount")
                )
            ):
                table_data.append(
                    KeyValuePair(                 
                        node.get_price_key(),
                        node.current_item.base_price
                    )
                )

        # Blocks
        placed_blocks = kwargs.get("blocks")
        for key, value in placed_blocks:
            table_data.append(KeyValuePair(key, value))

        # Entrances
        entrances = kwargs.get("entrances")
        for key, value in entrances:
            table_data.append(KeyValuePair(key, value))

        # Actor Attributes
        actor_attributes = kwargs.get("actor_data")
        for key, value in actor_attributes:
            table_data.append(KeyValuePair(key, value))

        palettes = kwargs.get("palettes")
        for key, value in palettes:
            table_data.append(KeyValuePair(key, value))

        # Move Costs
        move_costs = kwargs.get("move_costs")
        for key, value in move_costs:
            table_data.append(KeyValuePair(key, value))

        # Audio
        music_list = kwargs.get("music_list")
        for key, value in music_list:
            table_data.append(KeyValuePair(key, value))

        table_data.sort(key=lambda pair: pair.key)
        return table_data

    def generate_palettes_pairs(self, **kwargs):
        table_data = []

        palettes = kwargs.get("palettes")
        for key, value in palettes:
            table_data.append(KeyValuePair(key, value))

        table_data.sort(key=lambda pair: pair.key)
        return table_data

    def generate_cosmetics_pairs(self, **kwargs):
        table_data = []

        cosmetic_options = kwargs.get("cosmetics")
        for option in cosmetic_options:
            table_data.append(
                KeyValuePair(
                    Option.get(Option.name == option).get_key(),
                    cosmetic_options[option]
                )
            )

        table_data.sort(key=lambda pair: pair.key)
        return table_data
    
    def generate_audio_option_pairs(self, **kwargs):
        table_data = []

        cosmetic_options = kwargs.get("audio_options")
        for option in cosmetic_options:
            table_data.append(
                KeyValuePair(
                    Option.get(Option.name == option).get_key(),
                    cosmetic_options[option]
                )
            )

        table_data.sort(key=lambda pair: pair.key)
        return table_data


    def create(self):
        self.info = get_table_info()
