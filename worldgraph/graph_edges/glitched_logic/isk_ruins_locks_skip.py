"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Ruins Locks Skip.
"""
edges_isk_add_ruins_locks_skip_clippy = [
    # Sarcophagus Hall 1 Exit Top Right -> Sand Drainage Room 1 Exit Upper Room Left
    {"from": {"map": "ISK_02", "id": 1}, "to": {"map": "ISK_03", "id": 0}, "reqs": [["Lakilester"],["Boots"]], "mapchange": False},

    #? Descending Stairs 1 Exit Middle Left -> Descending Stairs 1 Exit Bottom Left
    {"from": {"map": "ISK_04", "id": 0}, "to": {"map": "ISK_04", "id": 1}, "reqs": [], "pseudoitems": ["RF_ISK04_CanReachBeetle"], "mapchange": False},
    #? Descending Stairs 1 Exit Bottom Right -> Descending Stairs 1 Exit Bottom Left
    {"from": {"map": "ISK_04", "id": 4}, "to": {"map": "ISK_04", "id": 1}, "reqs": [], "pseudoitems": ["RF_ISK04_CanReachBeetle"], "mapchange": False},
    # Descending Stairs 1 Exit Bottom Left -> Sarcophagus Hall 2 Exit Right
    {"from": {"map": "ISK_04", "id": 1}, "to": {"map": "ISK_07", "id": 1}, "reqs": [["Lakilester"],["RF_ISK04_CanReachBeetle"]], "mapchange": False},
]
