"""This file represents all edges of the world graph that have origin-nodes in the DGB (Tubba Blubba's Castle) area."""
edges_dgb = [
    # DGB_00 Escape Scene
    {"from": {"map": "DGB_00", "id": 0}, "to": {"map": "ARN_04", "id": 1}, "reqs": []}, # Escape Scene Exit Left -> Wasteland Ascent 2 Exit East
    {"from": {"map": "DGB_00", "id": 1}, "to": {"map": "DGB_01", "id": 0}, "reqs": []}, # Escape Scene Door Right -> Great Hall Door 1F Bottom

    {"from": {"map": "DGB_00", "id": 0}, "to": {"map": "DGB_00", "id": 1}, "reqs": []}, #? Escape Scene Exit Left -> Escape Scene Door Right
    {"from": {"map": "DGB_00", "id": 1}, "to": {"map": "DGB_00", "id": 0}, "reqs": []}, #? Escape Scene Door Right -> Escape Scene Exit Left

    # DGB_01 Great Hall
    {"from": {"map": "DGB_01", "id": 0}, "to": {"map": "DGB_00", "id": 1}, "reqs": []}, # Great Hall Door 1F Bottom -> Escape Scene Door Right
    {"from": {"map": "DGB_01", "id": 1}, "to": {"map": "DGB_02", "id": 1}, "reqs": []}, # Great Hall Door Door 1F Left -> West Hall (1F) Door Far Right
    {"from": {"map": "DGB_01", "id": 2}, "to": {"map": "DGB_08", "id": 0}, "reqs": [[{"TubbaCastleKey": 1}]]}, # Great Hall Door Door 1F Right -> East Hall (1/2F) Door 1F Left
    {"from": {"map": "DGB_01", "id": 3}, "to": {"map": "DGB_09", "id": 1}, "reqs": []}, # Great Hall Door Door 2F Left -> West Hall (2F) Door Far Right
    {"from": {"map": "DGB_01", "id": 4}, "to": {"map": "DGB_08", "id": 1}, "reqs": []}, # Great Hall Door Door 2F Right -> East Hall (1/2F) Door 2F Left
    {"from": {"map": "DGB_01", "id": 5}, "to": {"map": "DGB_17", "id": 1}, "reqs": []}, # Great Hall Door Door 3F Left -> Save Room (3F) Door Right
    {"from": {"map": "DGB_01", "id": 6}, "to": {"map": "DGB_18", "id": 0}, "reqs": []}, # Great Hall Door Door 3F Right -> Master Bedroom (3F) Door Left

    {"from": {"map": "DGB_01", "id": 0}, "to": {"map": "DGB_01", "id": 1}, "reqs": [["Bow"]]}, #? Great Hall Door 1F Bottom -> Great Hall Door Door 1F Left
    {"from": {"map": "DGB_01", "id": 1}, "to": {"map": "DGB_01", "id": 0}, "reqs": []}, #? Great Hall Door Door 1F Left -> Great Hall Door 1F Bottom
    {"from": {"map": "DGB_01", "id": 0}, "to": {"map": "DGB_01", "id": 2}, "reqs": [["Bow"]]}, #? Great Hall Door 1F Bottom -> Great Hall Door Door 1F Right

    {"from": {"map": "DGB_01", "id": 2}, "to": {"map": "DGB_01", "id": 0}, "reqs": []}, #? Great Hall Door Door 1F Right -> Great Hall Door 1F Bottom
    {"from": {"map": "DGB_01", "id": 3}, "to": {"map": "DGB_01", "id": 4}, "reqs": []}, #? Great Hall Door Door 2F Left -> Great Hall Door Door 2F Right
    {"from": {"map": "DGB_01", "id": 4}, "to": {"map": "DGB_01", "id": 3}, "reqs": []}, #? Great Hall Door Door 2F Right -> Great Hall Door Door 2F Left
    {"from": {"map": "DGB_01", "id": 5}, "to": {"map": "DGB_01", "id": 6}, "reqs": []}, #? Great Hall Door Door 3F Left -> Great Hall Door Door 3F Right
    {"from": {"map": "DGB_01", "id": 6}, "to": {"map": "DGB_01", "id": 5}, "reqs": []}, #? Great Hall Door Door 3F Right -> Great Hall Door Door 3F Left

    # DGB_02 West Hall (1F)
    {"from": {"map": "DGB_02", "id": 0}, "to": {"map": "DGB_03", "id": 1}, "reqs": []}, # West Hall (1F) Door Far Left -> Table/Clock Room (1/2F) Door 1F Right
    {"from": {"map": "DGB_02", "id": 1}, "to": {"map": "DGB_01", "id": 1}, "reqs": []}, # West Hall (1F) Door Far Right -> Great Hall Door Door 1F Left
    {"from": {"map": "DGB_02", "id": 2}, "to": {"map": "DGB_07", "id": 0}, "reqs": []}, # West Hall (1F) Door Top Left -> Study (1F) Door Bottom
    {"from": {"map": "DGB_02", "id": 3}, "to": {"map": "DGB_11", "id": 0}, "reqs": []}, # West Hall (1F) Door Top Right -> Covered Tables Room (1F) Door Bottom

    {"from": {"map": "DGB_02", "id": 0}, "to": {"map": "DGB_02", "id": 1}, "reqs": []}, #? West Hall (1F) Door Far Left -> West Hall (1F) Door Far Right
    {"from": {"map": "DGB_02", "id": 1}, "to": {"map": "DGB_02", "id": 0}, "reqs": []}, #? West Hall (1F) Door Far Right -> West Hall (1F) Door Far Left
    {"from": {"map": "DGB_02", "id": 0}, "to": {"map": "DGB_02", "id": 2}, "reqs": []}, #? West Hall (1F) Door Far Left -> West Hall (1F) Door Top Left
    {"from": {"map": "DGB_02", "id": 2}, "to": {"map": "DGB_02", "id": 0}, "reqs": []}, #? West Hall (1F) Door Top Left -> West Hall (1F) Door Far Left
    {"from": {"map": "DGB_02", "id": 0}, "to": {"map": "DGB_02", "id": 3}, "reqs": []}, #? West Hall (1F) Door Far Left -> West Hall (1F) Door Top Right
    {"from": {"map": "DGB_02", "id": 3}, "to": {"map": "DGB_02", "id": 0}, "reqs": []}, #? West Hall (1F) Door Top Right -> West Hall (1F) Door Far Left

    # DGB_03 Table/Clock Room (1/2F)
    {"from": {"map": "DGB_03", "id": 0}, "to": {"map": "DGB_04", "id": 0}, "reqs": []}, # Table/Clock Room (1/2F) Door 1F Far Left -> Stairs to Basement Door Top Right
    {"from": {"map": "DGB_03", "id": 1}, "to": {"map": "DGB_02", "id": 0}, "reqs": []}, # Table/Clock Room (1/2F) Door 1F Right -> West Hall (1F) Door Far Left
    {"from": {"map": "DGB_03", "id": 2}, "to": {"map": "DGB_05", "id": 0}, "reqs": []}, # Table/Clock Room (1/2F) Door 1F Top Left -> Stairs Above Basement Door Top
    {"from": {"map": "DGB_03", "id": 3}, "to": {"map": "DGB_14", "id": 0}, "reqs": [[{"TubbaCastleKey": 2}]]}, # Table/Clock Room (1/2F) Door 2F Far Left -> Stairs to Third Floor Door Bottom Right
    {"from": {"map": "DGB_03", "id": 4}, "to": {"map": "DGB_09", "id": 0}, "reqs": []}, # Table/Clock Room (1/2F) Door 2F Far Right -> West Hall (2F) Door Far Left
    {"from": {"map": "DGB_03", "id": 5}, "to": {"map": "DGB_13", "id": 0}, "reqs": []}, # Table/Clock Room (1/2F) 2F Behind The Clock -> Hidden Bedroom (2F) Door Bottom

    {"from": {"map": "DGB_03", "id": 0}, "to": {"map": "DGB_03", "id": 1}, "reqs": []}, #? Table/Clock Room (1/2F) Door 1F Far Left -> Table/Clock Room (1/2F) Door 1F Right
    {"from": {"map": "DGB_03", "id": 1}, "to": {"map": "DGB_03", "id": 0}, "reqs": []}, #? Table/Clock Room (1/2F) Door 1F Right -> Table/Clock Room (1/2F) Door 1F Far Left
    {"from": {"map": "DGB_03", "id": 0}, "to": {"map": "DGB_03", "id": 2}, "reqs": []}, #? Table/Clock Room (1/2F) Door 1F Far Left -> Table/Clock Room (1/2F) Door 1F Top Left
    {"from": {"map": "DGB_03", "id": 2}, "to": {"map": "DGB_03", "id": 0}, "reqs": []}, #? Table/Clock Room (1/2F) Door 1F Top Left -> Table/Clock Room (1/2F) Door 1F Far Left
    {"from": {"map": "DGB_03", "id": 3}, "to": {"map": "DGB_03", "id": 4}, "reqs": []}, #? Table/Clock Room (1/2F) Door 2F Far Left -> Table/Clock Room (1/2F) Door 2F Far Right
    {"from": {"map": "DGB_03", "id": 4}, "to": {"map": "DGB_03", "id": 3}, "reqs": []}, #? Table/Clock Room (1/2F) Door 2F Far Right -> Table/Clock Room (1/2F) Door 2F Far Left
    {"from": {"map": "DGB_03", "id": 4}, "to": {"map": "DGB_03", "id": 5}, "reqs": []}, #? Table/Clock Room (1/2F) Door 2F Far Right -> Table/Clock Room (1/2F) 2F Behind The Clock
    {"from": {"map": "DGB_03", "id": 5}, "to": {"map": "DGB_03", "id": 4}, "reqs": []}, #? Table/Clock Room (1/2F) 2F Behind The Clock -> Table/Clock Room (1/2F) Door 2F Far Right

    {"from": {"map": "DGB_03", "id": 4},       "to": {"map": "DGB_03", "id": "ItemA"}, "reqs": []}, #* Table/Clock Room (1/2F) Door 2F Far Right -> ItemA (StarPiece)
    {"from": {"map": "DGB_03", "id": "ItemA"}, "to": {"map": "DGB_03", "id": 0},       "reqs": []}, #* ItemA (StarPiece) -> Table/Clock Room (1/2F) Door 1F Far Left

    # DGB_04 Stairs to Basement
    {"from": {"map": "DGB_04", "id": 0}, "to": {"map": "DGB_03", "id": 0}, "reqs": []}, # Stairs to Basement Door Top Right -> Table/Clock Room (1/2F) Door 1F Far Left
    {"from": {"map": "DGB_04", "id": 1}, "to": {"map": "DGB_06", "id": 0}, "reqs": []}, # Stairs to Basement Door Bottom Right -> Basement Door Bottom Left

    {"from": {"map": "DGB_04", "id": 0}, "to": {"map": "DGB_04", "id": 1}, "reqs": []}, #? Stairs to Basement Door Top Right -> Stairs to Basement Door Bottom Right
    {"from": {"map": "DGB_04", "id": 1}, "to": {"map": "DGB_04", "id": 0}, "reqs": []}, #? Stairs to Basement Door Bottom Right -> Stairs to Basement Door Top Right

    # DGB_05 Stairs Above Basement
    {"from": {"map": "DGB_05", "id": 0}, "to": {"map": "DGB_03", "id": 2}, "reqs": []}, # Stairs Above Basement Door Top -> Table/Clock Room (1/2F) Door 1F Top Left
    {"from": {"map": "DGB_05", "id": 1}, "to": {"map": "DGB_06", "id": 1}, "reqs": [["SuperBoots"]]}, # Stairs Above Basement Hole Bottom -> Basement Fall From Ceiling

    {"from": {"map": "DGB_05", "id": 0}, "to": {"map": "DGB_05", "id": 1}, "reqs": []}, #? Stairs Above Basement Door Top -> Stairs Above Basement Hole Bottom
    {"from": {"map": "DGB_05", "id": 1}, "to": {"map": "DGB_05", "id": 0}, "reqs": []}, #? Stairs Above Basement Hole Bottom -> Stairs Above Basement Door Top

    # DGB_06 Basement
    {"from": {"map": "DGB_06", "id": 0}, "to": {"map": "DGB_04", "id": 1}, "reqs": []}, # Basement Door Bottom Left -> Stairs to Basement Door Bottom Right
    #{"from": {"map": "DGB_06", "id": 1}, "to": {"map": None, "id": None}, "reqs": []},  # Basement Fall From Ceiling

    {"from": {"map": "DGB_06", "id": 1}, "to": {"map": "DGB_06", "id": 0}, "reqs": []}, #? Basement Fall From Ceiling -> Basement Door Bottom Left

    {"from": {"map": "DGB_06", "id": 1}, "to": {"map": "DGB_06", "id": "ChestA"}, "reqs": []}, #* Basement Fall From Ceiling -> ChestA (CastleKey1)

    # DGB_07 Study (1F)
    {"from": {"map": "DGB_07", "id": 0}, "to": {"map": "DGB_02", "id": 2}, "reqs": []}, # Study (1F) Door Bottom -> West Hall (1F) Door Top Left

    {"from": {"map": "DGB_07", "id": 0}, "to": {"map": "DGB_07", "id": "ItemA"}, "reqs": [["Boots"]]}, #* Study (1F) Door Bottom -> ItemA (StarPiece)

    # DGB_08 East Hall (1/2F)
    {"from": {"map": "DGB_08", "id": 0}, "to": {"map": "DGB_01", "id": 2}, "reqs": []}, # East Hall (1/2F) Door 1F Left -> Great Hall Door Door 1F Right
    {"from": {"map": "DGB_08", "id": 1}, "to": {"map": "DGB_01", "id": 4}, "reqs": []}, # East Hall (1/2F) Door 2F Left -> Great Hall Door Door 2F Right

    {"from": {"map": "DGB_08", "id": 0}, "to": {"map": "DGB_08", "id": 1}, "reqs": [["Bow"]]}, #? East Hall (1/2F) Door 1F Left -> East Hall (1/2F) Door 2F Left
    {"from": {"map": "DGB_08", "id": 1}, "to": {"map": "DGB_08", "id": 0}, "reqs": [["Bow"]]}, #? East Hall (1/2F) Door 2F Left -> East Hall (1/2F) Door 1F Left

    # DGB_09 West Hall (2F)
    {"from": {"map": "DGB_09", "id": 0}, "to": {"map": "DGB_03", "id": 4}, "reqs": []}, # West Hall (2F) Door Far Left -> Table/Clock Room (1/2F) Door 2F Far Right
    {"from": {"map": "DGB_09", "id": 1}, "to": {"map": "DGB_01", "id": 3}, "reqs": []}, # West Hall (2F) Door Far Right -> Great Hall Door Door 2F Left
    {"from": {"map": "DGB_09", "id": 2}, "to": {"map": "DGB_12", "id": 0}, "reqs": []}, # West Hall (2F) Door Top Left -> Spike Trap Room (2F) Door Bottom Left
    {"from": {"map": "DGB_09", "id": 3}, "to": {"map": "DGB_10", "id": 0}, "reqs": [["Bombette"]]}, # West Hall (2F) Cracked Wall -> Sealed Room (2F) Cracked Wall Bottom Left

    {"from": {"map": "DGB_09", "id": 0}, "to": {"map": "DGB_09", "id": 1}, "reqs": []}, #? West Hall (2F) Door Far Left -> West Hall (2F) Door Far Right
    {"from": {"map": "DGB_09", "id": 1}, "to": {"map": "DGB_09", "id": 0}, "reqs": []}, #? West Hall (2F) Door Far Right -> West Hall (2F) Door Far Left
    {"from": {"map": "DGB_09", "id": 0}, "to": {"map": "DGB_09", "id": 2}, "reqs": []}, #? West Hall (2F) Door Far Left -> West Hall (2F) Door Top Left
    {"from": {"map": "DGB_09", "id": 2}, "to": {"map": "DGB_09", "id": 0}, "reqs": []}, #? West Hall (2F) Door Top Left -> West Hall (2F) Door Far Left
    {"from": {"map": "DGB_09", "id": 0}, "to": {"map": "DGB_09", "id": 3}, "reqs": []}, #? West Hall (2F) Door Far Left -> West Hall (2F) Cracked Wall
    {"from": {"map": "DGB_09", "id": 3}, "to": {"map": "DGB_09", "id": 0}, "reqs": []}, #? West Hall (2F) Cracked Wall -> West Hall (2F) Door Far Left

    # DGB_10 Sealed Room (2F)
    {"from": {"map": "DGB_10", "id": 0}, "to": {"map": "DGB_09", "id": 3}, "reqs": []}, # Sealed Room (2F) Cracked Wall Bottom Left -> West Hall (2F) Cracked Wall
    {"from": {"map": "DGB_10", "id": 1}, "to": {"map": "DGB_11", "id": 3}, "reqs": [["SuperBoots"]]}, # Sealed Room (2F) Top Left Hole -> Covered Tables Room (1F) Spring To Ceiling
    {"from": {"map": "DGB_10", "id": 2}, "to": {"map": "DGB_11", "id": 2}, "reqs": [["SuperBoots"]]}, # Sealed Room (2F) Top Right Hole -> Covered Tables Room (1F) Top Right Ceiling Hole
    {"from": {"map": "DGB_10", "id": 3}, "to": {"map": "DGB_11", "id": 1}, "reqs": [["SuperBoots"]]}, # Sealed Room (2F) Bottom Right Hole -> Covered Tables Room (1F) Bottom Right Ceiling Hole

    {"from": {"map": "DGB_10", "id": 0}, "to": {"map": "DGB_10", "id": 1}, "reqs": []}, #? Sealed Room (2F) Cracked Wall Bottom Left -> Sealed Room (2F) Top Left Hole
    {"from": {"map": "DGB_10", "id": 1}, "to": {"map": "DGB_10", "id": 0}, "reqs": []}, #? Sealed Room (2F) Top Left Hole -> Sealed Room (2F) Cracked Wall Bottom Left
    {"from": {"map": "DGB_10", "id": 0}, "to": {"map": "DGB_10", "id": 2}, "reqs": []}, #? Sealed Room (2F) Cracked Wall Bottom Left -> Sealed Room (2F) Top Right Hole
    {"from": {"map": "DGB_10", "id": 2}, "to": {"map": "DGB_10", "id": 0}, "reqs": []}, #? Sealed Room (2F) Top Right Hole -> Sealed Room (2F) Cracked Wall Bottom Left
    {"from": {"map": "DGB_10", "id": 0}, "to": {"map": "DGB_10", "id": 3}, "reqs": []}, #? Sealed Room (2F) Cracked Wall Bottom Left -> Sealed Room (2F) Bottom Right Hole
    {"from": {"map": "DGB_10", "id": 3}, "to": {"map": "DGB_10", "id": 0}, "reqs": []}, #? Sealed Room (2F) Bottom Right Hole -> Sealed Room (2F) Cracked Wall Bottom Left

    {"from": {"map": "DGB_10", "id": 1}, "to": {"map": "DGB_10", "id": 1}, "reqs": [], "pseudoitems": ["GF_DGB10_BoardedFloor3"]}, #+ Sealed Room (2F) Top Left Hole

    # DGB_11 Covered Tables Room (1F)
    {"from": {"map": "DGB_11", "id": 0}, "to": {"map": "DGB_02", "id": 3}, "reqs": []}, # Covered Tables Room (1F) Door Bottom -> West Hall (1F) Door Top Right
    #{"from": {"map": "DGB_11", "id": 1}, "to": {"map": None, "id": None}, "reqs": []},  # Covered Tables Room (1F) Bottom Right Ceiling Hole
    #{"from": {"map": "DGB_11", "id": 2}, "to": {"map": None, "id": None}, "reqs": []},  # Covered Tables Room (1F) Top Right Ceiling Hole
    {"from": {"map": "DGB_11", "id": 3}, "to": {"map": "DGB_10", "id": 1}, "reqs": [["GF_DGB10_BoardedFloor3"],["Boots"]]}, # Covered Tables Room (1F) Spring To Ceiling -> Sealed Room (2F) Top Left Hole

    {"from": {"map": "DGB_11", "id": 0}, "to": {"map": "DGB_11", "id": 1}, "reqs": []}, #? Covered Tables Room (1F) Door Bottom -> Covered Tables Room (1F) Bottom Right Ceiling Hole
    {"from": {"map": "DGB_11", "id": 1}, "to": {"map": "DGB_11", "id": 0}, "reqs": []}, #? Covered Tables Room (1F) Bottom Right Ceiling Hole -> Covered Tables Room (1F) Door Bottom
    {"from": {"map": "DGB_11", "id": 2}, "to": {"map": "DGB_11", "id": 0}, "reqs": []}, #? Covered Tables Room (1F) Top Right Ceiling Hole -> Covered Tables Room (1F) Door Bottom
    {"from": {"map": "DGB_11", "id": 2}, "to": {"map": "DGB_11", "id": 3}, "reqs": [["GF_DGB10_BoardedFloor3"]]}, #? Covered Tables Room (1F) Top Right Ceiling Hole -> Covered Tables Room (1F) Spring To Ceiling
    {"from": {"map": "DGB_11", "id": 0}, "to": {"map": "DGB_11", "id": 3}, "reqs": []}, #? Covered Tables Room (1F) Door Bottom -> Covered Tables Room (1F) Spring To Ceiling
    {"from": {"map": "DGB_11", "id": 3}, "to": {"map": "DGB_11", "id": 0}, "reqs": []}, #? Covered Tables Room (1F) Spring To Ceiling -> Covered Tables Room (1F) Door Bottom

    {"from": {"map": "DGB_11", "id": 2}, "to": {"map": "DGB_11", "id": "ItemA"}, "reqs": [["Parakarry"]]}, #* Covered Tables Room (1F) Top Right Ceiling Hole -> ItemA (DDownJump)

    # DGB_12 Spike Trap Room (2F)
    {"from": {"map": "DGB_12", "id": 0}, "to": {"map": "DGB_09", "id": 2}, "reqs": []}, # Spike Trap Room (2F) Door Bottom Left -> West Hall (2F) Door Top Left

    {"from": {"map": "DGB_12", "id": 0}, "to": {"map": "DGB_12", "id": "ChestA"}, "reqs": [["Bow","Lakilester"]]}, #* Spike Trap Room (2F) Door Bottom Left -> ChestA (CastleKey1)

    # DGB_13 Hidden Bedroom (2F)
    {"from": {"map": "DGB_13", "id": 0}, "to": {"map": "DGB_03", "id": 5}, "reqs": []}, # Hidden Bedroom (2F) Door Bottom -> Table/Clock Room (1/2F) 2F Behind The Clock

    {"from": {"map": "DGB_13", "id": "ItemB"}, "to": {"map": "DGB_13", "id": "ItemA"}, "reqs": []}, #+ CHAINED REQUIREMENTS -> ItemA (MegaRush)
    {"from": {"map": "DGB_13", "id": 0},       "to": {"map": "DGB_13", "id": "ItemB"}, "reqs": [["Boots"],["Parakarry"]]}, #* Hidden Bedroom (2F) Door Bottom -> ItemB (Coin)
    {"from": {"map": "DGB_13", "id": "ItemB"}, "to": {"map": "DGB_13", "id": "ItemC"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemC (Coin)
    {"from": {"map": "DGB_13", "id": "ItemB"}, "to": {"map": "DGB_13", "id": "ItemD"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemD (Coin)
    {"from": {"map": "DGB_13", "id": "ItemB"}, "to": {"map": "DGB_13", "id": "ItemE"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemE (Coin)
    {"from": {"map": "DGB_13", "id": "ItemB"}, "to": {"map": "DGB_13", "id": "ItemF"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemF (Coin)
    {"from": {"map": "DGB_13", "id": "ItemB"}, "to": {"map": "DGB_13", "id": "ItemG"}, "reqs": []}, #+ SHARED REQUIREMENTS -> ItemG (Coin)

    # DGB_14 Stairs to Third Floor
    {"from": {"map": "DGB_14", "id": 0}, "to": {"map": "DGB_03", "id": 3}, "reqs": []}, # Stairs to Third Floor Door Bottom Right -> Table/Clock Room (1/2F) Door 2F Far Left
    {"from": {"map": "DGB_14", "id": 1}, "to": {"map": "DGB_15", "id": 0}, "reqs": []}, # Stairs to Third Floor Door Top Right -> West Hall (3F) Door Far Left

    {"from": {"map": "DGB_14", "id": 0}, "to": {"map": "DGB_14", "id": 1}, "reqs": []}, #? Stairs to Third Floor Door Bottom Right -> Stairs to Third Floor Door Top Right
    {"from": {"map": "DGB_14", "id": 1}, "to": {"map": "DGB_14", "id": 0}, "reqs": []}, #? Stairs to Third Floor Door Top Right -> Stairs to Third Floor Door Bottom Right

    {"from": {"map": "DGB_14", "id": 0}, "to": {"map": "DGB_14", "id": "YBlockA"}, "reqs": []}, #* Stairs to Third Floor Door Bottom Right -> YBlockA (MapleSyrup)

    # DGB_15 West Hall (3F)
    {"from": {"map": "DGB_15", "id": 0}, "to": {"map": "DGB_14", "id": 1}, "reqs": []}, # West Hall (3F) Door Far Left -> Stairs to Third Floor Door Top Right
    {"from": {"map": "DGB_15", "id": 1}, "to": {"map": "DGB_17", "id": 0}, "reqs": [[{"TubbaCastleKey": 3}]]}, # West Hall (3F) Door Far Right -> Save Room (3F) Door Left
    {"from": {"map": "DGB_15", "id": 2}, "to": {"map": "DGB_16", "id": 0}, "reqs": []}, # West Hall (3F) Door Top Right -> Sleeping Clubbas Room (3F) Door Bottom Right

    {"from": {"map": "DGB_15", "id": 0}, "to": {"map": "DGB_15", "id": 1}, "reqs": []}, #? West Hall (3F) Door Far Left -> West Hall (3F) Door Far Right
    {"from": {"map": "DGB_15", "id": 1}, "to": {"map": "DGB_15", "id": 0}, "reqs": []}, #? West Hall (3F) Door Far Right -> West Hall (3F) Door Far Left
    {"from": {"map": "DGB_15", "id": 0}, "to": {"map": "DGB_15", "id": 2}, "reqs": []}, #? West Hall (3F) Door Far Left -> West Hall (3F) Door Top Right
    {"from": {"map": "DGB_15", "id": 2}, "to": {"map": "DGB_15", "id": 0}, "reqs": []}, #? West Hall (3F) Door Top Right -> West Hall (3F) Door Far Left

    # DGB_16 Sleeping Clubbas Room (3F)
    {"from": {"map": "DGB_16", "id": 0}, "to": {"map": "DGB_15", "id": 2}, "reqs": []}, # Sleeping Clubbas Room (3F) Door Bottom Right -> West Hall (3F) Door Top Right

    {"from": {"map": "DGB_16", "id": 0}, "to": {"map": "DGB_16", "id": "ItemA"}, "reqs": [["can_climb_steps"]]}, #* Sleeping Clubbas Room (3F) Door Bottom Right -> ItemA (CastleKey1)

    # DGB_17 Save Room (3F)
    {"from": {"map": "DGB_17", "id": 0}, "to": {"map": "DGB_15", "id": 1}, "reqs": []}, # Save Room (3F) Door Left -> West Hall (3F) Door Far Right
    {"from": {"map": "DGB_17", "id": 1}, "to": {"map": "DGB_01", "id": 5}, "reqs": []}, # Save Room (3F) Door Right -> Great Hall Door Door 3F Left

    {"from": {"map": "DGB_17", "id": 0}, "to": {"map": "DGB_17", "id": 1}, "reqs": []}, #? Save Room (3F) Door Left -> Save Room (3F) Door Right
    {"from": {"map": "DGB_17", "id": 1}, "to": {"map": "DGB_17", "id": 0}, "reqs": []}, #? Save Room (3F) Door Right -> Save Room (3F) Door Left

    # DGB_18 Master Bedroom (3F)
    {"from": {"map": "DGB_18", "id": 0}, "to": {"map": "DGB_01", "id": 6}, "reqs": []}, # Master Bedroom (3F) Door Left -> Great Hall Door Door 3F Right

    {"from": {"map": "DGB_18", "id": 0}, "to": {"map": "DGB_18", "id": 0}, "reqs": [], "pseudoitems": ["MysticalKey"]}, #+ Master Bedroom (3F) Door Left
]
