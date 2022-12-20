"""This file represents all edges of the world graph that have origin-nodes in the IWA (Mt. Rugged) area."""
edges_iwa = [
    # IWA_00 Mt Rugged 1
    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_10", "id": 1}, "reqs": []}, # Mt Rugged 1 Exit Left -> Train Station Exit Top Right
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_01", "id": 0}, "reqs": []}, # Mt Rugged 1 Exit Right -> Mt Rugged 2 Exit Bottom Left

    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_00", "id": 1}, "reqs": [["can_climb_steps", "Lakilester"]]}, #? Mt Rugged 1 Exit Left -> Mt Rugged 1 Exit Right
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_00", "id": 0}, "reqs": []}, #? Mt Rugged 1 Exit Right -> Mt Rugged 1 Exit Left

    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_00", "id": "ItemA"},   "reqs": []}, #* Mt Rugged 1 Exit Left -> ItemA (Coin)
    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_00", "id": "ItemB"},   "reqs": [["Kooper", "Lakilester"]]}, #* Mt Rugged 1 Exit Left -> ItemB (Coin)
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_00", "id": "ItemB"},   "reqs": [["can_climb_steps"]]}, #* Mt Rugged 1 Exit Right -> ItemB (Coin)
    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_00", "id": "ItemC"},   "reqs": [["Kooper", "Lakilester"]]}, #* Mt Rugged 1 Exit Left -> ItemC (Coin)
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_00", "id": "ItemC"},   "reqs": [["can_climb_steps"]]}, #* Mt Rugged 1 Exit Right -> ItemC (Coin)
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_00", "id": "ItemD"},   "reqs": [["RF_Missable"],["Hammer", "Bombette"]]}, #* Mt Rugged 1 Exit Right -> ItemD (WhackasBump)
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_00", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Mt Rugged 1 Exit Right -> YBlockA (SleepySheep)

    # IWA_01 Mt Rugged 2
    {"from": {"map": "IWA_01", "id": 0}, "to": {"map": "IWA_00", "id": 1}, "reqs": []}, # Mt Rugged 2 Exit Bottom Left -> Mt Rugged 1 Exit Right
    {"from": {"map": "IWA_01", "id": 1}, "to": {"map": "IWA_03", "id": 0}, "reqs": []}, # Mt Rugged 2 Exit Top Left -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_01", "id": 2}, "to": {"map": "IWA_02", "id": 0}, "reqs": []}, # Mt Rugged 2 Exit Bottom Right -> Mt Rugged 3 Exit Bottom Left
    {"from": {"map": "IWA_01", "id": 3}, "to": {"map": "IWA_02", "id": 1}, "reqs": []}, # Mt Rugged 2 Exit Top Right -> Mt Rugged 3 Exit Top Left

    {"from": {"map": "IWA_01", "id": 0}, "to": {"map": "IWA_01", "id": 2}, "reqs": [["Boots"]]}, #? Mt Rugged 2 Exit Bottom Left -> Mt Rugged 2 Exit Bottom Right
    {"from": {"map": "IWA_01", "id": 2}, "to": {"map": "IWA_01", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Mt Rugged 2 Exit Bottom Right -> Mt Rugged 2 Exit Bottom Left
    {"from": {"map": "IWA_01", "id": 3}, "to": {"map": "IWA_01", "id": 1}, "reqs": []}, #? Mt Rugged 2 Exit Top Right -> Mt Rugged 2 Exit Top Left
    {"from": {"map": "IWA_01", "id": 1}, "to": {"map": "IWA_01", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Mt Rugged 2 Exit Top Left -> Mt Rugged 2 Exit Bottom Left

    {"from": {"map": "IWA_01", "id": 0},       "to": {"map": "IWA_01", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Mt Rugged 2 Exit Bottom Left -> HiddenPanel (StarPiece)
    {"from": {"map": "IWA_01", "id": 2},       "to": {"map": "IWA_01", "id": "ItemB"},       "reqs": [["Kooper","Parakarry"]]}, #* Mt Rugged 2 Exit Bottom Right -> ItemB (Letter01)
    {"from": {"map": "IWA_01", "id": "ItemB"}, "to": {"map": "IWA_01", "id": "ItemA"},       "reqs": [["Parakarry"]]}, #* ItemB (Letter01) -> ItemA (QuakeHammer)

    # IWA_02 Mt Rugged 3
    {"from": {"map": "IWA_02", "id": 0}, "to": {"map": "IWA_01", "id": 2}, "reqs": []}, # Mt Rugged 3 Exit Bottom Left -> Mt Rugged 2 Exit Bottom Right
    {"from": {"map": "IWA_02", "id": 1}, "to": {"map": "IWA_01", "id": 3}, "reqs": []}, # Mt Rugged 3 Exit Top Left -> Mt Rugged 2 Exit Top Right
    {"from": {"map": "IWA_02", "id": 2}, "to": {"map": "IWA_04", "id": 0}, "reqs": []}, # Mt Rugged 3 Exit Top Right -> Suspension Bridge Exit Left

    {"from": {"map": "IWA_02", "id": 0}, "to": {"map": "IWA_02", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Mt Rugged 3 Exit Bottom Left -> Mt Rugged 3 Exit Top Left
    {"from": {"map": "IWA_02", "id": 1}, "to": {"map": "IWA_02", "id": 0}, "reqs": []}, #? Mt Rugged 3 Exit Top Left -> Mt Rugged 3 Exit Bottom Left
    {"from": {"map": "IWA_02", "id": 1}, "to": {"map": "IWA_02", "id": 2}, "reqs": []}, #? Mt Rugged 3 Exit Top Left -> Mt Rugged 3 Exit Top Right
    {"from": {"map": "IWA_02", "id": 2}, "to": {"map": "IWA_02", "id": 1}, "reqs": []}, #? Mt Rugged 3 Exit Top Right -> Mt Rugged 3 Exit Top Left

    {"from": {"map": "IWA_02", "id": 0}, "to": {"map": "IWA_02", "id": "GiftA"}, "reqs": [["Parakarry"]]}, #* Mt Rugged 3 Exit Bottom Left -> GiftA (MagicalSeed2)
    {"from": {"map": "IWA_02", "id": 1}, "to": {"map": "IWA_02", "id": "ItemA"}, "reqs": []}, #* Mt Rugged 3 Exit Top Left -> ItemA (StarPiece)

    # IWA_03 Mt Rugged 4
    {"from": {"map": "IWA_03", "id": 0}, "to": {"map": "IWA_01", "id": 1}, "reqs": []}, # Mt Rugged 4 Exit Bottom Right -> Mt Rugged 2 Exit Top Left

    {"from": {"map": "IWA_03", "id": 0},        "to": {"map": "IWA_03", "id": "ChestA"},  "reqs": [["can_climb_steps"]]}, #* Mt Rugged 4 Exit Bottom Right -> ChestA (DamageDodgeB)
    {"from": {"map": "IWA_03", "id": "ChestA"}, "to": {"map": "IWA_03", "id": "ItemA"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemA (Letter25)
    {"from": {"map": "IWA_03", "id": 0},        "to": {"map": "IWA_03", "id": "ItemB"},   "reqs": [["Parakarry"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemB (StarPiece)
    {"from": {"map": "IWA_03", "id": "ChestA"}, "to": {"map": "IWA_03", "id": "ItemC"},   "reqs": [["Kooper","Parakarry"]]}, #+ CHAINED REQUIREMENTS -> ItemC (Coin) (circle-right)
    {"from": {"map": "IWA_03", "id": "ItemB"},  "to": {"map": "IWA_03", "id": "ItemD"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemD (Coin)
    {"from": {"map": "IWA_03", "id": "ItemB"},  "to": {"map": "IWA_03", "id": "ItemE"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemE (Coin)
    {"from": {"map": "IWA_03", "id": "ItemB"},  "to": {"map": "IWA_03", "id": "ItemF"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemF (Coin)
    {"from": {"map": "IWA_03", "id": "ItemB"},  "to": {"map": "IWA_03", "id": "ItemG"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemG (Coin)
    {"from": {"map": "IWA_03", "id": "ItemB"},  "to": {"map": "IWA_03", "id": "ItemH"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemH (Coin)
    {"from": {"map": "IWA_03", "id": "ChestA"}, "to": {"map": "IWA_03", "id": "ItemI"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemI (Coin) (bottom1)
    {"from": {"map": "IWA_03", "id": "ChestA"}, "to": {"map": "IWA_03", "id": "ItemJ"},   "reqs": []}, #+ SHARED REQUIREMENTS -> ItemJ (Coin) (bottom2)
    {"from": {"map": "IWA_03", "id": "ChestA"}, "to": {"map": "IWA_03", "id": "YBlockA"}, "reqs": [["can_hit_grounded_blocks"]]}, #+ CHAINED REQUIREMENTS -> YBlockA (Coin)
    {"from": {"map": "IWA_03", "id": 0},        "to": {"map": "IWA_03", "id": "YBlockB"}, "reqs": [["can_hit_floating_blocks"]]}, #* Mt Rugged 4 Exit Bottom Right -> YBlockB (Mushroom)
    {"from": {"map": "IWA_03", "id": "ChestA"}, "to": {"map": "IWA_03", "id": "YBlockC"}, "reqs": [["can_hit_grounded_blocks"]]}, #+ CHAINED REQUIREMENTS -> YBlockC (HoneySyrup)

    # IWA_04 Suspension Bridge
    {"from": {"map": "IWA_04", "id": 0}, "to": {"map": "IWA_02", "id": 2}, "reqs": []}, # Suspension Bridge Exit Left -> Mt Rugged 3 Exit Top Right
    {"from": {"map": "IWA_04", "id": 1}, "to": {"map": "SBK_99", "id": 0}, "reqs": []}, # Suspension Bridge Exit Right -> Entrance Exit Left

    {"from": {"map": "IWA_04", "id": 0}, "to": {"map": "IWA_04", "id": 1}, "reqs": [["Parakarry"]]}, #? Suspension Bridge Exit Left -> Suspension Bridge Exit Right
    {"from": {"map": "IWA_04", "id": 1}, "to": {"map": "IWA_04", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Suspension Bridge Exit Right -> Suspension Bridge Exit Left

    {"from": {"map": "IWA_04", "id": 0}, "to": {"map": "IWA_04", "id": "ItemA"}, "reqs": []}, #* Suspension Bridge Exit Left -> ItemA (Letter10)

    # IWA_10 Train Station
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_11", "id": 1}, "reqs": []}, # Train Station Ride The Train -> Train Ride Scene Exit Right
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_00", "id": 0}, "reqs": []}, # Train Station Exit Top Right -> Mt Rugged 1 Exit Left

    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": 1}, "reqs": [["Boots"]]}, #? Train Station Ride The Train -> Train Station Exit Top Right
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": 0}, "reqs": [["Boots"]]}, #? Train Station Exit Top Right -> Train Station Ride The Train

    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": "Bush1_Drop1"}, "reqs": []}, #* Train Station Ride The Train -> Bush1_Drop1 (Coin) Bottom Bush
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": "Bush1_Drop1"}, "reqs": []}, #* Train Station Exit Top Right -> Bush1_Drop1 (Coin) Bottom Bush
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": "Bush2_Drop1"}, "reqs": []}, #* Train Station Ride The Train -> Bush2_Drop1 (Coin) Right Bush
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": "Bush2_Drop1"}, "reqs": []}, #* Train Station Exit Top Right -> Bush2_Drop1 (Coin) Right Bush
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": "Bush3_Drop1"}, "reqs": []}, #* Train Station Ride The Train -> Bush3_Drop1 (Coin) Left Bush
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": "Bush3_Drop1"}, "reqs": []}, #* Train Station Exit Top Right -> Bush3_Drop1 (Coin) Left Bush
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": "Bush4_Drop1"}, "reqs": []}, #* TrainTrain Station Ride The Train -> Bush4_Drop1 (Egg2) Top Bush
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": "Bush4_Drop1"}, "reqs": []}, #* Train Station Exit Top Right -> Bush4_Drop1 (Egg2) Top Bush
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": "Partner"},     "reqs": [["has_parakarry_letters"]]}, #* Train Station Exit Top Right -> Partner (Parakarry)

    # IWA_11 Train Ride Scene
    {"from": {"map": "IWA_11", "id": 0}, "to": {"map": "MAC_03", "id": 1}, "reqs": []}, # Train Ride Scene Exit Left -> Station District Train
    {"from": {"map": "IWA_11", "id": 1}, "to": {"map": "IWA_10", "id": 0}, "reqs": []}, # Train Ride Scene Exit Right -> Train Station Ride The Train

    {"from": {"map": "IWA_11", "id": 0}, "to": {"map": "IWA_11", "id": 1}, "reqs": []}, #? Train Ride Scene Exit Left -> Train Ride Scene Exit Right
    {"from": {"map": "IWA_11", "id": 1}, "to": {"map": "IWA_11", "id": 0}, "reqs": []}, #? Train Ride Scene Exit Right -> Train Ride Scene Exit Left
]
