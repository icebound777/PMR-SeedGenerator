"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Toad Town Sushie Glitch.
An additional partner is required to switch in battle and exit the sushie glitch
state.
"""
edges_mac_add_toad_town_sushie_glitch = [
    #? Gate District Exit Left -> Gate District Exit Right
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "MAC_00", "id": 1}, "reqs": [["Sushie"], ["can_end_sushie_glitch"]], "pseudoitems": ["RF_ToadTownSushieGlitch"], "mapchange": False},

    #? Goomba King's Castle Exit Right -> Goomba King's Castle Exit Left
    {"from": {"map": "KMR_11", "id": 1}, "to": {"map": "KMR_11", "id": 0}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},

    #? Goomba Village Exit Left -> Goomba Village Exit Right
    {"from": {"map": "KMR_02", "id": 1 },  "to": {"map": "KMR_02", "id": 0 },  "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
    #? Goomba Village Exit Right -> Goomba Village Exit Left
    {"from": {"map": "KMR_02", "id": 0 },  "to": {"map": "KMR_02", "id": 1 },  "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
    #? Toad Town Entrance Exit Right -> Toad Town Entrance Exit Left
    {"from": {"map": "KMR_10", "id": 1 },  "to": {"map": "KMR_10", "id": 0 },  "reqs": [["RF_PrologueSushieGlitch"]], "mapchange": False},

    #* Residental District Exit Right -> ItemA (SnowmanDoll)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemA"}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
    #* Residental District Exit Right -> ItemB (VoltShroom)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemB"}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
    #* Residental District Exit Right -> ItemC (ToyTrain)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemC"}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
    #* Residental District Exit Right -> ItemD (DizzyDial)
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": "ItemD"}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},

    #? Pleasant Path Bridge Exit Left -> Pleasant Path Bridge Exit Right
    {"from": {"map": "NOK_12", "id": 0}, "to": {"map": "NOK_12", "id": 1}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
    #? Pleasant Path Bridge Exit Right -> Pleasant Path Bridge Exit Left
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": 0}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},

    #* Pleasant Path Bridge Exit Right -> ItemA (StarPiece)
    {"from": {"map": "NOK_12", "id": 1}, "to": {"map": "NOK_12", "id": "ItemA"}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},

    #? Path to Fortress 1 Exit Left -> Path to Fortress 1 Exit Right
    {"from": {"map": "NOK_14", "id": 0}, "to": {"map": "NOK_14", "id": 1}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
    #? Path to Fortress 1 Exit Right -> Path to Fortress 1 Exit Left
    {"from": {"map": "NOK_14", "id": 1}, "to": {"map": "NOK_14", "id": 0}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},

    #? Exit to Gusty Gulch Exit West -> Exit to Gusty Gulch Exit East
    {"from": {"map": "MIM_12", "id": 0}, "to": {"map": "MIM_12", "id": 1}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
    #? Exit to Gusty Gulch Exit East -> Exit to Gusty Gulch Exit West
    {"from": {"map": "MIM_12", "id": 1}, "to": {"map": "MIM_12", "id": 0}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},

    #* Wasteland Ascent 1 Exit West -> ItemA (DizzyDial)
    {"from": {"map": "ARN_02", "id": 0}, "to": {"map": "ARN_02", "id": "ItemA"}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
    #? Wasteland Ascent 2 Exit West -> Wasteland Ascent 2 Exit East
    {"from": {"map": "ARN_04", "id": 0}, "to": {"map": "ARN_04", "id": 1}, "reqs": [["RF_ToadTownSushieGlitch"]], "mapchange": False},
]
