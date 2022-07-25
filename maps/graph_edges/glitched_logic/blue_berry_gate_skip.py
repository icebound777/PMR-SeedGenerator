"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Blue Berry Gate Skip.
"""
edges_flo_add_blue_berry_gate_skip_laki = [
    #? (West) Path to Maze Exit Right -> (West) Path to Maze Exit Left
    {"from": {"map": "FLO_23", "id": 0}, "to": {"map": "FLO_23", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},
    #? (West) Path to Maze Exit Left -> (West) Path to Maze Exit Right
    {"from": {"map": "FLO_23", "id": 1}, "to": {"map": "FLO_23", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False},
]

edges_flo_add_blue_berry_gate_skip_bombette_push = [
    #? (West) Path to Maze Exit Right -> (West) Path to Maze Exit Left
    {"from": {"map": "FLO_23", "id": 0}, "to": {"map": "FLO_23", "id": 1}, "reqs": [["Bombette"]], "mapchange": False},
    #? (West) Path to Maze Exit Left -> (West) Path to Maze Exit Right
    {"from": {"map": "FLO_23", "id": 1}, "to": {"map": "FLO_23", "id": 0}, "reqs": [], "mapchange": False},
]
