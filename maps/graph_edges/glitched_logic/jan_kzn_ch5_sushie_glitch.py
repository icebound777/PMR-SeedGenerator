"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Chapter 5 Sushie Glitch.
An additional partner is required to switch in battle and exit the sushie glitch
state.
"""
edges_jan_kzn_add_ch5_sushie_glitch = [
    #? NE Jungle (Raven Statue) Exit Bottom -> NE Jungle (Raven Statue) Exit Top
    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_06", "id": 2}, "reqs": [["Sushie"], ["can_end_sushie_glitch"]], "pseudoitems": ["RF_Ch5_SushieGlitch"], "mapchange": False},
    #? NE Jungle (Raven Statue) Exit Right -> NE Jungle (Raven Statue) Exit Left
    {"from": {"map": "JAN_06", "id": 1}, "to": {"map": "JAN_06", "id": 3}, "reqs": [["RF_Ch5_SushieGlitch"]], "mapchange": False},
    #? Path to the Volcano Exit Left -> Path to the Volcano Exit Right
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 2}, "reqs": [["RF_Ch5_SushieGlitch"]], "mapchange": False},
    #? Path to the Volcano Exit Right -> Path to the Volcano Exit Left
    {"from": {"map": "JAN_22", "id": 2}, "to": {"map": "JAN_22", "id": 0}, "reqs": [["RF_Ch5_SushieGlitch"]], "mapchange": False},

    #? Central Cavern Exit West Upper -> Central Cavern Exit East Lower 1 (Ultra Block)
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_03", "id": 2}, "reqs": [["RF_Ch5_SushieGlitch"]], "mapchange": False},
    #? Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit West
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 1}, "reqs": [["RF_Ch5_SushieGlitch"]], "mapchange": False},
    #? Flowing Lava Puzzle Exit West -> Flowing Lava Puzzle Exit East Upper
    {"from": {"map": "KZN_06", "id": 1}, "to": {"map": "KZN_06", "id": 0}, "reqs": [["RF_Ch5_SushieGlitch"]], "mapchange": False},
    #? Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit East Lower
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 2}, "reqs": [["RF_Ch5_SushieGlitch"]], "mapchange": False},
    #? Ultra Hammer Room Exit East -> BigChest (UltraHammer)
    {"from": {"map": "KZN_07", "id": 0}, "to": {"map": "KZN_07", "id": "BigChest"}, "reqs": [["RF_Ch5_SushieGlitch"], ["can_climb_steps"]], "pseudoitems": ["RF_KZN07_OpenedHammerChest"], "mapchange": False},
    #* Dizzy Stomp Room Exit West -> ChestA (DizzyStomp)
    {"from": {"map": "KZN_08", "id": 0}, "to": {"map": "KZN_08", "id": "ChestA"}, "reqs": [["RF_Ch5_SushieGlitch"], ["can_climb_steps"]], "mapchange": False},
]

edges_kzn_add_volcano_sushie_glitch = [
    #? Central Cavern Exit West Upper -> Central Cavern Exit East Upper
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_03", "id": 1}, "reqs": [["Sushie"], ["Goombario", "Kooper", "Bombette"], ["SuperBoots"], ["can_end_sushie_glitch"]], "pseudoitems": ["RF_Volcano_SushieGlitch"], "mapchange": False},

    #? Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit West
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 1}, "reqs": [["RF_Volcano_SushieGlitch"]], "mapchange": False},
    #? Flowing Lava Puzzle Exit West -> Flowing Lava Puzzle Exit East Upper
    {"from": {"map": "KZN_06", "id": 1}, "to": {"map": "KZN_06", "id": 0}, "reqs": [["RF_Volcano_SushieGlitch"]], "mapchange": False},
    #? Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit East Lower
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 2}, "reqs": [["RF_Volcano_SushieGlitch"]], "mapchange": False},
    #? Ultra Hammer Room Exit East -> BigChest (UltraHammer)
    {"from": {"map": "KZN_07", "id": 0}, "to": {"map": "KZN_07", "id": "BigChest"}, "reqs": [["RF_Volcano_SushieGlitch"]], "pseudoitems": ["RF_KZN07_OpenedHammerChest"], "mapchange": False},
    #* Dizzy Stomp Room Exit West -> ChestA (DizzyStomp)
    {"from": {"map": "KZN_08", "id": 0}, "to": {"map": "KZN_08", "id": "ChestA"}, "reqs": [["RF_Volcano_SushieGlitch"]], "mapchange": False},
]
