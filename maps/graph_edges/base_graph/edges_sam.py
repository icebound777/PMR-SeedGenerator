"""This file represents all edges of the world graph that have origin-nodes in the SAM (Shiver Mountain) area."""
edges_sam = [
    # SAM_01 Shiver City Mayor Area
    {"from": {"map": "SAM_01", "id": 0}, "to": {"map": "SAM_02", "id": 0}, "reqs": []}, # Shiver City Mayor Area Exit East -> Shiver City Center Exit West

    {"from": {"map": "SAM_01", "id": 0}, "to": {"map": "SAM_01", "id": 0}, "reqs": [], "pseudoitems": ["RF_Ch7_MurderMysteryStarted"]}, #+ Shiver City Mayor Area Exit East
    {"from": {"map": "SAM_01", "id": 0}, "to": {"map": "SAM_01", "id": 0}, "reqs": [["RF_Ch7_SpokeWithHerringway"]], "pseudoitems": ["RF_Ch7_MurderMysterySolved"]}, #+ Shiver City Mayor Area Exit East

    {"from": {"map": "SAM_01", "id": 0}, "to": {"map": "SAM_01", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"],["RF_Ch7_MurderMysterySolved"]]}, #* Shiver City Mayor Area Exit East -> HiddenPanel (StarPiece)
    {"from": {"map": "SAM_01", "id": 0}, "to": {"map": "SAM_01", "id": "GiftA"},       "reqs": [["RF_Ch7_MurderMysterySolved"],["RF_Ch7_GotSnowmanScarf"]]}, #* Shiver City Mayor Area Exit East -> GiftA (SnowmanBucket)
    {"from": {"map": "SAM_01", "id": 0}, "to": {"map": "SAM_01", "id": "GiftB"},       "reqs": [["Parakarry"],["Letter05"]]}, #* Shiver City Mayor Area Exit East -> GiftB (StarPiece)
    {"from": {"map": "SAM_01", "id": 0}, "to": {"map": "SAM_01", "id": "ChestA"},      "reqs": [["Boots"]]}, #* Shiver City Mayor Area Exit East -> ChestA (AttackFXE)

    {"from": {"map": "SAM_01", "id": 0}, "to": {"map": "SAM_01", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_SAM_1",
                                                                                                     #  "StarPiece_SAM_2",
                                                                                                     #  "StarPiece_SAM_3",
                                                                                                     #  "StarPiece_SAM_4",
                                                                                                     #  "StarPiece_SAM_5",
                                                                                                     #  "StarPiece_SAM_6",
                                                                                                     #  "StarPiece_SAM_7",
                                                                                                       "StarPiece_SAM_8"]}, #+ Quizmo StarPieces

    # SAM_02 Shiver City Center
    {"from": {"map": "SAM_02", "id": 0}, "to": {"map": "SAM_01", "id": 0}, "reqs": []}, # Shiver City Center Exit West -> Shiver City Mayor Area Exit East
    {"from": {"map": "SAM_02", "id": 1}, "to": {"map": "SAM_11", "id": 0}, "reqs": []}, # Shiver City Center Exit East -> Shiver City Pond Area Exit West
    {"from": {"map": "SAM_02", "id": 2}, "to": {"map": "TIK_17", "id": 1}, "reqs": []}, # Shiver City Center Pipe Entrance -> Frozen Room (B3) Green Pipe Right

    {"from": {"map": "SAM_02", "id": 0}, "to": {"map": "SAM_02", "id": 1}, "reqs": []}, #? Shiver City Center Exit West -> Shiver City Center Exit East
    {"from": {"map": "SAM_02", "id": 1}, "to": {"map": "SAM_02", "id": 0}, "reqs": []}, #? Shiver City Center Exit East -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0}, "to": {"map": "SAM_02", "id": 2}, "reqs": [["can_climb_steps"]]}, #? Shiver City Center Exit West -> Shiver City Center Pipe Entrance
    {"from": {"map": "SAM_02", "id": 2}, "to": {"map": "SAM_02", "id": 0}, "reqs": []}, #? Shiver City Center Pipe Entrance -> Shiver City Center Exit West

    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ItemA"},     "reqs": []}, #* Shiver City Center Exit West -> ItemA (IcedPotato)
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ItemB"},     "reqs": [["MF_SAM_04_UnlockedShiverMountain"]]}, #* Shiver City Center Exit West -> ItemB (UltraShroom)
    {"from": {"map": "SAM_02", "id": "ItemB"},     "to": {"map": "SAM_02", "id": "ItemC"},     "reqs": []}, #+ SHARED REQUIREMENTS -> ItemC (Mushroom)
    {"from": {"map": "SAM_02", "id": "ItemB"},     "to": {"map": "SAM_02", "id": "ItemD"},     "reqs": []}, #+ SHARED REQUIREMENTS -> ItemD (Mushroom)
    {"from": {"map": "SAM_02", "id": "ItemB"},     "to": {"map": "SAM_02", "id": "ItemE"},     "reqs": []}, #+ SHARED REQUIREMENTS -> ItemE (Mushroom)
    {"from": {"map": "SAM_02", "id": "ItemB"},     "to": {"map": "SAM_02", "id": "ItemF"},     "reqs": []}, #+ SHARED REQUIREMENTS -> ItemF (Mushroom)
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ShopItemA"}, "reqs": [["RF_Ch7_MurderMysterySolved"]]}, #* Shiver City Center Exit West -> ShopItemA (DizzyDial)
    {"from": {"map": "SAM_02", "id": "ShopItemA"}, "to": {"map": "SAM_02", "id": "ShopItemB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemB (ShootingStar)
    {"from": {"map": "SAM_02", "id": "ShopItemA"}, "to": {"map": "SAM_02", "id": "ShopItemC"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemC (SnowmanDoll)
    {"from": {"map": "SAM_02", "id": "ShopItemA"}, "to": {"map": "SAM_02", "id": "ShopItemD"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemD (MapleSyrup)
    {"from": {"map": "SAM_02", "id": "ShopItemA"}, "to": {"map": "SAM_02", "id": "ShopItemE"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemE (LifeShroom)
    {"from": {"map": "SAM_02", "id": "ShopItemA"}, "to": {"map": "SAM_02", "id": "ShopItemF"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemF (SuperShroom)

    {"from": {"map": "SAM_02", "id": 0}, "to": {"map": "SAM_02", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_SAM_1",
                                                                                                     #  "StarPiece_SAM_2",
                                                                                                     #  "StarPiece_SAM_3",
                                                                                                     #  "StarPiece_SAM_4",
                                                                                                     #  "StarPiece_SAM_5",
                                                                                                     #  "StarPiece_SAM_6",
                                                                                                     #  "StarPiece_SAM_7",
                                                                                                       "StarPiece_SAM_8"]}, #+ Quizmo StarPieces

    # SAM_03 Road to Shiver Snowfield
    {"from": {"map": "SAM_03", "id": 0}, "to": {"map": "SAM_11", "id": 1}, "reqs": []}, # Road to Shiver Snowfield Exit West -> Shiver City Pond Area Exit East
    {"from": {"map": "SAM_03", "id": 1}, "to": {"map": "SAM_04", "id": 0}, "reqs": []}, # Road to Shiver Snowfield Exit East -> Shiver Snowfield Exit West

    {"from": {"map": "SAM_03", "id": 0}, "to": {"map": "SAM_03", "id": 1}, "reqs": []}, #? Road to Shiver Snowfield Exit West -> Road to Shiver Snowfield Exit East
    {"from": {"map": "SAM_03", "id": 1}, "to": {"map": "SAM_03", "id": 0}, "reqs": []}, #? Road to Shiver Snowfield Exit East -> Road to Shiver Snowfield Exit West

    # SAM_04 Shiver Snowfield
    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_03", "id": 1}, "reqs": []}, # Shiver Snowfield Exit West -> Road to Shiver Snowfield Exit East
    {"from": {"map": "SAM_04", "id": 1}, "to": {"map": "SAM_05", "id": 0}, "reqs": []}, # Shiver Snowfield Exit East -> Path to Starborn Valley Exit West
    {"from": {"map": "SAM_04", "id": 2}, "to": {"map": "SAM_07", "id": 0}, "reqs": []}, # Shiver Snowfield Mountain Entrance -> Shiver Mountain Passage Mountain Entrance

    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_04", "id": 1}, "reqs": []}, #? Shiver Snowfield Exit West -> Shiver Snowfield Exit East
    {"from": {"map": "SAM_04", "id": 1}, "to": {"map": "SAM_04", "id": 0}, "reqs": []}, #? Shiver Snowfield Exit East -> Shiver Snowfield Exit West
    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_04", "id": 2}, "reqs": [["SnowmanBucket"],["SnowmanScarf"]], "pseudoitems": ["MF_SAM_04_UnlockedShiverMountain"]}, #? Shiver Snowfield Exit West -> Shiver Snowfield Mountain Entrance
    {"from": {"map": "SAM_04", "id": 2}, "to": {"map": "SAM_04", "id": 0}, "reqs": []}, #? Shiver Snowfield Mountain Entrance -> Shiver Snowfield Exit West

    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_04", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Shiver Snowfield Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_04", "id": "Tree2_Drop1"}, "reqs": [["Hammer"]]}, #* Shiver Snowfield Exit West -> Tree2_Drop1 (Letter05)
    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_04", "id": "ItemA"},       "reqs": []}, #* Shiver Snowfield Exit West -> ItemA (RepelGel)

    # SAM_05 Path to Starborn Valley
    {"from": {"map": "SAM_05", "id": 0}, "to": {"map": "SAM_04", "id": 1}, "reqs": []}, # Path to Starborn Valley Exit West -> Shiver Snowfield Exit East
    {"from": {"map": "SAM_05", "id": 1}, "to": {"map": "SAM_06", "id": 0}, "reqs": []}, # Path to Starborn Valley Exit East -> Starborn Valley Town Entrance

    {"from": {"map": "SAM_05", "id": 0}, "to": {"map": "SAM_05", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Path to Starborn Valley Exit West -> Path to Starborn Valley Exit East
    {"from": {"map": "SAM_05", "id": 1}, "to": {"map": "SAM_05", "id": 0}, "reqs": []}, #? Path to Starborn Valley Exit East -> Path to Starborn Valley Exit West

    {"from": {"map": "SAM_05", "id": 0}, "to": {"map": "SAM_05", "id": "ItemA"},         "reqs": []}, #* Path to Starborn Valley Exit West -> ItemA (Letter06)
    {"from": {"map": "SAM_05", "id": 1}, "to": {"map": "SAM_05", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* Path to Starborn Valley Exit West -> HiddenYBlockA (StopWatch)

    # SAM_06 Starborn Valley
    {"from": {"map": "SAM_06", "id": 0}, "to": {"map": "SAM_05", "id": 1}, "reqs": []}, # Starborn Valley Town Entrance -> Path to Starborn Valley Exit East

    {"from": {"map": "SAM_06", "id": 0}, "to": {"map": "SAM_06", "id": "GiftA"}, "reqs": [["can_climb_steps"]], "pseudoitems": ["RF_Ch7_GotSnowmanScarf"]}, #* Starborn Valley Town Entrance -> GiftA (SnowmanScarf)
    {"from": {"map": "SAM_06", "id": 0}, "to": {"map": "SAM_06", "id": "GiftB"}, "reqs": [["Parakarry"],["Letter23"]]}, #* Starborn Valley Town Entrance -> GiftB (Letter24)

    # SAM_07 Shiver Mountain Passage
    {"from": {"map": "SAM_07", "id": 0}, "to": {"map": "SAM_04", "id": 2}, "reqs": []}, # Shiver Mountain Passage Mountain Entrance -> Shiver Snowfield Mountain Entrance
    {"from": {"map": "SAM_07", "id": 1}, "to": {"map": "SAM_08", "id": 0}, "reqs": []}, # Shiver Mountain Passage Exit East -> Shiver Mountain Hills Exit West

    {"from": {"map": "SAM_07", "id": 0}, "to": {"map": "SAM_07", "id": 1}, "reqs": [["SuperBoots"]]}, #? Shiver Mountain Passage Mountain Entrance -> Shiver Mountain Passage Exit East
    {"from": {"map": "SAM_07", "id": 1}, "to": {"map": "SAM_07", "id": 0}, "reqs": [["SuperBoots"]]}, #? Shiver Mountain Passage Exit East -> Shiver Mountain Passage Mountain Entrance

    {"from": {"map": "SAM_07", "id": 1}, "to": {"map": "SAM_07", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["UltraBoots"]]}, #* Shiver Mountain Passage Exit East -> HiddenYBlockA (UltraShroom)

    # SAM_08 Shiver Mountain Hills
    {"from": {"map": "SAM_08", "id": 0}, "to": {"map": "SAM_07", "id": 1}, "reqs": []}, # Shiver Mountain Hills Exit West -> Shiver Mountain Passage Exit East
    {"from": {"map": "SAM_08", "id": 1}, "to": {"map": "SAM_09", "id": 0}, "reqs": []}, # Shiver Mountain Hills Exit East -> Shiver Mountain Tunnel Exit West

    {"from": {"map": "SAM_08", "id": 0}, "to": {"map": "SAM_08", "id": 1}, "reqs": [["RF_DefeatedFirstDuplighost"],["can_climb_steps"]]}, #? Shiver Mountain Hills Exit West -> Shiver Mountain Hills Exit East
    {"from": {"map": "SAM_08", "id": 1}, "to": {"map": "SAM_08", "id": 0}, "reqs": [["RF_DefeatedFirstDuplighost","can_climb_steps"]]}, #? Shiver Mountain Hills Exit East -> Shiver Mountain Hills Exit West

    {"from": {"map": "SAM_08", "id": 1}, "to": {"map": "SAM_08", "id": 1}, "reqs": [["Hammer"]], "pseudoitems": ["RF_DefeatedFirstDuplighost"]}, #+ Shiver Mountain Hills Exit East
    {"from": {"map": "SAM_08", "id": 0}, "to": {"map": "SAM_08", "id": 0}, "reqs": [["Kooper"],["Hammer"]], "pseudoitems": ["RF_DefeatedFirstDuplighost"]}, #+ Shiver Mountain Hills Exit East

    {"from": {"map": "SAM_08", "id": 0},       "to": {"map": "SAM_08", "id": "ItemA"}, "reqs": []}, #* Shiver Mountain Hills Exit West -> ItemA (Pebble)
    {"from": {"map": "SAM_08", "id": 1},       "to": {"map": "SAM_08", "id": "ItemA"}, "reqs": []}, #* Shiver Mountain Hills Exit East -> ItemA (Pebble)
    {"from": {"map": "SAM_08", "id": "ItemA"}, "to": {"map": "SAM_08", "id": 0},       "reqs": [["can_climb_steps"]]}, #* ItemA (Pebble) -> Shiver Mountain Hills Exit West

    # SAM_09 Shiver Mountain Tunnel
    {"from": {"map": "SAM_09", "id": 0}, "to": {"map": "SAM_08", "id": 1}, "reqs": []}, # Shiver Mountain Tunnel Exit West -> Shiver Mountain Hills Exit East
    {"from": {"map": "SAM_09", "id": 1}, "to": {"map": "SAM_10", "id": 0}, "reqs": []}, # Shiver Mountain Tunnel Exit East -> Shiver Mountain Peaks Exit West

    {"from": {"map": "SAM_09", "id": 0}, "to": {"map": "SAM_09", "id": 1}, "reqs": []}, #? Shiver Mountain Tunnel Exit West -> Shiver Mountain Tunnel Exit East
    {"from": {"map": "SAM_09", "id": 1}, "to": {"map": "SAM_09", "id": 0}, "reqs": []}, #? Shiver Mountain Tunnel Exit East -> Shiver Mountain Tunnel Exit West

    {"from": {"map": "SAM_09", "id": 0}, "to": {"map": "SAM_09", "id": "ItemA"}, "reqs": []}, #* Shiver Mountain Tunnel Exit West -> ItemA (ShootingStar)
    {"from": {"map": "SAM_09", "id": 0}, "to": {"map": "SAM_09", "id": "ItemB"}, "reqs": []}, #* Shiver Mountain Tunnel Exit West -> ItemB (SnowmanDoll)
    {"from": {"map": "SAM_09", "id": 0}, "to": {"map": "SAM_09", "id": "ItemC"}, "reqs": []}, #* Shiver Mountain Tunnel Exit West -> ItemC (ThunderRage)
# todo: entrance rando ^ this as first room
    # SAM_10 Shiver Mountain Peaks
    {"from": {"map": "SAM_10", "id": 0}, "to": {"map": "SAM_09", "id": 1}, "reqs": []}, # Shiver Mountain Peaks Exit West -> Shiver Mountain Tunnel Exit East
    {"from": {"map": "SAM_10", "id": 1}, "to": {"map": "PRA_01", "id": 0}, "reqs": []}, # Shiver Mountain Peaks Exit East -> Entrance Exit West
    {"from": {"map": "SAM_10", "id": 2}, "to": {"map": "SAM_12", "id": 0}, "reqs": []}, # Shiver Mountain Peaks Bombable Wall -> Merlar's Sanctuary Bombable Wall

    {"from": {"map": "SAM_10", "id": 0}, "to": {"map": "SAM_10", "id": 1}, "reqs": [["StarStone"],["can_climb_steps"]]}, #? Shiver Mountain Peaks Exit West -> Shiver Mountain Peaks Exit East
    {"from": {"map": "SAM_10", "id": 1}, "to": {"map": "SAM_10", "id": 0}, "reqs": []}, #? Shiver Mountain Peaks Exit East -> Shiver Mountain Peaks Exit West
    {"from": {"map": "SAM_10", "id": 0}, "to": {"map": "SAM_10", "id": 2}, "reqs": [["Bombette"]]}, #? Shiver Mountain Peaks Exit West -> Shiver Mountain Peaks Bombable Wall
    {"from": {"map": "SAM_10", "id": 2}, "to": {"map": "SAM_10", "id": 0}, "reqs": []}, #? Shiver Mountain Peaks Bombable Wall -> Shiver Mountain Peaks Exit West

    {"from": {"map": "SAM_10", "id": "ItemA"}, "to": {"map": "SAM_10", "id": "RBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #+ CHAINED REQUIREMENTS -> RBlockA (MegaJump)
    {"from": {"map": "SAM_10", "id": 0},       "to": {"map": "SAM_10", "id": "ItemA"},   "reqs": [["StarStone"],["can_climb_steps"]]}, #* Shiver Mountain Peaks Exit West -> ItemA (StarPiece)

    # SAM_11 Shiver City Pond Area
    {"from": {"map": "SAM_11", "id": 0}, "to": {"map": "SAM_02", "id": 1}, "reqs": []}, # Shiver City Pond Area Exit West -> Shiver City Center Exit East
    {"from": {"map": "SAM_11", "id": 1}, "to": {"map": "SAM_03", "id": 0}, "reqs": []}, # Shiver City Pond Area Exit East -> Road to Shiver Snowfield Exit West

    {"from": {"map": "SAM_11", "id": 0}, "to": {"map": "SAM_11", "id": 1}, "reqs": [["RF_Ch7_MurderMysterySolved"]]}, #? Shiver City Pond Area Exit West -> Shiver City Pond Area Exit East
    {"from": {"map": "SAM_11", "id": 1}, "to": {"map": "SAM_11", "id": 0}, "reqs": []}, #? Shiver City Pond Area Exit East -> Shiver City Pond Area Exit West

    {"from": {"map": "SAM_11", "id": 0}, "to": {"map": "SAM_11", "id": 0}, "reqs": [["RF_Ch7_MurderMysteryStarted"],["WarehouseKey"],["Boots"]], "pseudoitems": ["RF_Ch7_SpokeWithHerringway"]}, #+ Shiver City Pond Area Exit West

    {"from": {"map": "SAM_11", "id": 0}, "to": {"map": "SAM_11", "id": "ItemA"}, "reqs": [["Bombette","SuperBoots"],["Sushie"],["RF_Ch7_MurderMysteryStarted"]]}, #* Shiver City Pond Area Exit West -> ItemA (WarehouseKey)

    {"from": {"map": "SAM_11", "id": 0}, "to": {"map": "SAM_11", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_SAM_1",
                                                                                                    #   "StarPiece_SAM_2",
                                                                                                    #   "StarPiece_SAM_3",
                                                                                                    #   "StarPiece_SAM_4",
                                                                                                    #   "StarPiece_SAM_5",
                                                                                                    #   "StarPiece_SAM_6",
                                                                                                    #   "StarPiece_SAM_7",
                                                                                                       "StarPiece_SAM_8"]}, #+ Quizmo StarPieces

    # SAM_12 Merlar's Sanctuary
    {"from": {"map": "SAM_12", "id": 0}, "to": {"map": "SAM_10", "id": 2}, "reqs": []}, # Merlar's Sanctuary Bombable Wall -> Shiver Mountain Peaks Bombable Wall

    {"from": {"map": "SAM_12", "id": 0}, "to": {"map": "SAM_12", "id": "ItemA"}, "reqs": [["can_climb_steps"]]}, #* Merlar's Sanctuary Bombable Wall -> ItemA (StarStone)
]
