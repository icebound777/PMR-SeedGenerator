"""
This file represents edges of the world graph that have to be added / removed
for the Shorten Bowser's Castle setting.
"""
edges_kpa_add = [
    # KPA_32 Lower Grand Hall Door Bottom Left -> Guard Door 2 Guard Door Right
    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_82",  "id": 1}, "reqs": [], "mapchange": True},

    # KPA_33 Upper Grand Hall Door Top Right -> Blue Fire Bridge Door Left
    {"from": {"map": "KPA_33",  "id": 2}, "to": {"map": "KPA_102", "id": 0}, "reqs": [], "mapchange": True},

    # KPA_50 Hall to Guard Door 1 Door Right -> Guard Door 2 Door Left
    {"from": {"map": "KPA_50",  "id": 1}, "to": {"map": "KPA_82",  "id": 0}, "reqs": [], "mapchange": True},

    # KPA_51 Hall to Water Puzzle Door Right -> Bill Blaster Hall Door Left
    {"from": {"map": "KPA_51",  "id": 1}, "to": {"map": "KPA_130", "id": 0}, "reqs": [], "mapchange": True},

    # KPA_61 Battlement Door Bottom Left -> Hidden Passage 1 Door Right
    {"from": {"map": "KPA_61",  "id": 0}, "to": {"map": "KPA_112", "id": 1}, "reqs": [], "mapchange": True},

    # KPA_62 Front Door Exterior Front Door -> Entry Lava Hall Door Left
    #+ This removes the key requirement
    {"from": {"map": "KPA_62",  "id": 0}, "to": {"map": "KPA_70",  "id": 0}, "reqs": []},

    # KPA_82 Guard Door 2 Door Left -> Hall to Guard Door 1 Door Right
    {"from": {"map": "KPA_82",  "id": 0}, "to": {"map": "KPA_50",  "id": 1}, "reqs": [], "mapchange": True},
    # KPA_82 Guard Door 2 Guard Door Right -> Lower Grand Hall Door Bottom Left
    {"from": {"map": "KPA_82",  "id": 1}, "to": {"map": "KPA_32",  "id": 0}, "reqs": [], "mapchange": True},

    # KPA_102 Blue Fire Bridge Door Left -> Upper Grand Hall Door Top Right
    {"from": {"map": "KPA_102", "id": 0}, "to": {"map": "KPA_33",  "id": 2}, "reqs": [], "mapchange": True},

    # KPA_112 Hidden Passage 1 Door Right -> Battlement Door Bottom Left
    {"from": {"map": "KPA_112", "id": 1}, "to": {"map": "KPA_61",  "id": 0}, "reqs": [], "mapchange": True},

    # KPA_130 Bill Blaster Hall Door Left -> Hall to Water Puzzle Door Right
    {"from": {"map": "KPA_130", "id": 0}, "to": {"map": "KPA_51",  "id": 1}, "reqs": [], "mapchange": True},
]

edges_kpa_remove = [
    # KPA_32 Lower Grand Hall Door Bottom Left -> Guard Door 1 Guard Door Right
    {"from": {"map": "KPA_32",  "id": 0}, "to": {"map": "KPA_81",  "id": 2}, "reqs": []},

    # KPA_33 Upper Grand Hall Door Top Right -> Split Level Hall Door Left
    {"from": {"map": "KPA_33",  "id": 2}, "to": {"map": "KPA_52",  "id": 0}, "reqs": []},

    # KPA_50 Hall to Guard Door 1 Door Right -> Guard Door 1 Door Left
    {"from": {"map": "KPA_50",  "id": 1}, "to": {"map": "KPA_81",  "id": 0}, "reqs": []},

    # KPA_51 Hall to Water Puzzle Door Right -> Left Water Puzzle Door Bottom Left
    {"from": {"map": "KPA_51",  "id": 1}, "to": {"map": "KPA_133", "id": 0}, "reqs": []},

    # KPA_61 Battlement Bottom Left -> Guard Door 2 Guard Door Right
    {"from": {"map": "KPA_61",  "id": 0}, "to": {"map": "KPA_82",  "id": 1}, "reqs": []},

    #? KPA_62 Front Door Exterior Front Door -> Entry Lava Hall Door Left
    # This removes the key requirement
    {"from": {"map": "KPA_62",  "id": 0}, "to": {"map": "KPA_70",  "id": 0}, "reqs": [[{"BowserCastleKey": 1}]]},

    # KPA_82 Guard Door 2 Door Left -> Room with Hidden Door 2 Door Right
    {"from": {"map": "KPA_82",  "id": 0}, "to": {"map": "KPA_113", "id": 1}, "reqs": []},
    # KPA_82 Guard Door 2 Door Left -> Battlement Door Bottom Left
    {"from": {"map": "KPA_82",  "id": 1}, "to": {"map": "KPA_61",  "id": 0}, "reqs": []},

    # KPA_102 Blue Fire Bridge Door Left -> Maze Room Door Top Right
    {"from": {"map": "KPA_102", "id": 0}, "to": {"map": "KPA_41",  "id": 2}, "reqs": []},

    # KPA_112 Hidden Passage 1 Door Right -> Room with Hidden Door 2 Door Left
    {"from": {"map": "KPA_112", "id": 1}, "to": {"map": "KPA_113", "id": 0}, "reqs": []},

    # KPA_130 Bill Blaster Hall Door Left -> Right Water Puzzle Door Bottom Right
    {"from": {"map": "KPA_130", "id": 0}, "to": {"map": "KPA_134", "id": 1}, "reqs": []},
]
