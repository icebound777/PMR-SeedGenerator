"""This file represents all edges of the world graph that have origin-nodes in the KPA (Bowser's Castle) area."""
edges_kpa = [
    # KPA_01 Dark Cave 1
    {"from": {"map": "KPA_01",  "id": 0}, "to": {"map": "KPA_14",  "id": 1}, "reqs": []}, # Dark Cave 1 Door Bottom Left -> Lava Channel 3 Door Right
    {"from": {"map": "KPA_01",  "id": 1}, "to": {"map": "KPA_03",  "id": 0}, "reqs": []}, # Dark Cave 1 Exit Top Left -> Dark Cave 2 Exit Right

    {"from": {"map": "KPA_01",  "id": 0}, "to": {"map": "KPA_01",  "id": 1}, "reqs": [["Parakarry"]]}, #? Dark Cave 1 Door Bottom Left -> Dark Cave 1 Exit Top Left
    {"from": {"map": "KPA_01",  "id": 1}, "to": {"map": "KPA_01",  "id": 0}, "reqs": []}, #? Dark Cave 1 Exit Top Left -> Dark Cave 1 Door Bottom Left

    {"from": {"map": "KPA_01",  "id": 1}, "to": {"map": "KPA_01",  "id": "YBlockA"}, "reqs": [["Parakarry"],["can_hit_floating_blocks"]]}, #* Dark Cave 1 Exit Top Left -> YBlockA (POWBlock)

    # KPA_03 Dark Cave 2
    {"from": {"map": "KPA_03",  "id": 0}, "to": {"map": "KPA_01",  "id": 1}, "reqs": []}, # Dark Cave 2 Exit Right -> Dark Cave 1 Exit Top Left
    {"from": {"map": "KPA_03",  "id": 1}, "to": {"map": "KPA_04",  "id": 0}, "reqs": []}, # Dark Cave 2 Door Top Left -> Cave Exit Door Right

    {"from": {"map": "KPA_03",  "id": 0}, "to": {"map": "KPA_03",  "id": 1}, "reqs": [["Parakarry"]]}, #? Dark Cave 2 Exit Right -> Dark Cave 2 Door Top Left
    {"from": {"map": "KPA_03",  "id": 1}, "to": {"map": "KPA_03",  "id": 0}, "reqs": [["can_climb_steps"]]}, #? Dark Cave 2 Door Top Left -> Dark Cave 2 Exit Right

    {"from": {"map": "KPA_03",  "id": 0}, "to": {"map": "KPA_03",  "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Dark Cave 2 Exit Right -> YBlockA (ShootingStar)

    # KPA_04 Cave Exit
    {"from": {"map": "KPA_04",  "id": 0}, "to": {"map": "KPA_03",  "id": 1}, "reqs": []}, # Cave Exit Door Right -> Dark Cave 2 Door Top Left
    {"from": {"map": "KPA_04",  "id": 1}, "to": {"map": "KPA_81",  "id": 3}, "reqs": []}, # Cave Exit Hidden Door Bottom -> Guard Door 1 Hidden Door Top

    {"from": {"map": "KPA_04",  "id": 0}, "to": {"map": "KPA_04",  "id": 1}, "reqs": []}, #? Cave Exit Door Right -> Cave Exit Hidden Door Bottom
    {"from": {"map": "KPA_04",  "id": 1}, "to": {"map": "KPA_04",  "id": 0}, "reqs": []}, #? Cave Exit Hidden Door Bottom -> Cave Exit Door Right

    # KPA_08 Castle Key Timing Puzzle
    {"from": {"map": "KPA_08",  "id": 0}, "to": {"map": "KPA_52",  "id": 2}, "reqs": []}, # Castle Key Timing Puzzle Door Left -> Split Level Hall Door Top Right
    {"from": {"map": "KPA_08",  "id": 1}, "to": {"map": "KPA_100", "id": 0}, "reqs": []}, # Castle Key Timing Puzzle Door Right -> Castle Key Room Door Left

    {"from": {"map": "KPA_08",  "id": 0}, "to": {"map": "KPA_08",  "id": 1}, "reqs": [["Kooper","Bombette"],["Boots"]]}, #? Castle Key Timing Puzzle Door Left -> Castle Key Timing Puzzle Door Right
    {"from": {"map": "KPA_08",  "id": 1}, "to": {"map": "KPA_08",  "id": 0}, "reqs": []}, #? Castle Key Timing Puzzle Door Right -> Castle Key Timing Puzzle Door Left

    # KPA_09 Ultra Shroom Timing Puzzle
    {"from": {"map": "KPA_09",  "id": 0}, "to": {"map": "KPA_101", "id": 0}, "reqs": []}, # Ultra Shroom Timing Puzzle Door Left -> Ultra Shroom Room Door Right
    {"from": {"map": "KPA_09",  "id": 1}, "to": {"map": "KPA_33",  "id": 3}, "reqs": []}, # Ultra Shroom Timing Puzzle Door Right -> Upper Grand Hall Door Top Left

    {"from": {"map": "KPA_09",  "id": 0}, "to": {"map": "KPA_09",  "id": 1}, "reqs": []}, #? Ultra Shroom Timing Puzzle Door Left -> Ultra Shroom Timing Puzzle Door Right
    {"from": {"map": "KPA_09",  "id": 1}, "to": {"map": "KPA_09",  "id": 0}, "reqs": [["Bombette"],["Boots"]]}, #? Ultra Shroom Timing Puzzle Door Right -> Ultra Shroom Timing Puzzle Door Left

    # KPA_10 Outside Lower Jail (No Lava)
    {"from": {"map": "KPA_10",  "id": 0}, "to": {"map": "KPA_62",  "id": 1}, "reqs": []}, # Outside Lower Jail (No Lava) Door Top Left -> Front Door Exterior Door Right
    {"from": {"map": "KPA_10",  "id": 1}, "to": {"map": "KPA_12",  "id": 0}, "reqs": []}, # Outside Lower Jail (No Lava) Door Right -> Lava Channel 1 Door Left
    {"from": {"map": "KPA_10",  "id": 2}, "to": {"map": "KPA_17",  "id": 1}, "reqs": []}, # Outside Lower Jail (No Lava) Cracked Wall To Jail -> Lower Jail Cracked Wall Right
    {"from": {"map": "KPA_10",  "id": 3}, "to": {"map": "KPA_62",  "id": 2}, "reqs": []}, # Outside Lower Jail (No Lava) Lava Door Left -> Front Door Exterior Lava Door Right
    {"from": {"map": "KPA_10",  "id": 4}, "to": {"map": "KPA_12",  "id": 2}, "reqs": []}, # Outside Lower Jail (No Lava) Lava Door Right -> Lava Channel 1 Lava Door Left

    {"from": {"map": "KPA_10",  "id": 1}, "to": {"map": "KPA_10",  "id": 2}, "reqs": []}, #? Outside Lower Jail (No Lava) Door Right -> Outside Lower Jail (No Lava) Cracked Wall To Jail
    {"from": {"map": "KPA_10",  "id": 2}, "to": {"map": "KPA_10",  "id": 1}, "reqs": []}, #? Outside Lower Jail (No Lava) Cracked Wall To Jail -> Outside Lower Jail (No Lava) Door Right
    {"from": {"map": "KPA_10",  "id": 3}, "to": {"map": "KPA_10",  "id": 4}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Outside Lower Jail (No Lava) Lava Door Left -> Outside Lower Jail (No Lava) Lava Door Right
    {"from": {"map": "KPA_10",  "id": 4}, "to": {"map": "KPA_10",  "id": 3}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Outside Lower Jail (No Lava) Lava Door Right -> Outside Lower Jail (No Lava) Lava Door Left

    {"from": {"map": "KPA_10",  "id": 4}, "to": {"map": "KPA_10",  "id": "YBlockA"}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"],["can_hit_floating_blocks"]]}, #* Outside Lower Jail (No Lava) Lava Door Right -> YBlockA (LifeShroom)

    # KPA_11 Outside Lower Jail (Lava)
    {"from": {"map": "KPA_11",  "id": 0}, "to": {"map": "KPA_62",  "id": 1}, "reqs": []}, # Outside Lower Jail (Lava) Door Top Left -> Front Door Exterior Door Right
    {"from": {"map": "KPA_11",  "id": 1}, "to": {"map": "KPA_12",  "id": 0}, "reqs": []}, # Outside Lower Jail (Lava) Door Right -> Lava Channel 1 Door Left
    {"from": {"map": "KPA_11",  "id": 2}, "to": {"map": "KPA_17",  "id": 1}, "reqs": []}, # Outside Lower Jail (Lava) Cracked Wall To Jail -> Lower Jail Cracked Wall Right
    {"from": {"map": "KPA_11",  "id": 3}, "to": {"map": "KPA_62",  "id": 2}, "reqs": []}, # Outside Lower Jail (Lava) Lava Door Left -> Front Door Exterior Lava Door Right
    {"from": {"map": "KPA_11",  "id": 4}, "to": {"map": "KPA_12",  "id": 2}, "reqs": []}, # Outside Lower Jail (Lava) Lava Door Right -> Lava Channel 1 Lava Door Left

    {"from": {"map": "KPA_11",  "id": 1}, "to": {"map": "KPA_11",  "id": 2}, "reqs": []}, #? Outside Lower Jail (Lava) Door Right -> Outside Lower Jail (Lava) Cracked Wall To Jail
    {"from": {"map": "KPA_11",  "id": 2}, "to": {"map": "KPA_11",  "id": 1}, "reqs": []}, #? Outside Lower Jail (Lava) Cracked Wall To Jail -> Outside Lower Jail (Lava) Door Right
    {"from": {"map": "KPA_11",  "id": 3}, "to": {"map": "KPA_11",  "id": 4}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Outside Lower Jail (Lava) Lava Door Left -> Outside Lower Jail (Lava) Lava Door Right
    {"from": {"map": "KPA_11",  "id": 4}, "to": {"map": "KPA_11",  "id": 3}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Outside Lower Jail (Lava) Lava Door Right -> Outside Lower Jail (Lava) Lava Door Left

    {"from": {"map": "KPA_11",  "id": 0}, "to": {"map": "KPA_11",  "id": "ItemA"}, "reqs": []}, #* Outside Lower Jail (Lava) Door Top Left -> ItemA (BowserCastleKey)

    # KPA_12 Lava Channel 1
    {"from": {"map": "KPA_12",  "id": 0}, "to": {"map": "KPA_10",  "id": 1}, "reqs": []}, # Lava Channel 1 Door Left -> Outside Lower Jail (No Lava) Door Right
    {"from": {"map": "KPA_12",  "id": 0}, "to": {"map": "KPA_11",  "id": 1}, "reqs": []}, # Lava Channel 1 Door Left -> Outside Lower Jail (Lava) Door Right
    {"from": {"map": "KPA_12",  "id": 1}, "to": {"map": "KPA_13",  "id": 0}, "reqs": []}, # Lava Channel 1 Door Right -> Lava Channel 2 Door Left
    {"from": {"map": "KPA_12",  "id": 2}, "to": {"map": "KPA_10",  "id": 4}, "reqs": []}, # Lava Channel 1 Lava Door Left -> Outside Lower Jail (No Lava) Lava Door Right
    {"from": {"map": "KPA_12",  "id": 2}, "to": {"map": "KPA_11",  "id": 4}, "reqs": []}, # Lava Channel 1 Lava Door Left -> Outside Lower Jail (Lava) Lava Door Right

    {"from": {"map": "KPA_12",  "id": 0}, "to": {"map": "KPA_12",  "id": 1}, "reqs": [["Boots"]]}, #? Lava Channel 1 Door Left -> Lava Channel 1 Door Right
    #+ note for above: while can_climb_steps would be okay for lava active, lava inactive hard-requires Boots
    {"from": {"map": "KPA_12",  "id": 1}, "to": {"map": "KPA_12",  "id": 0}, "reqs": [["can_climb_steps","GF_KPA16_ShutOffLava"]]}, #? Lava Channel 1 Door Right -> Lava Channel 1 Door Left
    {"from": {"map": "KPA_12",  "id": 0}, "to": {"map": "KPA_12",  "id": 2}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Lava Channel 1 Door Left -> Lava Channel 1 Lava Door Left
    {"from": {"map": "KPA_12",  "id": 2}, "to": {"map": "KPA_12",  "id": 0}, "reqs": []}, #? Lava Channel 1 Lava Door Left -> Lava Channel 1 Door Left

    # KPA_13 Lava Channel 2
    {"from": {"map": "KPA_13",  "id": 0}, "to": {"map": "KPA_12",  "id": 1}, "reqs": []}, # Lava Channel 2 Door Left -> Lava Channel 1 Door Right
    {"from": {"map": "KPA_13",  "id": 1}, "to": {"map": "KPA_14",  "id": 0}, "reqs": []}, # Lava Channel 2 Door Right -> Lava Channel 3 Door Left
    {"from": {"map": "KPA_13",  "id": 2}, "to": {"map": "KPA_15",  "id": 0}, "reqs": []}, # Lava Channel 2 Lava Door Center -> Lava Key Room Door Left

    {"from": {"map": "KPA_13",  "id": 0}, "to": {"map": "KPA_13",  "id": 1}, "reqs": [["Parakarry","GF_KPA16_ShutOffLava"],["Lakilester","Boots","GF_KPA16_ShutOffLava"],["can_climb_steps"]]}, #? Lava Channel 2 Door Left -> Lava Channel 2 Door Right
    #+ note: above minimized from: "(Parakarry AND (Parakarry OR Lakilester) AND (can_climb_steps OR Hammer OR Kooper OR Bombette) AND (Lakilester OR Boots)) OR (Lava off AND can_climb_steps)"
    {"from": {"map": "KPA_13",  "id": 1}, "to": {"map": "KPA_13",  "id": 0}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Lava Channel 2 Door Right -> Lava Channel 2 Door Left
    {"from": {"map": "KPA_13",  "id": 0}, "to": {"map": "KPA_13",  "id": 2}, "reqs": [["can_climb_steps"],["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Lava Channel 2 Door Left -> Lava Channel 2 Lava Door Center
    {"from": {"map": "KPA_13",  "id": 2}, "to": {"map": "KPA_13",  "id": 0}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Lava Channel 2 Lava Door Center -> Lava Channel 2 Door Left

    # KPA_14 Lava Channel 3
    {"from": {"map": "KPA_14",  "id": 0}, "to": {"map": "KPA_13",  "id": 1}, "reqs": []}, # Lava Channel 3 Door Left -> Lava Channel 2 Door Right
    {"from": {"map": "KPA_14",  "id": 1}, "to": {"map": "KPA_01",  "id": 0}, "reqs": [[{"BowserCastleKey": 2}]]}, # Lava Channel 3 Door Right -> Dark Cave 1 Door Bottom Left
    {"from": {"map": "KPA_14",  "id": 2}, "to": {"map": "KPA_16",  "id": 0}, "reqs": []}, # Lava Channel 3 Lava Door Center -> Lava Control Room Lava Door Left

    {"from": {"map": "KPA_14",  "id": 0}, "to": {"map": "KPA_14",  "id": 1}, "reqs": [["GF_KPA16_ShutOffLava"],["can_climb_steps"]]}, #? Lava Channel 3 Door Left -> Lava Channel 3 Door Right

    {"from": {"map": "KPA_14",  "id": 1}, "to": {"map": "KPA_14",  "id": 0}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Lava Channel 3 Door Right -> Lava Channel 3 Door Left
    {"from": {"map": "KPA_14",  "id": 0}, "to": {"map": "KPA_14",  "id": 2}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"],["Bow","GF_KPA16_ShutOffLava"],["Parakarry","GF_KPA16_ShutOffLava"],["can_climb_steps"]]}, #? Lava Channel 3 Door Left -> Lava Channel 3 Lava Door Center
    {"from": {"map": "KPA_14",  "id": 2}, "to": {"map": "KPA_14",  "id": 0}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"]]}, #? Lava Channel 3 Lava Door Center -> Lava Channel 3 Door Left

    {"from": {"map": "KPA_14",  "id": 0}, "to": {"map": "KPA_14",  "id": "ItemA"}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"],["Lakilester","can_climb_steps"],["Kooper","Parakarry","GF_KPA16_ShutOffLava"],["Kooper","can_climb_steps"],["can_climb_steps","GF_KPA16_ShutOffLava"]]}, #* Lava Channel 3 Door Left -> ItemA (Mystery)
    #+ note: above set up from: "(Laki AND (Kooper OR Parakarry) AND can_climb_steps[lava-failsafe]) OR (Lava off AND can_climb_steps)"
    {"from": {"map": "KPA_14",  "id": 0}, "to": {"map": "KPA_14",  "id": "ItemB"}, "reqs": [["GF_KPA16_ShutOffLava"],["Boots"]]}, #* Lava Channel 3 Door Left -> ItemB (ThunderRage)

    # KPA_15 Lava Key Room
    {"from": {"map": "KPA_15",  "id": 0}, "to": {"map": "KPA_13",  "id": 2}, "reqs": []}, # Lava Key Room Door Left -> Lava Channel 2 Lava Door Center

    {"from": {"map": "KPA_15",  "id": 0}, "to": {"map": "KPA_15",  "id": "ChestA"}, "reqs": [["GF_KPA16_ShutOffLava"],["can_climb_steps"]]}, #* Lava Key Room Door Left -> ChestA (BowserCastleKey)

    # KPA_16 Lava Control Room
    {"from": {"map": "KPA_16",  "id": 0}, "to": {"map": "KPA_14",  "id": 2}, "reqs": []}, # Lava Control Room Lava Door Left -> Lava Channel 3 Lava Door Center

    {"from": {"map": "KPA_16",  "id": 0}, "to": {"map": "KPA_16",  "id": 0}, "reqs": [["Lakilester"],["can_climb_steps"]], "pseudoitems": ["GF_KPA16_ShutOffLava"]}, #+ Shut off Lava Control

    # KPA_17 Lower Jail
    #{"from": {"map": "KPA_17",  "id": 0}, "to": {"map": None, "id": None}, "reqs": []},   # Lower Jail Fall From Ceiling
    {"from": {"map": "KPA_17",  "id": 1}, "to": {"map": "KPA_10",  "id": 2}, "reqs": []}, # Lower Jail Cracked Wall Right -> Outside Lower Jail (No Lava) Cracked Wall To Jail
    {"from": {"map": "KPA_17",  "id": 1}, "to": {"map": "KPA_11",  "id": 2}, "reqs": []}, # Lower Jail Cracked Wall Right -> Outside Lower Jail (Lava) Cracked Wall To Jail

    {"from": {"map": "KPA_17",  "id": 0}, "to": {"map": "KPA_17",  "id": 1}, "reqs": [["Bombette"]]}, #? Lower Jail Fall From Ceiling -> Lower Jail Cracked Wall Right
    {"from": {"map": "KPA_17",  "id": 1}, "to": {"map": "KPA_17",  "id": 0}, "reqs": []}, #? Lower Jail Cracked Wall Right -> Lower Jail Fall From Ceiling

    {"from": {"map": "KPA_17",  "id": 0},        "to": {"map": "KPA_17",  "id": "CrateA"}, "reqs": [["SuperBoots"]]}, #* Lower Jail Fall From Ceiling -> CrateA (TastyTonic)
    {"from": {"map": "KPA_17",  "id": "CrateA"}, "to": {"map": "KPA_17",  "id": "CrateB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> CrateB (LifeShroom)

    # KPA_32 Lower Grand Hall
    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_81",  "id": 2}, "reqs": []}, # Lower Grand Hall Door Bottom Left -> Guard Door 1 Guard Door Right
    {"from": {"map": "KPA_32",  "id": 1}, "to": {"map": "KPA_90",  "id": 0}, "reqs": []}, # Lower Grand Hall Door Bottom Right -> Stairs to East Upper Jail Door Top Left
    {"from": {"map": "KPA_32",  "id": 2}, "to": {"map": "KPA_51",  "id": 0}, "reqs": []}, # Lower Grand Hall Door Top Right -> Hall to Water Puzzle Door Left
    {"from": {"map": "KPA_32",  "id": 3}, "to": {"map": "KPA_96",  "id": 0}, "reqs": []}, # Lower Grand Hall Door Top Left -> Item Shop Door Right

    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_32",  "id": 1}, "reqs": []}, #? Lower Grand Hall Door Bottom Left -> Lower Grand Hall Door Bottom Right
    {"from": {"map": "KPA_32",  "id": 1}, "to": {"map": "KPA_32",  "id": 0}, "reqs": []}, #? Lower Grand Hall Door Bottom Right -> Lower Grand Hall Door Bottom Left
    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_32",  "id": 2}, "reqs": [["Boots"]]}, #? Lower Grand Hall Door Bottom Left -> Lower Grand Hall Door Top Right
    {"from": {"map": "KPA_32",  "id": 2}, "to": {"map": "KPA_32",  "id": 0}, "reqs": []}, #? Lower Grand Hall Door Top Right -> Lower Grand Hall Door Bottom Left
    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_32",  "id": 3}, "reqs": [["Boots"]]}, #? Lower Grand Hall Door Bottom Left -> Lower Grand Hall Door Top Left
    {"from": {"map": "KPA_32",  "id": 3}, "to": {"map": "KPA_32",  "id": 0}, "reqs": []}, #? Lower Grand Hall Door Top Left -> Lower Grand Hall Door Bottom Left

    # KPA_33 Upper Grand Hall
    {"from": {"map": "KPA_33",  "id": 0}, "to": {"map": "KPA_94",  "id": 1}, "reqs": []}, # Upper Grand Hall Door Bottom Left -> Stairs to West Upper Jail Door Top Right
    {"from": {"map": "KPA_33",  "id": 1}, "to": {"map": "KPA_61",  "id": 1}, "reqs": []}, # Upper Grand Hall Door Bottom Right -> Battlement Door Top Left
    {"from": {"map": "KPA_33",  "id": 2}, "to": {"map": "KPA_52",  "id": 0}, "reqs": []}, # Upper Grand Hall Door Top Right -> Split Level Hall Door Left
    {"from": {"map": "KPA_33",  "id": 3}, "to": {"map": "KPA_09",  "id": 1}, "reqs": []}, # Upper Grand Hall Door Top Left -> Ultra Shroom Timing Puzzle Door Right

    {"from": {"map": "KPA_33",  "id": 0}, "to": {"map": "KPA_33",  "id": 1}, "reqs": []}, #? Upper Grand Hall Door Bottom Left -> Upper Grand Hall Door Bottom Right
    {"from": {"map": "KPA_33",  "id": 1}, "to": {"map": "KPA_33",  "id": 0}, "reqs": []}, #? Upper Grand Hall Door Bottom Right -> Upper Grand Hall Door Bottom Left
    {"from": {"map": "KPA_33",  "id": 0}, "to": {"map": "KPA_33",  "id": 2}, "reqs": [["Boots"]]}, #? Upper Grand Hall Door Bottom Left -> Upper Grand Hall Door Top Right
    {"from": {"map": "KPA_33",  "id": 2}, "to": {"map": "KPA_33",  "id": 0}, "reqs": []}, #? Upper Grand Hall Door Top Right -> Upper Grand Hall Door Bottom Left
    {"from": {"map": "KPA_33",  "id": 0}, "to": {"map": "KPA_33",  "id": 3}, "reqs": [["Boots"]]}, #? Upper Grand Hall Door Bottom Left -> Upper Grand Hall Door Top Left
    {"from": {"map": "KPA_33",  "id": 3}, "to": {"map": "KPA_33",  "id": 0}, "reqs": []}, #? Upper Grand Hall Door Top Left -> Upper Grand Hall Door Bottom Left

    # KPA_40 Maze Guide Room
    {"from": {"map": "KPA_40",  "id": 0}, "to": {"map": "KPA_52",  "id": 1}, "reqs": []}, # Maze Guide Room Door Left -> Split Level Hall Door Bottom Right
    {"from": {"map": "KPA_40",  "id": 1}, "to": {"map": "KPA_40",  "id": 3}, "reqs": []}, # Maze Guide Room Door Bottom Right -> Maze Guide Room Door Top Left
    {"from": {"map": "KPA_40",  "id": 2}, "to": {"map": "KPA_41",  "id": 3}, "reqs": []}, # Maze Guide Room Door Top Right -> Maze Room Door Top Left
    #{"from": {"map": "KPA_40",  "id": 3}, "to": {"map": None,  "id": None},  "reqs": []}, # Maze Guide Room Door Top Left

    {"from": {"map": "KPA_40",  "id": 0}, "to": {"map": "KPA_40",  "id": 1}, "reqs": []}, #? Maze Guide Room Door Left -> Maze Guide Room Door Bottom Right
    {"from": {"map": "KPA_40",  "id": 1}, "to": {"map": "KPA_40",  "id": 0}, "reqs": []}, #? Maze Guide Room Door Bottom Right -> Maze Guide Room Door Left
    {"from": {"map": "KPA_40",  "id": 0}, "to": {"map": "KPA_40",  "id": 2}, "reqs": [["can_climb_steps"]]}, #? Maze Guide Room Door Left -> Maze Guide Room Door Top Right
    {"from": {"map": "KPA_40",  "id": 2}, "to": {"map": "KPA_40",  "id": 0}, "reqs": []}, #? Maze Guide Room Door Top Right -> Maze Guide Room Door Left
    {"from": {"map": "KPA_40",  "id": 3}, "to": {"map": "KPA_40",  "id": 0}, "reqs": []}, #? Maze Guide Room Door Top Left -> Maze Guide Room Door Left

    # KPA_41 Maze Room
    {"from": {"map": "KPA_41",  "id": 0}, "to": {"map": "KPA_40",  "id": 1}, "reqs": []}, # Maze Room Door Bottom Left -> Maze Guide Room Door Bottom Right
    {"from": {"map": "KPA_41",  "id": 1}, "to": {"map": "KPA_41",  "id": 0}, "reqs": []}, # Maze Room Door Bottom Right -> Maze Room Door Bottom Left
    {"from": {"map": "KPA_41",  "id": 2}, "to": {"map": "KPA_102", "id": 0}, "reqs": []}, # Maze Room Door Top Right -> Blue Fire Bridge Door Left
    {"from": {"map": "KPA_41",  "id": 3}, "to": {"map": "KPA_40",  "id": 2}, "reqs": []}, # Maze Room Door Top Left -> Maze Guide Room Door Top Right

    {"from": {"map": "KPA_41",  "id": 0}, "to": {"map": "KPA_41",  "id": 1}, "reqs": []}, #? Maze Room Door Bottom Left -> Maze Room Door Bottom Right
    {"from": {"map": "KPA_41",  "id": 1}, "to": {"map": "KPA_41",  "id": 0}, "reqs": []}, #? Maze Room Door Bottom Right -> Maze Room Door Bottom Left
    {"from": {"map": "KPA_41",  "id": 0}, "to": {"map": "KPA_41",  "id": 2}, "reqs": [["can_climb_steps"]]}, #? Maze Room Door Bottom Left -> Maze Room Door Top Right
    {"from": {"map": "KPA_41",  "id": 2}, "to": {"map": "KPA_41",  "id": 0}, "reqs": []}, #? Maze Room Door Top Right -> Maze Room Door Bottom Left
    {"from": {"map": "KPA_41",  "id": 0}, "to": {"map": "KPA_41",  "id": 3}, "reqs": [["can_climb_steps"]]}, #? Maze Room Door Bottom Left -> Maze Room Door Top Left
    {"from": {"map": "KPA_41",  "id": 3}, "to": {"map": "KPA_41",  "id": 0}, "reqs": []}, #? Maze Room Door Top Left -> Maze Room Door Bottom Left

    # KPA_50 Hall to Guard Door 1
    {"from": {"map": "KPA_50",  "id": 0}, "to": {"map": "KPA_70",  "id": 1}, "reqs": []}, # Hall to Guard Door 1 Door Left -> Entry Lava Hall Door Right
    {"from": {"map": "KPA_50",  "id": 1}, "to": {"map": "KPA_81",  "id": 0}, "reqs": []}, # Hall to Guard Door 1 Door Right -> Guard Door 1 Door Left

    {"from": {"map": "KPA_50",  "id": 0}, "to": {"map": "KPA_50",  "id": 1}, "reqs": []}, #? Hall to Guard Door 1 Door Left -> Hall to Guard Door 1 Door Right
    {"from": {"map": "KPA_50",  "id": 1}, "to": {"map": "KPA_50",  "id": 0}, "reqs": []}, #? Hall to Guard Door 1 Door Right -> Hall to Guard Door 1 Door Left

    # KPA_51 Hall to Water Puzzle
    {"from": {"map": "KPA_51",  "id": 0}, "to": {"map": "KPA_32",  "id": 2}, "reqs": []}, # Hall to Water Puzzle Door Left -> Lower Grand Hall Door Top Right
    {"from": {"map": "KPA_51",  "id": 1}, "to": {"map": "KPA_133", "id": 0}, "reqs": []}, # Hall to Water Puzzle Door Right -> Left Water Puzzle Door Bottom Left

    {"from": {"map": "KPA_51",  "id": 0}, "to": {"map": "KPA_51",  "id": 1}, "reqs": []}, #? Hall to Water Puzzle Door Left -> Hall to Water Puzzle Door Right
    {"from": {"map": "KPA_51",  "id": 1}, "to": {"map": "KPA_51",  "id": 0}, "reqs": []}, #? Hall to Water Puzzle Door Right -> Hall to Water Puzzle Door Left

    # KPA_52 Split Level Hall
    {"from": {"map": "KPA_52",  "id": 0}, "to": {"map": "KPA_33",  "id": 2}, "reqs": []}, # Split Level Hall Door Left -> Upper Grand Hall Door Top Right
    {"from": {"map": "KPA_52",  "id": 1}, "to": {"map": "KPA_40",  "id": 0}, "reqs": [[{"BowserCastleKey": 5}]]}, # Split Level Hall Door Bottom Right -> Maze Guide Room Door Left
    {"from": {"map": "KPA_52",  "id": 2}, "to": {"map": "KPA_08",  "id": 0}, "reqs": []}, # Split Level Hall Door Top Right -> Castle Key Timing Puzzle Door Left

    {"from": {"map": "KPA_52",  "id": 0}, "to": {"map": "KPA_52",  "id": 1}, "reqs": []}, #? Split Level Hall Door Left -> Split Level Hall Door Bottom Right
    {"from": {"map": "KPA_52",  "id": 1}, "to": {"map": "KPA_52",  "id": 0}, "reqs": []}, #? Split Level Hall Door Bottom Right -> Split Level Hall Door Left
    {"from": {"map": "KPA_52",  "id": 0}, "to": {"map": "KPA_52",  "id": 2}, "reqs": [["can_climb_steps"]]}, #? Split Level Hall Door Left -> Split Level Hall Door Top Right
    {"from": {"map": "KPA_52",  "id": 2}, "to": {"map": "KPA_52",  "id": 0}, "reqs": []}, #? Split Level Hall Door Top Right -> Split Level Hall Door Left

    # KPA_53 Fake Peach Hallway
    {"from": {"map": "KPA_53",  "id": 0}, "to": {"map": "KPA_102", "id": 1}, "reqs": []}, # Fake Peach Hallway Door Left -> Blue Fire Bridge Door Right
    {"from": {"map": "KPA_53",  "id": 1}, "to": {"map": "KPA_83",  "id": 0}, "reqs": []}, # Fake Peach Hallway Door Right -> Guard Door 3 Door Left

    {"from": {"map": "KPA_53",  "id": 0}, "to": {"map": "KPA_53",  "id": 1}, "reqs": [["Boots","Hammer","Kooper","Bombette"]]}, #? Fake Peach Hallway Door Left -> Fake Peach Hallway Door Right
    {"from": {"map": "KPA_53",  "id": 1}, "to": {"map": "KPA_53",  "id": 0}, "reqs": []}, #? Fake Peach Hallway Door Right -> Fake Peach Hallway Door Left

    # KPA_60 Ship Enter/Exit Scenes
    {"from": {"map": "KPA_60",  "id": 4}, "to": {"map": "HOS_20",  "id": 2}, "reqs": []}, # Ship Enter/Exit Scenes Leave Hangar To Starhaven -> Riding Star Ship Scene Fly To Bowser's Castle
    {"from": {"map": "KPA_60",  "id": 5}, "to": {"map": "KPA_63",  "id": 1}, "reqs": []}, # Ship Enter/Exit Scenes Land Starship In Hangar -> Hangar Leave Hangar With Starship

    {"from": {"map": "KPA_60",  "id": 4}, "to": {"map": "KPA_60",  "id": 5}, "reqs": []}, #? Ship Enter/Exit Scenes Leave Hangar To Starhaven -> Ship Enter/Exit Scenes Land Starship In Hangar
    {"from": {"map": "KPA_60",  "id": 5}, "to": {"map": "KPA_60",  "id": 4}, "reqs": []}, #? Ship Enter/Exit Scenes Land Starship In Hangar -> Ship Enter/Exit Scenes Leave Hangar To Starhaven

    # KPA_61 Battlement
    {"from": {"map": "KPA_61",  "id": 0}, "to": {"map": "KPA_82",  "id": 1}, "reqs": []}, # Battlement Door Bottom Left -> Guard Door 2 Guard Door Right
    {"from": {"map": "KPA_61",  "id": 1}, "to": {"map": "KPA_33",  "id": 1}, "reqs": []}, # Battlement Door Top Left -> Upper Grand Hall Door Bottom Right

    {"from": {"map": "KPA_61",  "id": 0}, "to": {"map": "KPA_61",  "id": 1}, "reqs": [["can_climb_steps"]]}, #? Battlement Door Bottom Left -> Battlement Door Top Left
    {"from": {"map": "KPA_61",  "id": 1}, "to": {"map": "KPA_61",  "id": 0}, "reqs": []}, #? Battlement Door Top Left -> Battlement Door Bottom Left

    {"from": {"map": "KPA_61",  "id": 0},         "to": {"map": "KPA_61",  "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Battlement Door Bottom Left -> YBlockA (SuperShroom)
    {"from": {"map": "KPA_61",  "id": "YBlockA"}, "to": {"map": "KPA_61",  "id": "YBlockB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockB (MapleSyrup)
    {"from": {"map": "KPA_61",  "id": "YBlockA"}, "to": {"map": "KPA_61",  "id": "YBlockC"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockC (SuperShroom)
    {"from": {"map": "KPA_61",  "id": 1},         "to": {"map": "KPA_61",  "id": "ItemA"},   "reqs": []}, #* Battlement Door Top Left -> ItemA (JamminJelly)

    # KPA_62 Front Door Exterior
    {"from": {"map": "KPA_62",  "id": 0}, "to": {"map": "KPA_70",  "id": 0}, "reqs": [[{"BowserCastleKey": 1}]]}, # Front Door Exterior Front Door -> Entry Lava Hall Door Left
    {"from": {"map": "KPA_62",  "id": 1}, "to": {"map": "KPA_10",  "id": 0}, "reqs": []}, # Front Door Exterior Door Right -> Outside Lower Jail (No Lava) Door Top Left
    {"from": {"map": "KPA_62",  "id": 1}, "to": {"map": "KPA_11",  "id": 0}, "reqs": []}, # Front Door Exterior Door Right -> Outside Lower Jail (Lava) Door Top Left
    {"from": {"map": "KPA_62",  "id": 2}, "to": {"map": "KPA_10",  "id": 3}, "reqs": []}, # Front Door Exterior Lava Door Right -> Outside Lower Jail (No Lava) Lava Door Left
    {"from": {"map": "KPA_62",  "id": 2}, "to": {"map": "KPA_11",  "id": 3}, "reqs": []}, # Front Door Exterior Lava Door Right -> Outside Lower Jail (Lava) Lava Door Left
    {"from": {"map": "KPA_62",  "id": 3}, "to": {"map": "KPA_63",  "id": 0}, "reqs": []}, # Front Door Exterior Hangar Door Bottom Left -> Hangar Door Bottom Right

    {"from": {"map": "KPA_62",  "id": 3}, "to": {"map": "KPA_62",  "id": 1}, "reqs": []}, #? Front Door Exterior Hangar Door Bottom Left -> Front Door Exterior Door Right
    {"from": {"map": "KPA_62",  "id": 1}, "to": {"map": "KPA_62",  "id": 3}, "reqs": []}, #? Front Door Exterior Door Right -> Front Door Exterior Hangar Door Bottom Left
    {"from": {"map": "KPA_62",  "id": 0}, "to": {"map": "KPA_62",  "id": 3}, "reqs": []}, #? Front Door Exterior Front Door -> Front Door Exterior Hangar Door Bottom Left
    {"from": {"map": "KPA_62",  "id": 3}, "to": {"map": "KPA_62",  "id": 0}, "reqs": []}, #? Front Door Exterior Hangar Door Bottom Left -> Front Door Exterior Front Door

    {"from": {"map": "KPA_62",  "id": 2}, "to": {"map": "KPA_62",  "id": "RBlockA"}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"],["can_climb_steps"],["can_hit_floating_blocks"]]}, #* Front Door Exterior Lava Door Right -> RBlockA (DeepFocus3)

    # KPA_63 Hangar
    {"from": {"map": "KPA_63",  "id": 0}, "to": {"map": "KPA_62",  "id": 3}, "reqs": []}, # Hangar Door Bottom Right -> Front Door Exterior Hangar Door Bottom Left
    {"from": {"map": "KPA_63",  "id": 1}, "to": {"map": "KPA_60",  "id": 5}, "reqs": []}, # Hangar Leave Hangar With Starship -> Ship Enter/Exit Scenes Land Starship In Hangar

    {"from": {"map": "KPA_63",  "id": 0}, "to": {"map": "KPA_63",  "id": 1}, "reqs": []}, #? Hangar Door Bottom Right -> Hangar Leave Hangar With Starship
    {"from": {"map": "KPA_63",  "id": 1}, "to": {"map": "KPA_63",  "id": 0}, "reqs": []}, #? Hangar Leave Hangar With Starship -> Hangar Door Bottom Right

    # KPA_70 Entry Lava Hall
    {"from": {"map": "KPA_70",  "id": 0}, "to": {"map": "KPA_62",  "id": 0}, "reqs": []}, # Entry Lava Hall Door Left -> Front Door Exterior Front Door
    {"from": {"map": "KPA_70",  "id": 1}, "to": {"map": "KPA_50",  "id": 0}, "reqs": []}, # Entry Lava Hall Door Right -> Hall to Guard Door 1 Door Left

    {"from": {"map": "KPA_70",  "id": 0}, "to": {"map": "KPA_70",  "id": 1}, "reqs": []}, #? Entry Lava Hall Door Left -> Entry Lava Hall Door Right
    {"from": {"map": "KPA_70",  "id": 1}, "to": {"map": "KPA_70",  "id": 0}, "reqs": []}, #? Entry Lava Hall Door Right -> Entry Lava Hall Door Left

    # KPA_81 Guard Door 1
    {"from": {"map": "KPA_81",  "id": 0}, "to": {"map": "KPA_50",  "id": 1}, "reqs": []}, # Guard Door 1 Door Left -> Hall to Guard Door 1 Door Right
    {"from": {"map": "KPA_81",  "id": 1}, "to": {"map": "KPA_17",  "id": 0}, "reqs": []}, # Guard Door 1 Fall In Trap Door -> Lower Jail Fall From Ceiling
    {"from": {"map": "KPA_81",  "id": 2}, "to": {"map": "KPA_32",  "id": 0}, "reqs": []}, # Guard Door 1 Guard Door Right -> Lower Grand Hall Door Bottom Left
    {"from": {"map": "KPA_81",  "id": 3}, "to": {"map": "KPA_04",  "id": 1}, "reqs": []}, # Guard Door 1 Hidden Door Top -> Cave Exit Hidden Door Bottom

    {"from": {"map": "KPA_81",  "id": 0}, "to": {"map": "KPA_81",  "id": 1}, "reqs": [["Bombette"], ["Lakilester"], ["Parakarry"], ["Bow"]]}, #? Guard Door 1 Door Left -> Guard Door 1 Fall In Trap Door
    {"from": {"map": "KPA_81",  "id": 1}, "to": {"map": "KPA_81",  "id": 0}, "reqs": []}, #? Guard Door 1 Fall In Trap Door -> Guard Door 1 Door Left
    {"from": {"map": "KPA_81",  "id": 0}, "to": {"map": "KPA_81",  "id": 2}, "reqs": [["RF_Ch8_FirstGuardDoor"]]}, #? Guard Door 1 Door Left -> Guard Door 1 Guard Door Right
    {"from": {"map": "KPA_81",  "id": 2}, "to": {"map": "KPA_81",  "id": 0}, "reqs": []}, #? Guard Door 1 Guard Door Right -> Guard Door 1 Door Left
    {"from": {"map": "KPA_81",  "id": 0}, "to": {"map": "KPA_81",  "id": 3}, "reqs": [["RF_Ch8_FirstGuardDoor"]]}, #? Guard Door 1 Door Left -> Guard Door 1 Hidden Door Top
    {"from": {"map": "KPA_81",  "id": 3}, "to": {"map": "KPA_81",  "id": 0}, "reqs": [], "pseudoitems": ["RF_Ch8_FirstGuardDoor"]}, #? Guard Door 1 Hidden Door Top -> Guard Door 1 Door Left

    # KPA_82 Guard Door 2
    {"from": {"map": "KPA_82",  "id": 0}, "to": {"map": "KPA_113", "id": 1}, "reqs": []}, # Guard Door 2 Door Left -> Room with Hidden Door 2 Door Right
    {"from": {"map": "KPA_82",  "id": 1}, "to": {"map": "KPA_61",  "id": 0}, "reqs": []}, # Guard Door 2 Guard Door Right -> Battlement Door Bottom Left

    {"from": {"map": "KPA_82",  "id": 0}, "to": {"map": "KPA_82",  "id": 1}, "reqs": []}, #? Guard Door 2 Door Left -> Guard Door 2 Guard Door Right
    {"from": {"map": "KPA_82",  "id": 1}, "to": {"map": "KPA_82",  "id": 0}, "reqs": []}, #? Guard Door 2 Guard Door Right -> Guard Door 2 Door Left

    # KPA_83 Guard Door 3
    {"from": {"map": "KPA_83",  "id": 0}, "to": {"map": "KPA_53",  "id": 1}, "reqs": []}, # Guard Door 3 Door Left -> Fake Peach Hallway Door Right
    {"from": {"map": "KPA_83",  "id": 1}, "to": {"map": "KPA_121", "id": 0}, "reqs": []}, # Guard Door 3 Guard Door Right -> Exit to Peach's Castle Door Bottom Left

    {"from": {"map": "KPA_83",  "id": 0}, "to": {"map": "KPA_83",  "id": 1}, "reqs": []}, #? Guard Door 3 Door Left -> Guard Door 3 Guard Door Right
    {"from": {"map": "KPA_83",  "id": 1}, "to": {"map": "KPA_83",  "id": 0}, "reqs": []}, #? Guard Door 3 Guard Door Right -> Guard Door 3 Door Left

    # KPA_90 Stairs to East Upper Jail
    {"from": {"map": "KPA_90",  "id": 0}, "to": {"map": "KPA_32",  "id": 1}, "reqs": []}, # Stairs to East Upper Jail Door Top Left -> Lower Grand Hall Door Bottom Right
    {"from": {"map": "KPA_90",  "id": 1}, "to": {"map": "KPA_91",  "id": 0}, "reqs": []}, # Stairs to East Upper Jail Door Bottom Right To Jail -> East Upper Jail Door Left

    {"from": {"map": "KPA_90",  "id": 0}, "to": {"map": "KPA_90",  "id": 1}, "reqs": []}, #? Stairs to East Upper Jail Door Top Left -> Stairs to East Upper Jail Door Bottom Right To Jail
    {"from": {"map": "KPA_90",  "id": 1}, "to": {"map": "KPA_90",  "id": 0}, "reqs": []}, #? Stairs to East Upper Jail Door Bottom Right To Jail -> Stairs to East Upper Jail Door Top Left

    # KPA_91 East Upper Jail
    {"from": {"map": "KPA_91",  "id": 0}, "to": {"map": "KPA_90",  "id": 1}, "reqs": []}, # East Upper Jail Door Left -> Stairs to East Upper Jail Door Bottom Right To Jail

    {"from": {"map": "KPA_91",  "id": 0}, "to": {"map": "KPA_91",  "id": "ItemA"}, "reqs": []}, #* East Upper Jail Door Left -> ItemA (PrisonKey1)

    # KPA_94 Stairs to West Upper Jail
    {"from": {"map": "KPA_94",  "id": 0}, "to": {"map": "KPA_95",  "id": 0}, "reqs": []}, # Stairs to West Upper Jail Door Bottom Left To Jail -> West Upper Jail Door Right
    {"from": {"map": "KPA_94",  "id": 1}, "to": {"map": "KPA_33",  "id": 0}, "reqs": []}, # Stairs to West Upper Jail Door Top Right -> Upper Grand Hall Door Bottom Left

    {"from": {"map": "KPA_94",  "id": 0}, "to": {"map": "KPA_94",  "id": 1}, "reqs": []}, #? Stairs to West Upper Jail Door Bottom Left To Jail -> Stairs to West Upper Jail Door Top Right
    {"from": {"map": "KPA_94",  "id": 1}, "to": {"map": "KPA_94",  "id": 0}, "reqs": []}, #? Stairs to West Upper Jail Door Top Right -> Stairs to West Upper Jail Door Bottom Left To Jail

    # KPA_95 West Upper Jail
    {"from": {"map": "KPA_95",  "id": 0}, "to": {"map": "KPA_94",  "id": 0}, "reqs": []}, # West Upper Jail Door Right -> Stairs to West Upper Jail Door Bottom Left To Jail

    {"from": {"map": "KPA_95",  "id": 0}, "to": {"map": "KPA_95",  "id": "ItemA"}, "reqs": []}, #* West Upper Jail Door Right -> ItemA (PrisonKey1)

    # KPA_96 Item Shop
    {"from": {"map": "KPA_96",  "id": 0}, "to": {"map": "KPA_32",  "id": 3}, "reqs": []}, # Item Shop Door Right -> Lower Grand Hall Door Top Left

    {"from": {"map": "KPA_96",  "id": 0}, "to": {"map": "KPA_96",  "id": "ShopItemA"}, "reqs": []}, #* Item Shop Door Right -> ShopItemA (Mystery)
    {"from": {"map": "KPA_96",  "id": 0}, "to": {"map": "KPA_96",  "id": "ShopItemB"}, "reqs": []}, #* Item Shop Door Right -> ShopItemB (DizzyDial)
    {"from": {"map": "KPA_96",  "id": 0}, "to": {"map": "KPA_96",  "id": "ShopItemC"}, "reqs": []}, #* Item Shop Door Right -> ShopItemC (POWBlock)
    {"from": {"map": "KPA_96",  "id": 0}, "to": {"map": "KPA_96",  "id": "ShopItemD"}, "reqs": []}, #* Item Shop Door Right -> ShopItemD (ThunderRage)
    {"from": {"map": "KPA_96",  "id": 0}, "to": {"map": "KPA_96",  "id": "ShopItemE"}, "reqs": []}, #* Item Shop Door Right -> ShopItemE (MapleSyrup)
    {"from": {"map": "KPA_96",  "id": 0}, "to": {"map": "KPA_96",  "id": "ShopItemF"}, "reqs": []}, #* Item Shop Door Right -> ShopItemF (SuperShroom)

    # KPA_100 Castle Key Room
    {"from": {"map": "KPA_100", "id": 0}, "to": {"map": "KPA_08",  "id": 1}, "reqs": []}, # Castle Key Room Door Left -> Castle Key Timing Puzzle Door Right

    {"from": {"map": "KPA_100", "id": 0}, "to": {"map": "KPA_100", "id": "ItemA"}, "reqs": []}, #* Castle Key Room Door Left -> ItemA (BowserCastleKey)

    # KPA_101 Ultra Shroom Room
    {"from": {"map": "KPA_101", "id": 0}, "to": {"map": "KPA_09",  "id": 0}, "reqs": []}, # Ultra Shroom Room Door Right -> Ultra Shroom Timing Puzzle Door Left

    {"from": {"map": "KPA_101", "id": 0}, "to": {"map": "KPA_101", "id": "ItemA"}, "reqs": [["can_climb_steps"]]}, #* Ultra Shroom Room Door Right -> ItemA (UltraShroom)

    # KPA_102 Blue Fire Bridge
    {"from": {"map": "KPA_102", "id": 0}, "to": {"map": "KPA_41",  "id": 2}, "reqs": []}, # Blue Fire Bridge Door Left -> Maze Room Door Top Right
    {"from": {"map": "KPA_102", "id": 1}, "to": {"map": "KPA_53",  "id": 0}, "reqs": []}, # Blue Fire Bridge Door Right -> Fake Peach Hallway Door Left

    {"from": {"map": "KPA_102", "id": 0}, "to": {"map": "KPA_102", "id": 1}, "reqs": []}, #? Blue Fire Bridge Door Left -> Blue Fire Bridge Door Right
    {"from": {"map": "KPA_102", "id": 1}, "to": {"map": "KPA_102", "id": 0}, "reqs": []}, #? Blue Fire Bridge Door Right -> Blue Fire Bridge Door Left

    # KPA_111 Room with Hidden Door 1
    {"from": {"map": "KPA_111", "id": 0}, "to": {"map": "KPA_130", "id": 1}, "reqs": []}, # Room with Hidden Door 1 Door Left -> Bill Blaster Hall Door Top Right
    {"from": {"map": "KPA_111", "id": 1}, "to": {"map": "KPA_112", "id": 0}, "reqs": []}, # Room with Hidden Door 1 Hidden Door -> Hidden Passage 1 Hidden Door Bottom Left

    {"from": {"map": "KPA_111", "id": 0}, "to": {"map": "KPA_111", "id": 1}, "reqs": []}, #? Room with Hidden Door 1 Door Left -> Room with Hidden Door 1 Hidden Door
    {"from": {"map": "KPA_111", "id": 1}, "to": {"map": "KPA_111", "id": 0}, "reqs": []}, #? Room with Hidden Door 1 Hidden Door -> Room with Hidden Door 1 Door Left

    {"from": {"map": "KPA_111", "id": 0},         "to": {"map": "KPA_111", "id": "YBlockA"},       "reqs": [["can_hit_floating_blocks"]]}, #* Room with Hidden Door 1 Door Left -> YBlockA (SuperShroom)
    {"from": {"map": "KPA_111", "id": "YBlockA"}, "to": {"map": "KPA_111", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"]]}, #+ CHAINED REQUIREMENTS -> HiddenYBlockA (MapleSyrup)

    # KPA_112 Hidden Passage 1
    {"from": {"map": "KPA_112", "id": 0}, "to": {"map": "KPA_111", "id": 1}, "reqs": []}, # Hidden Passage 1 Hidden Door Bottom Left -> Room with Hidden Door 1 Hidden Door
    {"from": {"map": "KPA_112", "id": 1}, "to": {"map": "KPA_113", "id": 0}, "reqs": []}, # Hidden Passage 1 Door Right -> Room with Hidden Door 2 Door Left

    {"from": {"map": "KPA_112", "id": 0}, "to": {"map": "KPA_112", "id": 1}, "reqs": []}, #? Hidden Passage 1 Hidden Door Bottom Left -> Hidden Passage 1 Door Right
    {"from": {"map": "KPA_112", "id": 1}, "to": {"map": "KPA_112", "id": 0}, "reqs": []}, #? Hidden Passage 1 Door Right -> Hidden Passage 1 Hidden Door Bottom Left

    # KPA_113 Room with Hidden Door 2
    {"from": {"map": "KPA_113", "id": 0}, "to": {"map": "KPA_112", "id": 1}, "reqs": []}, # Room with Hidden Door 2 Door Left -> Hidden Passage 1 Door Right
    {"from": {"map": "KPA_113", "id": 1}, "to": {"map": "KPA_82",  "id": 0}, "reqs": [[{"BowserCastleKey": 4}]]}, # Room with Hidden Door 2 Door Right -> Guard Door 2 Door Left
    {"from": {"map": "KPA_113", "id": 2}, "to": {"map": "KPA_114", "id": 0}, "reqs": []}, # Room with Hidden Door 2 Hidden Door -> Hidden Passage 2 Hidden Door Bottom Left

    {"from": {"map": "KPA_113", "id": 0}, "to": {"map": "KPA_113", "id": 1}, "reqs": []}, #? Room with Hidden Door 2 Door Left -> Room with Hidden Door 2 Door Right
    {"from": {"map": "KPA_113", "id": 1}, "to": {"map": "KPA_113", "id": 0}, "reqs": []}, #? Room with Hidden Door 2 Door Right -> Room with Hidden Door 2 Door Left
    {"from": {"map": "KPA_113", "id": 0}, "to": {"map": "KPA_113", "id": 2}, "reqs": []}, #? Room with Hidden Door 2 Door Left -> Room with Hidden Door 2 Hidden Door
    {"from": {"map": "KPA_113", "id": 2}, "to": {"map": "KPA_113", "id": 0}, "reqs": []}, #? Room with Hidden Door 2 Hidden Door -> Room with Hidden Door 2 Door Left

    # KPA_114 Hidden Passage 2
    {"from": {"map": "KPA_114", "id": 0}, "to": {"map": "KPA_113", "id": 2}, "reqs": []}, # Hidden Passage 2 Hidden Door Bottom Left -> Room with Hidden Door 2 Hidden Door
    {"from": {"map": "KPA_114", "id": 1}, "to": {"map": "KPA_115", "id": 0}, "reqs": []}, # Hidden Passage 2 Door Right -> Room with Hidden Door 3 Door Left
    #
    {"from": {"map": "KPA_114", "id": 0}, "to": {"map": "KPA_114", "id": 1}, "reqs": []}, #? Hidden Passage 2 Hidden Door Bottom Left -> Hidden Passage 2 Door Right
    {"from": {"map": "KPA_114", "id": 1}, "to": {"map": "KPA_114", "id": 0}, "reqs": []}, #? Hidden Passage 2 Door Right -> Hidden Passage 2 Hidden Door Bottom Left

    # KPA_115 Room with Hidden Door 3
    {"from": {"map": "KPA_115", "id": 0}, "to": {"map": "KPA_114", "id": 1}, "reqs": []}, # Room with Hidden Door 3 Door Left -> Hidden Passage 2 Door Right
    {"from": {"map": "KPA_115", "id": 1}, "to": {"map": "KPA_116", "id": 0}, "reqs": []}, # Room with Hidden Door 3 Fake Hidden Door -> Dead End Passage Hidden Door Bottom Left
    {"from": {"map": "KPA_115", "id": 2}, "to": {"map": "KPA_118", "id": 0}, "reqs": []}, # Room with Hidden Door 3 Actual Hidden Door -> Hidden Passage 3 Hidden Door Bottom Right

    {"from": {"map": "KPA_115", "id": 0}, "to": {"map": "KPA_115", "id": 1}, "reqs": []}, #? Room with Hidden Door 3 Door Left -> Room with Hidden Door 3 Fake Hidden Door
    {"from": {"map": "KPA_115", "id": 1}, "to": {"map": "KPA_115", "id": 0}, "reqs": []}, #? Room with Hidden Door 3 Fake Hidden Door -> Room with Hidden Door 3 Door Left
    {"from": {"map": "KPA_115", "id": 0}, "to": {"map": "KPA_115", "id": 2}, "reqs": []}, #? Room with Hidden Door 3 Door Left -> Room with Hidden Door 3 Actual Hidden Door
    {"from": {"map": "KPA_115", "id": 2}, "to": {"map": "KPA_115", "id": 0}, "reqs": []}, #? Room with Hidden Door 3 Actual Hidden Door -> Room with Hidden Door 3 Door Left

    # KPA_116 Dead End Passage
    {"from": {"map": "KPA_116", "id": 0}, "to": {"map": "KPA_115", "id": 1}, "reqs": []}, # Dead End Passage Hidden Door Bottom Left -> Room with Hidden Door 3 Fake Hidden Door
    {"from": {"map": "KPA_116", "id": 1}, "to": {"map": "KPA_117", "id": 0}, "reqs": []}, # Dead End Passage Door Right -> Dead End Room Door Left

    {"from": {"map": "KPA_116", "id": 0}, "to": {"map": "KPA_116", "id": 1}, "reqs": []}, #? Dead End Passage Hidden Door Bottom Left -> Dead End Passage Door Right
    {"from": {"map": "KPA_116", "id": 1}, "to": {"map": "KPA_116", "id": 0}, "reqs": []}, #? Dead End Passage Door Right -> Dead End Passage Hidden Door Bottom Left

    # KPA_117 Dead End Room
    {"from": {"map": "KPA_117", "id": 0}, "to": {"map": "KPA_116", "id": 1}, "reqs": []}, # Dead End Room Door Left -> Dead End Passage Door Right

    # KPA_118 Hidden Passage 3
    {"from": {"map": "KPA_118", "id": 0}, "to": {"map": "KPA_115", "id": 2}, "reqs": []}, # Hidden Passage 3 Hidden Door Bottom Right -> Room with Hidden Door 3 Actual Hidden Door
    {"from": {"map": "KPA_118", "id": 1}, "to": {"map": "KPA_119", "id": 0}, "reqs": []}, # Hidden Passage 3 Door Left -> Hidden Key Room Door Right

    {"from": {"map": "KPA_118", "id": 0}, "to": {"map": "KPA_118", "id": 1}, "reqs": []}, #? Hidden Passage 3 Hidden Door Bottom Right -> Hidden Passage 3 Door Left
    {"from": {"map": "KPA_118", "id": 1}, "to": {"map": "KPA_118", "id": 0}, "reqs": []}, #? Hidden Passage 3 Door Left -> Hidden Passage 3 Hidden Door Bottom Right

    # KPA_119 Hidden Key Room
    {"from": {"map": "KPA_119", "id": 0}, "to": {"map": "KPA_118", "id": 1}, "reqs": []}, # Hidden Key Room Door Right -> Hidden Passage 3 Door Left

    {"from": {"map": "KPA_119", "id": 0}, "to": {"map": "KPA_119", "id": "ItemA"}, "reqs": [["can_climb_steps"]]}, #* Hidden Key Room Door Right -> ItemA (BowserCastleKey)

    # KPA_121 Exit to Peach's Castle
    {"from": {"map": "KPA_121", "id": 0}, "to": {"map": "KPA_83",  "id": 1}, "reqs": []}, # Exit to Peach's Castle Door Bottom Left -> Guard Door 3 Guard Door Right
    {"from": {"map": "KPA_121", "id": 1}, "to": {"map": "OSR_02",  "id": 0}, "reqs": []}, # Exit to Peach's Castle Door Top Right -> Hijacked Castle Entrance Door West

    {"from": {"map": "KPA_121", "id": 0}, "to": {"map": "KPA_121", "id": 1}, "reqs": []}, #? Exit to Peach's Castle Door Bottom Left -> Exit to Peach's Castle Door Top Right
    {"from": {"map": "KPA_121", "id": 1}, "to": {"map": "KPA_121", "id": 0}, "reqs": []}, #? Exit to Peach's Castle Door Top Right -> Exit to Peach's Castle Door Bottom Left

    # KPA_130 Bill Blaster Hall
    {"from": {"map": "KPA_130", "id": 0}, "to": {"map": "KPA_134", "id": 1}, "reqs": []}, # Bill Blaster Hall Door Left -> Right Water Puzzle Door Bottom Right
    {"from": {"map": "KPA_130", "id": 1}, "to": {"map": "KPA_111", "id": 0}, "reqs": []}, # Bill Blaster Hall Door Top Right -> Room with Hidden Door 1 Door Left

    {"from": {"map": "KPA_130", "id": 0}, "to": {"map": "KPA_130", "id": 1}, "reqs": [["Boots"]]}, #? Bill Blaster Hall Door Left -> Bill Blaster Hall Door Top Right
    {"from": {"map": "KPA_130", "id": 1}, "to": {"map": "KPA_130", "id": 0}, "reqs": []}, #? Bill Blaster Hall Door Top Right -> Bill Blaster Hall Door Left

    # KPA_133 Left Water Puzzle
    {"from": {"map": "KPA_133", "id": 0}, "to": {"map": "KPA_51",  "id": 1}, "reqs": []}, # Left Water Puzzle Door Bottom Left -> Hall to Water Puzzle Door Right
    {"from": {"map": "KPA_133", "id": 1}, "to": {"map": "KPA_134", "id": 0}, "reqs": []}, # Left Water Puzzle Door Bottom Right -> Right Water Puzzle Door Bottom Left
    {"from": {"map": "KPA_133", "id": 2}, "to": {"map": "KPA_134", "id": 2}, "reqs": []}, # Left Water Puzzle Door Bottom Right Upper Half -> Right Water Puzzle Door Bottom Left Upper Half
    {"from": {"map": "KPA_133", "id": 3}, "to": {"map": "KPA_134", "id": 3}, "reqs": []}, # Left Water Puzzle Door Bombable Wall -> Right Water Puzzle Bombable Wall

    {"from": {"map": "KPA_133", "id": 0}, "to": {"map": "KPA_133", "id": 1}, "reqs": []}, #? Left Water Puzzle Door Bottom Left -> Left Water Puzzle Door Bottom Right
    {"from": {"map": "KPA_133", "id": 1}, "to": {"map": "KPA_133", "id": 0}, "reqs": []}, #? Left Water Puzzle Door Bottom Right -> Left Water Puzzle Door Bottom Left
    {"from": {"map": "KPA_133", "id": 2}, "to": {"map": "KPA_133", "id": 3}, "reqs": [["Sushie"],["Bombette"],["can_climb_steps"]]}, #? Left Water Puzzle Door Bottom Right Upper Half -> Left Water Puzzle Door Bombable Wall
    {"from": {"map": "KPA_133", "id": 3}, "to": {"map": "KPA_133", "id": 2}, "reqs": []}, #? Left Water Puzzle Door Bombable Wall -> Left Water Puzzle Door Bottom Right Upper Half
    {"from": {"map": "KPA_133", "id": 2}, "to": {"map": "KPA_133", "id": 1}, "reqs": []}, #? Left Water Puzzle Door Bottom Right Upper Half -> Left Water Puzzle Door Bottom Right
    {"from": {"map": "KPA_133", "id": 3}, "to": {"map": "KPA_133", "id": 1}, "reqs": []}, #? Left Water Puzzle Door Bombable Wall -> Left Water Puzzle Door Bottom Right

    {"from": {"map": "KPA_133", "id": 3}, "to": {"map": "KPA_133", "id": "ItemA"}, "reqs": [["Sushie"],["RF_WaterLevel2"]]}, #* Left Water Puzzle Door Bombable Wall -> ItemA (BowserCastleKey)

    # KPA_134 Right Water Puzzle
    {"from": {"map": "KPA_134", "id": 0}, "to": {"map": "KPA_133", "id": 1}, "reqs": []}, # Right Water Puzzle Door Bottom Left -> Left Water Puzzle Door Bottom Right
    {"from": {"map": "KPA_134", "id": 1}, "to": {"map": "KPA_130", "id": 0}, "reqs": [[{"BowserCastleKey": 3}]]}, # Right Water Puzzle Door Bottom Right -> Bill Blaster Hall Door Left
    {"from": {"map": "KPA_134", "id": 2}, "to": {"map": "KPA_133", "id": 2}, "reqs": []}, # Right Water Puzzle Door Bottom Left Upper Half -> Left Water Puzzle Door Bottom Right Upper Half
    {"from": {"map": "KPA_134", "id": 3}, "to": {"map": "KPA_133", "id": 3}, "reqs": []}, # Right Water Puzzle Bombable Wall -> Left Water Puzzle Door Bombable Wall

    {"from": {"map": "KPA_134", "id": 0}, "to": {"map": "KPA_134", "id": 1}, "reqs": []}, #? Right Water Puzzle Door Bottom Left -> Right Water Puzzle Door Bottom Right
    {"from": {"map": "KPA_134", "id": 1}, "to": {"map": "KPA_134", "id": 0}, "reqs": []}, #? Right Water Puzzle Door Bottom Right -> Right Water Puzzle Door Bottom Left
    {"from": {"map": "KPA_134", "id": 0}, "to": {"map": "KPA_134", "id": 2}, "reqs": [["Sushie"],["can_climb_steps"],["can_hit_floating_blocks"]]}, #? Right Water Puzzle Door Bottom Left -> Right Water Puzzle Door Bottom Left Upper Half
    {"from": {"map": "KPA_134", "id": 2}, "to": {"map": "KPA_134", "id": 0}, "reqs": [["Sushie"],["can_hit_floating_blocks"]]}, #? Right Water Puzzle Door Bottom Left Upper Half -> Right Water Puzzle Door Bottom Left

    {"from": {"map": "KPA_134", "id": 3}, "to": {"map": "KPA_134", "id": "HiddenYBlockA"}, "reqs": [["can_see_hidden_blocks"],["UltraBoots"]], "pseudoitems": ["RF_WaterLevel2"]}, #* Right Water Puzzle Bombable Wall -> HiddenYBlockA (MapleSyrup)
]
