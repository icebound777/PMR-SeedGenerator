locations = {
#map          check             item            requires      #TODO index = least significat bit of dbkey
"nok_11":  [("Yellow?Block",    "FrightJar",    None),
            ("Red?Block",       "DizzyAttack",  None),
            ],

"nok_12":  [("Yellow?Block",    "POWBlock",     None),
            ("BehindFence",     "SleepySheep",  None),
            ("Island",          "StarPiece",    [("Kooper",)]),
            ],

"nok_13":  [("BehindCane",      "HoneySyrup",   None),
            ("Hidden?Block",    "AttackFXB",    [("Hammer",)]),
            ("Panel",           "StarPiece",    [("SuperBoots",), ("UltraHammer",)]),
            ],

"nok_01":  [("Bush1",           "DriedShroom",  None),
            ("Bush2",           "KoopaLeaf",    None),
            ("Bush3",           "EmptyWallet",  [("KKF06",)]),
            ("Panel",           "EmptyWallet",  [("SuperBoots",), ("UltraHammer",)]),
            ("MortTLetter",     "StarPiece",    [("Parakarry", "Letter03")]),
            ("KooverLetter1",   "Letter15",     [("Parakarry", "Letter14")]),
            ("KooverLetter2",   "Letter17",     [("Parakarry", "Letter16")]),
            ],

"nok_02":  [("PushBlock",       "StarPiece",    [("GF_HelpedKooper",)]),
            ("MrsColorado",     "KoopaLegends", [("KKF01",)]),
#           ("KKF02",           "SilverCredit", [("KKF02","SleepySheep")]),
#           ("KKF04",           "StarPiece(3)", [("KKF04","KoopaTea")]),
#           ("KKF08",           "StarPiece(3)", [("KKF08","Autograph2")]),
#           ("KKF10",           "GoldCredit",   [("KKF08","LifeShroom")]),
#           ("KKF12",           "StarPiece(3)", [("KKF12","GF_TalkenToBobombs")]),
#           ("KKF16",           "StarPiece(3)", [("KKF16","Lime")]),
#           ("KKF20",           "StarPiece(3)", [("KKF20","RedJar")]),
            ],

"nok_03":  [("OntopOfBlock",    "HPPlusB",      None),
            ],

"nok_04":  [("FuzzyGame1",      "KoopersShell", None),
            ("FuzzyGame2",      "Kooper",       [("KoopersShell",)]),
            ],

"nok_14":  [("OntopOfBlock",    "ThunderBolt",  [("Kooper",), ("SuperBoots",)]),
            ("Hidden?Block",    "FireFlower",   [("Kooper",)]),
            ("Panel",           "StarPiece",    [("SuperBoots",), ("UltraHammer",)]),
            ],

"nok_15":  [("Tree",            "StarPiece",    [("Kooper", "Hammer")]),
            ],

"trd_00":  [("ChestOnLedge",    "FPPlusB",      [("Kooper", "Bombette")]),
            ("FarRightChest",   "Refund",       [("Kooper", "Bombette", "FortressKey")]),
            ],

"trd_01":  [("DefeatKoopa",     "FortressKey",  [("Kooper",)]),
            ("Pedestal",        "SmashCharge",  [("Kooper", "FortressKey", "FortressKey", "FortressKey", "FortressKey")]),
            ],

"trd_03":  [("LeftCell",        "FortressKey",  [("Kooper", "Bombette", "FortressKey", "FortressKey", "FortressKey")]),
            ("MiddleCell",      "PowerBounce",  [("Kooper", "FortressKey")]),
            ("RightCell",       "FortressKey",  [("Kooper", "Bombette", "FortressKey")]),
            ],

"trd_08":  [("Pedestal",        "FortressKey",  [("Kooper", "FortressKey")]),
            ],

"trd_06":  [("Jail",            "Bombette",     [("Kooper", "FortressKey", "FortressKey"),
                                                 ("Kooper", "Bombette", "FortressKey")]),
            ],

"trd_09":  [("Block",           "MapleSyrup",   [("Kooper", "Bombette", "FortressKey", "FortressKey", "FortressKey", "FortressKey")]),
            ],

#"trd_10":  [("Boss",            "Eldstar",      [("Kooper", "FortressKey", "FortressKey", "FortressKey", "FortressKey")]),
#            ],
}