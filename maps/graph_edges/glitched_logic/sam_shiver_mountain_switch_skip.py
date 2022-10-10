"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Shiver Mountain Switch Skip
"""
edges_sam_add_shiver_mountain_switch_skip = [
    #? Shiver Mountain Passage Mountain Entrance -> Shiver Mountain Passage Exit East
    {"from": {"map": "SAM_07", "id": 0}, "to": {"map": "SAM_07", "id": 1}, "reqs": [["Lakilester"], ["Boots"]], "mapchange": False},

    #? Shiver Mountain Passage Exit East -> Shiver Mountain Passage Mountain Entrance
    {"from": {"map": "SAM_07", "id": 1}, "to": {"map": "SAM_07", "id": 0}, "reqs": [["Lakilester"], ["Boots"]], "mapchange": False},
]
