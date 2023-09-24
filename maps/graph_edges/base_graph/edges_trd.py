"""This file represents all edges of the world graph that have origin-nodes in the TRD (Koopa Bros. Fortress) area."""
edges_trd = [
    # TRD_00 Fortress Exterior
    {"from": {"map": "TRD_00", "id": 0}, "to": {"map": "NOK_15", "id": 1}, "reqs": []}, # Fortress Exterior Exit Bottom Left -> Path to Fortress 2 Exit Bottom Right
    {"from": {"map": "TRD_00", "id": 1}, "to": {"map": "TRD_01", "id": 0}, "reqs": []}, # Fortress Exterior Main Entrance -> Left Tower Exit Bottom Left
    {"from": {"map": "TRD_00", "id": 2}, "to": {"map": "TRD_05", "id": 1}, "reqs": []}, # Fortress Exterior Save Block -> Right Tower Exit Bottom Down
    {"from": {"map": "TRD_00", "id": 3}, "to": {"map": "TRD_05", "id": 2}, "reqs": [["Bombette"]]}, # Fortress Exterior Refund Chest -> Right Tower Exit Bottom Right
    {"from": {"map": "TRD_00", "id": 4}, "to": {"map": "NOK_15", "id": 2}, "reqs": []}, # Fortress Exterior Exit Top Left -> Path to Fortress 2 Exit Top Right

    {"from": {"map": "TRD_00", "id": 0}, "to": {"map": "TRD_00", "id": 1}, "reqs": []}, #? Fortress Exterior Exit Bottom Left -> Fortress Exterior Main Entrance
    {"from": {"map": "TRD_00", "id": 1}, "to": {"map": "TRD_00", "id": 0}, "reqs": []}, #? Fortress Exterior Main Entrance -> Fortress Exterior Exit Bottom Left

    {"from": {"map": "TRD_00", "id": 3},        "to": {"map": "TRD_00", "id": "ChestA"}, "reqs": []}, #* Fortress Exterior Exit Bottom Left -> ChestA (Refund)
    {"from": {"map": "TRD_00", "id": "ChestA"}, "to": {"map": "TRD_00", "id": 3},        "reqs": [["Bombette"]]}, #* ChestA (Refund) -> Fortress Exterior Exit Bottom Left
    {"from": {"map": "TRD_00", "id": 4},        "to": {"map": "TRD_00", "id": "ChestB"}, "reqs": []}, #* Fortress Exterior Exit Top Left -> ChestB (FPPlusB)

    # TRD_01 Left Tower
    {"from": {"map": "TRD_01", "id": 0}, "to": {"map": "TRD_00", "id": 1}, "reqs": []}, # Left Tower Exit Bottom Left -> Fortress Exterior Main Entrance
    {"from": {"map": "TRD_01", "id": 1}, "to": {"map": "TRD_02", "id": 0}, "reqs": [[{"KoopaFortressKey": 1}]]}, # Left Tower Exit Bottom Right -> Left Stairway Exit Bottom Left
    {"from": {"map": "TRD_01", "id": 2}, "to": {"map": "TRD_02", "id": 2}, "reqs": []}, # Left Tower Exit Middle Right -> Left Stairway Exit Top Left
    {"from": {"map": "TRD_01", "id": 3}, "to": {"map": "TRD_09", "id": 0}, "reqs": []}, # Left Tower Exit Top Right -> Battlement Exit Left

    {"from": {"map": "TRD_01", "id": 0}, "to": {"map": "TRD_01", "id": 1}, "reqs": []}, #? Left Tower Exit Bottom Left -> Left Tower Exit Bottom Right
    {"from": {"map": "TRD_01", "id": 1}, "to": {"map": "TRD_01", "id": 0}, "reqs": []}, #? Left Tower Exit Bottom Right -> Left Tower Exit Bottom Left
    {"from": {"map": "TRD_01", "id": 2}, "to": {"map": "TRD_01", "id": 3}, "reqs": [["MF_TRD01_RaisedStairs"]]}, #? Left Tower Exit Middle Right -> Left Tower Exit Top Right
    {"from": {"map": "TRD_01", "id": 3}, "to": {"map": "TRD_01", "id": 2}, "reqs": [["MF_TRD01_RaisedStairs"]]}, #? Left Tower Exit Top Right -> Left Tower Exit Middle Right

    {"from": {"map": "TRD_01", "id": 2}, "to": {"map": "TRD_01", "id": 2}, "reqs": [["can_climb_steps","Hammer","Kooper","Bombette"]], "pseudoitems": ["MF_TRD01_RaisedStairs"]}, #+ Left Tower Exit Middle Right

    {"from": {"map": "TRD_01", "id": 0}, "to": {"map": "TRD_01", "id": "ItemB"}, "reqs": []}, #* Left Tower Exit Bottom Left -> ItemB (KoopaFortressKey)
    {"from": {"map": "TRD_01", "id": 3}, "to": {"map": "TRD_01", "id": "ItemA"}, "reqs": [["can_climb_steps"]]}, #* Left Tower Exit Top Right -> ItemA (SmashCharge)

    # TRD_02 Left Stairway
    {"from": {"map": "TRD_02", "id": 0}, "to": {"map": "TRD_01", "id": 1}, "reqs": []}, # Left Stairway Exit Bottom Left -> Left Tower Exit Bottom Right
    {"from": {"map": "TRD_02", "id": 1}, "to": {"map": "TRD_03", "id": 0}, "reqs": []}, # Left Stairway Exit Bottom Right -> Central Hall Exit Bottom Left
    {"from": {"map": "TRD_02", "id": 2}, "to": {"map": "TRD_01", "id": 2}, "reqs": [[{"KoopaFortressKey": 4}]]}, # Left Stairway Exit Top Left -> Left Tower Exit Middle Right
    {"from": {"map": "TRD_02", "id": 3}, "to": {"map": "TRD_03", "id": 2}, "reqs": []}, # Left Stairway Exit Top Right -> Central Hall Exit Top Left
    {"from": {"map": "TRD_02", "id": 4}, "to": {"map": "TRD_03", "id": 4}, "reqs": [["Bombette"]], "pseudoitems": ["RF_TRD_02_OpenedLeftJail"]}, # Left Stairway Exit Middle Right -> Central Hall Exit Left Cell

    {"from": {"map": "TRD_02", "id": 0}, "to": {"map": "TRD_02", "id": 1}, "reqs": []}, #? Left Stairway Exit Bottom Left -> Left Stairway Exit Bottom Right
    {"from": {"map": "TRD_02", "id": 1}, "to": {"map": "TRD_02", "id": 0}, "reqs": []}, #? Left Stairway Exit Bottom Right -> Left Stairway Exit Bottom Left
    {"from": {"map": "TRD_02", "id": 1}, "to": {"map": "TRD_02", "id": 4}, "reqs": [["MF_TRD02_LoweredStairs"],["Boots"]]}, #? Left Stairway Exit Bottom Right -> Left Stairway Exit Middle Right
    {"from": {"map": "TRD_02", "id": 4}, "to": {"map": "TRD_02", "id": 1}, "reqs": []}, #? Left Stairway Exit Middle Right -> Left Stairway Exit Bottom Right
    {"from": {"map": "TRD_02", "id": 2}, "to": {"map": "TRD_02", "id": 3}, "reqs": []}, #? Left Stairway Exit Top Left -> Left Stairway Exit Top Right
    {"from": {"map": "TRD_02", "id": 3}, "to": {"map": "TRD_02", "id": 2}, "reqs": []}, #? Left Stairway Exit Top Right -> Left Stairway Exit Top Left
    {"from": {"map": "TRD_02", "id": 3}, "to": {"map": "TRD_02", "id": 1}, "reqs": [["MF_TRD02_LoweredStairs"]]}, #? Left Stairway Exit Top Right -> Left Stairway Exit Bottom Right
    {"from": {"map": "TRD_02", "id": 1}, "to": {"map": "TRD_02", "id": 3}, "reqs": [["MF_TRD02_LoweredStairs"],["Boots"]]}, #? Left Stairway Exit Bottom Right -> Left Stairway Exit Top Right
    {"from": {"map": "TRD_02", "id": 3}, "to": {"map": "TRD_02", "id": 4}, "reqs": [["MF_TRD02_LoweredStairs"],["can_climb_steps"]]}, #? Left Stairway Exit Top Right -> Left Stairway Exit Middle Right
    {"from": {"map": "TRD_02", "id": 4}, "to": {"map": "TRD_02", "id": 3}, "reqs": [["MF_TRD02_LoweredStairs"],["can_climb_steps"]]}, #? Left Stairway Exit Middle Right -> Left Stairway Exit Top Right

    {"from": {"map": "TRD_02", "id": 3}, "to": {"map": "TRD_02", "id": 3}, "reqs": [["can_climb_steps","Hammer","Kooper","Bombette"]], "pseudoitems": ["MF_TRD02_LoweredStairs"]}, #+ Left Stairway Exit Top Right

    # TRD_03 Central Hall
    {"from": {"map": "TRD_03", "id": 0}, "to": {"map": "TRD_02", "id": 1}, "reqs": []}, # Central Hall Exit Bottom Left -> Left Stairway Exit Bottom Right
    {"from": {"map": "TRD_03", "id": 1}, "to": {"map": "TRD_04", "id": 0}, "reqs": []}, # Central Hall Exit Bottom Right -> Right Starway Exit Middle Left
    {"from": {"map": "TRD_03", "id": 2}, "to": {"map": "TRD_02", "id": 3}, "reqs": [["can_climb_steps"]]}, # Central Hall Exit Top Left -> Left Stairway Exit Top Right
    {"from": {"map": "TRD_03", "id": 3}, "to": {"map": "TRD_04", "id": 2}, "reqs": [["can_climb_steps"]]}, # Central Hall Exit Top Right -> Right Starway Exit Top Left
    {"from": {"map": "TRD_03", "id": 4}, "to": {"map": "TRD_02", "id": 4}, "reqs": [["RF_TRD_02_OpenedLeftJail"]]}, # Central Hall Exit Left Cell -> Left Stairway Exit Middle Right

    {"from": {"map": "TRD_03", "id": 0}, "to": {"map": "TRD_03", "id": 1}, "reqs": []}, #? Central Hall Exit Bottom Left -> Central Hall Exit Bottom Right
    {"from": {"map": "TRD_03", "id": 1}, "to": {"map": "TRD_03", "id": 0}, "reqs": []}, #? Central Hall Exit Bottom Right -> Central Hall Exit Bottom Left
    {"from": {"map": "TRD_03", "id": 2}, "to": {"map": "TRD_03", "id": 3}, "reqs": [["Kooper","Parakarry"]]}, #? Central Hall Exit Top Left -> Central Hall Exit Top Right
    {"from": {"map": "TRD_03", "id": 3}, "to": {"map": "TRD_03", "id": 2}, "reqs": [["Kooper","Parakarry"]]}, #? Central Hall Exit Top Right-> Central Hall Exit Top Left
    {"from": {"map": "TRD_03", "id": 2}, "to": {"map": "TRD_03", "id": 0}, "reqs": []}, #? Central Hall Exit Top Left -> Central Hall Exit Bottom Left
    {"from": {"map": "TRD_03", "id": 3}, "to": {"map": "TRD_03", "id": 1}, "reqs": []}, #? Central Hall Exit Top Right-> Central Hall Exit Bottom Right

    {"from": {"map": "TRD_03", "id": 4}, "to": {"map": "TRD_03", "id": "ItemA"}, "reqs": []}, #* Central Hall Exit Left Cell -> ItemA (KoopaFortressKey) (Left)
    {"from": {"map": "TRD_03", "id": 0}, "to": {"map": "TRD_03", "id": "ItemC"}, "reqs": []}, #* Central Hall Exit Bottom Left -> ItemC (PowerBounce)
    {"from": {"map": "TRD_03", "id": 1}, "to": {"map": "TRD_03", "id": "ItemB"}, "reqs": [["Bombette"]]}, #* Central Hall Exit Bottom Right -> ItemB (KoopaFortressKey) (Right)

    # TRD_04 Right Stairway
    {"from": {"map": "TRD_04", "id": 0}, "to": {"map": "TRD_03", "id": 1}, "reqs": []}, # Right Starway Exit Middle Left -> Central Hall Exit Bottom Right
    {"from": {"map": "TRD_04", "id": 1}, "to": {"map": "TRD_05", "id": 0}, "reqs": [[{"KoopaFortressKey": 2}]]}, # Right Starway Exit Middle Right -> Right Tower Exit Bottom Left
    {"from": {"map": "TRD_04", "id": 2}, "to": {"map": "TRD_03", "id": 3}, "reqs": [[{"KoopaFortressKey": 3}]]}, # Right Starway Exit Top Left -> Central Hall Exit Top Right
    {"from": {"map": "TRD_04", "id": 3}, "to": {"map": "TRD_05", "id": 3}, "reqs": []}, # Right Starway Exit Top Right -> Right Tower Exit Top Left
    {"from": {"map": "TRD_04", "id": 4}, "to": {"map": "TRD_07", "id": 0}, "reqs": []}, # Right Starway Exit Bottom Left -> Dungeon Trap Exit Right
    {"from": {"map": "TRD_04", "id": 5}, "to": {"map": "TRD_06", "id": 1}, "reqs": []}, # Right Starway Exit Bottom Right -> Jail Exit Left

    {"from": {"map": "TRD_04", "id": 0}, "to": {"map": "TRD_04", "id": 1}, "reqs": []}, #? Right Starway Exit Middle Left -> Right Starway Exit Middle Right
    {"from": {"map": "TRD_04", "id": 1}, "to": {"map": "TRD_04", "id": 0}, "reqs": []}, #? Right Starway Exit Middle Right -> Right Starway Exit Middle Left
    {"from": {"map": "TRD_04", "id": 0}, "to": {"map": "TRD_04", "id": 5}, "reqs": [["MF_TRD04_LoweredStairs"]]}, #? Right Starway Exit Middle Left -> Right Starway Exit Bottom Right
    {"from": {"map": "TRD_04", "id": 5}, "to": {"map": "TRD_04", "id": 0}, "reqs": [["MF_TRD04_LoweredStairs"],["can_climb_steps"]]}, #? Right Starway Exit Bottom Right -> Right Starway Exit Middle Left
    {"from": {"map": "TRD_04", "id": 4}, "to": {"map": "TRD_04", "id": 5}, "reqs": []}, #? Right Starway Exit Bottom Left -> Right Starway Exit Bottom Right
    {"from": {"map": "TRD_04", "id": 5}, "to": {"map": "TRD_04", "id": 4}, "reqs": []}, #? Right Starway Exit Bottom Right -> Right Starway Exit Bottom Left
    {"from": {"map": "TRD_04", "id": 2}, "to": {"map": "TRD_04", "id": 3}, "reqs": []}, #? Right Starway Exit Top Left -> Right Starway Exit Top Right
    {"from": {"map": "TRD_04", "id": 3}, "to": {"map": "TRD_04", "id": 2}, "reqs": []}, #? Right Starway Exit Top Right -> Right Starway Exit Top Left
    {"from": {"map": "TRD_04", "id": 3}, "to": {"map": "TRD_04", "id": 0}, "reqs": []}, #? Right Starway Exit Top Right -> Right Starway Exit Middle Left

    {"from": {"map": "TRD_04", "id": 0}, "to": {"map": "TRD_04", "id": 0}, "reqs": [["can_climb_steps","Hammer","Kooper","Bombette"]], "pseudoitems": ["MF_TRD04_LoweredStairs"]}, #+ Right Starway Exit Middle Left
    {"from": {"map": "TRD_04", "id": 4}, "to": {"map": "TRD_04", "id": 4}, "reqs": [], "pseudoitems": ["MF_TRD04_LoweredStairs"]}, #+ Right Starway Exit Bottom Left
    {"from": {"map": "TRD_04", "id": 5}, "to": {"map": "TRD_04", "id": 5}, "reqs": [], "pseudoitems": ["MF_TRD04_LoweredStairs"]}, #+ Right Starway Exit Bottom Right

    # TRD_05 Right Tower
    {"from": {"map": "TRD_05", "id": 0}, "to": {"map": "TRD_04", "id": 1}, "reqs": []}, # Right Tower Exit Bottom Left -> Right Starway Exit Middle Right
    {"from": {"map": "TRD_05", "id": 1}, "to": {"map": "TRD_00", "id": 2}, "reqs": []}, # Right Tower Exit Bottom Down-> Fortress Exterior Save Block
    {"from": {"map": "TRD_05", "id": 2}, "to": {"map": "TRD_00", "id": 3}, "reqs": [["Bombette"]]}, # Right Tower Exit Bottom Right -> Fortress Exterior Refund Chest
    {"from": {"map": "TRD_05", "id": 3}, "to": {"map": "TRD_04", "id": 3}, "reqs": []}, # Right Tower Exit Top Left -> Right Starway Exit Top Right
    {"from": {"map": "TRD_05", "id": 4}, "to": {"map": "TRD_06", "id": 0}, "reqs": []}, # Right Tower YBlock Trap -> Jail Fall From Ceiling

    {"from": {"map": "TRD_05", "id": 0}, "to": {"map": "TRD_05", "id": 1}, "reqs": []}, #? Right Tower Exit Bottom Left -> Right Tower Exit Bottom Down
    {"from": {"map": "TRD_05", "id": 1}, "to": {"map": "TRD_05", "id": 0}, "reqs": []}, #? Right Tower Exit Bottom Down -> Right Tower Exit Bottom Left
    {"from": {"map": "TRD_05", "id": 0}, "to": {"map": "TRD_05", "id": 2}, "reqs": []}, #? Right Tower Exit Bottom Left -> Right Tower Exit Bottom Right
    {"from": {"map": "TRD_05", "id": 2}, "to": {"map": "TRD_05", "id": 0}, "reqs": []}, #? Right Tower Exit Bottom Right -> Right Tower Exit Bottom Left
    {"from": {"map": "TRD_05", "id": 0}, "to": {"map": "TRD_05", "id": 3}, "reqs": []}, #? Right Tower Exit Bottom Left -> Right Tower Exit Top Left
    {"from": {"map": "TRD_05", "id": 3}, "to": {"map": "TRD_05", "id": 0}, "reqs": []}, #? Right Tower Exit Top Left -> Right Tower Exit Bottom Left
    {"from": {"map": "TRD_05", "id": 0}, "to": {"map": "TRD_05", "id": 4}, "reqs": [["can_hit_floating_blocks"]]}, #? Right Tower Exit Bottom Left -> Right Tower YBlock Trap
    {"from": {"map": "TRD_05", "id": 4}, "to": {"map": "TRD_05", "id": 0}, "reqs": []}, #? Right Tower YBlock Trap -> Right Tower Exit Bottom Left

    # TRD_06 Jail
    #{"from": {"map": "TRD_06", "id": 0}, "to": {"map": None, "id": None},  "reqs": []}, # Jail Fall From Ceiling
    {"from": {"map": "TRD_06", "id": 1}, "to": {"map": "TRD_04", "id": 5}, "reqs": []}, # Jail Exit Left -> Right Starway Exit Bottom Right

    {"from": {"map": "TRD_06", "id": 1}, "to": {"map": "TRD_06", "id": 0}, "reqs": [["Bombette"]]}, #? Jail Exit Left -> Jail Fall From Ceiling
    {"from": {"map": "TRD_06", "id": 0}, "to": {"map": "TRD_06", "id": 1}, "reqs": [["Bombette"]]}, #? Jail Fall From Ceiling -> Jail Exit Left

    {"from": {"map": "TRD_06", "id": 0}, "to": {"map": "TRD_06", "id": "Partner"}, "reqs": []}, #* Jail Fall From Ceiling -> Partner (Bombette)

    # TRD_07 Dungeon Trap
    {"from": {"map": "TRD_07", "id": 0}, "to": {"map": "TRD_04", "id": 4}, "reqs": []}, # Dungeon Trap Exit Right -> Right Starway Exit Bottom Left
    {"from": {"map": "TRD_07", "id": 1}, "to": {"map": "TRD_08", "id": 0}, "reqs": []}, # Dungeon Trap Exit Left -> Dungeon Fire Room Exit Right

    {"from": {"map": "TRD_07", "id": 0}, "to": {"map": "TRD_07", "id": 1}, "reqs": []}, #? Dungeon Trap Exit Right -> Dungeon Trap Exit Left
    {"from": {"map": "TRD_07", "id": 1}, "to": {"map": "TRD_07", "id": 0}, "reqs": []}, #? Dungeon Trap Exit Left -> Dungeon Trap Exit Right

    # TRD_08 Dungeon Fire Room
    {"from": {"map": "TRD_08", "id": 0}, "to": {"map": "TRD_07", "id": 1}, "reqs": []}, # Dungeon Fire Room Exit Right -> Dungeon Trap Exit Left

    {"from": {"map": "TRD_08", "id": 0}, "to": {"map": "TRD_08", "id": "ItemA"}, "reqs": [["can_climb_steps"]]}, #* Dungeon Fire Room Exit Right -> ItemA (KoopaFortressKey)
    {"from": {"map": "TRD_08", "id": "ItemA"}, "to": {"map": "TRD_08", "id": 0}, "reqs": []}, #* ItemA (KoopaFortressKey) -> Dungeon Fire Room Exit Right

    # TRD_09 Battlement
    {"from": {"map": "TRD_09", "id": 0}, "to": {"map": "TRD_01", "id": 3}, "reqs": []}, # Battlement Exit Left -> Left Tower Exit Top Right
    {"from": {"map": "TRD_09", "id": 1}, "to": {"map": "TRD_10", "id": 0}, "reqs": []}, # Battlement Exit Right -> Boss Battle Room Exit Left

    {"from": {"map": "TRD_09", "id": 0}, "to": {"map": "TRD_09", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Battlement Exit Left -> Battlement Exit Right
    {"from": {"map": "TRD_09", "id": 1}, "to": {"map": "TRD_09", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Battlement Exit Right -> Battlement Exit Left

    {"from": {"map": "TRD_09", "id": 0}, "to": {"map": "TRD_09", "id": "YBlockA"}, "reqs": [["Bombette"],["can_hit_floating_blocks"]]}, #* Battlement Exit Left -> YBlockA (MapleSyrup)
    {"from": {"map": "TRD_09", "id": 1}, "to": {"map": "TRD_09", "id": "YBlockA"}, "reqs": [["Bombette"],["can_hit_floating_blocks"]]}, #* Battlement Exit Right -> YBlockA (MapleSyrup)

    # TRD_10 Boss Battle Room
    {"from": {"map": "TRD_10", "id": 0}, "to": {"map": "TRD_09", "id": 1}, "reqs": []}, # Boss Battle Room Exit Left -> Battlement Exit Right

    {"from": {"map": "TRD_10", "id": 0}, "to": {"map": "TRD_10", "id": 0}, "reqs": [["Hammer","Bombette","Watt"]], "pseudoitems": ["STARSPIRIT_1","MF_Ch1_RescuedStarSpirit"]}, #+ Boss Battle Room Exit Left
]
