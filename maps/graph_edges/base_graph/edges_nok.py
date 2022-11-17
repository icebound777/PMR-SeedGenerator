"""This file represents all edges of the world graph that have origin-nodes in the NOK (Koopa Region) area."""
edges_nok = [
    # NOK_01 Koopa Village 1
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_13", "id": 1}, "reqs": []}, # Koopa Village 1 Exit Left -> Pleasant Crossroads Exit Bottom
    {"from": {"map": "NOK_01", "id": 1}, "to": {"map": "NOK_02", "id": 0}, "reqs": []}, # Koopa Village 1 Exit Right -> Koopa Village 2 Exit Left

    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": 1}, "reqs": []}, #? Koopa Village 1 Exit Left -> Koopa Village 1 Exit Right
    {"from": {"map": "NOK_01", "id": 1}, "to": {"map": "NOK_01", "id": 0}, "reqs": []}, #? Koopa Village 1 Exit Right -> Koopa Village 1 Exit Left

    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "Bush1_Drop1A"},  "reqs": []}, #* Koopa Village 1 Exit Left -> Bush1_Drop1A (Coin)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "Bush3_Drop1A"},  "reqs": []}, #* Koopa Village 1 Exit Left -> Bush3_Drop1A (DriedShroom)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "Bush4_Drop1A"},  "reqs": []}, #* Koopa Village 1 Exit Left -> Bush4_Drop1A (KoopaLeaf)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "Bush5_Drop1A"},  "reqs": []}, #* Koopa Village 1 Exit Left -> Bush5_Drop1A (Coin)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "Bush6A_Drop1A"}, "reqs": [["FAVOR_6_01_active"]]}, #* Koopa Village 1 Exit Left -> Bush6A_Drop1A (KootGlasses)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "Bush7A_Drop1A"}, "reqs": [["FAVOR_3_01_active"]]}, #* Koopa Village 1 Exit Left -> Bush7A_Drop1A (KootEmptyWallet)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "HiddenPanel"},   "reqs": [["can_flip_panels"]]}, #* Koopa Village 1 Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "GiftA"},         "reqs": [["Parakarry"],["Letter03"]]}, #* Koopa Village 1 Exit Left -> GiftA (StarPiece)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "GiftB"},         "reqs": [["RF_Ch1_Fuzzies_Banished"],["Parakarry"],["Letter14"]]}, #* Koopa Village 1 Exit Left -> GiftB (Letter15)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "GiftC"},         "reqs": [["RF_Ch1_Fuzzies_Banished"],["Parakarry"],["Letter16"]]}, #* Koopa Village 1 Exit Left -> GiftC (Letter17)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "ShopItemA"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemA (DizzyDial)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "ShopItemB"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemB (POWBlock)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "ShopItemC"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemC (FireFlower)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "ShopItemD"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemD (HoneySyrup)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "ShopItemE"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemE (VoltShroom)
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": "ShopItemF"},     "reqs": []}, #* Koopa Village 1 Exit Left -> ShopItemF (Mushroom)

    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_NOK_1",
                                                                                                     #  "StarPiece_NOK_2",
                                                                                                     #  "StarPiece_NOK_3",
                                                                                                     #  "StarPiece_NOK_4",
                                                                                                     #  "StarPiece_NOK_5",
                                                                                                     #  "StarPiece_NOK_6",
                                                                                                     #  "StarPiece_NOK_7",
                                                                                                       "StarPiece_NOK_8"]}, #+ Quizmo StarPieces
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": 0}, "reqs": [[{"starspirits": 1}],["RF_Ch1_Fuzzies_Banished"]], "pseudoitems": ["RF_RadioTradeEvt1"]}, #+ Radio Trade Event 1
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": 0}, "reqs": [[{"starspirits": 3}],["RF_RadioTradeEvt1Done"]], "pseudoitems": ["RF_RadioTradeEvt2"]}, #+ Radio Trade Event 2
    {"from": {"map": "NOK_01", "id": 0}, "to": {"map": "NOK_01", "id": 0}, "reqs": [[{"starspirits": 5}],["RF_RadioTradeEvt2Done"]], "pseudoitems": ["RF_RadioTradeEvt3"]}, #+ Radio Trade Event 3

    # NOK_02 Koopa Village 2
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_01", "id": 1}, "reqs": []}, # Koopa Village 2 Exit Left -> Koopa Village 1 Exit Right
    {"from": {"map": "NOK_02", "id": 1}, "to": {"map": "NOK_03", "id": 0}, "reqs": []}, # Koopa Village 2 Exit Top -> Behind Koopa Village Exit Left
    {"from": {"map": "NOK_02", "id": 2}, "to": {"map": "TIK_01", "id": 3}, "reqs": []}, # Koopa Village 2 Blue Pipe -> Warp Zone 1 (B1) Blue Pipe (Center)

    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 1}, "reqs": []}, #? Koopa Village 2 Exit Left -> Koopa Village 2 Exit Top
    {"from": {"map": "NOK_02", "id": 1}, "to": {"map": "NOK_02", "id": 0}, "reqs": []}, #? Koopa Village 2 Exit Top -> Koopa Village 2 Exit Left
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 2}, "reqs": [["GF_TIK01_WarpPipes"],["Boots"]]}, #? Koopa Village 2 Exit Left -> Koopa Village 2 Blue Pipe
    {"from": {"map": "NOK_02", "id": 2}, "to": {"map": "NOK_02", "id": 0}, "reqs": []}, #? Koopa Village 2 Blue Pipe -> Koopa Village 2 Exit Left

    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "GiftA"},       "reqs": [["FAVOR_1_01_active"]]}, #* Koopa Village 2 Exit Left -> GiftA (KootKoopaLegends)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "ItemA"},       "reqs": [["RF_Ch1_Fuzzies_Banished"],["can_climb_steps"],["can_hit_floating_blocks"]]}, #* Koopa Village 2 Exit Left -> ItemA (StarPiece)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "Bush1_Drop1"}, "reqs": []}, #* Koopa Village 2 Exit Left -> Bush1_Drop1 (KoopaLeaf)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "Partner"},     "reqs": [["KooperShell"]]}, #* Koopa Village 2 Exit Left -> Partner (Kooper)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "GiftD"},       "reqs": [["Artifact"],["RF_Ch1_Fuzzies_Banished"],["RF_CanVisitDesertCamp","RF_Ch2_SavedStarSpirit"]]}, #* Koopa Village 2 Exit Left -> GiftD (StarPiece)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "GiftE"},       "reqs": [["Parakarry"],["Letter25"],["RF_Ch1_Fuzzies_Banished"],["RF_CanVisitDesertCamp","RF_Ch2_SavedStarSpirit"]]}, #* Koopa Village 2 Exit Left -> GiftE (StarPiece)
    # Koopa Koot Initial Favors (*MB_SpiritsRescued < 1)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift00"},  "reqs": [["KootKoopaLegends"],["RF_Ch1_Fuzzies_Banished"]], "pseudoitems": ["FAVOR_1_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift00 (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift01"},  "reqs": [["SleepySheep"],["FAVOR_1_01_done"]], "pseudoitems": ["FAVOR_1_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift01 (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "GiftB"},       "reqs": [["FAVOR_1_02_done"]]}, #* Koopa Village 2 Exit Left -> GiftB (SilverCredit)
    # Koopa Koot Favors (*MB_SpiritsRescued < 2)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift02"},  "reqs": [["KootTheTape"],["FAVOR_1_02_done"],[{"starspirits": 1}]], "pseudoitems": ["FAVOR_2_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift02 (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift03"},  "reqs": [["KoopaTea"],["FAVOR_2_01_done"],[{"starspirits": 1}]], "pseudoitems": ["FAVOR_2_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift03 (StarPiece)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift04"},  "reqs": [["KootLuigiAutograph"],["FAVOR_2_02_done"],[{"starspirits": 1}]], "pseudoitems": ["FAVOR_2_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift04 (Coin)
    # Koopa Koot Favors (*MB_SpiritsRescued < 3)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift05"},  "reqs": [["KootEmptyWallet"],["FAVOR_2_03_done"],[{"starspirits": 2}]], "pseudoitems": ["FAVOR_3_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift05 (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift06"},  "reqs": [["TastyTonic"],["FAVOR_3_01_done"],[{"starspirits": 2}]], "pseudoitems": ["FAVOR_3_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift06 (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift07"},  "reqs": [["KootMerluvleeAutograph"],["FAVOR_3_02_done"],[{"starspirits": 2}]], "pseudoitems": ["FAVOR_3_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift07 (StarPiece)
    # Koopa Koot Favors (*MB_SpiritsRescued < 4)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift08"},  "reqs": [["RF_CanReadToadTownNews"],["FAVOR_3_03_done"],[{"starspirits": 3}]], "pseudoitems": ["FAVOR_4_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift08 (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift09"},  "reqs": [["LifeShroom"],["FAVOR_4_01_done"],[{"starspirits": 3}]], "pseudoitems": ["FAVOR_4_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift09 (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "GiftC"},       "reqs": [["FAVOR_4_02_done"]]}, #* Koopa Village 2 Exit Left -> GiftC (GoldCredit)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift0A"},  "reqs": [["NuttyCake"],["FAVOR_4_02_done"],[{"starspirits": 3}]], "pseudoitems": ["FAVOR_4_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift0A (Coin)
    # Koopa Koot Favors (*MB_SpiritsRescued < 5)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift0B"},  "reqs": [["Bombette"],["FAVOR_4_03_done"],["MF_Ch1_RescuedStarSpirit"],[{"starspirits": 4}]], "pseudoitems": ["FAVOR_5_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift0B (StarPiece)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift0C"},  "reqs": [["KootOldPhoto"],["FAVOR_5_01_done"],[{"starspirits": 4}]], "pseudoitems": ["FAVOR_5_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift0C (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift0D"},  "reqs": [["Koopasta"],["FAVOR_5_02_done"],[{"starspirits": 4}]], "pseudoitems": ["FAVOR_5_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift0D (Coin)
    # Koopa Koot Favors (*MB_SpiritsRescued < 6)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift0E"},  "reqs": [["KootGlasses"],["FAVOR_5_03_done"],[{"starspirits": 5}]], "pseudoitems": ["FAVOR_6_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift0E (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift0F"},  "reqs": [["Lime"],["FAVOR_6_01_done"],[{"starspirits": 5}]], "pseudoitems": ["FAVOR_6_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift0F (StarPiece)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift10"},  "reqs": [["KookyCookie"],["FAVOR_6_02_done"],[{"starspirits": 5}]], "pseudoitems": ["FAVOR_6_03_done"]}, #* Koopa Village 2 Exit Left -> KootGift10 (Coin)
    # Koopa Koot Favors (*MB_SpiritsRescued >= 6)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift11"},  "reqs": [["KootPackage"],["FAVOR_6_03_done"],[{"starspirits": 6}]], "pseudoitems": ["FAVOR_7_01_done"]}, #* Koopa Village 2 Exit Left -> KootGift11 (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift12"},  "reqs": [["Coconut"],["FAVOR_7_01_done"],[{"starspirits": 6}]], "pseudoitems": ["FAVOR_7_02_done"]}, #* Koopa Village 2 Exit Left -> KootGift12 (Coin)
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": "KootGift13"},  "reqs": [["KootRedJar"],["FAVOR_7_02_done"],[{"starspirits": 6}]]}, #* Koopa Village 2 Exit Left -> KootGift13 (StarPiece)
    #+ Koopa Koot Favors: Active Favor Flags
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 0}, "reqs": [["RF_Ch1_Fuzzies_Banished"]], "pseudoitems": ["FAVOR_1_01_active"]}, #+ Get KootKoopaLegends from Kolorado's Wife
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 0}, "reqs": [["FAVOR_1_02_done"], [{"starspirits": 1}]], "pseudoitems": ["FAVOR_2_01_active"]}, #+ Get KootTheTape from Goompa
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 0}, "reqs": [["FAVOR_2_02_done"], [{"starspirits": 1}]], "pseudoitems": ["FAVOR_2_03_active"]}, #+ Get KootLuigiAutgraph from Luigi
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 0}, "reqs": [["FAVOR_2_03_done"], [{"starspirits": 2}]], "pseudoitems": ["FAVOR_3_01_active"]}, #+ Get KootEmptyWallet from Bush
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 0}, "reqs": [["FAVOR_3_02_done"], [{"starspirits": 2}]], "pseudoitems": ["FAVOR_3_03_active"]}, #+ Get KootMerluvleeAutograph from Merluvlee
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 0}, "reqs": [["FAVOR_5_01_done"], [{"starspirits": 4}]], "pseudoitems": ["FAVOR_5_02_active"]}, #+ Get KootOldPhoto from Franky
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 0}, "reqs": [["FAVOR_5_03_done"], [{"starspirits": 5}]], "pseudoitems": ["FAVOR_6_01_active"]}, #+ Get KootGlasses from Bush
    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 0}, "reqs": [["FAVOR_6_03_done"], [{"starspirits": 6}]], "pseudoitems": ["FAVOR_7_01_active"]}, #+ Get KootPackage from Gusty Gulch Boo

    {"from": {"map": "NOK_02", "id": 0}, "to": {"map": "NOK_02", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_NOK_1",
                                                                                                    #   "StarPiece_NOK_2",
                                                                                                    #   "StarPiece_NOK_3",
                                                                                                    #   "StarPiece_NOK_4",
                                                                                                    #   "StarPiece_NOK_5",
                                                                                                    #   "StarPiece_NOK_6",
                                                                                                    #   "StarPiece_NOK_7",
                                                                                                       "StarPiece_NOK_8"]}, #+ Quizmo StarPieces

    # NOK_03 Behind Koopa Village
    {"from": {"map": "NOK_03", "id": 0}, "to": {"map": "NOK_02", "id": 1}, "reqs": []}, # Behind Koopa Village Exit Left -> Koopa Village 2 Exit Top
    {"from": {"map": "NOK_03", "id": 1}, "to": {"map": "NOK_04", "id": 0}, "reqs": []}, # Behind Koopa Village Exit Right -> Fuzzy Forest Exit Left

    {"from": {"map": "NOK_03", "id": 0}, "to": {"map": "NOK_03", "id": 1}, "reqs": []}, #? Behind Koopa Village Exit Left -> Behind Koopa Village Exit Right
    {"from": {"map": "NOK_03", "id": 1}, "to": {"map": "NOK_03", "id": 0}, "reqs": []}, #? Behind Koopa Village Exit Right -> Behind Koopa Village Exit Left

    {"from": {"map": "NOK_03", "id": 0}, "to": {"map": "NOK_03", "id": "ItemA"}, "reqs": [["Kooper","Parakarry"],["can_climb_steps"]]}, #* Behind Koopa Village Exit Left -> ItemA (HPPlusB)

    # NOK_04 Fuzzy Forest
    {"from": {"map": "NOK_04", "id": 0}, "to": {"map": "NOK_03", "id": 1}, "reqs": []}, # Fuzzy Forest Exit Left -> Behind Koopa Village Exit Right

    {"from": {"map": "NOK_04", "id": 0}, "to": {"map": "NOK_04", "id": "GiftA"}, "reqs": [["Hammer"]], "pseudoitems": ["RF_Ch1_Fuzzies_Banished"]}, #* Fuzzy Forest Exit Left -> GiftA (KooperShell)

    # NOK_11 Pleasant Path Entry
    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "MAC_01", "id": 1}, "reqs": []}, # Pleasant Path Entry Exit Left -> Plaza District Exit Right
    {"from": {"map": "NOK_11", "id": 1}, "to": {"map": "NOK_12", "id": 0}, "reqs": []}, # Pleasant Path Entry Exit Right -> Pleasant Path Bridge Exit Left

    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "NOK_11", "id": 1}, "reqs": []}, #? Pleasant Path Entry Exit Left -> Pleasant Path Entry Exit Right
    {"from": {"map": "NOK_11", "id": 1}, "to": {"map": "NOK_11", "id": 0}, "reqs": []}, #? Pleasant Path Entry Exit Right -> Pleasant Path Entry Exit Left

    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "NOK_11", "id": "RBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Pleasant Path Entry Exit Left -> RBlockA (DizzyAttack)
    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "NOK_11", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Pleasant Path Entry Exit Left -> YBlockA (Coin)
    {"from": {"map": "NOK_11", "id": 0}, "to": {"map": "NOK_11", "id": "YBlockB"}, "reqs": [["can_hit_floating_blocks"]]}, #* Pleasant Path Entry Exit Left -> YBlockB (FrightJar)

    # NOK_12 Pleasant Path Bridge
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_11", "id": 1}, "reqs": []}, # Pleasant Path Bridge Exit Left -> Pleasant Path Entry Exit Right
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_13", "id": 0}, "reqs": []}, # Pleasant Path Bridge Exit Right -> Pleasant Crossroads Exit Left

    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": 1}, "reqs": [["MF_NOK12_BuiltBridge"],["can_climb_steps"]]}, #? Pleasant Path Bridge Exit Left -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": 0}, "reqs": [["MF_NOK12_BuiltBridge"]]}, #? Pleasant Path Bridge Exit Right -> Pleasant Path Bridge Exit Left

    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": 0}, "reqs": [["can_shake_trees"]], "pseudoitems": ["MF_NOK12_BuiltBridge"]}, #+ Pleasant Path Bridge Exit Left

    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Pleasant Path Bridge Exit Left -> YBlockA (POWBlock)
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": "ItemA"},   "reqs": [["Kooper"],["MF_NOK12_BuiltBridge"]]}, #* Pleasant Path Bridge Exit Left -> ItemA (StarPiece)
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": "ItemA"},   "reqs": [["Kooper"]]}, #* Pleasant Path Bridge Exit Right -> ItemA (StarPiece)
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": "ItemB"},   "reqs": []}, #* Pleasant Path Bridge Exit Right -> ItemB (SleepySheep)

    # NOK_13 Pleasant Crossroads
    {"from": {"map": "NOK_13", "id": 0}, "to": {"map": "NOK_12", "id": 1}, "reqs": []}, # Pleasant Crossroads Exit Left -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_13", "id": 1}, "to": {"map": "NOK_01", "id": 0}, "reqs": []}, # Pleasant Crossroads Exit Bottom -> Koopa Village 1 Exit Left
    {"from": {"map": "NOK_13", "id": 2}, "to": {"map": "NOK_14", "id": 0}, "reqs": []}, # Pleasant Crossroads Exit Right -> Path to Fortress 1 Exit Left

    {"from": {"map": "NOK_13", "id": 0}, "to": {"map": "NOK_13", "id": 1}, "reqs": []}, #? Pleasant Crossroads Exit Left -> Pleasant Crossroads Exit Bottom
    {"from": {"map": "NOK_13", "id": 1}, "to": {"map": "NOK_13", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Pleasant Crossroads Exit Bottom -> Pleasant Crossroads Exit Left
    {"from": {"map": "NOK_13", "id": 0}, "to": {"map": "NOK_13", "id": 2}, "reqs": []}, #? Pleasant Crossroads Exit Left -> Pleasant Crossroads Exit Right
    {"from": {"map": "NOK_13", "id": 2}, "to": {"map": "NOK_13", "id": 0}, "reqs": []}, #? Pleasant Crossroads Exit Right -> Pleasant Crossroads Exit Left

    {"from": {"map": "NOK_13", "id": 0}, "to": {"map": "NOK_13", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Pleasant Crossroads Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "NOK_13", "id": 0}, "to": {"map": "NOK_13", "id": "ItemA"},       "reqs": []}, #* Pleasant Crossroads Exit Left -> ItemA (HoneySyrup)
    {"from": {"map": "NOK_13", "id": 1}, "to": {"map": "NOK_13", "id": "RBlockA"},     "reqs": [["can_hit_grounded_blocks"],["can_hit_floating_blocks"]]}, #* Pleasant Crossroads Exit Bottom -> RBlockA (AttackFXB)

    # NOK_14 Path to Fortress 1
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_13", "id": 2}, "reqs": []}, # Path to Fortress 1 Exit Left -> Pleasant Crossroads Exit Right
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_15", "id": 0}, "reqs": []}, # Path to Fortress 1 Exit Right -> Path to Fortress 2 Exit Left

    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": 1}, "reqs": [["MF_NOK14_BuiltBridge"]]}, #? Path to Fortress 1 Exit Left -> Path to Fortress 1 Exit Right
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_14", "id": 0}, "reqs": [["MF_NOK14_BuiltBridge"],["can_climb_steps"]]}, #? Path to Fortress 1 Exit Right -> Path to Fortress 1 Exit Left

    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": 0}, "reqs": [["Kooper"]], "pseudoitems": ["MF_NOK14_BuiltBridge"]}, #+ Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_14", "id": 1}, "reqs": [["can_climb_steps","Hammer","Kooper","Bombette"]], "pseudoitems": ["MF_NOK14_BuiltBridge"]}, #+ Path to Fortress 1 Exit Left

    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": "HiddenPanel"},   "reqs": [["can_flip_panels"]]}, #* Path to Fortress 1 Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": "ItemA"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemA (Coin)
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": "ItemB"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemB (Coin)
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": "ItemC"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemC (Coin)
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": "ItemD"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemD (Coin)
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": "ItemE"},         "reqs": []}, #* Path to Fortress 1 Exit Left -> ItemE (Coin)
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": "ItemF"},         "reqs": [["Kooper","UltraBoots"]]}, #* Path to Fortress 1 Exit Left -> ItemF (ThunderBolt)
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_14", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["can_hit_floating_blocks"]]}, #* Path to Fortress 1 Exit Right -> HiddenYBlockA (FireFlower)

    # NOK_15 Path to Fortress 2
    {"from": {"map": "NOK_15", "id": 0}, "to": {"map": "NOK_14", "id": 1}, "reqs": []}, # Path to Fortress 2 Exit Left -> Path to Fortress 1 Exit Right
    {"from": {"map": "NOK_15", "id": 1}, "to": {"map": "TRD_00", "id": 0}, "reqs": []}, # Path to Fortress 2 Exit Bottom Right -> Fortress Exterior Exit Bottom Left
    {"from": {"map": "NOK_15", "id": 2}, "to": {"map": "TRD_00", "id": 4}, "reqs": []}, # Path to Fortress 2 Exit Top Right -> Fortress Exterior Exit Top Left
    {"from": {"map": "NOK_15", "id": 3}, "to": {"map": "NOK_15", "id": 4}, "reqs": []}, # Path to Fortress 2 Bottom Pipe -> Path to Fortress 2 Top Pipe
    {"from": {"map": "NOK_15", "id": 4}, "to": {"map": "NOK_15", "id": 3}, "reqs": []}, # Path to Fortress 2 Top Pipe -> Path to Fortress 2 Bottom Pipe

    {"from": {"map": "NOK_15", "id": 0}, "to": {"map": "NOK_15", "id": 1}, "reqs": []}, #? Path to Fortress 2 Exit Left -> Path to Fortress 2 Exit Bottom Right
    {"from": {"map": "NOK_15", "id": 1}, "to": {"map": "NOK_15", "id": 0}, "reqs": []}, #? Path to Fortress 2 Exit Bottom Right -> Path to Fortress 2 Exit Left
    {"from": {"map": "NOK_15", "id": 1}, "to": {"map": "NOK_15", "id": 3}, "reqs": [["Bombette"],["can_climb_steps"]]}, #? Path to Fortress 2 Exit Bottom Right -> Path to Fortress 2 Bottom Pipe
    {"from": {"map": "NOK_15", "id": 3}, "to": {"map": "NOK_15", "id": 1}, "reqs": [["Bombette"]]}, #? Path to Fortress 2 Bottom Pipe -> Path to Fortress 2 Exit Bottom Right
    {"from": {"map": "NOK_15", "id": 4}, "to": {"map": "NOK_15", "id": 2}, "reqs": []}, #? Path to Fortress 2 Top Pipe -> Path to Fortress 2 Exit Top Right
    {"from": {"map": "NOK_15", "id": 2}, "to": {"map": "NOK_15", "id": 4}, "reqs": []}, #? Path to Fortress 2 Exit Top Right -> Path to Fortress 2 Top Pipe
    {"from": {"map": "NOK_15", "id": 4}, "to": {"map": "NOK_15", "id": 1}, "reqs": []}, #? Path to Fortress 2 Top Pipe -> Path to Fortress 2 Exit Bottom Right

    {"from": {"map": "NOK_15", "id": 0}, "to": {"map": "NOK_15", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"]]}, #* Path to Fortress 2 Exit Left -> Tree1_Drop1A (StarPiece)
]
