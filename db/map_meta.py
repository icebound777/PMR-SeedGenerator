"""This model represents map metadata."""
import os
import xml.etree.ElementTree as ET

from peewee import *
from playhouse.migrate import *
from db.db import db


class MapMeta(Model):
    name = CharField(null=False)
    verbose_name = CharField(null=False)

    class Meta:
        database = db


def create_mapmeta():
    """Build or rebuilds the mapmeta db table."""
    db.drop_tables([MapMeta])
    db.create_tables([MapMeta])

    path_maptable = f"{__file__}/../../../../map/MapTable.xml"
    xml_tree = ET.parse(os.path.abspath(path_maptable))
    root = xml_tree.getroot()
    for child in root.iter():
        if child.tag == "Area":
            for sub_child in child:
                if "nickname" in sub_child.attrib:
                    MapMeta.get_or_create(
                        name = sub_child.attrib["name"].upper(),
                        verbose_name = sub_child.attrib["nickname"]
                    )
