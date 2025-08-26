import json

from peewee import *
from playhouse.sqlite_ext import JSONField
from db.db import db


class ActorAttribute(Model):
    area_id = IntegerField()
    actor_id = IntegerField()
    index = IntegerField()

    actor_name = CharField()
    attribute = CharField()
    value = IntegerField()

    def __str__(self):
        return f"{self.actor_name}[{self.attribute}] = {self.value}"

    def get_key(self):
        return (ActorAttribute._meta.key_type << 24) | (self.area_id << 16) | (self.actor_id << 8) | self.index

    class Meta:
        database = db
        key_type = 0xA2


# Run this to create all actors in ActorAttribute table
def create_actor_attributes():
    db.drop_tables([ActorAttribute])
    db.create_tables([ActorAttribute])

    with open("./debug/keys.json", "r") as file:
        actor_keys = json.load(file)["actors"]

    with open("./debug/values.json", "r") as file:
        actor_values = json.load(file)["actors"]

    for actor_data in actor_keys.values():
        for attribute,data in actor_data.items():
            value = actor_values[data["name"]][attribute]

            actor_attribute,created = ActorAttribute.get_or_create(
                area_id=data["area_id"],
                actor_id=data["actor_id"],
                index=data["value_id"],
                actor_name=data["name"],
                defaults={
                    "attribute": attribute,
                    "value": value,
                }
            )

            print(actor_attribute, created)