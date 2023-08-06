"""This file represents all edges of the world graph that have origin-nodes in the FLO (Flower Fields) area."""
edges_flo = [
    # FLO_00 Center
    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "MAC_01", "id": 5}, "reqs": []}, # Center Tree Door -> Plaza District Flower Door
    {"from": {"map": "FLO_00", "id": 1}, "to": {"map": "FLO_14", "id": 0}, "reqs": []}, # Center Exit Top Left -> (NW) Bubble Flower Exit Right
    {"from": {"map": "FLO_00", "id": 2}, "to": {"map": "FLO_23", "id": 0}, "reqs": []}, # Center Exit Left -> (West) Path to Maze Exit Right
    {"from": {"map": "FLO_00", "id": 3}, "to": {"map": "FLO_25", "id": 0}, "reqs": []}, # Center Exit Bottom Left -> (SW) Path to Crystal Tree Exit Right
    {"from": {"map": "FLO_00", "id": 4}, "to": {"map": "FLO_16", "id": 0}, "reqs": []}, # Center Exit Top Right -> (NE) Elevators Exit Left
    {"from": {"map": "FLO_00", "id": 5}, "to": {"map": "FLO_09", "id": 0}, "reqs": []}, # Center Exit Right -> (East) Triple Tree Path Exit Left
    {"from": {"map": "FLO_00", "id": 6}, "to": {"map": "FLO_08", "id": 0}, "reqs": []}, # Center Exit Bottom Right -> (SE) Briar Platforming Exit Left
    {"from": {"map": "FLO_00", "id": 8}, "to": {"map": "FLO_19", "id": 3}, "reqs": [["RF_GrewBeanstalk"]]}, # Center Ride Beanstalk Up -> Cloudy Climb Ride Beanstalk Down

    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "FLO_00", "id": 1}, "reqs": []}, #? Center Tree Door -> Center Exit Top Left
    {"from": {"map": "FLO_00", "id": 1}, "to": {"map": "FLO_00", "id": 0}, "reqs": []}, #? Center Exit Top Left -> Center Tree Door
    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "FLO_00", "id": 2}, "reqs": []}, #? Center Tree Door -> Center Exit Left
    {"from": {"map": "FLO_00", "id": 2}, "to": {"map": "FLO_00", "id": 0}, "reqs": []}, #? Center Exit Left -> Center Tree Door
    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "FLO_00", "id": 3}, "reqs": []}, #? Center Tree Door -> Center Exit Bottom Left
    {"from": {"map": "FLO_00", "id": 3}, "to": {"map": "FLO_00", "id": 0}, "reqs": []}, #? Center Exit Bottom Left -> Center Tree Door
    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "FLO_00", "id": 4}, "reqs": []}, #? Center Tree Door -> Center Exit Top Right
    {"from": {"map": "FLO_00", "id": 4}, "to": {"map": "FLO_00", "id": 0}, "reqs": []}, #? Center Exit Top Right -> Center Tree Door
    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "FLO_00", "id": 5}, "reqs": []}, #? Center Tree Door -> Center Exit Right
    {"from": {"map": "FLO_00", "id": 5}, "to": {"map": "FLO_00", "id": 0}, "reqs": []}, #? Center Exit Right -> Center Tree Door
    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "FLO_00", "id": 6}, "reqs": []}, #? Center Tree Door -> Center Exit Bottom Right
    {"from": {"map": "FLO_00", "id": 6}, "to": {"map": "FLO_00", "id": 0}, "reqs": []}, #? Center Exit Bottom Right -> Center Tree Door
    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "FLO_00", "id": 8}, "reqs": []}, #? Center Tree Door -> Center Ride Beanstalk Up
    {"from": {"map": "FLO_00", "id": 8}, "to": {"map": "FLO_00", "id": 0}, "reqs": []}, #? Center Ride Beanstalk Up -> Center Tree Door

    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "FLO_00", "id": 0}, "reqs": [["RF_Ch6_DestroyedPuffPuffMachine"],
                                                                                    ["MagicalBean"],
                                                                                    ["FertileSoil"],
                                                                                    ["MiracleWater"],
                                                                                    ["can_climb_steps"]], "pseudoitems": ["RF_GrewBeanstalk"]}, #+ Plant beanstalk

    # FLO_16 (NE) Elevators
    {"from": {"map": "FLO_16", "id": 0}, "to": {"map": "FLO_00", "id": 4}, "reqs": []}, # (NE) Elevators Exit Left -> Center Exit Top Right
    {"from": {"map": "FLO_16", "id": 1}, "to": {"map": "FLO_17", "id": 0}, "reqs": []}, # (NE) Elevators Exit Right -> (NE) Fallen Logs Exit Left

    {"from": {"map": "FLO_16", "id": 0}, "to": {"map": "FLO_16", "id": 1}, "reqs": [["SuperBoots"], ["Lakilester"]]}, #? (NE) Elevators Exit Left -> (NE) Elevators Exit Right
    {"from": {"map": "FLO_16", "id": 1}, "to": {"map": "FLO_16", "id": 0}, "reqs": [["SuperBoots","Lakilester"]]}, #? (NE) Elevators Exit Right -> (NE) Elevators Exit Left

    {"from": {"map": "FLO_16", "id": 1}, "to": {"map": "FLO_16", "id": "ItemA"}, "reqs": [["SuperBoots"]]}, #* (NE) Elevators Exit Right -> ItemA (StarPiece)
    {"from": {"map": "FLO_16", "id": 0}, "to": {"map": "FLO_16", "id": "ItemB"}, "reqs": [["can_climb_steps","Kooper","Lakilester"]]}, #* (NE) Elevators Exit Left -> ItemB (StinkyHerb)

    # FLO_17 (NE) Fallen Logs
    {"from": {"map": "FLO_17", "id": 0}, "to": {"map": "FLO_16", "id": 1}, "reqs": []}, # (NE) Fallen Logs Exit Left -> (NE) Elevators Exit Right
    {"from": {"map": "FLO_17", "id": 1}, "to": {"map": "FLO_18", "id": 0}, "reqs": []}, # (NE) Fallen Logs Exit Right -> (NE) Puff Puff Machine Exit Left

    {"from": {"map": "FLO_17", "id": 0}, "to": {"map": "FLO_17", "id": 1}, "reqs": []}, #? (NE) Fallen Logs Exit Left -> (NE) Fallen Logs Exit Right
    {"from": {"map": "FLO_17", "id": 1}, "to": {"map": "FLO_17", "id": 0}, "reqs": []}, #? (NE) Fallen Logs Exit Right -> (NE) Fallen Logs Exit Left

    {"from": {"map": "FLO_17", "id": 0}, "to": {"map": "FLO_17", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* (NE) Fallen Logs Exit Left -> HiddenYBlockA (ThunderRage)
    {"from": {"map": "FLO_17", "id": 0}, "to": {"map": "FLO_17", "id": "ItemA"},         "reqs": []}, #* (NE) Fallen Logs Exit Left -> ItemA (Letter09)

    # FLO_18 (NE) Puff Puff Machine
    {"from": {"map": "FLO_18", "id": 0}, "to": {"map": "FLO_17", "id": 1}, "reqs": []}, # (NE) Puff Puff Machine Exit Left -> (NE) Fallen Logs Exit Right

    {"from": {"map": "FLO_18", "id": 0}, "to": {"map": "FLO_18", "id": 0}, "reqs": [["Hammer","Bombette"]], "pseudoitems": ["RF_Ch6_DestroyedPuffPuffMachine"]}, #+ (NE) Puff Puff Machine Exit Left

    # FLO_09 (East) Triple Tree Path
    {"from": {"map": "FLO_09", "id": 0}, "to": {"map": "FLO_00", "id": 5}, "reqs": []}, # (East) Triple Tree Path Exit Left -> Center Exit Right
    {"from": {"map": "FLO_09", "id": 1}, "to": {"map": "FLO_03", "id": 0}, "reqs": []}, # (East) Triple Tree Path Exit Right -> (East) Petunia's Field Exit Left

    {"from": {"map": "FLO_09", "id": 0}, "to": {"map": "FLO_09", "id": 1}, "reqs": []}, #? (East) Triple Tree Path Exit Left -> (East) Triple Tree Path Exit Right
    {"from": {"map": "FLO_09", "id": 1}, "to": {"map": "FLO_09", "id": 0}, "reqs": []}, #? (East) Triple Tree Path Exit Right -> (East) Triple Tree Path Exit Left

    {"from": {"map": "FLO_09", "id": 0}, "to": {"map": "FLO_09", "id": "Tree1_Drop1"}, "reqs": [["can_shake_trees"]]}, #* (East) Triple Tree Path Exit Left -> Tree1_Drop1 (HappyFlowerB)
    {"from": {"map": "FLO_09", "id": 0}, "to": {"map": "FLO_09", "id": "ItemA"},       "reqs": []}, #* (East) Triple Tree Path Exit Left -> ItemA (StinkyHerb)

    # FLO_03 (East) Petunia's Field
    {"from": {"map": "FLO_03", "id": 0}, "to": {"map": "FLO_09", "id": 1}, "reqs": []}, # (East) Petunia's Field Exit Left -> (East) Triple Tree Path Exit Right
    {"from": {"map": "FLO_03", "id": 1}, "to": {"map": "FLO_22", "id": 0}, "reqs": []}, # (East) Petunia's Field Exit Right -> (East) Old Well Exit Left

    {"from": {"map": "FLO_03", "id": 0}, "to": {"map": "FLO_03", "id": 1}, "reqs": []}, #? (East) Petunia's Field Exit Left -> (East) Petunia's Field Exit Right
    {"from": {"map": "FLO_03", "id": 1}, "to": {"map": "FLO_03", "id": 0}, "reqs": []}, #? (East) Petunia's Field Exit Right -> (East) Petunia's Field Exit Left

    {"from": {"map": "FLO_03", "id": 0},              "to": {"map": "FLO_03", "id": "HiddenPanel"},  "reqs": [["can_flip_panels"]]}, #* (East) Petunia's Field Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "FLO_03", "id": 0},              "to": {"map": "FLO_03", "id": "GiftA"},        "reqs": []}, #* (East) Petunia's Field Exit Left -> GiftA (MagicalBean)
    {"from": {"map": "FLO_03", "id": 0},              "to": {"map": "FLO_03", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* (East) Petunia's Field Exit Left -> Tree1_Drop1A (RedBerry)
    {"from": {"map": "FLO_03", "id": "Tree1_Drop1A"}, "to": {"map": "FLO_03", "id": "Tree1_Drop1B"}, "reqs": []}, #+ SHARED REQUIREMENTS -> Tree1_Drop1B (RedBerry)

    # FLO_22 (East) Old Well
    {"from": {"map": "FLO_22", "id": 0}, "to": {"map": "FLO_03", "id": 1}, "reqs": []}, # (East) Old Well Exit Left -> (East) Petunia's Field Exit Right

    {"from": {"map": "FLO_22", "id": 0}, "to": {"map": "FLO_22", "id": "ItemA"}, "reqs": [["BlueBerry"]]}, #* (East) Old Well Exit Left -> ItemA (FLowerSaverB)

    # FLO_08 (SE) Briar Platforming
    {"from": {"map": "FLO_08", "id": 0}, "to": {"map": "FLO_00", "id": 6}, "reqs": []}, # (SE) Briar Platforming Exit Left -> Center Exit Bottom Right
    {"from": {"map": "FLO_08", "id": 1}, "to": {"map": "FLO_24", "id": 0}, "reqs": []}, # (SE) Briar Platforming Exit Right -> (SE) Water Level Room Exit Left

    {"from": {"map": "FLO_08", "id": 0}, "to": {"map": "FLO_08", "id": 1}, "reqs": [["GF_FLO08_GaveYellowBerry"], ["Parakarry","Lakilester"]]}, #? (SE) Briar Platforming Exit Left -> (SE) Briar Platforming Exit Right
    {"from": {"map": "FLO_08", "id": 1}, "to": {"map": "FLO_08", "id": 0}, "reqs": [["GF_FLO08_GaveYellowBerry"], ["Parakarry","Lakilester"]]}, #? (SE) Briar Platforming Exit Right -> (SE) Briar Platforming Exit Left

    {"from": {"map": "FLO_08", "id": 1},              "to": {"map": "FLO_08", "id": "ItemA"},        "reqs": []}, #* (SE) Briar Platforming Exit Right -> ItemA (StarPiece)
    {"from": {"map": "FLO_08", "id": 0},              "to": {"map": "FLO_08", "id": "ItemB"},        "reqs": []}, #* (SE) Briar Platforming Exit Left -> ItemB (StinkyHerb)
    {"from": {"map": "FLO_08", "id": 1},              "to": {"map": "FLO_08", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* (SE) Briar Platforming Exit Right -> Tree1_Drop1A (BlueBerry)
    {"from": {"map": "FLO_08", "id": "Tree1_Drop1A"}, "to": {"map": "FLO_08", "id": "Tree1_Drop1B"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemA (BlueBerry)

    {"from": {"map": "FLO_08", "id": 0}, "to": {"map": "FLO_08", "id": 0}, "reqs": [["YellowBerry"]], "pseudoitems": ["GF_FLO08_GaveYellowBerry"]}, #+ (SE) Briar Platforming Exit Left


    # FLO_24 (SE) Water Level Room
    {"from": {"map": "FLO_24", "id": 0}, "to": {"map": "FLO_08", "id": 1}, "reqs": []}, # (SE) Water Level Room Exit Left -> (SE) Briar Platforming Exit Right
    {"from": {"map": "FLO_24", "id": 1}, "to": {"map": "FLO_10", "id": 0}, "reqs": []}, # (SE) Water Level Room Exit Right -> (SE) Lily's Fountain Exit Left

    {"from": {"map": "FLO_24", "id": 0}, "to": {"map": "FLO_24", "id": 1}, "reqs": [["can_climb_steps","RF_Ch6_ReturnedWaterStone"],["can_climb_steps","Sushie"]]}, #? (SE) Water Level Room Exit Left -> (SE) Water Level Room Exit Right
    {"from": {"map": "FLO_24", "id": 1}, "to": {"map": "FLO_24", "id": 0}, "reqs": [["can_climb_steps","RF_Ch6_ReturnedWaterStone"],["can_climb_steps","Sushie"]]}, #? (SE) Water Level Room Exit Right -> (SE) Water Level Room Exit Left

    {"from": {"map": "FLO_24", "id": 0},              "to": {"map": "FLO_24", "id": "YBlockA"},       "reqs": [["can_hit_floating_blocks"]]}, #* (SE) Water Level Room Exit Left -> YBlockA (DizzyDial)
    {"from": {"map": "FLO_24", "id": 1},              "to": {"map": "FLO_24", "id": "HiddenPanel"},   "reqs": [["can_flip_panels"]]}, #* (SE) Water Level Room Exit Right -> HiddenPanel (StarPiece)
    {"from": {"map": "FLO_24", "id": 1},              "to": {"map": "FLO_24", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"], ["can_hit_floating_blocks"]]}, #* (SE) Water Level Room Exit Right -> HiddenYBlockA (MapleSyrup)
    {"from": {"map": "FLO_24", "id": 0},              "to": {"map": "FLO_24", "id": "Tree1_Drop1A"},  "reqs": [["can_shake_trees"], ["Sushie"], ["RF_Ch6_ReturnedWaterStone"]]}, #* (SE) Water Level Room Exit Left -> Tree1_Drop1A (BubbleBerry)
    {"from": {"map": "FLO_24", "id": "Tree1_Drop1A"}, "to": {"map": "FLO_24", "id": "Tree1_Drop1B"},  "reqs": []}, #+ SHARED REQUIREMENTS -> Tree1_Drop1B (BubbleBerry)

    # FLO_10 (SE) Lily's Fountain
    {"from": {"map": "FLO_10", "id": 0}, "to": {"map": "FLO_24", "id": 1}, "reqs": []}, # (SE) Lily's Fountain Exit Left -> (SE) Water Level Room Exit Right

    {"from": {"map": "FLO_10", "id": 0}, "to": {"map": "FLO_10", "id": "GiftA"},        "reqs": [["WaterStone"]], "pseudoitems": ["RF_Ch6_ReturnedWaterStone"]}, #* (SE) Lily's Fountain Exit Left -> GiftA (MiracleWater)
    {"from": {"map": "FLO_10", "id": 0}, "to": {"map": "FLO_10", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* (SE) Lily's Fountain Exit Left -> Tree1_Drop1A (JamminJelly)

    # FLO_25 (SW) Path to Crystal Tree
    {"from": {"map": "FLO_25", "id": 0}, "to": {"map": "FLO_00", "id": 3}, "reqs": []}, # (SW) Path to Crystal Tree Exit Right -> Center Exit Bottom Left
    {"from": {"map": "FLO_25", "id": 1}, "to": {"map": "FLO_07", "id": 0}, "reqs": []}, # (SW) Path to Crystal Tree Exit Left -> (SW) Posie and Crystal Tree Exit Right

    {"from": {"map": "FLO_25", "id": 0}, "to": {"map": "FLO_25", "id": 1}, "reqs": [["GF_FLO25_GaveRedBerry"]]}, #? (SW) Path to Crystal Tree Exit Right -> (SW) Path to Crystal Tree Exit Left
    {"from": {"map": "FLO_25", "id": 1}, "to": {"map": "FLO_25", "id": 0}, "reqs": [["GF_FLO25_GaveRedBerry"]]}, #? (SW) Path to Crystal Tree Exit Left -> (SW) Path to Crystal Tree Exit Right

    {"from": {"map": "FLO_25", "id": 1},              "to": {"map": "FLO_25", "id": "HiddenPanel"},  "reqs": [["can_flip_panels"]]}, #* (SW) Path to Crystal Tree Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "FLO_25", "id": 1},              "to": {"map": "FLO_25", "id": "ItemA"},        "reqs": []}, #* (SW) Path to Crystal Tree Exit Left -> ItemA (StinkyHerb)
    {"from": {"map": "FLO_25", "id": 1},              "to": {"map": "FLO_25", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* (SW) Path to Crystal Tree Exit Left -> Tree1_Drop1A (YellowBerry)
    {"from": {"map": "FLO_25", "id": "Tree1_Drop1A"}, "to": {"map": "FLO_25", "id": "Tree1_Drop1B"}, "reqs": []}, #+ SHARED REQUIREMENTS -> Tree1_Drop1B (YellowBerry)

    {"from": {"map": "FLO_25", "id": 0}, "to": {"map": "FLO_25", "id": 0}, "reqs": [["RedBerry"]], "pseudoitems": ["GF_FLO25_GaveRedBerry"]}, #+ (SW) Path to Crystal Tree Exit Right

    # FLO_07 (SW) Posie and Crystal Tree
    {"from": {"map": "FLO_07", "id": 0}, "to": {"map": "FLO_25", "id": 1}, "reqs": []}, # (SW) Posie and Crystal Tree Exit Right -> (SW) Path to Crystal Tree Exit Left

    {"from": {"map": "FLO_07", "id": 0}, "to": {"map": "FLO_07", "id": "ItemA"}, "reqs": []}, #* (SW) Posie and Crystal Tree Exit Right -> ItemA (CrystalBerry)
    {"from": {"map": "FLO_07", "id": 0}, "to": {"map": "FLO_07", "id": "GiftA"}, "reqs": []}, #* (SW) Posie and Crystal Tree Exit Right -> GiftA (FertileSoil)

    # FLO_23 (West) Path to Maze
    {"from": {"map": "FLO_23", "id": 0}, "to": {"map": "FLO_00", "id": 2}, "reqs": []}, # (West) Path to Maze Exit Right -> Center Exit Left
    {"from": {"map": "FLO_23", "id": 1}, "to": {"map": "FLO_11", "id": 0}, "reqs": []}, # (West) Path to Maze Exit Left -> (West) Maze Exit Right

    {"from": {"map": "FLO_23", "id": 0}, "to": {"map": "FLO_23", "id": 1}, "reqs": [["GF_FLO23_GaveBlueBerry"]]}, #? (West) Path to Maze Exit Right -> (West) Path to Maze Exit Left
    {"from": {"map": "FLO_23", "id": 1}, "to": {"map": "FLO_23", "id": 0}, "reqs": [["GF_FLO23_GaveBlueBerry"]]}, #? (West) Path to Maze Exit Left -> (West) Path to Maze Exit Right

    {"from": {"map": "FLO_23", "id": 1}, "to": {"map": "FLO_23", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["Boots"]]}, #* (West) Path to Maze Exit Left -> HiddenYBlockA (ShootingStar)
    {"from": {"map": "FLO_23", "id": 1}, "to": {"map": "FLO_23", "id": "HiddenYBlockB"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* (West) Path to Maze Exit Left -> HiddenYBlockB (Coin)

    {"from": {"map": "FLO_23", "id": 0}, "to": {"map": "FLO_23", "id": 1}, "reqs": [["BlueBerry"]], "pseudoitems": ["GF_FLO23_GaveBlueBerry"]}, #+ (West) Path to Maze Exit Right

    # FLO_11 (West) Maze
    #+ Right Side Entrances
    {"from": {"map": "FLO_11", "id": 0}, "to": {"map": "FLO_23", "id": 1}, "reqs": []}, # (West) Maze Exit Right -> (West) Path to Maze Exit Left
    {"from": {"map": "FLO_11", "id": 2}, "to": {"map": "FLO_11", "id": 5}, "reqs": [["can_climb_steps"]]}, # (West) Maze Pipe Top Right -> (West) Maze Pipe Bottom
    {"from": {"map": "FLO_11", "id": 5}, "to": {"map": "FLO_11", "id": 2}, "reqs": [["can_climb_steps"]]}, # (West) Maze Pipe Bottom -> (West) Maze Pipe Top Right
    {"from": {"map": "FLO_11", "id": 3}, "to": {"map": "FLO_11", "id": 6}, "reqs": [["can_climb_steps"]]}, # (West) Maze Pipe Top Center -> (West) Maze Top Left
    {"from": {"map": "FLO_11", "id": 6}, "to": {"map": "FLO_11", "id": 3}, "reqs": [["can_climb_steps"]]}, # (West) Maze Pipe Top Left -> (West) Maze Top Center
    {"from": {"map": "FLO_11", "id": 4}, "to": {"map": "FLO_11", "id": 7}, "reqs": [["can_climb_steps"]]}, # (West) Maze Pipe Center -> (West) Maze Pipe Left
    #+ Left Side Entrances
    {"from": {"map": "FLO_11", "id": 1}, "to": {"map": "FLO_12", "id": 0}, "reqs": []}, # (West) Maze Exit Left -> (West) Rosie's Trellis Exit Right
    {"from": {"map": "FLO_11", "id": 7}, "to": {"map": "FLO_11", "id": 4}, "reqs": [["can_climb_steps"]]}, # (West) Maze Pipe Left -> (West) Maze Pipe Center

    #+ Right Side edges
    {"from": {"map": "FLO_11", "id": 0}, "to": {"map": "FLO_11", "id": 2}, "reqs": [["Boots"]]}, #? (West) Maze Exit Right -> (West) Maze Pipe Top Right
    {"from": {"map": "FLO_11", "id": 0}, "to": {"map": "FLO_11", "id": 3}, "reqs": [["Boots"]]}, #? (West) Maze Exit Right -> (West) Maze Pipe Top Center
    {"from": {"map": "FLO_11", "id": 0}, "to": {"map": "FLO_11", "id": 4}, "reqs": [["Boots"]]}, #? (West) Maze Exit Right -> (West) Maze Pipe Center
    {"from": {"map": "FLO_11", "id": 0}, "to": {"map": "FLO_11", "id": 5}, "reqs": [["Boots"]]}, #? (West) Maze Exit Right -> (West) Maze Pipe Bottom
    {"from": {"map": "FLO_11", "id": 0}, "to": {"map": "FLO_11", "id": 6}, "reqs": [["Boots"]]}, #? (West) Maze Exit Right -> (West) Maze Pipe Top Left
    {"from": {"map": "FLO_11", "id": 2}, "to": {"map": "FLO_11", "id": 0}, "reqs": []}, #? (West) Maze Pipe Top Right -> (West) Maze Exit Right
    {"from": {"map": "FLO_11", "id": 3}, "to": {"map": "FLO_11", "id": 0}, "reqs": []}, #? (West) Maze Pipe Top Center -> (West) Maze Exit Right
    {"from": {"map": "FLO_11", "id": 4}, "to": {"map": "FLO_11", "id": 0}, "reqs": []}, #? (West) Maze Pipe Center -> (West) Maze Exit Right
    {"from": {"map": "FLO_11", "id": 5}, "to": {"map": "FLO_11", "id": 0}, "reqs": []}, #? (West) Maze Pipe Bottom -> (West) Maze Exit Right
    {"from": {"map": "FLO_11", "id": 6}, "to": {"map": "FLO_11", "id": 0}, "reqs": []}, #? (West) Maze Pipe Top Left -> (West) Maze Exit Right
    #+ Left Side edges
    {"from": {"map": "FLO_11", "id": 1}, "to": {"map": "FLO_11", "id": 7}, "reqs": [["Boots"]]}, #? (West) Maze Exit Left -> (West) Maze Pipe Left
    {"from": {"map": "FLO_11", "id": 7}, "to": {"map": "FLO_11", "id": 1}, "reqs": []}, #? (West) Maze Pipe Left -> (West) Maze Exit Left

    # FLO_12 (West) Rosie's Trellis
    {"from": {"map": "FLO_12", "id": 0}, "to": {"map": "FLO_11", "id": 1}, "reqs": []}, # (West) Rosie's Trellis Exit Right -> (West) Maze Exit Left

    {"from": {"map": "FLO_12", "id": 0}, "to": {"map": "FLO_12", "id": "GiftA"}, "reqs": [["CrystalBerry"]]}, #* (West) Rosie's Trellis Exit Right -> GiftA (WaterStone)

    # FLO_14 (NW) Bubble Flower
    {"from": {"map": "FLO_14", "id": 0}, "to": {"map": "FLO_00", "id": 1}, "reqs": []}, # (NW) Bubble Flower Exit Right -> Center Exit Top Left
    {"from": {"map": "FLO_14", "id": 1}, "to": {"map": "FLO_13", "id": 0}, "reqs": []}, # (NW) Bubble Flower Exit Left -> (NW) Lakilester Exit Right

    {"from": {"map": "FLO_14", "id": 0}, "to": {"map": "FLO_14", "id": 1}, "reqs": [["Lakilester","BubbleBerry"]]}, #? (NW) Bubble Flower Exit Right -> (NW) Bubble Flower Exit Left
    {"from": {"map": "FLO_14", "id": 1}, "to": {"map": "FLO_14", "id": 0}, "reqs": [["Lakilester","can_climb_steps"]]}, #? (NW) Bubble Flower Exit Left -> (NW) Bubble Flower Exit Right

    {"from": {"map": "FLO_14", "id": 1}, "to": {"map": "FLO_14", "id": "ItemA"}, "reqs": [["can_climb_steps"]]}, #* (NW) Bubble Flower Exit Left -> ItemA (StarPiece)
    {"from": {"map": "FLO_14", "id": 0}, "to": {"map": "FLO_14", "id": "ItemB"}, "reqs": []}, #* (NW) Bubble Flower Exit Right -> ItemB (StinkyHerb)

    # FLO_13 (NW) Lakilester
    {"from": {"map": "FLO_13", "id": 0}, "to": {"map": "FLO_14", "id": 1}, "reqs": []}, # (NW) Lakilester Exit Right -> (NW) Bubble Flower Exit Left
    {"from": {"map": "FLO_13", "id": 1}, "to": {"map": "FLO_15", "id": 0}, "reqs": []}, # (NW) Lakilester Exit Left -> (NW) Sun Tower Exit Right

    {"from": {"map": "FLO_13", "id": 0}, "to": {"map": "FLO_13", "id": 1}, "reqs": []}, #? (NW) Lakilester Exit Right -> (NW) Lakilester Exit Left
    {"from": {"map": "FLO_13", "id": 1}, "to": {"map": "FLO_13", "id": 0}, "reqs": []}, #? (NW) Lakilester Exit Left -> (NW) Lakilester Exit Right

    {"from": {"map": "FLO_13", "id": 0}, "to": {"map": "FLO_13", "id": "ItemA"},   "reqs": [["Bombette"],["can_climb_steps"]]}, #* (NW) Lakilester Exit Right -> ItemA (MegaSmash)
    {"from": {"map": "FLO_13", "id": 0}, "to": {"map": "FLO_13", "id": "ItemB"},   "reqs": []}, #* (NW) Lakilester Exit Right -> ItemB (ShootingStar)
    {"from": {"map": "FLO_13", "id": 0}, "to": {"map": "FLO_13", "id": "Partner"}, "reqs": [["RF_Ch6_SpokeWithTheSun"]]}, #* (NW) Lakilester Exit Right -> Partner (Lakilester)

    # FLO_15 (NW) Sun Tower
    {"from": {"map": "FLO_15", "id": 0}, "to": {"map": "FLO_13", "id": 1}, "reqs": []}, # (NW) Sun Tower Exit Right -> (NW) Lakilester Exit Left

    {"from": {"map": "FLO_15", "id": 0}, "to": {"map": "FLO_15", "id": 0}, "reqs": [["Bombette"]], "pseudoitems": ["RF_Ch6_SpokeWithTheSun"]}, #+ (NW) Sun Tower Exit Right

    # FLO_19 Cloudy Climb
    {"from": {"map": "FLO_19", "id": 1}, "to": {"map": "FLO_21", "id": 0}, "reqs": []}, # Cloudy Climb Exit Right -> Huff N Puff Room Exit Left
    {"from": {"map": "FLO_19", "id": 3}, "to": {"map": "FLO_00", "id": 8}, "reqs": [["can_climb_steps"],["RF_GrewBeanstalk"]]}, # Cloudy Climb Ride Beanstalk Down -> Center Ride Beanstalk Up

    {"from": {"map": "FLO_19", "id": 1}, "to": {"map": "FLO_19", "id": 3}, "reqs": []}, #? Cloudy Climb Exit Right -> Cloudy Climb Ride Beanstalk Down
    {"from": {"map": "FLO_19", "id": 3}, "to": {"map": "FLO_19", "id": 1}, "reqs": []}, #? Cloudy Climb Ride Beanstalk Down -> Cloudy Climb Exit Right

    {"from": {"map": "FLO_19", "id": 1}, "to": {"map": "FLO_19", "id": "ItemA"}, "reqs": [["can_climb_steps","Kooper"]]}, #* Cloudy Climb Exit Right -> ItemA (SJumpChg)

    # FLO_21 Huff N Puff Room
    {"from": {"map": "FLO_21", "id": 0}, "to": {"map": "FLO_19", "id": 1}, "reqs": []}, # Huff N Puff Room Exit Left -> Cloudy Climb Exit Right

    {"from": {"map": "FLO_21", "id": 0}, "to": {"map": "FLO_21", "id": 0}, "reqs": [["can_climb_steps"]], "pseudoitems": ["STARSPIRIT_6"]}, #+ Huff N Puff Room Exit Left
]
