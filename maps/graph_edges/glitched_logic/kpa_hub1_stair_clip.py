"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Hub 1 Stair Clip
By precisely walking into the left corner of the lower stair, 
Mario can clip out of bounds and fall to the upper level.
"""
edges_kpa_add_hub1_stair_clip = [
    #? Lower Grand Hall Door Bottom Left -> Lower Grand Hall Door Top Right
    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_32",  "id": 2}, "reqs": [], "mapchange": False}, 
    #? Lower Grand Hall Door Bottom Left -> Lower Grand Hall Door Top Left 
    # (no existing connection from 2->3 so connect to both upper doors)
    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_32",  "id": 3}, "reqs": [], "mapchange": False}, 
]
