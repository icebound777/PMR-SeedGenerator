import re

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
    entrances = {}
    with open("../globals/patch/RandomEntrances.patch", "r") as file:
        for line in file:
            if match := re.match(r"#export\s*.DBKey:Entrance:(\S*):(\S*)\s*(\S*)", line):
                map_name = match.group(1)
                map_exit = int(match.group(2), 16)
                key = match.group(3)
                byte_id = int(key[0:2], 16)
                area_id = int(key[2:4], 16)
                map_id =  int(key[4:6], 16)
                entry_id =  int(key[6:8], 16)

                if map_name not in entrances:
                    entrances[map_name] = {}
                entrances[map_name][map_exit] = {
                    "byte_id": byte_id,
                    "area": area_id,
                    "map": map_id,
                    "entry": entry_id,
                }

    for map_name,entrances in entrances.items():
        for data in entrances.values():
            map_area,created = MapArea.get_or_create(
                area_id=data["area"],
                map_id=data["map"],
                name=map_name,
                verbose_name=MapArea.get_verbose_name(map_name)
            )

            print(map_area, created)

            entrance,created = Entrance.get_or_create(
                map_name=map_name,
                area_id=data["area"],
                map_id=data["map"],
                index=data["entry"],
                map_area=map_area,
            )

            print(entrance, created)


# Run this once to modify entrances with correct destination and type data
def connect_entrances():
    with open("./maps/links.csv", "r") as file:
        columns = file.readline().strip().split(",")
        links = []
        for i,line in enumerate(file.readlines()):
            values = line.strip().split(",")
            links.append({
                "src": (values[0], int(values[1])),
                "dest": (values[2], int(values[3])),
                "type": values[4],
                "index": i,
            })

        for link in links:
            src = Entrance.get(Entrance.map_name==link["src"][0].upper(), Entrance.index==link["src"][1])
            dest = Entrance.get(Entrance.map_name==link["dest"][0].upper(), Entrance.index==link["dest"][1])

            src.destination = dest
            src.entrance_type = link["type"]
            src.save()

            dest.destination = src
            dest.entrance_type = link["type"]
            dest.save()




