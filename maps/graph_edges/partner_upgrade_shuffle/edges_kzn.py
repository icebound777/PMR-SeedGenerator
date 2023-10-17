"""
This file represents edges of the world graph that have to be added
in the KZN region (Mt. Lavalava) for Shuffle Partner Upgrades.
"""
edges_kzn_add_partnerupgrades = [
    #* Fire Bar Bridge -> RandomBlockItemA (SuperBlock)
    (0xA1120340, {"from": {"map": "KZN_04", "id": 0}, "to": {"map": "KZN_04", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* Zipline Cavern Exit West Upper -> RandomBlockItemA (SuperBlock)
    (0xA1120840, {"from": {"map": "KZN_09", "id": 0}, "to": {"map": "KZN_09", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
]
