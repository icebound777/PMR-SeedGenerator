"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Hidden Blocks with Bombette
Video: https://www.youtube.com/watch?v=fIq6-r3ylks
"""
edges_global_hidden_blocks_with_bombette = [
    #* RED Moving Platforms Exit East -> HiddenYBlockA (VoltShroom)
    {"from": {"map": "OMO_11", "id": 1}, "to": {"map": "OMO_11", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["Bombette"],["RF_MovingPlatformsLaki"]]},
    #* RED Moving Platforms Exit West -> HiddenYBlockB (SnowmanDoll)
    {"from": {"map": "OMO_11", "id": 0}, "to": {"map": "OMO_11", "id": "HiddenYBlockB"}, "reqs": [["can_see_hidden_blocks"],["Bombette"],["RF_MovingPlatformsLaki"]]},

    #* Beach Exit Left -> HiddenYBlockA (RepelGel)
    {"from": {"map": "JAN_01", "id": 0}, "to": {"map": "JAN_01", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["Bombette"]]},
]
