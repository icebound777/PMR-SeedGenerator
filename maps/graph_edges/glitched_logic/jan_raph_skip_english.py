"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Raph Skip (English)
"""
edges_jan_add_raph_skip_english = [
    #? Base of Great Tree Exit Right -> Base of Great Tree Exit Left
    {"from": {"map": "JAN_16", "id": 1}, "to": {"map": "JAN_16", "id": 0}, "reqs": [], "mapchange": False},

    #? Path to the Volcano Exit Left -> Path to the Volcano Exit Right
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 2}, "reqs": [["Boots"]], "mapchange": False},

    #? Path to the Volcano Exit Left -> Path to the Volcano Exit Top
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 1}, "reqs": [["Boots"]], "mapchange": False},

    #? Path to the Volcano Exit Right -> Path to the Volcano Exit Left
    {"from": {"map": "JAN_22", "id": 2}, "to": {"map": "JAN_22", "id": 0}, "reqs": [], "mapchange": False},
]
