"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Blue House Skip.
"""
edges_mac_add_bhs_jump = [
    #? Southern District Exit Top -> Southern District Blue House Pipe
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 5}, "reqs": [["Boots"]], "mapchange": False},
    #? Southern District Blue House Pipe -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 5}, "to": {"map": "MAC_02", "id": 2}, "reqs": [], "mapchange": False},
]

edges_mac_add_bhs_laki = [
    #? Southern District Exit Top -> Southern District Blue House Pipe
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 5}, "reqs": [["Lakilester"],["can_climb_steps"]], "mapchange": False},
    #? Southern District Blue House Pipe -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 5}, "to": {"map": "MAC_02", "id": 2}, "reqs": [], "mapchange": False},
]

edges_mac_add_bhs_toad_lure = [
    #? Southern District Exit Top -> Southern District Blue House Pipe
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 5}, "reqs": [["Hammer"],["can_climb_steps"]], "mapchange": False},
    #? Southern District Blue House Pipe -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 5}, "to": {"map": "MAC_02", "id": 2}, "reqs": [], "mapchange": False},
]
