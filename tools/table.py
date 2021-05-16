from parse import get_default_table, create_table, get_table_info

from db.option import Option
from db.entrance import Entrance
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

		# Entrances
		if kwargs.get("entrances"):
			for entrance in Entrance.select():
				# Only include entrances that have destinations defined
				if entrance.destination is not None:
					table_data.append({
						"key": entrance.get_key(),
						"value": entrance.destination.get_key(),
					})

		# Items
		for node in Node.select().where(key_name_item.is_null(False) & current_item.is_null(False)):
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
		for node in Node.select().where(key_name_price.is_null(False) & key_name_price % "ShopItem%"):
			table_data.append({
				"key": node.get_price_key(),
				"value": node.current_item.base_price
			})

		for item_price in ItemPrice.select():
			# TODO: Modify price value based on the item its tied to
			item = item_price.itemlocation.get()

			table_data.append({
				"key": item_price.get_key(),
				"value": item_price.value,
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
