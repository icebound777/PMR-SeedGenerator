"""
This file represents edges of the world graph that have to be added
in the SBK region (Dry Dry Desert) for Shuffle Partner Upgrades.
"""
edges_sbk_add_partnerupgrades = [
    #* N3E3 -> RandomBlockItemA (MultiCoinBlock)
    (0xA10A0640, {"from": {"map": "SBK_06", "id": 0}, "to": {"map": "SBK_06", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* N2E1 (Tweester A) -> RandomBlockItemA (MultiCoinBlock)
    (0xA10A0B40, {"from": {"map": "SBK_14", "id": 0}, "to": {"map": "SBK_14", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* N1E2 -> RandomBlockItem[AB] (MultiCoinBlock)
    (0xA10A1340, {"from": {"map": "SBK_25", "id": 0}, "to": {"map": "SBK_25", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    (0xA10A1341, {"from": {"map": "SBK_25", "id": 0}, "to": {"map": "SBK_25", "id": "RandomBlockItemB"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* S1W3 -> RandomBlockItemA (MultiCoinBlock)
    (0xA10A1C40, {"from": {"map": "SBK_40", "id": 1}, "to": {"map": "SBK_40", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* S2W1 -> RandomBlockItemA (MultiCoinBlock)
    (0xA10A2540, {"from": {"map": "SBK_52", "id": 0}, "to": {"map": "SBK_52", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* S2E2 West of Oasis -> RandomBlockItemA (MultiCoinBlock)
    (0xA10A2840, {"from": {"map": "SBK_55", "id": 0}, "to": {"map": "SBK_55", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* S2E3 Oasis -> RandomBlockItemA (SuperBlock)
    (0xA10A2940, {"from": {"map": "SBK_56", "id": 0}, "to": {"map": "SBK_56", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    #* S3E3 South of Oasis -> RandomBlockItem[ABCDEF] (MultiCoinBlock)
    (0xA10A3040, {"from": {"map": "SBK_66", "id": 0}, "to": {"map": "SBK_66", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    (0xA10A3041, {"from": {"map": "SBK_66", "id": 0}, "to": {"map": "SBK_66", "id": "RandomBlockItemB"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    (0xA10A3042, {"from": {"map": "SBK_66", "id": 0}, "to": {"map": "SBK_66", "id": "RandomBlockItemC"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    (0xA10A3043, {"from": {"map": "SBK_66", "id": 0}, "to": {"map": "SBK_66", "id": "RandomBlockItemD"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    (0xA10A3044, {"from": {"map": "SBK_66", "id": 0}, "to": {"map": "SBK_66", "id": "RandomBlockItemE"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
    (0xA10A3045, {"from": {"map": "SBK_66", "id": 0}, "to": {"map": "SBK_66", "id": "RandomBlockItemF"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
]
