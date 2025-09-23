"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Cannonless
Cannonless allows the cannon room to be crossed jumpless using Parakarry and Lakilester.
"""
edges_kpa_add_cannonless = [
    #? Bill Blaster Hall Door Left -> Bill Blaster Hall Door Top Right
    {"from": {"map": "KPA_130",  "id": 0}, "to": {"map": "KPA_130",  "id": 1}, "reqs": [["Lakilester"],["can_climb_steps"]], "mapchange": False}, 
]
