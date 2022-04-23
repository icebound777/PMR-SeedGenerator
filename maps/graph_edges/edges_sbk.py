from rando_modules.simulate import *

"""This file represents all edges of the world graph that have origin-nodes in the SBK (Dry Dry Desert) area."""
edges_sbk = [
    # SBK_00 N3W3
    {"from": {"map": "SBK_00", "id": 1}, "to": {"map": "SBK_01", "id": 0}, "reqs": []}, # N3W3 Exit East -> N3W2 Exit West
    {"from": {"map": "SBK_00", "id": 3}, "to": {"map": "SBK_10", "id": 2}, "reqs": []}, # N3W3 Exit South -> N2W3 Exit North
    
    {"from": {"map": "SBK_00", "id": 1}, "to": {"map": "SBK_00", "id": 3}, "reqs": []}, #? N3W3 Exit East -> N3W3 Exit South
    {"from": {"map": "SBK_00", "id": 3}, "to": {"map": "SBK_00", "id": 1}, "reqs": []}, #? N3W3 Exit South -> N3W3 Exit East
    
    {"from": {"map": "SBK_00", "id": 1},         "to": {"map": "SBK_00", "id": "YBlockA"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N3W3 Exit East -> YBlockA (FrightJar)
    {"from": {"map": "SBK_00", "id": "YBlockA"}, "to": {"map": "SBK_00", "id": 1},         "reqs": []}, #* YBlockA (FrightJar) -> N3W3 Exit East
    {"from": {"map": "SBK_00", "id": 1},         "to": {"map": "SBK_00", "id": "YBlockB"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N3W3 Exit East -> YBlockB (Coin)
    {"from": {"map": "SBK_00", "id": "YBlockB"}, "to": {"map": "SBK_00", "id": 1},         "reqs": []}, #* YBlockB (Coin) -> N3W3 Exit East

    # SBK_01 N3W2
    {"from": {"map": "SBK_01", "id": 0}, "to": {"map": "SBK_00", "id": 1}, "reqs": []}, # N3W2 Exit West -> N3W3 Exit East
    {"from": {"map": "SBK_01", "id": 1}, "to": {"map": "SBK_02", "id": 0}, "reqs": []}, # N3W2 Exit East -> N3W1 Ruins Entrance Exit West
    {"from": {"map": "SBK_01", "id": 3}, "to": {"map": "SBK_11", "id": 2}, "reqs": []}, # N3W2 Exit South -> N2W2 Exit North
    
    {"from": {"map": "SBK_01", "id": 0}, "to": {"map": "SBK_01", "id": 1}, "reqs": []}, #? N3W2 Exit West -> N3W2 Exit East
    {"from": {"map": "SBK_01", "id": 1}, "to": {"map": "SBK_01", "id": 0}, "reqs": []}, #? N3W2 Exit East -> N3W2 Exit West
    {"from": {"map": "SBK_01", "id": 0}, "to": {"map": "SBK_01", "id": 3}, "reqs": []}, #? N3W2 Exit West -> N3W2 Exit South
    {"from": {"map": "SBK_01", "id": 3}, "to": {"map": "SBK_01", "id": 0}, "reqs": []}, #? N3W2 Exit South -> N3W2 Exit West

    # SBK_02 N3W1 Ruins Entrance
    {"from": {"map": "SBK_02", "id": 0}, "to": {"map": "SBK_01", "id": 1}, "reqs": []}, # N3W1 Ruins Entrance Exit West -> N3W2 Exit East
    {"from": {"map": "SBK_02", "id": 1}, "to": {"map": "SBK_03", "id": 0}, "reqs": []}, # N3W1 Ruins Entrance Exit East -> N3 Exit West
    {"from": {"map": "SBK_02", "id": 3}, "to": {"map": "SBK_12", "id": 2}, "reqs": []}, # N3W1 Ruins Entrance Exit South -> N2W1 Exit North
    {"from": {"map": "SBK_02", "id": 4}, "to": {"map": "ISK_01", "id": 0}, "reqs": []}, # N3W1 Ruins Entrance Enter Ruins -> ISK Entrance Exit West
    
    {"from": {"map": "SBK_02", "id": 0}, "to": {"map": "SBK_02", "id": 1}, "reqs": []}, #? N3W1 Ruins Entrance Exit West -> N3W1 Ruins Entrance Exit East
    {"from": {"map": "SBK_02", "id": 1}, "to": {"map": "SBK_02", "id": 0}, "reqs": []}, #? N3W1 Ruins Entrance Exit East -> N3W1 Ruins Entrance Exit West
    {"from": {"map": "SBK_02", "id": 0}, "to": {"map": "SBK_02", "id": 3}, "reqs": []}, #? N3W1 Ruins Entrance Exit West -> N3W1 Ruins Entrance Exit South
    {"from": {"map": "SBK_02", "id": 3}, "to": {"map": "SBK_02", "id": 0}, "reqs": []}, #? N3W1 Ruins Entrance Exit South -> N3W1 Ruins Entrance Exit West
    {"from": {"map": "SBK_02", "id": 0}, "to": {"map": "SBK_02", "id": 4}, "reqs": [require(item="PulseStone")]}, #? N3W1 Ruins Entrance Exit West -> N3W1 Ruins Entrance Enter Ruins
    {"from": {"map": "SBK_02", "id": 4}, "to": {"map": "SBK_02", "id": 0}, "reqs": []}, #? N3W1 Ruins Entrance Enter Ruins -> N3W1 Ruins Entrance Exit West

    # SBK_03 N3
    {"from": {"map": "SBK_03", "id": 0}, "to": {"map": "SBK_02", "id": 1}, "reqs": []}, # N3 Exit West -> N3W1 Ruins Entrance Exit East
    {"from": {"map": "SBK_03", "id": 1}, "to": {"map": "SBK_04", "id": 0}, "reqs": []}, # N3 Exit East -> N3E1 Exit West
    {"from": {"map": "SBK_03", "id": 3}, "to": {"map": "SBK_13", "id": 2}, "reqs": []}, # N3 Exit South -> N2 Exit North
    
    {"from": {"map": "SBK_03", "id": 0}, "to": {"map": "SBK_03", "id": 1}, "reqs": []}, #? N3 Exit West -> N3 Exit East
    {"from": {"map": "SBK_03", "id": 1}, "to": {"map": "SBK_03", "id": 0}, "reqs": []}, #? N3 Exit East -> N3 Exit West
    {"from": {"map": "SBK_03", "id": 0}, "to": {"map": "SBK_03", "id": 3}, "reqs": []}, #? N3 Exit West -> N3 Exit South
    {"from": {"map": "SBK_03", "id": 3}, "to": {"map": "SBK_03", "id": 0}, "reqs": []}, #? N3 Exit South -> N3 Exit West

    # SBK_04 N3E1
    {"from": {"map": "SBK_04", "id": 0}, "to": {"map": "SBK_03", "id": 1}, "reqs": []}, # N3E1 Exit West -> N3 Exit East
    {"from": {"map": "SBK_04", "id": 1}, "to": {"map": "SBK_05", "id": 0}, "reqs": []}, # N3E1 Exit East -> N3E2 Pokey Army Exit West
    {"from": {"map": "SBK_04", "id": 3}, "to": {"map": "SBK_14", "id": 2}, "reqs": []}, # N3E1 Exit South -> N2E1 (Tweester A) Exit North
    
    {"from": {"map": "SBK_04", "id": 0}, "to": {"map": "SBK_04", "id": 1}, "reqs": []}, #? N3E1 Exit West -> N3E1 Exit East
    {"from": {"map": "SBK_04", "id": 1}, "to": {"map": "SBK_04", "id": 0}, "reqs": []}, #? N3E1 Exit East -> N3E1 Exit West
    {"from": {"map": "SBK_04", "id": 0}, "to": {"map": "SBK_04", "id": 3}, "reqs": []}, #? N3E1 Exit West -> N3E1 Exit South
    {"from": {"map": "SBK_04", "id": 3}, "to": {"map": "SBK_04", "id": 0}, "reqs": []}, #? N3E1 Exit South -> N3E1 Exit West

    # SBK_05 N3E2 Pokey Army
    {"from": {"map": "SBK_05", "id": 0}, "to": {"map": "SBK_04", "id": 1}, "reqs": []}, # N3E2 Pokey Army Exit West -> N3E1 Exit East
    {"from": {"map": "SBK_05", "id": 1}, "to": {"map": "SBK_06", "id": 0}, "reqs": []}, # N3E2 Pokey Army Exit East -> N3E3 Exit West
    {"from": {"map": "SBK_05", "id": 3}, "to": {"map": "SBK_15", "id": 2}, "reqs": []}, # N3E2 Pokey Army Exit South -> N2E2 Exit North
    {"from": {"map": "SBK_05", "id": 4}, "to": {"map": None, "id": None},  "reqs": []}, # N3E2 Pokey Army Fall From Sky
    
    {"from": {"map": "SBK_05", "id": 0}, "to": {"map": "SBK_05", "id": 1}, "reqs": []}, #? N3E2 Pokey Army Exit West -> N3E2 Pokey Army Exit East
    {"from": {"map": "SBK_05", "id": 1}, "to": {"map": "SBK_05", "id": 0}, "reqs": []}, #? N3E2 Pokey Army Exit East -> N3E2 Pokey Army Exit West
    {"from": {"map": "SBK_05", "id": 0}, "to": {"map": "SBK_05", "id": 3}, "reqs": []}, #? N3E2 Pokey Army Exit West -> N3E2 Pokey Army Exit South
    {"from": {"map": "SBK_05", "id": 3}, "to": {"map": "SBK_05", "id": 0}, "reqs": []}, #? N3E2 Pokey Army Exit South -> N3E2 Pokey Army Exit West
    {"from": {"map": "SBK_05", "id": 0}, "to": {"map": "SBK_05", "id": 4}, "reqs": []}, #? N3E2 Pokey Army Exit West -> N3E2 Pokey Army Fall From Sky
    {"from": {"map": "SBK_05", "id": 4}, "to": {"map": "SBK_05", "id": 0}, "reqs": []}, #? N3E2 Pokey Army Fall From Sky -> N3E2 Pokey Army Exit West
    
    {"from": {"map": "SBK_05", "id": 0},       "to": {"map": "SBK_05", "id": "ItemA"}, "reqs": []}, #* N3E2 Pokey Army Exit West -> ItemA (FireFlower)
    {"from": {"map": "SBK_05", "id": "ItemA"}, "to": {"map": "SBK_05", "id": 0},       "reqs": []}, #* ItemA (FireFlower) -> N3E2 Pokey Army Exit West

    # SBK_06 N3E3
    {"from": {"map": "SBK_06", "id": 0}, "to": {"map": "SBK_05", "id": 1}, "reqs": []}, # N3E3 Exit West -> N3E2 Pokey Army Exit East
    {"from": {"map": "SBK_06", "id": 3}, "to": {"map": "SBK_16", "id": 2}, "reqs": []}, # N3E3 Exit South -> N2E3 Exit North
    
    {"from": {"map": "SBK_06", "id": 0}, "to": {"map": "SBK_06", "id": 3}, "reqs": []}, #? N3E3 Exit West -> N3E3 Exit South
    {"from": {"map": "SBK_06", "id": 3}, "to": {"map": "SBK_06", "id": 0}, "reqs": []}, #? N3E3 Exit South -> N3E3 Exit West

    # SBK_10 N2W3
    {"from": {"map": "SBK_10", "id": 1}, "to": {"map": "SBK_11", "id": 0}, "reqs": []}, # N2W3 Exit East -> N2W2 Exit West
    {"from": {"map": "SBK_10", "id": 2}, "to": {"map": "SBK_00", "id": 3}, "reqs": []}, # N2W3 Exit North -> N3W3 Exit South
    {"from": {"map": "SBK_10", "id": 3}, "to": {"map": "SBK_20", "id": 2}, "reqs": []}, # N2W3 Exit South -> N1W3 Special Block Exit North
    
    {"from": {"map": "SBK_10", "id": 1}, "to": {"map": "SBK_10", "id": 2}, "reqs": []}, #? N2W3 Exit East -> N2W3 Exit North
    {"from": {"map": "SBK_10", "id": 2}, "to": {"map": "SBK_10", "id": 1}, "reqs": []}, #? N2W3 Exit North -> N2W3 Exit East
    {"from": {"map": "SBK_10", "id": 1}, "to": {"map": "SBK_10", "id": 3}, "reqs": []}, #? N2W3 Exit East -> N2W3 Exit South
    {"from": {"map": "SBK_10", "id": 3}, "to": {"map": "SBK_10", "id": 1}, "reqs": []}, #? N2W3 Exit South -> N2W3 Exit East
    
    {"from": {"map": "SBK_10", "id": 1},               "to": {"map": "SBK_10", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt",flag="RF_HiddenBlocksVisible")]}, #* N2W3 Exit East -> HiddenYBlockA (ThunderRage)
    {"from": {"map": "SBK_10", "id": "HiddenYBlockA"}, "to": {"map": "SBK_10", "id": 1},               "reqs": []}, #* HiddenYBlockA (ThunderRage) -> N2W3 Exit East

    # SBK_11 N2W2
    {"from": {"map": "SBK_11", "id": 0}, "to": {"map": "SBK_10", "id": 1}, "reqs": []}, # N2W2 Exit West -> N2W3 Exit East
    {"from": {"map": "SBK_11", "id": 1}, "to": {"map": "SBK_12", "id": 0}, "reqs": []}, # N2W2 Exit East -> N2W1 Exit West
    {"from": {"map": "SBK_11", "id": 2}, "to": {"map": "SBK_01", "id": 3}, "reqs": []}, # N2W2 Exit North -> N3W2 Exit South
    {"from": {"map": "SBK_11", "id": 3}, "to": {"map": "SBK_21", "id": 2}, "reqs": []}, # N2W2 Exit South -> N1W2 Exit North
    
    {"from": {"map": "SBK_11", "id": 0}, "to": {"map": "SBK_11", "id": 1}, "reqs": []}, #? N2W2 Exit West -> N2W2 Exit East
    {"from": {"map": "SBK_11", "id": 1}, "to": {"map": "SBK_11", "id": 0}, "reqs": []}, #? N2W2 Exit East -> N2W2 Exit West
    {"from": {"map": "SBK_11", "id": 0}, "to": {"map": "SBK_11", "id": 2}, "reqs": []}, #? N2W2 Exit West -> N2W2 Exit North
    {"from": {"map": "SBK_11", "id": 2}, "to": {"map": "SBK_11", "id": 0}, "reqs": []}, #? N2W2 Exit North -> N2W2 Exit West
    {"from": {"map": "SBK_11", "id": 0}, "to": {"map": "SBK_11", "id": 3}, "reqs": []}, #? N2W2 Exit West -> N2W2 Exit South
    {"from": {"map": "SBK_11", "id": 3}, "to": {"map": "SBK_11", "id": 0}, "reqs": []}, #? N2W2 Exit South -> N2W2 Exit West

    # SBK_12 N2W1
    {"from": {"map": "SBK_12", "id": 0}, "to": {"map": "SBK_11", "id": 1}, "reqs": []}, # N2W1 Exit West -> N2W2 Exit East
    {"from": {"map": "SBK_12", "id": 1}, "to": {"map": "SBK_13", "id": 0}, "reqs": []}, # N2W1 Exit East -> N2 Exit West
    {"from": {"map": "SBK_12", "id": 2}, "to": {"map": "SBK_02", "id": 3}, "reqs": []}, # N2W1 Exit North -> N3W1 Ruins Entrance Exit South
    {"from": {"map": "SBK_12", "id": 3}, "to": {"map": "SBK_22", "id": 2}, "reqs": []}, # N2W1 Exit South -> N1W1 Exit North
    
    {"from": {"map": "SBK_12", "id": 0}, "to": {"map": "SBK_12", "id": 1}, "reqs": []}, #? N2W1 Exit West -> N2W1 Exit East
    {"from": {"map": "SBK_12", "id": 1}, "to": {"map": "SBK_12", "id": 0}, "reqs": []}, #? N2W1 Exit East -> N2W1 Exit West
    {"from": {"map": "SBK_12", "id": 0}, "to": {"map": "SBK_12", "id": 2}, "reqs": []}, #? N2W1 Exit West -> N2W1 Exit North
    {"from": {"map": "SBK_12", "id": 2}, "to": {"map": "SBK_12", "id": 0}, "reqs": []}, #? N2W1 Exit North -> N2W1 Exit West
    {"from": {"map": "SBK_12", "id": 0}, "to": {"map": "SBK_12", "id": 3}, "reqs": []}, #? N2W1 Exit West -> N2W1 Exit South
    {"from": {"map": "SBK_12", "id": 3}, "to": {"map": "SBK_12", "id": 0}, "reqs": []}, #? N2W1 Exit South -> N2W1 Exit West

    # SBK_13 N2
    {"from": {"map": "SBK_13", "id": 0}, "to": {"map": "SBK_12", "id": 1}, "reqs": []}, # N2 Exit West -> N2W1 Exit East
    {"from": {"map": "SBK_13", "id": 1}, "to": {"map": "SBK_14", "id": 0}, "reqs": []}, # N2 Exit East -> N2E1 (Tweester A) Exit West
    {"from": {"map": "SBK_13", "id": 2}, "to": {"map": "SBK_03", "id": 3}, "reqs": []}, # N2 Exit North -> N3 Exit South
    {"from": {"map": "SBK_13", "id": 3}, "to": {"map": "SBK_23", "id": 2}, "reqs": []}, # N2 Exit South -> N1 (Tweester B) Exit North
    
    {"from": {"map": "SBK_13", "id": 0}, "to": {"map": "SBK_13", "id": 1}, "reqs": []}, #? N2 Exit West -> N2 Exit East
    {"from": {"map": "SBK_13", "id": 1}, "to": {"map": "SBK_13", "id": 0}, "reqs": []}, #? N2 Exit East -> N2 Exit West
    {"from": {"map": "SBK_13", "id": 0}, "to": {"map": "SBK_13", "id": 2}, "reqs": []}, #? N2 Exit West -> N2 Exit North
    {"from": {"map": "SBK_13", "id": 2}, "to": {"map": "SBK_13", "id": 0}, "reqs": []}, #? N2 Exit North -> N2 Exit West
    {"from": {"map": "SBK_13", "id": 0}, "to": {"map": "SBK_13", "id": 3}, "reqs": []}, #? N2 Exit West -> N2 Exit South
    {"from": {"map": "SBK_13", "id": 3}, "to": {"map": "SBK_13", "id": 0}, "reqs": []}, #? N2 Exit South -> N2 Exit West

    # SBK_14 N2E1 (Tweester A)
    {"from": {"map": "SBK_14", "id": 0}, "to": {"map": "SBK_13", "id": 1}, "reqs": []}, # N2E1 (Tweester A) Exit West -> N2 Exit East
    {"from": {"map": "SBK_14", "id": 1}, "to": {"map": "SBK_15", "id": 0}, "reqs": []}, # N2E1 (Tweester A) Exit East -> N2E2 Exit West
    {"from": {"map": "SBK_14", "id": 2}, "to": {"map": "SBK_04", "id": 3}, "reqs": []}, # N2E1 (Tweester A) Exit North -> N3E1 Exit South
    {"from": {"map": "SBK_14", "id": 3}, "to": {"map": "SBK_24", "id": 2}, "reqs": []}, # N2E1 (Tweester A) Exit South -> N1E1 Palm Trio Exit North
    {"from": {"map": "SBK_14", "id": 4}, "to": {"map": "SBK_05", "id": 4}, "reqs": []}, # N2E1 (Tweester A) Tweester -> N3E2 Pokey Army Fall From Sky
    
    {"from": {"map": "SBK_14", "id": 0}, "to": {"map": "SBK_14", "id": 1}, "reqs": []}, #? N2E1 (Tweester A) Exit West -> N2E1 (Tweester A) Exit East
    {"from": {"map": "SBK_14", "id": 1}, "to": {"map": "SBK_14", "id": 0}, "reqs": []}, #? N2E1 (Tweester A) Exit East -> N2E1 (Tweester A) Exit West
    {"from": {"map": "SBK_14", "id": 0}, "to": {"map": "SBK_14", "id": 2}, "reqs": []}, #? N2E1 (Tweester A) Exit West -> N2E1 (Tweester A) Exit North
    {"from": {"map": "SBK_14", "id": 2}, "to": {"map": "SBK_14", "id": 0}, "reqs": []}, #? N2E1 (Tweester A) Exit North -> N2E1 (Tweester A) Exit West
    {"from": {"map": "SBK_14", "id": 0}, "to": {"map": "SBK_14", "id": 3}, "reqs": []}, #? N2E1 (Tweester A) Exit West -> N2E1 (Tweester A) Exit South
    {"from": {"map": "SBK_14", "id": 3}, "to": {"map": "SBK_14", "id": 0}, "reqs": []}, #? N2E1 (Tweester A) Exit South -> N2E1 (Tweester A) Exit West
    {"from": {"map": "SBK_14", "id": 0}, "to": {"map": "SBK_14", "id": 4}, "reqs": []}, #? N2E1 (Tweester A) Exit West -> N2E1 (Tweester A) Tweester
    {"from": {"map": "SBK_14", "id": 4}, "to": {"map": "SBK_14", "id": 0}, "reqs": []}, #? N2E1 (Tweester A) Tweester -> N2E1 (Tweester A) Exit West
    
    {"from": {"map": "SBK_14", "id": 0},         "to": {"map": "SBK_14", "id": "YBlockA"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N2E1 (Tweester A) Exit West -> YBlockA (Coin)
    {"from": {"map": "SBK_14", "id": "YBlockA"}, "to": {"map": "SBK_14", "id": 0},         "reqs": []}, #* YBlockA (Coin) -> N2E1 (Tweester A) Exit West
    {"from": {"map": "SBK_14", "id": 0},         "to": {"map": "SBK_14", "id": "YBlockB"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N2E1 (Tweester A) Exit West -> YBlockB (HoneySyrup)
    {"from": {"map": "SBK_14", "id": "YBlockB"}, "to": {"map": "SBK_14", "id": 0},         "reqs": []}, #* YBlockB (HoneySyrup) -> N2E1 (Tweester A) Exit West

    # SBK_15 N2E2
    {"from": {"map": "SBK_15", "id": 0}, "to": {"map": "SBK_14", "id": 1}, "reqs": []}, # N2E2 Exit West -> N2E1 (Tweester A) Exit East
    {"from": {"map": "SBK_15", "id": 1}, "to": {"map": "SBK_16", "id": 0}, "reqs": []}, # N2E2 Exit East -> N2E3 Exit West
    {"from": {"map": "SBK_15", "id": 2}, "to": {"map": "SBK_05", "id": 3}, "reqs": []}, # N2E2 Exit North -> N3E2 Pokey Army Exit South
    {"from": {"map": "SBK_15", "id": 3}, "to": {"map": "SBK_25", "id": 2}, "reqs": []}, # N2E2 Exit South -> N1E2 Exit North
    
    {"from": {"map": "SBK_15", "id": 0}, "to": {"map": "SBK_15", "id": 1}, "reqs": []}, #? N2E2 Exit West -> N2E2 Exit East
    {"from": {"map": "SBK_15", "id": 1}, "to": {"map": "SBK_15", "id": 0}, "reqs": []}, #? N2E2 Exit East -> N2E2 Exit West
    {"from": {"map": "SBK_15", "id": 0}, "to": {"map": "SBK_15", "id": 2}, "reqs": []}, #? N2E2 Exit West -> N2E2 Exit North
    {"from": {"map": "SBK_15", "id": 2}, "to": {"map": "SBK_15", "id": 0}, "reqs": []}, #? N2E2 Exit North -> N2E2 Exit West
    {"from": {"map": "SBK_15", "id": 0}, "to": {"map": "SBK_15", "id": 3}, "reqs": []}, #? N2E2 Exit West -> N2E2 Exit South
    {"from": {"map": "SBK_15", "id": 3}, "to": {"map": "SBK_15", "id": 0}, "reqs": []}, #? N2E2 Exit South -> N2E2 Exit West

    # SBK_16 N2E3
    {"from": {"map": "SBK_16", "id": 0}, "to": {"map": "SBK_15", "id": 1}, "reqs": []}, # N2E3 Exit West -> N2E2 Exit East
    {"from": {"map": "SBK_16", "id": 2}, "to": {"map": "SBK_06", "id": 3}, "reqs": []}, # N2E3 Exit North -> N3E3 Exit South
    {"from": {"map": "SBK_16", "id": 3}, "to": {"map": "SBK_26", "id": 2}, "reqs": []}, # N2E3 Exit South -> N1E3 Exit North
    
    {"from": {"map": "SBK_16", "id": 0}, "to": {"map": "SBK_16", "id": 2}, "reqs": []}, #? N2E3 Exit West -> N2E3 Exit North
    {"from": {"map": "SBK_16", "id": 2}, "to": {"map": "SBK_16", "id": 0}, "reqs": []}, #? N2E3 Exit North -> N2E3 Exit West
    {"from": {"map": "SBK_16", "id": 0}, "to": {"map": "SBK_16", "id": 3}, "reqs": []}, #? N2E3 Exit West -> N2E3 Exit South
    {"from": {"map": "SBK_16", "id": 3}, "to": {"map": "SBK_16", "id": 0}, "reqs": []}, #? N2E3 Exit South -> N2E3 Exit West

    # SBK_20 N1W3 Special Block
    {"from": {"map": "SBK_20", "id": 1}, "to": {"map": "SBK_21", "id": 0}, "reqs": []}, # N1W3 Special Block Exit East -> N1W2 Exit West
    {"from": {"map": "SBK_20", "id": 2}, "to": {"map": "SBK_10", "id": 3}, "reqs": []}, # N1W3 Special Block Exit North -> N2W3 Exit South
    {"from": {"map": "SBK_20", "id": 3}, "to": {"map": "SBK_30", "id": 2}, "reqs": []}, # N1W3 Special Block Exit South -> W3 Kolorado's Camp Exit North
    
    {"from": {"map": "SBK_20", "id": 1}, "to": {"map": "SBK_20", "id": 2}, "reqs": []}, #? N1W3 Special Block Exit East -> N1W3 Special Block Exit North
    {"from": {"map": "SBK_20", "id": 2}, "to": {"map": "SBK_20", "id": 1}, "reqs": []}, #? N1W3 Special Block Exit North -> N1W3 Special Block Exit East
    {"from": {"map": "SBK_20", "id": 1}, "to": {"map": "SBK_20", "id": 3}, "reqs": []}, #? N1W3 Special Block Exit East -> N1W3 Special Block Exit South
    {"from": {"map": "SBK_20", "id": 3}, "to": {"map": "SBK_20", "id": 1}, "reqs": []}, #? N1W3 Special Block Exit South -> N1W3 Special Block Exit East
    
    {"from": {"map": "SBK_20", "id": 1},         "to": {"map": "SBK_20", "id": "YBlockA"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N1W3 Special Block Exit East -> YBlockA (Mushroom)
    {"from": {"map": "SBK_20", "id": "YBlockA"}, "to": {"map": "SBK_20", "id": 1},         "reqs": []}, #* YBlockA (Mushroom) -> N1W3 Special Block Exit East
    {"from": {"map": "SBK_20", "id": 1},         "to": {"map": "SBK_20", "id": "YBlockB"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N1W3 Special Block Exit East -> YBlockB (SuperShroom)
    {"from": {"map": "SBK_20", "id": "YBlockB"}, "to": {"map": "SBK_20", "id": 1},         "reqs": []}, #* YBlockB (SuperShroom) -> N1W3 Special Block Exit East
    {"from": {"map": "SBK_20", "id": 1},         "to": {"map": "SBK_20", "id": "YBlockC"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N1W3 Special Block Exit East -> YBlockC (UltraShroom)
    {"from": {"map": "SBK_20", "id": "YBlockC"}, "to": {"map": "SBK_20", "id": 1},         "reqs": []}, #* YBlockC (UltraShroom) -> N1W3 Special Block Exit East

    # SBK_21 N1W2
    {"from": {"map": "SBK_21", "id": 0}, "to": {"map": "SBK_20", "id": 1}, "reqs": []}, # N1W2 Exit West -> N1W3 Special Block Exit East
    {"from": {"map": "SBK_21", "id": 1}, "to": {"map": "SBK_22", "id": 0}, "reqs": []}, # N1W2 Exit East -> N1W1 Exit West
    {"from": {"map": "SBK_21", "id": 2}, "to": {"map": "SBK_11", "id": 3}, "reqs": []}, # N1W2 Exit North -> N2W2 Exit South
    {"from": {"map": "SBK_21", "id": 3}, "to": {"map": "SBK_31", "id": 2}, "reqs": []}, # N1W2 Exit South -> W2 Exit North
    
    {"from": {"map": "SBK_21", "id": 0}, "to": {"map": "SBK_21", "id": 1}, "reqs": []}, #? N1W2 Exit West -> N1W2 Exit East
    {"from": {"map": "SBK_21", "id": 1}, "to": {"map": "SBK_21", "id": 0}, "reqs": []}, #? N1W2 Exit East -> N1W2 Exit West
    {"from": {"map": "SBK_21", "id": 0}, "to": {"map": "SBK_21", "id": 2}, "reqs": []}, #? N1W2 Exit West -> N1W2 Exit North
    {"from": {"map": "SBK_21", "id": 2}, "to": {"map": "SBK_21", "id": 0}, "reqs": []}, #? N1W2 Exit North -> N1W2 Exit West
    {"from": {"map": "SBK_21", "id": 0}, "to": {"map": "SBK_21", "id": 3}, "reqs": []}, #? N1W2 Exit West -> N1W2 Exit South
    {"from": {"map": "SBK_21", "id": 3}, "to": {"map": "SBK_21", "id": 0}, "reqs": []}, #? N1W2 Exit South -> N1W2 Exit West

    # SBK_22 N1W1
    {"from": {"map": "SBK_22", "id": 0}, "to": {"map": "SBK_21", "id": 1}, "reqs": []}, # N1W1 Exit West -> N1W2 Exit East
    {"from": {"map": "SBK_22", "id": 1}, "to": {"map": "SBK_23", "id": 0}, "reqs": []}, # N1W1 Exit East -> N1 (Tweester B) Exit West
    {"from": {"map": "SBK_22", "id": 2}, "to": {"map": "SBK_12", "id": 3}, "reqs": []}, # N1W1 Exit North -> N2W1 Exit South
    {"from": {"map": "SBK_22", "id": 3}, "to": {"map": "SBK_32", "id": 2}, "reqs": []}, # N1W1 Exit South -> W1 Exit North
    
    {"from": {"map": "SBK_22", "id": 0}, "to": {"map": "SBK_22", "id": 1}, "reqs": []}, #? N1W1 Exit West -> N1W1 Exit East
    {"from": {"map": "SBK_22", "id": 1}, "to": {"map": "SBK_22", "id": 0}, "reqs": []}, #? N1W1 Exit East -> N1W1 Exit West
    {"from": {"map": "SBK_22", "id": 0}, "to": {"map": "SBK_22", "id": 2}, "reqs": []}, #? N1W1 Exit West -> N1W1 Exit North
    {"from": {"map": "SBK_22", "id": 2}, "to": {"map": "SBK_22", "id": 0}, "reqs": []}, #? N1W1 Exit North -> N1W1 Exit West
    {"from": {"map": "SBK_22", "id": 0}, "to": {"map": "SBK_22", "id": 3}, "reqs": []}, #? N1W1 Exit West -> N1W1 Exit South
    {"from": {"map": "SBK_22", "id": 3}, "to": {"map": "SBK_22", "id": 0}, "reqs": []}, #? N1W1 Exit South -> N1W1 Exit West
    
    {"from": {"map": "SBK_22", "id": 0},         "to": {"map": "SBK_22", "id": "YBlockA"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N1W1 Exit West -> YBlockA (Coin)
    {"from": {"map": "SBK_22", "id": "YBlockA"}, "to": {"map": "SBK_22", "id": 0},         "reqs": []}, #* YBlockA (Coin) -> N1W1 Exit West
    {"from": {"map": "SBK_22", "id": 0},         "to": {"map": "SBK_22", "id": "YBlockB"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N1W1 Exit West -> YBlockB (Coin)
    {"from": {"map": "SBK_22", "id": "YBlockB"}, "to": {"map": "SBK_22", "id": 0},         "reqs": []}, #* YBlockB (Coin) -> N1W1 Exit West
    {"from": {"map": "SBK_22", "id": 0},         "to": {"map": "SBK_22", "id": "YBlockC"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N1W1 Exit West -> YBlockC (Coin)
    {"from": {"map": "SBK_22", "id": "YBlockC"}, "to": {"map": "SBK_22", "id": 0},         "reqs": []}, #* YBlockC (Coin) -> N1W1 Exit West
    {"from": {"map": "SBK_22", "id": 0},         "to": {"map": "SBK_22", "id": "YBlockD"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N1W1 Exit West -> YBlockD (Coin)
    {"from": {"map": "SBK_22", "id": "YBlockD"}, "to": {"map": "SBK_22", "id": 0},         "reqs": []}, #* YBlockD (Coin) -> N1W1 Exit West
    {"from": {"map": "SBK_22", "id": 0},         "to": {"map": "SBK_22", "id": "YBlockE"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* N1W1 Exit West -> YBlockE (FireFlower)
    {"from": {"map": "SBK_22", "id": "YBlockE"}, "to": {"map": "SBK_22", "id": 0},         "reqs": []}, #* YBlockE (FireFlower) -> N1W1 Exit West

    # SBK_23 N1 (Tweester B)
    {"from": {"map": "SBK_23", "id": 0}, "to": {"map": "SBK_22", "id": 1}, "reqs": []}, # N1 (Tweester B) Exit West -> N1W1 Exit East
    {"from": {"map": "SBK_23", "id": 1}, "to": {"map": "SBK_24", "id": 0}, "reqs": []}, # N1 (Tweester B) Exit East -> N1E1 Palm Trio Exit West
    {"from": {"map": "SBK_23", "id": 2}, "to": {"map": "SBK_13", "id": 3}, "reqs": []}, # N1 (Tweester B) Exit North -> N2 Exit South
    {"from": {"map": "SBK_23", "id": 3}, "to": {"map": "SBK_33", "id": 2}, "reqs": []}, # N1 (Tweester B) Exit South -> Center (Tweester C)
    {"from": {"map": "SBK_23", "id": 4}, "to": {"map": "SBK_14", "id": 4}, "reqs": []}, # N1 (Tweester B) Tweester -> N2E1 (Tweester A) Fall From Sky
    
    {"from": {"map": "SBK_23", "id": 0}, "to": {"map": "SBK_23", "id": 1}, "reqs": []}, #? N1 (Tweester B) Exit West -> N1 (Tweester B) Exit East
    {"from": {"map": "SBK_23", "id": 1}, "to": {"map": "SBK_23", "id": 0}, "reqs": []}, #? N1 (Tweester B) Exit East -> N1 (Tweester B) Exit West
    {"from": {"map": "SBK_23", "id": 0}, "to": {"map": "SBK_23", "id": 2}, "reqs": []}, #? N1 (Tweester B) Exit West -> N1 (Tweester B) Exit North
    {"from": {"map": "SBK_23", "id": 2}, "to": {"map": "SBK_23", "id": 0}, "reqs": []}, #? N1 (Tweester B) Exit North -> N1 (Tweester B) Exit West
    {"from": {"map": "SBK_23", "id": 0}, "to": {"map": "SBK_23", "id": 3}, "reqs": []}, #? N1 (Tweester B) Exit West -> N1 (Tweester B) Exit South
    {"from": {"map": "SBK_23", "id": 3}, "to": {"map": "SBK_23", "id": 0}, "reqs": []}, #? N1 (Tweester B) Exit South -> N1 (Tweester B) Exit West
    {"from": {"map": "SBK_23", "id": 0}, "to": {"map": "SBK_23", "id": 4}, "reqs": []}, #? N1 (Tweester B) Exit West -> N1 (Tweester B) Tweester
    {"from": {"map": "SBK_23", "id": 4}, "to": {"map": "SBK_23", "id": 0}, "reqs": []}, #? N1 (Tweester B) Tweester -> N1 (Tweester B) Exit West

    # SBK_24 N1E1 Palm Trio
    {"from": {"map": "SBK_24", "id": 0}, "to": {"map": "SBK_23", "id": 1}, "reqs": []}, # N1E1 Palm Trio Exit West -> N1 (Tweester B) Exit East
    {"from": {"map": "SBK_24", "id": 1}, "to": {"map": "SBK_25", "id": 0}, "reqs": []}, # N1E1 Palm Trio Exit East -> N1E2 Exit West
    {"from": {"map": "SBK_24", "id": 2}, "to": {"map": "SBK_14", "id": 3}, "reqs": []}, # N1E1 Palm Trio Exit North -> N2E1 (Tweester A) Exit South
    {"from": {"map": "SBK_24", "id": 3}, "to": {"map": "SBK_34", "id": 2}, "reqs": []}, # N1E1 Palm Trio Exit South -> E1 Nomadimouse Exit North
    {"from": {"map": "SBK_24", "id": 4}, "to": {"map": None, "id": None},  "reqs": []}, # N1E1 Palm Trio Fall From Sky
    
    {"from": {"map": "SBK_24", "id": 0}, "to": {"map": "SBK_24", "id": 1}, "reqs": []}, #? N1E1 Palm Trio Exit West -> N1E1 Palm Trio Exit East
    {"from": {"map": "SBK_24", "id": 1}, "to": {"map": "SBK_24", "id": 0}, "reqs": []}, #? N1E1 Palm Trio Exit East -> N1E1 Palm Trio Exit West
    {"from": {"map": "SBK_24", "id": 0}, "to": {"map": "SBK_24", "id": 2}, "reqs": []}, #? N1E1 Palm Trio Exit West -> N1E1 Palm Trio Exit North
    {"from": {"map": "SBK_24", "id": 2}, "to": {"map": "SBK_24", "id": 0}, "reqs": []}, #? N1E1 Palm Trio Exit North -> N1E1 Palm Trio Exit West
    {"from": {"map": "SBK_24", "id": 0}, "to": {"map": "SBK_24", "id": 3}, "reqs": []}, #? N1E1 Palm Trio Exit West -> N1E1 Palm Trio Exit South
    {"from": {"map": "SBK_24", "id": 3}, "to": {"map": "SBK_24", "id": 0}, "reqs": []}, #? N1E1 Palm Trio Exit South -> N1E1 Palm Trio Exit West
    {"from": {"map": "SBK_24", "id": 0}, "to": {"map": "SBK_24", "id": 4}, "reqs": []}, #? N1E1 Palm Trio Exit West -> N1E1 Palm Trio Fall From Sky
    {"from": {"map": "SBK_24", "id": 4}, "to": {"map": "SBK_24", "id": 0}, "reqs": []}, #? N1E1 Palm Trio Fall From Sky -> N1E1 Palm Trio Exit West
    
    {"from": {"map": "SBK_24", "id": 0},               "to": {"map": "SBK_24", "id": "HiddenRBlockA"}, "reqs": [require(partner="Watt",flag="RF_HiddenBlocksVisible")]}, #* N1E1 Palm Trio Exit West -> HiddenRBlockA (RunawayPay)
    {"from": {"map": "SBK_24", "id": "HiddenRBlockA"}, "to": {"map": "SBK_24", "id": 0},               "reqs": []}, #* HiddenRBlockA (RunawayPay) -> N1E1 Palm Trio Exit West

    # SBK_25 N1E2
    {"from": {"map": "SBK_25", "id": 0}, "to": {"map": "SBK_24", "id": 1}, "reqs": []}, # N1E2 Exit West -> N1E1 Palm Trio Exit East
    {"from": {"map": "SBK_25", "id": 1}, "to": {"map": "SBK_26", "id": 0}, "reqs": []}, # N1E2 Exit East -> N1E3 Exit West
    {"from": {"map": "SBK_25", "id": 2}, "to": {"map": "SBK_15", "id": 3}, "reqs": []}, # N1E2 Exit North -> N2E2 Exit South
    {"from": {"map": "SBK_25", "id": 3}, "to": {"map": "SBK_35", "id": 2}, "reqs": []}, # N1E2 Exit South -> E2 Exit North
    
    {"from": {"map": "SBK_25", "id": 0}, "to": {"map": "SBK_25", "id": 1}, "reqs": []}, #? N1E2 Exit West -> N1E2 Exit East
    {"from": {"map": "SBK_25", "id": 1}, "to": {"map": "SBK_25", "id": 0}, "reqs": []}, #? N1E2 Exit East -> N1E2 Exit West
    {"from": {"map": "SBK_25", "id": 0}, "to": {"map": "SBK_25", "id": 2}, "reqs": []}, #? N1E2 Exit West -> N1E2 Exit North
    {"from": {"map": "SBK_25", "id": 2}, "to": {"map": "SBK_25", "id": 0}, "reqs": []}, #? N1E2 Exit North -> N1E2 Exit West
    {"from": {"map": "SBK_25", "id": 0}, "to": {"map": "SBK_25", "id": 3}, "reqs": []}, #? N1E2 Exit West -> N1E2 Exit South
    {"from": {"map": "SBK_25", "id": 3}, "to": {"map": "SBK_25", "id": 0}, "reqs": []}, #? N1E2 Exit South -> N1E2 Exit West

    # SBK_26 N1E3
    {"from": {"map": "SBK_26", "id": 0}, "to": {"map": "SBK_25", "id": 1}, "reqs": []}, # N1E3 Exit West -> N1E2 Exit East
    {"from": {"map": "SBK_26", "id": 2}, "to": {"map": "SBK_16", "id": 3}, "reqs": []}, # N1E3 Exit North -> N2E3 Exit South
    {"from": {"map": "SBK_26", "id": 3}, "to": {"map": "SBK_36", "id": 2}, "reqs": []}, # N1E3 Exit South -> E3 Outside Outpost Exit North
    
    {"from": {"map": "SBK_26", "id": 0}, "to": {"map": "SBK_26", "id": 2}, "reqs": []}, #? N1E3 Exit West -> N1E3 Exit North
    {"from": {"map": "SBK_26", "id": 2}, "to": {"map": "SBK_26", "id": 0}, "reqs": []}, #? N1E3 Exit North -> N1E3 Exit West
    {"from": {"map": "SBK_26", "id": 0}, "to": {"map": "SBK_26", "id": 3}, "reqs": []}, #? N1E3 Exit West -> N1E3 Exit South
    {"from": {"map": "SBK_26", "id": 3}, "to": {"map": "SBK_26", "id": 0}, "reqs": []}, #? N1E3 Exit South -> N1E3 Exit West

    # SBK_30 W3 Kolorado's Camp
    {"from": {"map": "SBK_30", "id": 0}, "to": {"map": "SBK_99", "id": 1}, "reqs": []}, # W3 Kolorado's Camp Exit West -> Entrance Exit East
    {"from": {"map": "SBK_30", "id": 1}, "to": {"map": "SBK_31", "id": 0}, "reqs": []}, # W3 Kolorado's Camp Exit East -> W2 Exit West
    {"from": {"map": "SBK_30", "id": 2}, "to": {"map": "SBK_20", "id": 3}, "reqs": []}, # W3 Kolorado's Camp Exit North -> N1W3 Special Block Exit South
    {"from": {"map": "SBK_30", "id": 3}, "to": {"map": "SBK_40", "id": 2}, "reqs": []}, # W3 Kolorado's Camp Exit South -> S1W3 Exit North
    
    {"from": {"map": "SBK_30", "id": 0}, "to": {"map": "SBK_30", "id": 1}, "reqs": []}, #? W3 Kolorado's Camp Exit West -> W3 Kolorado's Camp Exit East
    {"from": {"map": "SBK_30", "id": 1}, "to": {"map": "SBK_30", "id": 0}, "reqs": []}, #? W3 Kolorado's Camp Exit East -> W3 Kolorado's Camp Exit West
    {"from": {"map": "SBK_30", "id": 0}, "to": {"map": "SBK_30", "id": 2}, "reqs": []}, #? W3 Kolorado's Camp Exit West -> W3 Kolorado's Camp Exit North
    {"from": {"map": "SBK_30", "id": 2}, "to": {"map": "SBK_30", "id": 0}, "reqs": []}, #? W3 Kolorado's Camp Exit North -> W3 Kolorado's Camp Exit West
    {"from": {"map": "SBK_30", "id": 0}, "to": {"map": "SBK_30", "id": 3}, "reqs": []}, #? W3 Kolorado's Camp Exit West -> W3 Kolorado's Camp Exit South
    {"from": {"map": "SBK_30", "id": 3}, "to": {"map": "SBK_30", "id": 0}, "reqs": []}, #? W3 Kolorado's Camp Exit South -> W3 Kolorado's Camp Exit West
    
    {"from": {"map": "SBK_30", "id": 0},              "to": {"map": "SBK_30", "id": "Tree2_Drop1A"}, "reqs": [require(flag="RF_Ch2_SavedStarSpirit"), can_shake_trees]}, #* W3 Kolorado's Camp Exit West -> Tree2_Drop1A (Letter02)
    {"from": {"map": "SBK_30", "id": "Tree2_Drop1A"}, "to": {"map": "SBK_30", "id": 0},              "reqs": []}, #* Tree2_Drop1A (Letter02) -> W3 Kolorado's Camp Exit West

    {"from": {"map": "SBK_30", "id": 0}, "to": {"map": "SBK_30", "id": 0}, "reqs": [], "pseudoitems": ["RF_CanVisitDesertCamp"]}, #+ Can trade Artifact in camp

    # SBK_31 W2
    {"from": {"map": "SBK_31", "id": 0}, "to": {"map": "SBK_30", "id": 1}, "reqs": []}, # W2 Exit West -> W3 Kolorado's Camp Exit East
    {"from": {"map": "SBK_31", "id": 1}, "to": {"map": "SBK_32", "id": 0}, "reqs": []}, # W2 Exit East -> W1 Exit West
    {"from": {"map": "SBK_31", "id": 2}, "to": {"map": "SBK_21", "id": 3}, "reqs": []}, # W2 Exit North -> N1W2 Exit South
    {"from": {"map": "SBK_31", "id": 3}, "to": {"map": "SBK_41", "id": 2}, "reqs": []}, # W2 Exit South -> S1W2 (Tweester D)
    
    {"from": {"map": "SBK_31", "id": 0}, "to": {"map": "SBK_31", "id": 1}, "reqs": []}, #? W2 Exit West -> W2 Exit East
    {"from": {"map": "SBK_31", "id": 1}, "to": {"map": "SBK_31", "id": 0}, "reqs": []}, #? W2 Exit East -> W2 Exit West
    {"from": {"map": "SBK_31", "id": 0}, "to": {"map": "SBK_31", "id": 2}, "reqs": []}, #? W2 Exit West -> W2 Exit North
    {"from": {"map": "SBK_31", "id": 2}, "to": {"map": "SBK_31", "id": 0}, "reqs": []}, #? W2 Exit North -> W2 Exit West
    {"from": {"map": "SBK_31", "id": 0}, "to": {"map": "SBK_31", "id": 3}, "reqs": []}, #? W2 Exit West -> W2 Exit South
    {"from": {"map": "SBK_31", "id": 3}, "to": {"map": "SBK_31", "id": 0}, "reqs": []}, #? W2 Exit South -> W2 Exit West

    # SBK_32 W1
    {"from": {"map": "SBK_32", "id": 0}, "to": {"map": "SBK_31", "id": 1}, "reqs": []}, # W1 Exit West -> W2 Exit East
    {"from": {"map": "SBK_32", "id": 1}, "to": {"map": "SBK_33", "id": 0}, "reqs": []}, # W1 Exit East -> Center (Tweester C) Exit West
    {"from": {"map": "SBK_32", "id": 2}, "to": {"map": "SBK_22", "id": 3}, "reqs": []}, # W1 Exit North -> N1W1 Exit South
    {"from": {"map": "SBK_32", "id": 3}, "to": {"map": "SBK_42", "id": 2}, "reqs": []}, # W1 Exit South -> S1W1 Exit North
    {"from": {"map": "SBK_32", "id": 4}, "to": {"map": None, "id": None}, "reqs": []},  # W1 Fall From Sky
    
    {"from": {"map": "SBK_32", "id": 0}, "to": {"map": "SBK_32", "id": 1}, "reqs": []}, #? W1 Exit West -> W1 Exit East
    {"from": {"map": "SBK_32", "id": 1}, "to": {"map": "SBK_32", "id": 0}, "reqs": []}, #? W1 Exit East -> W1 Exit West
    {"from": {"map": "SBK_32", "id": 0}, "to": {"map": "SBK_32", "id": 2}, "reqs": []}, #? W1 Exit West -> W1 Exit North
    {"from": {"map": "SBK_32", "id": 2}, "to": {"map": "SBK_32", "id": 0}, "reqs": []}, #? W1 Exit North -> W1 Exit West
    {"from": {"map": "SBK_32", "id": 0}, "to": {"map": "SBK_32", "id": 3}, "reqs": []}, #? W1 Exit West -> W1 Exit South
    {"from": {"map": "SBK_32", "id": 3}, "to": {"map": "SBK_32", "id": 0}, "reqs": []}, #? W1 Exit South -> W1 Exit West
    {"from": {"map": "SBK_32", "id": 0}, "to": {"map": "SBK_32", "id": 4}, "reqs": []}, #? W1 Exit West -> W1 Fall From Sky
    {"from": {"map": "SBK_32", "id": 4}, "to": {"map": "SBK_32", "id": 0}, "reqs": []}, #? W1 Fall From Sky -> W1 Exit West

    # SBK_33 Center (Tweester C)
    {"from": {"map": "SBK_33", "id": 0}, "to": {"map": "SBK_32", "id": 1}, "reqs": []}, # Center (Tweester C) Exit West -> W1 Exit East
    {"from": {"map": "SBK_33", "id": 1}, "to": {"map": "SBK_34", "id": 0}, "reqs": []}, # Center (Tweester C) Exit East -> E1 Nomadimouse Exit West
    {"from": {"map": "SBK_33", "id": 2}, "to": {"map": "SBK_23", "id": 3}, "reqs": []}, # Center (Tweester C) Exit North -> N1 (Tweester B) Exit South
    {"from": {"map": "SBK_33", "id": 3}, "to": {"map": "SBK_43", "id": 2}, "reqs": []}, # Center (Tweester C) Exit South -> S1 Exit North
    {"from": {"map": "SBK_33", "id": 4}, "to": {"map": "SBK_24", "id": 4}, "reqs": []}, # Center (Tweester C) Tweester -> N1E1 Palm Trio Fall From Sky
    
    {"from": {"map": "SBK_33", "id": 0}, "to": {"map": "SBK_33", "id": 1}, "reqs": []}, #? Center (Tweester C) Exit West -> Center (Tweester C) Exit East
    {"from": {"map": "SBK_33", "id": 1}, "to": {"map": "SBK_33", "id": 0}, "reqs": []}, #? Center (Tweester C) Exit East -> Center (Tweester C) Exit West
    {"from": {"map": "SBK_33", "id": 0}, "to": {"map": "SBK_33", "id": 2}, "reqs": []}, #? Center (Tweester C) Exit West -> Center (Tweester C) Exit North
    {"from": {"map": "SBK_33", "id": 2}, "to": {"map": "SBK_33", "id": 0}, "reqs": []}, #? Center (Tweester C) Exit North -> Center (Tweester C) Exit West
    {"from": {"map": "SBK_33", "id": 0}, "to": {"map": "SBK_33", "id": 3}, "reqs": []}, #? Center (Tweester C) Exit West -> Center (Tweester C) Exit South
    {"from": {"map": "SBK_33", "id": 3}, "to": {"map": "SBK_33", "id": 0}, "reqs": []}, #? Center (Tweester C) Exit South -> Center (Tweester C) Exit West
    {"from": {"map": "SBK_33", "id": 0}, "to": {"map": "SBK_33", "id": 4}, "reqs": []}, #? Center (Tweester C) Exit West -> Center (Tweester C) Tweester
    {"from": {"map": "SBK_33", "id": 4}, "to": {"map": "SBK_33", "id": 0}, "reqs": []}, #? Center (Tweester C) Tweester -> Center (Tweester C) Exit West
    
    {"from": {"map": "SBK_33", "id": 0},             "to": {"map": "SBK_33", "id": "HiddenPanel"}, "reqs": [can_flip_panels]}, #* Center (Tweester C) Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "SBK_33", "id": "HiddenPanel"}, "to": {"map": "SBK_33", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Center (Tweester C) Exit West

    # SBK_34 E1 Nomadimouse
    {"from": {"map": "SBK_34", "id": 0}, "to": {"map": "SBK_33", "id": 1}, "reqs": []}, # E1 Nomadimouse Exit West -> Center (Tweester C) Exit East
    {"from": {"map": "SBK_34", "id": 1}, "to": {"map": "SBK_35", "id": 0}, "reqs": []}, # E1 Nomadimouse Exit East -> E2 Exit West
    {"from": {"map": "SBK_34", "id": 2}, "to": {"map": "SBK_24", "id": 3}, "reqs": []}, # E1 Nomadimouse Exit North -> N1E1 Palm Trio Exit South
    {"from": {"map": "SBK_34", "id": 3}, "to": {"map": "SBK_44", "id": 2}, "reqs": []}, # E1 Nomadimouse Exit South -> S1E1 Exit North
    
    {"from": {"map": "SBK_34", "id": 0}, "to": {"map": "SBK_34", "id": 1}, "reqs": []}, #? E1 Nomadimouse Exit West -> E1 Nomadimouse Exit East
    {"from": {"map": "SBK_34", "id": 1}, "to": {"map": "SBK_34", "id": 0}, "reqs": []}, #? E1 Nomadimouse Exit East -> E1 Nomadimouse Exit West
    {"from": {"map": "SBK_34", "id": 0}, "to": {"map": "SBK_34", "id": 2}, "reqs": []}, #? E1 Nomadimouse Exit West -> E1 Nomadimouse Exit North
    {"from": {"map": "SBK_34", "id": 2}, "to": {"map": "SBK_34", "id": 0}, "reqs": []}, #? E1 Nomadimouse Exit North -> E1 Nomadimouse Exit West
    {"from": {"map": "SBK_34", "id": 0}, "to": {"map": "SBK_34", "id": 3}, "reqs": []}, #? E1 Nomadimouse Exit West -> E1 Nomadimouse Exit South
    {"from": {"map": "SBK_34", "id": 3}, "to": {"map": "SBK_34", "id": 0}, "reqs": []}, #? E1 Nomadimouse Exit South -> E1 Nomadimouse Exit West

    # SBK_35 E2
    {"from": {"map": "SBK_35", "id": 0}, "to": {"map": "SBK_34", "id": 1}, "reqs": []}, # E2 Exit West -> E1 Nomadimouse Exit East
    {"from": {"map": "SBK_35", "id": 1}, "to": {"map": "SBK_36", "id": 0}, "reqs": []}, # E2 Exit East -> E3 Outside Outpost
    {"from": {"map": "SBK_35", "id": 2}, "to": {"map": "SBK_25", "id": 3}, "reqs": []}, # E2 Exit North -> N1E2 Exit South
    {"from": {"map": "SBK_35", "id": 3}, "to": {"map": "SBK_45", "id": 2}, "reqs": []}, # E2 Exit South -> S1E2 Small Bluffs Exit North
    
    {"from": {"map": "SBK_35", "id": 0}, "to": {"map": "SBK_35", "id": 1}, "reqs": []}, #? E2 Exit West -> E2 Exit East
    {"from": {"map": "SBK_35", "id": 1}, "to": {"map": "SBK_35", "id": 0}, "reqs": []}, #? E2 Exit East -> E2 Exit West
    {"from": {"map": "SBK_35", "id": 0}, "to": {"map": "SBK_35", "id": 2}, "reqs": []}, #? E2 Exit West -> E2 Exit North
    {"from": {"map": "SBK_35", "id": 2}, "to": {"map": "SBK_35", "id": 0}, "reqs": []}, #? E2 Exit North -> E2 Exit West
    {"from": {"map": "SBK_35", "id": 0}, "to": {"map": "SBK_35", "id": 3}, "reqs": []}, #? E2 Exit West -> E2 Exit South
    {"from": {"map": "SBK_35", "id": 3}, "to": {"map": "SBK_35", "id": 0}, "reqs": []}, #? E2 Exit South -> E2 Exit West

    # SBK_36 E3 Outside Outpost
    {"from": {"map": "SBK_36", "id": 0}, "to": {"map": "SBK_35", "id": 1}, "reqs": []}, # E3 Outside Outpost Exit West -> E2 Exit East
    {"from": {"map": "SBK_36", "id": 1}, "to": {"map": "DRO_01", "id": 0}, "reqs": []}, # E3 Outside Outpost Exit East -> Outpost 1 Exit West
    {"from": {"map": "SBK_36", "id": 2}, "to": {"map": "SBK_26", "id": 3}, "reqs": []}, # E3 Outside Outpost Exit North -> N1E3 Exit South
    {"from": {"map": "SBK_36", "id": 3}, "to": {"map": "SBK_46", "id": 2}, "reqs": []}, # E3 Outside Outpost Exit South -> S1E3 North of Oasis Exit North
    
    {"from": {"map": "SBK_36", "id": 0}, "to": {"map": "SBK_36", "id": 1}, "reqs": []}, #? E3 Outside Outpost Exit West -> E3 Outside Outpost Exit East
    {"from": {"map": "SBK_36", "id": 1}, "to": {"map": "SBK_36", "id": 0}, "reqs": []}, #? E3 Outside Outpost Exit East -> E3 Outside Outpost Exit West
    {"from": {"map": "SBK_36", "id": 0}, "to": {"map": "SBK_36", "id": 2}, "reqs": []}, #? E3 Outside Outpost Exit West -> E3 Outside Outpost Exit North
    {"from": {"map": "SBK_36", "id": 2}, "to": {"map": "SBK_36", "id": 0}, "reqs": []}, #? E3 Outside Outpost Exit North -> E3 Outside Outpost Exit West
    {"from": {"map": "SBK_36", "id": 0}, "to": {"map": "SBK_36", "id": 3}, "reqs": []}, #? E3 Outside Outpost Exit West -> E3 Outside Outpost Exit South
    {"from": {"map": "SBK_36", "id": 3}, "to": {"map": "SBK_36", "id": 0}, "reqs": []}, #? E3 Outside Outpost Exit South -> E3 Outside Outpost Exit West
    
    {"from": {"map": "SBK_36", "id": 0},              "to": {"map": "SBK_36", "id": "Tree9_Drop1A"}, "reqs": [can_shake_trees]}, #* E3 Outside Outpost Exit West -> Tree9_Drop1A (Letter03)
    {"from": {"map": "SBK_36", "id": "Tree9_Drop1A"}, "to": {"map": "SBK_36", "id": 0},              "reqs": []}, #* Tree9_Drop1A (Letter03) -> E3 Outside Outpost Exit West

    # SBK_40 S1W3
    {"from": {"map": "SBK_40", "id": 1}, "to": {"map": "SBK_41", "id": 0}, "reqs": []}, # S1W3 Exit East -> S1W2 (Tweester D) Exit West
    {"from": {"map": "SBK_40", "id": 2}, "to": {"map": "SBK_30", "id": 3}, "reqs": []}, # S1W3 Exit North -> W3 Kolorado's Camp Exit South
    {"from": {"map": "SBK_40", "id": 3}, "to": {"map": "SBK_50", "id": 2}, "reqs": []}, # S1W3 Exit South -> S2W3 Exit North
    
    {"from": {"map": "SBK_40", "id": 1}, "to": {"map": "SBK_40", "id": 2}, "reqs": []}, #? S1W3 Exit East -> S1W3 Exit North
    {"from": {"map": "SBK_40", "id": 2}, "to": {"map": "SBK_40", "id": 1}, "reqs": []}, #? S1W3 Exit North -> S1W3 Exit East
    {"from": {"map": "SBK_40", "id": 1}, "to": {"map": "SBK_40", "id": 3}, "reqs": []}, #? S1W3 Exit East -> S1W3 Exit South
    {"from": {"map": "SBK_40", "id": 3}, "to": {"map": "SBK_40", "id": 1}, "reqs": []}, #? S1W3 Exit South -> S1W3 Exit East

    # SBK_41 S1W2 (Tweester D)
    {"from": {"map": "SBK_41", "id": 0}, "to": {"map": "SBK_40", "id": 1}, "reqs": []}, # S1W2 (Tweester D) Exit West -> S1W3 Exit East
    {"from": {"map": "SBK_41", "id": 1}, "to": {"map": "SBK_42", "id": 0}, "reqs": []}, # S1W2 (Tweester D) Exit East -> S1W1 Exit West
    {"from": {"map": "SBK_41", "id": 2}, "to": {"map": "SBK_31", "id": 3}, "reqs": []}, # S1W2 (Tweester D) Exit North -> W2 Exit South
    {"from": {"map": "SBK_41", "id": 3}, "to": {"map": "SBK_51", "id": 2}, "reqs": []}, # S1W2 (Tweester D) Exit South -> S2W2 Exit North
    {"from": {"map": "SBK_41", "id": 4}, "to": {"map": "SBK_32", "id": 4}, "reqs": []}, # S1W2 (Tweester D) Tweester -> W1 Fall From Sky
    
    {"from": {"map": "SBK_41", "id": 0}, "to": {"map": "SBK_41", "id": 1}, "reqs": []}, #? S1W2 (Tweester D) Exit West -> S1W2 (Tweester D) Exit East
    {"from": {"map": "SBK_41", "id": 1}, "to": {"map": "SBK_41", "id": 0}, "reqs": []}, #? S1W2 (Tweester D) Exit East -> S1W2 (Tweester D) Exit West
    {"from": {"map": "SBK_41", "id": 0}, "to": {"map": "SBK_41", "id": 2}, "reqs": []}, #? S1W2 (Tweester D) Exit West -> S1W2 (Tweester D) Exit North
    {"from": {"map": "SBK_41", "id": 2}, "to": {"map": "SBK_41", "id": 0}, "reqs": []}, #? S1W2 (Tweester D) Exit North -> S1W2 (Tweester D) Exit West
    {"from": {"map": "SBK_41", "id": 0}, "to": {"map": "SBK_41", "id": 3}, "reqs": []}, #? S1W2 (Tweester D) Exit West -> S1W2 (Tweester D) Exit South
    {"from": {"map": "SBK_41", "id": 3}, "to": {"map": "SBK_41", "id": 0}, "reqs": []}, #? S1W2 (Tweester D) Exit South -> S1W2 (Tweester D) Exit West
    {"from": {"map": "SBK_41", "id": 0}, "to": {"map": "SBK_41", "id": 4}, "reqs": []}, #? S1W2 (Tweester D) Exit West -> S1W2 (Tweester D) Tweester
    {"from": {"map": "SBK_41", "id": 4}, "to": {"map": "SBK_41", "id": 0}, "reqs": []}, #? S1W2 (Tweester D) Tweester -> S1W2 (Tweester D) Exit West

    # SBK_42 S1W1
    {"from": {"map": "SBK_42", "id": 0}, "to": {"map": "SBK_41", "id": 1}, "reqs": []}, # S1W1 Exit West -> S1W2 (Tweester D) Exit East
    {"from": {"map": "SBK_42", "id": 1}, "to": {"map": "SBK_43", "id": 0}, "reqs": []}, # S1W1 Exit East -> S1 Exit West
    {"from": {"map": "SBK_42", "id": 2}, "to": {"map": "SBK_32", "id": 3}, "reqs": []}, # S1W1 Exit North -> W1 Exit South
    {"from": {"map": "SBK_42", "id": 3}, "to": {"map": "SBK_52", "id": 2}, "reqs": []}, # S1W1 Exit South -> S2W1 Exit North
    
    {"from": {"map": "SBK_42", "id": 0}, "to": {"map": "SBK_42", "id": 1}, "reqs": []}, #? S1W1 Exit West -> S1W1 Exit East
    {"from": {"map": "SBK_42", "id": 1}, "to": {"map": "SBK_42", "id": 0}, "reqs": []}, #? S1W1 Exit East -> S1W1 Exit West
    {"from": {"map": "SBK_42", "id": 0}, "to": {"map": "SBK_42", "id": 2}, "reqs": []}, #? S1W1 Exit West -> S1W1 Exit North
    {"from": {"map": "SBK_42", "id": 2}, "to": {"map": "SBK_42", "id": 0}, "reqs": []}, #? S1W1 Exit North -> S1W1 Exit West
    {"from": {"map": "SBK_42", "id": 0}, "to": {"map": "SBK_42", "id": 3}, "reqs": []}, #? S1W1 Exit West -> S1W1 Exit South
    {"from": {"map": "SBK_42", "id": 3}, "to": {"map": "SBK_42", "id": 0}, "reqs": []}, #? S1W1 Exit South -> S1W1 Exit West

    # SBK_43 S1
    {"from": {"map": "SBK_43", "id": 0}, "to": {"map": "SBK_42", "id": 1}, "reqs": []}, # S1 Exit West -> S1W1 Exit East
    {"from": {"map": "SBK_43", "id": 1}, "to": {"map": "SBK_44", "id": 0}, "reqs": []}, # S1 Exit East -> S1E1 Exit West
    {"from": {"map": "SBK_43", "id": 2}, "to": {"map": "SBK_33", "id": 3}, "reqs": []}, # S1 Exit North -> Center (Tweester C) Exit South
    {"from": {"map": "SBK_43", "id": 3}, "to": {"map": "SBK_53", "id": 2}, "reqs": []}, # S1 Exit South -> S2 Exit North
    
    {"from": {"map": "SBK_43", "id": 0}, "to": {"map": "SBK_43", "id": 1}, "reqs": []}, #? S1 Exit West -> S1 Exit East
    {"from": {"map": "SBK_43", "id": 1}, "to": {"map": "SBK_43", "id": 0}, "reqs": []}, #? S1 Exit East -> S1 Exit West
    {"from": {"map": "SBK_43", "id": 0}, "to": {"map": "SBK_43", "id": 2}, "reqs": []}, #? S1 Exit West -> S1 Exit North
    {"from": {"map": "SBK_43", "id": 2}, "to": {"map": "SBK_43", "id": 0}, "reqs": []}, #? S1 Exit North -> S1 Exit West
    {"from": {"map": "SBK_43", "id": 0}, "to": {"map": "SBK_43", "id": 3}, "reqs": []}, #? S1 Exit West -> S1 Exit South
    {"from": {"map": "SBK_43", "id": 3}, "to": {"map": "SBK_43", "id": 0}, "reqs": []}, #? S1 Exit South -> S1 Exit West
    
    {"from": {"map": "SBK_43", "id": 0},         "to": {"map": "SBK_43", "id": "YBlockA"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* S1 Exit West -> YBlockA (Coin)
    {"from": {"map": "SBK_43", "id": "YBlockA"}, "to": {"map": "SBK_43", "id": 0},         "reqs": []}, #* YBlockA (Coin) -> S1 Exit West

    # SBK_44 S1E1
    {"from": {"map": "SBK_44", "id": 0}, "to": {"map": "SBK_43", "id": 1}, "reqs": []}, # S1E1 Exit West -> S1 Exit East
    {"from": {"map": "SBK_44", "id": 1}, "to": {"map": "SBK_45", "id": 0}, "reqs": []}, # S1E1 Exit East -> S1E2 Small Bluffs Exit West
    {"from": {"map": "SBK_44", "id": 2}, "to": {"map": "SBK_34", "id": 3}, "reqs": []}, # S1E1 Exit North -> E1 Nomadimouse Exit South
    {"from": {"map": "SBK_44", "id": 3}, "to": {"map": "SBK_54", "id": 2}, "reqs": []}, # S1E1 Exit South -> S2E1 Blue Cactus Exit North
    
    {"from": {"map": "SBK_44", "id": 0}, "to": {"map": "SBK_44", "id": 1}, "reqs": []}, #? S1E1 Exit West -> S1E1 Exit East
    {"from": {"map": "SBK_44", "id": 1}, "to": {"map": "SBK_44", "id": 0}, "reqs": []}, #? S1E1 Exit East -> S1E1 Exit West
    {"from": {"map": "SBK_44", "id": 0}, "to": {"map": "SBK_44", "id": 2}, "reqs": []}, #? S1E1 Exit West -> S1E1 Exit North
    {"from": {"map": "SBK_44", "id": 2}, "to": {"map": "SBK_44", "id": 0}, "reqs": []}, #? S1E1 Exit North -> S1E1 Exit West
    {"from": {"map": "SBK_44", "id": 0}, "to": {"map": "SBK_44", "id": 3}, "reqs": []}, #? S1E1 Exit West -> S1E1 Exit South
    {"from": {"map": "SBK_44", "id": 3}, "to": {"map": "SBK_44", "id": 0}, "reqs": []}, #? S1E1 Exit South -> S1E1 Exit West

    # SBK_45 S1E2 Small Bluffs
    {"from": {"map": "SBK_45", "id": 0}, "to": {"map": "SBK_44", "id": 1}, "reqs": []}, # S1E2 Small Bluffs Exit West -> S1E1 Exit East
    {"from": {"map": "SBK_45", "id": 1}, "to": {"map": "SBK_46", "id": 0}, "reqs": []}, # S1E2 Small Bluffs Exit East -> S1E3 North of Oasis Exit West
    {"from": {"map": "SBK_45", "id": 2}, "to": {"map": "SBK_35", "id": 3}, "reqs": []}, # S1E2 Small Bluffs Exit North -> E2 Exit South
    {"from": {"map": "SBK_45", "id": 3}, "to": {"map": "SBK_55", "id": 2}, "reqs": []}, # S1E2 Small Bluffs Exit South -> S2E2 West of Oasis Exit North
    {"from": {"map": "SBK_45", "id": 4}, "to": {"map": None, "id": None},  "reqs": []}, # S1E2 Small Bluffs Fall From Sky
    
    {"from": {"map": "SBK_45", "id": 0}, "to": {"map": "SBK_45", "id": 1}, "reqs": []}, #? S1E2 Small Bluffs Exit West -> S1E2 Small Bluffs Exit East
    {"from": {"map": "SBK_45", "id": 1}, "to": {"map": "SBK_45", "id": 0}, "reqs": []}, #? S1E2 Small Bluffs Exit East -> S1E2 Small Bluffs Exit West
    {"from": {"map": "SBK_45", "id": 0}, "to": {"map": "SBK_45", "id": 2}, "reqs": []}, #? S1E2 Small Bluffs Exit West -> S1E2 Small Bluffs Exit North
    {"from": {"map": "SBK_45", "id": 2}, "to": {"map": "SBK_45", "id": 0}, "reqs": []}, #? S1E2 Small Bluffs Exit North -> S1E2 Small Bluffs Exit West
    {"from": {"map": "SBK_45", "id": 0}, "to": {"map": "SBK_45", "id": 3}, "reqs": []}, #? S1E2 Small Bluffs Exit West -> S1E2 Small Bluffs Exit South
    {"from": {"map": "SBK_45", "id": 3}, "to": {"map": "SBK_45", "id": 0}, "reqs": []}, #? S1E2 Small Bluffs Exit South -> S1E2 Small Bluffs Exit West
    {"from": {"map": "SBK_45", "id": 4}, "to": {"map": "SBK_45", "id": 0}, "reqs": []}, #? S1E2 Small Bluffs Fall From Sky -> S1E2 Small Bluffs Exit West
    
    {"from": {"map": "SBK_45", "id": 0},       "to": {"map": "SBK_45", "id": "ItemA"}, "reqs": [require(boots=3,partner="Kooper")]}, #* S1E2 Small Bluffs Exit West -> ItemA (StopWatch)
    {"from": {"map": "SBK_45", "id": "ItemA"}, "to": {"map": "SBK_45", "id": 0},       "reqs": []}, #* ItemA (StopWatch) -> S1E2 Small Bluffs Exit West
    {"from": {"map": "SBK_45", "id": 4},       "to": {"map": "SBK_45", "id": "ItemB"}, "reqs": []}, #* S1E2 Small Bluffs Exit West -> ItemB (SpinAttack)
    {"from": {"map": "SBK_45", "id": "ItemB"}, "to": {"map": "SBK_45", "id": 4},       "reqs": []}, #* ItemB (SpinAttack) -> S1E2 Small Bluffs Exit West

    # SBK_46 S1E3 North of Oasis
    {"from": {"map": "SBK_46", "id": 0}, "to": {"map": "SBK_45", "id": 1}, "reqs": []}, # S1E3 North of Oasis Exit West -> S1E2 Small Bluffs Exit East
    {"from": {"map": "SBK_46", "id": 2}, "to": {"map": "SBK_36", "id": 3}, "reqs": []}, # S1E3 North of Oasis Exit North -> E3 Outside Outpost Exit South
    {"from": {"map": "SBK_46", "id": 3}, "to": {"map": "SBK_56", "id": 2}, "reqs": []}, # S1E3 North of Oasis Exit South -> S2E3 Oasis Exit North
    
    {"from": {"map": "SBK_46", "id": 0}, "to": {"map": "SBK_46", "id": 2}, "reqs": []}, #? S1E3 North of Oasis Exit West -> S1E3 North of Oasis Exit North
    {"from": {"map": "SBK_46", "id": 2}, "to": {"map": "SBK_46", "id": 0}, "reqs": []}, #? S1E3 North of Oasis Exit North -> S1E3 North of Oasis Exit West
    {"from": {"map": "SBK_46", "id": 0}, "to": {"map": "SBK_46", "id": 3}, "reqs": []}, #? S1E3 North of Oasis Exit West -> S1E3 North of Oasis Exit South
    {"from": {"map": "SBK_46", "id": 3}, "to": {"map": "SBK_46", "id": 0}, "reqs": []}, #? S1E3 North of Oasis Exit South -> S1E3 North of Oasis Exit West
    
    {"from": {"map": "SBK_46", "id": 0},               "to": {"map": "SBK_46", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt",flag="RF_HiddenBlocksVisible")]}, #* S1E3 North of Oasis Exit West -> HiddenYBlockA (LifeShroom)
    {"from": {"map": "SBK_46", "id": "HiddenYBlockA"}, "to": {"map": "SBK_46", "id": 0},               "reqs": []}, #* HiddenYBlockA (LifeShroom) -> S1E3 North of Oasis Exit West
    {"from": {"map": "SBK_46", "id": 0},               "to": {"map": "SBK_46", "id": "YBlockA"},       "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* S1E3 North of Oasis Exit West -> YBlockA (Coin)
    {"from": {"map": "SBK_46", "id": "YBlockA"},       "to": {"map": "SBK_46", "id": 0},               "reqs": []}, #* YBlockA (Coin) -> S1E3 North of Oasis Exit West

    # SBK_50 S2W3
    {"from": {"map": "SBK_50", "id": 1}, "to": {"map": "SBK_51", "id": 0}, "reqs": []}, # S2W3 Exit East -> S2W2 Exit West
    {"from": {"map": "SBK_50", "id": 2}, "to": {"map": "SBK_40", "id": 3}, "reqs": []}, # S2W3 Exit North -> S1W3 Exit South
    {"from": {"map": "SBK_50", "id": 3}, "to": {"map": "SBK_60", "id": 2}, "reqs": []}, # S2W3 Exit South -> S3W3 Exit North
    
    {"from": {"map": "SBK_50", "id": 1}, "to": {"map": "SBK_50", "id": 2}, "reqs": []}, #? S2W3 Exit East -> S2W3 Exit North
    {"from": {"map": "SBK_50", "id": 2}, "to": {"map": "SBK_50", "id": 1}, "reqs": []}, #? S2W3 Exit North -> S2W3 Exit East
    {"from": {"map": "SBK_50", "id": 1}, "to": {"map": "SBK_50", "id": 3}, "reqs": []}, #? S2W3 Exit East -> S2W3 Exit South
    {"from": {"map": "SBK_50", "id": 3}, "to": {"map": "SBK_50", "id": 1}, "reqs": []}, #? S2W3 Exit South -> S2W3 Exit East

    # SBK_51 S2W2
    {"from": {"map": "SBK_51", "id": 0}, "to": {"map": "SBK_50", "id": 1}, "reqs": []}, # S2W2 Exit West -> S2W3 Exit East
    {"from": {"map": "SBK_51", "id": 1}, "to": {"map": "SBK_52", "id": 0}, "reqs": []}, # S2W2 Exit East -> S2W1 Exit West
    {"from": {"map": "SBK_51", "id": 2}, "to": {"map": "SBK_41", "id": 3}, "reqs": []}, # S2W2 Exit North -> S1W2 (Tweester D) Exit South
    {"from": {"map": "SBK_51", "id": 3}, "to": {"map": "SBK_61", "id": 2}, "reqs": []}, # S2W2 Exit South -> S3W2 Hidden AttackFX Exit North
    
    {"from": {"map": "SBK_51", "id": 0}, "to": {"map": "SBK_51", "id": 1}, "reqs": []}, #? S2W2 Exit West -> S2W2 Exit East
    {"from": {"map": "SBK_51", "id": 1}, "to": {"map": "SBK_51", "id": 0}, "reqs": []}, #? S2W2 Exit East -> S2W2 Exit West
    {"from": {"map": "SBK_51", "id": 0}, "to": {"map": "SBK_51", "id": 2}, "reqs": []}, #? S2W2 Exit West -> S2W2 Exit North
    {"from": {"map": "SBK_51", "id": 2}, "to": {"map": "SBK_51", "id": 0}, "reqs": []}, #? S2W2 Exit North -> S2W2 Exit West
    {"from": {"map": "SBK_51", "id": 0}, "to": {"map": "SBK_51", "id": 3}, "reqs": []}, #? S2W2 Exit West -> S2W2 Exit South
    {"from": {"map": "SBK_51", "id": 3}, "to": {"map": "SBK_51", "id": 0}, "reqs": []}, #? S2W2 Exit South -> S2W2 Exit West

    # SBK_52 S2W1
    {"from": {"map": "SBK_52", "id": 0}, "to": {"map": "SBK_51", "id": 1}, "reqs": []}, # S2W1 Exit West -> S2W2 Exit East
    {"from": {"map": "SBK_52", "id": 1}, "to": {"map": "SBK_53", "id": 0}, "reqs": []}, # S2W1 Exit East -> S2 Exit West
    {"from": {"map": "SBK_52", "id": 2}, "to": {"map": "SBK_42", "id": 3}, "reqs": []}, # S2W1 Exit North -> S1W1 Exit South
    {"from": {"map": "SBK_52", "id": 3}, "to": {"map": "SBK_62", "id": 2}, "reqs": []}, # S2W1 Exit South -> S3W1 Exit North
    
    {"from": {"map": "SBK_52", "id": 0}, "to": {"map": "SBK_52", "id": 1}, "reqs": []}, #? S2W1 Exit West -> S2W1 Exit East
    {"from": {"map": "SBK_52", "id": 1}, "to": {"map": "SBK_52", "id": 0}, "reqs": []}, #? S2W1 Exit East -> S2W1 Exit West
    {"from": {"map": "SBK_52", "id": 0}, "to": {"map": "SBK_52", "id": 2}, "reqs": []}, #? S2W1 Exit West -> S2W1 Exit North
    {"from": {"map": "SBK_52", "id": 2}, "to": {"map": "SBK_52", "id": 0}, "reqs": []}, #? S2W1 Exit North -> S2W1 Exit West
    {"from": {"map": "SBK_52", "id": 0}, "to": {"map": "SBK_52", "id": 3}, "reqs": []}, #? S2W1 Exit West -> S2W1 Exit South
    {"from": {"map": "SBK_52", "id": 3}, "to": {"map": "SBK_52", "id": 0}, "reqs": []}, #? S2W1 Exit South -> S2W1 Exit West

    # SBK_53 S2
    {"from": {"map": "SBK_53", "id": 0}, "to": {"map": "SBK_52", "id": 1}, "reqs": []}, # S2 Exit West -> S2W1 Exit East
    {"from": {"map": "SBK_53", "id": 1}, "to": {"map": "SBK_54", "id": 0}, "reqs": []}, # S2 Exit East -> S2E1 Blue Cactus Exit West
    {"from": {"map": "SBK_53", "id": 2}, "to": {"map": "SBK_43", "id": 3}, "reqs": []}, # S2 Exit North -> S1 Exit South
    {"from": {"map": "SBK_53", "id": 3}, "to": {"map": "SBK_63", "id": 2}, "reqs": []}, # S2 Exit South -> S3 Exit North
    
    {"from": {"map": "SBK_53", "id": 0}, "to": {"map": "SBK_53", "id": 1}, "reqs": []}, #? S2 Exit West -> S2 Exit East
    {"from": {"map": "SBK_53", "id": 1}, "to": {"map": "SBK_53", "id": 0}, "reqs": []}, #? S2 Exit East -> S2 Exit West
    {"from": {"map": "SBK_53", "id": 0}, "to": {"map": "SBK_53", "id": 2}, "reqs": []}, #? S2 Exit West -> S2 Exit North
    {"from": {"map": "SBK_53", "id": 2}, "to": {"map": "SBK_53", "id": 0}, "reqs": []}, #? S2 Exit North -> S2 Exit West
    {"from": {"map": "SBK_53", "id": 0}, "to": {"map": "SBK_53", "id": 3}, "reqs": []}, #? S2 Exit West -> S2 Exit South
    {"from": {"map": "SBK_53", "id": 3}, "to": {"map": "SBK_53", "id": 0}, "reqs": []}, #? S2 Exit South -> S2 Exit West

    # SBK_54 S2E1 Blue Cactus
    {"from": {"map": "SBK_54", "id": 0}, "to": {"map": "SBK_53", "id": 1}, "reqs": []}, # S2E1 Blue Cactus Exit West -> S2 Exit East
    {"from": {"map": "SBK_54", "id": 1}, "to": {"map": "SBK_55", "id": 0}, "reqs": []}, # S2E1 Blue Cactus Exit East -> S2E2 West of Oasis Exit West
    {"from": {"map": "SBK_54", "id": 2}, "to": {"map": "SBK_44", "id": 3}, "reqs": []}, # S2E1 Blue Cactus Exit North -> S1E1 Exit South
    {"from": {"map": "SBK_54", "id": 3}, "to": {"map": "SBK_64", "id": 2}, "reqs": []}, # S2E1 Blue Cactus Exit South -> S3E1 Exit North
    {"from": {"map": "SBK_54", "id": 4}, "to": {"map": "SBK_45", "id": 4}, "reqs": []}, # S2E1 Blue Cactus Tweester -> S1E2 Small Bluffs Fall From Sky
    
    {"from": {"map": "SBK_54", "id": 0}, "to": {"map": "SBK_54", "id": 1}, "reqs": []}, #? S2E1 Blue Cactus Exit West -> S2E1 Blue Cactus Exit East
    {"from": {"map": "SBK_54", "id": 1}, "to": {"map": "SBK_54", "id": 0}, "reqs": []}, #? S2E1 Blue Cactus Exit East -> S2E1 Blue Cactus Exit West
    {"from": {"map": "SBK_54", "id": 0}, "to": {"map": "SBK_54", "id": 2}, "reqs": []}, #? S2E1 Blue Cactus Exit West -> S2E1 Blue Cactus Exit North
    {"from": {"map": "SBK_54", "id": 2}, "to": {"map": "SBK_54", "id": 0}, "reqs": []}, #? S2E1 Blue Cactus Exit North -> S2E1 Blue Cactus Exit West
    {"from": {"map": "SBK_54", "id": 0}, "to": {"map": "SBK_54", "id": 3}, "reqs": []}, #? S2E1 Blue Cactus Exit West -> S2E1 Blue Cactus Exit South
    {"from": {"map": "SBK_54", "id": 3}, "to": {"map": "SBK_54", "id": 0}, "reqs": []}, #? S2E1 Blue Cactus Exit South -> S2E1 Blue Cactus Exit West
    {"from": {"map": "SBK_54", "id": 0}, "to": {"map": "SBK_54", "id": 4}, "reqs": []}, #? S2E1 Blue Cactus Exit West -> S2E1 Blue Cactus Tweester
    {"from": {"map": "SBK_54", "id": 4}, "to": {"map": "SBK_54", "id": 0}, "reqs": []}, #? S2E1 Blue Cactus Tweester -> S2E1 Blue Cactus Exit West

    # SBK_55 S2E2 West of Oasis
    {"from": {"map": "SBK_55", "id": 0}, "to": {"map": "SBK_54", "id": 1}, "reqs": []}, # S2E2 West of Oasis Exit West -> S2E1 Blue Cactus Exit East
    {"from": {"map": "SBK_55", "id": 1}, "to": {"map": "SBK_56", "id": 0}, "reqs": []}, # S2E2 West of Oasis Exit East -> S2E3 Oasis Exit West
    {"from": {"map": "SBK_55", "id": 2}, "to": {"map": "SBK_45", "id": 3}, "reqs": []}, # S2E2 West of Oasis Exit North -> S1E2 Small Bluffs Exit South
    {"from": {"map": "SBK_55", "id": 3}, "to": {"map": "SBK_65", "id": 2}, "reqs": []}, # S2E2 West of Oasis Exit South -> S3E2 Exit North
    
    {"from": {"map": "SBK_55", "id": 0}, "to": {"map": "SBK_55", "id": 1}, "reqs": []}, #? S2E2 West of Oasis Exit West -> S2E2 West of Oasis Exit East
    {"from": {"map": "SBK_55", "id": 1}, "to": {"map": "SBK_55", "id": 0}, "reqs": []}, #? S2E2 West of Oasis Exit East -> S2E2 West of Oasis Exit West
    {"from": {"map": "SBK_55", "id": 0}, "to": {"map": "SBK_55", "id": 2}, "reqs": []}, #? S2E2 West of Oasis Exit West -> S2E2 West of Oasis Exit North
    {"from": {"map": "SBK_55", "id": 2}, "to": {"map": "SBK_55", "id": 0}, "reqs": []}, #? S2E2 West of Oasis Exit North -> S2E2 West of Oasis Exit West
    {"from": {"map": "SBK_55", "id": 0}, "to": {"map": "SBK_55", "id": 3}, "reqs": []}, #? S2E2 West of Oasis Exit West -> S2E2 West of Oasis Exit South
    {"from": {"map": "SBK_55", "id": 3}, "to": {"map": "SBK_55", "id": 0}, "reqs": []}, #? S2E2 West of Oasis Exit South -> S2E2 West of Oasis Exit West
    
    {"from": {"map": "SBK_55", "id": 0},       "to": {"map": "SBK_55", "id": "ItemA"}, "reqs": []}, #* S2E2 West of Oasis Exit West -> ItemA (TastyTonic)
    {"from": {"map": "SBK_55", "id": "ItemA"}, "to": {"map": "SBK_55", "id": 0},       "reqs": []}, #* ItemA (TastyTonic) -> S2E2 West of Oasis Exit West

    # SBK_56 S2E3 Oasis
    {"from": {"map": "SBK_56", "id": 0}, "to": {"map": "SBK_55", "id": 1}, "reqs": []}, # S2E3 Oasis Exit West -> S2E2 West of Oasis Exit East
    {"from": {"map": "SBK_56", "id": 2}, "to": {"map": "SBK_46", "id": 3}, "reqs": []}, # S2E3 Oasis Exit North -> S1E3 North of Oasis Exit South
    {"from": {"map": "SBK_56", "id": 3}, "to": {"map": "SBK_66", "id": 2}, "reqs": []}, # S2E3 Oasis Exit South -> S3E3 South of Oasis Exit North
    
    {"from": {"map": "SBK_56", "id": 0}, "to": {"map": "SBK_56", "id": 2}, "reqs": []}, #? S2E3 Oasis Exit West -> S2E3 Oasis Exit North
    {"from": {"map": "SBK_56", "id": 2}, "to": {"map": "SBK_56", "id": 0}, "reqs": []}, #? S2E3 Oasis Exit North -> S2E3 Oasis Exit West
    {"from": {"map": "SBK_56", "id": 0}, "to": {"map": "SBK_56", "id": 3}, "reqs": []}, #? S2E3 Oasis Exit West -> S2E3 Oasis Exit South
    {"from": {"map": "SBK_56", "id": 3}, "to": {"map": "SBK_56", "id": 0}, "reqs": []}, #? S2E3 Oasis Exit South -> S2E3 Oasis Exit West
    
    {"from": {"map": "SBK_56", "id": 0},              "to": {"map": "SBK_56", "id": "Tree1_Drop1A"}, "reqs": [can_shake_trees]}, #* S2E3 Oasis Exit West -> Tree1_Drop1A (Lemon)
    {"from": {"map": "SBK_56", "id": "Tree1_Drop1A"}, "to": {"map": "SBK_56", "id": 0},              "reqs": []}, #* Tree1_Drop1A (Lemon) -> S2E3 Oasis Exit West
    {"from": {"map": "SBK_56", "id": 0},              "to": {"map": "SBK_56", "id": "Tree2_Drop1A"}, "reqs": [can_shake_trees]}, #* S2E3 Oasis Exit West -> Tree2_Drop1A (Lime)
    {"from": {"map": "SBK_56", "id": "Tree2_Drop1A"}, "to": {"map": "SBK_56", "id": 0},              "reqs": []}, #* Tree2_Drop1A (Lime) -> S2E3 Oasis Exit West

    # SBK_60 S3W3
    {"from": {"map": "SBK_60", "id": 1}, "to": {"map": "SBK_61", "id": 0}, "reqs": []}, # S3W3 Exit East -> S3W2 Hidden AttackFX Exit West
    {"from": {"map": "SBK_60", "id": 2}, "to": {"map": "SBK_50", "id": 3}, "reqs": []}, # S3W3 Exit North -> S2W3 Exit South
    
    {"from": {"map": "SBK_60", "id": 1}, "to": {"map": "SBK_60", "id": 2}, "reqs": []}, #? S3W3 Exit East -> S3W3 Exit North
    {"from": {"map": "SBK_60", "id": 2}, "to": {"map": "SBK_60", "id": 1}, "reqs": []}, #? S3W3 Exit North -> S3W3 Exit East

    # SBK_61 S3W2 Hidden AttackFX
    {"from": {"map": "SBK_61", "id": 0}, "to": {"map": "SBK_60", "id": 1}, "reqs": []}, # S3W2 Hidden AttackFX Exit West -> S3W3 Exit East
    {"from": {"map": "SBK_61", "id": 1}, "to": {"map": "SBK_62", "id": 0}, "reqs": []}, # S3W2 Hidden AttackFX Exit East -> S3W1 Exit West
    {"from": {"map": "SBK_61", "id": 2}, "to": {"map": "SBK_51", "id": 3}, "reqs": []}, # S3W2 Hidden AttackFX Exit North -> S2W2 Exit South
    
    {"from": {"map": "SBK_61", "id": 0}, "to": {"map": "SBK_61", "id": 1}, "reqs": []}, #? S3W2 Hidden AttackFX Exit West -> S3W2 Hidden AttackFX Exit East
    {"from": {"map": "SBK_61", "id": 1}, "to": {"map": "SBK_61", "id": 0}, "reqs": []}, #? S3W2 Hidden AttackFX Exit East -> S3W2 Hidden AttackFX Exit West
    {"from": {"map": "SBK_61", "id": 0}, "to": {"map": "SBK_61", "id": 2}, "reqs": []}, #? S3W2 Hidden AttackFX Exit West -> S3W2 Hidden AttackFX Exit North
    {"from": {"map": "SBK_61", "id": 2}, "to": {"map": "SBK_61", "id": 0}, "reqs": []}, #? S3W2 Hidden AttackFX Exit North -> S3W2 Hidden AttackFX Exit West
    
    {"from": {"map": "SBK_61", "id": 0},               "to": {"map": "SBK_61", "id": "HiddenRBlockA"}, "reqs": [require(partner="Watt",flag="RF_HiddenBlocksVisible")]}, #* S3W2 Hidden AttackFX Exit West -> HiddenRBlockA (AttackFXC)
    {"from": {"map": "SBK_61", "id": "HiddenRBlockA"}, "to": {"map": "SBK_61", "id": 0},               "reqs": []}, #* HiddenRBlockA (AttackFXC) -> S3W2 Hidden AttackFX Exit West

    # SBK_62 S3W1
    {"from": {"map": "SBK_62", "id": 0}, "to": {"map": "SBK_61", "id": 1}, "reqs": []}, # S3W1 Exit West -> S3W2 Hidden AttackFX Exit East
    {"from": {"map": "SBK_62", "id": 1}, "to": {"map": "SBK_63", "id": 0}, "reqs": []}, # S3W1 Exit East -> S3 Exit West
    {"from": {"map": "SBK_62", "id": 2}, "to": {"map": "SBK_52", "id": 3}, "reqs": []}, # S3W1 Exit North -> S2W1 Exit South
    
    {"from": {"map": "SBK_62", "id": 0}, "to": {"map": "SBK_62", "id": 1}, "reqs": []}, #? S3W1 Exit West -> S3W1 Exit East
    {"from": {"map": "SBK_62", "id": 1}, "to": {"map": "SBK_62", "id": 0}, "reqs": []}, #? S3W1 Exit East -> S3W1 Exit West
    {"from": {"map": "SBK_62", "id": 0}, "to": {"map": "SBK_62", "id": 2}, "reqs": []}, #? S3W1 Exit West -> S3W1 Exit North
    {"from": {"map": "SBK_62", "id": 2}, "to": {"map": "SBK_62", "id": 0}, "reqs": []}, #? S3W1 Exit North -> S3W1 Exit West

    # SBK_63 S3
    {"from": {"map": "SBK_63", "id": 0}, "to": {"map": "SBK_62", "id": 1}, "reqs": []}, # S3 Exit West -> S3W1 Exit East
    {"from": {"map": "SBK_63", "id": 1}, "to": {"map": "SBK_64", "id": 0}, "reqs": []}, # S3 Exit East -> S3E1 Exit West
    {"from": {"map": "SBK_63", "id": 2}, "to": {"map": "SBK_53", "id": 3}, "reqs": []}, # S3 Exit North -> S2 Exit South
    
    {"from": {"map": "SBK_63", "id": 0}, "to": {"map": "SBK_63", "id": 1}, "reqs": []}, #? S3 Exit West -> S3 Exit East
    {"from": {"map": "SBK_63", "id": 1}, "to": {"map": "SBK_63", "id": 0}, "reqs": []}, #? S3 Exit East -> S3 Exit West
    {"from": {"map": "SBK_63", "id": 0}, "to": {"map": "SBK_63", "id": 2}, "reqs": []}, #? S3 Exit West -> S3 Exit North
    {"from": {"map": "SBK_63", "id": 2}, "to": {"map": "SBK_63", "id": 0}, "reqs": []}, #? S3 Exit North -> S3 Exit West

    # SBK_64 S3E1
    {"from": {"map": "SBK_64", "id": 0}, "to": {"map": "SBK_63", "id": 1}, "reqs": []}, # S3E1 Exit West -> S3 Exit East
    {"from": {"map": "SBK_64", "id": 1}, "to": {"map": "SBK_65", "id": 0}, "reqs": []}, # S3E1 Exit East -> S3E2 Exit West
    {"from": {"map": "SBK_64", "id": 2}, "to": {"map": "SBK_54", "id": 3}, "reqs": []}, # S3E1 Exit North -> S2E1 Blue Cactus Exit South
    
    {"from": {"map": "SBK_64", "id": 0}, "to": {"map": "SBK_64", "id": 1}, "reqs": []}, #? S3E1 Exit West -> S3E1 Exit East
    {"from": {"map": "SBK_64", "id": 1}, "to": {"map": "SBK_64", "id": 0}, "reqs": []}, #? S3E1 Exit East -> S3E1 Exit West
    {"from": {"map": "SBK_64", "id": 0}, "to": {"map": "SBK_64", "id": 2}, "reqs": []}, #? S3E1 Exit West -> S3E1 Exit North
    {"from": {"map": "SBK_64", "id": 2}, "to": {"map": "SBK_64", "id": 0}, "reqs": []}, #? S3E1 Exit North -> S3E1 Exit West
    
    {"from": {"map": "SBK_64", "id": 0},         "to": {"map": "SBK_64", "id": "YBlockA"}, "reqs": [require(hammer=1,boots=2,partner=["Kooper","Bombette"])]}, #* S3E1 Exit West -> YBlockA (Coin)
    {"from": {"map": "SBK_64", "id": "YBlockA"}, "to": {"map": "SBK_64", "id": 0},         "reqs": []}, #* YBlockA (Coin) -> S3E1 Exit West

    # SBK_65 S3E2
    {"from": {"map": "SBK_65", "id": 0}, "to": {"map": "SBK_64", "id": 1}, "reqs": []}, # S3E2 Exit West -> S3E1 Exit East
    {"from": {"map": "SBK_65", "id": 1}, "to": {"map": "SBK_66", "id": 0}, "reqs": []}, # S3E2 Exit East -> S3E3 South of Oasis Exit West
    {"from": {"map": "SBK_65", "id": 2}, "to": {"map": "SBK_55", "id": 3}, "reqs": []}, # S3E2 Exit North -> S2E2 West of Oasis Exit South
    
    {"from": {"map": "SBK_65", "id": 0}, "to": {"map": "SBK_65", "id": 1}, "reqs": []}, #? S3E2 Exit West -> S3E2 Exit East
    {"from": {"map": "SBK_65", "id": 1}, "to": {"map": "SBK_65", "id": 0}, "reqs": []}, #? S3E2 Exit East -> S3E2 Exit West
    {"from": {"map": "SBK_65", "id": 0}, "to": {"map": "SBK_65", "id": 2}, "reqs": []}, #? S3E2 Exit West -> S3E2 Exit North
    {"from": {"map": "SBK_65", "id": 2}, "to": {"map": "SBK_65", "id": 0}, "reqs": []}, #? S3E2 Exit North -> S3E2 Exit West

    # SBK_66 S3E3 South of Oasis
    {"from": {"map": "SBK_66", "id": 0}, "to": {"map": "SBK_65", "id": 1}, "reqs": []}, # S3E3 South of Oasis Exit North -> S2E3 Oasis Exit South
    {"from": {"map": "SBK_66", "id": 2}, "to": {"map": "SBK_56", "id": 3}, "reqs": []}, # S3E3 South of Oasis Exit West -> S3E2 Exit East
    
    {"from": {"map": "SBK_66", "id": 0}, "to": {"map": "SBK_66", "id": 2}, "reqs": []}, #? S3E3 South of Oasis Exit North -> S3E3 South of Oasis Exit West
    {"from": {"map": "SBK_66", "id": 2}, "to": {"map": "SBK_66", "id": 0}, "reqs": []}, #? S3E3 South of Oasis Exit West -> S3E3 South of Oasis Exit North
    
    # SBK_99 Entrance
    {"from": {"map": "SBK_99", "id": 0}, "to": {"map": "IWA_04", "id": 1}, "reqs": []}, # Entrance Exit West -> Suspension Bridge Exit Right
    {"from": {"map": "SBK_99", "id": 1}, "to": {"map": "SBK_30", "id": 0}, "reqs": []}, # Entrance Exit East -> W3 Kolorado's Camp Exit West
    
    {"from": {"map": "SBK_99", "id": 0}, "to": {"map": "SBK_99", "id": 1}, "reqs": []}, #? Entrance Exit West -> Entrance Exit East
    {"from": {"map": "SBK_99", "id": 1}, "to": {"map": "SBK_99", "id": 0}, "reqs": []}, #? Entrance Exit East -> Entrance Exit West
]
