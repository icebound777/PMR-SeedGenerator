"""This file represents all edges of the world graph that have origin-nodes in the OMO (Shy Guy's Toybox) area."""
edges_omo = [
    # OMO_01 BLU Large Playroom
    {"from": {"map": "OMO_01", "id": 0}, "to": {"map": "OMO_13", "id": 0}, "reqs": []}, # BLU Large Playroom Exit East -> BLU Anti-Guy Hall Exit West

    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemA"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemA (Calculator)
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemB"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemB (MapleSyrup)
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemC"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemC (CakeMix)
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemD"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemD (CakeMix)
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemE"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemE (Mushroom)
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemF"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemF (FireFLower)
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* BLU Large Playroom Exit East -> HiddenYBlockA (Mystery)
    {"from": {"map": "OMO_01", "id": "HiddenYBlockA"}, "to": {"map": "OMO_01", "id": "HiddenYBlockB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> HiddenYBlockB (FrightJar)

    # OMO_02 RED Boss Barricade
    {"from": {"map": "OMO_02", "id": 0}, "to": {"map": "OMO_10", "id": 1}, "reqs": []}, # RED Boss Barricade Exit West -> RED Station Exit East
    {"from": {"map": "OMO_02", "id": 1}, "to": {"map": "OMO_14", "id": 0}, "reqs": []}, # RED Boss Barricade Exit East -> RED Boss Antechamber Exit West

    {"from": {"map": "OMO_02", "id": 0}, "to": {"map": "OMO_02", "id": 1}, "reqs": [["Bombette"]]}, #? RED Boss Barricade Exit West -> RED Boss Barricade Exit East
    {"from": {"map": "OMO_02", "id": 1}, "to": {"map": "OMO_02", "id": 0}, "reqs": [["Bombette"]]}, #? RED Boss Barricade Exit East -> RED Boss Barricade Exit West

    {"from": {"map": "OMO_02", "id": 1},         "to": {"map": "OMO_02", "id": "YBlockA"},       "reqs": [["can_hit_floating_blocks"]]}, #* RED Boss Barricade Exit East -> YBlockA (SleepySheep)
    {"from": {"map": "OMO_02", "id": "YBlockA"}, "to": {"map": "OMO_02", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"]]}, #+ CHAINED REQUIREMENTS (Coin)
    {"from": {"map": "OMO_02", "id": 1},         "to": {"map": "OMO_02", "id": "ItemA"},         "reqs": [["Boots"],["Kooper","UltraBoots"],["Hammer","SuperBoots"],["can_see_hidden_blocks","UltraBoots"],["can_hit_floating_blocks","UltraBoots"]]}, #* RED Boss Barricade Exit East -> ItemA (ShootingStar)

    # OMO_03 BLU Station
    {"from": {"map": "OMO_03", "id": 0}, "to": {"map": "OMO_13", "id": 1}, "reqs": []}, # BLU Station Exit West -> BLU Anti-Guy Hall Exit East
    {"from": {"map": "OMO_03", "id": 1}, "to": {"map": "OMO_04", "id": 0}, "reqs": []}, # BLU Station Exit East -> BLU Block City Exit West
    {"from": {"map": "OMO_03", "id": 2}, "to": {"map": "OMO_10", "id": 3}, "reqs": [["MF_Ch4_CanThrowInTrain"],["ToyTrain"],["RF_BlueSwitchPulled"],["Boots"]]}, # BLU Station Ride Train West -> RED Station Ride Train East
    {"from": {"map": "OMO_03", "id": 3}, "to": {"map": "OMO_06", "id": 2}, "reqs": [["MF_Ch4_CanThrowInTrain"],["ToyTrain"],["Boots"]]}, # BLU Station Ride Train East -> PNK Station Ride Train West
    {"from": {"map": "OMO_03", "id": 4}, "to": {"map": "MAC_04", "id": 2}, "reqs": [["can_climb_steps"]]}, # BLU Station Spring to Toad Town -> Residental District Toybox Spring

    {"from": {"map": "OMO_03", "id": 0}, "to": {"map": "OMO_03", "id": 1}, "reqs": []}, #? BLU Station Exit West -> BLU Station Exit East
    {"from": {"map": "OMO_03", "id": 1}, "to": {"map": "OMO_03", "id": 0}, "reqs": []}, #? BLU Station Exit East -> BLU Station Exit West
    {"from": {"map": "OMO_03", "id": 0}, "to": {"map": "OMO_03", "id": 2}, "reqs": [["MF_Ch4_CanThrowInTrain"],["ToyTrain"],["RF_BlueSwitchPulled"],["Boots"]]}, #? BLU Station Exit West -> BLU Station Ride Train West
    {"from": {"map": "OMO_03", "id": 2}, "to": {"map": "OMO_03", "id": 0}, "reqs": [], "pseudoitems": ["RF_BlueSwitchPulled"]}, #? BLU Station Ride Train West -> BLU Station Exit West
    {"from": {"map": "OMO_03", "id": 0}, "to": {"map": "OMO_03", "id": 3}, "reqs": []}, #? BLU Station Exit West -> BLU Station Ride Train East
    {"from": {"map": "OMO_03", "id": 3}, "to": {"map": "OMO_03", "id": 0}, "reqs": []}, #? BLU Station Ride Train East -> BLU Station Exit West
    {"from": {"map": "OMO_03", "id": 0}, "to": {"map": "OMO_03", "id": 4}, "reqs": []}, #? BLU Station Exit West -> BLU Station Spring to Toad Town
    {"from": {"map": "OMO_03", "id": 4}, "to": {"map": "OMO_03", "id": 0}, "reqs": []}, #? BLU Station Spring to Toad Town -> BLU Station Exit West

    {"from": {"map": "OMO_03", "id": 4}, "to": {"map": "OMO_03", "id": "HiddenPanel"},   "reqs": [["can_flip_panels"]]}, #* BLU Station Spring to Toad Town -> HiddenPanel (StarPiece)
    {"from": {"map": "OMO_03", "id": 4}, "to": {"map": "OMO_03", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* BLU Station Spring to Toad Town -> HiddenYBlockA (StoneCap)

    # OMO_04 BLU Block City
    {"from": {"map": "OMO_04", "id": 0}, "to": {"map": "OMO_03", "id": 1}, "reqs": []}, # BLU Block City Exit West -> BLU Station Exit East

    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemA"},   "reqs": [["Boots"],["Hammer","SuperBoots"]]}, #* BLU Block City Exit West -> ItemA (Mushroom)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ChestA"},  "reqs": []}, #+ SHARED REQUIREMENTS -> ChestA (StoreroomKey)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "YBlockA"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockA (Coin)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "YBlockB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockB (Coin)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "YBlockC"}, "reqs": [["Parakarry"]]}, #+ CHAINED REQUIREMENTS -> YBlockC (ThunderBolt)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ItemB"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemB (Coin)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ItemC"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemC (Coin)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ItemD"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemD (Coin)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ItemE"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemE (Coin)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ItemF"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemF (Coin)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ItemG"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemG (Coin)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ItemH"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemH (Coin)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ItemI"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemI (Coin)
    {"from": {"map": "OMO_04", "id": "YBlockC"}, "to": {"map": "OMO_04", "id": "ItemJ"},   "reqs": []}, #+ CHAINED REQUIREMENTS -> ItemJ (StarPiece) on building
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": "ItemK"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemK (StarPiece)
    #! note: "can_hit_floating_blocks" is redundant above as boots is hard-required to reach the floating blocks

    # OMO_05 PNK Gourmet Guy Crossing
    {"from": {"map": "OMO_05", "id": 0}, "to": {"map": "OMO_17", "id": 0}, "reqs": []}, # PNK Gourmet Guy Crossing Exit East (South) -> PNK Tracks Hallway Exit West (South)
    {"from": {"map": "OMO_05", "id": 1}, "to": {"map": "OMO_17", "id": 1}, "reqs": []}, # PNK Gourmet Guy Crossing Exit East (North) -> PNK Tracks Hallway Exit West (North)

    {"from": {"map": "OMO_05", "id": 0}, "to": {"map": "OMO_05", "id": 1}, "reqs": [["MF_Ch4_GaveCakeToGourmetGuy"]]}, #? PNK Gourmet Guy Crossing Exit East (South) -> PNK Gourmet Guy Crossing Exit East (North)
    {"from": {"map": "OMO_05", "id": 1}, "to": {"map": "OMO_05", "id": 0}, "reqs": []}, #? PNK Gourmet Guy Crossing Exit East (North) -> PNK Gourmet Guy Crossing Exit East (South)

    {"from": {"map": "OMO_05", "id": 0},               "to": {"map": "OMO_05", "id": "ItemA"},         "reqs": [["MF_Ch4_GaveCakeToGourmetGuy"]]}, #* PNK Gourmet Guy Crossing Exit East (South) -> ItemA (Cookbook)
    {"from": {"map": "OMO_05", "id": 1},               "to": {"map": "OMO_05", "id": "YBlockA"},       "reqs": [["can_hit_floating_blocks"]]}, #* PNK Gourmet Guy Crossing Exit East (North) -> YBlockA (Coin)
    {"from": {"map": "OMO_05", "id": "YBlockA"},       "to": {"map": "OMO_05", "id": "YBlockB"},       "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockB (Coin)
    {"from": {"map": "OMO_05", "id": "YBlockA"},       "to": {"map": "OMO_05", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"]]}, #+ CHAINED REQUIREMENTS -> HiddenYBlockA (DizzyDial)
    {"from": {"map": "OMO_05", "id": "HiddenYBlockA"}, "to": {"map": "OMO_05", "id": "HiddenYBlockB"}, "reqs": []}, #+ CHAINED REQUIREMENTS -> HiddenYBlockB (SuperSoda)

    {"from": {"map": "OMO_05", "id": 0}, "to": {"map": "OMO_05", "id": 0}, "reqs": [["Cake"]], "pseudoitems": ["MF_Ch4_GaveCakeToGourmetGuy"]}, #+ Give Cake to Gourmet Guy

    # OMO_06 PNK Station
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_17", "id": 2}, "reqs": []}, # PNK Station Exit West -> PNK Tracks Hallway Exit East (South)
    {"from": {"map": "OMO_06", "id": 1}, "to": {"map": "OMO_17", "id": 3}, "reqs": []}, # PNK Station Exit West (Switch Area) -> PNK Tracks Hallway Exit East (North)
    {"from": {"map": "OMO_06", "id": 2}, "to": {"map": "OMO_03", "id": 3}, "reqs": [["ToyTrain"],["MF_Ch4_CanThrowInTrain"],["Boots"]]}, # PNK Station Ride Train West -> BLU Station Ride Train East
    {"from": {"map": "OMO_06", "id": 3}, "to": {"map": "OMO_08", "id": 1}, "reqs": [["MF_Ch4_PulledPinkSwitch"],["Boots"],["ToyTrain"],["MF_Ch4_CanThrowInTrain"]]}, # PNK Station Ride Train East -> GRN Station Ride Train West
    {"from": {"map": "OMO_06", "id": 4}, "to": {"map": "OMO_07", "id": 0}, "reqs": []}, # PNK Station Exit East -> PNK Playhouse Exit West

    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": 2}, "reqs": []}, #? PNK Station Exit West -> PNK Station Ride Train West
    {"from": {"map": "OMO_06", "id": 2}, "to": {"map": "OMO_06", "id": 0}, "reqs": []}, #? PNK Station Ride Train West -> PNK Station Exit West
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": 3}, "reqs": []}, #? PNK Station Exit West -> PNK Station Ride Train East
    {"from": {"map": "OMO_06", "id": 3}, "to": {"map": "OMO_06", "id": 0}, "reqs": []}, #? PNK Station Ride Train East -> PNK Station Exit West
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": 4}, "reqs": []}, #? PNK Station Exit West -> PNK Station Exit East
    {"from": {"map": "OMO_06", "id": 4}, "to": {"map": "OMO_06", "id": 0}, "reqs": []}, #? PNK Station Exit East -> PNK Station Exit West

    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": "HiddenPanel"},   "reqs": [["can_flip_panels"]]}, #* PNK Station Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": "ChestA"},        "reqs": []}, #* PNK Station Exit West -> ChestA (Mailbag)
    {"from": {"map": "OMO_06", "id": 1}, "to": {"map": "OMO_06", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* PNK Station Exit West (Switch Area) -> HiddenYBlockA (ThunderRage)

    {"from": {"map": "OMO_06", "id": 1}, "to": {"map": "OMO_06", "id": 1}, "reqs": [], "pseudoitems": ["MF_Ch4_PulledPinkSwitch"]}, #+ Pull pink switch

    # OMO_07 PNK Playhouse
    {"from": {"map": "OMO_07", "id": 0}, "to": {"map": "OMO_06", "id": 4}, "reqs": []}, # PNK Playhouse Exit West -> PNK Station Exit East

    {"from": {"map": "OMO_07", "id": 0},       "to": {"map": "OMO_07", "id": "ItemA"},   "reqs": [["Boots"],["Hammer","SuperBoots"]]}, #* PNK Playhouse Exit West -> ItemA (ThunderRage)
    {"from": {"map": "OMO_07", "id": "ItemA"}, "to": {"map": "OMO_07", "id": "ChestA"},  "reqs": []}, #+ SHARED REQUIREMENTS -> ChestA (FryingPan)
    {"from": {"map": "OMO_07", "id": "ItemA"}, "to": {"map": "OMO_07", "id": "ChestB"},  "reqs": []}, #+ SHARED REQUIREMENTS -> ChestB (DefendPlusA)
    {"from": {"map": "OMO_07", "id": "ItemA"}, "to": {"map": "OMO_07", "id": "ChestC"},  "reqs": []}, #+ SHARED REQUIREMENTS -> ChestC (IcePower)
    {"from": {"map": "OMO_07", "id": "ItemA"}, "to": {"map": "OMO_07", "id": "YBlockA"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockA (Coin)
    #! note: "can_hit_floating_blocks" is redundant above as boots is hard-required to reach the floating block

    # OMO_08 GRN Station
    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_09", "id": 0}, "reqs": []}, # GRN Station Exit East -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_08", "id": 1}, "to": {"map": "OMO_06", "id": 3}, "reqs": [["ToyTrain"],["MF_Ch4_CanThrowInTrain"],["Boots"]]}, # GRN Station Ride Train West -> PNK Station Ride Train East
    {"from": {"map": "OMO_08", "id": 2}, "to": {"map": "OMO_10", "id": 2}, "reqs": [["ToyTrain"],["MF_Ch4_CanThrowInTrain"],["MF_Ch4_SolvedColorPuzzle"],["Boots"]]}, # GRN Station Ride Train East -> RED Station Ride Train West

    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_08", "id": 1}, "reqs": []}, #? GRN Station Exit East -> GRN Station Ride Train West
    {"from": {"map": "OMO_08", "id": 1}, "to": {"map": "OMO_08", "id": 0}, "reqs": []}, #? GRN Station Ride Train West -> GRN Station Exit East
    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_08", "id": 2}, "reqs": []}, #? GRN Station Exit East -> GRN Station Ride Train East
    {"from": {"map": "OMO_08", "id": 2}, "to": {"map": "OMO_08", "id": 0}, "reqs": []}, #? GRN Station Ride Train East -> GRN Station Exit East

    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_08", "id": "HiddenPanel"},   "reqs": [["can_flip_panels"]]}, #* GRN Station Exit East -> HiddenPanel (StarPiece)
    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_08", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* GRN Station Exit East -> HiddenYBlockA (FireFlower)

    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_08", "id": 0}, "reqs": [["RF_CanVisitRussT"],["MysteryNote"],["Dictionary"],["Hammer"]], "pseudoitems": ["MF_Ch4_SolvedColorPuzzle"]}, #+ Solve Color Puzzle

    # OMO_09 GRN Treadmills/Slot Machine
    {"from": {"map": "OMO_09", "id": 0}, "to": {"map": "OMO_08", "id": 0}, "reqs": []}, # GRN Treadmills/Slot Machine Exit West -> GRN Station Exit East

    {"from": {"map": "OMO_09", "id": "ItemH"}, "to": {"map": "OMO_09", "id": "ItemA"},  "reqs": [["Parakarry"]]}, #+ CHAINED REQUIREMENTS -> ItemA (SuperSoda)
    {"from": {"map": "OMO_09", "id": "ItemA"}, "to": {"map": "OMO_09", "id": "ChestA"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ChestA (Dictionary)
    {"from": {"map": "OMO_09", "id": "ItemO"}, "to": {"map": "OMO_09", "id": "ItemH"},  "reqs": [["Boots"]]}, #+ CHAINED REQUIREMENTS -> ItemH (StarPiece)
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemO"},  "reqs": [["Bow"]]}, #* GRN Treadmills/Slot Machine Exit West -> ItemO (MysteryNote)
    # Treadmill Coins
    {"from": {"map": "OMO_09", "id": 0}, "to": {"map": "OMO_09", "id": "ItemB"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemB (Coin)
    {"from": {"map": "OMO_09", "id": 0}, "to": {"map": "OMO_09", "id": "ItemC"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemC (Coin)
    {"from": {"map": "OMO_09", "id": 0}, "to": {"map": "OMO_09", "id": "ItemD"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemD (Coin)
    {"from": {"map": "OMO_09", "id": 0}, "to": {"map": "OMO_09", "id": "ItemE"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemE (Coin)
    {"from": {"map": "OMO_09", "id": 0}, "to": {"map": "OMO_09", "id": "ItemF"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemF (Coin)
    {"from": {"map": "OMO_09", "id": 0}, "to": {"map": "OMO_09", "id": "ItemG"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemG (Coin)
    # Starpiece Coins
    {"from": {"map": "OMO_09", "id": "ItemH"}, "to": {"map": "OMO_09", "id": "ItemI"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemI (Coin)
    {"from": {"map": "OMO_09", "id": "ItemH"}, "to": {"map": "OMO_09", "id": "ItemJ"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemJ (Coin)
    {"from": {"map": "OMO_09", "id": "ItemH"}, "to": {"map": "OMO_09", "id": "ItemK"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemK (Coin)
    {"from": {"map": "OMO_09", "id": "ItemH"}, "to": {"map": "OMO_09", "id": "ItemL"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemL (Coin)
    {"from": {"map": "OMO_09", "id": "ItemH"}, "to": {"map": "OMO_09", "id": "ItemM"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemM (Coin)
    {"from": {"map": "OMO_09", "id": "ItemH"}, "to": {"map": "OMO_09", "id": "ItemN"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemN (Coin)

    # OMO_10 RED Station
    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_11", "id": 1}, "reqs": []}, # RED Station Exit West -> RED Moving Platforms Exit East
    {"from": {"map": "OMO_10", "id": 1}, "to": {"map": "OMO_02", "id": 0}, "reqs": []}, # RED Station Exit East -> RED Boss Barricade Exit West
    {"from": {"map": "OMO_10", "id": 2}, "to": {"map": "OMO_08", "id": 2}, "reqs": [["ToyTrain"],["MF_Ch4_CanThrowInTrain"],["Boots"]]}, # RED Station Ride Train West -> GRN Station Ride Train East
    {"from": {"map": "OMO_10", "id": 3}, "to": {"map": "OMO_03", "id": 2}, "reqs": [["ToyTrain"],["MF_Ch4_CanThrowInTrain"],["Boots"]]}, # RED Station Ride Train East -> BLU Station Ride Train West

    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_10", "id": 1}, "reqs": []}, #? RED Station Exit West -> RED Station Exit East
    {"from": {"map": "OMO_10", "id": 1}, "to": {"map": "OMO_10", "id": 0}, "reqs": []}, #? RED Station Exit East -> RED Station Exit West
    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_10", "id": 2}, "reqs": []}, #? RED Station Exit West -> RED Station Ride Train West
    {"from": {"map": "OMO_10", "id": 2}, "to": {"map": "OMO_10", "id": 0}, "reqs": []}, #? RED Station Ride Train West -> RED Station Exit West
    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_10", "id": 3}, "reqs": []}, #? RED Station Exit West -> RED Station Ride Train East
    {"from": {"map": "OMO_10", "id": 3}, "to": {"map": "OMO_10", "id": 0}, "reqs": []}, #? RED Station Ride Train East -> RED Station Exit West

    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_10", "id": "HiddenPanel"},   "reqs": [["can_flip_panels"]]}, #* RED Station Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_10", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* RED Station Exit West -> HiddenYBlockA (SuperShroom)

    # OMO_11 RED Moving Platforms
    {"from": {"map": "OMO_11", "id": 0}, "to": {"map": "OMO_12", "id": 0}, "reqs": []}, # RED Moving Platforms Exit West -> RED Lantern Ghost Exit East
    {"from": {"map": "OMO_11", "id": 1}, "to": {"map": "OMO_10", "id": 0}, "reqs": []}, # RED Moving Platforms Exit East -> RED Station Exit West

    {"from": {"map": "OMO_11", "id": 0}, "to": {"map": "OMO_11", "id": 1}, "reqs": []}, #? RED Moving Platforms Exit West -> RED Moving Platforms Exit East
    {"from": {"map": "OMO_11", "id": 1}, "to": {"map": "OMO_11", "id": 0}, "reqs": []}, #? RED Moving Platforms Exit East -> RED Moving Platforms Exit West

    {"from": {"map": "OMO_11", "id": 1},         "to": {"map": "OMO_11", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* RED Moving Platforms Exit East -> HiddenYBlockA (VoltShroom)
    {"from": {"map": "OMO_11", "id": 0},         "to": {"map": "OMO_11", "id": "HiddenYBlockB"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* RED Moving Platforms Exit West -> HiddenYBlockB (SnowmanDoll)
    {"from": {"map": "OMO_11", "id": 0},         "to": {"map": "OMO_11", "id": "YBlockA"},       "reqs": [["Boots"]]}, #* RED Moving Platforms Exit West -> YBlockA (Coin)
    {"from": {"map": "OMO_11", "id": "YBlockA"}, "to": {"map": "OMO_11", "id": "YBlockB"},       "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockB (Coin)
    {"from": {"map": "OMO_11", "id": "YBlockA"}, "to": {"map": "OMO_11", "id": "HiddenRBlockA"}, "reqs": [["can_see_hidden_blocks"]]}, #+ CHAINED REQUIREMENTS -> HiddenRBlockA (DeepFocus2)
    #! note: "can_hit_floating_blocks" is partially redundant above as boots is hard-required to reach some of the floating blocks

    # OMO_12 RED Lantern Ghost
    {"from": {"map": "OMO_12", "id": 0}, "to": {"map": "OMO_11", "id": 0}, "reqs": []}, # RED Lantern Ghost Exit East -> RED Moving Platforms Exit West

    {"from": {"map": "OMO_12", "id": 0}, "to": {"map": "OMO_12", "id": "Partner"}, "reqs": [["Hammer","Kooper","Bombette"]]}, #* RED Lantern Ghost Exit East -> Partner (Watt)

    # OMO_13 BLU Anti-Guy Hall
    {"from": {"map": "OMO_13", "id": 0}, "to": {"map": "OMO_01", "id": 0}, "reqs": []}, # BLU Anti-Guy Hall Exit West -> BLU Large Playroom Exit East
    {"from": {"map": "OMO_13", "id": 1}, "to": {"map": "OMO_03", "id": 0}, "reqs": []}, # BLU Anti-Guy Hall Exit East -> BLU Station Exit West

    {"from": {"map": "OMO_13", "id": 0}, "to": {"map": "OMO_13", "id": 1}, "reqs": []}, #? BLU Anti-Guy Hall Exit West -> BLU Anti-Guy Hall Exit East
    {"from": {"map": "OMO_13", "id": 1}, "to": {"map": "OMO_13", "id": 0}, "reqs": []}, #? BLU Anti-Guy Hall Exit East -> BLU Anti-Guy Hall Exit West

    {"from": {"map": "OMO_13", "id": 0},         "to": {"map": "OMO_13", "id": "ChestA"},        "reqs": [["LemonCandy"]]}, #* BLU Anti-Guy Hall Exit West -> ChestA (PowerPlusB)
    {"from": {"map": "OMO_13", "id": 0},         "to": {"map": "OMO_13", "id": "YBlockA"},       "reqs": [["can_hit_floating_blocks"]]}, #* BLU Anti-Guy Hall Exit West -> YBlockA (Coin)
    {"from": {"map": "OMO_13", "id": "YBlockA"}, "to": {"map": "OMO_13", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"]]}, #+ CHAINED REQUIREMENTS -> HiddenYBlockA (MapleSyrup)

    # OMO_14 RED Boss Antechamber
    {"from": {"map": "OMO_14", "id": 0}, "to": {"map": "OMO_02", "id": 1}, "reqs": []}, # RED Boss Antechamber Exit West -> RED Boss Barricade Exit East
    {"from": {"map": "OMO_14", "id": 1}, "to": {"map": "OMO_15", "id": 0}, "reqs": [["Watt"]]}, # RED Boss Antechamber Exit East -> RED General Guy Room Exit West

    {"from": {"map": "OMO_14", "id": 0}, "to": {"map": "OMO_14", "id": 1}, "reqs": []}, #? RED Boss Antechamber Exit West -> RED Boss Antechamber Exit East
    {"from": {"map": "OMO_14", "id": 1}, "to": {"map": "OMO_14", "id": 0}, "reqs": []}, #? RED Boss Antechamber Exit East -> RED Boss Antechamber Exit West

    # OMO_15 RED General Guy Room
    {"from": {"map": "OMO_15", "id": 0}, "to": {"map": "OMO_14", "id": 1}, "reqs": []}, # RED General Guy Room Exit West -> RED Boss Antechamber Exit East

    {"from": {"map": "OMO_15", "id": 0}, "to": {"map": "OMO_15", "id": 0}, "reqs": [], "pseudoitems": ["STARSPIRIT_4"]}, # RED General Guy Room Exit West -> RED Boss Antechamber Exit East

    # OMO_17 PNK Tracks Hallway
    {"from": {"map": "OMO_17", "id": 0}, "to": {"map": "OMO_05", "id": 0}, "reqs": []}, # PNK Tracks Hallway Exit West (South) -> PNK Gourmet Guy Crossing Exit East (South)
    {"from": {"map": "OMO_17", "id": 1}, "to": {"map": "OMO_05", "id": 1}, "reqs": []}, # PNK Tracks Hallway Exit West (North) -> PNK Gourmet Guy Crossing Exit East (North)
    {"from": {"map": "OMO_17", "id": 2}, "to": {"map": "OMO_06", "id": 0}, "reqs": []}, # PNK Tracks Hallway Exit East (South) -> PNK Station Exit West
    {"from": {"map": "OMO_17", "id": 3}, "to": {"map": "OMO_06", "id": 1}, "reqs": []}, # PNK Tracks Hallway Exit East (North) -> PNK Station Exit West (Switch Area)

    {"from": {"map": "OMO_17", "id": 0}, "to": {"map": "OMO_17", "id": 2}, "reqs": []}, #? PNK Tracks Hallway Exit West (South) -> PNK Tracks Hallway Exit East (South)
    {"from": {"map": "OMO_17", "id": 2}, "to": {"map": "OMO_17", "id": 0}, "reqs": []}, #? PNK Tracks Hallway Exit East (South) -> PNK Tracks Hallway Exit West (South)
    {"from": {"map": "OMO_17", "id": 1}, "to": {"map": "OMO_17", "id": 3}, "reqs": []}, #? PNK Tracks Hallway Exit West (North) -> PNK Tracks Hallway Exit East (North)
    {"from": {"map": "OMO_17", "id": 3}, "to": {"map": "OMO_17", "id": 1}, "reqs": []}, #? PNK Tracks Hallway Exit East (North) -> PNK Tracks Hallway Exit West (North)

    {"from": {"map": "OMO_17", "id": 0},         "to": {"map": "OMO_17", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* PNK Tracks Hallway Exit West (South) -> YBlockA (Coin)
    {"from": {"map": "OMO_17", "id": 1},         "to": {"map": "OMO_17", "id": "YBlockB"}, "reqs": [["can_hit_floating_blocks"]]}, #* PNK Tracks Hallway Exit West (North) -> YBlockB (Coin)
    {"from": {"map": "OMO_17", "id": "YBlockB"}, "to": {"map": "OMO_17", "id": "YBlockC"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockC (Coin)
]
