"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Sushie-less Jungle Starpiece and Letter
"""
edges_jan_add_sushieless_jungle_starpiece_and_letter_lzs = [
    #* Sushi Tree Exit Left -> ItemA (StarPiece)
    {"from": {"map": "JAN_04", "id": 0}, "to": {"map": "JAN_04", "id": "ItemA"}, "reqs": [["Boots"]], "mapchange": False},

    #* Sushi Tree Exit Left -> Tree2_Drop1A (Letter04)
    {"from": {"map": "JAN_04", "id": 0}, "to": {"map": "JAN_04", "id": "Tree2_Drop1A"}, "reqs": [["Boots"], ["can_shake_trees"]], "mapchange": False},
]
