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
    def __init__(self, id):
        self.id = id


class Map:
    maps = {}

    def __init__(self, name):
        self.name = name.upper()
        Map.maps[self.name] = self

    def __str__(self):
        return f"{self.name} - {pretty_names[self.name]}"

    def entrances(self):
        entrances = []
        for map_name,data in Table.instance.db["Entrance"][self.name].items():
            entrances.append(data)
        return entrances
