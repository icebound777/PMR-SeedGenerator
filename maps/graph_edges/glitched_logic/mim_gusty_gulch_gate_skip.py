"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Gusty Gulch Gate Skip.
"""
edges_mim_add_gusty_gulch_gate_skip_lzs = [
    #? Exit to Gusty Gulch Exit West -> Exit to Gusty Gulch Exit East
    {"from": {"map": "MIM_12", "id": 0}, "to": {"map": "MIM_12", "id": 1}, "reqs": [], "mapchange": False},
    #? Exit to Gusty Gulch Exit East -> Exit to Gusty Gulch Exit West
    {"from": {"map": "MIM_12", "id": 1}, "to": {"map": "MIM_12", "id": 0}, "reqs": [], "mapchange": False},
]

edges_mim_add_gusty_gulch_gate_skip_laki = [
    #? Exit to Gusty Gulch Exit West -> Exit to Gusty Gulch Exit East
    {"from": {"map": "MIM_12", "id": 0}, "to": {"map": "MIM_12", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Exit to Gusty Gulch Exit East -> Exit to Gusty Gulch Exit West
    {"from": {"map": "MIM_12", "id": 1}, "to": {"map": "MIM_12", "id": 0}, "reqs": [["Lakilester"]], "mapchange": False},
]