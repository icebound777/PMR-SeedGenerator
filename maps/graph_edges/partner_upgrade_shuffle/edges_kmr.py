"""
This file represents edges of the world graph that have to be added
in the KMR region (Goomba Region) for Shuffle Partner Upgrades.
"""
edges_kmr_add_partnerupgrades = [
    #* Jr. Troopa's Playground -> RandomBlockItemA (MultiCoinBlock)
    (0xA1000340, {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "RandomBlockItemA"}, "reqs": [["can_hit_grounded_blocks"]], "mapchange": False})
]
