"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Knows Puzzle Solutions
"""
edges_global_knows_puzzle_solutions = [
    #+ ShopItemE 
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": 0}, "reqs": [["RF_MouserReturned"]], "pseudoitems": ["RF_CanMeetMoustafa"], "mapchange": False},
    #* Outpost 1 Exit West -> GiftB (KootRedJar)
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": "GiftB"}, "reqs": [["RF_MouserReturned"]], "mapchange": False}, 
    #? Stone Puzzle Room Exit Left -> Stone Puzzle Room Exit Hidden Stairway
    {"from": {"map": "ISK_11", "id": 0}, "to": {"map": "ISK_11", "id": 3}, "reqs": [["PyramidStone"],["DiamondStone"],["LunarStone"]], "pseudoitems": ["MB_Ch2_Spirit_ISK11_SolvedArtifactPuzzle"], "mapchange": False},
    #+ Solve Color Puzzle 
    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_08", "id": 0}, "reqs": [["Hammer"]], "pseudoitems": ["MF_Ch4_SolvedColorPuzzle"], "mapchange": False}, 
]
