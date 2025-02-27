"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Mt. Rugged Quake Hammer Room Jumpless Clippy.
From the lower left loading zone, the upper right loading zone can be reached
with a laki teleport followed by using Clippy and falling out of bounds.
The clippy portion can be found in this video from mrzebra: https://youtu.be/yLdXnkNiXPs
"""
edges_iwa_add_quake_hammer_room_jumpless_clippy = [
    #? Mt Rugged 2 Exit Bottom Left -> Mt Rugged 2 Exit Top Right
    {"from": {"map": "IWA_01", "id": 0}, "to": {"map": "IWA_01", "id": 3}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Mt Rugged 2 Exit Top Left -> Mt Rugged 2 Exit Top Right
    {"from": {"map": "IWA_01", "id": 1}, "to": {"map": "IWA_01", "id": 3}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Mt Rugged 2 Exit Bottom Right -> Mt Rugged 2 Exit Top Right
    {"from": {"map": "IWA_01", "id": 2}, "to": {"map": "IWA_01", "id": 3}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Mt Rugged 2 Exit Bottom Left -> Mt Rugged 2 Exit Bottom Right
    {"from": {"map": "IWA_01", "id": 0}, "to": {"map": "IWA_01", "id": 2}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Mt Rugged 2 Exit Top Left -> Mt Rugged 2 Exit Bottom Right
    {"from": {"map": "IWA_01", "id": 1}, "to": {"map": "IWA_01", "id": 2}, "reqs": [["Lakilester"]], "mapchange": False},
    #? Mt Rugged 2 Exit Top Right -> Mt Rugged 2 Exit Bottom Right
    {"from": {"map": "IWA_01", "id": 3}, "to": {"map": "IWA_01", "id": 2}, "reqs": [["Lakilester"]], "mapchange": False},
]
