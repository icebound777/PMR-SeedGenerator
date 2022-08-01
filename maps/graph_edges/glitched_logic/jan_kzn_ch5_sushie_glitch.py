"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Chapter 5 Sushie Glitch.
An additional partner is required to switch in battle and exit the sushie glitch
state.
"""
edges_jan_kzn_add_ch5_sushie_glitch = [
    #? NE Jungle (Raven Statue) Exit Bottom -> NE Jungle (Raven Statue) Exit Top
    {"from": {"map": "JAN_06", "id": 0}, "to": {"map": "JAN_06", "id": 2}, "reqs": [["Sushie"], ["Goombario", "Kooper", "Bombette", "Parakarry", "Bow", "Watt", "Lakilester"]], "pseudoitems": ["RF_Ch5_SushieGlitch"], "mapchange": False},
    #? NE Jungle (Raven Statue) Exit Right -> NE Jungle (Raven Statue) Exit Left
    {"from": {"map": "JAN_06", "id": 1}, "to": {"map": "JAN_06", "id": 3}, "reqs": [["RF_Ch5_SushieGlitch"]]},
    #? Path to the Volcano Exit Left -> Path to the Volcano Exit Right
    {"from": {"map": "JAN_22", "id": 0}, "to": {"map": "JAN_22", "id": 2}, "reqs": [["RF_Ch5_SushieGlitch"]]}, 
    #? Path to the Volcano Exit Right -> Path to the Volcano Exit Left
    {"from": {"map": "JAN_22", "id": 2}, "to": {"map": "JAN_22", "id": 0}, "reqs": [["RF_Ch5_SushieGlitch"]]},

    #? Central Cavern Exit West Upper -> Central Cavern Exit East Lower 1 (Ultra Block) 
    {"from": {"map": "KZN_03", "id": 0}, "to": {"map": "KZN_03", "id": 2}, "reqs": [["RF_Ch5_SushieGlitch"]]}, 
    #? Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit West
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 1}, "reqs": [["RF_Ch5_SushieGlitch"]]}, 
    #? Flowing Lava Puzzle Exit West -> Flowing Lava Puzzle Exit East Upper
    {"from": {"map": "KZN_06", "id": 1}, "to": {"map": "KZN_06", "id": 0}, "reqs": [["RF_Ch5_SushieGlitch"]]}, 
    #? Flowing Lava Puzzle Exit East Upper -> Flowing Lava Puzzle Exit East Lower
    {"from": {"map": "KZN_06", "id": 0}, "to": {"map": "KZN_06", "id": 2}, "reqs": [["RF_Ch5_SushieGlitch"]]}, 
    #? Ultra Hammer Room Exit East -> BigChest (UltraHammer)
    {"from": {"map": "KZN_07", "id": 0}, "to": {"map": "KZN_07", "id": "BigChest"}, "reqs": [["RF_Ch5_SushieGlitch"]], "pseudoitems": ["RF_KZN07_OpenedHammerChest"]}, 
    #* Dizzy Stomp Room Exit West -> ChestA (DizzyStomp)
    {"from": {"map": "KZN_08", "id": 0}, "to": {"map": "KZN_08", "id": "ChestA"}, "reqs": [["RF_Ch5_SushieGlitch"]]}, 
    #? Spike Roller Trap Exit West -> Spike Roller Trap Exit East
    {"from": {"map": "KZN_17", "id": 0}, "to": {"map": "KZN_17", "id": 1}, "reqs": [["RF_Ch5_SushieGlitch"]]},

]
