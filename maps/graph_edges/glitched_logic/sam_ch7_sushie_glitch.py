"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Chapter 7 Sushie Glitch.
An additional partner is required to switch in battle and exit the sushie glitch
state.
"""
edges_sam_add_ch7_sushie_glitch = [
    #? Shiver City Pond Area Exit West -> Shiver City Pond Area Exit East
    {"from": {"map": "SAM_11", "id": 0}, "to": {"map": "SAM_11", "id": 1}, "reqs": [["RF_Ch7_MurderMysterySolved"], ["Sushie"], ["Bombette", "SuperBoots"], ["Goombario", "Kooper", "Bombette", "Parakarry", "Bow", "Watt", "Lakilester"]], "pseudoitems": ["RF_Ch7SushieGlitch"], "mapchange": False}, 
    
    #? Shiver Snowfield Exit West -> Shiver Snowfield Mountain Entrance
    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_04", "id": 2}, "reqs": [["RF_Ch7SushieGlitch"]], "mapchange": False},

    #? Shiver Mountain Hills Exit West -> Shiver Mountain Hills Exit East 
    {"from": {"map": "SAM_08", "id": 0}, "to": {"map": "SAM_08", "id": 1}, "reqs": [["RF_Ch7SushieGlitch"]], "mapchange": False}, 
]
