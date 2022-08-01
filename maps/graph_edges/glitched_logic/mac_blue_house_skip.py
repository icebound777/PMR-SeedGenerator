"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Blue House Skip.
"""
edges_mac_add_bhs = [
    #? Southern District Exit Top -> Southern District Blue House Pipe
    {"from": {"map": "MAC_02", "id": 2}, "to": {"map": "MAC_02", "id": 5}, "reqs": [], "mapchange": False},
    #? Southern District Blue House Pipe -> Southern District Exit Top
    {"from": {"map": "MAC_02", "id": 5}, "to": {"map": "MAC_02", "id": 2}, "reqs": [], "mapchange": False},
]
