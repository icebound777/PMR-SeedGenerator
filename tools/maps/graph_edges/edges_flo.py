from simulate import *

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
    {"from": {"map": "FLO_00", "id": 8}, "to": {"map": "FLO_19", "id": 3}, "reqs": []}, # Center Ride Beanstalk Up -> Cloudy Climb Ride Beanstalk Down
    
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
    {"from": {"map": "FLO_00", "id": 0}, "to": {"map": "FLO_00", "id": 8}, "reqs": [require(flag="RF_Ch6_DestroyedPuffPuffMachine"),
                                                                                    require(item="MagicalBean"),
                                                                                    require(item="FertileSoil"),
                                                                                    require(item="MiracleWater")]}, #? Center Tree Door -> Center Ride Beanstalk Up
    {"from": {"map": "FLO_00", "id": 8}, "to": {"map": "FLO_00", "id": 0}, "reqs": []}, #? Center Ride Beanstalk Up -> Center Tree Door

    # FLO_16 (NE) Elevators
    {"from": {"map": "FLO_16", "id": 0}, "to": {"map": "FLO_00", "id": 4}, "reqs": []}, # (NE) Elevators Exit Left -> Center Exit Top Right
    {"from": {"map": "FLO_16", "id": 1}, "to": {"map": "FLO_17", "id": 0}, "reqs": []}, # (NE) Elevators Exit Right -> (NE) Fallen Logs Exit Left
    
    {"from": {"map": "FLO_16", "id": 0}, "to": {"map": "FLO_16", "id": 1}, "reqs": [require(boots=1), require(partner="PARTNER_Lakilester")]}, #? (NE) Elevators Exit Left -> (NE) Elevators Exit Right
    {"from": {"map": "FLO_16", "id": 1}, "to": {"map": "FLO_16", "id": 0}, "reqs": [require(partner="PARTNER_Lakilester")]}, #? (NE) Elevators Exit Right -> (NE) Elevators Exit Left
    
    {"from": {"map": "FLO_16", "id": 1},       "to": {"map": "FLO_16", "id": "ItemA"}, "reqs": [require(boots=1)]}, #* (NE) Elevators Exit Right -> ItemA (StarPiece)
    {"from": {"map": "FLO_16", "id": "ItemA"}, "to": {"map": "FLO_16", "id": 1},       "reqs": []}, #* ItemA (StarPiece) -> (NE) Elevators Exit Right
    {"from": {"map": "FLO_16", "id": 0},       "to": {"map": "FLO_16", "id": "ItemB"}, "reqs": []}, #* (NE) Elevators Exit Left -> ItemB (StinkyHerb)
    {"from": {"map": "FLO_16", "id": "ItemB"}, "to": {"map": "FLO_16", "id": 0},       "reqs": []}, #* ItemB (StinkyHerb) -> (NE) Elevators Exit Left

    # FLO_17 (NE) Fallen Logs
    {"from": {"map": "FLO_17", "id": 0}, "to": {"map": "FLO_16", "id": 1}, "reqs": []}, # (NE) Fallen Logs Exit Left -> (NE) Elevators Exit Right
    {"from": {"map": "FLO_17", "id": 1}, "to": {"map": "FLO_18", "id": 0}, "reqs": []}, # (NE) Fallen Logs Exit Right -> (NE) Puff Puff Machine Exit Left
    
    {"from": {"map": "FLO_17", "id": 0}, "to": {"map": "FLO_17", "id": 1}, "reqs": []}, #? (NE) Fallen Logs Exit Left -> (NE) Fallen Logs Exit Right
    {"from": {"map": "FLO_17", "id": 1}, "to": {"map": "FLO_17", "id": 0}, "reqs": []}, #? (NE) Fallen Logs Exit Right -> (NE) Fallen Logs Exit Left
    
    {"from": {"map": "FLO_17", "id": 0},               "to": {"map": "FLO_17", "id": "HiddenYBlockA"}, "reqs": []}, #* (NE) Fallen Logs Exit Left -> HiddenYBlockA (ThunderRage)
    {"from": {"map": "FLO_17", "id": "HiddenYBlockA"}, "to": {"map": "FLO_17", "id": 0},               "reqs": []}, #* HiddenYBlockA (ThunderRage) -> (NE) Fallen Logs Exit Left
    {"from": {"map": "FLO_17", "id": 0},               "to": {"map": "FLO_17", "id": "ItemA"},         "reqs": []}, #* (NE) Fallen Logs Exit Left -> ItemA (Letter09)
    {"from": {"map": "FLO_17", "id": "ItemA"},         "to": {"map": "FLO_17", "id": 0},               "reqs": []}, #* ItemA (Letter09) -> (NE) Fallen Logs Exit Left

    # FLO_18 (NE) Puff Puff Machine
    {"from": {"map": "FLO_18", "id": 0}, "to": {"map": "FLO_17", "id": 1}, "reqs": []}, # (NE) Puff Puff Machine Exit Left -> (NE) Fallen Logs Exit Right

    {"from": {"map": "FLO_18", "id": 0}, "to": {"map": "FLO_18", "id": 0}, "reqs": [require(hammer=0)], "pseudoitems": ["RF_Ch6_DestroyedPuffPuffMachine"]}, #+ (NE) Puff Puff Machine Exit Left

    # FLO_09 (East) Triple Tree Path
    {"from": {"map": "FLO_09", "id": 0}, "to": {"map": "FLO_00", "id": 5}, "reqs": []}, # (East) Triple Tree Path Exit Left -> Center Exit Right
    {"from": {"map": "FLO_09", "id": 1}, "to": {"map": "FLO_03", "id": 0}, "reqs": []}, # (East) Triple Tree Path Exit Right -> (East) Petunia's Field Exit Left
    
    {"from": {"map": "FLO_09", "id": 0}, "to": {"map": "FLO_09", "id": 1}, "reqs": []}, #? (East) Triple Tree Path Exit Left -> (East) Triple Tree Path Exit Right
    {"from": {"map": "FLO_09", "id": 1}, "to": {"map": "FLO_09", "id": 0}, "reqs": []}, #? (East) Triple Tree Path Exit Right -> (East) Triple Tree Path Exit Left
    
    {"from": {"map": "FLO_09", "id": 0},       "to": {"map": "FLO_09", "id": "ItemA"}, "reqs": [shake_trees]}, #* (East) Triple Tree Path Exit Left -> ItemA (HappyFlowerB)
    {"from": {"map": "FLO_09", "id": "ItemA"}, "to": {"map": "FLO_09", "id": 0},       "reqs": []}, #* ItemA (HappyFlowerB) -> (East) Triple Tree Path Exit Left
    {"from": {"map": "FLO_09", "id": 0},       "to": {"map": "FLO_09", "id": "ItemB"}, "reqs": []}, #* (East) Triple Tree Path Exit Left -> ItemA (StinkyHerb)
    {"from": {"map": "FLO_09", "id": "ItemB"}, "to": {"map": "FLO_09", "id": 0},       "reqs": []}, #* ItemA (StinkyHerb) -> (East) Triple Tree Path Exit Left

    # FLO_03 (East) Petunia's Field
    {"from": {"map": "FLO_03", "id": 0}, "to": {"map": "FLO_09", "id": 1}, "reqs": []}, # (East) Petunia's Field Exit Left -> (East) Triple Tree Path Exit Right
    {"from": {"map": "FLO_03", "id": 1}, "to": {"map": "FLO_22", "id": 0}, "reqs": []}, # (East) Petunia's Field Exit Right -> (East) Old Well Exit Left
    
    {"from": {"map": "FLO_03", "id": 0}, "to": {"map": "FLO_03", "id": 1}, "reqs": []}, #? (East) Petunia's Field Exit Left -> (East) Petunia's Field Exit Right
    {"from": {"map": "FLO_03", "id": 1}, "to": {"map": "FLO_03", "id": 0}, "reqs": []}, #? (East) Petunia's Field Exit Right -> (East) Petunia's Field Exit Left
    
    {"from": {"map": "FLO_03", "id": 0},              "to": {"map": "FLO_03", "id": "HiddenPanel"},  "reqs": [flip_panels]}, #* (East) Petunia's Field Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "FLO_03", "id": "HiddenPanel"},  "to": {"map": "FLO_03", "id": 0},              "reqs": []}, #* HiddenPanel (StarPiece) -> (East) Petunia's Field Exit Left
    {"from": {"map": "FLO_03", "id": 0},              "to": {"map": "FLO_03", "id": "GiftA"},        "reqs": []}, #* (East) Petunia's Field Exit Left -> GiftA (MagicalBean)
    {"from": {"map": "FLO_03", "id": "GiftA"},        "to": {"map": "FLO_03", "id": 0},              "reqs": []}, #* GiftA (MagicalBean) -> (East) Petunia's Field Exit Left
    {"from": {"map": "FLO_03", "id": 0},              "to": {"map": "FLO_03", "id": "Tree1_Drop1A"}, "reqs": [shake_trees]}, #* (East) Petunia's Field Exit Left -> Tree1_Drop1A (RedBerry)
    {"from": {"map": "FLO_03", "id": "Tree1_Drop1A"}, "to": {"map": "FLO_03", "id": 0},              "reqs": []}, #* Tree1_Drop1A (RedBerry) -> (East) Petunia's Field Exit Left
    {"from": {"map": "FLO_03", "id": 0},              "to": {"map": "FLO_03", "id": "Tree1_Drop1B"}, "reqs": [shake_trees]}, #* (East) Petunia's Field Exit Left -> Tree1_Drop1B (RedBerry)
    {"from": {"map": "FLO_03", "id": "Tree1_Drop1B"}, "to": {"map": "FLO_03", "id": 0},              "reqs": []}, #* Tree1_Drop1B (RedBerry) -> (East) Petunia's Field Exit Left

    # FLO_22 (East) Old Well
    {"from": {"map": "FLO_22", "id": 0}, "to": {"map": "FLO_03", "id": 1}, "reqs": []}, # (East) Old Well Exit Left -> (East) Petunia's Field Exit Right
    
    {"from": {"map": "FLO_22", "id": 0},       "to": {"map": "FLO_22", "id": "ItemA"}, "reqs": [require(item="BlueBerry")]}, #* (East) Old Well Exit Left -> ItemA (FLowerSaverB)
    {"from": {"map": "FLO_22", "id": "ItemA"}, "to": {"map": "FLO_22", "id": 0},       "reqs": []}, #* ItemA (FLowerSaverB) -> (East) Old Well Exit Left

    # FLO_08 (SE) Briar Platforming
    {"from": {"map": "FLO_08", "id": 0}, "to": {"map": "FLO_00", "id": 6}, "reqs": []}, # (SE) Briar Platforming Exit Left -> Center Exit Bottom Right
    {"from": {"map": "FLO_08", "id": 1}, "to": {"map": "FLO_24", "id": 0}, "reqs": []}, # (SE) Briar Platforming Exit Right -> (SE) Water Level Room Exit Left
    
    {"from": {"map": "FLO_08", "id": 0}, "to": {"map": "FLO_08", "id": 1}, "reqs": [require(item="YellowBerry"), require(partner=["PARTNER_Parakarry","PARTNER_Lakilester"])]}, #? (SE) Briar Platforming Exit Left -> (SE) Briar Platforming Exit Right
    {"from": {"map": "FLO_08", "id": 1}, "to": {"map": "FLO_08", "id": 0}, "reqs": [require(partner=["PARTNER_Parakarry","PARTNER_Lakilester"])]}, #? (SE) Briar Platforming Exit Right -> (SE) Briar Platforming Exit Left
    
    {"from": {"map": "FLO_08", "id": 1},              "to": {"map": "FLO_08", "id": "ItemA"},        "reqs": []}, #* (SE) Briar Platforming Exit Right -> ItemA (StarPiece)
    {"from": {"map": "FLO_08", "id": "ItemA"},        "to": {"map": "FLO_08", "id": 1},              "reqs": []}, #* ItemA (StarPiece) -> (SE) Briar Platforming Exit Right
    {"from": {"map": "FLO_08", "id": 0},              "to": {"map": "FLO_08", "id": "ItemB"},        "reqs": []}, #* (SE) Briar Platforming Exit Left -> ItemB (StinkyHerb)
    {"from": {"map": "FLO_08", "id": "ItemB"},        "to": {"map": "FLO_08", "id": 0},              "reqs": []}, #* ItemB (StinkyHerb) -> (SE) Briar Platforming Exit Left
    {"from": {"map": "FLO_08", "id": 1},              "to": {"map": "FLO_08", "id": "Tree1_Drop1A"}, "reqs": [shake_trees]}, #* (SE) Briar Platforming Exit Right -> Tree1_Drop1A (BlueBerry)
    {"from": {"map": "FLO_08", "id": "Tree1_Drop1A"}, "to": {"map": "FLO_08", "id": 1},              "reqs": []}, #* Tree1_Drop1A (BlueBerry) -> (SE) Briar Platforming Exit Right
    {"from": {"map": "FLO_08", "id": 1},              "to": {"map": "FLO_08", "id": "Tree1_Drop1B"}, "reqs": [shake_trees]}, #* (SE) Briar Platforming Exit Right -> ItemA (BlueBerry)
    {"from": {"map": "FLO_08", "id": "Tree1_Drop1B"}, "to": {"map": "FLO_08", "id": 1},              "reqs": []}, #* ItemA (BlueBerry) -> (SE) Briar Platforming Exit Right

    # FLO_24 (SE) Water Level Room
    {"from": {"map": "FLO_24", "id": 0}, "to": {"map": "FLO_08", "id": 1}, "reqs": []}, # (SE) Water Level Room Exit Left -> (SE) Briar Platforming Exit Right
    {"from": {"map": "FLO_24", "id": 1}, "to": {"map": "FLO_10", "id": 0}, "reqs": []}, # (SE) Water Level Room Exit Right -> (SE) Lily's Fountain Exit Left
    
    {"from": {"map": "FLO_24", "id": 0}, "to": {"map": "FLO_24", "id": 1}, "reqs": []}, #? (SE) Water Level Room Exit Left -> (SE) Water Level Room Exit Right
    {"from": {"map": "FLO_24", "id": 1}, "to": {"map": "FLO_24", "id": 0}, "reqs": []}, #? (SE) Water Level Room Exit Right -> (SE) Water Level Room Exit Left
    
    {"from": {"map": "FLO_24", "id": 0},               "to": {"map": "FLO_24", "id": "YBlockA"},       "reqs": []}, #* (SE) Water Level Room Exit Left -> YBlockA (DizzyDial)
    {"from": {"map": "FLO_24", "id": "YBlockA"},       "to": {"map": "FLO_24", "id": 0},               "reqs": []}, #* YBlockA (DizzyDial) -> (SE) Water Level Room Exit Left
    {"from": {"map": "FLO_24", "id": 1},               "to": {"map": "FLO_24", "id": "HiddenPanel"},   "reqs": []}, #* (SE) Water Level Room Exit Right -> HiddenPanel (StarPiece)
    {"from": {"map": "FLO_24", "id": "HiddenPanel"},   "to": {"map": "FLO_24", "id": 1},               "reqs": []}, #* HiddenPanel (StarPiece) -> (SE) Water Level Room Exit Right
    {"from": {"map": "FLO_24", "id": 1},               "to": {"map": "FLO_24", "id": "HiddenYBlockA"}, "reqs": []}, #* (SE) Water Level Room Exit Right -> HiddenYBlockA (MapleSyrup)
    {"from": {"map": "FLO_24", "id": "HiddenYBlockA"}, "to": {"map": "FLO_24", "id": 1},               "reqs": []}, #* HiddenYBlockA (MapleSyrup) -> (SE) Water Level Room Exit Right
    {"from": {"map": "FLO_24", "id": 0},               "to": {"map": "FLO_24", "id": "Tree1_Drop1A"},  "reqs": [shake_trees, require(partner="PARTNER_Sushie"), require(flag="RF_Ch6_GotWaterStone")]}, #* (SE) Water Level Room Exit Left -> Tree1_Drop1A (BubbleBerry)
    {"from": {"map": "FLO_24", "id": "Tree1_Drop1A"},  "to": {"map": "FLO_24", "id": 0},               "reqs": []}, #* Tree1_Drop1A (BubbleBerry) -> (SE) Water Level Room Exit Left
    {"from": {"map": "FLO_24", "id": 0},               "to": {"map": "FLO_24", "id": "Tree1_Drop1B"},  "reqs": [shake_trees, require(partner="PARTNER_Sushie"), require(flag="RF_Ch6_GotWaterStone")]}, #* (SE) Water Level Room Exit Left -> Tree1_Drop1B (BubbleBerry)
    {"from": {"map": "FLO_24", "id": "Tree1_Drop1B"},  "to": {"map": "FLO_24", "id": 0},               "reqs": []}, #* Tree1_Drop1B (BubbleBerry) -> (SE) Water Level Room Exit Left

    # FLO_10 (SE) Lily's Fountain
    {"from": {"map": "FLO_10", "id": 0}, "to": {"map": "FLO_24", "id": 1}, "reqs": []}, # (SE) Lily's Fountain Exit Left -> (SE) Water Level Room Exit Right
    
    {"from": {"map": "FLO_10", "id": 0},              "to": {"map": "FLO_10", "id": "GiftA"},        "reqs": [require(item="WaterStone")], "pseudoitems": ["RF_Ch6_GotWaterStone"]}, #* (SE) Lily's Fountain Exit Left -> GiftA (MiracleWater)
    {"from": {"map": "FLO_10", "id": "GiftA"},        "to": {"map": "FLO_10", "id": 0},              "reqs": []}, #* GiftA (MiracleWater) -> (SE) Lily's Fountain Exit Left
    {"from": {"map": "FLO_10", "id": 0},              "to": {"map": "FLO_10", "id": "Tree1_Drop1A"}, "reqs": [shake_trees]}, #* (SE) Lily's Fountain Exit Left -> Tree1_Drop1A (JamminJelly)
    {"from": {"map": "FLO_10", "id": "Tree1_Drop1A"}, "to": {"map": "FLO_10", "id": 0},              "reqs": []}, #* Tree1_Drop1A (JamminJelly) -> (SE) Lily's Fountain Exit Left

    # FLO_25 (SW) Path to Crystal Tree
    {"from": {"map": "FLO_25", "id": 0}, "to": {"map": "FLO_00", "id": 3}, "reqs": []}, # (SW) Path to Crystal Tree Exit Right -> Center Exit Bottom Left
    {"from": {"map": "FLO_25", "id": 1}, "to": {"map": "FLO_07", "id": 0}, "reqs": []}, # (SW) Path to Crystal Tree Exit Left -> (SW) Posie and Crystal Tree Exit Right
    
    {"from": {"map": "FLO_25", "id": 0}, "to": {"map": "FLO_25", "id": 1}, "reqs": [require(item="RedBerry")]}, #? (SW) Path to Crystal Tree Exit Right -> (SW) Path to Crystal Tree Exit Left
    {"from": {"map": "FLO_25", "id": 1}, "to": {"map": "FLO_25", "id": 0}, "reqs": []}, #? (SW) Path to Crystal Tree Exit Left -> (SW) Path to Crystal Tree Exit Right
    
    {"from": {"map": "FLO_25", "id": 1},              "to": {"map": "FLO_25", "id": "HiddenPanel"},  "reqs": [flip_panels]}, #* (SW) Path to Crystal Tree Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "FLO_25", "id": "HiddenPanel"},  "to": {"map": "FLO_25", "id": 1},              "reqs": []}, #* HiddenPanel (StarPiece) -> (SW) Path to Crystal Tree Exit Left
    {"from": {"map": "FLO_25", "id": 1},              "to": {"map": "FLO_25", "id": "ItemA"},        "reqs": []}, #* (SW) Path to Crystal Tree Exit Left -> ItemA (StinkyHerb)
    {"from": {"map": "FLO_25", "id": "ItemA"},        "to": {"map": "FLO_25", "id": 1},              "reqs": []}, #* ItemA (StinkyHerb) -> (SW) Path to Crystal Tree Exit Left
    {"from": {"map": "FLO_25", "id": 1},              "to": {"map": "FLO_25", "id": "Tree1_Drop1A"}, "reqs": [shake_trees]}, #* (SW) Path to Crystal Tree Exit Left -> Tree1_Drop1A (YellowBerry)
    {"from": {"map": "FLO_25", "id": "Tree1_Drop1A"}, "to": {"map": "FLO_25", "id": 1},              "reqs": []}, #* Tree1_Drop1A (YellowBerry) -> (SW) Path to Crystal Tree Exit Left
    {"from": {"map": "FLO_25", "id": 1},              "to": {"map": "FLO_25", "id": "Tree1_Drop1B"}, "reqs": [shake_trees]}, #* (SW) Path to Crystal Tree Exit Left -> Tree1_Drop1B (YellowBerry)
    {"from": {"map": "FLO_25", "id": "Tree1_Drop1B"}, "to": {"map": "FLO_25", "id": 1},              "reqs": []}, #* Tree1_Drop1B (YellowBerry) -> (SW) Path to Crystal Tree Exit Left

    # FLO_07 (SW) Posie and Crystal Tree
    {"from": {"map": "FLO_07", "id": 0}, "to": {"map": "FLO_25", "id": 1}, "reqs": []}, # (SW) Posie and Crystal Tree Exit Right -> (SW) Path to Crystal Tree Exit Left
    
    {"from": {"map": "FLO_07", "id": 0},       "to": {"map": "FLO_07", "id": "ItemA"}, "reqs": []}, #* (SW) Posie and Crystal Tree Exit Right -> ItemA (CrystalBerry)
    {"from": {"map": "FLO_07", "id": "ItemA"}, "to": {"map": "FLO_07", "id": 0},       "reqs": []}, #* ItemA (CrystalBerry) -> (SW) Posie and Crystal Tree Exit Right
    {"from": {"map": "FLO_07", "id": 0},       "to": {"map": "FLO_07", "id": "GiftA"}, "reqs": []}, #* (SW) Posie and Crystal Tree Exit Right -> GiftA (FertileSoil)
    {"from": {"map": "FLO_07", "id": "GiftA"}, "to": {"map": "FLO_07", "id": 0},       "reqs": []}, #* GiftA (FertileSoil) -> (SW) Posie and Crystal Tree Exit Right

    # FLO_23 (West) Path to Maze
    {"from": {"map": "FLO_23", "id": 0}, "to": {"map": "FLO_00", "id": 2}, "reqs": []}, # (West) Path to Maze Exit Right -> Center Exit Left
    {"from": {"map": "FLO_23", "id": 1}, "to": {"map": "FLO_11", "id": 0}, "reqs": []}, # (West) Path to Maze Exit Left -> (West) Maze Exit Right
    
    {"from": {"map": "FLO_23", "id": 0}, "to": {"map": "FLO_23", "id": 1}, "reqs": [require(item="BlueBerry")]}, #? (West) Path to Maze Exit Right -> (West) Path to Maze Exit Left
    {"from": {"map": "FLO_23", "id": 1}, "to": {"map": "FLO_23", "id": 0}, "reqs": []}, #? (West) Path to Maze Exit Left -> (West) Path to Maze Exit Right
    
    {"from": {"map": "FLO_23", "id": 1},               "to": {"map": "FLO_23", "id": "HiddenYBlockA"}, "reqs": []}, #* (West) Path to Maze Exit Left -> HiddenYBlockA (ShootingStar)
    {"from": {"map": "FLO_23", "id": "HiddenYBlockA"}, "to": {"map": "FLO_23", "id": 1},               "reqs": []}, #* HiddenYBlockA (ShootingStar) -> (West) Path to Maze Exit Left
    {"from": {"map": "FLO_23", "id": 1},               "to": {"map": "FLO_23", "id": "HiddenYBlockB"}, "reqs": []}, #* (West) Path to Maze Exit Left -> HiddenYBlockB (Coin)
    {"from": {"map": "FLO_23", "id": "HiddenYBlockB"}, "to": {"map": "FLO_23", "id": 1},               "reqs": []}, #* HiddenYBlockB (Coin) -> (West) Path to Maze Exit Left

    # FLO_11 (West) Maze
    {"from": {"map": "FLO_11", "id": 0}, "to": {"map": "FLO_23", "id": 1}, "reqs": []}, # (West) Maze Exit Right -> (West) Path to Maze Exit Left
    {"from": {"map": "FLO_11", "id": 1}, "to": {"map": "FLO_12", "id": 0}, "reqs": []}, # (West) Maze Exit Left -> (West) Rosie's Trellis Exit Right
    
    {"from": {"map": "FLO_11", "id": 0}, "to": {"map": "FLO_11", "id": 1}, "reqs": []}, #? (West) Maze Exit Right -> (West) Maze Exit Left
    {"from": {"map": "FLO_11", "id": 1}, "to": {"map": "FLO_11", "id": 0}, "reqs": []}, #? (West) Maze Exit Left -> (West) Maze Exit Right

    # FLO_12 (West) Rosie's Trellis
    {"from": {"map": "FLO_12", "id": 0}, "to": {"map": "FLO_11", "id": 1}, "reqs": []}, # (West) Rosie's Trellis Exit Right -> (West) Maze Exit Left
    
    {"from": {"map": "FLO_12", "id": 0},       "to": {"map": "FLO_12", "id": "GiftA"}, "reqs": [require(item="CrystalBerry")]}, #* (West) Rosie's Trellis Exit Right -> GiftA (WaterStone)
    {"from": {"map": "FLO_12", "id": "GiftA"}, "to": {"map": "FLO_12", "id": 0},       "reqs": []}, #* GiftA (WaterStone) -> (West) Rosie's Trellis Exit Right

    # FLO_14 (NW) Bubble Flower
    {"from": {"map": "FLO_14", "id": 0}, "to": {"map": "FLO_00", "id": 1}, "reqs": []}, # (NW) Bubble Flower Exit Right -> Center Exit Top Left
    {"from": {"map": "FLO_14", "id": 1}, "to": {"map": "FLO_13", "id": 0}, "reqs": []}, # (NW) Bubble Flower Exit Left -> (NW) Lakilester Exit Right
    
    {"from": {"map": "FLO_14", "id": 0}, "to": {"map": "FLO_14", "id": 1}, "reqs": [require(partner="PARTNER_Lakilester",item="BubbleBerry")]}, #? (NW) Bubble Flower Exit Right -> (NW) Bubble Flower Exit Left
    {"from": {"map": "FLO_14", "id": 1}, "to": {"map": "FLO_14", "id": 0}, "reqs": []}, #? (NW) Bubble Flower Exit Left -> (NW) Bubble Flower Exit Right
    
    {"from": {"map": "FLO_14", "id": 1},       "to": {"map": "FLO_14", "id": "ItemA"}, "reqs": []}, #* (NW) Bubble Flower Exit Left -> ItemA (StarPiece)
    {"from": {"map": "FLO_14", "id": "ItemA"}, "to": {"map": "FLO_14", "id": 1},       "reqs": []}, #* ItemA (StarPiece) -> (NW) Bubble Flower Exit Left
    {"from": {"map": "FLO_14", "id": 0},       "to": {"map": "FLO_14", "id": "ItemB"}, "reqs": []}, #* (NW) Bubble Flower Exit Right -> ItemB (StinkyHerb)
    {"from": {"map": "FLO_14", "id": "ItemB"}, "to": {"map": "FLO_14", "id": 0},       "reqs": []}, #* ItemB (StinkyHerb) -> (NW) Bubble Flower Exit Right

    # FLO_13 (NW) Lakilester
    {"from": {"map": "FLO_13", "id": 0}, "to": {"map": "FLO_14", "id": 1}, "reqs": []}, # (NW) Lakilester Exit Right -> (NW) Bubble Flower Exit Left
    {"from": {"map": "FLO_13", "id": 1}, "to": {"map": "FLO_15", "id": 0}, "reqs": []}, # (NW) Lakilester Exit Left -> (NW) Sun Tower Exit Right
    
    {"from": {"map": "FLO_13", "id": 0}, "to": {"map": "FLO_13", "id": 1}, "reqs": []}, #? (NW) Lakilester Exit Right -> (NW) Lakilester Exit Left
    {"from": {"map": "FLO_13", "id": 1}, "to": {"map": "FLO_13", "id": 0}, "reqs": []}, #? (NW) Lakilester Exit Left -> (NW) Lakilester Exit Right
    
    {"from": {"map": "FLO_13", "id": 0},       "to": {"map": "FLO_13", "id": "ItemA"}, "reqs": [require(partner="PARTNER_Bombette")]}, #* (NW) Lakilester Exit Right -> ItemA (MegaSmash)
    {"from": {"map": "FLO_13", "id": "ItemA"}, "to": {"map": "FLO_13", "id": 0},       "reqs": []}, #* ItemA (MegaSmash) -> (NW) Lakilester Exit Right
    {"from": {"map": "FLO_13", "id": 0},       "to": {"map": "FLO_13", "id": "ItemB"}, "reqs": []}, #* (NW) Lakilester Exit Right -> ItemB (ShootingStar)
    {"from": {"map": "FLO_13", "id": "ItemB"}, "to": {"map": "FLO_13", "id": 0},       "reqs": []}, #* ItemB (ShootingStar) -> (NW) Lakilester Exit Right

    {"from": {"map": "FLO_13", "id": 1}, "to": {"map": "FLO_13", "id": 1}, "reqs": [require(flag="RF_Ch6_SpokeWithTheSun")], "pseudoitems": ["PARTNER_Lakilester"]}, #+ (NW) Lakilester Exit Left

    # FLO_15 (NW) Sun Tower
    {"from": {"map": "FLO_15", "id": 0}, "to": {"map": "FLO_13", "id": 1}, "reqs": []}, # (NW) Sun Tower Exit Right -> (NW) Lakilester Exit Left

    {"from": {"map": "FLO_15", "id": 0}, "to": {"map": "FLO_15", "id": 0}, "reqs": [require(partner="PARTNER_Bombette")], "pseudoitems": ["RF_Ch6_SpokeWithTheSun"]}, #+ (NW) Sun Tower Exit Right

    # FLO_19 Cloudy Climb
    {"from": {"map": "FLO_19", "id": 1}, "to": {"map": "FLO_21", "id": 0}, "reqs": []}, # Cloudy Climb Exit Right -> Huff N Puff Room Exit Left
    {"from": {"map": "FLO_19", "id": 3}, "to": {"map": "FLO_00", "id": 8}, "reqs": []}, # Cloudy Climb Ride Beanstalk Down -> Center Ride Beanstalk Up
    
    {"from": {"map": "FLO_19", "id": 1}, "to": {"map": "FLO_19", "id": 3}, "reqs": []}, #? Cloudy Climb Exit Right -> Cloudy Climb Ride Beanstalk Down
    {"from": {"map": "FLO_19", "id": 3}, "to": {"map": "FLO_19", "id": 1}, "reqs": []}, #? Cloudy Climb Ride Beanstalk Down -> Cloudy Climb Exit Right
    
    {"from": {"map": "FLO_19", "id": 1},       "to": {"map": "FLO_19", "id": "ItemA"}, "reqs": []}, #* Cloudy Climb Exit Right -> ItemA (SJumpChg)
    {"from": {"map": "FLO_19", "id": "ItemA"}, "to": {"map": "FLO_19", "id": 1},       "reqs": []}, #* ItemA (SJumpChg) -> Cloudy Climb Exit Right

    # FLO_21 Huff N Puff Room
    {"from": {"map": "FLO_21", "id": 0}, "to": {"map": "FLO_19", "id": 1}, "reqs": []}, # Huff N Puff Room Exit Left -> Cloudy Climb Exit Right

    {"from": {"map": "FLO_21", "id": 0}, "to": {"map": "FLO_21", "id": 0}, "reqs": [], "pseudoitems": ["STARSPIRIT"]}, #+ Huff N Puff Room Exit Left
]