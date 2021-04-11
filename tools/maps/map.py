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
        Entrance.entrances[self.key] = self

    def __str__(self):
        return f"[{self.map}] Entrance 0x{self.key:0X} : 0x{self.value:0X}"

class Map:
    maps = {}

    def __init__(self, name):
        self.name = name.upper()
        self.area_id = None
        self.map_id = None
        Map.maps[self.name] = self

        # Create Entrances for this map
        retrieved_map_info = False
        for entrance,data in Table.instance.db["Entrance"][self.name].items():
            if not retrieved_map_info:
                retrieved_map_info = True
                self.area_id = (data["key"] & 0x00FF0000) >> 16
                self.map_id = (data["key"] & 0x0000FF00) >> 8

            Entrance(self, **data)

    def __str__(self):
        return f"{self.name} - {pretty_names[self.name]}"

    def entrances(self):
        entrances = []
        for entrance in Entrance.entrances.values():
            if entrance.map is self:
                entrances.append(entrance)
        return entrances
