import json

from peewee import *
from playhouse.sqlite_ext import JSONField
from db.db import db
from db.map_area import MapArea


class Quiz(Model):
    area_id = IntegerField()
    map_id = IntegerField()
    index = IntegerField()

    name = CharField()
    value = IntegerField()

    def __str__(self):
        return f"Quiz[{self.name}] = {self.value}"

    def get_key(self):
        return (Quiz._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index

    class Meta:
        database = db
        key_type = 0xAF


# Run this to create all actors in ActorAttribute table
def create_quizzes():
    db.drop_tables([Quiz])
    db.create_tables([Quiz])

    with open("./debug/keys.json", "r") as file:
        quiz_keys = json.load(file)["quizzes"]

    with open("./debug/values.json", "r") as file:
        quiz_values = json.load(file)["quizzes"]

    for key,data in quiz_keys.items():
        value = quiz_values[data["name"]]

        quiz,created = Quiz.get_or_create(
            area_id=data["area_id"],
            map_id=data["map_id"],
            index=data["value_id"],
            name=data["name"],
            value=value,
        )

        print(quiz, created)