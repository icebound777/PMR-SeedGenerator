import re
import os
import sys
import json
import time
import shutil
import random
import threading
import configparser

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


from enums import Enums
from logic import shuffle_entrances
from starrod import sr_dump, sr_copy, sr_compile
from parse import get_default_table, get_table_info, create_table

from table import Table

from maps.map import Map
from items.item import Item



class Stream(QtCore.QObject):
	newText = QtCore.pyqtSignal(str)

	def write(self, text):
		self.newText.emit(str(text))


class Window(QMainWindow):

	def __init__(self, app):
		super().__init__()

		# Setup
		self.app = app
		self.setGeometry(0, 0, 800, 600)
		self.setWindowTitle("Paper Mario Open World Randomizer")

		# Move to center of window
		rectangle = self.frameGeometry()
		center_point = QDesktopWidget().availableGeometry().center()
		rectangle.moveCenter(center_point)
		self.move(rectangle.topLeft())

		# Actions
		self.action_select_rom = QAction("&Select ROM", self)
		self.action_select_rom.triggered.connect(self.select_rom)
		self.action_randomize = QAction("&Randomize", self)
		self.action_randomize.triggered.connect(self.randomize)

		# Create Menu Bar
		self.menu_bar = self.menuBar()

		# Add File Menu
		self.menu_file = QMenu("&File", self)
		self.menu_file.addAction(self.action_select_rom)
		self.menu_file.addAction(self.action_randomize)
		self.menu_bar.addMenu(self.menu_file)

		# Create log box
		self.log = QTextEdit()
		self.log.moveCursor(QtGui.QTextCursor.Start)
		self.log.ensureCursorVisible()
		self.log.setLineWrapColumnOrWidth(500)
		self.log.setLineWrapMode(QTextEdit.FixedPixelWidth)
		self.log.setReadOnly(True)

		# Layout
		self.main_widget = QWidget(self)
		self.setCentralWidget(self.main_widget)
		layout = QHBoxLayout(self.main_widget)
		layout.addWidget(self.log)

		# Pipe stdout into this thingy
		self.stream = Stream(newText=self.on_update_text)
		sys.stdout = self.stream

		self.show()
		self.configure()

	def on_update_text(self, text):
		cursor = self.log.textCursor()
		cursor.movePosition(QtGui.QTextCursor.End)
		cursor.insertText(text)
		self.log.setTextCursor(cursor)
		self.log.ensureCursorVisible()

	def configure(self):
		# Read configuration data
		self.config = configparser.ConfigParser()
		self.config.read("./config.ini")
		self.sr_path = self.config.get("starrod", "path")
		self.seed_str = self.config.get("options", "seed")

		# Initialize Random Seed
		self.seed = hash(self.seed_str) & 0xFFFFFFFF
		random.seed(self.seed)

		# Create enums
		for name in os.listdir("../globals/enum/"):
			name = name.split(".")[0]
			Enums(f"../globals/enum/{name}.enum")

		# Check if the ROM already exists in the correct location
		rom_exists = False
		for filename in os.listdir("../ROM"):
			if filename == "PM64.z64":
				rom_exists = True
				break
		if not rom_exists:
			self.select_rom()
			if self.rom_path:
				shutil.copyfile(self.rom_path, "../ROM/PM64.z64")
		else:
			self.display(f"Successfully found ROM")

	def display(self, message):
		self.statusBar().showMessage(message)

	def select_rom(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.rom_path, _ = QFileDialog.getOpenFileName(self, "Select ROM", "./", "z64(*.z64)", options=options)

	def randomize(self):
		sr = False

		# Ensure we've dumped a ROM, copied its contents to the mod folder, and compiled it
		if sr:
			thread = sr_dump(self.sr_path, console=True)
			while thread.is_alive():
				self.app.processEvents()
			thread = sr_copy(self.sr_path, console=True)
			while thread.is_alive():
				self.app.processEvents()
			thread = sr_compile(self.sr_path, console=True)
			while thread.is_alive():
				self.app.processEvents()

		# TODO: Be smart and figure out why the text printed after this overlaps the stuff above even though it shouldn't

		# Create the ROM table
		rom_table = Table()
		rom_table.create()

		# Create Maps
		for map_name in rom_table["Entrance"]:
			Map(map_name)

		# Create Items
		for table,table_data in rom_table.items():
			for name,data in table_data.items():
				if data.get("enum_type") == "Item":
					Item(data)

		# Test - List all items
		"""
		print("List of all items:")
		for key,item in Item.items.items(): # Hooray for confusing syntax
			print(item)
		"""

		# Test - Swap two items
		item1 = Item.items[2701197584] # ShopItemA
		item2 = Item.items[2701526790] # NOK_14 HiddenItemA 
		item1.swap(item2)

		# Set every entrance pointing to MAC_00 to go to instead
		mac_00 = Map.maps["MAC_00"]
		for entrance in mac_00.entrances():
			entrance["value"] = 0xA3000000

		# Create a sorted list of key:value pairs to be written into the ROM
		table_data = []
		for table,data in rom_table.items():
			for _,pair in data.items():
				pairs = [pair]
				if "key" not in pair:
					pairs = []
					for sub_dict in pair.values():
						pairs.append(sub_dict)
				table_data.extend(pairs)
		table_data.sort(key=lambda pair: pair["key"])

		# Update table info with variable data
		rom_table.info["num_entries"] = len(table_data)
		rom_table.info["seed"] = self.seed

		# Write data to log file
		with open("./debug/log.txt", "w") as log:
			log.write("OPTIONS:\n\n")
			log.write(f"Seed: 0x{self.seed:0X} \"{self.seed_str}\"\n")
			for name,data in rom_table["Options"].items():
				log.write(f"{name:20}: {data['value']}\n")
			log.write("\n")

		# Modify the table data in the ROM
		with open("../out/PM64.z64", "r+b") as file:

			# Write the header
			file.seek(rom_table.info["address"])
			file.write(rom_table.info["magic_value"].to_bytes(4, byteorder="big"))
			file.write(rom_table.info["header_size"].to_bytes(4, byteorder="big"))
			file.write(rom_table.info["num_entries"].to_bytes(4, byteorder="big"))
			file.write(rom_table.info["seed"].to_bytes(4, byteorder="big"))

			# Write table data and generate log file
			file.seek(rom_table.info["address"] + rom_table.info["header_size"])
			with open("./debug/log.txt", "a") as log:
				log.write("ITEM CHANGES:\n\n")

				for pair in table_data:
					key_int = pair["key"].to_bytes(4, byteorder="big")
					value_int = pair["value"].to_bytes(4, byteorder="big")
					file.write(key_int)
					file.write(value_int)
					if enum_type := pair.get("enum_type"):
						if enum_type == "Item":
							column_left = f"[{pair['table']}][{pair['attribute']}]"
							original_item_id = rom_table.default_db[pair["table"]][pair['attribute']]["value"]
							original_item = Enums.get("Item")[original_item_id]
							column_right = f"{original_item} -> {Enums.get('Item')[pair['value']]}"
							log_statement = f"{column_left:25} : {column_right}"
							log.write(log_statement + "\n")
						if enum_type == "Entrance":
							pass #print(pair)

		# Dump the data we used for randomization
		with open("./debug/default_db.json", "w") as file:
			json.dump(rom_table.default_db, file, indent=4)
		with open("./debug/db.json", "w") as file:
			json.dump(rom_table.db, file, indent=4)

		self.display("Created Randomized ROM!")


app = QApplication(sys.argv)
window = Window(app)
sys.exit(app.exec_())