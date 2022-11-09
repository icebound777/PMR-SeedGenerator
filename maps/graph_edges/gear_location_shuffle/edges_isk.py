"""
This file represents edges of the world graph that have origin-nodes in the ISK
(Dry Dry Ruins) area, which have to be added / removed for the Big Chest Shuffle
setting.
"""
# Note: Instead of using custom RandomizerFlags to check for dynamic hammer
# blocks, we just check for the actual hammer upgrade, as dynamic hammer blocks
# is turned off for Big Chest Shuffle.
edges_isk_add = [
    # ISK_05 Pyramid Stone Room Exit Left -> ItemA (PyramidStone)
    {"from": {"map": "ISK_05", "id": 0}, "to": {"map": "ISK_05", "id": "ItemA"}, "reqs": [["SuperHammer"],["can_climb_steps"]], "mapchange": False},

    # ISK_07 Sarcophagus Hall 2 Exit Right -> ItemB (Artifact)
    {"from": {"map": "ISK_07", "id": 1}, "to": {"map": "ISK_07", "id": "ItemB"}, "reqs": [["SuperHammer"],["can_climb_steps"]], "mapchange": False},

    # ISK_09 Super Hammer Room Exit Right -> BigChest (SuperHammer)
    {"from": {"map": "ISK_09", "id": 0}, "to": {"map": "ISK_09", "id": "BigChest"}, "reqs": [["can_climb_steps"]], "mapchange": False},

    # ISK_12 Sand Drainage Room 3 Exit Bottom Left -> ItemA (RuinsKey)
    {"from": {"map": "ISK_12", "id": 1}, "to": {"map": "ISK_12", "id": "ItemA"}, "reqs": [["RF_DrainedThirdSandRoomAndCanSolvePuzzle","can_climb_steps"],["RF_DrainedThirdSandRoomAndCanSolvePuzzle","SuperHammer"]], "mapchange": False},
    # ISK_12 Sand Drainage Room 3 Exit Bottom Left -> ItemA (RuinsKey)
    {"from": {"map": "ISK_12", "id": 2}, "to": {"map": "ISK_12", "id": "ItemA"}, "reqs": [["SuperHammer"],["can_climb_steps"]], "mapchange": False},

    # ISK_13 Lunar Stone Room Exit Left -> ItemA (LunarStone)
    {"from": {"map": "ISK_13", "id": 0}, "to": {"map": "ISK_13", "id": "ItemA"}, "reqs": [["SuperHammer"],["can_climb_steps"]], "mapchange": False},

    # ISK_14 Diamond Stone Room Exit Right -> ItemA (DiamondStone)
    {"from": {"map": "ISK_14", "id": 0}, "to": {"map": "ISK_14", "id": "ItemA"}, "reqs": [["SuperHammer"],["can_climb_steps"]], "mapchange": False},
]

edges_isk_remove = [
    # ISK_05 Pyramid Stone Room Exit Left -> ItemA (PyramidStone)
    {"from": {"map": "ISK_05", "id": 0}, "to": {"map": "ISK_05", "id": "ItemA"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]},

    # ISK_07 Sarcophagus Hall 2 Exit Right -> ItemB (Artifact)
    {"from": {"map": "ISK_07", "id": 1}, "to": {"map": "ISK_07", "id": "ItemB"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]},

    # ISK_09 Super Hammer Room Exit Right -> BigChest (SuperHammer)
    {"from": {"map": "ISK_09", "id": 0}, "to": {"map": "ISK_09", "id": "BigChest"}, "reqs": [["can_climb_steps"]], "pseudoitems": ["RF_ISK09_OpenedHammerChest"]},

    # ISK_12 Sand Drainage Room 3 Exit Bottom Left -> ItemA (RuinsKey)
    {"from": {"map": "ISK_12", "id": 1}, "to": {"map": "ISK_12", "id": "ItemA"}, "reqs": [["RF_DrainedThirdSandRoomAndCanSolvePuzzle","can_climb_steps"],["RF_DrainedThirdSandRoomAndCanSolvePuzzle","RF_ISK09_OpenedHammerChest"]]},
    # ISK_12 Sand Drainage Room 3 Exit Bottom Left -> ItemA (RuinsKey)
    {"from": {"map": "ISK_12", "id": 2}, "to": {"map": "ISK_12", "id": "ItemA"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]},

    # ISK_13 Lunar Stone Room Exit Left -> ItemA (LunarStone)
    {"from": {"map": "ISK_13", "id": 0}, "to": {"map": "ISK_13", "id": "ItemA"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]},

    # ISK_14 Diamond Stone Room Exit Right -> ItemA (DiamondStone)
    {"from": {"map": "ISK_14", "id": 0}, "to": {"map": "ISK_14", "id": "ItemA"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]},
]
