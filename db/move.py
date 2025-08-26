import json

from peewee import *

from db.db import db

class Move(Model):
    # name
    move_name = CharField()
    # partner move, badge move, starpower move
    move_type = CharField(null=True)
    # cost type (FP/BP) and cost value
    cost_type = CharField()
    cost_value = IntegerField()

    area_id = IntegerField()
    map_id = IntegerField()
    index = IntegerField()

    def get_key(self):
        return (Move._meta.key_type << 24) | (self.area_id << 16) | (self.map_id << 8) | self.index

    class Meta:
        database = db
        key_type = 0xA6

def create_moves():
    db.drop_tables([Move])
    db.create_tables([Move])

    with open("./debug/keys.json", "r") as file:
        move_keys = json.load(file)["move_costs"]

    with open("./debug/values.json", "r") as file:
        move_values = json.load(file)["move_costs"]

    for data in move_keys.values():
        fp = None
        bp = None
        if data["cost_type"] == "MoveFP":
            fp = move_values[data["name"]]["FP"]
        elif data["cost_type"] == "MoveBP":
            bp = move_values[data["name"]]["BP"]

        if data["name"] in ["Refresh", "Lullaby", "StarStorm", "ChillOutMove",
                            "Smooch", "TimeOut", "UpAndAway"]:
            move_type = "STARPOWER"
        elif data["name"] in ["Charge", "Multibonk",
                              "PowerShell", "DizzyShell","FireShell",
                              "Bomb", "PowerBomb", "MegaBomb",
                              "ShellShot", "AirLift", "AirRaid",
                              "PowerShock", "TurboCharge", "MegaShock",
                              "Squirt", "WaterBlock", "TidalWave",
                              "SpinySurge", "CloudNine", "Hurricane",
                              "OuttaSight", "Spook", "FanSmack"]:
            move_type = "PARTNER"
        else:
            move_type = "BADGE"

        if fp:
            move,created = Move.get_or_create(
                move_name=data["name"],
                move_type=move_type,
                cost_type="FP",
                cost_value=fp,
                area_id=data["area_id"],
                map_id=data["map_id"],
                index=data["value_id"],
            )
        elif bp:
            move,created = Move.get_or_create(
                move_name=data["name"],
                move_type=move_type,
                cost_type="BP",
                cost_value=bp,
                area_id=data["area_id"],
                map_id=data["map_id"],
                index=data["value_id"],
            )
        print (move,created)
