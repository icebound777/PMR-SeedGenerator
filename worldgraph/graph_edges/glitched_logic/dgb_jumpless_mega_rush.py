"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Jumpless Mega Rush
Can climb the bookshelf by partially clipping into each shelf and using Parakarry.
"""
edges_dgb_add_jumpless_mega_rush = [
    #* Hidden Bedroom (2F) Door Bottom -> ItemB (Coin)
    {"from": {"map": "DGB_13", "id": 0}, "to": {"map": "DGB_13", "id": "ItemB"}, "reqs": [["Parakarry"]], "mapchange": False},
]
