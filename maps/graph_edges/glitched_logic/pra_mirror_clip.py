"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Mirror Clip
"""
edges_pra_add_mirror_clip_laki= [
    # Entry Hall Entrance Door -> Entry Hall Entrance Door (Mirror Side)
    {"from": {"map": "PRA_02", "id": 0}, "to": {"map": "PRA_02", "id": 5}, "reqs": [["Lakilester"]], "mapchange": False},
    # Entry Hall Entrance Door (Mirror Side) -> Entry Hall Entrance Door
    {"from": {"map": "PRA_02", "id": 0}, "to": {"map": "PRA_02", "id": 5}, "reqs": [], "mapchange": False},
]
