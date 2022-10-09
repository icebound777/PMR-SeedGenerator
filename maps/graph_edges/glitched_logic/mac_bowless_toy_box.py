"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Bowless Toy Box.
"""
edges_mac_add_bowless_toybox_hammer_lure = [
    #? Residental District Exit Right -> Residental District Toybox Spring
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 2}, "reqs": [["Hammer"],["can_climb_steps"]], "mapchange": False},
]

edges_mac_add_bowless_toybox_hammerless_lure = [
    #? Residental District Exit Right -> Residental District Toybox Spring
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 2}, "reqs": [["can_climb_steps"]], "mapchange": False},
]
