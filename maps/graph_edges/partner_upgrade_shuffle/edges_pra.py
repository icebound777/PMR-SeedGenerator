"""
This file represents edges of the world graph that have to be added
in the PRA region (Crystal Palace) for Shuffle Partner Upgrades.
"""
edges_pra_add_partnerupgrades = [
    #* Blue Mirror Hall 2 -> RandomBlockItem[AB] (MultiCoinBlocks)
    (0xA1150B40, {"from": {"map": "PRA_14", "id": 0}, "to": {"map": "PRA_14", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    (0xA1150B40, {"from": {"map": "PRA_14", "id": 1}, "to": {"map": "PRA_14", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    (0xA1150B41, {"from": {"map": "PRA_14", "id": 0}, "to": {"map": "PRA_14", "id": "RandomBlockItemB"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    (0xA1150B41, {"from": {"map": "PRA_14", "id": 1}, "to": {"map": "PRA_14", "id": "RandomBlockItemB"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
]
