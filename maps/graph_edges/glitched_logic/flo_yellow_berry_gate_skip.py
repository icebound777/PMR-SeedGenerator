"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Yellow Berry Gate Skip.
"""
edges_flo_add_yellow_berry_gate_skip_lzs = [
    #? (SE) Briar Platforming Exit Left -> (SE) Briar Platforming Exit Right
    {"from": {"map": "FLO_08", "id": 0}, "to": {"map": "FLO_08", "id": 1}, "reqs": [["Boots"]], "mapchange": False},
    #? (SE) Briar Platforming Exit Right -> (SE) Briar Platforming Exit Left
    {"from": {"map": "FLO_08", "id": 1}, "to": {"map": "FLO_08", "id": 0}, "reqs": [], "mapchange": False},
]

edges_flo_add_yellow_berry_gate_skip_laki = [
    #? (SE) Briar Platforming Exit Left -> (SE) Briar Platforming Exit Right
    {"from": {"map": "FLO_08", "id": 0}, "to": {"map": "FLO_08", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},
    #? (SE) Briar Platforming Exit Right -> (SE) Briar Platforming Exit Left
    {"from": {"map": "FLO_08", "id": 1}, "to": {"map": "FLO_08", "id": 0}, "reqs": [], "mapchange": False},
]

edges_flo_add_yellow_berry_gate_skip_bombette_push = [
    #? (SE) Briar Platforming Exit Left -> (SE) Briar Platforming Exit Right
    {"from": {"map": "FLO_08", "id": 0}, "to": {"map": "FLO_08", "id": 1}, "reqs": [["Bombette"]], "mapchange": False},
    #? (SE) Briar Platforming Exit Right -> (SE) Briar Platforming Exit Left
    {"from": {"map": "FLO_08", "id": 1}, "to": {"map": "FLO_08", "id": 0}, "reqs": [], "mapchange": False},
]
