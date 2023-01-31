"""This file represents all edges of the world graph that have origin-nodes in the ISK (Dry Dry Ruins) area."""
# Note: Instead of checking for hammer-levels, these edges check for a custom RandomizerFlag "RF_ISK09_OpenedHammerChest".
#       This is because the hammer blocks in here change depending on wether or not the hammer chest in Mt. Lavalava was opened beforehand.
edges_isk = [
    # ISK_01 Entrance
    {"from": {"map": "ISK_01", "id": 0}, "to": {"map": "SBK_02", "id": 4}, "reqs": []}, # Entrance Exit Left -> N3W1 Ruins Entrance Enter Ruins
    {"from": {"map": "ISK_01", "id": 1}, "to": {"map": "ISK_02", "id": 0}, "reqs": []}, # Entrance Exit Right -> Sarcophagus Hall 1 Exit Left

    {"from": {"map": "ISK_01", "id": 0}, "to": {"map": "ISK_01", "id": 1}, "reqs": []}, #? Entrance Exit Left -> Entrance Exit Right
    {"from": {"map": "ISK_01", "id": 1}, "to": {"map": "ISK_01", "id": 0}, "reqs": []}, #? Entrance Exit Right -> Entrance Exit Left

    # ISK_02 Sarcophagus Hall 1
    {"from": {"map": "ISK_02", "id": 0}, "to": {"map": "ISK_01", "id": 1}, "reqs": []}, # Sarcophagus Hall 1 Exit Left -> Entrance Exit Right
    {"from": {"map": "ISK_02", "id": 1}, "to": {"map": "ISK_03", "id": 0}, "reqs": [[{"RuinsKey": 1}]]}, # Sarcophagus Hall 1 Exit Top Right -> Sand Drainage Room 1 Exit Upper Room Left
    {"from": {"map": "ISK_02", "id": 2}, "to": {"map": "ISK_03", "id": 1}, "reqs": []}, # Sarcophagus Hall 1 Exit Bottom Right -> Sand Drainage Room 1 Exit Lower Room Left

    {"from": {"map": "ISK_02", "id": 0}, "to": {"map": "ISK_02", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Sarcophagus Hall 1 Exit Left -> Sarcophagus Hall 1 Exit Top Right
    {"from": {"map": "ISK_02", "id": 1}, "to": {"map": "ISK_02", "id": 0}, "reqs": []}, #? Sarcophagus Hall 1 Exit Top Right -> Sarcophagus Hall 1 Exit Left
    {"from": {"map": "ISK_02", "id": 0}, "to": {"map": "ISK_02", "id": 2}, "reqs": []}, #? Sarcophagus Hall 1 Exit Left -> Sarcophagus Hall 1 Exit Bottom Right
    {"from": {"map": "ISK_02", "id": 2}, "to": {"map": "ISK_02", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Sarcophagus Hall 1 Exit Bottom Right -> Sarcophagus Hall 1 Exit Left

    {"from": {"map": "ISK_02", "id": 0}, "to": {"map": "ISK_02", "id": "ItemA"}, "reqs": []}, #* Sarcophagus Hall 1 Exit Left -> ItemA (SpikeShield)

    # ISK_03 Sand Drainage Room 1
    {"from": {"map": "ISK_03", "id": 0}, "to": {"map": "ISK_02", "id": 1}, "reqs": []}, # Sand Drainage Room 1 Exit Upper Room Left -> Sarcophagus Hall 1 Exit Top Right
    {"from": {"map": "ISK_03", "id": 1}, "to": {"map": "ISK_02", "id": 2}, "reqs": []}, # Sand Drainage Room 1 Exit Lower Room Left -> Sarcophagus Hall 1 Exit Bottom Right
    {"from": {"map": "ISK_03", "id": 2}, "to": {"map": "ISK_04", "id": 0}, "reqs": [["MF_ISK03_DrainedFirstSandRoom"],["Boots"]]}, # Sand Drainage Room 1 Exit Lower Room Right -> Descending Stairs 1 Exit Middle Left

    {"from": {"map": "ISK_03", "id": 1}, "to": {"map": "ISK_03", "id": 2}, "reqs": []}, #? Sand Drainage Room 1 Exit Lower Room Left -> Sand Drainage Room 1 Exit Lower Room Right
    {"from": {"map": "ISK_03", "id": 2}, "to": {"map": "ISK_03", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Sand Drainage Room 1 Exit Lower Room Right -> Sand Drainage Room 1 Exit Lower Room Left

    {"from": {"map": "ISK_03", "id": 0}, "to": {"map": "ISK_03", "id": 0}, "reqs": [["can_climb_steps"]], "pseudoitems": ["MF_ISK03_DrainedFirstSandRoom"]}, #+ Sand Drainage Room 1 Exit Upper Room Left

    {"from": {"map": "ISK_03", "id": 1}, "to": {"map": "ISK_03", "id": "ItemA"}, "reqs": [["can_climb_steps","MF_ISK03_DrainedFirstSandRoom"]]}, #* Sand Drainage Room 1 Exit Lower Room Left -> ItemA (RuinsKey)

    # ISK_04 Descending Stairs 1
    {"from": {"map": "ISK_04", "id": 0}, "to": {"map": "ISK_03", "id": 2}, "reqs": []}, # Descending Stairs 1 Exit Middle Left -> Sand Drainage Room 1 Exit Lower Room Right
    {"from": {"map": "ISK_04", "id": 1}, "to": {"map": "ISK_07", "id": 1}, "reqs": [[{"RuinsKey": 2}]]}, # Descending Stairs 1 Exit Bottom Left -> Sarcophagus Hall 2 Exit Right
    {"from": {"map": "ISK_04", "id": 2}, "to": {"map": "ISK_06", "id": 0}, "reqs": [["Bombette"]]}, # Descending Stairs 1 Exit Top Right Cracked Wall -> Sand Drainage Room 2 Exit Upper Room Left
    {"from": {"map": "ISK_04", "id": 3}, "to": {"map": "ISK_06", "id": 1}, "reqs": []}, # Descending Stairs 1 Exit Middle Right -> Sand Drainage Room 2 Exit Lower Room Left
    {"from": {"map": "ISK_04", "id": 4}, "to": {"map": "ISK_05", "id": 0}, "reqs": []}, # Descending Stairs 1 Exit Bottom Right -> Pyramid Stone Room Exit Left

    {"from": {"map": "ISK_04", "id": 0}, "to": {"map": "ISK_04", "id": 1}, "reqs": []}, #? Descending Stairs 1 Exit Middle Left -> Descending Stairs 1 Exit Bottom Left
    {"from": {"map": "ISK_04", "id": 1}, "to": {"map": "ISK_04", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Descending Stairs 1 Exit Bottom Left -> Descending Stairs 1 Exit Middle Left
    {"from": {"map": "ISK_04", "id": 0}, "to": {"map": "ISK_04", "id": 2}, "reqs": [["Parakarry"]]}, #? Descending Stairs 1 Exit Middle Left -> Descending Stairs 1 Exit Top Right Cracked Wall
    {"from": {"map": "ISK_04", "id": 2}, "to": {"map": "ISK_04", "id": 0}, "reqs": []}, #? Descending Stairs 1 Exit Top Right Cracked Wall -> Descending Stairs 1 Exit Middle Left
    {"from": {"map": "ISK_04", "id": 0}, "to": {"map": "ISK_04", "id": 3}, "reqs": []}, #? Descending Stairs 1 Exit Middle Left -> Descending Stairs 1 Exit Middle Right
    {"from": {"map": "ISK_04", "id": 3}, "to": {"map": "ISK_04", "id": 0}, "reqs": []}, #? Descending Stairs 1 Exit Middle Right -> Descending Stairs 1 Exit Middle Left
    {"from": {"map": "ISK_04", "id": 0}, "to": {"map": "ISK_04", "id": 4}, "reqs": [["can_climb_steps"]]}, #? Descending Stairs 1 Exit Middle Left -> Descending Stairs 1 Exit Bottom Right
    {"from": {"map": "ISK_04", "id": 4}, "to": {"map": "ISK_04", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Descending Stairs 1 Exit Bottom Right -> Descending Stairs 1 Exit Middle Left
    {"from": {"map": "ISK_04", "id": 4}, "to": {"map": "ISK_04", "id": 1}, "reqs": []}, #? Descending Stairs 1 Exit Bottom Right -> Descending Stairs 1 Exit Bottom Left

    # ISK_05 Pyramid Stone Room
    {"from": {"map": "ISK_05", "id": 0}, "to": {"map": "ISK_04", "id": 4}, "reqs": []}, # Pyramid Stone Room Exit Left -> Descending Stairs 1 Exit Bottom Right

    {"from": {"map": "ISK_05", "id": 0}, "to": {"map": "ISK_05", "id": "ItemA"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]}, #* Pyramid Stone Room Exit Left -> ItemA (PyramidStone)

    # ISK_06 Sand Drainage Room 2
    {"from": {"map": "ISK_06", "id": 0}, "to": {"map": "ISK_04", "id": 2}, "reqs": []}, # Sand Drainage Room 2 Exit Upper Room Left -> Descending Stairs 1 Exit Top Right Cracked Wall
    {"from": {"map": "ISK_06", "id": 1}, "to": {"map": "ISK_04", "id": 3}, "reqs": []}, # Sand Drainage Room 2 Exit Lower Room Left -> Descending Stairs 1 Exit Middle Right

    {"from": {"map": "ISK_06", "id": 0}, "to": {"map": "ISK_06", "id": "ItemA"}, "reqs": [["MF_ISK06_DrainedSecondSandRoom"]]}, #* Sand Drainage Room 2 Exit Upper Room Left -> ItemA (StarPiece)
    {"from": {"map": "ISK_06", "id": 1}, "to": {"map": "ISK_06", "id": "ItemB"}, "reqs": [["MF_ISK06_DrainedSecondSandRoom"]]}, #* Sand Drainage Room 2 Exit Lower Room Left -> ItemB (RuinsKey)

    {"from": {"map": "ISK_06", "id": 0}, "to": {"map": "ISK_06", "id": 0}, "reqs": [["can_climb_steps"]], "pseudoitems": ["MF_ISK06_DrainedSecondSandRoom"]}, #+ Sand Drainage Room 2 Exit Upper Room Left

    # ISK_07 Sarcophagus Hall 2
    {"from": {"map": "ISK_07", "id": 0}, "to": {"map": "ISK_08", "id": 2}, "reqs": [[{"RuinsKey": 3}]]}, # Sarcophagus Hall 2 Exit Left -> Descending Stairs 2 Exit Top Right
    {"from": {"map": "ISK_07", "id": 1}, "to": {"map": "ISK_04", "id": 1}, "reqs": []}, # Sarcophagus Hall 2 Exit Right -> Descending Stairs 1 Exit Bottom Left

    {"from": {"map": "ISK_07", "id": 0}, "to": {"map": "ISK_07", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Sarcophagus Hall 2 Exit Left -> Sarcophagus Hall 2 Exit Right
    {"from": {"map": "ISK_07", "id": 1}, "to": {"map": "ISK_07", "id": 0}, "reqs": []}, #? Sarcophagus Hall 2 Exit Right -> Sarcophagus Hall 2 Exit Left

    {"from": {"map": "ISK_07", "id": 1}, "to": {"map": "ISK_07", "id": "ItemA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Sarcophagus Hall 2 Exit Right -> ItemA (RuinsKey)
    {"from": {"map": "ISK_07", "id": 1}, "to": {"map": "ISK_07", "id": "ItemB"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]}, #* Sarcophagus Hall 2 Exit Right -> ItemB (Artifact)

    # ISK_08 Descending Stairs 2
    {"from": {"map": "ISK_08", "id": 0}, "to": {"map": "ISK_09", "id": 0}, "reqs": []}, # Descending Stairs 2 Exit Top Left -> Super Hammer Room Exit Right
    {"from": {"map": "ISK_08", "id": 1}, "to": {"map": "ISK_10", "id": 0}, "reqs": [["Bombette"]]}, # Descending Stairs 2 Exit Bottom Left Cracked Wall -> Vertical Shaft Exit Top Right
    {"from": {"map": "ISK_08", "id": 2}, "to": {"map": "ISK_07", "id": 0}, "reqs": []}, # Descending Stairs 2 Exit Top Right -> Sarcophagus Hall 2 Exit Left
    {"from": {"map": "ISK_08", "id": 3}, "to": {"map": "ISK_11", "id": 0}, "reqs": []}, # Descending Stairs 2 Exit Bottom Right -> Stone Puzzle Room Exit Left

    {"from": {"map": "ISK_08", "id": 2}, "to": {"map": "ISK_08", "id": 0}, "reqs": [["Parakarry"]]}, #? Descending Stairs 2 Exit Top Right -> Descending Stairs 2 Exit Top Left
    {"from": {"map": "ISK_08", "id": 0}, "to": {"map": "ISK_08", "id": 3}, "reqs": []}, #? Descending Stairs 2 Exit Top Left -> Descending Stairs 2 Exit Bottom Right
    {"from": {"map": "ISK_08", "id": 3}, "to": {"map": "ISK_08", "id": 1}, "reqs": []}, #? Descending Stairs 2 Exit Bottom Right -> Descending Stairs 2 Exit Bottom Left Cracked Wall
    {"from": {"map": "ISK_08", "id": 1}, "to": {"map": "ISK_08", "id": 3}, "reqs": []}, #? Descending Stairs 2 Exit Bottom Left Cracked Wall -> Descending Stairs 2 Exit Bottom Right
    {"from": {"map": "ISK_08", "id": 3}, "to": {"map": "ISK_08", "id": 2}, "reqs": [["can_climb_steps"]]}, #? Descending Stairs 2 Exit Bottom Right -> Descending Stairs 2 Exit Top Right
    {"from": {"map": "ISK_08", "id": 2}, "to": {"map": "ISK_08", "id": 3}, "reqs": []}, #? Descending Stairs 2 Exit Top Right -> Descending Stairs 2 Exit Bottom Right

    # ISK_09 Super Hammer Room
    {"from": {"map": "ISK_09", "id": 0}, "to": {"map": "ISK_08", "id": 0}, "reqs": []}, # Super Hammer Room Exit Right -> Descending Stairs 2 Exit Top Left

    {"from": {"map": "ISK_09", "id": 0}, "to": {"map": "ISK_09", "id": "ChestA"},   "reqs": [["can_climb_steps"]]}, #* Super Hammer Room Exit Right -> ChestA (SlowGo)
    {"from": {"map": "ISK_09", "id": 0}, "to": {"map": "ISK_09", "id": "BigChest"}, "reqs": [["can_climb_steps"]], "pseudoitems": ["RF_ISK09_OpenedHammerChest"]}, #* Super Hammer Room Exit Right -> BigChest (SuperHammer)

    # ISK_10 Vertical Shaft
    {"from": {"map": "ISK_10", "id": 0}, "to": {"map": "ISK_08", "id": 1}, "reqs": [["Bombette"]]}, # Vertical Shaft Exit Top Right -> Descending Stairs 2 Exit Bottom Left Cracked Wall
    {"from": {"map": "ISK_10", "id": 1}, "to": {"map": "ISK_14", "id": 0}, "reqs": [["Bombette"]]}, # Vertical Shaft Exit Bottom Left -> Diamond Stone Room Exit Right
    {"from": {"map": "ISK_10", "id": 2}, "to": {"map": "ISK_18", "id": 0}, "reqs": []}, # Vertical Shaft Exit Bottom Right -> Deep Tunnel Exit Left

    {"from": {"map": "ISK_10", "id": 2}, "to": {"map": "ISK_10", "id": 1}, "reqs": []}, #? Vertical Shaft Exit Bottom Right -> Vertical Shaft Exit Bottom Left
    {"from": {"map": "ISK_10", "id": 1}, "to": {"map": "ISK_10", "id": 2}, "reqs": []}, #? Vertical Shaft Exit Bottom Left -> Vertical Shaft Exit Bottom Right
    {"from": {"map": "ISK_10", "id": 2}, "to": {"map": "ISK_10", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Vertical Shaft Exit Bottom Right -> Vertical Shaft Exit Top Right
    {"from": {"map": "ISK_10", "id": 0}, "to": {"map": "ISK_10", "id": 2}, "reqs": []}, #? Vertical Shaft Exit Top Right -> Vertical Shaft Exit Bottom Right

    # ISK_11 Stone Puzzle Room
    {"from": {"map": "ISK_11", "id": 0}, "to": {"map": "ISK_08", "id": 3}, "reqs": []}, # Stone Puzzle Room Exit Left -> Descending Stairs 2 Exit Bottom Right
    {"from": {"map": "ISK_11", "id": 1}, "to": {"map": "ISK_12", "id": 0}, "reqs": [[{"RuinsKey": 4}]]}, # Stone Puzzle Room Exit Top Right -> Sand Drainage Room 3 Exit Upper Room Left
    {"from": {"map": "ISK_11", "id": 2}, "to": {"map": "ISK_12", "id": 1}, "reqs": []}, # Stone Puzzle Room Exit Bottom Right -> Sand Drainage Room 3 Exit Top Left
    {"from": {"map": "ISK_11", "id": 3}, "to": {"map": "ISK_19", "id": 0}, "reqs": []}, # Stone Puzzle Room Exit Hidden Stairway -> Boss Antechamber Exit Left

    {"from": {"map": "ISK_11", "id": 0}, "to": {"map": "ISK_11", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Stone Puzzle Room Exit Left -> Stone Puzzle Room Exit Top Right
    {"from": {"map": "ISK_11", "id": 1}, "to": {"map": "ISK_11", "id": 0}, "reqs": []}, #? Stone Puzzle Room Exit Top Right -> Stone Puzzle Room Exit Left
    {"from": {"map": "ISK_11", "id": 0}, "to": {"map": "ISK_11", "id": 2}, "reqs": []}, #? Stone Puzzle Room Exit Left -> Stone Puzzle Room Exit Bottom Right
    {"from": {"map": "ISK_11", "id": 2}, "to": {"map": "ISK_11", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Stone Puzzle Room Exit Bottom Right -> Stone Puzzle Room Exit Left
    {"from": {"map": "ISK_11", "id": 0}, "to": {"map": "ISK_11", "id": 3}, "reqs": [["PyramidStone"],["DiamondStone"],["LunarStone"],["RF_DrainedThirdSandRoomAndCanSolvePuzzle"]], "pseudoitems": ["MB_Ch2_Spirit_ISK11_SolvedArtifactPuzzle"]}, #? Stone Puzzle Room Exit Left -> Stone Puzzle Room Exit Hidden Stairway
    {"from": {"map": "ISK_11", "id": 3}, "to": {"map": "ISK_11", "id": 0}, "reqs": [["MB_Ch2_Spirit_ISK11_SolvedArtifactPuzzle"],["can_climb_steps"]]}, #? Stone Puzzle Room Exit Hidden Stairway -> Stone Puzzle Room Exit Left

    # ISK_12 Sand Drainage Room 3
    {"from": {"map": "ISK_12", "id": 0}, "to": {"map": "ISK_11", "id": 1}, "reqs": []}, # Sand Drainage Room 3 Exit Upper Room Left -> Stone Puzzle Room Exit Top Right
    {"from": {"map": "ISK_12", "id": 1}, "to": {"map": "ISK_11", "id": 2}, "reqs": []}, # Sand Drainage Room 3 Exit Top Left -> Stone Puzzle Room Exit Bottom Right
    {"from": {"map": "ISK_12", "id": 2}, "to": {"map": "ISK_18", "id": 1}, "reqs": []}, # Sand Drainage Room 3 Exit Bottom Left -> Deep Tunnel Exit Right
    {"from": {"map": "ISK_12", "id": 3}, "to": {"map": "ISK_13", "id": 0}, "reqs": []}, # Sand Drainage Room 3 Exit Top Right -> Lunar Stone Room Exit Left

    #{"from": {"map": "ISK_12", "id": 1}, "to": {"map": "ISK_12", "id": 2}, "reqs": [["RF_NeverTraversible"]]}, #? Sand Drainage Room 3 Exit Top Left -> Sand Drainage Room 3 Exit Bottom Left
    {"from": {"map": "ISK_12", "id": 1}, "to": {"map": "ISK_12", "id": 3}, "reqs": [["RF_DrainedThirdSandRoomAndCanSolvePuzzle"]]}, #? Sand Drainage Room 3 Exit Top Left -> Sand Drainage Room 3 Exit Top Right
    {"from": {"map": "ISK_12", "id": 3}, "to": {"map": "ISK_12", "id": 1}, "reqs": [["RF_DrainedThirdSandRoomAndCanSolvePuzzle"],["can_climb_steps"]]}, #? Sand Drainage Room 3 Exit Top Right -> Sand Drainage Room 3 Exit Top Left
    #{"from": {"map": "ISK_12", "id": 3}, "to": {"map": "ISK_12", "id": 2}, "reqs": [["RF_NeverTraversible"]]}, #? Sand Drainage Room 3 Exit Top Right -> Sand Drainage Room 3 Exit Bottom Left

    {"from": {"map": "ISK_12", "id": 0}, "to": {"map": "ISK_12", "id": 0}, "reqs": [["can_climb_steps"]], "pseudoitems": ["RF_DrainedThirdSandRoomAndCanSolvePuzzle"]}, #+ Sand Drainage Room 3 Exit Upper Room Left
    {"from": {"map": "ISK_12", "id": 1}, "to": {"map": "ISK_12", "id": 1}, "reqs": [], "pseudoitems": ["RF_ISK12_CanEnterFromAbove"]}, #+ Sand Drainage Room 3 Exit Top Left
    {"from": {"map": "ISK_12", "id": 3}, "to": {"map": "ISK_12", "id": 3}, "reqs": [], "pseudoitems": ["RF_ISK12_CanEnterFromAbove"]}, #+ Sand Drainage Room 3 Exit Top Right

    {"from": {"map": "ISK_12", "id": 1},       "to": {"map": "ISK_12", "id": "ItemA"}, "reqs": [["RF_DrainedThirdSandRoomAndCanSolvePuzzle","can_climb_steps"],["RF_DrainedThirdSandRoomAndCanSolvePuzzle","RF_ISK09_OpenedHammerChest"]]}, #* Sand Drainage Room 3 Exit Top Left -> ItemA (RuinsKey)
    {"from": {"map": "ISK_12", "id": "ItemA"}, "to": {"map": "ISK_12", "id": 1},       "reqs": [["can_climb_steps"],["RF_ISK12_CanEnterFromAbove"]]}, #* ItemA (RuinsKey) -> Sand Drainage Room 3 Exit Top Left
    {"from": {"map": "ISK_12", "id": 2},       "to": {"map": "ISK_12", "id": "ItemA"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]}, #* Sand Drainage Room 3 Exit Bottom Left -> ItemA (RuinsKey)
    {"from": {"map": "ISK_12", "id": 3},       "to": {"map": "ISK_12", "id": "ItemA"}, "reqs": []}, #* Sand Drainage Room 3 Exit Top Right -> ItemA (RuinsKey)
    {"from": {"map": "ISK_12", "id": "ItemA"}, "to": {"map": "ISK_12", "id": 3},       "reqs": [["RF_DrainedThirdSandRoomAndCanSolvePuzzle"],["RF_ISK12_CanEnterFromAbove"]]}, #* ItemA (RuinsKey) -> Sand Drainage Room 3 Exit Top Right

    # ISK_13 Lunar Stone Room
    {"from": {"map": "ISK_13", "id": 0}, "to": {"map": "ISK_12", "id": 3}, "reqs": []}, # Lunar Stone Room Exit Left -> Sand Drainage Room 3 Exit Top Right

    {"from": {"map": "ISK_13", "id": 0}, "to": {"map": "ISK_13", "id": "ItemA"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]}, #* Lunar Stone Room Exit Left -> ItemA (LunarStone)

    # ISK_14 Diamond Stone Room
    {"from": {"map": "ISK_14", "id": 0}, "to": {"map": "ISK_10", "id": 1}, "reqs": []}, # Diamond Stone Room Exit Right -> Vertical Shaft Exit Bottom Left

    {"from": {"map": "ISK_14", "id": 0}, "to": {"map": "ISK_14", "id": "ItemA"}, "reqs": [["RF_ISK09_OpenedHammerChest"],["can_climb_steps"]]}, #* Diamond Stone Room Exit Right -> ItemA (DiamondStone)

    # ISK_16 Tutankoopa Room
    {"from": {"map": "ISK_16", "id": 0}, "to": {"map": "ISK_19", "id": 1}, "reqs": []}, # Tutankoopa Room Exit Left -> Boss Antechamber Exit Right

    {"from": {"map": "ISK_16", "id": 0}, "to": {"map": "ISK_16", "id": 0}, "reqs": [["MB_Ch2_Spirit_ISK11_SolvedArtifactPuzzle"]], "pseudoitems": ["STARSPIRIT_2", "RF_Ch2_SavedStarSpirit"]}, #+ Tutankoopa Room Exit Left

    # ISK_18 Deep Tunnel
    {"from": {"map": "ISK_18", "id": 0}, "to": {"map": "ISK_10", "id": 2}, "reqs": []}, # Deep Tunnel Exit Left -> Vertical Shaft Exit Bottom Right
    {"from": {"map": "ISK_18", "id": 1}, "to": {"map": "ISK_12", "id": 2}, "reqs": []}, # Deep Tunnel Exit Right -> Sand Drainage Room 3 Exit Bottom Left

    #{"from": {"map": "ISK_18", "id": 0}, "to": {"map": "ISK_18", "id": 1}, "reqs": [["RF_NeverTraversible"]]}, #? Deep Tunnel Exit Left -> Deep Tunnel Exit Right
    {"from": {"map": "ISK_18", "id": 1}, "to": {"map": "ISK_18", "id": 0}, "reqs": []}, #? Deep Tunnel Exit Right -> Deep Tunnel Exit Left

    # ISK_19 Boss Antechamber
    {"from": {"map": "ISK_19", "id": 0}, "to": {"map": "ISK_11", "id": 3}, "reqs": []}, # Boss Antechamber Exit Left -> Stone Puzzle Room Exit Hidden Stairway
    {"from": {"map": "ISK_19", "id": 1}, "to": {"map": "ISK_16", "id": 0}, "reqs": []}, # Boss Antechamber Exit Right -> Tutankoopa Room Exit Left

    {"from": {"map": "ISK_19", "id": 0}, "to": {"map": "ISK_19", "id": 1}, "reqs": []}, #? Boss Antechamber Exit Left -> Boss Antechamber Exit Right
    {"from": {"map": "ISK_19", "id": 1}, "to": {"map": "ISK_19", "id": 0}, "reqs": []}, #? Boss Antechamber Exit Right -> Boss Antechamber Exit Left
]
