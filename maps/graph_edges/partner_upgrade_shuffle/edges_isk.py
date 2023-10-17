"""
This file represents edges of the world graph that have to be added
in the ISK region (Dry Dry Ruins) for Shuffle Partner Upgrades.
"""
edges_isk_add_partnerupgrades = [
    #* Vertical Shaft Exit Bottom Right -> RandomBlockItemA (SuperBlock)
    (0xA10B0940, {"from": {"map": "ISK_10", "id": 2}, "to": {"map": "ISK_10", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False})
]
