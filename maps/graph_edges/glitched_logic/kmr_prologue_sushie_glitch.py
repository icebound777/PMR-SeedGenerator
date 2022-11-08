"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Prologue Sushie Glitch.
state.
"""

edges_kmr_add_prologue_sushie_glitch_common = [
    #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 1 },  "to": {"map": "KMR_02", "id": 0 },  "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},
    #? Goomba Village Exit Right -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 0 },  "to": {"map": "KMR_02", "id": 1 },  "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},

    #* Residental District Exit Right -> ItemA (SnowmanDoll)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemA"}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},
    #* Residental District Exit Right -> ItemB (VoltShroom)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemB"}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},
    #* Residental District Exit Right -> ItemC (ToyTrain)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemC"}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},
    #* Residental District Exit Right -> ItemD (DizzyDial)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemD"}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},

    #? Pleasant Path Bridge Exit Left -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": 1}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},
    #? Pleasant Path Bridge Exit Right -> Pleasant Path Bridge Exit Left
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": 0}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},

    #* Pleasant Path Bridge Exit Right -> ItemA (StarPiece)
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": "ItemA"}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},

    #? Path to Fortress 1 Exit Left -> Path to Fortress 1 Exit Right
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": 1}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},
    #? Path to Fortress 1 Exit Right -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_14", "id": 0}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},

    #? Exit to Gusty Gulch Exit West -> Exit to Gusty Gulch Exit East
    {"from": {"map": "MIM_12", "id": 0}, "to": {"map": "MIM_12", "id": 1}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},
    #? Exit to Gusty Gulch Exit East -> Exit to Gusty Gulch Exit West
    {"from": {"map": "MIM_12", "id": 1}, "to": {"map": "MIM_12", "id": 0}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},

    #* Wasteland Ascent 1 Exit West -> ItemA (DizzyDial)
    {"from": {"map": "ARN_02", "id": 0}, "to": {"map": "ARN_02", "id": "ItemA"}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},
    #? Wasteland Ascent 2 Exit West -> Wasteland Ascent 2 Exit East
    {"from": {"map": "ARN_04", "id": 0}, "to": {"map": "ARN_04", "id": 1}, "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},
]

edges_kmr_add_prologue_sushie_glitch_ksj = [
    # Jr. Troopa's Playground Exit Right -> Bottom of the Cliff Exit Left
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_03", "id": 0}, "reqs": [["Kooper"], ["Sushie"], ["SuperBoots"]], "pseudoitems": ["RF_PrologueSushieGlitch"], "mapchange": False},
]

edges_kmr_add_prologue_sushie_glitch_ultra_boots_laki = [
    # Jr. Troopa's Playground Exit Right -> Bottom of the Cliff Exit Left
    {"from": {"map": "KMR_04", "id": 0}, "to": {"map": "KMR_03", "id": 0}, "reqs": [["Goombario", "Kooper", "Bombette"], ["Lakilester"], ["Sushie"], ["UltraBoots"]], "pseudoitems": ["RF_PrologueSushieGlitch"], "mapchange": False},
]
