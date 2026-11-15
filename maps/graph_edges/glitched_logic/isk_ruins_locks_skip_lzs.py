"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Ruins Locks Skip (LZS).
"""
edges_isk_add_ruins_locks_skip_lzs = [
    # Sarcophagus Hall 1 Exit Top Right -> Sand Drainage Room 1 Exit Upper Room Left
    {"from": {"map": "ISK_02", "id": 1}, "to": {"map": "ISK_03", "id": 0}, "reqs": [["Boots"]], "mapchange": False},

    # Descending Stairs 1 Exit Bottom Left -> Sarcophagus Hall 2 Exit Right
    {"from": {"map": "ISK_04", "id": 1}, "to": {"map": "ISK_07", "id": 1}, "reqs": [["Boots"]], "mapchange": False},

    # Stone Puzzle Room Exit Top Right -> Sand Drainage Room 3 Exit Upper Room Left
    {"from": {"map": "ISK_11", "id": 1}, "to": {"map": "ISK_12", "id": 0}, "reqs": [["Boots"]], "mapchange": False},
]
