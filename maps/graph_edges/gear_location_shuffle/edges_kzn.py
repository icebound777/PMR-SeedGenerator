"""
This file represents edges of the world graph that have origin-nodes in the KZN
(Mt. Lavalava) area, which have to be added / removed for the Big Chest Shuffle
setting.
"""
# Note: Instead of using custom RandomizerFlags to check for dynamic hammer
# blocks, we just check for the actual hammer upgrade, as dynamic hammer blocks
# is turned off for Big Chest Shuffle.
edges_kzn_add = [
    #? KZN_03 Central Cavern Exit East Lower 1 (Ultra Block) -> Zipline Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 2}, "to": {"map": "KZN_09", "id": 0}, "reqs": [["UltraHammer"]], "mapchange": False},
    # TODO: hmm, mapchange?

    # KZN_06 Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit East Lower
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 2}, "reqs": [["UltraHammer"]], "mapchange": False},

    # KZN_07 Ultra Hammer Room Exit East -> BigChest (UltraHammer)
    {"from": {"map": "KZN_07", "id": 0}, "to": {"map": "KZN_07", "id": "BigChest"}, "reqs": [["Parakarry","Lakilester","UltraHammer"],["can_climb_steps"]], "mapchange": False},

    # KZN_17 Spike Roller Trap Exit West -> Spike Roller Trap Exit East
    {"from": {"map": "KZN_17", "id": 1}, "to": {"map": "KZN_18", "id": 0}, "reqs": [["UltraHammer"],["can_climb_steps"]], "mapchange": False},
    # TODO: hmm, mapchange?
]

edges_kzn_remove = [
    #? KZN_03 Central Cavern Exit East Lower 1 (Ultra Block) -> Zipline Cavern Exit West Upper
    {"from": {"map": "KZN_03", "id": 2}, "to": {"map": "KZN_09", "id": 0}, "reqs": [["RF_KZN07_OpenedHammerChest"]]},

    # KZN_06 Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit East Lower
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 2}, "reqs": [["RF_KZN07_OpenedHammerChest"]]},

    # KZN_07 Ultra Hammer Room Exit East -> BigChest (UltraHammer)
    {"from": {"map": "KZN_07", "id": 0}, "to": {"map": "KZN_07", "id": "BigChest"}, "reqs": [["Parakarry","Lakilester"],["can_climb_steps"]], "pseudoitems": ["RF_KZN07_OpenedHammerChest"]},

    # KZN_17 Spike Roller Trap Exit East -> Boss Antechamber Exit West
    {"from": {"map": "KZN_17", "id": 1}, "to": {"map": "KZN_18", "id": 0}, "reqs": [["RF_KZN07_OpenedHammerChest"],["can_climb_steps"]]},
]
