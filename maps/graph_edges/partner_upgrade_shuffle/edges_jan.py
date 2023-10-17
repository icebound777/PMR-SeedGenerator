"""
This file represents edges of the world graph that have to be added
in the JAN region (Jade Jungle) for Shuffle Partner Upgrades.
"""
edges_jan_add_partnerupgrades = [
    #* SW Jungle (Super Block) Exit Top -> RandomBlockItemA (SuperBlock)
    (0xA1110840, {"from": {"map": "JAN_08", "id": 2}, "to": {"map": "JAN_08", "id": "RandomBlockItemA"}, "reqs": [["can_hit_floating_blocks"]], "mapchange": False})
]
