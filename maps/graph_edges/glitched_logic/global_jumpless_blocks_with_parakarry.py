"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Jumpless Blocks with Parakarry
"""
edges_global_jumpless_blocks_with_parakarry = [
    # KMR
    #* Goomba Road 1 Exit Right -> YBlockA (Coin)
    {"from": {"map": "KMR_09", "id": 1}, "to": {"map": "KMR_09", "id": "YBlockA"}, "reqs": [["Parakarry"]]},
    #* Goomba Road 2 Exit Left -> RBlockA (CloseCall)
    {"from": {"map": "KMR_06", "id": 0}, "to": {"map": "KMR_06", "id": "RBlockA"}, "reqs": [["Parakarry"]]},

    # NOK
    #* Pleasant Path Entry Exit Right -> YBlockA (Coin)
    {"from": {"map": "NOK_11", "id": 1}, "to": {"map": "NOK_11", "id": "YBlockA"}, "reqs": [["Parakarry"]]},
    #* Pleasant Path Entry Exit Right -> RBlockA (DizzyAttack)
    {"from": {"map": "NOK_11", "id": 1}, "to": {"map": "NOK_11", "id": "RBlockA"}, "reqs": [["Parakarry"]]},

    #* Pleasant Path Bridge Exit Left -> YBlockA (POWBlock)
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": "YBlockA"}, "reqs": [["Parakarry"]]},

    #* Path to Fortress 1 Exit Right -> HiddenYBlockA (FireFlower)
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_14", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["Parakarry"]]},

    # TIK
    #* Hall to Blooper 1 (B1) Exit Left -> RandomBlockItemA (CoinBag)
    {"from": {"map": "TIK_18", "id": 0}, "to": {"map": "TIK_18", "id": "RandomBlockItemA"}, "reqs": [["Parakarry"]]},

    #* Spring Room (B2) Exit Right -> ChestA (PowerSmash1)
    {"from": {"map": "TIK_05", "id": 0}, "to": {"map": "TIK_05", "id": "ChestA"}, "reqs": [["Parakarry"]]},

    #* Winding Path (B3) Green Pipe -> YBlockA (Coin)
    {"from": {"map": "TIK_23", "id": 1}, "to": {"map": "TIK_23", "id": "YBlockA"}, "reqs": [["Parakarry"]]},

    # IWA
    #* Mt Rugged 1 Exit Right -> YBlockA (SleepySheep)
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_00", "id": "YBlockA"}, "reqs": [["Parakarry"]]},

    #* Mt Rugged 4 Exit Bottom Right -> YBlockB (Mushroom)
    {"from": {"map": "IWA_03", "id": 0}, "to": {"map": "IWA_03", "id": "YBlockB"}, "reqs": [["Parakarry"]]},

    # SBK
    #* N3E3 Exit West -> RandomBlockItemA (CoinBag)
    {"from": {"map": "SBK_06", "id": 0}, "to": {"map": "SBK_06", "id": "RandomBlockItemA"}, "reqs": [["Parakarry"]]},

    #* N1W3 Special Block Exit East -> YBlockA (Mushroom)
    {"from": {"map": "SBK_20", "id": 1}, "to": {"map": "SBK_20", "id": "YBlockA"}, "reqs": [["can_hit_grounded_blocks"],["Parakarry"]]},

    #* N1E2 Exit West -> RandomBlockItemA (CoinBag)
    {"from": {"map": "SBK_25", "id": 0}, "to": {"map": "SBK_25", "id": "RandomBlockItemA"}, "reqs": [["Parakarry"]]},

    #* S1W3 Exit East -> RandomBlockItemA (CoinBag)
    {"from": {"map": "SBK_40", "id": 1}, "to": {"map": "SBK_40", "id": "RandomBlockItemA"}, "reqs": [["Parakarry"]]},

    #* S1E3 North of Oasis Exit West -> HiddenYBlockA (LifeShroom)
    {"from": {"map": "SBK_46", "id": 0}, "to": {"map": "SBK_46", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["Parakarry"]]},

    #* S3E3 South of Oasis Exit North -> RandomBlockItemA (CoinBag)
    {"from": {"map": "SBK_66", "id": 0}, "to": {"map": "SBK_66", "id": "RandomBlockItemA"}, "reqs": [["Parakarry"]]},

    # MIM
    #* Flowers Appear (FP Plus) Correct Exit -> RBlockA (FPPlus)
    {"from": {"map": "MIM_09", "id": 2}, "to": {"map": "MIM_09", "id": "RBlockA"}, "reqs": [["Parakarry"]]},

    # ARN
    #* Wasteland Ascent 1 Exit West -> YBlockA (Coin)
    {"from": {"map": "ARN_02", "id": 0}, "to": {"map": "ARN_02", "id": "YBlockA"}, "reqs": [["Parakarry"]]},
    #* Wasteland Ascent 1 Exit East -> YBlockB (Coin)
    {"from": {"map": "ARN_02", "id": 1}, "to": {"map": "ARN_02", "id": "YBlockB"}, "reqs": [["Parakarry"]]},

    #* Wasteland Ascent 2 Exit East -> YBlockA (SuperShroom)
    {"from": {"map": "ARN_04", "id": 1}, "to": {"map": "ARN_04", "id": "YBlockA"}, "reqs": [["Parakarry"]]},

    # OMO
    #* BLU Anti-Guy Hall Exit West -> YBlockA (Coin)
    {"from": {"map": "OMO_13", "id": 0}, "to": {"map": "OMO_13", "id": "YBlockA"}, "reqs": [["Parakarry"]]},

    #* BLU Large Playroom Exit East -> HiddenYBlockA (Mystery)
    {"from": {"map": "OMO_01", "id": 0}, "to": {"map": "OMO_01", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["Parakarry"]]},

    #* PNK Gourmet Guy Crossing Exit East (North) -> YBlockA (Coin)
    {"from": {"map": "OMO_05", "id": 1}, "to": {"map": "OMO_05", "id": "YBlockA"}, "reqs": [["Parakarry"]]},

    #* PNK Tracks Hallway Exit West (North) -> YBlockB (Coin)
    {"from": {"map": "OMO_17", "id": 1}, "to": {"map": "OMO_17", "id": "YBlockB"}, "reqs": [["Parakarry"]]},

    #* RED Moving Platforms Exit West -> YBlockA (Coin)
    {"from": {"map": "OMO_11", "id": 0}, "to": {"map": "OMO_11", "id": "YBlockA"}, "reqs": [["RF_MovingPlatformsLaki"],["Parakarry"]]},

    #* RED Boss Barricade Exit East -> YBlockA (SleepySheep)
    {"from": {"map": "OMO_02", "id": 1}, "to": {"map": "OMO_02", "id": "YBlockA"}, "reqs": [["Parakarry"]]},

    # JAN
    #* Beach Exit Left -> HiddenYBlockA (RepelGel)
    {"from": {"map": "JAN_01", "id": 0}, "to": {"map": "JAN_01", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["Parakarry"]]},

    #* SE Jungle (Quake Hammer) Exit Right-> RBlockA (PowerQuake)
    {"from": {"map": "JAN_05", "id": 2}, "to": {"map": "JAN_05", "id": "RBlockA"}, "reqs": [["Sushie"],["Parakarry"]]},

    # KZN
    #* Central Cavern Exit West Upper -> YBlockA (Coin)
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_03", "id": "YBlockA"}, "reqs": [["Parakarry"]]},

    # FLO
    #* (SE) Briar Platforming Exit Right -> RandomBlockItemA (GenericUpgrade)
    {"from": {"map": "FLO_08", "id": 1}, "to": {"map": "FLO_08", "id": "RandomBlockItemA"}, "reqs": [["Parakarry"]]},

    #* (West) Path to Maze Exit Left -> HiddenYBlockB (Coin)
    {"from": {"map": "FLO_23", "id": 1}, "to": {"map": "FLO_23", "id": "HiddenYBlockB"}, "reqs": [["can_see_hidden_blocks"],["Parakarry"]]},

    # SAM
    #+ CHAINED REQUIREMENTS Shiver Mountain Peaks -> RBlockA (MegaJump)
    {"from": {"map": "SAM_10", "id": "ItemA"}, "to": {"map": "SAM_10", "id": "RBlockA"}, "reqs": [["Parakarry"]]},

    # PRA
    #* Reflected Save Room Door West -> YBlockA (SuperShroom)
    {"from": {"map": "PRA_04", "id": 0}, "to": {"map": "PRA_04", "id": "YBlockA"}, "reqs": [["Parakarry"]]},

    # KPA
    #* Room with Hidden Door 1 Door Left -> YBlockA (SuperShroom)
    {"from": {"map": "KPA_111", "id": 0}, "to": {"map": "KPA_111", "id": "YBlockA"}, "reqs": [["Parakarry"]]},
]
