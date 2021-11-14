"""This file represents all edges of the world graph that have origin-nodes in the MAC (Toad Town) area."""
edges_mac = [
    # MAC_00 Gate District
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "KMR_10", "id": 1}, "reqs": []}, # Gate District Exit Left -> Toad Town Entrance Exit Right
    {"from": {"map": "MAC_00", "id": 1}, "to": {"map": "MAC_01", "id": 0}, "reqs": []}, # Gate District Exit Right -> Plaza District Exit Left
    {"from": {"map": "MAC_00", "id": 3}, "to": {"map": "TIK_19", "id": 0}, "reqs": []}, # Gate District Island Pipe -> Under the Toad Town Pond Pipe Left
    {"from": {"map": "MAC_00", "id": 4}, "to": {"map": "KMR_20", "id": 4}, "reqs": []}, # Gate District Top Green Pipe -> Mario's House Green Pipe
    
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "MAC_00", "id": 1}, "reqs": []}, #? Gate District Exit Left -> Gate District Exit Right
    {"from": {"map": "MAC_00", "id": 1}, "to": {"map": "MAC_00", "id": 0}, "reqs": []}, #? Gate District Exit Right -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "MAC_00", "id": 3}, "reqs": []}, #? Gate District Exit Left -> Gate District Island Pipe
    {"from": {"map": "MAC_00", "id": 3}, "to": {"map": "MAC_00", "id": 0}, "reqs": []}, #? Gate District Island Pipe -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "MAC_00", "id": 4}, "reqs": []}, #? Gate District Exit Left -> Gate District Top Green Pipe
    {"from": {"map": "MAC_00", "id": 4}, "to": {"map": "MAC_00", "id": 0}, "reqs": []}, #? Gate District Top Green Pipe -> Gate District Exit Left
    
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "HiddenPanel"}, "reqs": []}, #* Gate District Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "MAC_00", "id": "HiddenPanel"}, "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "ItemA"},       "reqs": []}, #* Gate District Exit Left -> ItemA (StarPiece)
    {"from": {"map": "MAC_00", "id": "ItemA"},       "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* ItemA (StarPiece) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "ShopItemA"},   "reqs": []}, #* Gate District Exit Left -> ShopItemA (FrightJar)
    {"from": {"map": "MAC_00", "id": "ShopItemA"},   "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* ShopItemA (FrightJar) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "ShopItemB"},   "reqs": []}, #* Gate District Exit Left -> ShopItemB (SleepySheep)
    {"from": {"map": "MAC_00", "id": "ShopItemB"},   "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* ShopItemB (SleepySheep) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "ShopItemC"},   "reqs": []}, #* Gate District Exit Left -> ShopItemC (POWBlock)
    {"from": {"map": "MAC_00", "id": "ShopItemC"},   "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* ShopItemC (POWBlock) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "ShopItemD"},   "reqs": []}, #* Gate District Exit Left -> ShopItemD (FireFlower)
    {"from": {"map": "MAC_00", "id": "ShopItemD"},   "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* ShopItemD (FireFlower) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "ShopItemE"},   "reqs": []}, #* Gate District Exit Left -> ShopItemE (HoneySyrup)
    {"from": {"map": "MAC_00", "id": "ShopItemE"},   "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* ShopItemE (HoneySyrup) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "ShopItemF"},   "reqs": []}, #* Gate District Exit Left -> ShopItemF (Mushroom)
    {"from": {"map": "MAC_00", "id": "ShopItemF"},   "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* ShopItemF (Mushroom) -> Gate District Exit Left

    # MAC_01 Plaza District
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_00", "id": 1}, "reqs": []}, # Plaza District Exit Left -> Gate District Exit Right
    {"from": {"map": "MAC_01", "id": 1}, "to": {"map": "NOK_11", "id": 0}, "reqs": []}, # Plaza District Exit Right -> Pleasant Path Entry Exit Left
    {"from": {"map": "MAC_01", "id": 2}, "to": {"map": "OSR_01", "id": 0}, "reqs": []}, # Plaza District Exit Top -> Peach's Castle Ground Exit Bottom
    {"from": {"map": "MAC_01", "id": 3}, "to": {"map": "MAC_02", "id": 2}, "reqs": []}, # Plaza District Exit Bottom -> Southern District Exit Top
    {"from": {"map": "MAC_01", "id": 5}, "to": {"map": "FLO_00", "id": 0}, "reqs": []}, # Plaza District Flower Door -> Flower Fields Center Tree Door
    
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 1}, "reqs": []}, #? Plaza District Exit Left -> Plaza District Exit Right
    {"from": {"map": "MAC_01", "id": 1}, "to": {"map": "MAC_01", "id": 0}, "reqs": []}, #? Plaza District Exit Right -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 2}, "reqs": []}, #? Plaza District Exit Left -> Plaza District Exit Top
    {"from": {"map": "MAC_01", "id": 2}, "to": {"map": "MAC_01", "id": 0}, "reqs": []}, #? Plaza District Exit Top -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 3}, "reqs": []}, #? Plaza District Exit Left -> Plaza District Exit Bottom
    {"from": {"map": "MAC_01", "id": 3}, "to": {"map": "MAC_01", "id": 0}, "reqs": []}, #? Plaza District Exit Bottom -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 5}, "reqs": []}, #? Plaza District Exit Left -> Plaza District Flower Door
    {"from": {"map": "MAC_01", "id": 5}, "to": {"map": "MAC_01", "id": 0}, "reqs": []}, #? Plaza District Flower Door -> Plaza District Exit Left
    
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ItemA"},        "reqs": []}, #* Plaza District Exit Left -> ItemA (QuickChange)
    {"from": {"map": "MAC_01", "id": "ItemA"},        "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ItemA (QuickChange) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "Tree1_Drop1A"}, "reqs": []}, #* Plaza District Exit Left -> Tree1_Drop1A (StarPiece)
    {"from": {"map": "MAC_01", "id": "Tree1_Drop1A"}, "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* Tree1_Drop1A (StarPiece) -> Plaza District Exit Left

    # MAC_02 Southern District
    {"from": {"map": "MAC_02", "id": 0}, "to": {"map": "MAC_04", "id": 0}, "reqs": []}, # Southern District Exit Left -> Residental District Exit Right
    {"from": {"map": "MAC_02", "id": 1}, "to": {"map": "MIM_10", "id": 0}, "reqs": []}, # Southern District Exit Right -> Exit to Toad Town Exit left
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_01", "id": 3}, "reqs": []}, # Southern District Exit Top -> Plaza District Exit Bottom
    {"from": {"map": "MAC_02", "id": 3}, "to": {"map": "MAC_03", "id": 0}, "reqs": []}, # Southern District Exit Bottom -> Station District Exit Top
    {"from": {"map": "MAC_02", "id": 4}, "to": {"map": "TIK_06", "id": 3}, "reqs": []}, # Southern District Open Pipe -> Sewer Entrance (B1) Pipe Top
    {"from": {"map": "MAC_02", "id": 5}, "to": {"map": "TIK_15", "id": 1}, "reqs": []}, # Southern District Blue House Pipe -> Rip Cheato's Home (B3) Pipe Right
    
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 0}, "reqs": []}, #? Southern District Exit Top -> Southern District Exit Left
    {"from": {"map": "MAC_02", "id": 0}, "to": {"map": "MAC_02", "id": 2}, "reqs": []}, #? Southern District Exit Left -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 1}, "reqs": []}, #? Southern District Exit Top -> Southern District Exit Right
    {"from": {"map": "MAC_02", "id": 1}, "to": {"map": "MAC_02", "id": 2}, "reqs": []}, #? Southern District Exit Right -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 3}, "reqs": []}, #? Southern District Exit Top -> Southern District Exit Bottom
    {"from": {"map": "MAC_02", "id": 3}, "to": {"map": "MAC_02", "id": 2}, "reqs": []}, #? Southern District Exit Bottom -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 4}, "reqs": []}, #? Southern District Exit Top -> Southern District Open Pipe
    {"from": {"map": "MAC_02", "id": 4}, "to": {"map": "MAC_02", "id": 2}, "reqs": []}, #? Southern District Open Pipe -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 5}, "reqs": []}, #? Southern District Exit Top -> Southern District Blue House Pipe
    {"from": {"map": "MAC_02", "id": 5}, "to": {"map": "MAC_02", "id": 2}, "reqs": []}, #? Southern District Blue House Pipe -> Southern District Exit Top
    
    {"from": {"map": "MAC_02", "id": 2},             "to": {"map": "MAC_02", "id": "GiftA"},       "reqs": []}, #* Southern District Exit Top -> GiftA (MagicalSeed1)
    {"from": {"map": "MAC_02", "id": "GiftA"},       "to": {"map": "MAC_02", "id": 2},             "reqs": []}, #* GiftA (MagicalSeed1) -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 2},             "to": {"map": "MAC_02", "id": "GiftB"},       "reqs": []}, #* Southern District Exit Top -> GiftB (Cake)
    {"from": {"map": "MAC_02", "id": "GiftB"},       "to": {"map": "MAC_02", "id": 2},             "reqs": []}, #* GiftB (Cake) -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 2},             "to": {"map": "MAC_02", "id": "HiddenPanel"}, "reqs": []}, #* Southern District Exit Top -> HiddenPanel (StarPiece)
    {"from": {"map": "MAC_02", "id": "HiddenPanel"}, "to": {"map": "MAC_02", "id": 2},             "reqs": []}, #* HiddenPanel (StarPiece) -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 5},             "to": {"map": "MAC_02", "id": "ItemA"},       "reqs": []}, #* Southern District Blue House Pipe -> ItemA (OddKey)
    {"from": {"map": "MAC_02", "id": "ItemA"},       "to": {"map": "MAC_02", "id": 5},             "reqs": []}, #* ItemA (OddKey) -> Southern District Blue House Pipe

    # MAC_03 Station District
    {"from": {"map": "MAC_03", "id": 0}, "to": {"map": "MAC_02", "id": 3}, "reqs": []}, # Station District Exit Top -> Southern District Exit Bottom
    {"from": {"map": "MAC_03", "id": 1}, "to": {"map": "IWA_11", "id": 1}, "reqs": []}, # Station District Train -> Train Ride Scene Exit Left
    {"from": {"map": "MAC_03", "id": 2}, "to": {"map": "MGM_00", "id": 0}, "reqs": []}, # Station District Minigame Pipe -> Playroom Lobby Exit Pipe
    
    {"from": {"map": "MAC_03", "id": 0}, "to": {"map": "MAC_03", "id": 1}, "reqs": []}, #? Station District Exit Top -> Station District Train
    {"from": {"map": "MAC_03", "id": 1}, "to": {"map": "MAC_03", "id": 0}, "reqs": []}, #? Station District Train -> Station District Exit Top
    {"from": {"map": "MAC_03", "id": 0}, "to": {"map": "MAC_03", "id": 2}, "reqs": []}, #? Station District Exit Top -> Station District Minigame Pipe
    {"from": {"map": "MAC_03", "id": 2}, "to": {"map": "MAC_03", "id": 0}, "reqs": []}, #? Station District Minigame Pipe -> Station District Exit Top
    
    {"from": {"map": "MAC_03", "id": 0},             "to": {"map": "MAC_03", "id": "GiftA"},       "reqs": []}, #* Station District Exit Top -> GiftA (Letter21)
    {"from": {"map": "MAC_03", "id": "GiftA"},       "to": {"map": "MAC_03", "id": 0},             "reqs": []}, #* GiftA (Letter21) -> Station District Exit Top
    {"from": {"map": "MAC_03", "id": 0},             "to": {"map": "MAC_03", "id": "GiftB"},       "reqs": []}, #* Station District Exit Top -> GiftB (Letter23)
    {"from": {"map": "MAC_03", "id": "GiftB"},       "to": {"map": "MAC_03", "id": 0},             "reqs": []}, #* GiftB (Letter23) -> Station District Exit Top
    {"from": {"map": "MAC_03", "id": 0},             "to": {"map": "MAC_03", "id": "HiddenPanel"}, "reqs": []}, #* Station District Exit Top -> HiddenPanel (StarPiece)
    {"from": {"map": "MAC_03", "id": "HiddenPanel"}, "to": {"map": "MAC_03", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Station District Exit Top

    # MAC_04 Residental District
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_02", "id": 0}, "reqs": []}, # Residental District Exit Right -> Southern District Exit Left
    {"from": {"map": "MAC_04", "id": 1}, "to": {"map": "MAC_05", "id": 0}, "reqs": []}, # Residental District Exit Left -> Port District Exit Right
    {"from": {"map": "MAC_04", "id": 2}, "to": {"map": "OMO_03", "id": 4}, "reqs": []}, # Residental District Toybox Spring -> BLU Station Spring Exit
    
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 1}, "reqs": []}, #? Residental District Exit Right -> Residental District Exit Left
    {"from": {"map": "MAC_04", "id": 1}, "to": {"map": "MAC_04", "id": 0}, "reqs": []}, #? Residental District Exit Left -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 2}, "reqs": []}, #? Residental District Exit Right -> Residental District Toybox Spring
    {"from": {"map": "MAC_04", "id": 2}, "to": {"map": "MAC_04", "id": 0}, "reqs": []}, #? Residental District Toybox Spring -> Residental District Exit Right
    
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ItemA"},     "reqs": []}, #* Residental District Exit Right -> ItemA (SnowmanDoll)
    {"from": {"map": "MAC_04", "id": "ItemA"},     "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ItemA (SnowmanDoll) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ItemB"},     "reqs": []}, #* Residental District Exit Right -> ItemB (VoltShroom)
    {"from": {"map": "MAC_04", "id": "ItemB"},     "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ItemB (VoltShroom) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ItemC"},     "reqs": []}, #* Residental District Exit Right -> ItemC (ToyTrain)
    {"from": {"map": "MAC_04", "id": "ItemC"},     "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ItemC (ToyTrain) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ItemD"},     "reqs": []}, #* Residental District Exit Right -> ItemD (DizzyDial)
    {"from": {"map": "MAC_04", "id": "ItemD"},     "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ItemD (DizzyDial) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ShopItemA"}, "reqs": []}, #* Residental District Exit Right -> ShopItemA (StoneCap)
    {"from": {"map": "MAC_04", "id": "ShopItemA"}, "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ShopItemA (StoneCap) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ShopItemB"}, "reqs": []}, #* Residental District Exit Right -> ShopItemB (DizzyDial)
    {"from": {"map": "MAC_04", "id": "ShopItemB"}, "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ShopItemB (DizzyDial) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ShopItemC"}, "reqs": []}, #* Residental District Exit Right -> ShopItemC (ThunderRage)
    {"from": {"map": "MAC_04", "id": "ShopItemC"}, "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ShopItemC (ThunderRage) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ShopItemD"}, "reqs": []}, #* Residental District Exit Right -> ShopItemD (TastyTonic)
    {"from": {"map": "MAC_04", "id": "ShopItemD"}, "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ShopItemD (TastyTonic) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ShopItemE"}, "reqs": []}, #* Residental District Exit Right -> ShopItemE (VoltShroom)
    {"from": {"map": "MAC_04", "id": "ShopItemE"}, "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ShopItemE (VoltShroom) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ShopItemF"}, "reqs": []}, #* Residental District Exit Right -> ShopItemF (SuperShroom)
    {"from": {"map": "MAC_04", "id": "ShopItemF"}, "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ShopItemF (SuperShroom) -> Residental District Exit Right

    # MAC_05 Port District
    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_04", "id": 1}, "reqs": []}, # Port District Exit Right -> Residental District Exit Left
    {"from": {"map": "MAC_05", "id": 1}, "to": {"map": "JAN_00", "id": 0}, "reqs": []}, # Port District Ride Whale -> Whale Cove Ride Whale
    {"from": {"map": "MAC_05", "id": 3}, "to": {"map": "KGR_01", "id": 0}, "reqs": []}, # Port District Enter Whale -> Whale Mouth Exit Left
    
    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_05", "id": 1}, "reqs": []}, #? Port District Exit Right -> Port District Ride Whale
    {"from": {"map": "MAC_05", "id": 1}, "to": {"map": "MAC_05", "id": 0}, "reqs": []}, #? Port District Ride Whale -> Port District Exit Right
    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_05", "id": 3}, "reqs": []}, #? Port District Exit Right -> Port District Enter Whale
    {"from": {"map": "MAC_05", "id": 3}, "to": {"map": "MAC_05", "id": 0}, "reqs": []}, #? Port District Enter Whale -> Port District Exit Right
    
    {"from": {"map": "MAC_05", "id": 0},             "to": {"map": "MAC_05", "id": "GiftA"},       "reqs": []}, #* Port District Exit Right -> GiftA (Lyrics)
    {"from": {"map": "MAC_05", "id": "GiftA"},       "to": {"map": "MAC_05", "id": 0},             "reqs": []}, #* GiftA (Lyrics) -> Port District Exit Right
    {"from": {"map": "MAC_05", "id": 0},             "to": {"map": "MAC_05", "id": "HiddenPanel"}, "reqs": []}, #* Port District Exit Right -> HiddenPanel (StarPiece)
    {"from": {"map": "MAC_05", "id": "HiddenPanel"}, "to": {"map": "MAC_05", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Port District Exit Right
]