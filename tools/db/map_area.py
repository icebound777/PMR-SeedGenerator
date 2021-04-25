import xml.etree.ElementTree as ET

from peewee import *
from playhouse.migrate import *
from db.db import db, migrator


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


class MapArea(Model):
    area_id = IntegerField()
    map_id = IntegerField()

    name = CharField()
    verbose_name = CharField(null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_verbose_name(cls, name):
        return pretty_names.get(name)

    class Meta:
        database = db

db.create_tables([MapArea])
