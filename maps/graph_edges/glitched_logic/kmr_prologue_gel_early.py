"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Prologue Gel Early.
"""
edges_kmr_add_prologue_gel_early = [
    #* Bottom of the Cliff Exit Right -> HiddenYBlockA (RepelGel)
    # getting on top of stone block and using any of kooper / bombette / parakarry / lakilester methods
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_03", "id": "HiddenYBlockA"}, "reqs": [["Kooper", "Bombette", "Parakarry", "Lakilester"],["Boots"]], "mapchange": False},

    # parakarry clip into stone block and hit with kooper jump
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_03", "id": "HiddenYBlockA"}, "reqs": [["Kooper"], ["Parakarry"]], "mapchange": False},

    # parakarry clip into stone block, laki jump on top, use bombette to hit repel gel block
    {"from": {"map": "KMR_03", "id": 1}, "to": {"map": "KMR_03", "id": "HiddenYBlockA"}, "reqs": [["Bombette"], ["Parakarry"], ["Lakilester"]], "mapchange": False}
]
