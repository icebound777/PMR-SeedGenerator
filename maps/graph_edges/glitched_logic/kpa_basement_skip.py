"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Basement Skip
"""
edges_kpa_add_basement_skip_parakarry = [
    #? Front Door Exterior Lava Door Right -> Front Door Exterior Hangar Door Bottom Left (ultra boots clip and parakarry)
    {"from": {"map": "KPA_62",  "id": 2}, "to": {"map": "KPA_62",  "id": 0}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"],["Parakarry"],["UltraBoots"]], "mapchange": False}, 
]

edges_kpa_add_basement_skip_lakilester = [
    #? Front Door Exterior Lava Door Right -> Front Door Exterior Hangar Door Bottom Left (laki teleport)
    {"from": {"map": "KPA_62",  "id": 2}, "to": {"map": "KPA_62",  "id": 0}, "reqs": [["Lakilester"],["can_climb_steps"]], "mapchange": False}, 
]

edges_kpa_add_basement_skip_hammer = [
    #? Front Door Exterior Lava Door Right -> Front Door Exterior Hangar Door Bottom Left (hammer clip)
    {"from": {"map": "KPA_62",  "id": 2}, "to": {"map": "KPA_62",  "id": 0}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"],["can_climb_steps"],["Hammer"]], "mapchange": False}, 
]
