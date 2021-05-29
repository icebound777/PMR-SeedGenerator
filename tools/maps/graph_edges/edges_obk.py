"""This file represents all edges of the world graph that have origin-nodes in the OBK (Boo's Mansion) area."""
edges_obk = [
    # OBK_01 Foyer
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "MIM_11", "id": 2}, "reqs": []}, # Foyer Front Door -> Outside Boo's Mansion Front Door
    {"from": {"map": "OBK_01", "id": 1}, "to": {"map": "OBK_02", "id": 0}, "reqs": []}, # Foyer Lower Hidden Door -> Basement Stairs Upper Door
    {"from": {"map": "OBK_01", "id": 2}, "to": {"map": "OBK_05", "id": 0}, "reqs": []}, # Foyer Lower Door -> Pot Room Door South
    {"from": {"map": "OBK_01", "id": 3}, "to": {"map": "OBK_07", "id": 0}, "reqs": []}, # Foyer Upper Door West -> Record Player Room Door South
    {"from": {"map": "OBK_01", "id": 4}, "to": {"map": "OBK_08", "id": 0}, "reqs": []}, # Foyer Upper Door East -> Record Room Door South
    {"from": {"map": "OBK_01", "id": 5}, "to": {"map": "OBK_09", "id": 0}, "reqs": []}, # Foyer Third Floor Door West -> Lady Bow's Room Door South West
    {"from": {"map": "OBK_01", "id": 6}, "to": {"map": "OBK_09", "id": 1}, "reqs": []}, # Foyer Third Floor Door East -> Lady Bow's Room Door South East
    
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": 1}, "reqs": []}, #? Foyer Front Door -> Foyer Lower Hidden Door
    {"from": {"map": "OBK_01", "id": 1}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, #? Foyer Lower Hidden Door -> Foyer Front Door
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": 2}, "reqs": []}, #? Foyer Front Door -> Foyer Lower Door
    {"from": {"map": "OBK_01", "id": 2}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, #? Foyer Lower Door -> Foyer Front Door
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": 3}, "reqs": []}, #? Foyer Front Door -> Foyer Upper Door West
    {"from": {"map": "OBK_01", "id": 3}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, #? Foyer Upper Door West -> Foyer Front Door
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": 4}, "reqs": []}, #? Foyer Front Door -> Foyer Upper Door East
    {"from": {"map": "OBK_01", "id": 4}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, #? Foyer Upper Door East -> Foyer Front Door
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": 5}, "reqs": []}, #? Foyer Front Door -> Foyer Third Floor Door West
    {"from": {"map": "OBK_01", "id": 5}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, #? Foyer Third Floor Door West -> Foyer Front Door
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": 6}, "reqs": []}, #? Foyer Front Door -> Foyer Third Floor Door East
    {"from": {"map": "OBK_01", "id": 6}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, #? Foyer Third Floor Door East -> Foyer Front Door
    
    {"from": {"map": "OBK_01", "id": 0},             "to": {"map": "OBK_01", "id": "GiftA"},       "reqs": []}, #* Foyer Front Door -> GiftA (OldPhoto)
    {"from": {"map": "OBK_01", "id": "GiftA"},       "to": {"map": "OBK_01", "id": 0},             "reqs": []}, #* GiftA (OldPhoto) -> Foyer Front Door
    {"from": {"map": "OBK_01", "id": 0},             "to": {"map": "OBK_01", "id": "HiddenPanel"}, "reqs": []}, #* Foyer Front Door -> HiddenPanel (StarPiece)
    {"from": {"map": "OBK_01", "id": "HiddenPanel"}, "to": {"map": "OBK_01", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Foyer Front Door

    # OBK_02 Basement Stairs
    {"from": {"map": "OBK_02", "id": 0}, "to": {"map": "OBK_01", "id": 1}, "reqs": []}, # Basement Stairs Upper Door -> Foyer Lower Hidden Door
    {"from": {"map": "OBK_02", "id": 1}, "to": {"map": "OBK_03", "id": 0}, "reqs": []}, # Basement Stairs Lower Door South -> Basement Upper Door North
    {"from": {"map": "OBK_02", "id": 2}, "to": {"map": "OBK_06", "id": 1}, "reqs": []}, # Basement Stairs Bombable Wall -> Library Bombable Wall
    
    {"from": {"map": "OBK_02", "id": 0}, "to": {"map": "OBK_02", "id": 1}, "reqs": []}, #? Basement Stairs Upper Door -> Basement Stairs Lower Door South
    {"from": {"map": "OBK_02", "id": 1}, "to": {"map": "OBK_02", "id": 0}, "reqs": []}, #? Basement Stairs Lower Door South -> Basement Stairs Upper Door
    {"from": {"map": "OBK_02", "id": 0}, "to": {"map": "OBK_02", "id": 2}, "reqs": []}, #? Basement Stairs Upper Door -> Basement Stairs Bombable Wall
    {"from": {"map": "OBK_02", "id": 2}, "to": {"map": "OBK_02", "id": 0}, "reqs": []}, #? Basement Stairs Bombable Wall -> Basement Stairs Upper Door
    
    {"from": {"map": "OBK_02", "id": 0},             "to": {"map": "OBK_02", "id": "HiddenPanel"}, "reqs": []}, #* Basement Stairs Upper Door -> HiddenPanel (StarPiece)
    {"from": {"map": "OBK_02", "id": "HiddenPanel"}, "to": {"map": "OBK_02", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Basement Stairs Upper Door

    # OBK_03 Basement
    {"from": {"map": "OBK_03", "id": 0}, "to": {"map": "OBK_02", "id": 1}, "reqs": []}, # Basement Upper Door North -> Basement Stairs Lower Door South
    {"from": {"map": "OBK_03", "id": 1}, "to": {"map": "OBK_04", "id": 0}, "reqs": []}, # Basement Upper Door East -> Super Boots Room Vanishing Door
    {"from": {"map": "OBK_03", "id": 2}, "to": {"map": None, "id": None}, "reqs":  []}, # Basement Fall From Ceiling
    
    {"from": {"map": "OBK_03", "id": 0}, "to": {"map": "OBK_03", "id": 1}, "reqs": []}, #? Basement Upper Door North -> Basement Upper Door East
    {"from": {"map": "OBK_03", "id": 1}, "to": {"map": "OBK_03", "id": 0}, "reqs": []}, #? Basement Upper Door East -> Basement Upper Door North
    {"from": {"map": "OBK_03", "id": 0}, "to": {"map": "OBK_03", "id": 2}, "reqs": []}, #? Basement Upper Door North -> Basement Fall From Ceiling
    {"from": {"map": "OBK_03", "id": 2}, "to": {"map": "OBK_03", "id": 0}, "reqs": []}, #? Basement Fall From Ceiling -> Basement Upper Door North
    
    {"from": {"map": "OBK_03", "id": 0},           "to": {"map": "OBK_03", "id": "CrateA"},    "reqs": []}, #* Basement Upper Door North -> CrateA (SuperShroom)
    {"from": {"map": "OBK_03", "id": "CrateA"},    "to": {"map": "OBK_03", "id": 0},           "reqs": []}, #* CrateA (SuperShroom) -> Basement Upper Door North
    {"from": {"map": "OBK_03", "id": 2},           "to": {"map": "OBK_03", "id": "ShopItemA"}, "reqs": []}, #* Basement Fall From Ceiling -> ShopItemA (Mystery)
    {"from": {"map": "OBK_03", "id": "ShopItemA"}, "to": {"map": "OBK_03", "id": 2},           "reqs": []}, #* ShopItemA (Mystery) -> Basement Fall From Ceiling
    {"from": {"map": "OBK_03", "id": 2},           "to": {"map": "OBK_03", "id": "ShopItemB"}, "reqs": []}, #* Basement Fall From Ceiling -> ShopItemB (StopWatch)
    {"from": {"map": "OBK_03", "id": "ShopItemB"}, "to": {"map": "OBK_03", "id": 2},           "reqs": []}, #* ShopItemB (StopWatch) -> Basement Fall From Ceiling
    {"from": {"map": "OBK_03", "id": 2},           "to": {"map": "OBK_03", "id": "ShopItemC"}, "reqs": []}, #* Basement Fall From Ceiling -> ShopItemC (SnowmanDoll)
    {"from": {"map": "OBK_03", "id": "ShopItemC"}, "to": {"map": "OBK_03", "id": 2},           "reqs": []}, #* ShopItemC (SnowmanDoll) -> Basement Fall From Ceiling
    {"from": {"map": "OBK_03", "id": 2},           "to": {"map": "OBK_03", "id": "ShopItemD"}, "reqs": []}, #* Basement Fall From Ceiling -> ShopItemD (MapleSyrup)
    {"from": {"map": "OBK_03", "id": "ShopItemD"}, "to": {"map": "OBK_03", "id": 2},           "reqs": []}, #* ShopItemD (MapleSyrup) -> Basement Fall From Ceiling
    {"from": {"map": "OBK_03", "id": 2},           "to": {"map": "OBK_03", "id": "ShopItemE"}, "reqs": []}, #* Basement Fall From Ceiling -> ShopItemE (LifeShroom)
    {"from": {"map": "OBK_03", "id": "ShopItemE"}, "to": {"map": "OBK_03", "id": 2},           "reqs": []}, #* ShopItemE (LifeShroom) -> Basement Fall From Ceiling
    {"from": {"map": "OBK_03", "id": 2},           "to": {"map": "OBK_03", "id": "ShopItemF"}, "reqs": []}, #* Basement Fall From Ceiling -> ShopItemF (SuperShroom)
    {"from": {"map": "OBK_03", "id": "ShopItemF"}, "to": {"map": "OBK_03", "id": 2},           "reqs": []}, #* ShopItemF (SuperShroom) -> Basement Fall From Ceiling

    # OBK_04 Super Boots Room
    {"from": {"map": "OBK_04", "id": 0}, "to": {"map": None, "id": None},  "reqs": []}, # Super Boots Room Vanishing Door
    {"from": {"map": "OBK_04", "id": 1}, "to": {"map": "OBK_03", "id": 2}, "reqs": []}, # Super Boots Room Hole Under Planks -> Basement Fall From Ceiling
    
    {"from": {"map": "OBK_04", "id": 0}, "to": {"map": "OBK_04", "id": 1}, "reqs": []}, #? Super Boots Room Vanishing Door -> Super Boots Room Hole Under Planks
    {"from": {"map": "OBK_04", "id": 1}, "to": {"map": "OBK_04", "id": 0}, "reqs": []}, #? Super Boots Room Hole Under Planks -> Super Boots Room Vanishing Door
    
    {"from": {"map": "OBK_04", "id": 0},             "to": {"map": "OBK_04", "id": "CrateA"},      "reqs": []}, #* Super Boots Room Vanishing Door -> CrateA (MapleSyrup)
    {"from": {"map": "OBK_04", "id": "CrateA"},      "to": {"map": "OBK_04", "id": 0},             "reqs": []}, #* CrateA (MapleSyrup) -> Super Boots Room Vanishing Door
    {"from": {"map": "OBK_04", "id": 0},             "to": {"map": "OBK_04", "id": "HiddenPanel"}, "reqs": []}, #* Super Boots Room Vanishing Door -> HiddenPanel (StarPiece)
    {"from": {"map": "OBK_04", "id": "HiddenPanel"}, "to": {"map": "OBK_04", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Super Boots Room Vanishing Door

    # OBK_05 Pot Room
    {"from": {"map": "OBK_05", "id": 0}, "to": {"map": "OBK_01", "id": 2}, "reqs": []}, # Pot Room Door South -> Foyer Lower Door
    {"from": {"map": "OBK_05", "id": 1}, "to": {"map": "OBK_06", "id": 0}, "reqs": []}, # Pot Room Hole Under Planks -> Library Fall From Ceiling
    
    {"from": {"map": "OBK_05", "id": 0}, "to": {"map": "OBK_05", "id": 1}, "reqs": []}, #? Pot Room Door South -> Pot Room Hole Under Planks
    {"from": {"map": "OBK_05", "id": 1}, "to": {"map": "OBK_05", "id": 0}, "reqs": []}, #? Pot Room Hole Under Planks -> Pot Room Door South
    
    {"from": {"map": "OBK_05", "id": 0},        "to": {"map": "OBK_05", "id": "CrateA"}, "reqs": []}, #* Pot Room Door South -> CrateA (Apple)
    {"from": {"map": "OBK_05", "id": "CrateA"}, "to": {"map": "OBK_05", "id": 0},        "reqs": []}, #* CrateA (Apple) -> Pot Room Door South
    {"from": {"map": "OBK_05", "id": 0},        "to": {"map": "OBK_05", "id": "CrateB"}, "reqs": []}, #* Pot Room Door South -> CrateB (Apple)
    {"from": {"map": "OBK_05", "id": "CrateB"}, "to": {"map": "OBK_05", "id": 0},        "reqs": []}, #* CrateB (Apple) -> Pot Room Door South

    # OBK_06 Library
    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": None, "id": None},  "reqs": []}, # Library Fall From Ceiling
    {"from": {"map": "OBK_06", "id": 1}, "to": {"map": "OBK_02", "id": 2}, "reqs": []}, # Library Bombable Wall -> Basement Stairs Bombable Wall
    
    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_06", "id": 1}, "reqs": []}, #? Library Fall From Ceiling -> Library Bombable Wall
    
    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_06", "id": "CrateA"}, "reqs": []}, #* Library Fall From Ceiling -> CrateA (StarPiece)
    {"from": {"map": "OBK_06", "id": "CrateA"}, "to": {"map": "OBK_06", "id": 1}, "reqs": []}, #* CrateA (StarPiece) -> Library Bombable Wall
    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_06", "id": "ItemA"}, "reqs": []}, #* Library Fall From Ceiling -> ItemA (BoosPortrait)
    {"from": {"map": "OBK_06", "id": "ItemA"}, "to": {"map": "OBK_06", "id": 0}, "reqs": []}, #* ItemA (BoosPortrait) -> Library Fall From Ceiling

    # OBK_07 Record Player Room
    {"from": {"map": "OBK_07", "id": 0}, "to": {"map": "OBK_01", "id": 3}, "reqs": []}, # Record Player Room Door South -> Foyer Upper Door West
    
    {"from": {"map": "OBK_07", "id": 0},        "to": {"map": "OBK_07", "id": "ChestA"}, "reqs": []}, #* Record Player Room Door South -> ChestA (Weight)
    {"from": {"map": "OBK_07", "id": "ChestA"}, "to": {"map": "OBK_07", "id": 0},        "reqs": []}, #* ChestA (Weight) -> Record Player Room Door South

    # OBK_08 Record Room
    {"from": {"map": "OBK_08", "id": 0}, "to": {"map": "OBK_01", "id": 4}, "reqs": []}, # Record Room Door South -> Foyer Upper Door East
    
    {"from": {"map": "OBK_08", "id": 0},             "to": {"map": "OBK_08", "id": "HiddenPanel"}, "reqs": []}, #* Record Room Door South -> HiddenPanel (StarPiece)
    {"from": {"map": "OBK_08", "id": "HiddenPanel"}, "to": {"map": "OBK_08", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Record Room Door South
    {"from": {"map": "OBK_08", "id": 0},             "to": {"map": "OBK_08", "id": "ItemA"},       "reqs": []}, #* Record Room Door South -> ItemA (Record)
    {"from": {"map": "OBK_08", "id": "ItemA"},       "to": {"map": "OBK_08", "id": 0},             "reqs": []}, #* ItemA (Record) -> Record Room Door South

    # OBK_09 Lady Bow's Room
    {"from": {"map": "OBK_09", "id": 0}, "to": {"map": "OBK_01", "id": 5}, "reqs": []}, # Lady Bow's Room Door South West -> Foyer Third Floor Door West
    {"from": {"map": "OBK_09", "id": 1}, "to": {"map": "OBK_01", "id": 6}, "reqs": []}, # Lady Bow's Room Door South East -> Foyer Third Floor Door East
    
    {"from": {"map": "OBK_09", "id": 0}, "to": {"map": "OBK_09", "id": 1}, "reqs": []}, #? Lady Bow's Room Door South West -> Lady Bow's Room Door South East
    {"from": {"map": "OBK_09", "id": 1}, "to": {"map": "OBK_09", "id": 0}, "reqs": []}, #? Lady Bow's Room Door South East -> Lady Bow's Room Door South West
]