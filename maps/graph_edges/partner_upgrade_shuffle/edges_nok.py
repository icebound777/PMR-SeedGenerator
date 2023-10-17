"""
This file represents edges of the world graph that have to be added
in the NOK region (Koopa Region) for Shuffle Partner Upgrades.
"""
edges_nok_add_partnerupgrades = [
    #* Pleasant Path Bridge Exit Right -> RandomBlockItemA (MultiCoinBlock)
    (0xA1060540, {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False})
]
