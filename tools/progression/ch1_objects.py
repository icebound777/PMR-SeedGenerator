locations = {
#map          check             item            removes            requires      #TODO index = least significat bit of dbkey
"nok_11":  [("Yellow?Block",    "FrightJar",    None,              None),
            ("Red?Block",       "DizzyAttack",  None,              None),
            ],

"nok_12":  [("Yellow?Block",    "POWBlock",     None,              None),
            ("BehindFence",     "SleepySheep",  None,              None),
            ("Island",          "StarPiece",    None,              [("Kooper",)]),
            ],

"nok_13":  [("BehindCane",      "HoneySyrup",   None,               None),
            ("Hidden?Block",    "AttackFXB",    None,               [("Hammer",)]),
            ("Panel",           "StarPiece",    None,               [("SuperBoots",), ("UltraHammer",)]),
            ],

"nok_01":  [("Bush1",           "DriedShroom",  None,               None),
            ("Bush2",           "KoopaLeaf",    None,               None),
            ("Bush3",           "EmptyWallet",  None,               [("KKF06",)]),
            ("Panel",           "EmptyWallet",  None,               [("SuperBoots",), ("UltraHammer",)]),
            ("MortTLetter",     "StarPiece",    ("Letter03",),      [("Parakarry", "Letter03")]),
            ("KooverLetter1",   "Letter15",     ("Letter14",),      [("Parakarry", "Letter14")]),
            ("KooverLetter2",   "Letter17",     ("Letter16",),      [("Parakarry", "Letter16")]),
            ],

"nok_02":  [("PushBlock",       "StarPiece",    None,               [("GF_HelpedKooper",)]),
            ("MrsColorado",     "KoopaLegends", None,               [("KKF01",)]),
#           ("KKF02",           "SilverCredit", ("SleepySheep",),   [("KKF02","SleepySheep")]),
#           ("KKF04",           "StarPiece(3)", ("KoopaTea",),      [("KKF04","KoopaTea")]),
#           ("KKF08",           "StarPiece(3)", ("Autograph2",),    [("KKF08","Autograph2")]),
#           ("KKF10",           "GoldCredit",   ("SilverCredit",
#                                                "LifeShroom"),     [("KKF08","LifeShroom")]),
#           ("KKF12",           "StarPiece(3)", None,               [("KKF12","GF_TalkenToBobombs")]),
#           ("KKF16",           "StarPiece(3)", ("Lime",),          [("KKF16","Lime")]),
#           ("KKF20",           "StarPiece(3)", ("RedJar",),        [("KKF20","RedJar")]),
            ],

"nok_03":  [("OntopOfBlock",    "HPPlusB",       None,              []),
            ],

"nok_04":  [("FuzzyGame1",      "KoopersShell",  None,              []),
            ("FuzzyGame2",      "Kooper",        ("KoopersShell",), [("KoopersShell",)]),
            ],

"nok_14":  [("OntopOfBlock",    "ThunderBolt",   None,              [("Kooper",), ("SuperBoots",)]),
            ("Hidden?Block",    "FireFlower",    None,              [("Kooper",)]),
            ("Panel",           "StarPiece",     None,              [("SuperBoots",), ("UltraHammer",)]),
            ],

"nok_15":  [("Tree",            "StarPiece",     None,              [("Kooper", "Hammer")]),
            ],

"trd_00":  [("ChestOnLedge",    "FPPlusB",       None,              [("Kooper", "Bombette")]),
            ("FarRightChest",   "Refund",        None,              [("Kooper", "Bombette", "FortressKey")]),
            ],

# remove column gets clumsy for Fortress Keys, so I just set them to None for now
"trd_01":  [("DefeatKoopa",     "FortressKey",   None,              [("Kooper",)]),
            ("Pedestal",        "SmashCharge",   None,              [("Kooper", "FortressKey", "FortressKey", "FortressKey", "FortressKey")]),
            ],

"trd_03":  [("LeftCell",        "FortressKey",   None,              [("Kooper", "Bombette", "FortressKey", "FortressKey", "FortressKey")]),
            ("MiddleCell",      "PowerBounce",   None,              [("Kooper", "FortressKey")]),
            ("RightCell",       "FortressKey",   None,              [("Kooper", "Bombette", "FortressKey")]),
            ],

"trd_08":  [("Pedestal",        "FortressKey",   None,              [("Kooper", "FortressKey")]),
            ],

"trd_06":  [("Jail",            "Bombette",      None,              [("Kooper", "FortressKey", "FortressKey"),
                                                                     ("Kooper", "Bombette", "FortressKey")]),
            ],

"trd_09":  [("Block",           "MapleSyrup",    None,              [("Kooper", "Bombette", "FortressKey", "FortressKey", "FortressKey", "FortressKey")]),
            ],

#"trd_10":  [("Boss",            "Eldstar",       None,              [("Kooper", "FortressKey", "FortressKey", "FortressKey", "FortressKey")]),
#            ],
}