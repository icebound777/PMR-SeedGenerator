from rando_modules.simulate import *

"""This file represents all edges of the world graph that have origin-nodes in the NOK (Koopa Region) area."""
edges_nok = [
    # NOK_01 Koopa Village 1
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_13", "id": 1}, "reqs": []}, # Koopa Village 1 Exit Left -> Pleasant Crossroads Exit Bottom
    {"from": {"map": "NOK_01", "id": 1}, "to": {"map": "NOK_02", "id": 0}, "reqs": []}, # Koopa Village 1 Exit Right -> Koopa Village 2 Exit Left
    
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": 1}, "reqs": []}, #? Koopa Village 1 Exit Left -> Koopa Village 1 Exit Right
    {"from": {"map": "NOK_01", "id": 1}, "to": {"map": "NOK_01", "id": 0}, "reqs": []}, #? Koopa Village 1 Exit Right -> Koopa Village 1 Exit Left
    
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "Bush1_Drop1A"},  "reqs": []}, #* Koopa Village 1 Exit Left -> Bush1_Drop1A (Coin)
    {"from": {"map": "NOK_01", "id": "Bush1_Drop1A"},  "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* Bush1_Drop1A (Coin) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "Bush3_Drop1A"},  "reqs": []}, #* Koopa Village 1 Exit Left -> Bush3_Drop1A (DriedShroom)
    {"from": {"map": "NOK_01", "id": "Bush3_Drop1A"},  "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* Bush3_Drop1A (DriedShroom) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "Bush4_Drop1A"},  "reqs": []}, #* Koopa Village 1 Exit Left -> Bush4_Drop1A (KoopaLeaf)
    {"from": {"map": "NOK_01", "id": "Bush4_Drop1A"},  "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* Bush4_Drop1A (KoopaLeaf) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "Bush5_Drop1A"},  "reqs": []}, #* Koopa Village 1 Exit Left -> Bush5_Drop1A (Coin)
    {"from": {"map": "NOK_01", "id": "Bush5_Drop1A"},  "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* Bush5_Drop1A (Coin) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "Bush6A_Drop1A"}, "reqs": [require(favor="favor_ch5_1")]}, #* Koopa Village 1 Exit Left -> Bush6A_Drop1A (Glasses)
    {"from": {"map": "NOK_01", "id": "Bush6A_Drop1A"}, "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* Bush6A_Drop1A (Glasses) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "Bush7A_Drop1A"}, "reqs": [require(favor="favor_ch2_1")]}, #* Koopa Village 1 Exit Left -> Bush7A_Drop1A (EmptyWallet)
    {"from": {"map": "NOK_01", "id": "Bush7A_Drop1A"}, "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* Bush7A_Drop1A (EmptyWallet) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "HiddenPanel"},   "reqs": [can_flip_panels]}, #* Koopa Village 1 Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "NOK_01", "id": "HiddenPanel"},   "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* HiddenPanel (StarPiece) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "ShopItemA"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemA (DizzyDial)
    {"from": {"map": "NOK_01", "id": "ShopItemA"},     "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* ShopItemA (DizzyDial) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "ShopItemB"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemB (POWBlock)
    {"from": {"map": "NOK_01", "id": "ShopItemB"},     "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* ShopItemB (POWBlock) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "ShopItemC"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemC (FireFlower)
    {"from": {"map": "NOK_01", "id": "ShopItemC"},     "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* ShopItemC (FireFlower) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "ShopItemD"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemD (HoneySyrup)
    {"from": {"map": "NOK_01", "id": "ShopItemD"},     "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* ShopItemD (HoneySyrup) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "ShopItemE"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemE (VoltShroom)
    {"from": {"map": "NOK_01", "id": "ShopItemE"},     "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* ShopItemE (VoltShroom) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "ShopItemF"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemF (Mushroom)
    {"from": {"map": "NOK_01", "id": "ShopItemF"},     "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* ShopItemF (Mushroom) -> Koopa Village 1 Exit Left

    # NOK_02 Koopa Village 2
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_01", "id": 1}, "reqs": []}, # Koopa Village 2 Exit Left -> Koopa Village 1 Exit Right
    {"from": {"map": "NOK_02", "id": 1}, "to": {"map": "NOK_03", "id": 0}, "reqs": []}, # Koopa Village 2 Exit Top -> Behind Koopa Village Exit Left
    {"from": {"map": "NOK_02", "id": 2}, "to": {"map": "TIK_01", "id": 3}, "reqs": [require(flag="GF_TIK01_Defeated_Blooper")]}, # Koopa Village 2 Blue Pipe -> Warp Zone 1 (B1) Blue Pipe (Center)
    
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 1}, "reqs": []}, #? Koopa Village 2 Exit Left -> Koopa Village 2 Exit Top
    {"from": {"map": "NOK_02", "id": 1}, "to": {"map": "NOK_02", "id": 0}, "reqs": []}, #? Koopa Village 2 Exit Top -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 2}, "reqs": []}, #? Koopa Village 2 Exit Left -> Koopa Village 2 Blue Pipe
    {"from": {"map": "NOK_02", "id": 2}, "to": {"map": "NOK_02", "id": 0}, "reqs": []}, #? Koopa Village 2 Blue Pipe -> Koopa Village 2 Exit Left
    
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "GiftA"},       "reqs": [require(favor="favor_ch0_1")]}, #* Koopa Village 2 Exit Left -> GiftA (KoopaLegends)
    {"from": {"map": "NOK_02", "id": "GiftA"},       "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* GiftA (KoopaLegends) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "GiftB"},       "reqs": [require(item="SleepySheep")]}, #* Koopa Village 2 Exit Left -> GiftB (SilverCredit)
    {"from": {"map": "NOK_02", "id": "GiftB"},       "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* GiftB (SilverCredit) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "GiftC"},       "reqs": [require(item="LifeShroom")]}, #* Koopa Village 2 Exit Left -> GiftC (GoldCredit)
    {"from": {"map": "NOK_02", "id": "GiftC"},       "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* GiftC (GoldCredit) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "ItemA"},       "reqs": []}, #* Koopa Village 2 Exit Left -> ItemA (StarPiece)
    {"from": {"map": "NOK_02", "id": "ItemA"},       "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* ItemA (StarPiece) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "Bush1_Drop1"}, "reqs": []}, #* Koopa Village 2 Exit Left -> Bush1_Drop1 (KoopaLeaf)
    {"from": {"map": "NOK_02", "id": "Bush1_Drop1"}, "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* Bush1_Drop1 (KoopaLeaf) -> Koopa Village 2 Exit Left

    # NOK_03 Behind Koopa Village
    {"from": {"map": "NOK_03", "id": 0}, "to": {"map": "NOK_02", "id": 1}, "reqs": []}, # Behind Koopa Village Exit Left -> Koopa Village 2 Exit Top
    {"from": {"map": "NOK_03", "id": 1}, "to": {"map": "NOK_04", "id": 0}, "reqs": []}, # Behind Koopa Village Exit Right -> Fuzzy Forest Exit Left
    
    {"from": {"map": "NOK_03", "id": 0}, "to": {"map": "NOK_03", "id": 1}, "reqs": []}, #? Behind Koopa Village Exit Left -> Behind Koopa Village Exit Right
    {"from": {"map": "NOK_03", "id": 1}, "to": {"map": "NOK_03", "id": 0}, "reqs": []}, #? Behind Koopa Village Exit Right -> Behind Koopa Village Exit Left
    
    {"from": {"map": "NOK_03", "id": 0},       "to": {"map": "NOK_03", "id": "ItemA"}, "reqs": [require(partner="Kooper")]}, #* Behind Koopa Village Exit Left -> ItemA (HPPlusB)
    {"from": {"map": "NOK_03", "id": "ItemA"}, "to": {"map": "NOK_03", "id": 0},       "reqs": []}, #* ItemA (HPPlusB) -> Behind Koopa Village Exit Left

    # NOK_04 Fuzzy Forest
    {"from": {"map": "NOK_04", "id": 0}, "to": {"map": "NOK_03", "id": 1}, "reqs": []}, # Fuzzy Forest Exit Left -> Behind Koopa Village Exit Right
    
    {"from": {"map": "NOK_04", "id": 0},       "to": {"map": "NOK_04", "id": "GiftA"}, "reqs": []}, #* Fuzzy Forest Exit Left -> GiftA (KoopersShell)
    {"from": {"map": "NOK_04", "id": "GiftA"}, "to": {"map": "NOK_04", "id": 0},       "reqs": []}, #* GiftA (KoopersShell) -> Fuzzy Forest Exit Left

    # NOK_11 Pleasant Path Entry
    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "MAC_01", "id": 1}, "reqs": []}, # Pleasant Path Entry Exit Left -> Plaza District Exit Right
    {"from": {"map": "NOK_11", "id": 1}, "to": {"map": "NOK_12", "id": 0}, "reqs": []}, # Pleasant Path Entry Exit Right -> Pleasant Path Bridge Exit Left
    
    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "NOK_11", "id": 1}, "reqs": []}, #? Pleasant Path Entry Exit Left -> Pleasant Path Entry Exit Right
    {"from": {"map": "NOK_11", "id": 1}, "to": {"map": "NOK_11", "id": 0}, "reqs": []}, #? Pleasant Path Entry Exit Right -> Pleasant Path Entry Exit Left
    
    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "NOK_11", "id": "RBlockA"}, "reqs": []}, #* Pleasant Path Entry Exit Left -> RBlockA (DizzyAttack)
    {"from": {"map": "NOK_11", "id": "RBlockA"}, "to": {"map": "NOK_11", "id": 0}, "reqs": []}, #* RBlockA (DizzyAttack) -> Pleasant Path Entry Exit Left
    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "NOK_11", "id": "YBlockA"}, "reqs": []}, #* Pleasant Path Entry Exit Left -> YBlockA (Coin)
    {"from": {"map": "NOK_11", "id": "YBlockA"}, "to": {"map": "NOK_11", "id": 0}, "reqs": []}, #* YBlockA (Coin) -> Pleasant Path Entry Exit Left
    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "NOK_11", "id": "YBlockB"}, "reqs": []}, #* Pleasant Path Entry Exit Left -> YBlockB (FrightJar)
    {"from": {"map": "NOK_11", "id": "YBlockB"}, "to": {"map": "NOK_11", "id": 0}, "reqs": []}, #* YBlockB (FrightJar) -> Pleasant Path Entry Exit Left

    # NOK_12 Pleasant Path Bridge
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_11", "id": 1}, "reqs": []}, # Pleasant Path Bridge Exit Left -> Pleasant Path Entry Exit Right
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_13", "id": 0}, "reqs": []}, # Pleasant Path Bridge Exit Right -> Pleasant Crossroads Exit Left
    
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": 1}, "reqs": []}, #? Pleasant Path Bridge Exit Left -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": 0}, "reqs": []}, #? Pleasant Path Bridge Exit Right -> Pleasant Path Bridge Exit Left
    
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": "YBlockA"}, "reqs": []}, #* Pleasant Path Bridge Exit Left -> YBlockA (POWBlock)
    {"from": {"map": "NOK_12", "id": "YBlockA"}, "to": {"map": "NOK_12", "id": 0}, "reqs": []}, #* YBlockA (POWBlock) -> Pleasant Path Bridge Exit Left
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": "ItemA"}, "reqs": [require(partner="Kooper")]}, #* Pleasant Path Bridge Exit Right -> ItemA (StarPiece)
    {"from": {"map": "NOK_12", "id": "ItemA"}, "to": {"map": "NOK_12", "id": 1}, "reqs": []}, #* ItemA (StarPiece) -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": "ItemB"}, "reqs": []}, #* Pleasant Path Bridge Exit Right -> ItemB (SleepySheep)
    {"from": {"map": "NOK_12", "id": "ItemB"}, "to": {"map": "NOK_12", "id": 1}, "reqs": []}, #* ItemB (SleepySheep) -> Pleasant Path Bridge Exit Right

    # NOK_13 Pleasant Crossroads
    {"from": {"map": "NOK_13", "id": 0}, "to": {"map": "NOK_12", "id": 1}, "reqs": []}, # Pleasant Crossroads Exit Left -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_13", "id": 1}, "to": {"map": "NOK_01", "id": 0}, "reqs": []}, # Pleasant Crossroads Exit Bottom -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_13", "id": 2}, "to": {"map": "NOK_14", "id": 0}, "reqs": []}, # Pleasant Crossroads Exit Right -> Path to Fortress 1 Exit Left
    
    {"from": {"map": "NOK_13", "id": 0}, "to": {"map": "NOK_13", "id": 1}, "reqs": []}, #? Pleasant Crossroads Exit Left -> Pleasant Crossroads Exit Bottom
    {"from": {"map": "NOK_13", "id": 1}, "to": {"map": "NOK_13", "id": 0}, "reqs": []}, #? Pleasant Crossroads Exit Bottom -> Pleasant Crossroads Exit Left
    {"from": {"map": "NOK_13", "id": 0}, "to": {"map": "NOK_13", "id": 2}, "reqs": []}, #? Pleasant Crossroads Exit Left -> Pleasant Crossroads Exit Right
    {"from": {"map": "NOK_13", "id": 2}, "to": {"map": "NOK_13", "id": 0}, "reqs": []}, #? Pleasant Crossroads Exit Right -> Pleasant Crossroads Exit Left
    
    {"from": {"map": "NOK_13", "id": 0},             "to": {"map": "NOK_13", "id": "HiddenPanel"}, "reqs": [can_flip_panels]}, #* Pleasant Crossroads Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "NOK_13", "id": "HiddenPanel"}, "to": {"map": "NOK_13", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Pleasant Crossroads Exit Left
    {"from": {"map": "NOK_13", "id": 0},             "to": {"map": "NOK_13", "id": "ItemA"},       "reqs": []}, #* Pleasant Crossroads Exit Left -> ItemA (HoneySyrup)
    {"from": {"map": "NOK_13", "id": "ItemA"},       "to": {"map": "NOK_13", "id": 0},             "reqs": []}, #* ItemA (HoneySyrup) -> Pleasant Crossroads Exit Left
    {"from": {"map": "NOK_13", "id": 0},             "to": {"map": "NOK_13", "id": "RBlockA"},     "reqs": []}, #* Pleasant Crossroads Exit Left -> RBlockA (AttackFXB)
    {"from": {"map": "NOK_13", "id": "RBlockA"},     "to": {"map": "NOK_13", "id": 0},             "reqs": []}, #* RBlockA (AttackFXB) -> Pleasant Crossroads Exit Left

    # NOK_14 Path to Fortress 1
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_13", "id": 2}, "reqs": []}, # Path to Fortress 1 Exit Left -> Pleasant Crossroads Exit Right
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_15", "id": 0}, "reqs": []}, # Path to Fortress 1 Exit Right -> Path to Fortress 2 Exit Left
    
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": 1}, "reqs": []}, #? Path to Fortress 1 Exit Left -> Path to Fortress 1 Exit Right
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_14", "id": 0}, "reqs": []}, #? Path to Fortress 1 Exit Right -> Path to Fortress 1 Exit Left
    
    {"from": {"map": "NOK_14", "id": 0},               "to": {"map": "NOK_14", "id": "HiddenPanel"},   "reqs": [can_flip_panels]}, #* Path to Fortress 1 Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "NOK_14", "id": "HiddenPanel"},   "to": {"map": "NOK_14", "id": 0},               "reqs": []}, #* HiddenPanel (StarPiece) -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 0},               "to": {"map": "NOK_14", "id": "ItemA"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemA (Coin)
    {"from": {"map": "NOK_14", "id": "ItemA"},         "to": {"map": "NOK_14", "id": 0},               "reqs": []}, #* ItemA (Coin) -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 0},               "to": {"map": "NOK_14", "id": "ItemB"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemB (Coin)
    {"from": {"map": "NOK_14", "id": "ItemB"},         "to": {"map": "NOK_14", "id": 0},               "reqs": []}, #* ItemB (Coin) -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 0},               "to": {"map": "NOK_14", "id": "ItemC"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemC (Coin)
    {"from": {"map": "NOK_14", "id": "ItemC"},         "to": {"map": "NOK_14", "id": 0},               "reqs": []}, #* ItemC (Coin) -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 0},               "to": {"map": "NOK_14", "id": "ItemD"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemD (Coin)
    {"from": {"map": "NOK_14", "id": "ItemD"},         "to": {"map": "NOK_14", "id": 0},               "reqs": []}, #* ItemD (Coin) -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 0},               "to": {"map": "NOK_14", "id": "ItemE"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemE (Coin)
    {"from": {"map": "NOK_14", "id": "ItemE"},         "to": {"map": "NOK_14", "id": 0},               "reqs": []}, #* ItemE (Coin) -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 0},               "to": {"map": "NOK_14", "id": "ItemF"},         "reqs": [require(partner="Kooper", boots=2)]}, #* Path to Fortress 1 Exit Left -> ItemF (ThunderBolt)
    {"from": {"map": "NOK_14", "id": "ItemF"},         "to": {"map": "NOK_14", "id": 0},               "reqs": []}, #* ItemF (ThunderBolt) -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 1},               "to": {"map": "NOK_14", "id": "HiddenYBlockA"}, "reqs": []}, #* Path to Fortress 1 Exit Right -> HiddenYBlockA (FireFlower)
    {"from": {"map": "NOK_14", "id": "HiddenYBlockA"}, "to": {"map": "NOK_14", "id": 1},               "reqs": []}, #* HiddenYBlockA (FireFlower) -> Path to Fortress 1 Exit Right

    # NOK_15 Path to Fortress 2
    {"from": {"map": "NOK_15", "id": 0}, "to": {"map": "NOK_14", "id": 1}, "reqs": []}, # Path to Fortress 2 Exit Left -> Path to Fortress 1 Exit Right
    {"from": {"map": "NOK_15", "id": 1}, "to": {"map": "TRD_00", "id": 0}, "reqs": []}, # Path to Fortress 2 Exit Bottom Right -> Fortress Exterior Exit Bottom Left
    {"from": {"map": "NOK_15", "id": 2}, "to": {"map": "TRD_00", "id": 4}, "reqs": []}, # Path to Fortress 2 Exit Top Right -> Fortress Exterior Exit Top Left
    {"from": {"map": "NOK_15", "id": 3}, "to": {"map": "NOK_15", "id": 4}, "reqs": []}, # Path to Fortress 2 Bottom Pipe -> Path to Fortress 2 Top Pipe
    {"from": {"map": "NOK_15", "id": 4}, "to": {"map": "NOK_15", "id": 3}, "reqs": []}, # Path to Fortress 2 Top Pipe -> Path to Fortress 2 Bottom Pipe

    {"from": {"map": "NOK_15", "id": 0}, "to": {"map": "NOK_15", "id": 1}, "reqs": []}, #? Path to Fortress 2 Exit Left -> Path to Fortress 2 Exit Bottom Right
    {"from": {"map": "NOK_15", "id": 1}, "to": {"map": "NOK_15", "id": 0}, "reqs": []}, #? Path to Fortress 2 Exit Bottom Right -> Path to Fortress 2 Exit Left
    {"from": {"map": "NOK_15", "id": 1}, "to": {"map": "NOK_15", "id": 3}, "reqs": [require(partner="Bombette")]}, #? Path to Fortress 2 Exit Bottom Right -> Path to Fortress 2 Bottom Pipe
    {"from": {"map": "NOK_15", "id": 3}, "to": {"map": "NOK_15", "id": 1}, "reqs": []}, #? Path to Fortress 2 Bottom Pipe -> Path to Fortress 2 Exit Bottom Right
    {"from": {"map": "NOK_15", "id": 4}, "to": {"map": "NOK_15", "id": 2}, "reqs": []}, #? Path to Fortress 2 Top Pipe -> Path to Fortress 2 Exit Top Right
    {"from": {"map": "NOK_15", "id": 2}, "to": {"map": "NOK_15", "id": 4}, "reqs": []}, #? Path to Fortress 2 Exit Top Right -> Path to Fortress 2 Top Pipe
    {"from": {"map": "NOK_15", "id": 4}, "to": {"map": "NOK_15", "id": 1}, "reqs": []}, #? Path to Fortress 2 Top Pipe -> Path to Fortress 2 Exit Bottom Right
    
    {"from": {"map": "NOK_15", "id": 0},              "to": {"map": "NOK_15", "id": "Tree1_Drop1A"}, "reqs": []}, #* Path to Fortress 2 Exit Left -> Tree1_Drop1A (StarPiece)
    {"from": {"map": "NOK_15", "id": "Tree1_Drop1A"}, "to": {"map": "NOK_15", "id": 0},              "reqs": []}, #* Tree1_Drop1A (StarPiece) -> Path to Fortress 2 Exit Left
]