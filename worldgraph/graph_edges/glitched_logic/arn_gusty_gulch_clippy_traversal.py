"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Gusty Gulch Clippy Traversal.
Gusty Gulch can be traversed from left to right using clippy instead of needing to jump / climb ledges.
Video by mrzebra: https://youtu.be/pn54TLKKoaI
"""
edges_arn_add_gusty_gulch_clippy_traversal = [
    #? Wasteland Ascent 1 Exit West -> Wasteland Ascent 1 Exit East
    {"from": {"map": "ARN_02", "id": 0}, "to": {"map": "ARN_02", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Wasteland Ascent 2 Exit West -> Wasteland Ascent 2 Exit East
    {"from": {"map": "ARN_04", "id": 0}, "to": {"map": "ARN_04", "id": 1}, "reqs": [["Lakilester"]], "mapchange": False},
]
