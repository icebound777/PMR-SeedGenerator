from parse import get_default_table, create_table, get_table_info

from db.option import Option
from db.entrance import Entrance
from db.item import Item
from db.item_price import ItemPrice


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

	def generate_pairs(self):
		table_data = []
		for option in Option.select():
			table_data.append({
				"key": option.get_key(),
				"value": option.value,
			})
		for entrance in Entrance.select():
			if entrance.destination is not None:
				table_data.append({
					"key": entrance.get_key(),
					"value": entrance.destination.get_key(),
				})
		for item in Item.select():
			table_data.append({
				"key": item.get_key(),
				"value": item.value,
			})
		for item_price in ItemPrice.select():
			table_data.append({
				"key": item_price.get_key(),
				"value": item_price.value,
			})
		table_data.sort(key=lambda pair: pair["key"])
		return table_data

	def create(self):
		self.default_db = get_default_table()
		self.db = create_table(self.default_db)
		self.info = get_table_info()

	def items(self):
		return self.db.items()
