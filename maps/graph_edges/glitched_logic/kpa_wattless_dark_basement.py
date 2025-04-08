"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Wattless Dark Basement
"""
edges_kpa_add_wattless_dark_basement = [
    #? Dark Cave 1 Door Bottom Left -> Dark Cave 1 Exit Top Left
    {"from": {"map": "KPA_01",  "id": 0}, "to": {"map": "KPA_01",  "id": 1}, "reqs": [["Parakarry"]]}, 
    #? Dark Cave 1 Exit Top Left -> Dark Cave 1 Door Bottom Left
    {"from": {"map": "KPA_01",  "id": 1}, "to": {"map": "KPA_01",  "id": 0}, "reqs": []}, 
    #* Dark Cave 1 Exit Top Left -> YBlockA (POWBlock)
    {"from": {"map": "KPA_01",  "id": 1}, "to": {"map": "KPA_01",  "id": "YBlockA"}, "reqs": [["Parakarry"],["can_hit_floating_blocks"]]}, 

    #? Dark Cave 2 Exit Right -> Dark Cave 2 Door Top Left
    {"from": {"map": "KPA_03",  "id": 0}, "to": {"map": "KPA_03",  "id": 1}, "reqs": [["Parakarry"]]}, 
    #? Dark Cave 2 Door Top Left -> Dark Cave 2 Exit Right
    {"from": {"map": "KPA_03",  "id": 1}, "to": {"map": "KPA_03",  "id": 0}, "reqs": [["can_climb_steps"]]}, 
    #* Dark Cave 2 Exit Right -> YBlockA (ShootingStar)]
    {"from": {"map": "KPA_03",  "id": 0}, "to": {"map": "KPA_03",  "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, 

    #+ KPA_81 Guard Door 1
    {"from": {"map": "KPA_81",  "id": 0}, "to": {"map": "KPA_81",  "id": 0}, "reqs": [], "pseudoitems": ["RF_WattlessBasement"]},
]
