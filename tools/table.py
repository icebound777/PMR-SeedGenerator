from parse import get_default_table, create_table, get_table_info

from db.option import Option
from db.item import Item
from db.node import Node
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
		for node in Node.select().where(Node.key_name_item.is_null(False) & Node.current_item.is_null(False)):
			item = Item.get(Item.value == node.current_item.value)
			table_data.append({
				"key": node.get_item_key(),
				"value": item.value,
			})
			# Generate a ROM table pair that describes where a unique itemID resides in the game using areaID and mapID
			if item.item_type in ["KEYITEM", "BADGE"]:
				table_data.append({
					"key": (0xA5 << 24) | (item.value),
					"value": (node.map_area.area_id << 8) | (node.map_area.map_id),
				})

		# Item Prices
		for node in Node.select().where(Node.key_name_price.is_null(False) & Node.key_name_price.startswith("ShopPrice")):
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
