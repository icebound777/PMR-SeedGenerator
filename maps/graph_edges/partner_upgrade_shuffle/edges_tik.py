"""
This file represents edges of the world graph that have to be added
in the TIK region (Toad Town Tunnels) for Shuffle Partner Upgrades.
"""
edges_tik_add_partnerupgrades = [
    #* Elevator Attic Room (B2) -> RandomBlockItemA (SuperBlock)
    (0xA1020640, {"from": {"map": "TIK_07", "id": 0}, "to": {"map": "TIK_07", "id": "RandomBlockItemA"}, "reqs": [["can_climb_steps"],["can_hit_floating_blocks"]], "mapchange": False}),
    #* Block Puzzle Room (B2) -> RandomBlockItemA (SuperBlock)
    (0xA1020940, {"from": {"map": "TIK_10", "id": "HiddenYBlockA"}, "to": {"map": "TIK_10", "id": "RandomBlockItemA"}, "reqs": [["can_climb_steps"],["can_hit_floating_blocks"]], "mapchange": False}), #+ SHARED REQUIREMENTS
    #* Metal Block Room (B3) -> RandomBlockItemA (SuperBlock)
    (0xA1020A40, {"from": {"map": "TIK_12", "id": 0}, "to": {"map": "TIK_12", "id": "RandomBlockItemA"}, "reqs": [["UltraHammer"],["can_climb_steps"],["can_hit_floating_blocks"]], "mapchange": False}),
    #* Frozen Room (B3) -> RandomBlockItemA (SuperBlock)
    (0xA1020D40, {"from": {"map": "TIK_17", "id": 0}, "to": {"map": "TIK_17", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* Hall to Blooper 1 (B1) -> RandomBlockItemA (MultiCoinBlock)
    (0xA1020E40, {"from": {"map": "TIK_18", "id": 0}, "to": {"map": "TIK_18", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* Under the Toad Town Pond -> RandomBlockItemA (SuperBlock)
    (0xA1020F40, {"from": {"map": "TIK_19", "id": 0}, "to": {"map": "TIK_19", "id": "RandomBlockItemA"}, "reqs": [["can_climb_steps"],["can_hit_floating_blocks"]], "mapchange": False}),
]
