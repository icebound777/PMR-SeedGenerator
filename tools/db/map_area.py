from peewee import *
from playhouse.migrate import *
from db.db import db, migrator


class MapArea(Model):
    area_id = IntegerField()
    map_id = IntegerField()

    name = CharField()

    def __str__(self):
        return self.name

    class Meta:
        database = db

db.create_tables([MapArea])
