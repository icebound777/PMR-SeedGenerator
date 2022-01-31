import json

from peewee import *
from db.db import db


class Actor(Model):
    actor_name = CharField()
    pointer = IntegerField()

    class Meta:
        database = db

# Run this to create all actors in Actor table
def create_actors():
    db.drop_tables([Actor])
    db.create_tables([Actor])

    with open("./debug/values.json", "r") as file:
        actor_values = json.load(file)["actors"]
    
    for actor_name, actor_data in actor_values.items():
        if "Pointer" in actor_data:
            actor,created = Actor.get_or_create(
                actor_name=actor_name,
                pointer=actor_data["Pointer"],
            )

        print(actor, created)
