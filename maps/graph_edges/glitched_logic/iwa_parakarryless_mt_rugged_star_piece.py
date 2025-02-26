"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Parakarry-less Mt.Rugged Star Piece.

Clippy version is part of this video: https://youtu.be/yLdXnkNiXPs
"""
edges_iwa_add_parakarryless_star_piece_laki = [
    #* Mt Rugged 4 Exit Bottom Right -> ItemB (StarPiece)
    # edges_iwa has ItemB -> rest of items on this platform
    {"from": {"map": "IWA_03", "id": 0}, "to": {"map": "IWA_03", "id": "ItemB"}, "reqs": [["Lakilester"],["can_climb_steps"]], "mapchange": False},
]

edges_iwa_add_parakarryless_star_piece_clippy = [
    #* Mt Rugged 4 Exit Bottom Right -> ItemB (StarPiece)
    # edges_iwa has ItemB -> rest of items on this platform
    {"from": {"map": "IWA_03", "id": 0}, "to": {"map": "IWA_03", "id": "ItemB"}, "reqs": [["Lakilester"]], "mapchange": False},
    #* Mt Rugged 4 Exit Bottom Right -> ChestA (DamageDodgeB)
    # edges_iwa has ChestA -> YBlockA / YBlockC, this is still possible with clippy and no jump
    {"from": {"map": "IWA_03", "id": 0}, "to": {"map": "IWA_03", "id": "ChestA"}, "reqs": [["Lakilester"]], "mapchange": False},
]
