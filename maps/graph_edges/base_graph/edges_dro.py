"""This file represents all edges of the world graph that have origin-nodes in the DRO (Dry Dry Outpost) area."""
edges_dro = [
    # DRO_01 Outpost 1
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "SBK_36", "id": 1}, "reqs": []}, # Outpost 1 Exit West -> E3 Outside Outpost Exit East
    {"from": {"map": "DRO_01", "id": 1}, "to": {"map": "DRO_02", "id": 0}, "reqs": []}, # Outpost 1 Exit East -> Outpost 2 Exit West
    {"from": {"map": "DRO_01", "id": 2}, "to": {"map": "TIK_01", "id": 4}, "reqs": []}, # Outpost 1 Blue Warp Pipe -> Warp Zone 1 (B1) Blue Warp Pipe (Left)

    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": 1}, "reqs": []}, #? Outpost 1 Exit West -> Outpost 1 Exit East
    {"from": {"map": "DRO_01", "id": 1}, "to": {"map": "DRO_01", "id": 0}, "reqs": []}, #? Outpost 1 Exit East -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": 2}, "reqs": [["GF_TIK01_WarpPipes"],["Boots"]]}, #? Outpost 1 Exit West -> Outpost 1 Blue Warp Pipe
    {"from": {"map": "DRO_01", "id": 2}, "to": {"map": "DRO_01", "id": 0}, "reqs": []}, #? Outpost 1 Blue Warp Pipe -> Outpost 1 Exit West

    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "Tree1_Drop1"},"reqs": [["can_shake_trees"]]}, #* Outpost 1 Exit West -> Tree1_Drop1 (Coin)
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "GiftA"},      "reqs": [["Lyrics"]]}, #* Outpost 1 Exit West -> GiftA (Melody)
    {"from": {"map": "DRO_01", "id": "ShopItemA"}, "to": {"map": "DRO_01", "id": "GiftB"},      "reqs": [["FAVOR_7_02_done"]]}, #+ CHAINED REQUIREMENTS -> GiftB (KootRedJar)
    {"from": {"map": "DRO_01", "id": "ShopItemA"}, "to": {"map": "DRO_01", "id": "GiftC"},      "reqs": [["Parakarry"],["Letter19"]]}, #+ CHAINED REQUIREMENTS -> GiftC (Letter12)
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemA"},  "reqs": [["RF_MouserReturned"]]}, #* Outpost 1 Exit West -> ShopItemA (ThunderBolt)
    # {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": "ShopItemB"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemB (DustyHammer)
    {"from": {"map": "DRO_01", "id": "ShopItemA"}, "to": {"map": "DRO_01", "id": "ShopItemC"},  "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemC (HoneySyrup)
    # {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": "ShopItemD"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemD (DriedShroom)
    # {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": "ShopItemE"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemE (DriedPasta)
    {"from": {"map": "DRO_01", "id": "ShopItemA"}, "to": {"map": "DRO_01", "id": "ShopItemF"},  "reqs": []}, #+ SHARED REQUIREMENTS -> ShopItemF (Mushroom)

    {"from": {"map": "DRO_01", "id": "ShopItemA"}, "to": {"map": "DRO_01", "id": "ShopItemA"}, "reqs": [], "pseudoitems": ["DriedPasta"]}, #+ SHARED REQUIREMENTS -> ShopItemE
    {"from": {"map": "DRO_01", "id": "ShopItemA"}, "to": {"map": "DRO_01", "id": "ShopItemA"}, "reqs": [["RF_CanUseDROCode"]], "pseudoitems": ["RF_CanMeetMoustafa"]}, #+ CHAINED REQUIREMENTS -> ShopItemE
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": 0},           "reqs": [], "pseudoitems": ["RF_MouserLeftShop"]}, #+ See Mouser leave
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": 0},           "reqs": [], "pseudoitems": ["StarPiece_DRO_1",
                                                                                                                       #    "StarPiece_DRO_2",
                                                                                                                       #    "StarPiece_DRO_3",
                                                                                                                       #    "StarPiece_DRO_4",
                                                                                                                       #    "StarPiece_DRO_5",
                                                                                                                       #    "StarPiece_DRO_6",
                                                                                                                       #    "StarPiece_DRO_7",
                                                                                                                           "StarPiece_DRO_8"]}, #+ Quizmo StarPieces

    # DRO_02 Outpost 2
    {"from": {"map": "DRO_02", "id": 0}, "to": {"map": "DRO_01", "id": 1}, "reqs": []}, # Outpost 2 Exit West -> Outpost 1 Exit East

    {"from": {"map": "DRO_02", "id": 0},       "to": {"map": "DRO_02", "id": "GiftA"},       "reqs": [["GF_HOS06_MerluvleeRequestedCrystalBall"],["Boots"]]}, #* Outpost 2 Exit West -> GiftA (CrystalBall)
    {"from": {"map": "DRO_02", "id": 0},       "to": {"map": "DRO_02", "id": "GiftB"},       "reqs": [["RF_CanMeetMoustafa"],["Boots"]]}, #* Outpost 2 Exit West -> GiftB (PulseStone)
    {"from": {"map": "DRO_02", "id": 0},       "to": {"map": "DRO_02", "id": "GiftC"},       "reqs": [["Parakarry"],["Letter17"]]}, #* Outpost 2 Exit West -> GiftC (Letter18)
    {"from": {"map": "DRO_02", "id": "GiftB"}, "to": {"map": "DRO_02", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #+ CHAINED REQUIREMENTS -> HiddenPanel (StarPiece)
    {"from": {"map": "DRO_02", "id": "GiftB"}, "to": {"map": "DRO_02", "id": "ItemA"},       "reqs": []}, #+ SHARED REQUIREMENTS -> ItemA (Letter08)

    {"from": {"map": "DRO_02", "id": 0}, "to": {"map": "DRO_02", "id": 0}, "reqs": [["RF_MouserLeftShop"]], "pseudoitems": ["RF_MouserReturned"]}, #+ Chapter Progress
    {"from": {"map": "DRO_02", "id": 0}, "to": {"map": "DRO_02", "id": 0}, "reqs": [["Lemon"]], "pseudoitems": ["RF_CanUseDROCode"]}, #+ Chapter Progress
    {"from": {"map": "DRO_02", "id": 0}, "to": {"map": "DRO_02", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_DRO_1",
                                                                                                    #   "StarPiece_DRO_2",
                                                                                                    #   "StarPiece_DRO_3",
                                                                                                    #   "StarPiece_DRO_4",
                                                                                                    #   "StarPiece_DRO_5",
                                                                                                    #   "StarPiece_DRO_6",
                                                                                                    #   "StarPiece_DRO_7",
                                                                                                       "StarPiece_DRO_8"]}, #+ Quizmo StarPieces
]
