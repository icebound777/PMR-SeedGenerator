import json

from peewee import *

from db.db import db
from db.map_area import MapArea

# A block entity spawned in the world
class Block(Model):
    #BLOCKTYPE_MULTI = 0
    #BLOCKTYPE_SUPER = 1

    area_id = IntegerField()
    map_id = IntegerField()
    index = IntegerField()

    key_name = CharField()

    vanilla_type = IntegerField()

    def get_key(self):
        return (Block._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index

    class Meta:
        database = db
        key_type = 0xA1


# Run this to create all randomizable blocks in the Block table
def create_blocks():
    db.drop_tables([Block])
    db.create_tables([Block])

    with open("./debug/keys.json", "r") as file:
        keys_dict = json.load(file)
        block_keys = keys_dict["blocks"]

    with open("./debug/values.json", "r") as file:
        values_dict = json.load(file)
        block_values = values_dict["blocks"]
    
    # Create block info
    for data in block_keys.values():
        map_area, created = MapArea.get_or_create(
            area_id = data["area_id"],
            map_id = data["map_id"],
            name = data["map_name"],
            verbose_name = MapArea.get_verbose_name(data["map_name"])
        )
        
        block, created = Block.get_or_create(
            area_id=data["area_id"],
            map_id=data["map_id"],
            index=data["value_id"],
            key_name = data["name"],
            vanilla_type = block_values[data["map_name"]][data["name"]]
        )
        print(block, created)
