"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Clippy Ledge Star Piece
A laki teleport and fall out of bounds can be used to get the fire flower east of
the playground in prologue: https://youtu.be/BgYnyoo-DFY
"""
edges_kmr_add_jumpless_fire_flower = [
    #* Bottom of the Cliff Exit Left -> ItemA (Coin)
    # the rest of the coins and fire flower are implicitly implied by edges_kmr
    {{"map": "KMR_03", "id": 0}, "to": {"map": "KMR_03", "id": "ItemA"}, "reqs": [["Lakilester"]]}, 
]
