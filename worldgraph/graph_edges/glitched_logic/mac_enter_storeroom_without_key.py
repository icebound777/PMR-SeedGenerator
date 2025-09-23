"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Enter Storeroom without Key.
"""
edges_mac_add_storeroom_without_key_parakarry = [
    #* Residental District Exit Right -> ItemA (SnowmanDoll)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemA"}, "reqs": [["Parakarry"]], "mapchange": False},
]

edges_mac_add_storeroom_without_key_hammer = [
    #* Residental District Exit Right -> ItemA (SnowmanDoll)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemA"}, "reqs": [["Hammer"]], "mapchange": False},
]

edges_mac_add_storeroom_without_key_hammerless_lure = [
    #* Residental District Exit Right -> ItemA (SnowmanDoll)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemA"}, "reqs": [], "mapchange": False},
]
