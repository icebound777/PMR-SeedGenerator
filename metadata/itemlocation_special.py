"""
This file lists item locations that are, under certain circumstances, handled
in special ways.
"""

# Item locations that are associated with Koopa Koot's favors.
# These may be excluded from randomization.
kootfavors_reward_locations = [
    "NOK_02/GiftB", # Koopa Koot Reward SilverCredit
    "NOK_02/GiftC", # Koopa Koot Reward GoldCredit
    "NOK_02/KootGift00", # Koopa Koot Reward Coin
    "NOK_02/KootGift01", # Koopa Koot Reward Coin
    "NOK_02/KootGift02", # Koopa Koot Reward Coin
    "NOK_02/KootGift03", # Koopa Koot Reward StarPiecex3
    "NOK_02/KootGift04", # Koopa Koot Reward Coin
    "NOK_02/KootGift05", # Koopa Koot Reward Coin
    "NOK_02/KootGift06", # Koopa Koot Reward Coin
    "NOK_02/KootGift07", # Koopa Koot Reward StarPiecex3
    "NOK_02/KootGift08", # Koopa Koot Reward Coin
    "NOK_02/KootGift09", # Koopa Koot Reward Coin
    "NOK_02/KootGift0A", # Koopa Koot Reward Coin
    "NOK_02/KootGift0B", # Koopa Koot Reward StarPiecex3
    "NOK_02/KootGift0C", # Koopa Koot Reward Coin
    "NOK_02/KootGift0D", # Koopa Koot Reward Coin
    "NOK_02/KootGift0E", # Koopa Koot Reward Coin
    "NOK_02/KootGift0F", # Koopa Koot Reward StarPiecex3
    "NOK_02/KootGift10", # Koopa Koot Reward Coin
    "NOK_02/KootGift11", # Koopa Koot Reward Coin
    "NOK_02/KootGift12", # Koopa Koot Reward Coin
    "NOK_02/KootGift13", # Koopa Koot Reward StarPiecex3
]
kootfavors_keyitem_locations = [
    "NOK_01/Bush6A_Drop1A", # KootGlasses
    "NOK_01/Bush7A_Drop1A", # KootEmptyWallet
    "NOK_02/GiftA", # KoopaLegends
    "HOS_06/GiftA", # KootMerluvleeAutograph
    "OBK_01/GiftA", # KootOldPhoto
    "KMR_20/GiftA", # KootLuigiAutograph
    "KMR_02/GiftA", # KootTheTape
    "ARN_03/GiftA", # KootPackage
    "DRO_01/GiftB", # KootRedJar
    "DRO_02/GiftA", # CrystalBall
]

# Item locations that are associated with the letter chain sidequest.
# This quest is started by giving Goompapa in Goomba Village a specific letter
# and sends Mario around the world to acquire the Lucky Day badge in the end.
chainletter_giver_locations = [
    "KMR_02/GiftE", # Goompapa 1
    "OSR_01/GiftA", # Muss T.
    "NOK_01/GiftB", # Koover 1
    "MAC_05/GiftC", # Fishmael
    "NOK_01/GiftC", # Koover 2
    "DRO_02/GiftC", # Mr. E.
    "MAC_00/GiftC", # Miss T.
    "DRO_01/GiftC", # Little Mouser
    "OBK_01/GiftB", # Franky
    "MAC_03/GiftA", # Dane T. 1
    "JAN_03/GiftC", # Red Yoshi Kid
    "MAC_03/GiftB", # Dane T. 2
    "SAM_06/GiftB", # Frost T.
]
chainletter_final_reward_location = "KMR_02/GiftF" # Goompapa 2

simpleletter_locations = [
    "KMR_02/GiftD", # Goompa
    "MAC_00/GiftB", # Russ T.
    "MAC_01/GiftC", # Merlon
    "MAC_01/GiftD", # Minh T.
    "MAC_02/GiftC", # Fice T.
    "HOS_06/GiftB", # Merlow
    "NOK_01/GiftA", # Mort T.
    "NOK_02/GiftE", # Kolorado
    "SBK_34/GiftA", # Nomadimouse
    "OBK_03/GiftA", # Igor
    "SAM_01/GiftB", # Mayor Penguin
]

dojo_locations = [
    "MAC_00/DojoA",
    "MAC_00/DojoB",
    "MAC_00/DojoC",
    "MAC_00/DojoD",
    "MAC_00/DojoE",
]

bush_tree_coin_locations = [
    "KMR_02/Bush2_Drop1",
    "KMR_04/Bush1_Drop1",
    "KMR_04/Bush2_Drop1",
    "KMR_04/Bush3_Drop1A",
    "KMR_04/Bush3_Drop1B",
    "KMR_04/Bush4_Drop1",
    "KMR_04/Bush5_Drop1",
    "KMR_04/Tree1_Drop1",
    "KMR_04/Tree2_Drop1",
    "KMR_05/Tree1_Drop1A",
    "KMR_11/Tree2_Drop1",

    "NOK_01/Bush1_Drop1A",
    "NOK_01/Bush5_Drop1A",
    "NOK_02/Bush6_Drop1",

    "IWA_10/Bush1_Drop1",
    "IWA_10/Bush2_Drop1",
    "IWA_10/Bush3_Drop1",

    "DRO_01/Tree1_Drop1",

    "SBK_06/Tree1_Drop1",
    "SBK_26/Tree1_Drop1",
    "SBK_34/Tree1_Drop1",
    "SBK_35/Tree1_Drop1",
    "SBK_36/Tree1_Drop1",
    "SBK_36/Tree2_Drop1",
    "SBK_36/Tree6_Drop1",
    "SBK_46/Tree2_Drop1",
    "SBK_55/Tree1_Drop1",
    "SBK_56/Tree3_Drop1",
    "SBK_56/Tree9_Drop1",
    "SBK_66/Tree3_Drop1",

    "JAN_05/Bush1_Drop1",
    "JAN_05/Bush2_Drop1",
    "JAN_05/Tree2_Drop1",
    "JAN_06/Tree1_Drop1",
    "JAN_07/Tree1_Drop1",
    "JAN_08/Bush1_Drop1",
    "JAN_08/Bush2_Drop1",
    "JAN_08/Tree2_Drop1",
    "JAN_08/Tree3_Drop1",
    "JAN_09/Bush1_Drop1",
    "JAN_09/Bush6_Drop1",
    "JAN_09/Tree2_Drop1",
    "JAN_12/Tree1_Drop2",
    "JAN_13/Tree1_Drop1",
    "JAN_15/Tree2_Drop1",
]

overworld_coin_locations = [
    "KMR_03/ItemA",
    "KMR_03/ItemB",
    "KMR_03/ItemC",
    "KMR_03/ItemD",

    "NOK_14/ItemA",
    "NOK_14/ItemB",
    "NOK_14/ItemC",
    "NOK_14/ItemD",
    "NOK_14/ItemE",

    "IWA_00/ItemA",
    "IWA_00/ItemB",
    "IWA_00/ItemC",
    "IWA_03/ItemC",
    "IWA_03/ItemD",
    "IWA_03/ItemE",
    "IWA_03/ItemF",
    "IWA_03/ItemG",
    "IWA_03/ItemH",
    "IWA_03/ItemI",
    "IWA_03/ItemJ",

    "DGB_13/ItemB",
    "DGB_13/ItemC",
    "DGB_13/ItemD",
    "DGB_13/ItemE",
    "DGB_13/ItemF",
    "DGB_13/ItemG",

    "OMO_04/ItemB",
    "OMO_04/ItemC",
    "OMO_04/ItemD",
    "OMO_04/ItemE",
    "OMO_04/ItemF",
    "OMO_04/ItemG",
    "OMO_04/ItemH",
    "OMO_04/ItemI",
    "OMO_09/ItemB",
    "OMO_09/ItemC",
    "OMO_09/ItemD",
    "OMO_09/ItemE",
    "OMO_09/ItemF",
    "OMO_09/ItemG",
    "OMO_09/ItemI",
    "OMO_09/ItemJ",
    "OMO_09/ItemK",
    "OMO_09/ItemL",
    "OMO_09/ItemM",
    "OMO_09/ItemN",

    "JAN_00/ItemA",
    "JAN_00/ItemB",
    "JAN_01/ItemB",
    "JAN_01/ItemC",
    "JAN_06/ItemA",
    "JAN_08/ItemA",
    "JAN_08/ItemB",
    "JAN_08/ItemC",
]

block_coin_locations = [
    "KMR_03/YBlockA",
    "KMR_09/YBlockA",
    "KMR_09/YBlockB",

    "TIK_03/YBlockB",
    "TIK_03/YBlockC",
    "TIK_10/HiddenYBlockA",
    "TIK_10/HiddenYBlockB",
    "TIK_10/HiddenYBlockC",
    "TIK_21/YBlockA",
    "TIK_21/YBlockB",
    "TIK_21/YBlockC",
    "TIK_21/YBlockD",
    "TIK_21/YBlockE",
    "TIK_23/YBlockA",
    "TIK_24/YBlockA",
    "TIK_24/YBlockB",

    "NOK_11/YBlockA",

    "SBK_00/YBlockB",
    "SBK_14/YBlockA",
    "SBK_22/YBlockA",
    "SBK_22/YBlockB",
    "SBK_22/YBlockC",
    "SBK_22/YBlockD",
    "SBK_43/YBlockA",
    "SBK_46/YBlockA",
    "SBK_64/YBlockA",

    "IWA_03/YBlockA",

    "ARN_02/YBlockA",
    "ARN_02/YBlockB",
    "ARN_03/YBlockA",
    "ARN_04/YBlockB",

    "OMO_02/HiddenYBlockA",
    "OMO_04/YBlockA",
    "OMO_04/YBlockB",
    "OMO_05/YBlockA",
    "OMO_05/YBlockB",
    "OMO_07/YBlockA",
    "OMO_11/YBlockA",
    "OMO_11/YBlockB",
    "OMO_13/YBlockA",
    "OMO_17/YBlockA",
    "OMO_17/YBlockB",
    "OMO_17/YBlockC",

    "KZN_03/YBlockA",
    "KZN_03/YBlockB",
    "KZN_03/YBlockC",
    "KZN_03/YBlockD",

    "FLO_23/HiddenYBlockB",
]

favor_coin_locations = [
    "NOK_02/KootGift00",
    "NOK_02/KootGift01",
    "NOK_02/KootGift02",
    "NOK_02/KootGift04",
    "NOK_02/KootGift05",
    "NOK_02/KootGift06",
    "NOK_02/KootGift08",
    "NOK_02/KootGift09",
    "NOK_02/KootGift0A",
    "NOK_02/KootGift0C",
    "NOK_02/KootGift0D",
    "NOK_02/KootGift0E",
    "NOK_02/KootGift10",
    "NOK_02/KootGift11",
    "NOK_02/KootGift12",
]

radio_trade_event_locations = [
    "MAC_00/GiftD",
    "SBK_02/GiftA",
    "MAC_05/GiftD",
]

# Areas that are considered 'limited by item'.
# 'Limited by item' areas are only allowed to hold a subset of specific
# randomized items, instead of every item available in the pool.
# However, if every allowed item is already placed somewhere, these areas
# are again allowed to hold other items.
# This is used for limiting progression items to certain areas.
limited_by_item_areas = {
    # Chapter 1 Koopa Bros Fortress
    "TRD": {
        "keys": [
            "KoopaFortressKeyA",
            "KoopaFortressKeyB",
            "KoopaFortressKeyC",
            "KoopaFortressKeyD",
        ]
    },
    # Chapter 2 Dry Dry Ruins
    "ISK": {
        "keys": [
            "RuinsKeyA",
            "RuinsKeyB",
            "RuinsKeyC",
            "RuinsKeyD",
            "PyramidStone",
            "LunarStone",
            "DiamondStone",
        ]
    },
    # Chapter 3 Tubba Blubba's Castle
    "DGB": {
        "keys": [
            "TubbaCastleKeyA",
            "TubbaCastleKeyB",
            "TubbaCastleKeyC",
        ]
    },
    # Chapter 4 Shy Guy's Toybox
    "OMO": {
        "keys": [
            "FryingPan",
            "ToyTrain",
            "Dictionary",
            "MysteryNote"
        ],
        "misc": [
            "CakeMix",
        ]
    },
    # Chapter 5 Mt. Lavalava
    # Chapter 6 Flower Fields
    "FLO": {
        "keys": [
            "MagicalBean",
            "FertileSoil",
            "MiracleWater",
            "CrystalBerry",
            "WaterStone",
        ],
        "misc": [
            "BubbleBerry",
            "RedBerry",
            "BlueBerry",
            "YellowBerry"
        ]
    },
    # Chapter 7 Crystal Palace
    "PRA": {
        "keys": [
            "BlueKey",
            "RedKey",
            "CrystalPalaceKey",
        ]
    },
    # Chapter 8 Bowser's Castle
    "KPA": {
        "keys": [
            "BowserCastleKeyA",
            "BowserCastleKeyB",
            "BowserCastleKeyC",
            "BowserCastleKeyD",
            "BowserCastleKeyE",
        ]
    },
}

# Item locations that are considered 'limited by item type'.
# 'Limited by item type' locations are only allowed to hold a items of a certain
# item type, instead of every item available in the pool.
# This is used for limiting randomization of certain item types (like keyitems, 
# badges), so they are easier to find.
limited_by_itemtype_locations = [

]
