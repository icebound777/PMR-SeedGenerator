"""
This file represents edges of the world graph that have to be added
in the IWA region (Mt. Rugged) for Shuffle Partner Upgrades.
"""
edges_iwa_add_partnerupgrades = [
    #* Train Station -> RandomBlockItemA (SuperBlock)
    (0xA1080540, {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": "RandomBlockItemA"}, "reqs": [["SuperHammer"],["can_hit_floating_blocks"]], "mapchange": False})
]
