"""
This file represents edges of the world graph that have to be added
in the FLO region (Flower Fields) for Shuffle Partner Upgrades.
"""
edges_flo_add_partnerupgrades = [
    #* (SE) Briar Platforming Exit Right -> RandomBlockItemA (SuperBlock)
    (0xA1130340, {"from": {"map": "FLO_08", "id": 1}, "to": {"map": "FLO_08", "id": "RandomBlockItemA"}, "reqs": [["can_climb_steps"],["can_hit_floating_blocks"]], "mapchange": False}),
    #* (West) Maze Exit Left -> RandomBlockItemA (MultiCoinBlock)
    (0xA1130640, {"from": {"map": "FLO_11", "id": 1}, "to": {"map": "FLO_11", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* (NE) Elevators Exit Right -> RandomBlockItemA (SuperBlock)
    (0xA1130B40, {"from": {"map": "FLO_16", "id": 1}, "to": {"map": "FLO_16", "id": "RandomBlockItemA"}, "reqs": [["can_climb_steps"],["can_hit_floating_blocks"]], "mapchange": False}),
]
