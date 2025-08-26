"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Jumpless Deep Jungle Ledge

Using Clippy, you can access the ledge in the first deep jungle room jumpless. 
From Mr.Zebra: https://www.youtube.com/watch?v=PJwnU0aqQU4
"""
edges_jan_add_jumpless_deep_jungle_ledge = [
    #* Deep Jungle 1 Exit Bottom Left -> Tree1_Drop2 (Coin)
    {"from": {"map": "JAN_12", "id": 0}, "to": {"map": "JAN_12", "id": "Tree1_Drop2"}, "reqs": [["can_shake_trees"],["Lakilester"]], "mapchange": False}, 
    #* Deep Jungle 1 Exit Bottom Left -> HiddenYBlockA (StoneCap)
    {"from": {"map": "JAN_12", "id": 0}, "to": {"map": "JAN_12", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"],["Lakilester"]], "mapchange": False}, 
]
