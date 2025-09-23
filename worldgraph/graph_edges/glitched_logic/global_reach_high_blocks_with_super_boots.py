"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Reach High Blocks With Super Boots
"""
edges_global_reach_high_blocks_with_super_boots = [
    #* Path to Fortress 1 Exit Left -> ItemF (ThunderBolt)
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": "ItemF"}, "reqs": [["SuperBoots"]], "mapchange": False}, 

    #* S1E2 Small Bluffs Exit West -> ItemA (StopWatch)
    {"from": {"map": "SBK_45", "id": 0}, "to": {"map": "SBK_45", "id": "ItemA"}, "reqs": [["SuperBoots"]], "mapchange": False},

    #* Huge Statue Room Door West -> YBlockA (MapleSyrup)
    {"from": {"map": "PRA_21", "id": 0}, "to": {"map": "PRA_21", "id": "YBlockA"}, "reqs": [["SuperBoots"]], "mapchange": False},

    #* Small Statue Room Door West -> HiddenYBlockA (JamminJelly)
    {"from": {"map": "PRA_22", "id": 0}, "to": {"map": "PRA_22", "id": "HiddenYBlockA"}, "reqs": [["SuperBoots"],["can_see_hidden_blocks"]], "mapchange": False},
]
