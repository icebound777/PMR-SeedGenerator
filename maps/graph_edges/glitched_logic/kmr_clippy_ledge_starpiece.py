"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Clippy Ledge Star Piece
Can use clippy to go out of bounds for the tree and star piece as shown: https://youtu.be/cGPratiMYQs
"""
edges_kmr_add_clippy_ledge_starpiece = [
    #* Behind the Village Exit Right -> ItemA (StarPiece)
    {"from": {"map": "KMR_05", "id": 1}, "to": {"map": "KMR_05", "id": "ItemA"}, "reqs": [["Lakilester"]]}, 
    #* Behind the Village Exit Right -> Tree1_Drop1A (Coin)
    {"from": {"map": "KMR_05", "id": 1}, "to": {"map": "KMR_05", "id": "Tree1_Drop1A"}, "reqs": [["can_shake_trees"],["Lakilester"]]}, 
]
