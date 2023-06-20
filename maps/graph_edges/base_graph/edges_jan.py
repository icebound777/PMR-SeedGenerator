"""This file represents all edges of the world graph that have origin-nodes in the JAN (Jade Jungle) area."""
edges_jan = [
    # JAN_00 Whale Cove
    {"from": {"map": "JAN_00", "id": 0}, "to": {"map": "MAC_06", "id": 1}, "reqs": []}, # Whale Cove Ride The Whale -> Ride Whale (Lavalava Island)
    {"from": {"map": "JAN_00", "id": 1}, "to": {"map": "JAN_01", "id": 0}, "reqs": []}, # Whale Cove Exit Bottom Right -> Beach Exit Left
    {"from": {"map": "JAN_00", "id": 2}, "to": {"map": "JAN_08", "id": 0}, "reqs": []}, # Whale Cove Exit Top Right -> SW Jungle (Super Block) Exit Bottom Left

    {"from": {"map": "JAN_00", "id": 0}, "to": {"map": "JAN_00", "id": 1}, "reqs": []}, #? Whale Cove Ride The Whale -> Whale Cove Exit Bottom Right
    {"from": {"map": "JAN_00", "id": 1}, "to": {"map": "JAN_00", "id": 0}, "reqs": []}, #? Whale Cove Exit Bottom Right -> Whale Cove Ride The Whale
    {"from": {"map": "JAN_00", "id": 0}, "to": {"map": "JAN_00", "id": 2}, "reqs": [["can_climb_steps"]]}, #? Whale Cove Ride The Whale -> Whale Cove Exit Top Right
    {"from": {"map": "JAN_00", "id": 2}, "to": {"map": "JAN_00", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Whale Cove Exit Top Right -> Whale Cove Ride The Whale

    {"from": {"map": "JAN_00", "id": 0},       "to": {"map": "JAN_00", "id": "ItemA"},        "reqs": [["can_climb_steps"]]}, #* Whale Cove Ride The Whale -> ItemA (Coin)
    {"from": {"map": "JAN_00", "id": "ItemA"}, "to": {"map": "JAN_00", "id": "ItemB"},        "reqs": []}, #+ SHARED REQUIREMENTS -> ItemB (Coin)
    {"from": {"map": "JAN_00", "id": 0},       "to": {"map": "JAN_00", "id": "ItemC"},        "reqs": []}, #* Whale Cove Ride The Whale -> ItemC (StopWatch)
    {"from": {"map": "JAN_00", "id": 0},       "to": {"map": "JAN_00", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* Whale Cove Ride The Whale -> Tree1_Drop1A (Coconut)

    # JAN_01 Beach
    {"from": {"map": "JAN_01", "id": 0}, "to": {"map": "JAN_00", "id": 1}, "reqs": []}, # Beach Exit Left -> Whale Cove Exit Bottom Right
    {"from": {"map": "JAN_01", "id": 1}, "to": {"map": "JAN_02", "id": 0}, "reqs": []}, # Beach Exit Right -> Village Cove Exit Top Left

    {"from": {"map": "JAN_01", "id": 0}, "to": {"map": "JAN_01", "id": 1}, "reqs": []}, #? Beach Exit Left -> Beach Exit Right
    {"from": {"map": "JAN_01", "id": 1}, "to": {"map": "JAN_01", "id": 0}, "reqs": []}, #? Beach Exit Right -> Beach Exit Left

    {"from": {"map": "JAN_01", "id": 0},               "to": {"map": "JAN_01", "id": "ItemA"},         "reqs": [["can_climb_steps"]]}, #* Beach Exit Left -> ItemA (Letter11)
    {"from": {"map": "JAN_01", "id": "ItemA"},         "to": {"map": "JAN_01", "id": "ItemB"},         "reqs": []}, #+ SHARED REQUIREMENTS -> ItemB (Coin)
    {"from": {"map": "JAN_01", "id": "ItemA"},         "to": {"map": "JAN_01", "id": "ItemC"},         "reqs": []}, #+ SHARED REQUIREMENTS -> ItemC (Coin)
    {"from": {"map": "JAN_01", "id": 0},               "to": {"map": "JAN_01", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* Beach Exit Left -> HiddenYBlockA (RepelGel)
    {"from": {"map": "JAN_01", "id": "HiddenYBlockA"}, "to": {"map": "JAN_01", "id": "HiddenYBlockB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> HiddenYBlockB (Mystery)
    {"from": {"map": "JAN_01", "id": 0},               "to": {"map": "JAN_01", "id": "Tree2_Drop1"},   "reqs": [["can_shake_trees"]]}, #* Beach Exit Left -> Tree2_Drop1 (Coconut)
    {"from": {"map": "JAN_01", "id": "Tree2_Drop1"},   "to": {"map": "JAN_01", "id": "Tree3_Drop1"},   "reqs": []}, #+ SHARED REQUIREMENTS -> Tree3_Drop1 (Coconut)
    {"from": {"map": "JAN_01", "id": "Tree2_Drop1"},   "to": {"map": "JAN_01", "id": "Tree4_Drop1"},   "reqs": []}, #+ SHARED REQUIREMENTS -> Tree4_Drop1 (Coconut)
    {"from": {"map": "JAN_01", "id": "Tree2_Drop1"},   "to": {"map": "JAN_01", "id": "Tree5_Drop1"},   "reqs": []}, #+ SHARED REQUIREMENTS -> Tree5_Drop1 (Coconut)
    {"from": {"map": "JAN_01", "id": "Tree2_Drop1"},   "to": {"map": "JAN_01", "id": "Tree6_Drop1"},   "reqs": []}, #+ SHARED REQUIREMENTS -> Tree6_Drop1 (Coconut)
    {"from": {"map": "JAN_01", "id": "Tree2_Drop1"},   "to": {"map": "JAN_01", "id": "Tree7_Drop1A"},  "reqs": []}, #+ SHARED REQUIREMENTS -> Tree7_Drop1A (StarPiece)
    {"from": {"map": "JAN_01", "id": "Tree2_Drop1"},   "to": {"map": "JAN_01", "id": "Tree7_Drop1B"},  "reqs": []}, #+ SHARED REQUIREMENTS -> Tree7_Drop1B (Coconut)

    # JAN_02 Village Cove
    {"from": {"map": "JAN_02", "id": 0}, "to": {"map": "JAN_01", "id": 1}, "reqs": []}, # Village Cove Exit Top Left -> Beach Exit Right
    {"from": {"map": "JAN_02", "id": 1}, "to": {"map": "JAN_03", "id": 0}, "reqs": []}, # Village Cove Exit Right -> Village Buildings Exit Left

    {"from": {"map": "JAN_02", "id": 0}, "to": {"map": "JAN_02", "id": 1}, "reqs": []}, #? Village Cove Exit Top Left -> Village Cove Exit Right
    {"from": {"map": "JAN_02", "id": 1}, "to": {"map": "JAN_02", "id": 0}, "reqs": []}, #? Village Cove Exit Right -> Village Cove Exit Top Left

    {"from": {"map": "JAN_02", "id": 0},              "to": {"map": "JAN_02", "id": "HiddenPanel"},  "reqs": [["can_flip_panels"]]}, #* Village Cove Exit Top Left -> HiddenPanel (StarPiece)
    {"from": {"map": "JAN_02", "id": 0},              "to": {"map": "JAN_02", "id": "GiftA"},        "reqs": [["saved_all_yoshikids"]]}, #* Village Cove Exit Top Left -> GiftA (JadeRaven)
    {"from": {"map": "JAN_02", "id": 0},              "to": {"map": "JAN_02", "id": "Tree2_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* Village Cove Exit Top Left -> Tree2_Drop1A (Coconut)
    {"from": {"map": "JAN_02", "id": "Tree2_Drop1A"}, "to": {"map": "JAN_02", "id": "Tree3_Drop1A"}, "reqs": []}, #+ SHARED REQUIREMENTS -> Tree3_Drop1A (Coconut)

    {"from": {"map": "JAN_02", "id": 0}, "to": {"map": "JAN_02", "id": 0}, "reqs": [], "pseudoitems": ["RF_YoshiKidsMissing"]}, #+ Village visited -> Yoshi Kids Missing

    {"from": {"map": "JAN_02", "id": 0}, "to": {"map": "JAN_02", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_JAN_1",
                                                                                                      # "StarPiece_JAN_2",
                                                                                                      # "StarPiece_JAN_3",
                                                                                                      # "StarPiece_JAN_4",
                                                                                                      # "StarPiece_JAN_5",
                                                                                                      # "StarPiece_JAN_6",
                                                                                                      # "StarPiece_JAN_7",
                                                                                                       "StarPiece_JAN_8"]}, #+ Quizmo StarPieces

    # JAN_03 Village Buildings
    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_02", "id": 1}, "reqs": []}, # Village Buildings Exit Left -> Village Cove Exit Right
    {"from": {"map": "JAN_03", "id": 1}, "to": {"map": "JAN_05", "id": 0}, "reqs": []}, # Village Buildings Exit Top Left -> SE Jungle (Quake Hammer) Exit Bottom Right
    {"from": {"map": "JAN_03", "id": 2}, "to": {"map": "JAN_22", "id": 0}, "reqs": []}, # Village Buildings Exit Right -> Path to the Volcano Exit Left
    {"from": {"map": "JAN_03", "id": 3}, "to": {"map": "TIK_08", "id": 4}, "reqs": []}, # Village Buildings Blue Warp Pipe -> Second Level Entry (B2) Blue Warp Pipe

    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_03", "id": 1}, "reqs": []}, #? Village Buildings Exit Left -> Village Buildings Exit Top Left
    {"from": {"map": "JAN_03", "id": 1}, "to": {"map": "JAN_03", "id": 0}, "reqs": []}, #? Village Buildings Exit Top Left -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_03", "id": 2}, "reqs": []}, #? Village Buildings Exit Left -> Village Buildings Exit Right
    {"from": {"map": "JAN_03", "id": 2}, "to": {"map": "JAN_03", "id": 0}, "reqs": []}, #? Village Buildings Exit Right -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_03", "id": 3}, "reqs": [["GF_TIK08_WarpPipe"],["Boots"]]}, #? Village Buildings Exit Left -> Village Buildings Blue Warp Pipe
    {"from": {"map": "JAN_03", "id": 3}, "to": {"map": "JAN_03", "id": 0}, "reqs": []}, #? Village Buildings Blue Warp Pipe -> Village Buildings Exit Left

    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "GiftA"},       "reqs": [["saved_all_yoshikids"],["VolcanoVase"],["MF_Ch5_RescuedStarSpirit"]]}, #* Village Buildings Exit Left -> GiftA (MagicalSeed4)
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "GiftB"},       "reqs": [["saved_all_yoshikids"],["RF_CanVisitTayceT"],["RF_CanCook"],["MF_Ch5_RescuedStarSpirit"]]}, #* Village Buildings Exit Left -> GiftB (Melon)
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "GiftC"},       "reqs": [["RF_SavedYoshiKid_3"],["Parakarry"],["Letter21"]]}, #* Village Buildings Exit Left -> GiftC (Letter22)
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "Tree1_Drop1A"},"reqs": [["can_shake_trees"]]}, #* Village Buildings Exit Left -> Tree1_Drop1A (Coconut)
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "ShopItemA"},   "reqs": [["can_climb_steps"]]}, #* Village Buildings Exit Left -> ShopItemA (SnowmanDoll)
    {"from": {"map": "JAN_03", "id": "ShopItemA"}, "to": {"map": "JAN_03", "id": "ShopItemB"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemB (ThunderRage)
    {"from": {"map": "JAN_03", "id": "ShopItemA"}, "to": {"map": "JAN_03", "id": "ShopItemC"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemC (FireFlower)
    {"from": {"map": "JAN_03", "id": "ShopItemA"}, "to": {"map": "JAN_03", "id": "ShopItemD"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemD (TastyTonic)
    {"from": {"map": "JAN_03", "id": "ShopItemA"}, "to": {"map": "JAN_03", "id": "ShopItemE"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemE (HoneySyrup)
    {"from": {"map": "JAN_03", "id": "ShopItemA"}, "to": {"map": "JAN_03", "id": "ShopItemF"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemF (SuperShroom)

    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_03", "id": 0}, "reqs": [], "pseudoitems": ["RF_YoshiKidsMissing"]}, #+ Village visited -> Yoshi Kids Missing

    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_03", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_JAN_1",
                                                                                                     #  "StarPiece_JAN_2",
                                                                                                     #  "StarPiece_JAN_3",
                                                                                                     #  "StarPiece_JAN_4",
                                                                                                     #  "StarPiece_JAN_5",
                                                                                                     #  "StarPiece_JAN_6",
                                                                                                     #  "StarPiece_JAN_7",
                                                                                                       "StarPiece_JAN_8"]}, #+ Quizmo StarPieces

    # JAN_04 Sushi Tree
    {"from": {"map": "JAN_04", "id": 0}, "to": {"map": "JAN_05", "id": 2}, "reqs": []}, # Sushi Tree Exit Left -> SE Jungle (Quake Hammer) Exit Right

    {"from": {"map": "JAN_04", "id": 0},       "to": {"map": "JAN_04", "id": "ChestA"},       "reqs": [["MF_Ch5_RescuedStarSpirit"]]}, #* Sushi Tree Exit Left -> ChestA (VolcanoVase)
    {"from": {"map": "JAN_04", "id": 0},       "to": {"map": "JAN_04", "id": "ItemA"},        "reqs": [["Sushie"]]}, #* Sushi Tree Exit Left -> ItemA (StarPiece)
    {"from": {"map": "JAN_04", "id": "ItemA"}, "to": {"map": "JAN_04", "id": "Tree2_Drop1A"}, "reqs": [["can_shake_trees"]]}, #+ CHAINED REQUIREMENTS -> Tree2_Drop1A (Letter04)
    {"from": {"map": "JAN_04", "id": 0},       "to": {"map": "JAN_04", "id": "Partner"},      "reqs": [["can_shake_trees"]]}, #* Sushi Tree Exit Left -> Partner (Sushie)

    # JAN_05 SE Jungle (Quake Hammer)
    {"from": {"map": "JAN_05", "id": 0}, "to": {"map": "JAN_03", "id": 1}, "reqs": []}, # SE Jungle (Quake Hammer) Exit Bottom Right -> Village Buildings Exit Top Left
    {"from": {"map": "JAN_05", "id": 1}, "to": {"map": "JAN_08", "id": 1}, "reqs": []}, # SE Jungle (Quake Hammer) Exit Left -> SW Jungle (Super Block) Exit Right
    {"from": {"map": "JAN_05", "id": 2}, "to": {"map": "JAN_04", "id": 0}, "reqs": []}, # SE Jungle (Quake Hammer) Exit Right -> Sushi Tree Exit Left
    {"from": {"map": "JAN_05", "id": 3}, "to": {"map": "JAN_06", "id": 0}, "reqs": []}, # SE Jungle (Quake Hammer) Exit Top -> NE Jungle (Raven Statue) Exit Bottom

    {"from": {"map": "JAN_05", "id": 0}, "to": {"map": "JAN_05", "id": 1}, "reqs": [["Sushie"]]}, #? SE Jungle (Quake Hammer) Exit Bottom Right -> SE Jungle (Quake Hammer) Exit Left
    {"from": {"map": "JAN_05", "id": 1}, "to": {"map": "JAN_05", "id": 0}, "reqs": [["Sushie"]]}, #? SE Jungle (Quake Hammer) Exit Left-> SE Jungle (Quake Hammer) Exit Bottom Right
    {"from": {"map": "JAN_05", "id": 0}, "to": {"map": "JAN_05", "id": 2}, "reqs": []}, #? SE Jungle (Quake Hammer) Exit Bottom Right -> SE Jungle (Quake Hammer) Exit Right
    {"from": {"map": "JAN_05", "id": 2}, "to": {"map": "JAN_05", "id": 0}, "reqs": []}, #? SE Jungle (Quake Hammer) Exit Right-> SE Jungle (Quake Hammer) Exit Bottom Right
    {"from": {"map": "JAN_05", "id": 0}, "to": {"map": "JAN_05", "id": 3}, "reqs": [["GF_JAN05_CreateLogBridge"]]}, #? SE Jungle (Quake Hammer) Exit Bottom Right -> SE Jungle (Quake Hammer) Exit Top
    {"from": {"map": "JAN_05", "id": 3}, "to": {"map": "JAN_05", "id": 0}, "reqs": [["Hammer"]], "pseudoitems": ["GF_JAN05_CreateLogBridge"]}, #? SE Jungle (Quake Hammer) Exit Top-> SE Jungle (Quake Hammer) Exit Bottom Right

    {"from": {"map": "JAN_05", "id": 2}, "to": {"map": "JAN_05", "id": "RBlockA"},     "reqs": [["Sushie"],["can_hit_floating_blocks"]]}, #* SE Jungle (Quake Hammer) Exit Right-> RBlockA (PowerQuake)
    {"from": {"map": "JAN_05", "id": 2}, "to": {"map": "JAN_05", "id": "Bush1_Drop1"}, "reqs": []}, #* SE Jungle (Quake Hammer) Exit Right-> Bush1_Drop1 (Coin)
    {"from": {"map": "JAN_05", "id": 3}, "to": {"map": "JAN_05", "id": "Bush2_Drop1"}, "reqs": []}, #* SE Jungle (Quake Hammer) Exit Top-> Bush2_Drop1 (Coin)
    {"from": {"map": "JAN_05", "id": 2}, "to": {"map": "JAN_05", "id": "Tree2_Drop1"}, "reqs": [["can_shake_trees"]]}, #* SE Jungle (Quake Hammer) Exit Right-> Tree2_Drop1 (Coin)

    {"from": {"map": "JAN_05", "id": 3}, "to": {"map": "JAN_05", "id": 3}, "reqs": [["RF_YoshiKidsMissing"],["Hammer"]], "pseudoitems": ["RF_SavedYoshiKid_1"]}, #+ Save Yoshi Kid

    # JAN_06 NE Jungle (Raven Statue)
    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_05", "id": 3}, "reqs": []}, # NE Jungle (Raven Statue) Exit Bottom -> SE Jungle (Quake Hammer) Exit Top
    {"from": {"map": "JAN_06", "id": 1}, "to": {"map": "JAN_07", "id": 0}, "reqs": []}, # NE Jungle (Raven Statue) Exit Right -> Small Jungle Ledge Exit Left
    {"from": {"map": "JAN_06", "id": 2}, "to": {"map": "JAN_12", "id": 0}, "reqs": []}, # NE Jungle (Raven Statue) Exit Top -> Deep Jungle 1 Exit Bottom Left
    {"from": {"map": "JAN_06", "id": 3}, "to": {"map": "JAN_09", "id": 1}, "reqs": []}, # NE Jungle (Raven Statue) Exit Left -> NW Jungle (Large Ledge) Exit Right

    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_06", "id": 1}, "reqs": [["Sushie"]]}, #? NE Jungle (Raven Statue) Exit Bottom -> NE Jungle (Raven Statue) Exit Right
    {"from": {"map": "JAN_06", "id": 1}, "to": {"map": "JAN_06", "id": 0}, "reqs": [["Sushie"]]}, #? NE Jungle (Raven Statue) Exit Right -> NE Jungle (Raven Statue) Exit Bottom
    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_06", "id": 2}, "reqs": [["JadeRaven"],["Sushie"]]}, #? NE Jungle (Raven Statue) Exit Bottom -> NE Jungle (Raven Statue) Exit Top
    {"from": {"map": "JAN_06", "id": 2}, "to": {"map": "JAN_06", "id": 0}, "reqs": [["Sushie"]]}, #? NE Jungle (Raven Statue) Exit Top -> NE Jungle (Raven Statue) Exit Bottom
    {"from": {"map": "JAN_06", "id": 1}, "to": {"map": "JAN_06", "id": 3}, "reqs": [["GF_JAN06_CreateLogBridge"]]}, #? NE Jungle (Raven Statue) Exit Right -> NE Jungle (Raven Statue) Exit Left
    {"from": {"map": "JAN_06", "id": 3}, "to": {"map": "JAN_06", "id": 1}, "reqs": [["Hammer"]], "pseudoitems": ["GF_JAN06_CreateLogBridge"]}, #? NE Jungle (Raven Statue) Exit Left -> NE Jungle (Raven Statue) Exit Right

    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_06", "id": "ItemA"}, "reqs": [["Sushie"]]}, #* NE Jungle (Raven Statue) Exit Bottom -> ItemA (Coin)
    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_06", "id": "Tree1_Drop1"}, "reqs": [["Sushie"],["can_shake_trees"]]}, #* NE Jungle (Raven Statue) Exit Bottom -> Tree1_Drop1 (Coin)
    {"from": {"map": "JAN_06", "id": 2}, "to": {"map": "JAN_06", "id": "Tree1_Drop1"}, "reqs": [["can_shake_trees"]]}, #* NE Jungle (Raven Statue) Exit Top -> Tree1_Drop1 (Coin)

    # JAN_07 Small Jungle Ledge
    {"from": {"map": "JAN_07", "id": 0}, "to": {"map": "JAN_06", "id": 1}, "reqs": []}, # Small Jungle Ledge Exit Left -> NE Jungle (Raven Statue) Exit Right

    {"from": {"map": "JAN_07", "id": 0}, "to": {"map": "JAN_07", "id": "Tree1_Drop1"}, "reqs": [["can_shake_trees"]]}, #* Small Jungle Ledge Exit Left -> Tree1_Drop1 (Coin)

    {"from": {"map": "JAN_07", "id": 0}, "to": {"map": "JAN_07", "id": 0}, "reqs": [["RF_YoshiKidsMissing"]], "pseudoitems": ["RF_SavedYoshiKid_2"]}, #+ Save Yoshi Kid

    # JAN_08 SW Jungle (Super Block)
    {"from": {"map": "JAN_08", "id": 0}, "to": {"map": "JAN_00", "id": 2}, "reqs": []}, # SW Jungle (Super Block) Exit Bottom Left -> Whale Cove Exit Top Right
    {"from": {"map": "JAN_08", "id": 1}, "to": {"map": "JAN_05", "id": 1}, "reqs": []}, # SW Jungle (Super Block) Exit Right -> SE Jungle (Quake Hammer) Exit Left
    {"from": {"map": "JAN_08", "id": 2}, "to": {"map": "JAN_09", "id": 0}, "reqs": []}, # SW Jungle (Super Block) Exit Top -> NW Jungle (Large Ledge) Exit Bottom

    {"from": {"map": "JAN_08", "id": 0}, "to": {"map": "JAN_08", "id": 1}, "reqs": [["Sushie"]]}, #? SW Jungle (Super Block) Exit Bottom Left -> SW Jungle (Super Block) Exit Right
    {"from": {"map": "JAN_08", "id": 1}, "to": {"map": "JAN_08", "id": 0}, "reqs": [["Sushie"]]}, #? SW Jungle (Super Block) Exit Right -> SW Jungle (Super Block) Exit Bottom Left
    {"from": {"map": "JAN_08", "id": 0}, "to": {"map": "JAN_08", "id": 2}, "reqs": [["Sushie"]]}, #? SW Jungle (Super Block) Exit Bottom Left -> SW Jungle (Super Block) Exit Top
    {"from": {"map": "JAN_08", "id": 2}, "to": {"map": "JAN_08", "id": 0}, "reqs": [["Sushie"]]}, #? SW Jungle (Super Block) Exit Top -> SW Jungle (Super Block) Exit Bottom Left

    {"from": {"map": "JAN_08", "id": 0},       "to": {"map": "JAN_08", "id": "ItemA"},         "reqs": [["Sushie"]]}, #* SW Jungle (Super Block) Exit Bottom Left -> ItemA (Coin)
    {"from": {"map": "JAN_08", "id": "ItemA"}, "to": {"map": "JAN_08", "id": "ItemB"},         "reqs": []}, #+ SHARED REQUIREMENTS -> ItemB (Coin)
    {"from": {"map": "JAN_08", "id": "ItemA"}, "to": {"map": "JAN_08", "id": "ItemC"},         "reqs": []}, #+ SHARED REQUIREMENTS -> ItemC (Coin)
    {"from": {"map": "JAN_08", "id": 2},       "to": {"map": "JAN_08", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* SW Jungle (Super Block) Exit Top -> HiddenYBlockA (ThunderRage)
    {"from": {"map": "JAN_08", "id": 2},       "to": {"map": "JAN_08", "id": "Bush1_Drop1"},   "reqs": []}, #* SW Jungle (Super Block) Exit Top -> Bush1_Drop1 (Coin)
    {"from": {"map": "JAN_08", "id": 0},       "to": {"map": "JAN_08", "id": "Bush2_Drop1"},   "reqs": []}, #* SW Jungle (Super Block) Exit Bottom Left -> Bush2_Drop1 (Coin)
    {"from": {"map": "JAN_08", "id": 2},       "to": {"map": "JAN_08", "id": "Tree2_Drop1"},   "reqs": [["can_shake_trees"]]}, #* SW Jungle (Super Block) Exit Top -> Tree2_Drop1 (Coin)
    {"from": {"map": "JAN_08", "id": 2},       "to": {"map": "JAN_08", "id": "Tree3_Drop1"},   "reqs": [["can_shake_trees"]]}, #* SW Jungle (Super Block) Exit Top -> Tree3_Drop1 (Coin)

    {"from": {"map": "JAN_08", "id": 0}, "to": {"map": "JAN_08", "id": 0}, "reqs": [["RF_YoshiKidsMissing"]], "pseudoitems": ["RF_SavedYoshiKid_3"]}, #+ Save Yoshi Kid

    # JAN_09 NW Jungle (Large Ledge)
    {"from": {"map": "JAN_09", "id": 0}, "to": {"map": "JAN_08", "id": 2}, "reqs": []}, # NW Jungle (Large Ledge) Exit Bottom -> SW Jungle (Super Block) Exit Top
    {"from": {"map": "JAN_09", "id": 1}, "to": {"map": "JAN_06", "id": 3}, "reqs": []}, # NW Jungle (Large Ledge) Exit Right -> NE Jungle (Raven Statue) Exit Left
    {"from": {"map": "JAN_09", "id": 2}, "to": {"map": "JAN_10", "id": 0}, "reqs": []}, # NW Jungle (Large Ledge) Exit Left -> Western Dead End Exit Right
    {"from": {"map": "JAN_09", "id": 3}, "to": {"map": "JAN_11", "id": 0}, "reqs": []}, # NW Jungle (Large Ledge) Pipe On Hill -> Root Cavern Pipe Left

    {"from": {"map": "JAN_09", "id": 0}, "to": {"map": "JAN_09", "id": 1}, "reqs": []}, #? NW Jungle (Large Ledge) Exit Bottom -> NW Jungle (Large Ledge) Exit Right
    {"from": {"map": "JAN_09", "id": 1}, "to": {"map": "JAN_09", "id": 0}, "reqs": []}, #? NW Jungle (Large Ledge) Exit Right -> NW Jungle (Large Ledge) Exit Bottom
    {"from": {"map": "JAN_09", "id": 1}, "to": {"map": "JAN_09", "id": 2}, "reqs": [["Sushie"]]}, #? NW Jungle (Large Ledge) Exit Right -> NW Jungle (Large Ledge) Exit Left
    {"from": {"map": "JAN_09", "id": 2}, "to": {"map": "JAN_09", "id": 1}, "reqs": [["Sushie"]]}, #? NW Jungle (Large Ledge) Exit Left -> NW Jungle (Large Ledge) Exit Right
    {"from": {"map": "JAN_09", "id": 1}, "to": {"map": "JAN_09", "id": 3}, "reqs": [["Sushie"],["Boots"]]}, #? NW Jungle (Large Ledge) Exit Right -> NW Jungle (Large Ledge) Pipe On Hill
    {"from": {"map": "JAN_09", "id": 3}, "to": {"map": "JAN_09", "id": 1}, "reqs": [["Sushie"]]}, #? NW Jungle (Large Ledge) Pipe On Hill -> NW Jungle (Large Ledge) Exit Right

    {"from": {"map": "JAN_09", "id": 0},             "to": {"map": "JAN_09", "id": "Bush1_Drop1"}, "reqs": []}, #* NW Jungle (Large Ledge) Exit Bottom -> Bush1_Drop1 (Coin)
    {"from": {"map": "JAN_09", "id": 0},             "to": {"map": "JAN_09", "id": "Bush6_Drop1"}, "reqs": []}, #* NW Jungle (Large Ledge) Exit Bottom -> Bush6_Drop1 (Coin)
    {"from": {"map": "JAN_09", "id": "Tree3_Drop1"}, "to": {"map": "JAN_09", "id": "Tree2_Drop1"}, "reqs": [["Sushie"],["can_climb_steps"]]}, #+ CHAINED REQUIREMENTS -> Tree2_Drop1 (Coin)
    {"from": {"map": "JAN_09", "id": 3},             "to": {"map": "JAN_09", "id": "Tree2_Drop1"}, "reqs": [["can_shake_trees"]]}, #* NW Jungle (Large Ledge) Pipe On Hill -> Tree2_Drop1 (Coin)
    {"from": {"map": "JAN_09", "id": 1},             "to": {"map": "JAN_09", "id": "Tree3_Drop1"}, "reqs": [["can_shake_trees"]]}, #* NW Jungle (Large Ledge) Exit Right -> Tree3_Drop1 (FrightJar)

    # JAN_10 Western Dead End
    {"from": {"map": "JAN_10", "id": 0}, "to": {"map": "JAN_09", "id": 2}, "reqs": []}, # Western Dead End Exit Right -> NW Jungle (Large Ledge) Exit Left

    {"from": {"map": "JAN_10", "id": 0}, "to": {"map": "JAN_10", "id": "ItemA"}, "reqs": [["Sushie"]]}, #* Western Dead End Exit Right -> ItemA (StarPiece)

    {"from": {"map": "JAN_10", "id": 0}, "to": {"map": "JAN_10", "id": 0}, "reqs": [["RF_YoshiKidsMissing"],["Sushie"],["Hammer"]], "pseudoitems": ["RF_SavedYoshiKid_4"]}, #+ Save Yoshi Kid

    # JAN_11 Root Cavern
    {"from": {"map": "JAN_11", "id": 0}, "to": {"map": "JAN_09", "id": 3}, "reqs": []}, # Root Cavern Pipe Left -> NW Jungle (Large Ledge) Pipe On Hill

    {"from": {"map": "JAN_11", "id": 0}, "to": {"map": "JAN_11", "id": 0}, "reqs": [["RF_YoshiKidsMissing"],["Watt"],["Boots"]], "pseudoitems": ["RF_SavedYoshiKid_5"]}, #+ Save Yoshi Kid

    # JAN_12 Deep Jungle 1
    {"from": {"map": "JAN_12", "id": 0}, "to": {"map": "JAN_06", "id": 2}, "reqs": []}, # Deep Jungle 1 Exit Bottom Left -> NE Jungle (Raven Statue) Exit Top
    {"from": {"map": "JAN_12", "id": 1}, "to": {"map": "JAN_13", "id": 0}, "reqs": []}, # Deep Jungle 1 Exit Top Right -> Deep Jungle 2 (Block Puzzle) Exit Bottom Left

    {"from": {"map": "JAN_12", "id": 0}, "to": {"map": "JAN_12", "id": 1}, "reqs": []}, #? Deep Jungle 1 Exit Bottom Left -> Deep Jungle 1 Exit Top Right
    {"from": {"map": "JAN_12", "id": 1}, "to": {"map": "JAN_12", "id": 0}, "reqs": []}, #? Deep Jungle 1 Exit Top Right -> Deep Jungle 1 Exit Bottom Left

    {"from": {"map": "JAN_12", "id": 0}, "to": {"map": "JAN_12", "id": "Tree1_Drop1"},   "reqs": [["Boots"]]}, #* Deep Jungle 1 Exit Bottom Left -> Tree1_Drop1 (Egg)
    {"from": {"map": "JAN_12", "id": 0}, "to": {"map": "JAN_12", "id": "Tree1_Drop2"},   "reqs": [["can_shake_trees"]]}, #* Deep Jungle 1 Exit Bottom Left -> Tree1_Drop2 (Coin)
    {"from": {"map": "JAN_12", "id": 0}, "to": {"map": "JAN_12", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"],["can_climb_steps"]]}, #* Deep Jungle 1 Exit Bottom Left -> HiddenYBlockA (StoneCap)

    # JAN_13 Deep Jungle 2 (Block Puzzle)
    {"from": {"map": "JAN_13", "id": 0}, "to": {"map": "JAN_12", "id": 1}, "reqs": []}, # Deep Jungle 2 (Block Puzzle) Exit Bottom Left -> Deep Jungle 1 Exit Top Right
    {"from": {"map": "JAN_13", "id": 1}, "to": {"map": "JAN_14", "id": 0}, "reqs": []}, # Deep Jungle 2 (Block Puzzle) Exit Top Right -> Deep Jungle 3 Exit Bottom Left

    {"from": {"map": "JAN_13", "id": 0}, "to": {"map": "JAN_13", "id": 1}, "reqs": []}, #? Deep Jungle 2 (Block Puzzle) Exit Bottom Left -> Deep Jungle 2 (Block Puzzle) Exit Top Right
    {"from": {"map": "JAN_13", "id": 1}, "to": {"map": "JAN_13", "id": 0}, "reqs": []}, #? Deep Jungle 2 (Block Puzzle) Exit Top Right -> Deep Jungle 2 (Block Puzzle) Exit Bottom Left

    {"from": {"map": "JAN_13", "id": 0}, "to": {"map": "JAN_13", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"],["can_climb_steps"]]}, #* Deep Jungle 2 (Block Puzzle) Exit Bottom Left -> HiddenYBlockA (VoltShroom)
    {"from": {"map": "JAN_13", "id": 0}, "to": {"map": "JAN_13", "id": "Tree1_Drop1"},   "reqs": [["can_shake_trees"]]}, #* Deep Jungle 2 (Block Puzzle) Exit Bottom Left -> Tree1_Drop1 (Coin)

    # JAN_14 Deep Jungle 3
    {"from": {"map": "JAN_14", "id": 0}, "to": {"map": "JAN_13", "id": 1}, "reqs": []}, # Deep Jungle 3 Exit Bottom Left -> Deep Jungle 2 (Block Puzzle) Exit Top Right
    {"from": {"map": "JAN_14", "id": 1}, "to": {"map": "JAN_15", "id": 0}, "reqs": []}, # Deep Jungle 3 Exit Top Right -> Deep Jungle 4 (Ambush) Exit Bottom Left

    {"from": {"map": "JAN_14", "id": 0}, "to": {"map": "JAN_14", "id": 1}, "reqs": [["Boots"]]}, #? Deep Jungle 3 Exit Bottom Left -> Deep Jungle 3 Exit Top Right
    {"from": {"map": "JAN_14", "id": 1}, "to": {"map": "JAN_14", "id": 0}, "reqs": []}, #? Deep Jungle 3 Exit Top Right -> Deep Jungle 3 Exit Bottom Left

    {"from": {"map": "JAN_14", "id": 0},             "to": {"map": "JAN_14", "id": "Tree2_Drop1"}, "reqs": [["Boots"]]}, #* Deep Jungle 3 Exit Bottom Left -> Tree2_Drop1 (FireFlower)
    {"from": {"map": "JAN_14", "id": "Tree2_Drop1"}, "to": {"map": "JAN_14", "id": "Tree5_Drop1"}, "reqs": []}, #+ CHAINED REQUIREMENTS -> Tree5_Drop1 (Mushroom)

    # JAN_15 Deep Jungle 4 (Ambush)
    {"from": {"map": "JAN_15", "id": 0}, "to": {"map": "JAN_14", "id": 1}, "reqs": []}, # Deep Jungle 4 (Ambush) Exit Bottom Left -> Deep Jungle 3 Exit Top Right
    {"from": {"map": "JAN_15", "id": 1}, "to": {"map": "JAN_16", "id": 0}, "reqs": []}, # Deep Jungle 4 (Ambush) Exit Right -> Base of Great Tree Exit Left

    {"from": {"map": "JAN_15", "id": 0}, "to": {"map": "JAN_15", "id": 1}, "reqs": []}, #? Deep Jungle 4 (Ambush) Exit Bottom Left -> Deep Jungle 4 (Ambush) Exit Right
    {"from": {"map": "JAN_15", "id": 1}, "to": {"map": "JAN_15", "id": 0}, "reqs": []}, #? Deep Jungle 4 (Ambush) Exit Right -> Deep Jungle 4 (Ambush) Exit Bottom Left

    {"from": {"map": "JAN_15", "id": 0}, "to": {"map": "JAN_15", "id": "Tree2_Drop1"}, "reqs": [["can_shake_trees"]]}, #* Deep Jungle 4 (Ambush) Exit Bottom Left -> Tree2_Drop1 (Coin)
    {"from": {"map": "JAN_15", "id": 0}, "to": {"map": "JAN_15", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Deep Jungle 4 (Ambush) Exit Bottom Left -> HiddenPanel (StarPiece)

    # JAN_16 Base of Great Tree
    {"from": {"map": "JAN_16", "id": 0}, "to": {"map": "JAN_15", "id": 1}, "reqs": []}, # Base of Great Tree Exit Left -> Deep Jungle 4 (Ambush) Exit Right
    {"from": {"map": "JAN_16", "id": 1}, "to": {"map": "JAN_22", "id": 1}, "reqs": []}, # Base of Great Tree Exit Right -> Path to the Volcano Exit Top
    {"from": {"map": "JAN_16", "id": 2}, "to": {"map": "JAN_17", "id": 0}, "reqs": []}, # Base of Great Tree Enter Tree -> Lower Great Tree Interior Exit Bottom
    #{"from": {"map": "JAN_16", "id": 4}, "to": {"map": None, "id": None}, "reqs": []},  # Base of Great Tree Fall Off Of Tree

    {"from": {"map": "JAN_16", "id": 0}, "to": {"map": "JAN_16", "id": 1}, "reqs": [["MF_Ch5_TalkedToRafael"]], "pseudoitems": ["MF_Ch5_RafaelMovedRoot"]}, #? Base of Great Tree Exit Left -> Base of Great Tree Exit Right
    {"from": {"map": "JAN_16", "id": 1}, "to": {"map": "JAN_16", "id": 0}, "reqs": []}, #? Base of Great Tree Exit Right -> Base of Great Tree Exit Left
    {"from": {"map": "JAN_16", "id": 0}, "to": {"map": "JAN_16", "id": 2}, "reqs": []}, #? Base of Great Tree Exit Left -> Base of Great Tree Enter Tree
    {"from": {"map": "JAN_16", "id": 2}, "to": {"map": "JAN_16", "id": 0}, "reqs": []}, #? Base of Great Tree Enter Tree -> Base of Great Tree Exit Left
    {"from": {"map": "JAN_16", "id": 4}, "to": {"map": "JAN_16", "id": 0}, "reqs": []}, #? Base of Great Tree Fall Off Of Tree -> Base of Great Tree Exit Left

    # JAN_17 Lower Great Tree Interior
    {"from": {"map": "JAN_17", "id": 0}, "to": {"map": "JAN_16", "id": 2}, "reqs": []}, # Lower Great Tree Interior Exit Bottom -> Base of Great Tree Enter Tree
    {"from": {"map": "JAN_17", "id": 1}, "to": {"map": "JAN_18", "id": 0}, "reqs": []}, # Lower Great Tree Interior Exit Top -> Great Tree Vine Ascent Exit Bottom

    {"from": {"map": "JAN_17", "id": 0}, "to": {"map": "JAN_17", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Lower Great Tree Interior Exit Bottom -> Lower Great Tree Interior Exit Top
    {"from": {"map": "JAN_17", "id": 1}, "to": {"map": "JAN_17", "id": 0}, "reqs": []}, #? Lower Great Tree Interior Exit Top -> Lower Great Tree Interior Exit Bottom

    # JAN_18 Great Tree Vine Ascent
    {"from": {"map": "JAN_18", "id": 0}, "to": {"map": "JAN_17", "id": 1}, "reqs": []}, # Great Tree Vine Ascent Exit Bottom -> Lower Great Tree Interior Exit Top
    {"from": {"map": "JAN_18", "id": 1}, "to": {"map": "JAN_19", "id": 0}, "reqs": []}, # Great Tree Vine Ascent Exit Top -> Upper Great Tree Interior Exit Bottom

    {"from": {"map": "JAN_18", "id": 0}, "to": {"map": "JAN_18", "id": 1}, "reqs": []}, #? Great Tree Vine Ascent Exit Bottom -> Great Tree Vine Ascent Exit Top
    {"from": {"map": "JAN_18", "id": 1}, "to": {"map": "JAN_18", "id": 0}, "reqs": []}, #? Great Tree Vine Ascent Exit Top -> Great Tree Vine Ascent Exit Bottom

    {"from": {"map": "JAN_18", "id": 0}, "to": {"map": "JAN_18", "id": "ItemA"}, "reqs": []}, #* Great Tree Vine Ascent Exit Bottom -> ItemA (HappyHeartB)

    # JAN_19 Upper Great Tree Interior
    {"from": {"map": "JAN_19", "id": 0}, "to": {"map": "JAN_18", "id": 1}, "reqs": []}, # Upper Great Tree Interior Exit Bottom -> Great Tree Vine Ascent Exit Top
    {"from": {"map": "JAN_19", "id": 1}, "to": {"map": "JAN_23", "id": 0}, "reqs": []}, # Upper Great Tree Interior Exit Top -> Great Treetop Roost Exit Left

    {"from": {"map": "JAN_19", "id": 0}, "to": {"map": "JAN_19", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Upper Great Tree Interior Exit Bottom -> Upper Great Tree Interior Exit Top
    {"from": {"map": "JAN_19", "id": 1}, "to": {"map": "JAN_19", "id": 0}, "reqs": []}, #? Upper Great Tree Interior Exit Top -> Upper Great Tree Interior Exit Bottom

    # JAN_22 Path to the Volcano
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_03", "id": 2}, "reqs": []}, # Path to the Volcano Exit Left -> Village Buildings Exit Right
    {"from": {"map": "JAN_22", "id": 1}, "to": {"map": "JAN_16", "id": 1}, "reqs": []}, # Path to the Volcano Exit Top -> Base of Great Tree Exit Right
    {"from": {"map": "JAN_22", "id": 2}, "to": {"map": "KZN_01", "id": 0}, "reqs": []}, # Path to the Volcano Exit Right -> Volcano Entrance Exit West (Volcano Entrance)

    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 1}, "reqs": [["MF_Ch5_RafaelMovedRoot"]]}, #? Path to the Volcano Exit Left -> Path to the Volcano Exit Top
    {"from": {"map": "JAN_22", "id": 1}, "to": {"map": "JAN_22", "id": 0}, "reqs": []}, #? Path to the Volcano Exit Top -> Path to the Volcano Exit Left
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 2}, "reqs": [["MF_Ch5_ZiplineBuilt"],["can_climb_steps"]]}, #? Path to the Volcano Exit Left -> Path to the Volcano Exit Right
    {"from": {"map": "JAN_22", "id": 2}, "to": {"map": "JAN_22", "id": 0}, "reqs": [["MF_Ch5_ZiplineBuilt"]]}, #? Path to the Volcano Exit Right -> Path to the Volcano Exit Left

    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": "GiftA"}, "reqs": [["MF_Ch5_RafaelMovedRoot"]]}, #* Path to the Volcano Exit Left -> GiftA (UltraStone)
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": "ItemA"}, "reqs": []}, #* Path to the Volcano Exit Left -> ItemA (JamminJelly)

    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 0}, "reqs": [["MF_Ch5_RafaelMovedRoot"]], "pseudoitems": ["MF_Ch5_ZiplineBuilt"]}, #+ Let Raphael build the zipline
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 0}, "reqs": [["MF_Ch5_FoundEscapeRoute"]], "pseudoitems": ["STARSPIRIT_5", "MF_Ch5_RescuedStarSpirit"]}, #+ Get Star Spirit after escaping Volcano

    # JAN_23 Great Treetop Roost
    {"from": {"map": "JAN_23", "id": 0}, "to": {"map": "JAN_19", "id": 1}, "reqs": []}, # Great Treetop Roost Exit Left -> Upper Great Tree Interior Exit Top
    {"from": {"map": "JAN_23", "id": 1}, "to": {"map": "JAN_16", "id": 4}, "reqs": []}, # Great Treetop Roost Jump Off Of Tree -> Base of Great Tree Fall Off Of Tree

    {"from": {"map": "JAN_23", "id": 0}, "to": {"map": "JAN_23", "id": 1}, "reqs": []}, #? Great Treetop Roost Exit Left -> Great Treetop Roost Jump Off Of Tree
    {"from": {"map": "JAN_23", "id": 1}, "to": {"map": "JAN_23", "id": 0}, "reqs": []}, #? Great Treetop Roost Jump Off Of Tree -> Great Treetop Roost Exit Left

    {"from": {"map": "JAN_23", "id": 0}, "to": {"map": "JAN_23", "id": 0}, "reqs": [], "pseudoitems": ["MF_Ch5_TalkedToRafael"]}, #+ Talk to Raphael
]
