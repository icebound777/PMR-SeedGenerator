"""
This file represents edges of the world graph that have to be added
in the SAM region (Shiver Region) for Shuffle Partner Upgrades.
"""
edges_sam_add_partnerupgrades = [
    #* Shiver Mountain Hills Exit East -> RandomBlockItemA (SuperBlock)
    (0xA1140740, {"from": {"map": "SAM_08", "id": 1}, "to": {"map": "SAM_08", "id": "RandomBlockItemA"}, "reqs": [["can_climb_steps"],["can_hit_floating_blocks"]], "mapchange": False})
]
