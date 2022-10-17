"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Early Lakilester.
"""
edges_flo_add_early_lakilester_without_bombette = [
    #? (NW) Bubble Flower Exit Right -> (NW) Bubble Flower Exit Left
    {"from": {"map": "FLO_14", "id": 0}, "to": {"map": "FLO_14", "id": 1}, "reqs": [["Boots"]], "mapchange": False},
]

edges_flo_add_early_lakilester_bombette_push = [
    #? (NW) Bubble Flower Exit Right -> (NW) Bubble Flower Exit Left
    {"from": {"map": "FLO_14", "id": 0}, "to": {"map": "FLO_14", "id": 1}, "reqs": [["Bombette"],["Boots"]], "mapchange": False},
]
