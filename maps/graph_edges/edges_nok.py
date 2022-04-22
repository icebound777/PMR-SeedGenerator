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
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "Bush6A_Drop1A"}, "reqs": [require(favor="FAVOR_6_01_active")]}, #* Koopa Village 1 Exit Left -> Bush6A_Drop1A (KootGlasses)
    {"from": {"map": "NOK_01", "id": "Bush6A_Drop1A"}, "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* Bush6A_Drop1A (KootGlasses) -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": "Bush7A_Drop1A"}, "reqs": [require(favor="FAVOR_3_01_active")]}, #* Koopa Village 1 Exit Left -> Bush7A_Drop1A (KootEmptyWallet)
    {"from": {"map": "NOK_01", "id": "Bush7A_Drop1A"}, "to": {"map": "NOK_01", "id": 0},               "reqs": []}, #* Bush7A_Drop1A (KootEmptyWallet) -> Koopa Village 1 Exit Left
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

    {"from": {"map": "NOK_01", "id": 0},               "to": {"map": "NOK_01", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_NOK_1",
                                                                                                                     "StarPiece_NOK_2",
                                                                                                                     "StarPiece_NOK_3",
                                                                                                                     "StarPiece_NOK_4",
                                                                                                                     "StarPiece_NOK_5",
                                                                                                                     "StarPiece_NOK_6",
                                                                                                                     "StarPiece_NOK_7",
                                                                                                                     "StarPiece_NOK_8"]}, #+ Quizmo StarPieces

    # NOK_02 Koopa Village 2
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_01", "id": 1}, "reqs": []}, # Koopa Village 2 Exit Left -> Koopa Village 1 Exit Right
    {"from": {"map": "NOK_02", "id": 1}, "to": {"map": "NOK_03", "id": 0}, "reqs": []}, # Koopa Village 2 Exit Top -> Behind Koopa Village Exit Left
    {"from": {"map": "NOK_02", "id": 2}, "to": {"map": "TIK_01", "id": 3}, "reqs": []}, # Koopa Village 2 Blue Pipe -> Warp Zone 1 (B1) Blue Pipe (Center)
    
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 1}, "reqs": []}, #? Koopa Village 2 Exit Left -> Koopa Village 2 Exit Top
    {"from": {"map": "NOK_02", "id": 1}, "to": {"map": "NOK_02", "id": 0}, "reqs": []}, #? Koopa Village 2 Exit Top -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 2}, "reqs": [require(flag="GF_TIK01_WarpPipes")]}, #? Koopa Village 2 Exit Left -> Koopa Village 2 Blue Pipe
    {"from": {"map": "NOK_02", "id": 2}, "to": {"map": "NOK_02", "id": 0}, "reqs": []}, #? Koopa Village 2 Blue Pipe -> Koopa Village 2 Exit Left
    
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "GiftA"},       "reqs": [require(favor="FAVOR_1_01_active")]}, #* Koopa Village 2 Exit Left -> GiftA (KootKoopaLegends)
    {"from": {"map": "NOK_02", "id": "GiftA"},       "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* GiftA (KootKoopaLegends) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "ItemA"},       "reqs": [require(flag="RF_Ch1_Fuzzies_Banished")]}, #* Koopa Village 2 Exit Left -> ItemA (StarPiece)
    {"from": {"map": "NOK_02", "id": "ItemA"},       "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* ItemA (StarPiece) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "Bush1_Drop1"}, "reqs": []}, #* Koopa Village 2 Exit Left -> Bush1_Drop1 (KoopaLeaf)
    {"from": {"map": "NOK_02", "id": "Bush1_Drop1"}, "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* Bush1_Drop1 (KoopaLeaf) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "Partner"},     "reqs": [require(item="KooperShell")]}, #* Koopa Village 2 Exit Left -> Partner (Kooper)
    {"from": {"map": "NOK_02", "id": "Partner"},     "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* Partner (Kooper) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "GiftD"},       "reqs": [require(item="Artifact"),require(flag="RF_Ch1_Fuzzies_Banished"),require(flag=["RF_CanVisitDesertCamp","RF_Ch2_SavedStarSpirit"])]}, #* Koopa Village 2 Exit Left -> GiftD (StarPiece)
    {"from": {"map": "NOK_02", "id": "GiftD"},       "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* GiftD (StarPiece) -> Koopa Village 2 Exit Left
    # Koopa Koot Initial Favors (*MB_SpiritsRescued < 1)
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift00"},  "reqs": [require(item="KootKoopaLegends"),require(flag="RF_Ch1_Fuzzies_Banished")], "pseudoitems": ["FAVOR_1_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift00 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift00"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift00 (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift01"},  "reqs": [require(item="SleepySheep"),require(favor="FAVOR_1_01_done")], "pseudoitems": ["FAVOR_1_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift01 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift01"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift01 (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "GiftB"},       "reqs": [require(favor="FAVOR_1_02_done")]}, #* Koopa Village 2 Exit Left -> GiftB (SilverCredit)
    {"from": {"map": "NOK_02", "id": "GiftB"},       "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* GiftB (SilverCredit) -> Koopa Village 2 Exit Left
    # Koopa Koot Favors (*MB_SpiritsRescued < 2)
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift02"},  "reqs": [require(item="KootTheTape"),require(favor="FAVOR_1_02_done"),require(starspirits=1)], "pseudoitems": ["FAVOR_2_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift02 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift02"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift02 (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift03"},  "reqs": [require(item="KoopaLeaf"),require(flag="RF_CanVisitTayceT"),require(favor="FAVOR_2_01_done"),require(starspirits=1)], "pseudoitems": ["FAVOR_2_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift03 (StarPiece)
    {"from": {"map": "NOK_02", "id": "KootGift03"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift03 (StarPiece) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift04"},  "reqs": [require(item="KootLuigiAutograph"),require(favor="FAVOR_2_02_done"),require(starspirits=1)], "pseudoitems": ["FAVOR_2_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift04 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift04"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift04 (Coin) -> Koopa Village 2 Exit Left
    # Koopa Koot Favors (*MB_SpiritsRescued < 3)
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift05"},  "reqs": [require(item="KootEmptyWallet"),require(favor="FAVOR_2_03_done"),require(starspirits=2)], "pseudoitems": ["FAVOR_3_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift05 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift05"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift05 (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift06"},  "reqs": [require(item="TastyTonic"),require(favor="FAVOR_3_01_done"),require(starspirits=2)], "pseudoitems": ["FAVOR_3_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift06 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift06"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift06 (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift07"},  "reqs": [require(item="KootMerluvleeAutograph"),require(favor="FAVOR_3_02_done"),require(starspirits=2)], "pseudoitems": ["FAVOR_3_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift07 (StarPiece)
    {"from": {"map": "NOK_02", "id": "KootGift07"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift07 (StarPiece) -> Koopa Village 2 Exit Left
    # Koopa Koot Favors (*MB_SpiritsRescued < 4)
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift08"},  "reqs": [require(flag="RF_CanReadToadTownNews"),require(favor="FAVOR_3_03_done"),require(starspirits=3)], "pseudoitems": ["FAVOR_4_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift08 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift08"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift08 (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift09"},  "reqs": [require(item="LifeShroom"),require(favor="FAVOR_4_01_done"),require(starspirits=3)], "pseudoitems": ["FAVOR_4_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift09 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift09"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift09 (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "GiftC"},       "reqs": [require(favor="FAVOR_4_02_done")]}, #* Koopa Village 2 Exit Left -> GiftC (GoldCredit)
    {"from": {"map": "NOK_02", "id": "GiftC"},       "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* GiftC (GoldCredit) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift0A"},  "reqs": [require(item="Goomnut"),require(flag="RF_CanVisitTayceT"),require(favor="FAVOR_4_02_done"),require(starspirits=3)], "pseudoitems": ["FAVOR_4_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift0A (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift0A"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift0A (Coin) -> Koopa Village 2 Exit Left
    # Koopa Koot Favors (*MB_SpiritsRescued < 5)
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift0B"},  "reqs": [require(favor="FAVOR_4_03_done"),require(starspirits=4)], "pseudoitems": ["FAVOR_5_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift0B (StarPiece)
    {"from": {"map": "NOK_02", "id": "KootGift0B"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift0B (StarPiece) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift0C"},  "reqs": [require(item="KootOldPhoto"),require(favor="FAVOR_5_01_done"),require(starspirits=4)], "pseudoitems": ["FAVOR_5_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift0C (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift0C"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift0C (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift0D"},  "reqs": [require(item="DriedPasta"),require(flag="RF_CanVisitTayceT"),require(favor="FAVOR_5_02_done"),require(starspirits=4)], "pseudoitems": ["FAVOR_5_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift0D (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift0D"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift0D (Coin) -> Koopa Village 2 Exit Left
    # Koopa Koot Favors (*MB_SpiritsRescued < 6)
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift0E"},  "reqs": [require(item="KootGlasses"),require(favor="FAVOR_5_03_done"),require(starspirits=5)], "pseudoitems": ["FAVOR_6_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift0E (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift0E"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift0E (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift0F"},  "reqs": [require(item="Lime"),require(favor="FAVOR_6_01_done"),require(starspirits=5)], "pseudoitems": ["FAVOR_6_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift0F (StarPiece)
    {"from": {"map": "NOK_02", "id": "KootGift0F"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift0F (StarPiece) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift10"},  "reqs": [require(item="CakeMix"),require(flag="RF_CanVisitTayceT"),require(favor="FAVOR_6_02_done"),require(starspirits=5)], "pseudoitems": ["FAVOR_6_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift10 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift10"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift10 (Coin) -> Koopa Village 2 Exit Left
    # Koopa Koot Favors (*MB_SpiritsRescued >= 6)
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift11"},  "reqs": [require(item="KootPackage"),require(favor="FAVOR_6_03_done"),require(starspirits=6)], "pseudoitems": ["FAVOR_7_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift11 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift11"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift11 (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift12"},  "reqs": [require(item="Coconut"),require(favor="FAVOR_7_01_done"),require(starspirits=6)], "pseudoitems": ["FAVOR_7_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift12 (Coin)
    {"from": {"map": "NOK_02", "id": "KootGift12"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift12 (Coin) -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": "KootGift13"},  "reqs": [require(item="KootRedJar"),require(favor="FAVOR_7_02_done"),require(starspirits=6)]}, #* Koopa Village 2 Exit Left -> KootGift13 (StarPiece)
    {"from": {"map": "NOK_02", "id": "KootGift13"},  "to": {"map": "NOK_02", "id": 0},             "reqs": []}, #* KootGift13 (StarPiece) -> Koopa Village 2 Exit Left
    #+ Koopa Koot Favors: Active Favor Flags
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": 0},             "reqs": [require(flag="RF_Ch1_Fuzzies_Banished")], "pseudoitems": ["FAVOR_1_01_active"]}, #+ Get KootKoopaLegends from Kolorado's Wife
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": 0},             "reqs": [require(favor="FAVOR_1_02_done"), require(starspirits=1)], "pseudoitems": ["FAVOR_2_01_active"]}, #+ Get KootTheTape from Goompa
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": 0},             "reqs": [require(favor="FAVOR_2_02_done"), require(starspirits=1)], "pseudoitems": ["FAVOR_2_03_active"]}, #+ Get KootLuigiAutgraph from Luigi
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": 0},             "reqs": [require(favor="FAVOR_2_03_done"), require(starspirits=2)], "pseudoitems": ["FAVOR_3_01_active"]}, #+ Get KootEmptyWallet from Bush
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": 0},             "reqs": [require(favor="FAVOR_3_02_done"), require(starspirits=2)], "pseudoitems": ["FAVOR_3_03_active"]}, #+ Get KootMerluvleeAutograph from Merluvlee
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": 0},             "reqs": [require(favor="FAVOR_5_01_done"), require(starspirits=4)], "pseudoitems": ["FAVOR_5_02_active"]}, #+ Get KootOldPhoto from Bruce
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": 0},             "reqs": [require(favor="FAVOR_5_03_done"), require(starspirits=5)], "pseudoitems": ["FAVOR_6_01_active"]}, #+ Get KootOldPhoto from Bruce
    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": 0},             "reqs": [require(favor="FAVOR_6_03_done"), require(starspirits=6)], "pseudoitems": ["FAVOR_7_01_active"]}, #+ Get KootOldPhoto from Bruce

    {"from": {"map": "NOK_02", "id": 0},             "to": {"map": "NOK_02", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_NOK_1",
                                                                                                                   "StarPiece_NOK_2",
                                                                                                                   "StarPiece_NOK_3",
                                                                                                                   "StarPiece_NOK_4",
                                                                                                                   "StarPiece_NOK_5",
                                                                                                                   "StarPiece_NOK_6",
                                                                                                                   "StarPiece_NOK_7",
                                                                                                                   "StarPiece_NOK_8"]}, #+ Quizmo StarPieces

    # NOK_03 Behind Koopa Village
    {"from": {"map": "NOK_03", "id": 0}, "to": {"map": "NOK_02", "id": 1}, "reqs": []}, # Behind Koopa Village Exit Left -> Koopa Village 2 Exit Top
    {"from": {"map": "NOK_03", "id": 1}, "to": {"map": "NOK_04", "id": 0}, "reqs": []}, # Behind Koopa Village Exit Right -> Fuzzy Forest Exit Left
    
    {"from": {"map": "NOK_03", "id": 0}, "to": {"map": "NOK_03", "id": 1}, "reqs": []}, #? Behind Koopa Village Exit Left -> Behind Koopa Village Exit Right
    {"from": {"map": "NOK_03", "id": 1}, "to": {"map": "NOK_03", "id": 0}, "reqs": []}, #? Behind Koopa Village Exit Right -> Behind Koopa Village Exit Left
    
    {"from": {"map": "NOK_03", "id": 0},       "to": {"map": "NOK_03", "id": "ItemA"}, "reqs": [require(partner=["Kooper","Parakarry"])]}, #* Behind Koopa Village Exit Left -> ItemA (HPPlusB)
    {"from": {"map": "NOK_03", "id": "ItemA"}, "to": {"map": "NOK_03", "id": 0},       "reqs": []}, #* ItemA (HPPlusB) -> Behind Koopa Village Exit Left

    # NOK_04 Fuzzy Forest
    {"from": {"map": "NOK_04", "id": 0}, "to": {"map": "NOK_03", "id": 1}, "reqs": []}, # Fuzzy Forest Exit Left -> Behind Koopa Village Exit Right
    
    {"from": {"map": "NOK_04", "id": 0},       "to": {"map": "NOK_04", "id": "GiftA"}, "reqs": [require(hammer=1)], "pseudoitems": ["RF_Ch1_Fuzzies_Banished"]}, #* Fuzzy Forest Exit Left -> GiftA (KooperShell)
    {"from": {"map": "NOK_04", "id": "GiftA"}, "to": {"map": "NOK_04", "id": 0},       "reqs": []}, #* GiftA (KooperShell) -> Fuzzy Forest Exit Left

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
    
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": 1}, "reqs": [require(flag="MF_NOK12_BuiltBridge")]}, #? Pleasant Path Bridge Exit Left -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": 0}, "reqs": [require(flag="MF_NOK12_BuiltBridge")]}, #? Pleasant Path Bridge Exit Right -> Pleasant Path Bridge Exit Left
    
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": 0}, "reqs": [can_shake_trees], "pseudoitems": ["MF_NOK12_BuiltBridge"]}, #+ Pleasant Path Bridge Exit Left
    
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
    {"from": {"map": "NOK_13", "id": 0},             "to": {"map": "NOK_13", "id": "RBlockA"},     "reqs": [require(hammer=1, boots=2, partner=["Kooper","Bombette"])]}, #* Pleasant Crossroads Exit Left -> RBlockA (AttackFXB)
    {"from": {"map": "NOK_13", "id": "RBlockA"},     "to": {"map": "NOK_13", "id": 0},             "reqs": []}, #* RBlockA (AttackFXB) -> Pleasant Crossroads Exit Left

    # NOK_14 Path to Fortress 1
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_13", "id": 2}, "reqs": []}, # Path to Fortress 1 Exit Left -> Pleasant Crossroads Exit Right
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_15", "id": 0}, "reqs": []}, # Path to Fortress 1 Exit Right -> Path to Fortress 2 Exit Left
    
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": 1}, "reqs": [require(flag="MF_NOK14_BuiltBridge")]}, #? Path to Fortress 1 Exit Left -> Path to Fortress 1 Exit Right
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_14", "id": 0}, "reqs": [require(flag="MF_NOK14_BuiltBridge")]}, #? Path to Fortress 1 Exit Right -> Path to Fortress 1 Exit Left
    
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": 0}, "reqs": [require(partner="Kooper")], "pseudoitems": ["MF_NOK14_BuiltBridge"]}, #+ Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_14", "id": 1}, "reqs": [], "pseudoitems": ["MF_NOK14_BuiltBridge"]}, #+ Path to Fortress 1 Exit Left
    
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
    {"from": {"map": "NOK_14", "id": 0},               "to": {"map": "NOK_14", "id": "ItemF"},         "reqs": [require(partner="Kooper", boots=3)]}, #* Path to Fortress 1 Exit Left -> ItemF (ThunderBolt)
    {"from": {"map": "NOK_14", "id": "ItemF"},         "to": {"map": "NOK_14", "id": 0},               "reqs": []}, #* ItemF (ThunderBolt) -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 1},               "to": {"map": "NOK_14", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt",flag="RF_HiddenBlocksVisible")]}, #* Path to Fortress 1 Exit Right -> HiddenYBlockA (FireFlower)
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
    {"from": {"map": "NOK_15", "id": 3}, "to": {"map": "NOK_15", "id": 1}, "reqs": [require(partner="Bombette")]}, #? Path to Fortress 2 Bottom Pipe -> Path to Fortress 2 Exit Bottom Right
    {"from": {"map": "NOK_15", "id": 4}, "to": {"map": "NOK_15", "id": 2}, "reqs": []}, #? Path to Fortress 2 Top Pipe -> Path to Fortress 2 Exit Top Right
    {"from": {"map": "NOK_15", "id": 2}, "to": {"map": "NOK_15", "id": 4}, "reqs": []}, #? Path to Fortress 2 Exit Top Right -> Path to Fortress 2 Top Pipe
    {"from": {"map": "NOK_15", "id": 4}, "to": {"map": "NOK_15", "id": 1}, "reqs": []}, #? Path to Fortress 2 Top Pipe -> Path to Fortress 2 Exit Bottom Right
    
    {"from": {"map": "NOK_15", "id": 0},              "to": {"map": "NOK_15", "id": "Tree1_Drop1A"}, "reqs": [can_shake_trees]}, #* Path to Fortress 2 Exit Left -> Tree1_Drop1A (StarPiece)
    {"from": {"map": "NOK_15", "id": "Tree1_Drop1A"}, "to": {"map": "NOK_15", "id": 0},              "reqs": []}, #* Tree1_Drop1A (StarPiece) -> Path to Fortress 2 Exit Left
]
