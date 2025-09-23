"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Bow-less Bowser's Castle Basement
"""
edges_kpa_add_bowless_bowsers_castle_basement_laki = [
    #? Lava Channel 3 Door Left -> Lava Channel 3 Lava Door Center
    {"from": {"map": "KPA_14",  "id": 0}, "to": {"map": "KPA_14",  "id": 2}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"],["Parakarry","GF_KPA16_ShutOffLava"],["can_climb_steps"]], "mapchange": False}, 
    #? Guard Door 1 Door Left -> Guard Door 1 Fall In Trap Door
    {"from": {"map": "KPA_81",  "id": 0}, "to": {"map": "KPA_81",  "id": 1}, "reqs": [["Bombette"], ["Lakilester"], ["Parakarry"]], "mapchange": False},
]
