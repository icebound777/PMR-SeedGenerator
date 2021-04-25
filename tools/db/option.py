import json

from peewee import *
from playhouse.migrate import *
from db.db import db, migrator
from parse import get_default_table


class Option(Model):
    area_id = IntegerField()
    map_id = IntegerField()
    index = IntegerField()

    name = CharField()
    value = IntegerField()

    def __str__(self):
        return self.name

    def get_key(self):
        return (Option._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index

    class Meta:
        database = db
        key_type = 0xAF

# Run this to create all options in Option table
def create_options():
    db.drop_tables([Option])
    db.create_tables([Option])

    with open("./debug/keys.json", "r") as file:
        option_keys = json.load(file)["options"]

    with open("./debug/values.json", "r") as file:
        option_values= json.load(file)["options"]

    for key,data in option_keys.items():
        value = option_values[data["name"]]
        option,created = Option.get_or_create(
            name=data["name"],
            value=value,
            area_id=data["area_id"],
            map_id=data["map_id"],
            index=data["value_id"],
        )

        print(option, created)