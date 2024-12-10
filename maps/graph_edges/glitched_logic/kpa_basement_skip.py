"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Basement Skip
"""
edges_kpa_add_basement_skip_parakarry = [
    #? Front Door Exterior Lava Door Right -> Front Door Exterior Hangar Door Bottom Left (ultra boots clip and parakarry)
    {"from": {"map": "KPA_62",  "id": 2}, "to": {"map": "KPA_62",  "id": 0}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"],["Parakarry"],["UltraBoots"]], "pseudoitems": ["RF_Ch8_FirstGuardDoor"], "mapchange": False}, 
    #? Guard Door 1 Door Left -> Guard Door 1 Fall In Trap Door
    {"from": {"map": "KPA_81",  "id": 0}, "to": {"map": "KPA_81",  "id": 1}, "reqs": [["Bombette"], ["Lakilester"], ["Parakarry"], ["UltraBoots"]], "mapchange": False}, 
]

edges_kpa_add_basement_skip_lakilester = [
    #? Front Door Exterior Lava Door Right -> Front Door Exterior Hangar Door Bottom Left (laki teleport)
    {"from": {"map": "KPA_62",  "id": 2}, "to": {"map": "KPA_62",  "id": 0}, "reqs": [["Lakilester"],["can_climb_steps"]], "pseudoitems": ["RF_Ch8_FirstGuardDoor"], "mapchange": False}, 
    #? Guard Door 1 Door Left -> Guard Door 1 Fall In Trap Door
    {"from": {"map": "KPA_81",  "id": 0}, "to": {"map": "KPA_81",  "id": 1}, "reqs": [["Bombette"], ["Lakilester"], ["can_climb_steps"]], "mapchange": False}, 
]

edges_kpa_add_basement_skip_hammer = [
    #? Front Door Exterior Lava Door Right -> Front Door Exterior Hangar Door Bottom Left (hammer clip)
    {"from": {"map": "KPA_62",  "id": 2}, "to": {"map": "KPA_62",  "id": 0}, "reqs": [["Lakilester","GF_KPA16_ShutOffLava"],["can_climb_steps"],["Hammer"]], "pseudoitems": ["RF_Ch8_FirstGuardDoor"], "mapchange": False}, 
    #? Guard Door 1 Door Left -> Guard Door 1 Fall In Trap Door
    {"from": {"map": "KPA_81",  "id": 0}, "to": {"map": "KPA_81",  "id": 1}, "reqs": [["Bombette"], ["Lakilester"], ["Hammer"], ["can_climb_steps"]], "mapchange": False}, 
]
