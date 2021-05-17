import re
import json

from peewee import *
from playhouse.migrate import *

from db.db import db
from db.map_area import MapArea


class Entrance(Model):
    area_id = IntegerField()
    map_id = IntegerField()
    index = IntegerField()

    map_name = CharField()
    map_area = ForeignKeyField(MapArea, null=True, backref="entrances")
    entrance_type = CharField(null=True)
    destination = ForeignKeyField("self", null=True, related_name="source")

    def __str__(self):
        if self.destination is None:
            return f"{self.map_name}[{self.index}] -> None"
        return f"{self.map_name}[{self.index}] -> {self.destination.map_name}[{self.destination.index}]"

    def get_source(self):
        source = [entrance for entrance in self.source]
        if len(source) > 0:
            return source[0]
        return None

    def get_key(self):
        return (Entrance._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index

    @classmethod
    def get_entry_sources(self, map_name) -> list:
        ''' Get a list of Entrance objects that go to the specified map_name '''
        Parent = Entrance.alias()
        query = (Entrance
            .select()
            .join(Parent, on=(Entrance.destination == Parent.id))
            .where(Parent.map_name==map_name)
        )
        return list(query)

    class Meta:
        database = db
        key_type = 0xA3


# Run this to create all entrances in Entrance table
def create_entrances():
    db.drop_tables([Entrance])
    db.create_tables([Entrance])

    with open("./debug/keys.json", "r") as file:
        entrances = json.load(file)["entrances"]

    for key,data in entrances.items():
        # Create MapArea if neccessary
        map_area,created = MapArea.get_or_create(
            area_id=data["area_id"],
            map_id=data["map_id"],
            name=data["name"],
            verbose_name=MapArea.get_verbose_name(data["name"]),
        )
        # Create Entrance
        entrance,created = Entrance.get_or_create(
            map_name=data["name"],
            area_id=data["area_id"],
            map_id=data["map_id"],
            index=data["entrance"],
            map_area=map_area,
        )

