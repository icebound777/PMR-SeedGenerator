import json

from peewee import *

from db.db import db

class Battle(Model):
    # name
    name = CharField()
    # unmodified battleID
    vanilla_battle_id = IntegerField()

    def get_key(self):
        return (Battle._meta.key_type << 24) | self.vanilla_battle_id

    class Meta:
        database = db
        key_type = 0xA9


def create_battles():
    db.drop_tables([Battle])
    db.create_tables([Battle])

    with open("./debug/keys.json", "r") as file:
        battle_keys = json.load(file)["battles"]

    with open("./debug/values.json", "r") as file:
        battle_values = json.load(file)["battles"]

    # Create battle info
    for data in battle_keys.values():
        Battle.get_or_create(
            name = data["name"],
            vanilla_battle_id = battle_values[data["name"]]
        )
