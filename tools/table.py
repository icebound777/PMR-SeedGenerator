from parse import get_default_table, create_table, get_table_info

from db.option import Option
from db.actor_attribute import ActorAttribute
from db.quiz import Quiz


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
        for option in Option.select():
            table_data.append({
                "key": option.get_key(),
                "value": option.value,
            })

        # Quizzes
        for quiz in Quiz.select():
            table_data.append({
                "key": quiz.get_key(),
                "value": quiz.value,
            })

        # Items
        placed_items = kwargs.get("items")
        for node in placed_items:
            if node.key_name_item is not None and node.current_item is not None:
                table_data.append({
                    "key": node.get_item_key(),
                    "value": node.current_item.value,
                })
                # Generate a ROM table pair that describes where a unique itemID
				# resides in the game using areaID and mapID
                if node.current_item.item_type in ["KEYITEM", "BADGE"]:
                    table_data.append({
                        "key": (0xA5 << 24) | (node.current_item.value),
                        "value": (node.map_area.area_id << 8) | (node.map_area.map_id),
                    })

            # Item Prices
            if node.key_name_price is not None and node.key_name_price.startswith("ShopPrice"):
                # TODO: Modify price value based on the item its tied to
                table_data.append({
                    "key": node.get_price_key(),
                    "value": node.current_item.base_price
                })

        # Actor Attributes
        for actor_attribute in ActorAttribute.select():
            table_data.append({
                "key": actor_attribute.get_key(),
                "value": actor_attribute.value,
            })

        table_data.sort(key=lambda pair: pair["key"])
        return table_data

    def create(self):
        self.default_db = get_default_table()
        self.db = create_table(self.default_db)
        self.info = get_table_info()

    def items(self):
        return self.db.items()
