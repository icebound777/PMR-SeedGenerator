"""
This file represents edges of the world graph that have to be added
in the ARN region (Gusty Gulch) for Shuffle Partner Upgrades.
"""
edges_arn_add_partnerupgrades = [
    #* Wasteland Ascent 2 Exit East -> RandomBlockItemA (MultiCoinBlock)
    (0xA10E0240, {"from": {"map": "ARN_04", "id": 1}, "to": {"map": "ARN_04", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False})
]
