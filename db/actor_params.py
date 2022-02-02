"""
Defines the model for actor parameters / stats and offers functionality to
rebuild that part of the sqlite db.
"""
import csv
import os

from peewee import CharField, IntegerField, Model
from playhouse.migrate import *
from db.db import db


class ActorParam(Model):
    """Model for actor parameters / stats."""
    key = CharField(null=False)
    actor_name = CharField(null=False)
    actor_stat_name = CharField(null=False)
    default_value = IntegerField(null=False)
    native_chapter = IntegerField(null=False)
    chapter_0 = IntegerField(null=False)
    chapter_1 = IntegerField(null=False)
    chapter_2 = IntegerField(null=False)
    chapter_3 = IntegerField(null=False)
    chapter_4 = IntegerField(null=False)
    chapter_5 = IntegerField(null=False)
    chapter_6 = IntegerField(null=False)
    chapter_7 = IntegerField(null=False)
    chapter_8 = IntegerField(null=False)

    class Meta:
        database = db


def create_actor_params():
    """Rebuild db table actorparam from Star Rod mod sources."""
    db.drop_tables([ActorParam])
    db.create_tables([ActorParam])

    ENEMY_STATS_CSV_PATH = f"{__file__}/../../../../res/actor_params.csv"
    ENEMY_STATS_CSV = os.path.abspath(ENEMY_STATS_CSV_PATH)
    with open(ENEMY_STATS_CSV, mode="r", encoding="utf-8") as csv_file:
        file_lines = []
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            file_lines.append(row)

    CSV_ID_KEY = 0
    CSV_ID_NATIVE_CH = 1
    CSV_ID_DEFAULT_VAL = 2
    CSV_ID_CH0 = 3
    CSV_ID_CH1 = 4
    CSV_ID_CH2 = 5
    CSV_ID_CH3 = 6
    CSV_ID_CH4 = 7
    CSV_ID_CH5 = 8
    CSV_ID_CH6 = 9
    CSV_ID_CH7 = 10
    CSV_ID_CH8 = 11


    for row in file_lines[1:]:
        dbkey_name = row[CSV_ID_KEY]
        actor_name = dbkey_name[dbkey_name.index(":")+1:dbkey_name.rindex(":")]
        actor_native_chapter = row[CSV_ID_NATIVE_CH]
        actor_stat_name = dbkey_name[dbkey_name.rindex(":")+1:]
        actor_stat_default_val = row[CSV_ID_DEFAULT_VAL]

        ActorParam.get_or_create(
            key = dbkey_name,
            actor_name = actor_name,
            actor_stat_name = actor_stat_name,
            default_value = actor_stat_default_val,
            native_chapter = actor_native_chapter,
            chapter_0 = row[CSV_ID_CH0],
            chapter_1 = row[CSV_ID_CH1],
            chapter_2 = row[CSV_ID_CH2],
            chapter_3 = row[CSV_ID_CH3],
            chapter_4 = row[CSV_ID_CH4],
            chapter_5 = row[CSV_ID_CH5],
            chapter_6 = row[CSV_ID_CH6],
            chapter_7 = row[CSV_ID_CH7],
            chapter_8 = row[CSV_ID_CH8],
        )
