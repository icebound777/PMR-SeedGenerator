"""
This file represents edges of the world graph that have to be added
for Glitched Logic: RED Moving Platforms Laki Jump
"""
edges_omo_add_moving_platforms_laki_jump = [
    #? RED Moving Platforms Exit West -> RED Moving Platforms Exit East
    {"from": {"map": "OMO_11", "id": 0}, "to": {"map": "OMO_11", "id": 1}, "reqs": [["Lakilester"]]},
    #? RED Moving Platforms Exit East -> RED Moving Platforms Exit West
    {"from": {"map": "OMO_11", "id": 1}, "to": {"map": "OMO_11", "id": 0}, "reqs": [["Lakilester"]]},
    #* RED Moving Platforms Exit West -> YBlockA (Coin)
    {"from": {"map": "OMO_11", "id": 0}, "to": {"map": "OMO_11", "id": "YBlockA"}, "reqs": [["Lakilester"],["can_hit_floating_blocks"]]},
    #* RED Moving Platforms Exit West -> RandomBlockItemB (CoinBag)
    {"from": {"map": "OMO_11", "id": 0}, "to": {"map": "OMO_11", "id": "RandomBlockItemB"}, "reqs": [["Lakilester"],["can_hit_floating_blocks"]]},
]
