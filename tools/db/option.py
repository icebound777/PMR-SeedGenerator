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
    default_db = get_default_table()
    def create_from(filepath):
        with open(filepath, "r") as file:
            for line in file:
                if match := re.match(r"#export\s*.DBKey:Options:(\S*)\s*(\S*)", line):
                    attr = match.group(1)
                    key = match.group(2)
                    byte_id = int(key[0:2], 16)
                    area_id = int(key[2:4], 16)
                    map_id =  int(key[4:6], 16)
                    index =  int(key[6:8], 16)

                    data = default_db["Options"][attr]
                    option,created = Option.get_or_create(
                        name=attr,
                        value=data["value"],
                        area_id=area_id,
                        map_id=map_id,
                        index=index,
                    )

                    print(option, created)

    create_from("../globals/patch/DatabaseKeys.patch")
