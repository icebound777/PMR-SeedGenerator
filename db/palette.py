import json

from peewee import *

from db.db import db


class Palette(Model):
    dbkey = IntegerField(null=False)
    sprite = CharField(null=False)
    palette_count = IntegerField(null=False)

    def __str__(self):
        return f"Palette:{self.sprite},Count:{self.palette_count}"

    def get_key(self):
        return (self.dbkey)

    class Meta:
        database: db
        key_type = 0xA4


def create_palettes():
    db.drop_tables([Palette])
    db.create_tables([Palette])

    with open("./debug/keys.json", "r") as file:
        palette_keys = json.load(file)["palettes"]
    
    for key, data in palette_keys.items():
        palette, created = Palette.get_or_create(
            dbkey = key,
            sprite = data["sprite"],
            palette_count = data["palette_count"]
        )
        print(palette, created)
