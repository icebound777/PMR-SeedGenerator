"""Userinterface for controlling the randomizer."""
import os
import sys
import shutil
import random
import hashlib
import sqlite3 as sql
import configparser

from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, uic

from custom_seed import CUSTOM_SEED_PATH, generate as custom_seed_generate
import randomizer
from optionset import OptionSet, get_option_keyvalue_dict

from enums import Enums
from utility import sr_dump, sr_copy, sr_compile
from rando_modules.logic import place_items

from db.option import Option


# Get application path based on if running as script or EXE
# https://stackoverflow.com/a/42615559
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    APP_PATH = sys._MEIPASS
    COMPILED = True
else:
    APP_PATH = os.path.dirname(os.path.abspath(__file__))
    COMPILED = False

randomizer.init_randomizer(rebuild_database=False)


class Stream(QtCore.QObject):
    """Defines the text output"""
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        """Defines how to write to this stream."""
        self.newText.emit(str(text))


class Window(QMainWindow):
    """The main GUI window."""
    def __init__(self, app):
        super(Window, self).__init__()
        uic.loadUi("gui/main.ui", self)

        # Icons
        self.setWindowIcon(QtGui.QIcon("gui/icons/random_bag.ico"))
        self.tabwidget.setTabIcon(0, QtGui.QIcon("gui/icons/book.ico"))
        self.tabwidget.setTabIcon(1, QtGui.QIcon("gui/icons/fireflower.ico"))
        self.tabwidget.setTabIcon(2, QtGui.QIcon("gui/icons/pupddown.ico"))

        # Warning icons for options that cause a big difficulty spike
        self.chk_include_coins.setIcon(QtGui.QIcon("gui/icons/allornothing.ico"))
        self.radio_damage_4.setIcon(QtGui.QIcon("gui/icons/allornothing.ico"))
        self.chk_ohko.setIcon(QtGui.QIcon("gui/icons/allornothing.ico"))
        self.radio_by_all.setIcon(QtGui.QIcon("gui/icons/allornothing.ico"))

        # Setup
        self.setWindowTitle("Paper Mario Open World Randomizer")
        self.seed = None
        self.app = app
        self.app.setStyle("Fusion")
        self.progress_bar.setVisible(False)

        # Buttons
        self.button_compile.clicked.connect(self.compile_mod)
        self.button_load_settings.clicked.connect(self.load_settings)
        self.button_save_settings.clicked.connect(self.save_settings)
        self.button_randomize.clicked.connect(self.randomize)
        self.button_about.clicked.connect(self.about)
        self.button_generate.clicked.connect(self.generate_seed)

        self.button_compile.setIcon(QtGui.QIcon("gui/icons/calculator.ico"))
        self.button_load_settings.setIcon(QtGui.QIcon("gui/icons/load.ico"))
        self.button_save_settings.setIcon(QtGui.QIcon("gui/icons/save.ico"))
        self.button_randomize.setIcon(QtGui.QIcon("gui/icons/random_bag.ico"))
        self.button_about.setIcon(QtGui.QIcon("gui/icons/book.ico"))

        # CSS skillz
        self.button_compile.setStyleSheet("QPushButton { text-align: left; "\
                                          "padding: 0px 10px 0px 10px;}")
        self.button_load_settings.setStyleSheet("QPushButton { text-align: left; "\
                                                "padding: 0px 10px 0px 10px;}")
        self.button_save_settings.setStyleSheet("QPushButton { text-align: left; "\
                                                "padding: 0px 10px 0px 10px;}")
        self.button_randomize.setStyleSheet("QPushButton { text-align: left; "\
                                            "padding: 0px 10px 0px 10px;}")
        self.button_about.setStyleSheet("QPushButton { text-align: left; "\
                                        "padding: 0px 10px 0px 10px;}")

        # Move to center of window
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

        self.show()
        self.configure()

        # Log
        self.log.moveCursor(QtGui.QTextCursor.Start)
        self.log.ensureCursorVisible()
        self.stream = Stream(newText=self.on_update_text)
        sys.stdout = self.stream

        # Check if custom seed file exists in the correct location
        try:
            with open(CUSTOM_SEED_PATH, "r", encoding="utf-8") as _:
                self.display("Custom seed file found")
        except FileNotFoundError:
            self.display("Generating default custom seed file...")
            custom_seed_generate()
            self.display("Custom seed file generated")

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
            self.display("Successfully found ROM")

    def on_update_text(self, text):
        """Print text to combobox whenever it is updated."""
        cursor = self.log.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.log.setTextCursor(cursor)
        self.log.ensureCursorVisible()

    def generate_seed(self):
        """Generate a random string for the seed."""
        items = set()
        while len(items) < 4:
            item_str = Enums.get("Item")[random.randrange(0x80, 0xE0)]
            item_str = "".join([c for c in item_str if c.isalpha()])
            items.add(item_str)
        self.edit_seed.setText("".join(items))

    def about(self):
        """Shows a short 'about' section window."""
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("gui/icons/book.ico"))
        msg.setWindowTitle("About")
        msg.setText(
            "This is an open world randomizer for Paper Mario 64.\n" \
            "It's pretty neat."
        )
        msg.exec_()

    def load_settings(self):
        """Loads randomizer options from file using a file dialogue."""
        # Prompt user for a database to use for populating GUI widgets
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, is_ok = QFileDialog.getOpenFileName(self,
                                                      "Load Settings",
                                                      "",
                                                      "Settings Files (*.settings)",
                                                      options=options)

        if not is_ok:
            return

        # Update the temporary DB with data from this file
        options = {
            "InitialCoins": Option.get(Option.name == "InitialCoins"),
            "ReplaceDuplicateKeys": Option.get(Option.name == "ReplaceDuplicateKeys"),
            "DuplicateKeyReplacement": Option.get(Option.name == "DuplicateKeyReplacement"),
            "FlowerGateOpen": Option.get(Option.name == "FlowerGateOpen"),
            "BlueHouseOpen": Option.get(Option.name == "BlueHouseOpen"),
            "BlocksMatchContent": Option.get(Option.name == "BlocksMatchContent"),
            "SkipQuiz": Option.get(Option.name == "SkipQuiz"),
            "CapEnemyXP": Option.get(Option.name == "CapEnemyXP"),
            "2xDamage": Option.get(Option.name == "2xDamage"),
            "4xDamage": Option.get(Option.name == "4xDamage"),
            "OHKO": Option.get(Option.name == "OHKO"),
            # Items Tab
            "ShuffleItems": Option.get(Option.name == "ShuffleItems"),
            "IncludeCoins": Option.get(Option.name == "IncludeCoins"),
            "IncludeShops": Option.get(Option.name == "IncludeShops"),
            "IncludePanels": Option.get(Option.name == "IncludePanels"),
            # Entrances Tab
            "ShuffleEntrances": Option.get(Option.name == "ShuffleEntrances"),
            "ShuffleEntrancesByArea": Option.get(Option.name == "ShuffleEntrancesByArea"),
            "ShuffleEntrancesByAll": Option.get(Option.name == "ShuffleEntrancesByAll"),
            "MatchEntranceTypes": Option.get(Option.name == "MatchEntranceTypes"),
        }

        connection = sql.connect(filename)
        cursor = connection.cursor()
        for name,option in options.items():
            cursor.execute(f"SELECT * FROM option WHERE name = '{name}' LIMIT 1")
            result = cursor.fetchone()
            option.value = result[-1] # Set to value in settings database provided
            option.save()

        self.configure()
        self.display(f"Loaded: {filename}")

    def save_settings(self):
        """Writes randomizer options to file using a file dialogue."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, is_ok = QFileDialog.getSaveFileName(self,
                                                      "Save Settings",
                                                      "",
                                                      "Settings Files (*.settings)",
                                                      options=options)
        if is_ok:
            if not filename.endswith(".settings"):
                filename += ".settings"

            self.update_db()
            shutil.copy("db.sqlite", filename)
            self.display(f"Saved: {filename}")

    def save_rom(self):
        """Writes the modified ROM to file using a file dialogue."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, is_ok = QFileDialog.getSaveFileName(self,
                                                      "Save Randomized ROM",
                                                      "PM64.z64",
                                                      "Settings Files (*.z64)",
                                                      options=options)
        if is_ok:
            if not filename.endswith(".z64"):
                filename += ".z64"

            shutil.copy("../out/PM64.z64", filename)
            self.display(f"Saved: {filename}")

    def configure(self):
        """Set initial values of UI elements using config file."""
        # Read configuration data
        self.config = configparser.ConfigParser()
        self.config.read("./config.ini")
        self.sr_path = self.config.get("starrod", "path")

        # Seed
        self.edit_seed.setText(self.config.get("options", "seed"))

        # Initial Coin Amount
        self.edit_coins.setText(str(Option.get(Option.name == "InitialCoins").value))
        self.edit_coins.setValidator(QtGui.QIntValidator())

        # Duplicate Key Replacement
        self.chk_replace_keys.setChecked(Option.get(Option.name == "ReplaceDuplicateKeys").value)
        self.chk_replace_keys.clicked.connect(
            lambda checked: self.combo_replace.setEnabled(checked)
        )
        self.combo_replace.setEnabled(self.chk_replace_keys.isChecked())

        # Get all regular item names
        self.item_choices = []

        #for item_id in range(0x01, 0x16D):
        #    name = Enums.get("Item")[item_id]
        #    if Item.get_type(item_id) == "ITEM":
        #        self.item_choices.append((name, item_id))

        self.item_choices.append(("Mistake", 0xC2))
        self.item_choices.append(("Coin", 0x157))

        # Sort alphabetically and populate combobox
        self.item_choices.sort(key=lambda t: t[0])
        for choice in self.item_choices:
            self.combo_replace.addItem(choice[0])

        # Get the default item ID for replacement and select that index
        db_item_id = Option.get(Option.name == "DuplicateKeyReplacement").value
        for i,(_,item_id) in enumerate(self.item_choices):
            if item_id == db_item_id:
                self.combo_replace.setCurrentIndex(i)
                break

        # Checkboxes
        self.chk_flower_gate.setChecked(Option.get(Option.name == "FlowerGateOpen").value)
        self.chk_blue_house.setChecked(Option.get(Option.name == "BlueHouseOpen").value)
        self.chk_blocks_content.setChecked(Option.get(Option.name == "BlocksMatchContent").value)
        self.chk_skip_quiz.setChecked(Option.get(Option.name == "SkipQuiz").value)
        self.chk_cap_xp.setChecked(Option.get(Option.name == "CapEnemyXP").value)

        # Radioboxes
        self.chk_ohko.setChecked(Option.get(Option.name == "OHKO").value)
        self.radio_damage_4.setChecked(Option.get(Option.name == "4xDamage").value)
        self.radio_damage_2.setChecked(Option.get(Option.name == "2xDamage").value)
        self.radio_damage_1.setChecked(all([
            not self.radio_damage_4.isChecked(),
            not self.radio_damage_2.isChecked(),
        ]))

        # Item Options
        self.chk_shuffle_items.setChecked(Option.get(Option.name == "ShuffleItems").value)
        self.chk_include_coins.setChecked(Option.get(Option.name == "IncludeCoins").value)
        self.chk_include_shops.setChecked(Option.get(Option.name == "IncludeShops").value)
        self.chk_include_panels.setChecked(Option.get(Option.name == "IncludePanels").value)

        # Entrance Options
        self.chk_shuffle_entrances.setChecked(Option.get(Option.name == "ShuffleEntrances").value)
        self.radio_by_area.setChecked(Option.get(Option.name == "ShuffleEntrancesByArea").value)
        self.radio_by_all.setChecked(Option.get(Option.name == "ShuffleEntrancesByAll").value)
        self.chk_match_types.setChecked(Option.get(Option.name == "MatchEntranceTypes").value)

        # Ensure ShuffleItems is checked if extra item options are selected
        def update(checked):
            if checked:
                self.chk_shuffle_items.setChecked(True)
        self.chk_include_coins.clicked.connect(lambda checked: update(checked))
        self.chk_include_shops.clicked.connect(lambda checked: update(checked))
        self.chk_include_panels.clicked.connect(lambda checked: update(checked))

        # Disable/Enable extra item options when ShuffleItems changes
        def reset(checked, chk_widget):
            if not checked:
                chk_widget.setChecked(False)
                chk_widget.setEnabled(False)
            else:
                chk_widget.setEnabled(True)
        self.chk_shuffle_items.clicked.connect(
            lambda checked: reset(checked, self.chk_include_coins)
        )
        self.chk_shuffle_items.clicked.connect(
            lambda checked: reset(checked, self.chk_include_shops)
        )
        self.chk_shuffle_items.clicked.connect(
            lambda checked: reset(checked, self.chk_include_panels)
        )

        # Disable Entrance options if ShuffleEntrances is unchecked
        def update_entrance_widgets(checked):
            if not checked:
                self.radio_by_area.setChecked(False)
                self.radio_by_all.setChecked(False)
                self.radio_by_area.setEnabled(False)
                self.radio_by_all.setEnabled(False)
                self.chk_match_types.setChecked(False)
                self.chk_match_types.setEnabled(False)
            else:
                self.radio_by_area.setEnabled(True)
                self.radio_by_all.setEnabled(True)
                self.chk_match_types.setEnabled(True)
                self.radio_by_area.setChecked(True)
        self.chk_shuffle_entrances.clicked.connect(lambda checked: update_entrance_widgets(checked))

    def display(self, message):
        """Displays given message in status bar."""
        self.statusBar().showMessage(message)

    def select_rom(self):
        """Selects ROM using file dialogue."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.rom_path, _ = QFileDialog.getOpenFileName(self,
                                                       "Select ROM",
                                                       "./",
                                                       "z64(*.z64)",
                                                       options=options)

    def compile_mod(self):
        """Compiles a modded ROM using StarRod."""
        self.log.clear()
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("Dumping ROM")
        thread = sr_dump(self.sr_path, console=True)
        while thread.is_alive():
            self.app.processEvents()

        self.progress_bar.setValue(33)
        self.progress_bar.setFormat("Copying ROM")
        thread = sr_copy(self.sr_path, console=True)
        while thread.is_alive():
            self.app.processEvents()

        self.progress_bar.setValue(66)
        self.progress_bar.setFormat("Compiling ROM")
        thread = sr_compile(self.sr_path, console=True)
        while thread.is_alive():
            self.app.processEvents()

        self.progress_bar.setVisible(False)
        self.display("Finished Compiling Mod")

    def update_options(self):
        rando_settings = OptionSet()

        """Get option defaults from sqlite database."""
        options = {
            "InitialCoins": get_option_keyvalue_dict("InitialCoins"),
            "ReplaceDuplicateKeys": get_option_keyvalue_dict("ReplaceDuplicateKeys"),
            "DuplicateKeyReplacement": get_option_keyvalue_dict("DuplicateKeyReplacement"),
            "FlowerGateOpen": get_option_keyvalue_dict("FlowerGateOpen"),
            "BlueHouseOpen": get_option_keyvalue_dict("BlueHouseOpen"),
            "BlocksMatchContent": get_option_keyvalue_dict("BlocksMatchContent"),
            "SkipQuiz": get_option_keyvalue_dict("SkipQuiz"),
            "CapEnemyXP": get_option_keyvalue_dict("CapEnemyXP"),
            "2xDamage": get_option_keyvalue_dict("2xDamage"),
            "4xDamage": get_option_keyvalue_dict("4xDamage"),
            "OHKO": get_option_keyvalue_dict("OHKO"),
            # Items Tab
            "ShuffleItems": get_option_keyvalue_dict("ShuffleItems"),
            "IncludeCoins": get_option_keyvalue_dict("IncludeCoins"),
            "IncludeShops": get_option_keyvalue_dict("IncludeShops"),
            "IncludePanels": get_option_keyvalue_dict("IncludePanels"),
            # Entrances Tab
            "ShuffleEntrances": get_option_keyvalue_dict("ShuffleEntrances"),
            "ShuffleEntrancesByArea": get_option_keyvalue_dict("ShuffleEntrancesByArea"),
            "ShuffleEntrancesByAll": get_option_keyvalue_dict("ShuffleEntrancesByAll"),
            "MatchEntranceTypes": get_option_keyvalue_dict("MatchEntranceTypes"),
        }

        # Update options with values from the GUI
        options["InitialCoins"]["value"] = int(self.edit_coins.text())
        options["ReplaceDuplicateKeys"]["value"] = self.chk_replace_keys.isChecked()
        options["DuplicateKeyReplacement"]["value"] = \
            self.item_choices[self.combo_replace.currentIndex()][1]
        options["FlowerGateOpen"]["value"] = self.chk_flower_gate.isChecked()
        options["BlueHouseOpen"]["value"] = self.chk_blue_house.isChecked()
        options["BlocksMatchContent"]["value"] = self.chk_blocks_content.isChecked()
        options["SkipQuiz"]["value"] = self.chk_skip_quiz.isChecked()
        options["CapEnemyXP"]["value"] = self.chk_cap_xp.isChecked()
        options["2xDamage"]["value"] = self.radio_damage_2.isChecked()
        options["4xDamage"]["value"] = self.radio_damage_4.isChecked()
        options["OHKO"]["value"] = self.chk_ohko.isChecked()
        # Items Tab
        options["ShuffleItems"]["value"] = self.chk_shuffle_items.isChecked()
        options["IncludeCoins"]["value"] = self.chk_include_coins.isChecked()
        options["IncludeShops"]["value"] = self.chk_include_shops.isChecked()
        options["IncludePanels"]["value"] = self.chk_include_panels.isChecked()
        # Entrances Tab
        options["ShuffleEntrances"]["value"] = self.chk_shuffle_entrances.isChecked()
        options["ShuffleEntrancesByArea"]["value"] = self.radio_by_area.isChecked()
        options["ShuffleEntrancesByAll"]["value"] = self.radio_by_all.isChecked()
        options["MatchEntranceTypes"]["value"] = self.chk_match_types.isChecked()

        # Update OptionSet with chosen options
        rando_settings.update_options(options)

        return rando_settings

    def randomize(self):
        """
        Randomizes items etc. and writes them to ROM using the logic and
        randomizer modules.
        """
        self.log.clear()
        self.progress_bar.setVisible(True)

        # Initialize Random Seed
        md5_hash = hashlib.md5()
        md5_hash.update(self.edit_seed.text().lower().encode("utf-8"))
        self.seed = int(md5_hash.hexdigest()[0:8], 16)
        random.seed(self.seed)

        # Update database values from widgets
        selected_settings = self.update_options()

        # Item Placement
        placed_items = []
        for text,percent_complete in place_items(
            item_placement=placed_items,
            algorithm="ForwardFill",
            do_shuffle_items=selected_settings.shuffle_items["value"],
            do_randomize_coins=selected_settings.include_coins["value"],
            do_randomize_shops=selected_settings.include_shops["value"],
            do_randomize_panels=selected_settings.include_panels["value"],
            starting_map_id=selected_settings.starting_map["value"],
            startwith_bluehouse_open=selected_settings.bluehouse_open["value"],
            startwith_flowergate_open=selected_settings.flowergate_open["value"]
        ):
            self.progress_bar.setValue(percent_complete)
            self.progress_bar.setFormat(f"{text} ({percent_complete}%)")
            self.app.processEvents()

        # Make everything inexpensive
        randomizer.set_cheap_shopitems(placed_items)

        # Write data to ROM
        randomizer.write_data_to_rom(
            target_modfile="../out/PM64.z64",
            options=selected_settings,
            placed_items=placed_items,
            enemy_stats=[],
            battle_formations=[],
            move_costs=[],
            coin_palette_data=[],
            coin_palette_targets=[],
            music_list=[],
            seed=self.seed,
            edit_seed=self.edit_seed
        )

        # Write sorted spoiler log
        if selected_settings.write_spoilerlog:
            randomizer.write_spoiler_log(
                placed_items,
                do_pretty=selected_settings.pretty_spoilerlog
            )

        self.progress_bar.setVisible(False)
        self.progress_bar.setValue(0)
        self.display("Finished Randomizing ROM")

        if COMPILED:
            self.save_rom()

        # For dev use
        if not COMPILED:
            answer = QMessageBox.question(self,
                                          "Open ROM",
                                          "Open ROM with Default Application?",
                                          QMessageBox.Yes | QMessageBox.No)
            if answer == QMessageBox.Yes:
                os.startfile(APP_PATH + "/../out/PM64.z64")


app = QApplication(sys.argv)
window = Window(app)
sys.exit(app.exec_())
