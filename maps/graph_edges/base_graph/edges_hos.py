"""This file represents all edges of the world graph that have origin-nodes in the HOS (Shooting Star Summit) area."""
edges_hos = [
    # HOS_00 Shooting Star Path
    {"from": {"map": "HOS_00", "id": 0}, "to": {"map": "OSR_01", "id": 1}, "reqs": []}, # Shooting Star Path Exit Left -> Ruined Castle Grounds Exit East
    {"from": {"map": "HOS_00", "id": 1}, "to": {"map": "HOS_01", "id": 0}, "reqs": []}, # Shooting Star Path Exit Top Right -> Shooting Star Summit Exit Bottom Left
    {"from": {"map": "HOS_00", "id": 2}, "to": {"map": "HOS_06", "id": 0}, "reqs": []}, # Shooting Star Path Exit Bottom Right -> Merluvlee's House Exit Left

    {"from": {"map": "HOS_00", "id": 0}, "to": {"map": "HOS_00", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Shooting Star Path Exit Left -> Shooting Star Path Exit Top Right
    {"from": {"map": "HOS_00", "id": 1}, "to": {"map": "HOS_00", "id": 0}, "reqs": []}, #? Shooting Star Path Exit Top Right -> Shooting Star Path Exit Left
    {"from": {"map": "HOS_00", "id": 0}, "to": {"map": "HOS_00", "id": 2}, "reqs": []}, #? Shooting Star Path Exit Left -> Shooting Star Path Exit Bottom Right
    {"from": {"map": "HOS_00", "id": 2}, "to": {"map": "HOS_00", "id": 0}, "reqs": []}, #? Shooting Star Path Exit Bottom Right -> Shooting Star Path Exit Left

    {"from": {"map": "HOS_00", "id": 0},             "to": {"map": "HOS_00", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Shooting Star Path Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "HOS_00", "id": "HiddenPanel"}, "to": {"map": "HOS_00", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Shooting Star Path Exit Left

    # HOS_01 Shooting Star Summit
    {"from": {"map": "HOS_01", "id": 0}, "to": {"map": "HOS_00", "id": 1}, "reqs": []}, # Shooting Star Summit Exit Bottom Left -> Shooting Star Path Exit Top Right
    {"from": {"map": "HOS_01", "id": 1}, "to": {"map": "HOS_02", "id": 0}, "reqs": []}, # Shooting Star Summit Ride Up To Starway -> Star Way Ride Down To Summit

    {"from": {"map": "HOS_01", "id": 0}, "to": {"map": "HOS_01", "id": 1}, "reqs": [[{"starspirits": 7}],["can_climb_steps"]]}, #? Shooting Star Summit Exit Bottom Left -> Shooting Star Summit Ride Up To Starway
    {"from": {"map": "HOS_01", "id": 1}, "to": {"map": "HOS_01", "id": 0}, "reqs": []}, #? Shooting Star Summit Ride Up To Starway -> Shooting Star Summit Exit Bottom Left

    {"from": {"map": "HOS_01", "id": 0},             "to": {"map": "HOS_01", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"],["can_climb_steps"]]}, #* Shooting Star Summit Exit Bottom Left -> HiddenPanel (StarPiece)
    {"from": {"map": "HOS_01", "id": "HiddenPanel"}, "to": {"map": "HOS_01", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Shooting Star Summit Exit Bottom Left
    {"from": {"map": "HOS_01", "id": 0},             "to": {"map": "HOS_01", "id": "ItemA"},       "reqs": []}, #* Shooting Star Summit Exit Bottom Left -> ItemA (StarPiece)
    {"from": {"map": "HOS_01", "id": "ItemA"},       "to": {"map": "HOS_01", "id": 0},             "reqs": []}, #* ItemA (StarPiece) -> Shooting Star Summit Exit Bottom Left

    # HOS_02 Star Way
    {"from": {"map": "HOS_02", "id": 0}, "to": {"map": "HOS_01", "id": 1}, "reqs": []}, # Star Way Ride Down To Summit -> Shooting Star Summit Ride Up To Starway
    {"from": {"map": "HOS_02", "id": 1}, "to": {"map": "HOS_03", "id": 0}, "reqs": []}, # Star Way Exit Top Right -> Star Haven Exit Bottom Left

    {"from": {"map": "HOS_02", "id": 0}, "to": {"map": "HOS_02", "id": 1}, "reqs": []}, #? Star Way Ride Down To Summit -> Star Way Exit Top Right
    {"from": {"map": "HOS_02", "id": 1}, "to": {"map": "HOS_02", "id": 0}, "reqs": []}, #? Star Way Exit Top Right -> Star Way Ride Down To Summit

    # HOS_03 Star Haven
    {"from": {"map": "HOS_03", "id": 0}, "to": {"map": "HOS_02", "id": 1}, "reqs": []}, # Star Haven Exit Bottom Left -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 1}, "to": {"map": "HOS_04", "id": 0}, "reqs": []}, # Star Haven Exit Top Right -> Outside the Sanctuary Exit Left

    {"from": {"map": "HOS_03", "id": 0}, "to": {"map": "HOS_03", "id": 1}, "reqs": []}, #? Star Haven Exit Bottom Left -> Star Haven Exit Top Right
    {"from": {"map": "HOS_03", "id": 1}, "to": {"map": "HOS_03", "id": 0}, "reqs": []}, #? Star Haven Exit Top Right -> Star Haven Exit Bottom Left

    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemA"}, "reqs": [["Boots"]]}, #* Star Haven Exit Bottom Left -> ShopItemA (StopWatch)
    {"from": {"map": "HOS_03", "id": "ShopItemA"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemA (StopWatch) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemB"}, "reqs": [["Boots"]]}, #* Star Haven Exit Bottom Left -> ShopItemB (ShootingStar)
    {"from": {"map": "HOS_03", "id": "ShopItemB"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemB (ShootingStar) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemC"}, "reqs": [["Boots"]]}, #* Star Haven Exit Bottom Left -> ShopItemC (SuperSoda)
    {"from": {"map": "HOS_03", "id": "ShopItemC"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemC (SuperSoda) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemD"}, "reqs": [["Boots"]]}, #* Star Haven Exit Bottom Left -> ShopItemD (MapleSyrup)
    {"from": {"map": "HOS_03", "id": "ShopItemD"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemD (MapleSyrup) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemE"}, "reqs": [["Boots"]]}, #* Star Haven Exit Bottom Left -> ShopItemE (LifeShroom)
    {"from": {"map": "HOS_03", "id": "ShopItemE"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemE (LifeShroom) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemF"}, "reqs": [["Boots"]]}, #* Star Haven Exit Bottom Left -> ShopItemF (SuperShroom)
    {"from": {"map": "HOS_03", "id": "ShopItemF"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemF (SuperShroom) -> Star Haven Exit Bottom Left

    {"from": {"map": "HOS_03", "id": 0}, "to": {"map": "HOS_03", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_HOS_1",
                                                                                                     #  "StarPiece_HOS_2",
                                                                                                     #  "StarPiece_HOS_3",
                                                                                                     #  "StarPiece_HOS_4",
                                                                                                     #  "StarPiece_HOS_5",
                                                                                                     #  "StarPiece_HOS_6",
                                                                                                     #  "StarPiece_HOS_7",
                                                                                                       "StarPiece_HOS_8"]}, #+ Quizmo StarPieces

    # HOS_04 Outside the Sanctuary
    {"from": {"map": "HOS_04", "id": 0}, "to": {"map": "HOS_03", "id": 1}, "reqs": []}, # Outside the Sanctuary Exit Left -> Star Haven Exit Top Right
    {"from": {"map": "HOS_04", "id": 1}, "to": {"map": "HOS_05", "id": 0}, "reqs": []}, # Outside the Sanctuary Exit Right -> Star Sanctuary Exit Left

    {"from": {"map": "HOS_04", "id": 0}, "to": {"map": "HOS_04", "id": 1}, "reqs": []}, #? Outside the Sanctuary Exit Left -> Outside the Sanctuary Exit Right
    {"from": {"map": "HOS_04", "id": 1}, "to": {"map": "HOS_04", "id": 0}, "reqs": []}, #? Outside the Sanctuary Exit Right -> Outside the Sanctuary Exit Left

    # HOS_05 Star Sanctuary
    {"from": {"map": "HOS_05", "id": 0}, "to": {"map": "HOS_04", "id": 1}, "reqs": []}, # Star Sanctuary Exit Left -> Outside the Sanctuary Exit Right
    {"from": {"map": "HOS_05", "id": 1}, "to": {"map": "HOS_20", "id": 0}, "reqs": []}, # Star Sanctuary Fly Starship -> Riding Star Ship Scene Fly To Star Haven

    {"from": {"map": "HOS_05", "id": 0}, "to": {"map": "HOS_05", "id": 1}, "reqs": [["can_climb_steps"]], "pseudoitems": ["RF_HasStarbeam"]}, #? Star Sanctuary Exit Left -> Star Sanctuary Fly Starship
    {"from": {"map": "HOS_05", "id": 1}, "to": {"map": "HOS_05", "id": 0}, "reqs": []}, #? Star Sanctuary Fly Starship -> Star Sanctuary Exit Left

    # HOS_06 Merluvlee's House
    {"from": {"map": "HOS_06", "id": 0}, "to": {"map": "HOS_00", "id": 2}, "reqs": []}, # Merluvlee's House Exit Left -> Shooting Star Path Exit Bottom Right

    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Merluvlee's House Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "HOS_06", "id": "HiddenPanel"}, "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "GiftA"},       "reqs": [["FAVOR_3_03_active"], ["CrystalBall"]]}, #* Merluvlee's House Exit Left -> GiftA (KootMerluvleeAutograph)
    {"from": {"map": "HOS_06", "id": "GiftA"},       "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* GiftA (KootMerluvleeAutograph) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "GiftB"},       "reqs": [["Parakarry"],["Letter06"]]}, #* Merluvlee's House Exit Left -> GiftB (StarPiece)
    {"from": {"map": "HOS_06", "id": "GiftB"},       "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* GiftB (StarPiece) -> Merluvlee's House Exit Left

    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeA"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeA (AttackFXA)
    {"from": {"map": "HOS_06", "id": "ShopBadgeA"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeA (AttackFXA) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeB"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeB (PayOff)
    {"from": {"map": "HOS_06", "id": "ShopBadgeB"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeB (PayOff) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeC"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeC (ChillOut)
    {"from": {"map": "HOS_06", "id": "ShopBadgeC"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeC (ChillOut) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeD"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeD (PrettyLucky)
    {"from": {"map": "HOS_06", "id": "ShopBadgeD"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeD (PrettyLucky) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeE"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeE (FeelingFine)
    {"from": {"map": "HOS_06", "id": "ShopBadgeE"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeE (FeelingFine) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeF"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeF (HappyHeartA)
    {"from": {"map": "HOS_06", "id": "ShopBadgeF"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeF (HappyHeartA) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeG"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeG (HappyFlowerA)
    {"from": {"map": "HOS_06", "id": "ShopBadgeG"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeG (HappyFlowerA) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeH"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeH (Peekaboo)
    {"from": {"map": "HOS_06", "id": "ShopBadgeH"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeH (Peekaboo) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeI"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeI (ZapTap)
    {"from": {"map": "HOS_06", "id": "ShopBadgeI"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeI (ZapTap) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeJ"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeJ (HeartFinder)
    {"from": {"map": "HOS_06", "id": "ShopBadgeJ"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeJ (HeartFinder) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeK"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeK (FlowerFinder)
    {"from": {"map": "HOS_06", "id": "ShopBadgeK"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeK (FlowerFinder) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeL"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeL (HPDrain)
    {"from": {"map": "HOS_06", "id": "ShopBadgeL"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeL (HPDrain) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeM"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeM (MoneyMoney)
    {"from": {"map": "HOS_06", "id": "ShopBadgeM"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeM (MoneyMoney) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeN"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeN (FlowerSaverA)
    {"from": {"map": "HOS_06", "id": "ShopBadgeN"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeN (FlowerSaverA) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopBadgeO"},  "reqs": [["RF_OutOfLogic"],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopBadgeO (PowerPlusA)
    {"from": {"map": "HOS_06", "id": "ShopBadgeO"},  "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopBadgeO (PowerPlusA) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopRewardA"}, "reqs": [[{"starpieces": 10}],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopRewardA (Mushroom)
    {"from": {"map": "HOS_06", "id": "ShopRewardA"}, "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopRewardA (Mushroom) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopRewardB"}, "reqs": [[{"starpieces": 23}],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopRewardB (SuperShroom)
    {"from": {"map": "HOS_06", "id": "ShopRewardB"}, "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopRewardB (SuperShroom) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopRewardC"}, "reqs": [[{"starpieces": 35}],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopRewardC (ThunderRage)
    {"from": {"map": "HOS_06", "id": "ShopRewardC"}, "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopRewardC (ThunderRage) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopRewardD"}, "reqs": [[{"starpieces": 47}],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopRewardD (LifeShroom)
    {"from": {"map": "HOS_06", "id": "ShopRewardD"}, "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopRewardD (LifeShroom) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopRewardE"}, "reqs": [[{"starpieces": 57}],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopRewardE (UltraShroom)
    {"from": {"map": "HOS_06", "id": "ShopRewardE"}, "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopRewardE (UltraShroom) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "ShopRewardF"}, "reqs": [[{"starpieces": 68}],["can_climb_steps"]]}, #* Merluvlee's House Exit Left -> ShopRewardF (RepelGel)
    {"from": {"map": "HOS_06", "id": "ShopRewardF"}, "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* ShopRewardF (RepelGel) -> Merluvlee's House Exit Left

    {"from": {"map": "HOS_06", "id": 0}, "to": {"map": "HOS_06", "id": 0}, "reqs": [["FAVOR_3_03_active"]], "pseudoitems": ["GF_HOS06_MerluvleeRequestedCrystalBall"]}, #+ Merluvlee's House Exit Left

    # HOS_20 Riding Star Ship Scene
    {"from": {"map": "HOS_20", "id": 0}, "to": {"map": "HOS_05", "id": 1}, "reqs": []}, # Riding Star Ship Scene Fly To Star Haven -> Star Sanctuary Fly Starship
    {"from": {"map": "HOS_20", "id": 2}, "to": {"map": "KPA_60", "id": 4}, "reqs": []}, # Riding Star Ship Scene Fly To Bowser's Castle -> Ship Enter/Exit Scenes Leave Hangar To Starhaven

    {"from": {"map": "HOS_20", "id": 0}, "to": {"map": "HOS_20", "id": 2}, "reqs": []}, #? Riding Star Ship Scene Fly To Star Haven -> Riding Star Ship Scene Fly To Bowser's Castle
    {"from": {"map": "HOS_20", "id": 2}, "to": {"map": "HOS_20", "id": 0}, "reqs": []}, #? Riding Star Ship Scene Fly To Bowser's Castle -> Riding Star Ship Scene Fly To Star Haven
]
