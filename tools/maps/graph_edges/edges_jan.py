"""This file represents all edges of the world graph that have origin-nodes in the JAN (Jade Jungle) area."""
edges_jan = [
    # JAN_00 Whale Cove
    {"from": {"map": "JAN_00", "id": 0}, "to": {"map": "MAC_05", "id": 1}, "reqs": []}, # Whale Cove Ride The Whale -> Port District Ride Whale
    {"from": {"map": "JAN_00", "id": 1}, "to": {"map": "JAN_01", "id": 0}, "reqs": []}, # Whale Cove Exit Bottom Right -> Beach Exit Left
    {"from": {"map": "JAN_00", "id": 2}, "to": {"map": "JAN_08", "id": 0}, "reqs": []}, # Whale Cove Exit Top Right -> SW Jungle (Super Block) Exit Bottom Left
    
    {"from": {"map": "JAN_00", "id": 0}, "to": {"map": "JAN_00", "id": 1}, "reqs": []}, #? Whale Cove Ride The Whale -> Whale Cove Exit Bottom Right
    {"from": {"map": "JAN_00", "id": 1}, "to": {"map": "JAN_00", "id": 0}, "reqs": []}, #? Whale Cove Exit Bottom Right -> Whale Cove Ride The Whale
    {"from": {"map": "JAN_00", "id": 0}, "to": {"map": "JAN_00", "id": 2}, "reqs": []}, #? Whale Cove Ride The Whale -> Whale Cove Exit Top Right
    {"from": {"map": "JAN_00", "id": 2}, "to": {"map": "JAN_00", "id": 0}, "reqs": []}, #? Whale Cove Exit Top Right -> Whale Cove Ride The Whale
    
    {"from": {"map": "JAN_00", "id": 0},       "to": {"map": "JAN_00", "id": "ItemA"}, "reqs": []}, #* Whale Cove Ride The Whale -> ItemA (Coin)
    {"from": {"map": "JAN_00", "id": "ItemA"}, "to": {"map": "JAN_00", "id": 0},       "reqs": []}, #* ItemA (Coin) -> Whale Cove Ride The Whale
    {"from": {"map": "JAN_00", "id": 0},       "to": {"map": "JAN_00", "id": "ItemB"}, "reqs": []}, #* Whale Cove Ride The Whale -> ItemB (Coin)
    {"from": {"map": "JAN_00", "id": "ItemB"}, "to": {"map": "JAN_00", "id": 0},       "reqs": []}, #* ItemB (Coin) -> Whale Cove Ride The Whale
    {"from": {"map": "JAN_00", "id": 0},       "to": {"map": "JAN_00", "id": "ItemC"}, "reqs": []}, #* Whale Cove Ride The Whale -> ItemC (StopWatch)
    {"from": {"map": "JAN_00", "id": "ItemC"}, "to": {"map": "JAN_00", "id": 0},       "reqs": []}, #* ItemC (StopWatch) -> Whale Cove Ride The Whale

    # JAN_01 Beach
    {"from": {"map": "JAN_01", "id": 0}, "to": {"map": "JAN_00", "id": 1}, "reqs": []}, # Beach Exit Left -> Whale Cove Exit Bottom Right
    {"from": {"map": "JAN_01", "id": 1}, "to": {"map": "JAN_02", "id": 0}, "reqs": []}, # Beach Exit Right -> Village Cove Exit Top Left
    
    {"from": {"map": "JAN_01", "id": 0}, "to": {"map": "JAN_01", "id": 1}, "reqs": []}, #? Beach Exit Left -> Beach Exit Right
    {"from": {"map": "JAN_01", "id": 1}, "to": {"map": "JAN_01", "id": 0}, "reqs": []}, #? Beach Exit Right -> Beach Exit Left
    
    {"from": {"map": "JAN_01", "id": 0},               "to": {"map": "JAN_01", "id": "ItemA"},         "reqs": []}, #* Beach Exit Left -> ItemA (Letter11)
    {"from": {"map": "JAN_01", "id": "ItemA"},         "to": {"map": "JAN_01", "id": 0},               "reqs": []}, #* ItemA (Letter11) -> Beach Exit Left
    {"from": {"map": "JAN_01", "id": 0},               "to": {"map": "JAN_01", "id": "ItemB"},         "reqs": []}, #* Beach Exit Left -> ItemB (Coin)
    {"from": {"map": "JAN_01", "id": "ItemB"},         "to": {"map": "JAN_01", "id": 0},               "reqs": []}, #* ItemB (Coin) -> Beach Exit Left
    {"from": {"map": "JAN_01", "id": 0},               "to": {"map": "JAN_01", "id": "ItemC"},         "reqs": []}, #* Beach Exit Left -> ItemC (Coin)
    {"from": {"map": "JAN_01", "id": "ItemC"},         "to": {"map": "JAN_01", "id": 0},               "reqs": []}, #* ItemC (Coin) -> Beach Exit Left
    {"from": {"map": "JAN_01", "id": 0},               "to": {"map": "JAN_01", "id": "HiddenYBlockA"}, "reqs": []}, #* Beach Exit Left -> HiddenYBlockA (RepelGel)
    {"from": {"map": "JAN_01", "id": "HiddenYBlockA"}, "to": {"map": "JAN_01", "id": 0},               "reqs": []}, #* HiddenYBlockA (RepelGel) -> Beach Exit Left
    {"from": {"map": "JAN_01", "id": 0},               "to": {"map": "JAN_01", "id": "HiddenYBlockB"}, "reqs": []}, #* Beach Exit Left -> HiddenYBlockB (Mystery)
    {"from": {"map": "JAN_01", "id": "HiddenYBlockB"}, "to": {"map": "JAN_01", "id": 0},               "reqs": []}, #* HiddenYBlockB (Mystery) -> Beach Exit Left

    # JAN_02 Village Cove
    {"from": {"map": "JAN_02", "id": 0}, "to": {"map": "JAN_01", "id": 1}, "reqs": []}, # Village Cove Exit Top Left -> Beach Exit Right
    {"from": {"map": "JAN_02", "id": 1}, "to": {"map": "JAN_03", "id": 0}, "reqs": []}, # Village Cove Exit Right -> Village Buildings Exit Left
    
    {"from": {"map": "JAN_02", "id": 0}, "to": {"map": "JAN_02", "id": 1}, "reqs": []}, #? Village Cove Exit Top Left -> Village Cove Exit Right
    {"from": {"map": "JAN_02", "id": 1}, "to": {"map": "JAN_02", "id": 0}, "reqs": []}, #? Village Cove Exit Right -> Village Cove Exit Top Left
    
    {"from": {"map": "JAN_02", "id": 0},             "to": {"map": "JAN_02", "id": "HiddenPanel"}, "reqs": []}, #* Village Cove Exit Top Left -> HiddenPanel (StarPiece)
    {"from": {"map": "JAN_02", "id": "HiddenPanel"}, "to": {"map": "JAN_02", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Village Cove Exit Top Left
    {"from": {"map": "JAN_02", "id": 0},             "to": {"map": "JAN_02", "id": "GiftA"},       "reqs": []}, #* Village Cove Exit Top Left -> GiftA (JadeRaven)
    {"from": {"map": "JAN_02", "id": "GiftA"},       "to": {"map": "JAN_02", "id": 0},             "reqs": []}, #* GiftA (JadeRaven) -> Village Cove Exit Top Left

    # JAN_03 Village Buildings
    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_02", "id": 1}, "reqs": []}, # Village Buildings Exit Left -> Village Cove Exit Right
    {"from": {"map": "JAN_03", "id": 1}, "to": {"map": "JAN_05", "id": 0}, "reqs": []}, # Village Buildings Exit Top Left -> SE Jungle (Quake Hammer) Exit Bottom Right
    {"from": {"map": "JAN_03", "id": 2}, "to": {"map": "JAN_22", "id": 0}, "reqs": []}, # Village Buildings Exit Right -> Path to the Volcano Exit Left
    {"from": {"map": "JAN_03", "id": 3}, "to": {"map": "TIK_08", "id": 4}, "reqs": []}, # Village Buildings Blue Warp Pipe -> Second Level Entry (B2) Blue Warp Pipe
    
    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_03", "id": 1}, "reqs": []}, #? Village Buildings Exit Left -> Village Buildings Exit Top Left
    {"from": {"map": "JAN_03", "id": 1}, "to": {"map": "JAN_03", "id": 0}, "reqs": []}, #? Village Buildings Exit Top Left -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_03", "id": 2}, "reqs": []}, #? Village Buildings Exit Left -> Village Buildings Exit Right
    {"from": {"map": "JAN_03", "id": 2}, "to": {"map": "JAN_03", "id": 0}, "reqs": []}, #? Village Buildings Exit Right -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0}, "to": {"map": "JAN_03", "id": 3}, "reqs": []}, #? Village Buildings Exit Left -> Village Buildings Blue Warp Pipe
    {"from": {"map": "JAN_03", "id": 3}, "to": {"map": "JAN_03", "id": 0}, "reqs": []}, #? Village Buildings Blue Warp Pipe -> Village Buildings Exit Left
    
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "GiftA"},     "reqs": []}, #* Village Buildings Exit Left -> GiftA (MagicalSeed4)
    {"from": {"map": "JAN_03", "id": "GiftA"},     "to": {"map": "JAN_03", "id": 0},           "reqs": []}, #* GiftA (MagicalSeed4) -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "ShopItemA"}, "reqs": []}, #* Village Buildings Exit Left -> ShopItemA (SnowmanDoll)
    {"from": {"map": "JAN_03", "id": "ShopItemA"}, "to": {"map": "JAN_03", "id": 0},           "reqs": []}, #* ShopItemA (SnowmanDoll) -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "ShopItemB"}, "reqs": []}, #* Village Buildings Exit Left -> ShopItemB (ThunderRage)
    {"from": {"map": "JAN_03", "id": "ShopItemB"}, "to": {"map": "JAN_03", "id": 0},           "reqs": []}, #* ShopItemB (ThunderRage) -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "ShopItemC"}, "reqs": []}, #* Village Buildings Exit Left -> ShopItemC (FireFlower)
    {"from": {"map": "JAN_03", "id": "ShopItemC"}, "to": {"map": "JAN_03", "id": 0},           "reqs": []}, #* ShopItemC (FireFlower) -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "ShopItemD"}, "reqs": []}, #* Village Buildings Exit Left -> ShopItemD (TastyTonic)
    {"from": {"map": "JAN_03", "id": "ShopItemD"}, "to": {"map": "JAN_03", "id": 0},           "reqs": []}, #* ShopItemD (TastyTonic) -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "ShopItemE"}, "reqs": []}, #* Village Buildings Exit Left -> ShopItemE (HoneySyrup)
    {"from": {"map": "JAN_03", "id": "ShopItemE"}, "to": {"map": "JAN_03", "id": 0},           "reqs": []}, #* ShopItemE (HoneySyrup) -> Village Buildings Exit Left
    {"from": {"map": "JAN_03", "id": 0},           "to": {"map": "JAN_03", "id": "ShopItemF"}, "reqs": []}, #* Village Buildings Exit Left -> ShopItemF (SuperShroom)
    {"from": {"map": "JAN_03", "id": "ShopItemF"}, "to": {"map": "JAN_03", "id": 0},           "reqs": []}, #* ShopItemF (SuperShroom) -> Village Buildings Exit Left

    # JAN_04 Sushi Tree
    {"from": {"map": "JAN_04", "id": 0}, "to": {"map": "JAN_05", "id": 2}, "reqs": []}, # Sushi Tree Exit Left -> SE Jungle (Quake Hammer) Exit Right
    
    {"from": {"map": "JAN_04", "id": 0},              "to": {"map": "JAN_04", "id": "ChestA"},       "reqs": []}, #* Sushi Tree Exit Left -> ChestA (VolcanoVase)
    {"from": {"map": "JAN_04", "id": "ChestA"},       "to": {"map": "JAN_04", "id": 0},              "reqs": []}, #* ChestA (VolcanoVase) -> Sushi Tree Exit Left
    {"from": {"map": "JAN_04", "id": 0},              "to": {"map": "JAN_04", "id": "ItemA"},        "reqs": []}, #* Sushi Tree Exit Left -> ItemA (StarPiece)
    {"from": {"map": "JAN_04", "id": "ItemA"},        "to": {"map": "JAN_04", "id": 0},              "reqs": []}, #* ItemA (StarPiece) -> Sushi Tree Exit Left
    {"from": {"map": "JAN_04", "id": 0},              "to": {"map": "JAN_04", "id": "Tree2_Drop1A"}, "reqs": []}, #* Sushi Tree Exit Left -> Tree2_Drop1A (Letter04)
    {"from": {"map": "JAN_04", "id": "Tree2_Drop1A"}, "to": {"map": "JAN_04", "id": 0},              "reqs": []}, #* Tree2_Drop1A (Letter04) -> Sushi Tree Exit Left

    # JAN_05 SE Jungle (Quake Hammer)
    {"from": {"map": "JAN_05", "id": 0}, "to": {"map": "JAN_03", "id": 1}, "reqs": []}, # SE Jungle (Quake Hammer) Exit Bottom Right -> Village Buildings Exit Top Left
    {"from": {"map": "JAN_05", "id": 1}, "to": {"map": "JAN_08", "id": 1}, "reqs": []}, # SE Jungle (Quake Hammer) Exit Left -> SW Jungle (Super Block) Exit Right
    {"from": {"map": "JAN_05", "id": 2}, "to": {"map": "JAN_04", "id": 0}, "reqs": []}, # SE Jungle (Quake Hammer) Exit Right -> Sushi Tree Exit Left
    {"from": {"map": "JAN_05", "id": 3}, "to": {"map": "JAN_06", "id": 0}, "reqs": []}, # SE Jungle (Quake Hammer) Exit Top -> NE Jungle (Raven Statue) Exit Bottom
    
    {"from": {"map": "JAN_05", "id": 0}, "to": {"map": "JAN_05", "id": 1}, "reqs": []}, #? SE Jungle (Quake Hammer) Exit Bottom Right -> SE Jungle (Quake Hammer) Exit Left
    {"from": {"map": "JAN_05", "id": 1}, "to": {"map": "JAN_05", "id": 0}, "reqs": []}, #? SE Jungle (Quake Hammer) Exit Left-> SE Jungle (Quake Hammer) Exit Bottom Right
    {"from": {"map": "JAN_05", "id": 0}, "to": {"map": "JAN_05", "id": 2}, "reqs": []}, #? SE Jungle (Quake Hammer) Exit Bottom Right -> SE Jungle (Quake Hammer) Exit Right
    {"from": {"map": "JAN_05", "id": 2}, "to": {"map": "JAN_05", "id": 0}, "reqs": []}, #? SE Jungle (Quake Hammer) Exit Right-> SE Jungle (Quake Hammer) Exit Bottom Right
    {"from": {"map": "JAN_05", "id": 0}, "to": {"map": "JAN_05", "id": 3}, "reqs": []}, #? SE Jungle (Quake Hammer) Exit Bottom Right -> SE Jungle (Quake Hammer) Exit Top
    {"from": {"map": "JAN_05", "id": 3}, "to": {"map": "JAN_05", "id": 0}, "reqs": []}, #? SE Jungle (Quake Hammer) Exit Top-> SE Jungle (Quake Hammer) Exit Bottom Right
    
    {"from": {"map": "JAN_05", "id": 2},         "to": {"map": "JAN_05", "id": "RBlockA"}, "reqs": []}, #* SE Jungle (Quake Hammer) Exit Right-> RBlockA (PowerQuake)
    {"from": {"map": "JAN_05", "id": "RBlockA"}, "to": {"map": "JAN_05", "id": 2},         "reqs": []}, #* RBlockA (PowerQuake) -> SE Jungle (Quake Hammer) Exit Right

    # JAN_06 NE Jungle (Raven Statue)
    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_05", "id": 3}, "reqs": []}, # NE Jungle (Raven Statue) Exit Bottom -> SE Jungle (Quake Hammer) Exit Top
    {"from": {"map": "JAN_06", "id": 1}, "to": {"map": "JAN_07", "id": 0}, "reqs": []}, # NE Jungle (Raven Statue) Exit Right -> Small Jungle Ledge Exit Left
    {"from": {"map": "JAN_06", "id": 2}, "to": {"map": "JAN_12", "id": 0}, "reqs": []}, # NE Jungle (Raven Statue) Exit Top -> Deep Jungle 1 Exit Bottom Left
    {"from": {"map": "JAN_06", "id": 3}, "to": {"map": "JAN_09", "id": 1}, "reqs": []}, # NE Jungle (Raven Statue) Exit Left -> NW Jungle (Large Ledge) Exit Right
    
    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_06", "id": 1}, "reqs": []}, #? NE Jungle (Raven Statue) Exit Bottom -> NE Jungle (Raven Statue) Exit Right
    {"from": {"map": "JAN_06", "id": 1}, "to": {"map": "JAN_06", "id": 0}, "reqs": []}, #? NE Jungle (Raven Statue) Exit Right -> NE Jungle (Raven Statue) Exit Bottom
    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_06", "id": 2}, "reqs": []}, #? NE Jungle (Raven Statue) Exit Bottom -> NE Jungle (Raven Statue) Exit Top
    {"from": {"map": "JAN_06", "id": 2}, "to": {"map": "JAN_06", "id": 0}, "reqs": []}, #? NE Jungle (Raven Statue) Exit Top -> NE Jungle (Raven Statue) Exit Bottom
    {"from": {"map": "JAN_06", "id": 1}, "to": {"map": "JAN_06", "id": 3}, "reqs": []}, #? NE Jungle (Raven Statue) Exit Right -> NE Jungle (Raven Statue) Exit Left
    {"from": {"map": "JAN_06", "id": 3}, "to": {"map": "JAN_06", "id": 1}, "reqs": []}, #? NE Jungle (Raven Statue) Exit Left -> NE Jungle (Raven Statue) Exit Right
    
    {"from": {"map": "JAN_06", "id": 0},       "to": {"map": "JAN_06", "id": "ItemA"}, "reqs": []}, #* NE Jungle (Raven Statue) Exit Bottom -> ItemA (Coin)
    {"from": {"map": "JAN_06", "id": "ItemA"}, "to": {"map": "JAN_06", "id": 0},       "reqs": []}, #* ItemA (Coin) -> NE Jungle (Raven Statue) Exit Bottom

    # JAN_07 Small Jungle Ledge
    {"from": {"map": "JAN_07", "id": 0}, "to": {"map": "JAN_06", "id": 1}, "reqs": []}, # Small Jungle Ledge Exit Left -> NE Jungle (Raven Statue) Exit Right

    # JAN_08 SW Jungle (Super Block)
    {"from": {"map": "JAN_08", "id": 0}, "to": {"map": "JAN_00", "id": 2}, "reqs": []}, # SW Jungle (Super Block) Exit Bottom Left -> Whale Cove Exit Top Right
    {"from": {"map": "JAN_08", "id": 1}, "to": {"map": "JAN_05", "id": 1}, "reqs": []}, # SW Jungle (Super Block) Exit Right -> SE Jungle (Quake Hammer) Exit Left
    {"from": {"map": "JAN_08", "id": 2}, "to": {"map": "JAN_09", "id": 0}, "reqs": []}, # SW Jungle (Super Block) Exit Top -> NW Jungle (Large Ledge) Exit Bottom
    
    {"from": {"map": "JAN_08", "id": 0}, "to": {"map": "JAN_08", "id": 1}, "reqs": []}, #? SW Jungle (Super Block) Exit Bottom Left -> SW Jungle (Super Block) Exit Right
    {"from": {"map": "JAN_08", "id": 1}, "to": {"map": "JAN_08", "id": 0}, "reqs": []}, #? SW Jungle (Super Block) Exit Right -> SW Jungle (Super Block) Exit Bottom Left
    {"from": {"map": "JAN_08", "id": 0}, "to": {"map": "JAN_08", "id": 2}, "reqs": []}, #? SW Jungle (Super Block) Exit Bottom Left -> SW Jungle (Super Block) Exit Top
    {"from": {"map": "JAN_08", "id": 2}, "to": {"map": "JAN_08", "id": 0}, "reqs": []}, #? SW Jungle (Super Block) Exit Top -> SW Jungle (Super Block) Exit Bottom Left
    
    {"from": {"map": "JAN_08", "id": 0},               "to": {"map": "JAN_08", "id": "ItemA"},         "reqs": []}, #* SW Jungle (Super Block) Exit Bottom Left -> ItemA (Coin)
    {"from": {"map": "JAN_08", "id": "ItemA"},         "to": {"map": "JAN_08", "id": 0},               "reqs": []}, #* ItemA (Coin) -> SW Jungle (Super Block) Exit Bottom Left
    {"from": {"map": "JAN_08", "id": 0},               "to": {"map": "JAN_08", "id": "ItemB"},         "reqs": []}, #* SW Jungle (Super Block) Exit Bottom Left -> ItemB (Coin)
    {"from": {"map": "JAN_08", "id": "ItemB"},         "to": {"map": "JAN_08", "id": 0},               "reqs": []}, #* ItemB (Coin) -> SW Jungle (Super Block) Exit Bottom Left
    {"from": {"map": "JAN_08", "id": 0},               "to": {"map": "JAN_08", "id": "ItemC"},         "reqs": []}, #* SW Jungle (Super Block) Exit Bottom Left -> ItemC (Coin)
    {"from": {"map": "JAN_08", "id": "ItemC"},         "to": {"map": "JAN_08", "id": 0},               "reqs": []}, #* ItemC (Coin) -> SW Jungle (Super Block) Exit Bottom Left
    {"from": {"map": "JAN_08", "id": 2},               "to": {"map": "JAN_08", "id": "HiddenYBlockA"}, "reqs": []}, #* SW Jungle (Super Block) Exit Top -> HiddenYBlockA (ThunderRage)
    {"from": {"map": "JAN_08", "id": "HiddenYBlockA"}, "to": {"map": "JAN_08", "id": 2},               "reqs": []}, #* HiddenYBlockA (ThunderRage) -> SW Jungle (Super Block) Exit Top

    # JAN_09 NW Jungle (Large Ledge)
    {"from": {"map": "JAN_09", "id": 0}, "to": {"map": "JAN_08", "id": 2}, "reqs": []}, # NW Jungle (Large Ledge) Exit Bottom -> SW Jungle (Super Block) Exit Top
    {"from": {"map": "JAN_09", "id": 1}, "to": {"map": "JAN_06", "id": 3}, "reqs": []}, # NW Jungle (Large Ledge) Exit Right -> NE Jungle (Raven Statue) Exit Left
    {"from": {"map": "JAN_09", "id": 2}, "to": {"map": "JAN_10", "id": 0}, "reqs": []}, # NW Jungle (Large Ledge) Exit Left -> Western Dead End Exit Right
    {"from": {"map": "JAN_09", "id": 3}, "to": {"map": "JAN_11", "id": 0}, "reqs": []}, # NW Jungle (Large Ledge) Pipe On Hill -> Root Cavern Pipe Left
    
    {"from": {"map": "JAN_09", "id": 0}, "to": {"map": "JAN_09", "id": 1}, "reqs": []}, #? NW Jungle (Large Ledge) Exit Bottom -> NW Jungle (Large Ledge) Exit Right
    {"from": {"map": "JAN_09", "id": 1}, "to": {"map": "JAN_09", "id": 0}, "reqs": []}, #? NW Jungle (Large Ledge) Exit Right -> NW Jungle (Large Ledge) Exit Bottom
    {"from": {"map": "JAN_09", "id": 1}, "to": {"map": "JAN_09", "id": 2}, "reqs": []}, #? NW Jungle (Large Ledge) Exit Right -> NW Jungle (Large Ledge) Exit Left
    {"from": {"map": "JAN_09", "id": 2}, "to": {"map": "JAN_09", "id": 1}, "reqs": []}, #? NW Jungle (Large Ledge) Exit Left -> NW Jungle (Large Ledge) Exit Right
    {"from": {"map": "JAN_09", "id": 1}, "to": {"map": "JAN_09", "id": 3}, "reqs": []}, #? NW Jungle (Large Ledge) Exit Right -> NW Jungle (Large Ledge) Pipe On Hill
    {"from": {"map": "JAN_09", "id": 3}, "to": {"map": "JAN_09", "id": 1}, "reqs": []}, #? NW Jungle (Large Ledge) Pipe On Hill -> NW Jungle (Large Ledge) Exit Right

    # JAN_10 Western Dead End
    {"from": {"map": "JAN_10", "id": 0}, "to": {"map": "JAN_09", "id": 2}, "reqs": []}, # Western Dead End Exit Right -> NW Jungle (Large Ledge) Exit Left
    
    {"from": {"map": "JAN_10", "id": 0},       "to": {"map": "JAN_10", "id": "ItemA"}, "reqs": []}, #* Western Dead End Exit Right -> ItemA (StarPiece)
    {"from": {"map": "JAN_10", "id": "ItemA"}, "to": {"map": "JAN_10", "id": 0},       "reqs": []}, #* ItemA (StarPiece) -> Western Dead End Exit Right

    # JAN_11 Root Cavern
    {"from": {"map": "JAN_11", "id": 0}, "to": {"map": "JAN_09", "id": 3}, "reqs": []}, # Root Cavern Pipe Left -> NW Jungle (Large Ledge) Pipe On Hill

    # JAN_12 Deep Jungle 1
    {"from": {"map": "JAN_12", "id": 0}, "to": {"map": "JAN_06", "id": 2}, "reqs": []}, # Deep Jungle 1 Exit Bottom Left -> NE Jungle (Raven Statue) Exit Top
    {"from": {"map": "JAN_12", "id": 1}, "to": {"map": "JAN_13", "id": 0}, "reqs": []}, # Deep Jungle 1 Exit Top Right -> Deep Jungle 2 (Block Puzzle) Exit Bottom Left
    
    {"from": {"map": "JAN_12", "id": 0}, "to": {"map": "JAN_12", "id": 1}, "reqs": []}, #? Deep Jungle 1 Exit Bottom Left -> Deep Jungle 1 Exit Top Right
    {"from": {"map": "JAN_12", "id": 1}, "to": {"map": "JAN_12", "id": 0}, "reqs": []}, #? Deep Jungle 1 Exit Top Right -> Deep Jungle 1 Exit Bottom Left
    
    {"from": {"map": "JAN_12", "id": 0},               "to": {"map": "JAN_12", "id": "ItemA"},         "reqs": []}, #* Deep Jungle 1 Exit Bottom Left -> ItemA (Egg)
    {"from": {"map": "JAN_12", "id": "ItemA"},         "to": {"map": "JAN_12", "id": 0},               "reqs": []}, #* ItemA (Egg) -> Deep Jungle 1 Exit Bottom Left
    {"from": {"map": "JAN_12", "id": 0},               "to": {"map": "JAN_12", "id": "HiddenYBlockA"}, "reqs": []}, #* Deep Jungle 1 Exit Bottom Left -> HiddenYBlockA (StoneCap)
    {"from": {"map": "JAN_12", "id": "HiddenYBlockA"}, "to": {"map": "JAN_12", "id": 0},               "reqs": []}, #* HiddenYBlockA (StoneCap) -> Deep Jungle 1 Exit Bottom Left

    # JAN_13 Deep Jungle 2 (Block Puzzle)
    {"from": {"map": "JAN_13", "id": 0}, "to": {"map": "JAN_12", "id": 1}, "reqs": []}, # Deep Jungle 2 (Block Puzzle) Exit Bottom Left -> Deep Jungle 1 Exit Top Right
    {"from": {"map": "JAN_13", "id": 1}, "to": {"map": "JAN_14", "id": 0}, "reqs": []}, # Deep Jungle 2 (Block Puzzle) Exit Top Right -> Deep Jungle 3 Exit Bottom Left
    
    {"from": {"map": "JAN_13", "id": 0}, "to": {"map": "JAN_13", "id": 1}, "reqs": []}, #? Deep Jungle 2 (Block Puzzle) Exit Bottom Left -> Deep Jungle 2 (Block Puzzle) Exit Top Right
    {"from": {"map": "JAN_13", "id": 1}, "to": {"map": "JAN_13", "id": 0}, "reqs": []}, #? Deep Jungle 2 (Block Puzzle) Exit Top Right -> Deep Jungle 2 (Block Puzzle) Exit Bottom Left
    
    {"from": {"map": "JAN_13", "id": 0},               "to": {"map": "JAN_13", "id": "HiddenYBlockA"}, "reqs": []}, #* Deep Jungle 2 (Block Puzzle) Exit Bottom Left -> HiddenYBlockA (VoltShroom)
    {"from": {"map": "JAN_13", "id": "HiddenYBlockA"}, "to": {"map": "JAN_13", "id": 0},               "reqs": []}, #* HiddenYBlockA (VoltShroom) -> Deep Jungle 2 (Block Puzzle) Exit Bottom Left

    # JAN_14 Deep Jungle 3
    {"from": {"map": "JAN_14", "id": 0}, "to": {"map": "JAN_13", "id": 1}, "reqs": []}, # Deep Jungle 3 Exit Bottom Left -> Deep Jungle 2 (Block Puzzle) Exit Top Right
    {"from": {"map": "JAN_14", "id": 1}, "to": {"map": "JAN_15", "id": 0}, "reqs": []}, # Deep Jungle 3 Exit Top Right -> Deep Jungle 4 (Ambush) Exit Bottom Left
    
    {"from": {"map": "JAN_14", "id": 0}, "to": {"map": "JAN_14", "id": 1}, "reqs": []}, #? Deep Jungle 3 Exit Bottom Left -> Deep Jungle 3 Exit Top Right
    {"from": {"map": "JAN_14", "id": 1}, "to": {"map": "JAN_14", "id": 0}, "reqs": []}, #? Deep Jungle 3 Exit Top Right -> Deep Jungle 3 Exit Bottom Left
    
    {"from": {"map": "JAN_14", "id": 0},       "to": {"map": "JAN_14", "id": "ItemA"}, "reqs": []}, #* Deep Jungle 3 Exit Bottom Left -> ItemA (FireFlower)
    {"from": {"map": "JAN_14", "id": "ItemA"}, "to": {"map": "JAN_14", "id": 0},       "reqs": []}, #* ItemA (FireFlower) -> Deep Jungle 3 Exit Bottom Left
    {"from": {"map": "JAN_14", "id": 0},       "to": {"map": "JAN_14", "id": "ItemB"}, "reqs": []}, #* Deep Jungle 3 Exit Bottom Left -> ItemB (Mushroom)
    {"from": {"map": "JAN_14", "id": "ItemB"}, "to": {"map": "JAN_14", "id": 0},       "reqs": []}, #* ItemB (Mushroom) -> Deep Jungle 3 Exit Bottom Left

    # JAN_15 Deep Jungle 4 (Ambush)
    {"from": {"map": "JAN_15", "id": 0}, "to": {"map": "JAN_14", "id": 1}, "reqs": []}, # Deep Jungle 4 (Ambush) Exit Bottom Left -> Deep Jungle 3 Exit Top Right
    {"from": {"map": "JAN_15", "id": 1}, "to": {"map": "JAN_16", "id": 0}, "reqs": []}, # Deep Jungle 4 (Ambush) Exit Right -> Base of Great Tree Exit Left
    
    {"from": {"map": "JAN_15", "id": 0}, "to": {"map": "JAN_15", "id": 1}, "reqs": []}, #? Deep Jungle 4 (Ambush) Exit Bottom Left -> Deep Jungle 4 (Ambush) Exit Right
    {"from": {"map": "JAN_15", "id": 1}, "to": {"map": "JAN_15", "id": 0}, "reqs": []}, #? Deep Jungle 4 (Ambush) Exit Right -> Deep Jungle 4 (Ambush) Exit Bottom Left
    
    {"from": {"map": "JAN_15", "id": 0},             "to": {"map": "JAN_15", "id": "HiddenPanel"}, "reqs": []}, #* Deep Jungle 4 (Ambush) Exit Bottom Left -> HiddenPanel (StarPiece)
    {"from": {"map": "JAN_15", "id": "HiddenPanel"}, "to": {"map": "JAN_15", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Deep Jungle 4 (Ambush) Exit Bottom Left

    # JAN_16 Base of Great Tree
    {"from": {"map": "JAN_16", "id": 0}, "to": {"map": "JAN_15", "id": 1}, "reqs": []}, # Base of Great Tree Exit Left -> Deep Jungle 4 (Ambush) Exit Right
    {"from": {"map": "JAN_16", "id": 1}, "to": {"map": "JAN_22", "id": 1}, "reqs": []}, # Base of Great Tree Exit Right -> Path to the Volcano Exit Top
    {"from": {"map": "JAN_16", "id": 2}, "to": {"map": "JAN_17", "id": 0}, "reqs": []}, # Base of Great Tree Enter Tree -> Lower Great Tree Interior Exit Bottom
    {"from": {"map": "JAN_16", "id": 4}, "to": {"map": None, "id": None}, "reqs": []},  # Base of Great Tree Fall Off Of Tree
    
    {"from": {"map": "JAN_16", "id": 0}, "to": {"map": "JAN_16", "id": 1}, "reqs": []}, #? Base of Great Tree Exit Left -> Base of Great Tree Exit Right
    {"from": {"map": "JAN_16", "id": 1}, "to": {"map": "JAN_16", "id": 0}, "reqs": []}, #? Base of Great Tree Exit Right -> Base of Great Tree Exit Left
    {"from": {"map": "JAN_16", "id": 0}, "to": {"map": "JAN_16", "id": 2}, "reqs": []}, #? Base of Great Tree Exit Left -> Base of Great Tree Enter Tree
    {"from": {"map": "JAN_16", "id": 2}, "to": {"map": "JAN_16", "id": 0}, "reqs": []}, #? Base of Great Tree Enter Tree -> Base of Great Tree Exit Left
    {"from": {"map": "JAN_16", "id": 4}, "to": {"map": "JAN_16", "id": 0}, "reqs": []}, #? Base of Great Tree Fall Off Of Tree -> Base of Great Tree Exit Left

    # JAN_17 Lower Great Tree Interior
    {"from": {"map": "JAN_17", "id": 0}, "to": {"map": "JAN_16", "id": 2}, "reqs": []}, # Lower Great Tree Interior Exit Bottom -> Base of Great Tree Enter Tree
    {"from": {"map": "JAN_17", "id": 1}, "to": {"map": "JAN_18", "id": 0}, "reqs": []}, # Lower Great Tree Interior Exit Top -> Great Tree Vine Ascent Exit Bottom
    
    {"from": {"map": "JAN_17", "id": 0}, "to": {"map": "JAN_17", "id": 1}, "reqs": []}, #? Lower Great Tree Interior Exit Bottom -> Lower Great Tree Interior Exit Top
    {"from": {"map": "JAN_17", "id": 1}, "to": {"map": "JAN_17", "id": 0}, "reqs": []}, #? Lower Great Tree Interior Exit Top -> Lower Great Tree Interior Exit Bottom

    # JAN_18 Great Tree Vine Ascent
    {"from": {"map": "JAN_18", "id": 0}, "to": {"map": "JAN_17", "id": 1}, "reqs": []}, # Great Tree Vine Ascent Exit Bottom -> Lower Great Tree Interior Exit Top
    {"from": {"map": "JAN_18", "id": 1}, "to": {"map": "JAN_19", "id": 0}, "reqs": []}, # Great Tree Vine Ascent Exit Top -> Upper Great Tree Interior Exit Bottom
    
    {"from": {"map": "JAN_18", "id": 0}, "to": {"map": "JAN_18", "id": 1}, "reqs": []}, #? Great Tree Vine Ascent Exit Bottom -> Great Tree Vine Ascent Exit Top
    {"from": {"map": "JAN_18", "id": 1}, "to": {"map": "JAN_18", "id": 0}, "reqs": []}, #? Great Tree Vine Ascent Exit Top -> Great Tree Vine Ascent Exit Bottom
    
    {"from": {"map": "JAN_18", "id": 0},       "to": {"map": "JAN_18", "id": "ItemA"}, "reqs": []}, #* Great Tree Vine Ascent Exit Bottom -> ItemA (HappyHeartB)
    {"from": {"map": "JAN_18", "id": "ItemA"}, "to": {"map": "JAN_18", "id": 0},       "reqs": []}, #* ItemA (HappyHeartB) -> Great Tree Vine Ascent Exit Bottom

    # JAN_19 Upper Great Tree Interior
    {"from": {"map": "JAN_19", "id": 0}, "to": {"map": "JAN_18", "id": 1}, "reqs": []}, # Upper Great Tree Interior Exit Bottom -> Great Tree Vine Ascent Exit Top
    {"from": {"map": "JAN_19", "id": 1}, "to": {"map": "JAN_23", "id": 0}, "reqs": []}, # Upper Great Tree Interior Exit Top -> Great Treetop Roost Exit Left
    
    {"from": {"map": "JAN_19", "id": 0}, "to": {"map": "JAN_19", "id": 1}, "reqs": []}, #? Upper Great Tree Interior Exit Bottom -> Upper Great Tree Interior Exit Top
    {"from": {"map": "JAN_19", "id": 1}, "to": {"map": "JAN_19", "id": 0}, "reqs": []}, #? Upper Great Tree Interior Exit Top -> Upper Great Tree Interior Exit Bottom

    # JAN_22 Path to the Volcano
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_03", "id": 2}, "reqs": []}, # Path to the Volcano Exit Left -> Village Buildings Exit Right
    {"from": {"map": "JAN_22", "id": 1}, "to": {"map": "JAN_16", "id": 1}, "reqs": []}, # Path to the Volcano Exit Top -> Base of Great Tree Exit Right
    {"from": {"map": "JAN_22", "id": 2}, "to": {"map": "KZN_01", "id": 0}, "reqs": []}, # Path to the Volcano Exit Right -> Volcano Entrance Exit West (Volcano Entrance)
    
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 1}, "reqs": []}, #? Path to the Volcano Exit Left -> Path to the Volcano Exit Top
    {"from": {"map": "JAN_22", "id": 1}, "to": {"map": "JAN_22", "id": 0}, "reqs": []}, #? Path to the Volcano Exit Top -> Path to the Volcano Exit Left
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 2}, "reqs": []}, #? Path to the Volcano Exit Left -> Path to the Volcano Exit Right
    {"from": {"map": "JAN_22", "id": 2}, "to": {"map": "JAN_22", "id": 0}, "reqs": []}, #? Path to the Volcano Exit Right -> Path to the Volcano Exit Left
    
    {"from": {"map": "JAN_22", "id": 0},       "to": {"map": "JAN_22", "id": "GiftA"}, "reqs": []}, #* Path to the Volcano Exit Left -> GiftA (UltraStone)
    {"from": {"map": "JAN_22", "id": "GiftA"}, "to": {"map": "JAN_22", "id": 0},       "reqs": []}, #* GiftA (UltraStone) -> Path to the Volcano Exit Left
    {"from": {"map": "JAN_22", "id": 0},       "to": {"map": "JAN_22", "id": "ItemA"}, "reqs": []}, #* Path to the Volcano Exit Left -> ItemA (JamminJelly)
    {"from": {"map": "JAN_22", "id": "ItemA"}, "to": {"map": "JAN_22", "id": 0},       "reqs": []}, #* ItemA (JamminJelly) -> Path to the Volcano Exit Left

    # JAN_23 Great Treetop Roost
    {"from": {"map": "JAN_23", "id": 0}, "to": {"map": "JAN_19", "id": 1}, "reqs": []}, # Great Treetop Roost Exit Left -> Upper Great Tree Interior Exit Top
    {"from": {"map": "JAN_23", "id": 1}, "to": {"map": "JAN_16", "id": 4}, "reqs": []}, # Great Treetop Roost Jump Off Of Tree -> Base of Great Tree Fall Off Of Tree
    
    {"from": {"map": "JAN_23", "id": 0}, "to": {"map": "JAN_23", "id": 1}, "reqs": []}, #? Great Treetop Roost Exit Left -> Great Treetop Roost Jump Off Of Tree
    {"from": {"map": "JAN_23", "id": 1}, "to": {"map": "JAN_23", "id": 0}, "reqs": []}, #? Great Treetop Roost Jump Off Of Tree -> Great Treetop Roost Exit Left
]