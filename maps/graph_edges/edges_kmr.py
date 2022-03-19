from rando_modules.simulate import *

"""This file represents all edges of the world graph that have origin-nodes in the KMR (Goomba Region) area."""
edges_kmr  = [
    # KMR_00 Forest Clearing
    {"from": {"map": "KMR_00", "id": 0},             "to": {"map": "KMR_02", "id": 1},             "reqs": []}, # Forest Clearing Exit East -> Goomba Village Exit Left

    {"from": {"map": "KMR_00", "id": 0},             "to": {"map": "KMR_00", "id": "HiddenPanel"}, "reqs": [can_flip_panels]}, #* Forest Clearing Exit East -> HiddenPanel
    {"from": {"map": "KMR_00", "id": "HiddenPanel"}, "to": {"map": "KMR_00", "id": 0},             "reqs": []}, #* HiddenPanel -> Forest Clearing Exit East

    # KMR_02 Goomba Village
    {"from": {"map": "KMR_02", "id": 0             },  "to": {"map": "KMR_09", "id": 0             },  "reqs": []}, # Goomba Village Exit Right -> Goomba Road 1 Exit Left
    {"from": {"map": "KMR_02", "id": 1             },  "to": {"map": "KMR_00", "id": 0             },  "reqs": []}, # Goomba Village Exit Left -> Forest Clearing Exit East
    {"from": {"map": "KMR_02", "id": 2             },  "to": {"map": "KMR_05", "id": 1             },  "reqs": []}, # Goomba Village Exit Top Left -> Behind the Village Exit Right
    {"from": {"map": "KMR_02", "id": 3             },  "to": {"map": "TIK_01", "id": 2             },  "reqs": []}, # Goomba Village Blue Warp Pipe -> Warp Zone 1 (B1) Blue Pipe (Right)

    {"from": {"map": "KMR_02", "id": 1             },  "to": {"map": "KMR_02", "id": 0             },  "reqs": [require(hammer=0)]}, #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 0             },  "to": {"map": "KMR_02", "id": 1             },  "reqs": [require(hammer=0)]}, #? Goomba Village Exit Right -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 1             },  "to": {"map": "KMR_02", "id": 2             },  "reqs": []}, #? Goomba Village Exit Left -> Goomba Village Exit Top Left
    {"from": {"map": "KMR_02", "id": 2             },  "to": {"map": "KMR_02", "id": 1             },  "reqs": []}, #? Goomba Village Exit Top Left -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 1             },  "to": {"map": "KMR_02", "id": 3             },  "reqs": [require(flag="GF_TIK01_WarpPipes")]}, #? Goomba Village Exit Left -> Goomba Village Blue Warp Pipe
    {"from": {"map": "KMR_02", "id": 3             },  "to": {"map": "KMR_02", "id": 1             },  "reqs": []}, #? Goomba Village Blue Warp Pipe -> Goomba Village Exit Left

    {"from": {"map": "KMR_02", "id": 1             },  "to": {"map": "KMR_02", "id": "ItemA"       },  "reqs": []}, #* Goomba Village Exit Left -> ItemA (ShootingStar)
    {"from": {"map": "KMR_02", "id": "ItemA"       },  "to": {"map": "KMR_02", "id": 1             },  "reqs": []}, #* ItemA (ShootingStar) -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 1             },  "to": {"map": "KMR_02", "id": "GiftA"       },  "reqs": [require(favor="FAVOR_2_01_active")]}, #* Goomba Village Exit Left -> GiftA (KootTheTape)
    {"from": {"map": "KMR_02", "id": "GiftA"       },  "to": {"map": "KMR_02", "id": 1             },  "reqs": []}, #* GiftA (KootTheTape) -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 1             },  "to": {"map": "KMR_02", "id": "GiftB"       },  "reqs": []}, #* Goomba Village Exit Left -> GiftA (PowerJump)
    {"from": {"map": "KMR_02", "id": "GiftB"       },  "to": {"map": "KMR_02", "id": 1             },  "reqs": []}, #* GiftA (PowerJump) -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 1             },  "to": {"map": "KMR_02", "id": "Tree1_Drop1A"},  "reqs": [can_shake_trees]}, #* Goomba Village Exit Left -> Tree1_Drop1A (Goomnut)
    {"from": {"map": "KMR_02", "id": "Tree1_Drop1A"},  "to": {"map": "KMR_02", "id": 1             },  "reqs": []}, #* Tree1_Drop1A (Goomnut) -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 1             },  "to": {"map": "KMR_02", "id": "Partner"     },  "reqs": []}, #* Goomba Village Exit Left -> Partner (Goombario)
    {"from": {"map": "KMR_02", "id": "Partner"     },  "to": {"map": "KMR_02", "id": 1             },  "reqs": []}, #* Partner (Goombario) -> Goomba Village Exit Left

    {"from": {"map": "KMR_02", "id": 1},               "to": {"map": "KMR_02", "id": 1}, "reqs": [], "pseudoitems": ["StarPiece_KMR_1",
                                                                                                                     "StarPiece_KMR_2",
                                                                                                                     "StarPiece_KMR_3",
                                                                                                                     "StarPiece_KMR_4",
                                                                                                                     "StarPiece_KMR_5",
                                                                                                                     "StarPiece_KMR_6",
                                                                                                                     "StarPiece_KMR_7",
                                                                                                                     "StarPiece_KMR_8"]}, #+ Quizmo StarPieces

    # KMR_05 Behind the Village
    {"from": {"map": "KMR_05", "id": 0},               "to": {"map": "KMR_03", "id": 1},               "reqs": []}, # Behind the Village Exit Left -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_05", "id": 1},               "to": {"map": "KMR_02", "id": 2},               "reqs": []}, # Behind the Village Exit Right -> Goomba Village Exit Top Left

    {"from": {"map": "KMR_05", "id": 0},               "to": {"map": "KMR_05", "id": 1},               "reqs": []}, #? Behind the Village Exit Left -> Behind the Village Exit Right
    {"from": {"map": "KMR_05", "id": 1},               "to": {"map": "KMR_05", "id": 0},               "reqs": []}, #? Behind the Village Exit Right -> Behind the Village Exit Left
    
    {"from": {"map": "KMR_05", "id": 1      },         "to": {"map": "KMR_05", "id": "ItemA"},         "reqs": []}, #* Behind the Village Exit Right -> ItemA (StarPiece)
    {"from": {"map": "KMR_05", "id": "ItemA"},         "to": {"map": "KMR_05", "id": 1      },         "reqs": []}, #* ItemA (StarPiece) -> Behind the Village Exit Right
    {"from": {"map": "KMR_05", "id": 1      },         "to": {"map": "KMR_05", "id": "Tree1_Drop1A"},  "reqs": [can_shake_trees]}, #* Behind the Village Exit Right -> Tree1_Drop1A (Coin)
    {"from": {"map": "KMR_05", "id": "Tree1_Drop1A"},  "to": {"map": "KMR_05", "id": 1      },         "reqs": []}, #* Tree1_Drop1A (Coin) -> Behind the Village Exit Right

    # KMR_03 Bottom of the Cliff
    {"from": {"map": "KMR_03", "id": 0}, "to": {"map": "KMR_04", "id": 0}, "reqs": []}, # Bottom of the Cliff Exit Left -> Jr. Troopa's Playground Exit Right
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_05", "id": 0}, "reqs": []}, # Bottom of the Cliff Exit Right -> Behind the Village Exit Left
    
    {"from": {"map": "KMR_03", "id": 0}, "to": {"map": "KMR_03", "id": 1}, "reqs": []}, #? Bottom of the Cliff Exit Left -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_03", "id": 0}, "reqs": []}, #? Bottom of the Cliff Exit Right -> Bottom of the Cliff Exit Left
    
    {"from": {"map": "KMR_03", "id": 0},               "to": {"map": "KMR_03", "id": "YBlockA"},       "reqs": [require(hammer=0)]}, #* Bottom of the Cliff Exit Left -> YBlockA (Coin)
    {"from": {"map": "KMR_03", "id": "YBlockA"},       "to": {"map": "KMR_03", "id": 0},               "reqs": []}, #* YBlockA (Coin) -> Bottom of the Cliff Exit Left
    {"from": {"map": "KMR_03", "id": 0},               "to": {"map": "KMR_03", "id": "Tree1_Drop1A"},  "reqs": [can_shake_trees]}, #* Bottom of the Cliff Exit Left -> Tree1_Drop1A (Mushroom)
    {"from": {"map": "KMR_03", "id": "Tree1_Drop1A"},  "to": {"map": "KMR_03", "id": 0},               "reqs": []}, #* Tree1_Drop1A (Mushroom) -> Bottom of the Cliff Exit Left
    {"from": {"map": "KMR_03", "id": 1},               "to": {"map": "KMR_03", "id": "HiddenPanel"},   "reqs": [can_flip_panels]}, #* Bottom of the Cliff Exit Right -> HiddenPanel (StarPiece)
    {"from": {"map": "KMR_03", "id": "HiddenPanel"},   "to": {"map": "KMR_03", "id": 1},               "reqs": []}, #* HiddenPanel (StarPiece) -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 1},               "to": {"map": "KMR_03", "id": "HiddenYBlockA"}, "reqs": [require(hammer=1), require(partner="Watt",flag="RF_HiddenBlocksVisible")]}, #* Bottom of the Cliff Exit Right -> HiddenYBlockA (RepelGel)
    {"from": {"map": "KMR_03", "id": "HiddenYBlockA"}, "to": {"map": "KMR_03", "id": 1},               "reqs": []}, #* HiddenYBlockA (RepelGel) -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 1},               "to": {"map": "KMR_03", "id": "ItemA"},         "reqs": []}, #* Bottom of the Cliff Exit Right -> ItemA (Coin)
    {"from": {"map": "KMR_03", "id": "ItemA"},         "to": {"map": "KMR_03", "id": 1},               "reqs": []}, #* ItemA (Coin) -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 1},               "to": {"map": "KMR_03", "id": "ItemB"},         "reqs": []}, #* Bottom of the Cliff Exit Right -> ItemB (Coin)
    {"from": {"map": "KMR_03", "id": "ItemB"},         "to": {"map": "KMR_03", "id": 1},               "reqs": []}, #* ItemB (Coin) -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 1},               "to": {"map": "KMR_03", "id": "ItemC"},         "reqs": []}, #* Bottom of the Cliff Exit Right -> ItemC (Coin)
    {"from": {"map": "KMR_03", "id": "ItemC"},         "to": {"map": "KMR_03", "id": 1},               "reqs": []}, #* ItemC (Coin) -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 1},               "to": {"map": "KMR_03", "id": "ItemD"},         "reqs": []}, #* Bottom of the Cliff Exit Right -> ItemD (Coin)
    {"from": {"map": "KMR_03", "id": "ItemD"},         "to": {"map": "KMR_03", "id": 1},               "reqs": []}, #* ItemD (Coin) -> Bottom of the Cliff Exit Right
    {"from": {"map": "KMR_03", "id": 1},               "to": {"map": "KMR_03", "id": "ItemE"},         "reqs": []}, #* Bottom of the Cliff Exit Right -> ItemE (FireFlower)
    {"from": {"map": "KMR_03", "id": "ItemE"},         "to": {"map": "KMR_03", "id": 1},               "reqs": []}, #* ItemE (FireFlower) -> Bottom of the Cliff Exit Right

    # KMR_04 Jr. Troopa's Playground
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_03", "id": 0}, "reqs": []}, # Jr. Troopa's Playground Exit Right -> Bottom of the Cliff Exit Left

    {"from": {"map": "KMR_04", "id": 0},              "to": {"map": "KMR_04", "id": "Tree3_Drop1A"}, "reqs": [can_shake_trees]}, #* Jr. Troopa's Playground Exit Right -> Tree3_Drop1A (Dolly)
    {"from": {"map": "KMR_04", "id": "Tree3_Drop1A"}, "to": {"map": "KMR_04", "id": 0},              "reqs": []}, #* Tree3_Drop1A (Dolly) -> Jr. Troopa's Playground Exit Right

    # KMR_09 Goomba Road 1
    {"from": {"map": "KMR_09", "id": 0}, "to": {"map": "KMR_02", "id": 0}, "reqs": []}, # Goomba Road 1 Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_09", "id": 1}, "to": {"map": "KMR_06", "id": 0}, "reqs": []}, # Goomba Road 1 Exit Right -> Goomba Road 2 Exit Left
    
    {"from": {"map": "KMR_09", "id": 0}, "to": {"map": "KMR_09", "id": 1}, "reqs": []}, #? Goomba Road 1 Exit Left -> Goomba Road 1 Exit Right
    {"from": {"map": "KMR_09", "id": 1}, "to": {"map": "KMR_09", "id": 0}, "reqs": []}, #? Goomba Road 1 Exit Right -> Goomba Road 1 Exit Left
    
    {"from": {"map": "KMR_09", "id": 1},         "to": {"map": "KMR_09", "id": "YBlockA"}, "reqs": []}, #* Goomba Road 1 Exit Right -> YBlockA (Coin)
    {"from": {"map": "KMR_09", "id": "YBlockA"}, "to": {"map": "KMR_09", "id": 1},         "reqs": []}, #* YBlockA (Coin) -> Goomba Road 1 Exit Right
    {"from": {"map": "KMR_09", "id": 1},         "to": {"map": "KMR_09", "id": "YBlockB"}, "reqs": []}, #* Goomba Road 1 Exit Right -> YBlockB (Coin)
    {"from": {"map": "KMR_09", "id": "YBlockB"}, "to": {"map": "KMR_09", "id": 1},         "reqs": []}, #* YBlockB (Coin) -> Goomba Road 1 Exit Right

    # KMR_06 Goomba Road 2
    {"from": {"map": "KMR_06", "id": 0}, "to": {"map": "KMR_09", "id": 1}, "reqs": []}, # Goomba Road 2 Exit Left -> Goomba Road 1 Exit Right
    {"from": {"map": "KMR_06", "id": 1}, "to": {"map": "KMR_07", "id": 0}, "reqs": []}, # Goomba Road 2 Exit Right -> Goomba Road 3 Exit Left
    
    {"from": {"map": "KMR_06", "id": 0}, "to": {"map": "KMR_06", "id": 1}, "reqs": []}, #? Goomba Road 2 Exit Left -> Goomba Road 2 Exit Right
    {"from": {"map": "KMR_06", "id": 1}, "to": {"map": "KMR_06", "id": 0}, "reqs": []}, #? Goomba Road 2 Exit Right -> Goomba Road 2 Exit Left
    
    {"from": {"map": "KMR_06", "id": 0},         "to": {"map": "KMR_06", "id": "ItemA"},   "reqs": []}, #* Goomba Road 2 Exit Left -> ItemA (Mushroom)
    {"from": {"map": "KMR_06", "id": "ItemA"},   "to": {"map": "KMR_06", "id": 0},         "reqs": []}, #* ItemA (Mushroom) -> Goomba Road 2 Exit Left
    {"from": {"map": "KMR_06", "id": 0},         "to": {"map": "KMR_06", "id": "RBlockA"}, "reqs": []}, #* Goomba Road 2 Exit Left -> RBlockA (CloseCall)
    {"from": {"map": "KMR_06", "id": "RBlockA"}, "to": {"map": "KMR_06", "id": 0},         "reqs": []}, #* RBlockA (CloseCall) -> Goomba Road 2 Exit Left

    # KMR_07 Goomba Road 3
    {"from": {"map": "KMR_07", "id": 0}, "to": {"map": "KMR_06", "id": 1}, "reqs": []}, # Goomba Road 3 Exit Left -> Goomba Road 2 Exit Right
    {"from": {"map": "KMR_07", "id": 1}, "to": {"map": "KMR_12", "id": 0}, "reqs": []}, # Goomba Road 3 Exit Right -> Goomba Road 4 Exit Left
    
    {"from": {"map": "KMR_07", "id": 0}, "to": {"map": "KMR_07", "id": 1}, "reqs": []}, #? Goomba Road 3 Exit Left -> Goomba Road 3 Exit Right
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
    
    {"from": {"map": "KMR_11", "id": 0}, "to": {"map": "KMR_11", "id": 1}, "reqs": [require(flag="RF_BeatGoombaBros")], "pseudoitems": ["RF_BeatGoombaKing"]}, #? Goomba King's Castle Exit Left -> Goomba King's Castle Exit Right
    {"from": {"map": "KMR_11", "id": 1}, "to": {"map": "KMR_11", "id": 0}, "reqs": [require(flag="RF_BeatGoombaKing")]}, #? Goomba King's Castle Exit Right -> Goomba King's Castle Exit Left
    
    {"from": {"map": "KMR_11", "id": 0},              "to": {"map": "KMR_11", "id": "Tree1_Drop1A"}, "reqs": [can_shake_trees]}, #* Goomba King's Castle Exit Left -> Tree1_Drop1A (StarPiece)
    {"from": {"map": "KMR_11", "id": "Tree1_Drop1A"}, "to": {"map": "KMR_11", "id": 0},              "reqs": []}, #* Tree1_Drop1A (StarPiece) -> Goomba King's Castle Exit Left
    {"from": {"map": "KMR_11", "id": 1},              "to": {"map": "KMR_11", "id": "HiddenPanel"},  "reqs": [can_flip_panels]}, #* Goomba King's Castle Exit Right -> HiddenPanel (StarPiece)
    {"from": {"map": "KMR_11", "id": "HiddenPanel"},  "to": {"map": "KMR_11", "id": 1},              "reqs": []}, #* HiddenPanel (StarPiece) -> Goomba King's Castle Exit Right
    {"from": {"map": "KMR_11", "id": 1},              "to": {"map": "KMR_11", "id": "YBlockA"},      "reqs": [require(hammer=0)]}, #* Goomba King's Castle Exit Right -> YBlockA (SuperShroom)
    {"from": {"map": "KMR_11", "id": "YBlockA"},      "to": {"map": "KMR_11", "id": 1},              "reqs": []}, #* YBlockA (SuperShroom) -> Goomba King's Castle Exit Right

    # KMR_10 Toad Town Entrance
    {"from": {"map": "KMR_10", "id": 0}, "to": {"map": "KMR_11", "id": 1}, "reqs": []}, # Toad Town Entrance Exit Left -> Goomba King's Castle Exit Right
    {"from": {"map": "KMR_10", "id": 1}, "to": {"map": "MAC_00", "id": 0}, "reqs": []}, # Toad Town Entrance Exit Right -> Gate District Exit Left
    
    {"from": {"map": "KMR_10", "id": 0}, "to": {"map": "KMR_10", "id": 1}, "reqs": []}, #? Toad Town Entrance Exit Left -> Toad Town Entrance Exit Right
    {"from": {"map": "KMR_10", "id": 1}, "to": {"map": "KMR_10", "id": 0}, "reqs": []}, #? Toad Town Entrance Exit Right -> Toad Town Entrance Exit Left
    
    {"from": {"map": "KMR_10", "id": 1},         "to": {"map": "KMR_10", "id": "YBlockA"}, "reqs": []}, #* Toad Town Entrance Exit Right -> YBlockA (SleepySheep)
    {"from": {"map": "KMR_10", "id": "YBlockA"}, "to": {"map": "KMR_10", "id": 1},         "reqs": []}, #* YBlockA (SleepySheep) -> Toad Town Entrance Exit Right
    {"from": {"map": "KMR_10", "id": 1},         "to": {"map": "KMR_10", "id": "ChestA"},  "reqs": [can_shake_trees]}, #* Toad Town Entrance Exit Right -> ChestA (HammerThrow)
    {"from": {"map": "KMR_10", "id": "ChestA"},  "to": {"map": "KMR_10", "id": 1},         "reqs": []}, #* ChestA (HammerThrow) -> Toad Town Entrance Exit Right

    # KMR_20 Mario's House
    {"from": {"map": "KMR_20", "id": 4}, "to": {"map": "MAC_00", "id": 4}, "reqs": []}, # Mario's House Green Pipe -> Gate District Top Green Pipe

    {"from": {"map": "KMR_20", "id": 4},       "to": {"map": "KMR_20", "id": "GiftA"}, "reqs": [require(favor="FAVOR_2_03_active")]}, #* Mario's House Green Pipe -> GiftA (KootLuigiAutograph)
    {"from": {"map": "KMR_20", "id": "GiftA"}, "to": {"map": "KMR_20", "id": 4},       "reqs": []}, #* GiftA (KootLuigiAutograph) -> Mario's House Green Pipe
]