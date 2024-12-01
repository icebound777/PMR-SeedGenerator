"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Bubble Berry Tree Early.
"""

edges_flo_add_bubble_berry_tree_early_laki = [
    #* (SE) Water Level Room Exit Left -> Tree1_Drop1A (BubbleBerry)
    {"from": {"map": "FLO_24", "id": 0}, "to": {"map": "FLO_24", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"], ["Lakilester"]], "mapchange": False},
    #* (SE) Water Level Room Exit Left -> Tree1_Drop1B (BubbleBerry)
    {"from": {"map": "FLO_24", "id": 0}, "to": {"map": "FLO_24", "id": "Tree1_Drop1B"}, "reqs": [["can_shake_trees"], ["Lakilester"]], "mapchange": False},

    # Laki can be used to cross this room regardless of water level
    #? (SE) Water Level Room Exit Left -> (SE) Water Level Room Exit Right
    {"from": {"map": "FLO_24", "id": 0}, "to": {"map": "FLO_24", "id": 1}, "reqs": [["Lakilester"]]}, 
    #? (SE) Water Level Room Exit Right -> (SE) Water Level Room Exit Left
    {"from": {"map": "FLO_24", "id": 1}, "to": {"map": "FLO_24", "id": 0}, "reqs": [["Lakilester"]]}
]

edges_flo_add_bubble_berry_tree_early_ultra_boots = [
    #* (SE) Water Level Room Exit Left -> Tree1_Drop1A (BubbleBerry)
    {"from": {"map": "FLO_24", "id": 0}, "to": {"map": "FLO_24", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"], ["UltraBoots"]], "mapchange": False},
    #* (SE) Water Level Room Exit Left -> Tree1_Drop1B (BubbleBerry)
    {"from": {"map": "FLO_24", "id": 0}, "to": {"map": "FLO_24", "id": "Tree1_Drop1B"}, "reqs": [["can_shake_trees"], ["UltraBoots"]], "mapchange": False},
]
