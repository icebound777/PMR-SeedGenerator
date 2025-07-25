"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Hammer Clip Item Grab.

By facing away from a wall, spinning, and hammering towards the wall, Mario is able to grab
specific items: Odd Key, KBF Key 2 and Smash Charge.
"""
edges_global_hammer_clip_item_grab = [
    #* Southern District Exit Top -> ItemA (OddKey)
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": "ItemA"}, "reqs": [["Hammer"]], "mapchange": False},

    #* Dungeon Fire Room Exit Right -> ItemA (KoopaFortressKey)
    {"from": {"map": "TRD_08", "id": 0}, "to": {"map": "TRD_08", "id": "ItemA"}, "reqs": [["Hammer"]], "mapchange": False},

    #* Left Tower Exit Top Right -> ItemA (SmashCharge)
    {"from": {"map": "TRD_01", "id": 3}, "to": {"map": "TRD_01", "id": "ItemA"}, "reqs": [["Hammer"]], "mapchange": False},
]
