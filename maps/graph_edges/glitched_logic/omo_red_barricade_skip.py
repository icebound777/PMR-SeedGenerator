"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Red Barricade Skip
"""
edges_omo_add_red_barricade_skip = [
    #? RED Boss Barricade Exit West -> RED Boss Barricade Exit East
    {"from": {"map": "OMO_02", "id": 0}, "to": {"map": "OMO_02", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},
    #? RED Boss Barricade Exit East -> RED Boss Barricade Exit West
    {"from": {"map": "OMO_02", "id": 1}, "to": {"map": "OMO_02", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False},
]
