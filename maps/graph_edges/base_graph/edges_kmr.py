"""This file represents all edges of the world graph that have origin-nodes in the KMR (Goomba Region) area."""
edges_kmr  = [
    # KMR_00 Forest Clearing
    {"from": {"map": "KMR_00", "id": 0}, "to": {"map": "KMR_02", "id": 1}, "reqs": []}, # Forest Clearing Exit East -> Goomba Village Exit Left

    {"from": {"map": "KMR_00", "id": 0}, "to": {"map": "KMR_00", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Forest Clearing Exit East -> HiddenPanel

    # KMR_02 Goomba Village
    {"from": {"map": "KMR_02", "id": 0}, "to": {"map": "KMR_09", "id": 0}, "reqs": []}, # Goomba Village Exit Right -> Goomba Road 1 Exit Left
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_00", "id": 0}, "reqs": []}, # Goomba Village Exit Left -> Forest Clearing Exit East
    {"from": {"map": "KMR_02", "id": 2}, "to": {"map": "KMR_05", "id": 1}, "reqs": []}, # Goomba Village Exit Top Left -> Behind the Village Exit Right
    {"from": {"map": "KMR_02", "id": 3}, "to": {"map": "TIK_01", "id": 2}, "reqs": []}, # Goomba Village Blue Warp Pipe -> Warp Zone 1 (B1) Blue Pipe (Right)
    {"from": {"map": "KMR_02", "id": "GiftB"}, "to": {"map": "KMR_03", "id": 0}, "reqs": [["RF_BrokenVeranda"]]}, # Pseudo-Edge: Fall from balcony during vanilla start

    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": 0}, "reqs": [["Hammer", "Bombette"]]}, #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 0}, "to": {"map": "KMR_02", "id": 1}, "reqs": [["Hammer", "Bombette"]]}, #? Goomba Village Exit Right -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": 2}, "reqs": []}, #? Goomba Village Exit Left -> Goomba Village Exit Top Left
    {"from": {"map": "KMR_02", "id": 2}, "to": {"map": "KMR_02", "id": 1}, "reqs": []}, #? Goomba Village Exit Top Left -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": 3}, "reqs": [["GF_TIK01_WarpPipes"],["Boots"]]}, #? Goomba Village Exit Left -> Goomba Village Blue Warp Pipe
    {"from": {"map": "KMR_02", "id": 3}, "to": {"map": "KMR_02", "id": 1}, "reqs": []}, #? Goomba Village Blue Warp Pipe -> Goomba Village Exit Left

    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "ItemA"},        "reqs": [["RF_FixedVeranda"]]}, #* Goomba Village Exit Left -> ItemA (ShootingStar)
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "GiftA"},        "reqs": [["FAVOR_2_01_active"]]}, #* Goomba Village Exit Left -> GiftA (KootTheTape)
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "GiftB"},        "reqs": []}, #* Goomba Village Exit Left -> GiftB (PowerJump)
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "GiftC"},        "reqs": [["Dolly"]]}, #* Goomba Village Exit Left -> GiftC (StarPiece)
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "GiftD"},        "reqs": [["Parakarry"],["Letter02"]]}, #* Goomba Village Exit Left -> GiftD (StarPiece)
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "GiftE"},        "reqs": [["Parakarry"],["Letter10"]]}, #* Goomba Village Exit Left -> GiftE (Letter13)
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "GiftF"},        "reqs": [["Parakarry"],["Letter24"]]}, #* Goomba Village Exit Left -> GiftE (LuckyDay)
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* Goomba Village Exit Left -> Tree1_Drop1A (Goomnut)
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "Partner"},      "reqs": []}, #* Goomba Village Exit Left -> Partner (Goombario)
    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": "Bush2_Drop1"},  "reqs": []}, #* Goomba Village Exit Left -> Bush2_Drop1 (Coin)

    {"from": {"map": "KMR_02", "id": 1}, "to": {"map": "KMR_02", "id": 1}, "reqs": [], "pseudoitems": ["StarPiece_KMR_1",
                                                                                                     #  "StarPiece_KMR_2",
                                                                                                     #  "StarPiece_KMR_3",
                                                                                                     #  "StarPiece_KMR_4",
                                                                                                     #  "StarPiece_KMR_5",
                                                                                                     #  "StarPiece_KMR_6",
                                                                                                     #  "StarPiece_KMR_7",
                                                                                                       "StarPiece_KMR_8"]}, #+ Quizmo StarPieces

    # KMR_05 Behind the Village
    {"from": {"map": "KMR_05", "id": 0}, "to": {"map": "KMR_03", "id": 1}, "reqs": []}, # Behind the Village Exit Left -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_05", "id": 1}, "to": {"map": "KMR_02", "id": 2}, "reqs": []}, # Behind the Village Exit Right -> Goomba Village Exit Top Left

    {"from": {"map": "KMR_05", "id": 0}, "to": {"map": "KMR_05", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Behind the Village Exit Left -> Behind the Village Exit Right
    {"from": {"map": "KMR_05", "id": 1}, "to": {"map": "KMR_05", "id": 0}, "reqs": []}, #? Behind the Village Exit Right -> Behind the Village Exit Left

    {"from": {"map": "KMR_05", "id": 1}, "to": {"map": "KMR_05", "id": "ItemA"},        "reqs": [["Boots"]]}, #* Behind the Village Exit Right -> ItemA (StarPiece)
    {"from": {"map": "KMR_05", "id": 1}, "to": {"map": "KMR_05", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"],["Boots"]]}, #* Behind the Village Exit Right -> Tree1_Drop1A (Coin)

    # KMR_03 Bottom of the Cliff
    {"from": {"map": "KMR_03", "id": 0}, "to": {"map": "KMR_04", "id": 0}, "reqs": []}, # Bottom of the Cliff Exit Left -> Jr. Troopa's Playground Exit Right
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_05", "id": 0}, "reqs": []}, # Bottom of the Cliff Exit Right -> Behind the Village Exit Left

    {"from": {"map": "KMR_03", "id": 0}, "to": {"map": "KMR_03", "id": 1}, "reqs": [["Hammer", "Bombette"]], "pseudoitems": ["RF_FixedVeranda"]}, #? Bottom of the Cliff Exit Left -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_03", "id": 0}, "reqs": [["Hammer", "Bombette"]], "pseudoitems": ["RF_FixedVeranda"]}, #? Bottom of the Cliff Exit Right -> Bottom of the Cliff Exit Left

    {"from": {"map": "KMR_03", "id": 0},       "to": {"map": "KMR_03", "id": "YBlockA"},       "reqs": [["can_hit_grounded_blocks"]]}, #* Bottom of the Cliff Exit Left -> YBlockA (Coin)
    {"from": {"map": "KMR_03", "id": 0},       "to": {"map": "KMR_03", "id": "Tree1_Drop1A"},  "reqs": [["can_shake_trees"]]}, #* Bottom of the Cliff Exit Left -> Tree1_Drop1A (Mushroom)
    {"from": {"map": "KMR_03", "id": 1},       "to": {"map": "KMR_03", "id": "HiddenPanel"},   "reqs": [["can_flip_panels"]]}, #* Bottom of the Cliff Exit Right -> HiddenPanel (StarPiece)
    {"from": {"map": "KMR_03", "id": 1},       "to": {"map": "KMR_03", "id": "HiddenYBlockA"}, "reqs": [["SuperHammer"],["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* Bottom of the Cliff Exit Right -> HiddenYBlockA (RepelGel)
    {"from": {"map": "KMR_03", "id": 1},       "to": {"map": "KMR_03", "id": "ItemA"},         "reqs": [["can_climb_steps"]]}, #* Bottom of the Cliff Exit Right -> ItemA (Coin)
    {"from": {"map": "KMR_03", "id": "ItemA"}, "to": {"map": "KMR_03", "id": "ItemB"},         "reqs": []}, #+ SHARED REQUIREMENTS -> ItemB (Coin)
    {"from": {"map": "KMR_03", "id": "ItemA"}, "to": {"map": "KMR_03", "id": "ItemC"},         "reqs": []}, #+ SHARED REQUIREMENTS -> ItemC (Coin)
    {"from": {"map": "KMR_03", "id": "ItemA"}, "to": {"map": "KMR_03", "id": "ItemD"},         "reqs": []}, #+ SHARED REQUIREMENTS -> ItemD (Coin)
    {"from": {"map": "KMR_03", "id": "ItemA"}, "to": {"map": "KMR_03", "id": "ItemE"},         "reqs": []}, #+ SHARED REQUIREMENTS -> ItemE (FireFlower)

    # KMR_04 Jr. Troopa's Playground
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_03", "id": 0}, "reqs": []}, # Jr. Troopa's Playground Exit Right -> Bottom of the Cliff Exit Left

    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Tree1_Drop1"},  "reqs": [["can_shake_trees"]]}, #* Jr. Troopa's Playground Exit Right -> Tree1_Drop1 (Coin)
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Tree2_Drop1"},  "reqs": [["can_shake_trees"]]}, #* Jr. Troopa's Playground Exit Right -> Tree2_Drop1 (Coin)
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Tree3_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* Jr. Troopa's Playground Exit Right -> Tree3_Drop1A (Dolly)
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Bush1_Drop1"},  "reqs": []}, #* Jr. Troopa's Playground Exit Right -> Bush1_Drop1 (Coin)
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Bush2_Drop1"},  "reqs": []}, #* Jr. Troopa's Playground Exit Right -> Bush2_Drop1 (Coin)
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Bush3_Drop1A"}, "reqs": []}, #* Jr. Troopa's Playground Exit Right -> Bush3_Drop1A (Coin)
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Bush3_Drop1B"}, "reqs": []}, #* Jr. Troopa's Playground Exit Right -> Bush3_Drop1B (Coin)
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Bush4_Drop1"},  "reqs": []}, #* Jr. Troopa's Playground Exit Right -> Bush4_Drop1 (Coin)
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Bush5_Drop1"},  "reqs": []}, #* Jr. Troopa's Playground Exit Right -> Bush5_Drop1 (Coin)
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_04", "id": "Bush7_Drop1"},  "reqs": []}, #* Jr. Troopa's Playground Exit Right -> Bush7_Drop1 (Hammer)

    # KMR_09 Goomba Road 1
    {"from": {"map": "KMR_09", "id": 0}, "to": {"map": "KMR_02", "id": 0}, "reqs": []}, # Goomba Road 1 Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_09", "id": 1}, "to": {"map": "KMR_06", "id": 0}, "reqs": []}, # Goomba Road 1 Exit Right -> Goomba Road 2 Exit Left

    {"from": {"map": "KMR_09", "id": 0}, "to": {"map": "KMR_09", "id": 1}, "reqs": []}, #? Goomba Road 1 Exit Left -> Goomba Road 1 Exit Right
    {"from": {"map": "KMR_09", "id": 1}, "to": {"map": "KMR_09", "id": 0}, "reqs": []}, #? Goomba Road 1 Exit Right -> Goomba Road 1 Exit Left

    {"from": {"map": "KMR_09", "id": 1},         "to": {"map": "KMR_09", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Goomba Road 1 Exit Right -> YBlockA (Coin)
    {"from": {"map": "KMR_09", "id": "YBlockA"}, "to": {"map": "KMR_09", "id": "YBlockB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockB (Coin)

    # KMR_06 Goomba Road 2
    {"from": {"map": "KMR_06", "id": 0}, "to": {"map": "KMR_09", "id": 1}, "reqs": []}, # Goomba Road 2 Exit Left -> Goomba Road 1 Exit Right
    {"from": {"map": "KMR_06", "id": 1}, "to": {"map": "KMR_07", "id": 0}, "reqs": []}, # Goomba Road 2 Exit Right -> Goomba Road 3 Exit Left

    {"from": {"map": "KMR_06", "id": 0}, "to": {"map": "KMR_06", "id": 1}, "reqs": []}, #? Goomba Road 2 Exit Left -> Goomba Road 2 Exit Right
    {"from": {"map": "KMR_06", "id": 1}, "to": {"map": "KMR_06", "id": 0}, "reqs": []}, #? Goomba Road 2 Exit Right -> Goomba Road 2 Exit Left

    {"from": {"map": "KMR_06", "id": 0}, "to": {"map": "KMR_06", "id": "ItemA"},   "reqs": []}, #* Goomba Road 2 Exit Left -> ItemA (Mushroom)
    {"from": {"map": "KMR_06", "id": 0}, "to": {"map": "KMR_06", "id": "RBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Goomba Road 2 Exit Left -> RBlockA (CloseCall)

    # KMR_07 Goomba Road 3
    {"from": {"map": "KMR_07", "id": 0}, "to": {"map": "KMR_06", "id": 1}, "reqs": []}, # Goomba Road 3 Exit Left -> Goomba Road 2 Exit Right
    {"from": {"map": "KMR_07", "id": 1}, "to": {"map": "KMR_12", "id": 0}, "reqs": []}, # Goomba Road 3 Exit Right -> Goomba Road 4 Exit Left

    {"from": {"map": "KMR_07", "id": 0}, "to": {"map": "KMR_07", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Goomba Road 3 Exit Left -> Goomba Road 3 Exit Right
    {"from": {"map": "KMR_07", "id": 1}, "to": {"map": "KMR_07", "id": 0}, "reqs": []}, #? Goomba Road 3 Exit Right -> Goomba Road 3 Exit Left

    {"from": {"map": "KMR_07", "id": 0}, "to": {"map": "KMR_07", "id": 0}, "reqs": [], "pseudoitems": ["RF_BeatGoombaBros"]}, #+ Defeat Goomba Bros.

    # KMR_12 Goomba Road 4
    {"from": {"map": "KMR_12", "id": 0}, "to": {"map": "KMR_07", "id": 1}, "reqs": []}, # Goomba Road 4 Exit Left -> Goomba Road 3 Exit Right
    {"from": {"map": "KMR_12", "id": 1}, "to": {"map": "KMR_11", "id": 0}, "reqs": []}, # Goomba Road 4 Exit Right -> Goomba King's Castle Exit Left

    {"from": {"map": "KMR_12", "id": 0}, "to": {"map": "KMR_12", "id": 1}, "reqs": []}, #? Goomba Road 4 Exit Left -> Goomba Road 4 Exit Right
    {"from": {"map": "KMR_12", "id": 1}, "to": {"map": "KMR_12", "id": 0}, "reqs": []}, #? Goomba Road 4 Exit Right -> Goomba Road 4 Exit Left

    # KMR_11 Goomba King's Castle
    {"from": {"map": "KMR_11", "id": 0}, "to": {"map": "KMR_12", "id": 1}, "reqs": []}, # Goomba King's Castle Exit Left -> Goomba Road 4 Exit Right
    {"from": {"map": "KMR_11", "id": 1}, "to": {"map": "KMR_10", "id": 0}, "reqs": []}, # Goomba King's Castle Exit Right -> Toad Town Entrance Exit Left

    {"from": {"map": "KMR_11", "id": 0}, "to": {"map": "KMR_11", "id": 1}, "reqs": [["RF_BeatGoombaBros"],["can_climb_steps","Hammer","Kooper","Bombette"]], "pseudoitems": ["RF_BeatGoombaKing"]}, #? Goomba King's Castle Exit Left -> Goomba King's Castle Exit Right
    {"from": {"map": "KMR_11", "id": 1}, "to": {"map": "KMR_11", "id": 0}, "reqs": [["RF_BeatGoombaKing"]]}, #? Goomba King's Castle Exit Right -> Goomba King's Castle Exit Left

    {"from": {"map": "KMR_11", "id": 0}, "to": {"map": "KMR_11", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* Goomba King's Castle Exit Left -> Tree1_Drop1A (StarPiece)
    {"from": {"map": "KMR_11", "id": 1}, "to": {"map": "KMR_11", "id": "HiddenPanel"},  "reqs": [["can_flip_panels"]]}, #* Goomba King's Castle Exit Right -> HiddenPanel (StarPiece)
    {"from": {"map": "KMR_11", "id": 1}, "to": {"map": "KMR_11", "id": "YBlockA"},      "reqs": [["can_hit_grounded_blocks"],["can_hit_floating_blocks"]]}, #* Goomba King's Castle Exit Right -> YBlockA (SuperShroom)
    {"from": {"map": "KMR_11", "id": 1}, "to": {"map": "KMR_11", "id": "Tree2_Drop1"},  "reqs": [["can_shake_trees"]]}, #* Goomba King's Castle Exit Right -> Tree2_Drop1 (Coin)

    # KMR_10 Toad Town Entrance
    {"from": {"map": "KMR_10", "id": 0}, "to": {"map": "KMR_11", "id": 1}, "reqs": []}, # Toad Town Entrance Exit Left -> Goomba King's Castle Exit Right
    {"from": {"map": "KMR_10", "id": 1}, "to": {"map": "MAC_00", "id": 0}, "reqs": []}, # Toad Town Entrance Exit Right -> Gate District Exit Left

    {"from": {"map": "KMR_10", "id": 0}, "to": {"map": "KMR_10", "id": 1}, "reqs": []}, #? Toad Town Entrance Exit Left -> Toad Town Entrance Exit Right
    {"from": {"map": "KMR_10", "id": 1}, "to": {"map": "KMR_10", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Toad Town Entrance Exit Right -> Toad Town Entrance Exit Left

    {"from": {"map": "KMR_10", "id": 1}, "to": {"map": "KMR_10", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Toad Town Entrance Exit Right -> YBlockA (SleepySheep)
    {"from": {"map": "KMR_10", "id": 1}, "to": {"map": "KMR_10", "id": "ChestA"},  "reqs": [["can_shake_trees"],["can_climb_steps"]]}, #* Toad Town Entrance Exit Right -> ChestA (HammerThrow)

    # KMR_20 Mario's House
    {"from": {"map": "KMR_20", "id": 4}, "to": {"map": "MAC_00", "id": 4}, "reqs": []}, # Mario's House Green Pipe -> Gate District Top Green Pipe

    {"from": {"map": "KMR_20", "id": 4}, "to": {"map": "KMR_20", "id": "GiftA"}, "reqs": [["FAVOR_2_03_active"]]}, #* Mario's House Green Pipe -> GiftA (KootLuigiAutograph)
]
