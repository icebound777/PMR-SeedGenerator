from rando_modules.simulate import *

"""This file represents all edges of the world graph that have origin-nodes in the MAC (Toad Town) area."""
edges_mac = [
    # MAC_00 Gate District
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "KMR_10", "id": 1}, "reqs": []}, # Gate District Exit Left -> Toad Town Entrance Exit Right
    {"from": {"map": "MAC_00", "id": 1}, "to": {"map": "MAC_01", "id": 0}, "reqs": []}, # Gate District Exit Right -> Plaza District Exit Left
    {"from": {"map": "MAC_00", "id": 3}, "to": {"map": "TIK_19", "id": 0}, "reqs": []}, # Gate District Island Pipe -> Under the Toad Town Pond Pipe Left
    {"from": {"map": "MAC_00", "id": 4}, "to": {"map": "KMR_20", "id": 4}, "reqs": []}, # Gate District Top Green Pipe -> Mario's House Green Pipe
    
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "MAC_00", "id": 1}, "reqs": []}, #? Gate District Exit Left -> Gate District Exit Right
    {"from": {"map": "MAC_00", "id": 1}, "to": {"map": "MAC_00", "id": 0}, "reqs": []}, #? Gate District Exit Right -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "MAC_00", "id": 3}, "reqs": [require(partner="Sushie")]}, #? Gate District Exit Left -> Gate District Island Pipe
    {"from": {"map": "MAC_00", "id": 3}, "to": {"map": "MAC_00", "id": 0}, "reqs": [require(partner="Sushie")]}, #? Gate District Island Pipe -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "MAC_00", "id": 4}, "reqs": []}, #? Gate District Exit Left -> Gate District Top Green Pipe
    {"from": {"map": "MAC_00", "id": 4}, "to": {"map": "MAC_00", "id": 0}, "reqs": []}, #? Gate District Top Green Pipe -> Gate District Exit Left
    
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "HiddenPanel"}, "reqs": [can_flip_panels]}, #* Gate District Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "MAC_00", "id": "HiddenPanel"}, "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "ItemA"},       "reqs": [require(partner="Sushie")]}, #* Gate District Exit Left -> ItemA (StarPiece)
    {"from": {"map": "MAC_00", "id": "ItemA"},       "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* ItemA (StarPiece) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "GiftA"},       "reqs": [require(item="Dictionary")]}, #* Gate District Exit Left -> GiftA (StarPiece)
    {"from": {"map": "MAC_00", "id": "GiftA"},       "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* GiftA (StarPiece) -> Gate District Exit Left
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
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "DojoA"},       "reqs": []}, #* Gate District Exit Left -> Dojo Fight A (First Degree Card)
    {"from": {"map": "MAC_00", "id": "DojoA"},       "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* Dojo Fight A (First Degree Card) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "DojoB"},       "reqs": [require(starspirits=2)]}, #* Gate District Exit Left -> Dojo Fight B (Second Degree Card)
    {"from": {"map": "MAC_00", "id": "DojoB"},       "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* Dojo Fight B (Second Degree Card) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "DojoC"},       "reqs": [require(starspirits=3)]}, #* Gate District Exit Left -> Dojo Fight C (Third Degree Card)
    {"from": {"map": "MAC_00", "id": "DojoC"},       "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* Dojo Fight C (Third Degree Card) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "DojoD"},       "reqs": [require(starspirits=4)]}, #* Gate District Exit Left -> Dojo Fight D (Fourth Degree Card)
    {"from": {"map": "MAC_00", "id": "DojoD"},       "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* Dojo Fight D (Fourth Degree Card) -> Gate District Exit Left
    {"from": {"map": "MAC_00", "id": 0},             "to": {"map": "MAC_00", "id": "DojoE"},       "reqs": [require(starspirits=5)]}, #* Gate District Exit Left -> Dojo Fight E (Diploma)
    {"from": {"map": "MAC_00", "id": "DojoE"},       "to": {"map": "MAC_00", "id": 0},             "reqs": []}, #* Dojo Fight E (Diploma) -> Gate District Exit Left

    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "MAC_00", "id": 0}, "reqs": [], "pseudoitems": ["RF_CanVisitRussT"]}, #+ Can decipher MysteryNote

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
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 5}, "reqs": [require(flag="RF_Ch6_FlowerGateOpen")]}, #? Plaza District Exit Left -> Plaza District Flower Door
    {"from": {"map": "MAC_01", "id": 5}, "to": {"map": "MAC_01", "id": 0}, "reqs": []}, #? Plaza District Flower Door -> Plaza District Exit Left

    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 0}, "reqs": [require(item="MagicalSeed1"),
                                                                                    require(item="MagicalSeed2"),
                                                                                    require(item="MagicalSeed3"),
                                                                                    require(item="MagicalSeed4")],
                                                                           "pseudoitems": ["RF_Ch6_FlowerGateOpen"]}, #+ Plaza District Exit Left
    
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ItemA"},        "reqs": [require(boots=2)]}, #* Plaza District Exit Left -> ItemA (QuickChange)
    {"from": {"map": "MAC_01", "id": "ItemA"},        "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ItemA (QuickChange) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "GiftA"},        "reqs": [require(item="Calculator")]}, #* Plaza District Exit Left -> GiftA (ISpy)
    {"from": {"map": "MAC_01", "id": "GiftA"},        "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* GiftA (ISpy) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "GiftB"},        "reqs": [require(item="Mailbag")]}, #* Plaza District Exit Left -> GiftB (StarPiece)
    {"from": {"map": "MAC_01", "id": "GiftB"},        "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* GiftB (StarPiece) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "Tree1_Drop1A"}, "reqs": [can_shake_trees]}, #* Plaza District Exit Left -> Tree1_Drop1A (StarPiece)
    {"from": {"map": "MAC_01", "id": "Tree1_Drop1A"}, "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* Tree1_Drop1A (StarPiece) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeA"},   "reqs": []}, #* Plaza District Exit Left -> ShopBadgeA (SpeedySpin)
    {"from": {"map": "MAC_01", "id": "ShopBadgeA"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeA (SpeedySpin) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeB"},   "reqs": []}, #* Plaza District Exit Left -> ShopBadgeB (FirstAttack)
    {"from": {"map": "MAC_01", "id": "ShopBadgeB"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeB (FirstAttack) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeC"},   "reqs": []}, #* Plaza District Exit Left -> ShopBadgeC (Multibounce)
    {"from": {"map": "MAC_01", "id": "ShopBadgeC"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeC (Multibounce) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeD"},   "reqs": []}, #* Plaza District Exit Left -> ShopBadgeD (DDownPound)
    {"from": {"map": "MAC_01", "id": "ShopBadgeD"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeD (DDownPound) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeE"},   "reqs": [require(starspirits=1)]}, #* Plaza District Exit Left -> ShopBadgeE (DodgeMaster)
    {"from": {"map": "MAC_01", "id": "ShopBadgeE"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeE (DodgeMaster) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeF"},   "reqs": [require(starspirits=1)]}, #* Plaza District Exit Left -> ShopBadgeF (SleepStomp)
    {"from": {"map": "MAC_01", "id": "ShopBadgeF"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeF (SleepStomp) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeG"},   "reqs": [require(starspirits=1)]}, #* Plaza District Exit Left -> ShopBadgeG (DoubleDip)
    {"from": {"map": "MAC_01", "id": "ShopBadgeG"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeG (DoubleDip) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeH"},   "reqs": [require(starspirits=2)]}, #* Plaza District Exit Left -> ShopBadgeH (JumpCharge)
    {"from": {"map": "MAC_01", "id": "ShopBadgeH"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeH (JumpCharge) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeI"},   "reqs": [require(starspirits=2)]}, #* Plaza District Exit Left -> ShopBadgeI (SpinSmash)
    {"from": {"map": "MAC_01", "id": "ShopBadgeI"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeI (SpinSmash) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeJ"},   "reqs": [require(starspirits=2)]}, #* Plaza District Exit Left -> ShopBadgeJ (GroupFocus)
    {"from": {"map": "MAC_01", "id": "ShopBadgeJ"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeJ (GroupFocus) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeK"},   "reqs": [require(starspirits=3)]}, #* Plaza District Exit Left -> ShopBadgeK (AllorNothing)
    {"from": {"map": "MAC_01", "id": "ShopBadgeK"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeK (AllorNothing) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeL"},   "reqs": [require(starspirits=3)]}, #* Plaza District Exit Left -> ShopBadgeL (HPPlusC)
    {"from": {"map": "MAC_01", "id": "ShopBadgeL"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeL (HPPlusC) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeM"},   "reqs": [require(starspirits=3)]}, #* Plaza District Exit Left -> ShopBadgeM (FPPlusC)
    {"from": {"map": "MAC_01", "id": "ShopBadgeM"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeM (FPPlusC) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeN"},   "reqs": [require(starspirits=4)]}, #* Plaza District Exit Left -> ShopBadgeN (SSmashChg)
    {"from": {"map": "MAC_01", "id": "ShopBadgeN"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeN (SSmashChg) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeO"},   "reqs": [require(starspirits=4)]}, #* Plaza District Exit Left -> ShopBadgeO (DamageDodgeA)
    {"from": {"map": "MAC_01", "id": "ShopBadgeO"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeO (DamageDodgeA) -> Plaza District Exit Left
    {"from": {"map": "MAC_01", "id": 0},              "to": {"map": "MAC_01", "id": "ShopBadgeP"},   "reqs": [require(starspirits=4)]}, #* Plaza District Exit Left -> ShopBadgeP (MegaQuake)
    {"from": {"map": "MAC_01", "id": "ShopBadgeP"},   "to": {"map": "MAC_01", "id": 0},              "reqs": []}, #* ShopBadgeP (MegaQuake) -> Plaza District Exit Left

    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 0}, "reqs": [], "pseudoitems": ["RF_CanReadToadTownNews"]}, #+ For Koopa Koot Favor 4_01

    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_MAC_1",
                                                                                                       "StarPiece_MAC_2",
                                                                                                       "StarPiece_MAC_3",
                                                                                                       "StarPiece_MAC_4"]}, #+ Quizmo StarPieces
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 0}, "reqs": [require(starspirits=2)], "pseudoitems": ["StarPiece_MAC_5",
                                                                                                                             "StarPiece_MAC_6",
                                                                                                                             "StarPiece_MAC_7",
                                                                                                                             "StarPiece_MAC_8"]}, #+ Quizmo StarPieces
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 0}, "reqs": [require(starspirits=4)], "pseudoitems": ["StarPiece_MAC_9",
                                                                                                                             "StarPiece_MAC_10",
                                                                                                                             "StarPiece_MAC_11",
                                                                                                                             "StarPiece_MAC_12"]}, #+ Quizmo StarPieces
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 0}, "reqs": [require(starspirits=6)], "pseudoitems": ["StarPiece_MAC_13",
                                                                                                                             "StarPiece_MAC_14",
                                                                                                                             "StarPiece_MAC_15",
                                                                                                                             "StarPiece_MAC_16"]}, #+ Quizmo StarPieces

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
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 5}, "reqs": [require(item="OddKey",flag="GF_MAC02_UnlockedHouse")], "pseudoitems": ["GF_MAC02_UnlockedHouse"]}, #? Southern District Exit Top -> Southern District Blue House Pipe
    {"from": {"map": "MAC_02", "id": 5}, "to": {"map": "MAC_02", "id": 2}, "reqs": [require(item="OddKey",flag="GF_MAC02_UnlockedHouse")], "pseudoitems": ["GF_MAC02_UnlockedHouse"]}, #? Southern District Blue House Pipe -> Southern District Exit Top
    
    {"from": {"map": "MAC_02", "id": 2},             "to": {"map": "MAC_02", "id": "GiftA"},       "reqs": []}, #* Southern District Exit Top -> GiftA (MagicalSeed1)
    {"from": {"map": "MAC_02", "id": "GiftA"},       "to": {"map": "MAC_02", "id": 2},             "reqs": []}, #* GiftA (MagicalSeed1) -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 2},             "to": {"map": "MAC_02", "id": "GiftB"},       "reqs": [require(item="FryingPan")]}, #* Southern District Exit Top -> GiftB (Cake)
    {"from": {"map": "MAC_02", "id": "GiftB"},       "to": {"map": "MAC_02", "id": 2},             "reqs": []}, #* GiftB (Cake) -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 2},             "to": {"map": "MAC_02", "id": "HiddenPanel"}, "reqs": [can_flip_panels]}, #* Southern District Exit Top -> HiddenPanel (StarPiece)
    {"from": {"map": "MAC_02", "id": "HiddenPanel"}, "to": {"map": "MAC_02", "id": 2},             "reqs": []}, #* HiddenPanel (StarPiece) -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 5},             "to": {"map": "MAC_02", "id": "ItemA"},       "reqs": []}, #* Southern District Blue House Pipe -> ItemA (OddKey)
    {"from": {"map": "MAC_02", "id": "ItemA"},       "to": {"map": "MAC_02", "id": 5},             "reqs": []}, #* ItemA (OddKey) -> Southern District Blue House Pipe

    {"from": {"map": "MAC_02", "id": 0}, "to": {"map": "MAC_02", "id": 0}, "reqs": [], "pseudoitems": ["RF_CanVisitTayceT"]}, #+ Can visit Tayce T. for cooking

    # MAC_03 Station District
    {"from": {"map": "MAC_03", "id": 0}, "to": {"map": "MAC_02", "id": 3}, "reqs": []}, # Station District Exit Top -> Southern District Exit Bottom
    {"from": {"map": "MAC_03", "id": 1}, "to": {"map": "IWA_11", "id": 1}, "reqs": []}, # Station District Train -> Train Ride Scene Exit Left
    {"from": {"map": "MAC_03", "id": 2}, "to": {"map": "MGM_00", "id": 0}, "reqs": []}, # Station District Minigame Pipe -> Playroom Lobby Exit Pipe
    
    {"from": {"map": "MAC_03", "id": 0}, "to": {"map": "MAC_03", "id": 1}, "reqs": [require(flag="GF_MAC03_BombedRock")]}, #? Station District Exit Top -> Station District Train
    {"from": {"map": "MAC_03", "id": 1}, "to": {"map": "MAC_03", "id": 0}, "reqs": [], "pseudoitems": ["GF_MAC03_BombedRock"]}, #? Station District Train -> Station District Exit Top
    {"from": {"map": "MAC_03", "id": 0}, "to": {"map": "MAC_03", "id": 2}, "reqs": [can_shake_trees]}, #? Station District Exit Top -> Station District Minigame Pipe
    {"from": {"map": "MAC_03", "id": 2}, "to": {"map": "MAC_03", "id": 0}, "reqs": []}, #? Station District Minigame Pipe -> Station District Exit Top
    
    {"from": {"map": "MAC_03", "id": 0},             "to": {"map": "MAC_03", "id": "GiftA"},       "reqs": [require(item="Letter20")]}, #* Station District Exit Top -> GiftA (Letter21)
    {"from": {"map": "MAC_03", "id": "GiftA"},       "to": {"map": "MAC_03", "id": 0},             "reqs": []}, #* GiftA (Letter21) -> Station District Exit Top
    {"from": {"map": "MAC_03", "id": 0},             "to": {"map": "MAC_03", "id": "GiftB"},       "reqs": [require(item="Letter22")]}, #* Station District Exit Top -> GiftB (Letter23)
    {"from": {"map": "MAC_03", "id": "GiftB"},       "to": {"map": "MAC_03", "id": 0},             "reqs": []}, #* GiftB (Letter23) -> Station District Exit Top
    {"from": {"map": "MAC_03", "id": 0},             "to": {"map": "MAC_03", "id": "HiddenPanel"}, "reqs": [can_flip_panels]}, #* Station District Exit Top -> HiddenPanel (StarPiece)
    {"from": {"map": "MAC_03", "id": "HiddenPanel"}, "to": {"map": "MAC_03", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Station District Exit Top

    {"from": {"map": "MAC_03", "id": 0}, "to": {"map": "MAC_03", "id": 0}, "reqs": [require(partner="Bombette")], "pseudoitems": ["GF_MAC03_BombedRock"]}, #+ Station District Explode the rock

    # MAC_04 Residental District
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_02", "id": 0}, "reqs": []}, # Residental District Exit Right -> Southern District Exit Left
    {"from": {"map": "MAC_04", "id": 1}, "to": {"map": "MAC_05", "id": 0}, "reqs": []}, # Residental District Exit Left -> Port District Exit Right
    {"from": {"map": "MAC_04", "id": 2}, "to": {"map": "OMO_03", "id": 4}, "reqs": []}, # Residental District Toybox Spring -> BLU Station Spring Exit
    
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 1}, "reqs": []}, #? Residental District Exit Right -> Residental District Exit Left
    {"from": {"map": "MAC_04", "id": 1}, "to": {"map": "MAC_04", "id": 0}, "reqs": []}, #? Residental District Exit Left -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 2}, "reqs": [require(partner="Bow",flag="RF_ToyboxOpen")]}, #? Residental District Exit Right -> Residental District Toybox Spring    
    {"from": {"map": "MAC_04", "id": 2}, "to": {"map": "MAC_04", "id": 0}, "reqs": []}, #? Residental District Toybox Spring -> Residental District Exit Right

    {"from": {"map": "MAC_04", "id": 2}, "to": {"map": "MAC_04", "id": 2}, "reqs": [], "pseudoitems": ["MF_Ch4_CanThrowInTrain"]}, #+ Toybox: Can throw in ToyTrain
    
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ItemA"},     "reqs": [require(item="StoreroomKey")]}, #* Residental District Exit Right -> ItemA (SnowmanDoll)
    {"from": {"map": "MAC_04", "id": "ItemA"},     "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ItemA (SnowmanDoll) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ItemB"},     "reqs": [require(item="StoreroomKey")]}, #* Residental District Exit Right -> ItemB (VoltShroom)
    {"from": {"map": "MAC_04", "id": "ItemB"},     "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ItemB (VoltShroom) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ItemC"},     "reqs": [require(item="StoreroomKey")]}, #* Residental District Exit Right -> ItemC (ToyTrain)
    {"from": {"map": "MAC_04", "id": "ItemC"},     "to": {"map": "MAC_04", "id": 0},           "reqs": []}, #* ItemC (ToyTrain) -> Residental District Exit Right
    {"from": {"map": "MAC_04", "id": 0},           "to": {"map": "MAC_04", "id": "ItemD"},     "reqs": [require(item="StoreroomKey")]}, #* Residental District Exit Right -> ItemD (DizzyDial)
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

    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_MAC_1",
                                                                                                       "StarPiece_MAC_2",
                                                                                                       "StarPiece_MAC_3",
                                                                                                       "StarPiece_MAC_4"]}, #+ Quizmo StarPieces
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 0}, "reqs": [require(starspirits=2)], "pseudoitems": ["StarPiece_MAC_5",
                                                                                                                             "StarPiece_MAC_6",
                                                                                                                             "StarPiece_MAC_7",
                                                                                                                             "StarPiece_MAC_8"]}, #+ Quizmo StarPieces
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 0}, "reqs": [require(starspirits=4)], "pseudoitems": ["StarPiece_MAC_9",
                                                                                                                             "StarPiece_MAC_10",
                                                                                                                             "StarPiece_MAC_11",
                                                                                                                             "StarPiece_MAC_12"]}, #+ Quizmo StarPieces
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 0}, "reqs": [require(starspirits=6)], "pseudoitems": ["StarPiece_MAC_13",
                                                                                                                             "StarPiece_MAC_14",
                                                                                                                             "StarPiece_MAC_15",
                                                                                                                             "StarPiece_MAC_16"]}, #+ Quizmo StarPieces

    # MAC_05 Port District
    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_04", "id": 1}, "reqs": []}, # Port District Exit Right -> Residental District Exit Left
    {"from": {"map": "MAC_05", "id": 1}, "to": {"map": "MAC_06", "id": 0}, "reqs": []}, # Port District Ride Whale -> Ride Whale (Toad Town)
    {"from": {"map": "MAC_05", "id": 3}, "to": {"map": "KGR_01", "id": 0}, "reqs": []}, # Port District Enter Whale -> Whale Mouth Exit Left
    
    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_05", "id": 1}, "reqs": [require(flag="RF_CanRideWhale")]}, #? Port District Exit Right -> Port District Ride Whale
    {"from": {"map": "MAC_05", "id": 1}, "to": {"map": "MAC_05", "id": 0}, "reqs": []}, #? Port District Ride Whale -> Port District Exit Right
    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_05", "id": 3}, "reqs": [require(hammer=1, boots=2, partner="Bombette")]}, #? Port District Exit Right -> Port District Enter Whale
    {"from": {"map": "MAC_05", "id": 3}, "to": {"map": "MAC_05", "id": 0}, "reqs": []}, #? Port District Enter Whale -> Port District Exit Right
    
    {"from": {"map": "MAC_05", "id": 0},             "to": {"map": "MAC_05", "id": "GiftA"},       "reqs": []}, #* Port District Exit Right -> GiftA (Lyrics)
    {"from": {"map": "MAC_05", "id": "GiftA"},       "to": {"map": "MAC_05", "id": 0},             "reqs": []}, #* GiftA (Lyrics) -> Port District Exit Right
    {"from": {"map": "MAC_05", "id": 0},             "to": {"map": "MAC_05", "id": "GiftB"},       "reqs": [require(item="Melody")]}, #* Port District Exit Right -> GiftB (AttackFXD)
    {"from": {"map": "MAC_05", "id": "GiftB"},       "to": {"map": "MAC_05", "id": 0},             "reqs": []}, #* GiftB (AttackFXD) -> Port District Exit Right
    {"from": {"map": "MAC_05", "id": 0},             "to": {"map": "MAC_05", "id": "HiddenPanel"}, "reqs": [can_flip_panels]}, #* Port District Exit Right -> HiddenPanel (StarPiece)
    {"from": {"map": "MAC_05", "id": "HiddenPanel"}, "to": {"map": "MAC_05", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Port District Exit Right

    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_05", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_MAC_1",
                                                                                                       "StarPiece_MAC_2",
                                                                                                       "StarPiece_MAC_3",
                                                                                                       "StarPiece_MAC_4"]}, #+ Quizmo StarPieces
    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_05", "id": 0}, "reqs": [require(starspirits=2)], "pseudoitems": ["StarPiece_MAC_5",
                                                                                                                             "StarPiece_MAC_6",
                                                                                                                             "StarPiece_MAC_7",
                                                                                                                             "StarPiece_MAC_8"]}, #+ Quizmo StarPieces
    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_05", "id": 0}, "reqs": [require(starspirits=4)], "pseudoitems": ["StarPiece_MAC_9",
                                                                                                                             "StarPiece_MAC_10",
                                                                                                                             "StarPiece_MAC_11",
                                                                                                                             "StarPiece_MAC_12"]}, #+ Quizmo StarPieces
    {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_05", "id": 0}, "reqs": [require(starspirits=6)], "pseudoitems": ["StarPiece_MAC_13",
                                                                                                                             "StarPiece_MAC_14",
                                                                                                                             "StarPiece_MAC_15",
                                                                                                                             "StarPiece_MAC_16"]}, #+ Quizmo StarPieces

    # MAC_06 Riding the Whale
    {"from": {"map": "MAC_06", "id": 0}, "to": {"map": "MAC_05", "id": 1}, "reqs": []}, # Ride Whale (Toad Town) -> Port District Ride Whale
    {"from": {"map": "MAC_06", "id": 0}, "to": {"map": "JAN_00", "id": 0}, "reqs": []}, # Ride Whale (Lavalava Island) -> Whale Cove Ride The Whale

    {"from": {"map": "MAC_06", "id": 0}, "to": {"map": "MAC_06", "id": 1}, "reqs": []}, #? Ride Whale (Toad Town) -> Ride Whale (Lavalava Island)
    {"from": {"map": "MAC_06", "id": 1}, "to": {"map": "MAC_06", "id": 0}, "reqs": []}, #? Ride Whale (Lavalava Island) -> Ride Whale (Toad Town)
]
