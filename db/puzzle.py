import json

from peewee import *

from db.db import db

class Puzzle(Model):
    # name
    name = CharField()
    # default value
    default_value = IntegerField()
    # puzzle / minigame index
    index = IntegerField()

    def get_key(self):
        return (Puzzle._meta.key_type << 24) | self.index

    class Meta:
        database = db
        key_type = 0xA8


def create_puzzles():
    db.drop_tables([Puzzle])
    db.create_tables([Puzzle])

    with open("./debug/keys.json", "r") as file:
        puzzle_keys = json.load(file)["puzzles"]

    with open("./debug/values.json", "r") as file:
        puzzle_values = json.load(file)["puzzles"]

    for data in puzzle_keys.values():
        Puzzle.get_or_create(
            name=data["puzzle"],
            default_value=puzzle_values[data["puzzle"]],
            index=data["index"],
        )
