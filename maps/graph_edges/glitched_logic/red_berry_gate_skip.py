"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Red Berry Gate Skip.
"""

edges_flo_add_red_berry_gate_skip_laki = [
    {"from": {"map": "FLO_25", "id": 0}, "to": {"map": "FLO_25", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False}, #? (SW) Path to Crystal Tree Exit Right -> (SW) Path to Crystal Tree Exit Left
    {"from": {"map": "FLO_25", "id": 1}, "to": {"map": "FLO_25", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False}, #? (SW) Path to Crystal Tree Exit Left -> (SW) Path to Crystal Tree Exit Right
]

edges_flo_add_red_berry_gate_skip_bombette_push = [
    {"from": {"map": "FLO_25", "id": 0}, "to": {"map": "FLO_25", "id": 1}, "reqs": [["Bombette"]], "mapchange": False}, #? (SW) Path to Crystal Tree Exit Right -> (SW) Path to Crystal Tree Exit Left
    {"from": {"map": "FLO_25", "id": 1}, "to": {"map": "FLO_25", "id": 0}, "reqs": [], "mapchange": False}, #? (SW) Path to Crystal Tree Exit Left -> (SW) Path to Crystal Tree Exit Right
]
