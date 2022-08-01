"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Break Yellow Blocks With Bombette.
"""
edges_kmr_tik_add_break_yellow_blocks_bombette = [
    #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": 0}, "reqs": [["Bombette"]], "mapchange": False},
    #? Goomba Village Exit Right -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 0}, "to": {"map": "KMR_02", "id": 1}, "reqs": [["Bombette"]], "mapchange": False},

    #? Bottom of the Cliff Exit Left -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 0}, "to": {"map": "KMR_03", "id": 1}, "reqs": [["Bombette"]], "mapchange": False},
    #? Bottom of the Cliff Exit Right -> Bottom of the Cliff Exit Left
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_03", "id": 0}, "reqs": [["Bombette"]], "mapchange": False},

    #? Sewer Entrance (B1) Green Pipe Up -> Sewer Entrance (B1) Exit Right
    {"from": {"map": "TIK_06", "id": 3}, "to": {"map": "TIK_06", "id": 1}, "reqs": [["Bombette"]], "mapchange": False},
]
