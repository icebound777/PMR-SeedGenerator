"""
This file represents edges of the world graph that have to be added
in the OMO region (Shy Guy's Toybox) for Shuffle Partner Upgrades.
"""
edges_omo_add_partnerupgrades = [
    #* GRN Treadmills/Slot Machine -> RandomBlockItemA (MultiCoinBlock)
    (0xA1100840, {"from": {"map": "OMO_09", "id": "ItemH"}, "to": {"map": "OMO_09", "id": "RandomBlockItemA"}, "reqs": [["Parakarry"]], "mapchange": False}), #+ CHAINED REQUIREMENTS
    #* RED Moving Platforms -> RandomBlockItemA (SuperBlock)
    (0xA1100A40, {"from": {"map": "OMO_11", "id": "YBlockA"}, "to": {"map": "OMO_11", "id": "RandomBlockItemA"}, "reqs": [], "mapchange": False}), #+ CHAINED REQUIREMENTS
    #* RED Moving Platforms -> RandomBlockItemB (MultiCoinBlock)
    (0xA1100A41, {"from": {"map": "OMO_11", "id": "YBlockA"}, "to": {"map": "OMO_11", "id": "RandomBlockItemB"}, "reqs": [], "mapchange": False}), #+ CHAINED REQUIREMENTS
    #* PNK Tracks Hallway -> RandomBlockItemB (MultiCoinBlock)
    (0xA1101040, {"from": {"map": "OMO_17", "id": 1}, "to": {"map": "OMO_17", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False}),
]
