import json

from peewee import *
from playhouse.sqlite_ext import JSONField
from db.db import db


class Actor(Model):
    area_id = IntegerField()
    map_id = IntegerField()
    index = IntegerField()

    name = CharField()
    level = IntegerField(null=True)
    hp = IntegerField(null=True)
    increment = IntegerField(null=True)
    damage = JSONField(default={})

    def __str__(self):
        return self.name

    def get_key(self):
        return (Item._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index

    class Meta:
        database = db
        key_type = 0xA2


# Run this to create all actors in Actor table
def create_actors():
    db.drop_tables([Actor])
    db.create_tables([Actor])

    with open("./debug/keys.json", "r") as file:
        actor_keys = json.load(file)["actors"]

    with open("./debug/values.json", "r") as file:
        actor_values = json.load(file)["actors"]

    for key,actor_data in actor_keys.items():
        for attribute,data in actor_data.items():
            value = actor_values[data["name"]][attribute]

            actor,created = Actor.get_or_create(
                area_id=data["area_id"],
                map_id=data["map_id"],
                index=data["value_id"],
                name=data["name"]
            )

            if attribute.startswith("Damage"):
                actor.damage[attribute] = value
            elif attribute == "HP":
                actor.hp = value
            elif attribute == "Level":
                actor.level = value
            elif attribute == "Increment":
                actor.increment = value
            actor.save()

            print(actor, created)










    