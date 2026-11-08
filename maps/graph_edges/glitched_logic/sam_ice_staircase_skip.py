"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Ice Staircase Skip
"""
edges_sam_add_ice_staircase_skip = [
    #* Shiver Mountain Peaks Exit West -> ItemA (StarPiece)
    {"from": {"map": "SAM_10", "id": 0}, "to": {"map": "SAM_10", "id": "ItemA"}, "reqs": [["Lakilester"],["Boots"]]},
    #? Shiver Mountain Peaks Exit West -> Shiver Mountain Peaks Exit East
    {"from": {"map": "SAM_10", "id": 0}, "to": {"map": "SAM_10", "id": 1}, "reqs": [["Lakilester"],["Boots"]]},
]
