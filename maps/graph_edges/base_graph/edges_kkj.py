"""This file represents all edges of the world graph that have origin-nodes in the KKJ (Peach's Castle) area."""
edges_kkj = [
    # KKJ_10 Entry Hall (1F)
    {"from": {"map": "KKJ_10", "id": 0}, "to": {"map": "OSR_02", "id": 1}, "reqs": []}, # Entry Hall (1F) Door Bottom -> Hijacked Castle Entrance Door North
    {"from": {"map": "KKJ_10", "id": 1}, "to": {"map": "KKJ_11", "id": 0}, "reqs": []}, # Entry Hall (1F) Door Top -> Upper Hall (2F) Door Bottom Left
    {"from": {"map": "KKJ_10", "id": 2}, "to": {"map": "KKJ_21", "id": 0}, "reqs": []}, # Entry Hall (1F) Door Far Left -> Inactive Quiz-Off (1F) Door Right
    {"from": {"map": "KKJ_10", "id": 3}, "to": {"map": "KKJ_19", "id": 0}, "reqs": []}, # Entry Hall (1F) Door Back Right -> Kitchen (1F) Door Bottom Right
    {"from": {"map": "KKJ_10", "id": 4}, "to": {"map": "KKJ_20", "id": 0}, "reqs": []}, # Entry Hall (1F) Door Far Right -> Guest Room (1F) Door Left

    {"from": {"map": "KKJ_10", "id": 0}, "to": {"map": "KKJ_10", "id": 1}, "reqs": []}, #? Entry Hall (1F) Door Bottom -> Entry Hall (1F) Door Top
    {"from": {"map": "KKJ_10", "id": 1}, "to": {"map": "KKJ_10", "id": 0}, "reqs": []}, #? Entry Hall (1F) Door Top -> Entry Hall (1F) Door Bottom
    {"from": {"map": "KKJ_10", "id": 0}, "to": {"map": "KKJ_10", "id": 2}, "reqs": []}, #? Entry Hall (1F) Door Bottom -> Entry Hall (1F) Door Far Left
    {"from": {"map": "KKJ_10", "id": 2}, "to": {"map": "KKJ_10", "id": 0}, "reqs": []}, #? Entry Hall (1F) Door Far Left -> Entry Hall (1F) Door Bottom
    {"from": {"map": "KKJ_10", "id": 0}, "to": {"map": "KKJ_10", "id": 3}, "reqs": []}, #? Entry Hall (1F) Door Bottom -> Entry Hall (1F) Door Back Right
    {"from": {"map": "KKJ_10", "id": 3}, "to": {"map": "KKJ_10", "id": 0}, "reqs": []}, #? Entry Hall (1F) Door Back Right -> Entry Hall (1F) Door Bottom
    {"from": {"map": "KKJ_10", "id": 0}, "to": {"map": "KKJ_10", "id": 4}, "reqs": []}, #? Entry Hall (1F) Door Bottom -> Entry Hall (1F) Door Far Right
    {"from": {"map": "KKJ_10", "id": 4}, "to": {"map": "KKJ_10", "id": 0}, "reqs": []}, #? Entry Hall (1F) Door Far Right -> Entry Hall (1F) Door Bottom

    # KKJ_11 Upper Hall (2F)
    {"from": {"map": "KKJ_11", "id": 0}, "to": {"map": "KKJ_10", "id": 1}, "reqs": []}, # Upper Hall (2F) Door Bottom Left -> Entry Hall (1F) Door Top
    {"from": {"map": "KKJ_11", "id": 1}, "to": {"map": "KKJ_12", "id": 0}, "reqs": []}, # Upper Hall (2F) Door Top Back -> Stairs Hallway (3F) Door Left
    {"from": {"map": "KKJ_11", "id": 2}, "to": {"map": "KKJ_16", "id": 0}, "reqs": []}, # Upper Hall (2F) Door Left -> Library (2F) Door Right
    {"from": {"map": "KKJ_11", "id": 3}, "to": {"map": "KKJ_15", "id": 0}, "reqs": []}, # Upper Hall (2F) Door Back Left -> Passage Outlet (2F) Door Right
    {"from": {"map": "KKJ_11", "id": 4}, "to": {"map": "KKJ_14", "id": 0}, "reqs": []}, # Upper Hall (2F) Door Bottom Back -> Peach's Room (2F) Door Left
    {"from": {"map": "KKJ_11", "id": 5}, "to": {"map": "KKJ_17", "id": 0}, "reqs": []}, # Upper Hall (2F) Door Right -> Storeroom (2F) Door Left
    {"from": {"map": "KKJ_11", "id": 6}, "to": {"map": "KKJ_18", "id": 0}, "reqs": []}, # Upper Hall (2F) Door Bottom Right -> Dining Room (2F) Door Left

    {"from": {"map": "KKJ_11", "id": 0}, "to": {"map": "KKJ_11", "id": 1}, "reqs": []}, #? Upper Hall (2F) Door Bottom Left -> Upper Hall (2F) Door Top Back
    {"from": {"map": "KKJ_11", "id": 1}, "to": {"map": "KKJ_11", "id": 0}, "reqs": []}, #? Upper Hall (2F) Door Top Back -> Upper Hall (2F) Door Bottom Left
    {"from": {"map": "KKJ_11", "id": 0}, "to": {"map": "KKJ_11", "id": 2}, "reqs": []}, #? Upper Hall (2F) Door Bottom Left -> Upper Hall (2F) Door Left
    {"from": {"map": "KKJ_11", "id": 2}, "to": {"map": "KKJ_11", "id": 0}, "reqs": []}, #? Upper Hall (2F) Door Left -> Upper Hall (2F) Door Bottom Left
    {"from": {"map": "KKJ_11", "id": 0}, "to": {"map": "KKJ_11", "id": 3}, "reqs": []}, #? Upper Hall (2F) Door Bottom Left -> Upper Hall (2F) Door Back Left
    {"from": {"map": "KKJ_11", "id": 3}, "to": {"map": "KKJ_11", "id": 0}, "reqs": []}, #? Upper Hall (2F) Door Back Left -> Upper Hall (2F) Door Bottom Left
    {"from": {"map": "KKJ_11", "id": 0}, "to": {"map": "KKJ_11", "id": 4}, "reqs": []}, #? Upper Hall (2F) Door Bottom Left -> Upper Hall (2F) Door Bottom Back
    {"from": {"map": "KKJ_11", "id": 4}, "to": {"map": "KKJ_11", "id": 0}, "reqs": []}, #? Upper Hall (2F) Door Bottom Back -> Upper Hall (2F) Door Bottom Left
    {"from": {"map": "KKJ_11", "id": 0}, "to": {"map": "KKJ_11", "id": 5}, "reqs": []}, #? Upper Hall (2F) Door Bottom Left -> Upper Hall (2F) Door Right
    {"from": {"map": "KKJ_11", "id": 5}, "to": {"map": "KKJ_11", "id": 0}, "reqs": []}, #? Upper Hall (2F) Door Right -> Upper Hall (2F) Door Bottom Left
    {"from": {"map": "KKJ_11", "id": 0}, "to": {"map": "KKJ_11", "id": 6}, "reqs": []}, #? Upper Hall (2F) Door Bottom Left -> Upper Hall (2F) Door Bottom Right
    {"from": {"map": "KKJ_11", "id": 6}, "to": {"map": "KKJ_11", "id": 0}, "reqs": []}, #? Upper Hall (2F) Door Bottom Right -> Upper Hall (2F) Door Bottom Left

    # KKJ_12 Stairs Hallway (3F)
    {"from": {"map": "KKJ_12", "id": 0}, "to": {"map": "KKJ_11", "id": 1}, "reqs": []}, # Stairs Hallway (3F) Door Left -> Upper Hall (2F) Door Top Back
    {"from": {"map": "KKJ_12", "id": 1}, "to": {"map": "KKJ_13", "id": 0}, "reqs": []}, # Stairs Hallway (3F) Door Right -> Window Hallway (4F) Door Left

    {"from": {"map": "KKJ_12", "id": 0}, "to": {"map": "KKJ_12", "id": 1}, "reqs": []}, #? Stairs Hallway (3F) Door Left -> Stairs Hallway (3F) Door Right
    {"from": {"map": "KKJ_12", "id": 1}, "to": {"map": "KKJ_12", "id": 0}, "reqs": []}, #? Stairs Hallway (3F) Door Right -> Stairs Hallway (3F) Door Left

    # KKJ_13 Window Hallway (4F)
    {"from": {"map": "KKJ_13", "id": 0}, "to": {"map": "KKJ_12", "id": 1}, "reqs": []}, # Window Hallway (4F) Door Left -> Stairs Hallway (3F) Door Right
    {"from": {"map": "KKJ_13", "id": 1}, "to": {"map": "KKJ_22", "id": 0}, "reqs": []}, # Window Hallway (4F) Door Right -> Double Staircase (4F) Door Bottom Left

    {"from": {"map": "KKJ_13", "id": 0}, "to": {"map": "KKJ_13", "id": 1}, "reqs": []}, #? Window Hallway (4F) Door Left -> Window Hallway (4F) Door Right
    {"from": {"map": "KKJ_13", "id": 1}, "to": {"map": "KKJ_13", "id": 0}, "reqs": []}, #? Window Hallway (4F) Door Right -> Window Hallway (4F) Door Left

    # KKJ_14 Peach's Room (2F)
    {"from": {"map": "KKJ_14", "id": 0}, "to": {"map": "KKJ_11", "id": 4}, "reqs": []}, # Peach's Room (2F) Door Left -> Upper Hall (2F) Door Bottom Back
    {"from": {"map": "KKJ_14", "id": 1}, "to": {"map": "KKJ_26", "id": 0}, "reqs": []}, # Peach's Room (2F) Door Right -> Balcony (2F) Door Left

    {"from": {"map": "KKJ_14", "id": 0}, "to": {"map": "KKJ_14", "id": 1}, "reqs": []}, #? Peach's Room (2F) Door Left -> Peach's Room (2F) Door Right
    {"from": {"map": "KKJ_14", "id": 1}, "to": {"map": "KKJ_14", "id": 0}, "reqs": []}, #? Peach's Room (2F) Door Right -> Peach's Room (2F) Door Left

    # KKJ_15 Passage Outlet (2F)
    {"from": {"map": "KKJ_15", "id": 0}, "to": {"map": "KKJ_11", "id": 3}, "reqs": []}, # Passage Outlet (2F) Door Right -> Upper Hall (2F) Door Back Left

    # KKJ_16 Library (2F)
    {"from": {"map": "KKJ_16", "id": 0}, "to": {"map": "KKJ_11", "id": 2}, "reqs": []}, # Library (2F) Door Right -> Upper Hall (2F) Door Left

    {"from": {"map": "KKJ_16", "id": 0}, "to": {"map": "KKJ_16", "id": "ItemA"}, "reqs": [["can_climb_steps"]]}, #* Library (2F) Door Right -> ItemA (LifeShroom)
    {"from": {"map": "KKJ_16", "id": 0}, "to": {"map": "KKJ_16", "id": "ItemB"}, "reqs": []}, #* Library (2F) Door Right -> ItemB (PowerRush)

    # KKJ_17 Storeroom (2F)
    {"from": {"map": "KKJ_17", "id": 0}, "to": {"map": "KKJ_11", "id": 5}, "reqs": []}, # Storeroom (2F) Door Left -> Upper Hall (2F) Door Right

    {"from": {"map": "KKJ_17", "id": 0}, "to": {"map": "KKJ_17", "id": "ItemA"}, "reqs": []}, #* Storeroom (2F) Door Left -> ItemA (DeepFocus1)

    # KKJ_18 Dining Room (2F)
    {"from": {"map": "KKJ_18", "id": 0}, "to": {"map": "KKJ_11", "id": 6}, "reqs": []}, # Dining Room (2F) Door Left -> Upper Hall (2F) Door Bottom Right

    # KKJ_19 Kitchen (1F)
    {"from": {"map": "KKJ_19", "id": 0}, "to": {"map": "KKJ_10", "id": 3}, "reqs": []}, # Kitchen (1F) Door Bottom Right -> Entry Hall (1F) Door Back Right

    # KKJ_20 Guest Room (1F)
    {"from": {"map": "KKJ_20", "id": 0}, "to": {"map": "KKJ_10", "id": 4}, "reqs": []}, # Guest Room (1F) Door Left -> Entry Hall (1F) Door Far Right

    {"from": {"map": "KKJ_20", "id": 0}, "to": {"map": "KKJ_20", "id": "ChestA"}, "reqs": []}, #* Guest Room (1F) Door Left -> ChestA (LastStand)

    # KKJ_21 Inactive Quiz-Off (1F)
    {"from": {"map": "KKJ_21", "id": 0}, "to": {"map": "KKJ_10", "id": 2}, "reqs": []}, # Inactive Quiz-Off (1F) Door Right -> Entry Hall (1F) Door Far Left

    # KKJ_22 Double Staircase (4F)
    {"from": {"map": "KKJ_22", "id": 0}, "to": {"map": "KKJ_13", "id": 1}, "reqs": []}, # Double Staircase (4F) Door Bottom Left -> Window Hallway (4F) Door Right
    {"from": {"map": "KKJ_22", "id": 1}, "to": {"map": "KKJ_23", "id": 0}, "reqs": []}, # Double Staircase (4F) Door Top Left -> Rooftop (5F) Door Right

    {"from": {"map": "KKJ_22", "id": 0}, "to": {"map": "KKJ_22", "id": 1}, "reqs": []}, #? Double Staircase (4F) Door Bottom Left -> Double Staircase (4F) Door Top Left
    {"from": {"map": "KKJ_22", "id": 1}, "to": {"map": "KKJ_22", "id": 0}, "reqs": []}, #? Double Staircase (4F) Door Top Left -> Double Staircase (4F) Door Bottom Left

    # KKJ_23 Rooftop (5F)
    {"from": {"map": "KKJ_23", "id": 0}, "to": {"map": "KKJ_22", "id": 1}, "reqs": []}, # Rooftop (5F) Door Right -> Double Staircase (4F) Door Top Left
    {"from": {"map": "KKJ_23", "id": 1}, "to": {"map": "KKJ_24", "id": 0}, "reqs": []}, # Rooftop (5F) Door Left -> Tower Staircase (5F) Door Bottom

    {"from": {"map": "KKJ_23", "id": 0}, "to": {"map": "KKJ_23", "id": 1}, "reqs": []}, #? Rooftop (5F) Door Right -> Rooftop (5F) Door Left
    {"from": {"map": "KKJ_23", "id": 1}, "to": {"map": "KKJ_23", "id": 0}, "reqs": []}, #? Rooftop (5F) Door Left -> Rooftop (5F) Door Right

    # KKJ_24 Tower Staircase (5F)
    {"from": {"map": "KKJ_24", "id": 0}, "to": {"map": "KKJ_23", "id": 1}, "reqs": []}, # Tower Staircase (5F) Door Bottom -> Rooftop (5F) Door Left
    {"from": {"map": "KKJ_24", "id": 1}, "to": {"map": "KKJ_25", "id": 0}, "reqs": []}, # Tower Staircase (5F) Door Top -> Final Boss Arena (6F) Door Left

    {"from": {"map": "KKJ_24", "id": 0}, "to": {"map": "KKJ_24", "id": 1}, "reqs": []}, #? Tower Staircase (5F) Door Bottom -> Tower Staircase (5F) Door Top
    {"from": {"map": "KKJ_24", "id": 1}, "to": {"map": "KKJ_24", "id": 0}, "reqs": []}, #? Tower Staircase (5F) Door Top -> Tower Staircase (5F) Door Bottom

    # KKJ_25 Final Boss Arena (6F)
    {"from": {"map": "KKJ_25", "id": 0}, "to": {"map": "KKJ_24", "id": 1}, "reqs": []}, # Final Boss Arena (6F) Door Left -> Tower Staircase (5F) Door Top

    {"from": {"map": "KKJ_25", "id": 0}, "to": {"map": "KKJ_24", "id": 1}, "reqs": [["RF_HasStarbeam"]], "pseudoitems": ["YOUWIN"]}, #+ Beat Bowser

    # KKJ_26 Balcony (2F)
    {"from": {"map": "KKJ_26", "id": 0}, "to": {"map": "KKJ_14", "id": 1}, "reqs": []}, # Balcony (2F) Door Left -> Peach's Room (2F) Door Right
]
