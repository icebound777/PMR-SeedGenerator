import json
import xml.etree.ElementTree as ET

from table import Table


# Generate a dictionary: {"MAP_XX": "Pretty Map Name"}
pretty_names = {}
xml_tree = ET.parse("../map/MapTable.xml")
root = xml_tree.getroot()
done = False
for child in root.iter():
	if child.tag == "Area":
		for sub_child in child:
			if "nickname" in sub_child.attrib:
				pretty_names[sub_child.attrib["name"].upper()] = sub_child.attrib["nickname"]


class Entrance:
	entrances = {}

	def __init__(self, map_instance, **kwargs):
		self.map = map_instance
		self.value = kwargs.get("value")
		self.byte_id = (kwargs["key"] & 0xFF000000) >> 24
		self.area_id = (kwargs["key"] & 0x00FF0000) >> 16
		self.map_id =  (kwargs["key"] & 0x0000FF00) >> 8
		self.entry_id = (kwargs["key"] & 0x000000FF)
		self.key = (self.byte_id << 24 | self.area_id << 16 | self.map_id << 8 | self.entry_id)

		if self.map.name not in Entrance.entrances:
			Entrance.entrances[self.map.name] = {}
		Entrance.entrances[self.map.name][self.entry_id] = self

	def __str__(self):
		return f"[{self.map}] Entrance 0x{self.key:0X} : 0x{self.value:0X}"

	def swap(self, other):
		rom_table = Table.instance

		with open("./maps/default_linkages.json", "r") as file:
			linkages = json.load(file)

		exit1 = linkages[self.map.name][str(self.entry_id)]
		exit2 = linkages[other.map.name][str(other.entry_id)]

		link1 = (exit1, linkages[exit1["dest_map"]][str(exit1["dest_entry"])])
		link2 = (exit2, linkages[exit2["dest_map"]][str(exit2["dest_entry"])])

		# Linkage 1
		e1 = rom_table["Entrance"][link1[0]["dest_map"]][int(link1[0]["dest_entry"])]
		e2 = rom_table["Entrance"][link2[0]["dest_map"]][int(link2[0]["dest_entry"])]

		# Linkage 2
		e3 = rom_table["Entrance"][link2[1]["dest_map"]][int(link2[1]["dest_entry"])]
		e4 = rom_table["Entrance"][link1[1]["dest_map"]][int(link1[1]["dest_entry"])]

		# Swap exits
		e1["value"] = e2["value"]
		e3["value"] = e4["value"]

class Map:
	maps = {}

	def __init__(self, name):
		self.name = name.upper()
		Map.maps[self.name] = self

		# Create Entrances for this map
		for entrance,data in Table.instance.db["Entrance"][self.name].items():
			Entrance(self, **data)

	def __str__(self):
		return f"{self.name} - {pretty_names[self.name]}"

	def entrances(self):
		entrances = []
		for entrance in Entrance.entrances.values():
			if entrance.map is self:
				entrances.append(entrance)
		return entrances
