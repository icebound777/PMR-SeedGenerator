"""
This file represents edges of the world graph that have to be added
in the DGB region (Tubba Blubba's Castle) for Shuffle Partner Upgrades.
"""
edges_dgb_add_partnerupgrades = [
    #* Stairs to Basement -> RandomBlockItemA (SuperBlock)
    (0xA10F0440, {"from": {"map": "DGB_04", "id": 0}, "to": {"map": "DGB_04", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False})
]
