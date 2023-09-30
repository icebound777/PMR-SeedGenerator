"""
This file represents edges of the world graph that have to be added
in the MAC region (Toad Town) for Shuffle Partner Upgrades.
"""
edges_mac_add_partnerupgrades = [
    #* Port District -> RandomBlockItemA (MultiCoinBlock)
    (0xA1010640, {"from": {"map": "MAC_05", "id": 0}, "to": {"map": "MAC_05", "id": "RandomBlockItemA"}, "reqs": [["Boots"]], "mapchange": False})
]
