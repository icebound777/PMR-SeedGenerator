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

    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": 1}, "reqs": [["BooWeight"],["can_climb_steps"]]}, #? Foyer Front Door -> Foyer Lower Hidden Door
    {"from": {"map": "OBK_01", "id": 1}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, #? Foyer Lower Hidden Door -> Foyer Front Door
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": 2}, "reqs": []}, #? Foyer Front Door -> Foyer Lower Door
    {"from": {"map": "OBK_01", "id": 2}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, #? Foyer Lower Door -> Foyer Front Door
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": 3}, "reqs": [["Boots","BooWeight"],["can_climb_steps"]]}, #? Foyer Front Door -> Foyer Upper Door West
    {"from": {"map": "OBK_01", "id": 3}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, #? Foyer Upper Door West -> Foyer Front Door
    {"from": {"map": "OBK_01", "id": 3}, "to": {"map": "OBK_01", "id": 4}, "reqs": []}, #? Foyer Upper Door West -> Foyer Upper Door East
    {"from": {"map": "OBK_01", "id": 4}, "to": {"map": "OBK_01", "id": 3}, "reqs": []}, #? Foyer Upper Door East -> Foyer Upper Door West
    {"from": {"map": "OBK_01", "id": 3}, "to": {"map": "OBK_01", "id": 5}, "reqs": [["BooPortrait"]]}, #? Foyer Upper Door West -> Foyer Third Floor Door West
    {"from": {"map": "OBK_01", "id": 5}, "to": {"map": "OBK_01", "id": 3}, "reqs": []}, #? Foyer Third Floor Door West -> Foyer Upper Door West
    {"from": {"map": "OBK_01", "id": 5}, "to": {"map": "OBK_01", "id": 6}, "reqs": []}, #? Foyer Third Floor Door West -> Foyer Third Floor Door East
    {"from": {"map": "OBK_01", "id": 6}, "to": {"map": "OBK_01", "id": 5}, "reqs": []}, #? Foyer Third Floor Door East -> Foyer Third Floor Door West

    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": "GiftA"},       "reqs": [["RF_OpenedGustyGulch"],["FAVOR_5_02_active"]]}, #* Foyer Front Door -> GiftA (KootOldPhoto)
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": "GiftB"},       "reqs": [["RF_OpenedGustyGulch"],["Parakarry"],["Letter12"]]}, #* Foyer Front Door -> GiftB (Letter20)
    {"from": {"map": "OBK_01", "id": 0}, "to": {"map": "OBK_01", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Foyer Front Door -> HiddenPanel (StarPiece)

    # OBK_02 Basement Stairs
    {"from": {"map": "OBK_02", "id": 0}, "to": {"map": "OBK_01", "id": 1}, "reqs": []}, # Basement Stairs Upper Door -> Foyer Lower Hidden Door
    {"from": {"map": "OBK_02", "id": 1}, "to": {"map": "OBK_03", "id": 0}, "reqs": []}, # Basement Stairs Lower Door South -> Basement Upper Door North
    {"from": {"map": "OBK_02", "id": 2}, "to": {"map": "OBK_06", "id": 1}, "reqs": []}, # Basement Stairs Bombable Wall -> Library Bombable Wall

    {"from": {"map": "OBK_02", "id": 0}, "to": {"map": "OBK_02", "id": 1}, "reqs": []}, #? Basement Stairs Upper Door -> Basement Stairs Lower Door South
    {"from": {"map": "OBK_02", "id": 1}, "to": {"map": "OBK_02", "id": 0}, "reqs": [["Boots"]]}, #? Basement Stairs Lower Door South -> Basement Stairs Upper Door
    {"from": {"map": "OBK_02", "id": 1}, "to": {"map": "OBK_02", "id": 2}, "reqs": [["Bombette"]]}, #? Basement Stairs Lower Door South -> Basement Stairs Bombable Wall
    {"from": {"map": "OBK_02", "id": 2}, "to": {"map": "OBK_02", "id": 1}, "reqs": []}, #? Basement Stairs Bombable Wall -> Basement Stairs Lower Door South

    {"from": {"map": "OBK_02", "id": 0}, "to": {"map": "OBK_02", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Basement Stairs Upper Door -> HiddenPanel (StarPiece)

    # OBK_03 Basement
    {"from": {"map": "OBK_03", "id": 0}, "to": {"map": "OBK_02", "id": 1}, "reqs": []}, # Basement Upper Door North -> Basement Stairs Lower Door South
    {"from": {"map": "OBK_03", "id": 1}, "to": {"map": "OBK_04", "id": 0}, "reqs": []}, # Basement Upper Door East -> Super Boots Room Vanishing Door
    #{"from": {"map": "OBK_03", "id": 2}, "to": {"map": None, "id": None}, "reqs":  []}, # Basement Fall From Ceiling

    {"from": {"map": "OBK_03", "id": 0}, "to": {"map": "OBK_03", "id": 1}, "reqs": []}, #? Basement Upper Door North -> Basement Upper Door East
    {"from": {"map": "OBK_03", "id": 1}, "to": {"map": "OBK_03", "id": 0}, "reqs": []}, #? Basement Upper Door East -> Basement Upper Door North
    {"from": {"map": "OBK_03", "id": 0}, "to": {"map": "OBK_03", "id": 2}, "reqs": [["RF_OBK03_BuiltStairs"]]}, #? Basement Upper Door North -> Basement Fall From Ceiling
    {"from": {"map": "OBK_03", "id": 2}, "to": {"map": "OBK_03", "id": 0}, "reqs": [["RF_OBK03_BuiltStairs"]]}, #? Basement Fall From Ceiling -> Basement Upper Door North

    {"from": {"map": "OBK_03", "id": 2}, "to": {"map": "OBK_03", "id": 2}, "reqs": [["Boots"]], "pseudoitems": ["RF_OBK03_BuiltStairs"]}, #+ Basement Fall From Ceiling Activate Stairs

    {"from": {"map": "OBK_03", "id": 0},           "to": {"map": "OBK_03", "id": "CrateA"},    "reqs": [["SuperBoots"]]}, #* Basement Upper Door North -> CrateA (SuperShroom)
    {"from": {"map": "OBK_03", "id": 2},           "to": {"map": "OBK_03", "id": "GiftA"},     "reqs": [["Parakarry"],["Letter11"]]}, #* Basement Fall From Ceiling -> GiftA (StarPiece)
    {"from": {"map": "OBK_03", "id": 2},           "to": {"map": "OBK_03", "id": "ShopItemA"}, "reqs": [["RF_OpenedGustyGulch"]]}, #* Basement Fall From Ceiling -> ShopItemA (Mystery)
    {"from": {"map": "OBK_03", "id": "ShopItemA"}, "to": {"map": "OBK_03", "id": "ShopItemB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemB (StopWatch)
    {"from": {"map": "OBK_03", "id": "ShopItemA"}, "to": {"map": "OBK_03", "id": "ShopItemC"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemC (SnowmanDoll)
    {"from": {"map": "OBK_03", "id": "ShopItemA"}, "to": {"map": "OBK_03", "id": "ShopItemD"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemD (MapleSyrup)
    {"from": {"map": "OBK_03", "id": "ShopItemA"}, "to": {"map": "OBK_03", "id": "ShopItemE"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemE (LifeShroom)
    {"from": {"map": "OBK_03", "id": "ShopItemA"}, "to": {"map": "OBK_03", "id": "ShopItemF"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemF (SuperShroom)

    # OBK_04 Super Boots Room
    #{"from": {"map": "OBK_04", "id": 0}, "to": {"map": None, "id": None},  "reqs": []}, # Super Boots Room Vanishing Door
    {"from": {"map": "OBK_04", "id": 1}, "to": {"map": "OBK_03", "id": 2}, "reqs": []}, # Super Boots Room Hole Under Planks -> Basement Fall From Ceiling

    {"from": {"map": "OBK_04", "id": 0}, "to": {"map": "OBK_04", "id": 1}, "reqs": [["RF_OBK04_OpenedBigChest"]]}, #? Super Boots Room Vanishing Door -> Super Boots Room Hole Under Planks
    {"from": {"map": "OBK_04", "id": 1}, "to": {"map": "OBK_04", "id": 0}, "reqs": []}, #? Super Boots Room Hole Under Planks -> Super Boots Room Vanishing Door

    {"from": {"map": "OBK_04", "id": 0}, "to": {"map": "OBK_04", "id": "CrateA"},      "reqs": [["SuperBoots"]]}, #* Super Boots Room Vanishing Door -> CrateA (MapleSyrup)
    {"from": {"map": "OBK_04", "id": 0}, "to": {"map": "OBK_04", "id": "BigChest"},    "reqs": [["Boots","Hammer"]], "pseudoitems": ["RF_OBK04_OpenedBigChest"]}, #* Super Boots Room Vanishing Door -> BigChest (SuperBoots)
    {"from": {"map": "OBK_04", "id": 0}, "to": {"map": "OBK_04", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Super Boots Room Vanishing Door -> HiddenPanel (StarPiece)

    # OBK_05 Pot Room
    {"from": {"map": "OBK_05", "id": 0}, "to": {"map": "OBK_01", "id": 2}, "reqs": []}, # Pot Room Door South -> Foyer Lower Door
    {"from": {"map": "OBK_05", "id": 1}, "to": {"map": "OBK_06", "id": 0}, "reqs": []}, # Pot Room Hole Under Planks -> Library Fall From Ceiling

    {"from": {"map": "OBK_05", "id": 0}, "to": {"map": "OBK_05", "id": 1}, "reqs": [["SuperBoots"], ["Bombette"]]}, #? Pot Room Door South -> Pot Room Hole Under Planks
    {"from": {"map": "OBK_05", "id": 1}, "to": {"map": "OBK_05", "id": 0}, "reqs": []}, #? Pot Room Hole Under Planks -> Pot Room Door South

    {"from": {"map": "OBK_05", "id": 0},        "to": {"map": "OBK_05", "id": "CrateA"}, "reqs": [["SuperBoots"]]}, #* Pot Room Door South -> CrateA (Apple)
    {"from": {"map": "OBK_05", "id": "CrateA"}, "to": {"map": "OBK_05", "id": "CrateB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> CrateB (Apple)

    # OBK_06 Library
    #{"from": {"map": "OBK_06", "id": 0}, "to": {"map": None, "id": None},  "reqs": []}, # Library Fall From Ceiling
    {"from": {"map": "OBK_06", "id": 1}, "to": {"map": "OBK_02", "id": 2}, "reqs": []}, # Library Bombable Wall -> Basement Stairs Bombable Wall

    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_06", "id": 1}, "reqs": [["Bombette"]]}, #? Library Fall From Ceiling -> Library Bombable Wall

    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_06", "id": "CrateA"}, "reqs": [["SuperBoots"]]}, #* Library Fall From Ceiling -> CrateA (StarPiece)
    {"from": {"map": "OBK_06", "id": 0}, "to": {"map": "OBK_06", "id": "ItemA"},  "reqs": [["Parakarry"]]}, #* Library Fall From Ceiling -> ItemA (BooPortrait)

    # OBK_07 Record Player Room
    {"from": {"map": "OBK_07", "id": 0}, "to": {"map": "OBK_01", "id": 3}, "reqs": []}, # Record Player Room Door South -> Foyer Upper Door West

    {"from": {"map": "OBK_07", "id": 0}, "to": {"map": "OBK_07", "id": "ChestA"}, "reqs": [["BooRecord"]]}, #* Record Player Room Door South -> ChestA (BooWeight)

    # OBK_08 Record Room
    {"from": {"map": "OBK_08", "id": 0}, "to": {"map": "OBK_01", "id": 4}, "reqs": []}, # Record Room Door South -> Foyer Upper Door East

    {"from": {"map": "OBK_08", "id": 0}, "to": {"map": "OBK_08", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Record Room Door South -> HiddenPanel (StarPiece)
    {"from": {"map": "OBK_08", "id": 0}, "to": {"map": "OBK_08", "id": "ItemA"},       "reqs": [["Boots","Hammer"]]}, #* Record Room Door South -> ItemA (BooRecord)

    # OBK_09 Lady Bow's Room
    {"from": {"map": "OBK_09", "id": 0}, "to": {"map": "OBK_01", "id": 5}, "reqs": []}, # Lady Bow's Room Door South West -> Foyer Third Floor Door West
    {"from": {"map": "OBK_09", "id": 1}, "to": {"map": "OBK_01", "id": 6}, "reqs": []}, # Lady Bow's Room Door South East -> Foyer Third Floor Door East

    {"from": {"map": "OBK_09", "id": 0}, "to": {"map": "OBK_09", "id": 1}, "reqs": []}, #? Lady Bow's Room Door South West -> Lady Bow's Room Door South East
    {"from": {"map": "OBK_09", "id": 1}, "to": {"map": "OBK_09", "id": 0}, "reqs": []}, #? Lady Bow's Room Door South East -> Lady Bow's Room Door South West

    {"from": {"map": "OBK_09", "id": 0}, "to": {"map": "OBK_09", "id": "Partner"}, "reqs": []}, #* Lady Bow's Room Door South West -> Partner (Bow)

    {"from": {"map": "OBK_09", "id": 0}, "to": {"map": "OBK_09", "id": 0}, "reqs": [], "pseudoitems": ["RF_OpenedGustyGulch"]}, #+ Lady Bow's Room Door South West
]
