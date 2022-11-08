"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Ultra Hammer Skip
"""
edges_kzn_add_ultra_hammer_skip = [
    #? Central Cavern Exit West Upper -> Central Cavern Exit East Lower 1 (Ultra Block)
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_03", "id": 2}, "reqs": [["Boots"]], "mapchange": False},
]

edges_kzn_add_ultra_hammer_skip_laki = [
    #? Central Cavern Exit East Upper -> Central Cavern Exit East Lower 1 (Ultra Block)
    {"from": {"map": "KZN_03", "id": 1}, "to": {"map": "KZN_03", "id": 2}, "reqs": [["Lakilester"]], "mapchange": False},
]

edges_kzn_add_ultra_hammer_skip_sushie = [
    #? Central Cavern Exit East Upper -> Central Cavern Exit East Lower 1 (Ultra Block)
    {"from": {"map": "KZN_03", "id": 1}, "to": {"map": "KZN_03", "id": 2}, "reqs": [["Sushie"], ["Goombario", "Kooper", "Bombette"], ["SuperBoots"], ["can_end_sushie_glitch"]], "pseudoitems": ["RF_Volcano_SushieGlitch"], "mapchange": False},
]
