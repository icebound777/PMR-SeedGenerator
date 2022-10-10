"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Fast Flood Room
"""
edges_kpa_add_fast_flood_room_kooper = [
    # KPA_133 Left Water Puzzle
    #? Left Water Puzzle Door Bottom Right Upper Half -> Left Water Puzzle Door Bombable Wall
    {"from": {"map": "KPA_133", "id": 2}, "to": {"map": "KPA_133", "id": 3}, "reqs": [["Lakilester"],["Bombette"], ["can_climb_steps"]], "mapchange": False},
    #* Left Water Puzzle Door Bombable Wall -> ItemA (BowserCastleKey)
    {"from": {"map": "KPA_133", "id": 3}, "to": {"map": "KPA_133", "id": "ItemA"}, "reqs": [["Lakilester"],["Kooper"]], "mapchange": False},

    # KPA_134 Right Water Puzzle
    #? Right Water Puzzle Door Bottom Left -> Right Water Puzzle Door Bottom Left Upper Half
    {"from": {"map": "KPA_134", "id": 0}, "to": {"map": "KPA_134", "id": 2}, "reqs": [["Lakilester"],["can_climb_steps"],["can_hit_floating_blocks"]], "mapchange": False},
    #? Right Water Puzzle Door Bottom Left Upper Half -> Right Water Puzzle Door Bottom Left
    {"from": {"map": "KPA_134", "id": 2}, "to": {"map": "KPA_134", "id": 0}, "reqs": [["Lakilester"],["can_hit_floating_blocks"]], "mapchange": False},
]

edges_kpa_add_fast_flood_room_bombette_ultra_boots = [
    # KPA_133 Left Water Puzzle
    #? Left Water Puzzle Door Bottom Right Upper Half -> Left Water Puzzle Door Bombable Wall
    {"from": {"map": "KPA_133", "id": 2}, "to": {"map": "KPA_133", "id": 3}, "reqs": [["Lakilester"],["Bombette"],["can_climb_steps"]], "mapchange": False},
    #* Left Water Puzzle Door Bombable Wall -> ItemA (BowserCastleKey)
    {"from": {"map": "KPA_133", "id": 3}, "to": {"map": "KPA_133", "id": "ItemA"}, "reqs": [["Lakilester"],["Bombette"],["UltraBoots"]], "mapchange": False},

    # KPA_134 Right Water Puzzle
    #? Right Water Puzzle Door Bottom Left -> Right Water Puzzle Door Bottom Left Upper Half
    {"from": {"map": "KPA_134", "id": 0}, "to": {"map": "KPA_134", "id": 2}, "reqs": [["Lakilester"],["can_climb_steps"],["can_hit_floating_blocks"]], "mapchange": False},
    #? Right Water Puzzle Door Bottom Left Upper Half -> Right Water Puzzle Door Bottom Left
    {"from": {"map": "KPA_134", "id": 2}, "to": {"map": "KPA_134", "id": 0}, "reqs": [["Lakilester"],["can_hit_floating_blocks"]], "mapchange": False},
]
