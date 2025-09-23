"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Clippy Boots (Stone and Metal Block Skip).
"""
edges_tik_add_clippy_boots_stone_block_skip = [
    #? Windy Path (B3) Green Pipe -> Windy Path (B3) Exit Left
    {"from": {"map": "TIK_23", "id": 1}, "to": {"map": "TIK_23", "id": 0}, "reqs": [["Lakilester"],["Boots"]], "mapchange": False},
]

edges_tik_add_clippy_boots_metal_block_skip = [
    #? Hall to Ultra Boots (B3) Exit Right -> Hall to Ultra Boots (B3) Exit Left
    {"from": {"map": "TIK_24", "id": 1}, "to": {"map": "TIK_24", "id": 0}, "reqs": [["Lakilester"],["Boots"]], "mapchange": False},
]
