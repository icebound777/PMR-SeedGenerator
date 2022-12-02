"""This file represents all edges of the world graph that have origin-nodes in the ARN (Gusty Gulch) area."""
edges_arn = [
    # ARN_02 Wasteland Ascent 1
    {"from": {"map": "ARN_02", "id": 0}, "to": {"map": "ARN_05", "id": 1}, "reqs": []}, # Wasteland Ascent 1 Exit West -> Ghost Town 2 Exit East
    {"from": {"map": "ARN_02", "id": 1}, "to": {"map": "ARN_04", "id": 0}, "reqs": []}, # Wasteland Ascent 1 Exit East -> Wasteland Ascent 2 Exit West

    {"from": {"map": "ARN_02", "id": 0}, "to": {"map": "ARN_02", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Wasteland Ascent 1 Exit West -> Wasteland Ascent 1 Exit East
    {"from": {"map": "ARN_02", "id": 1}, "to": {"map": "ARN_02", "id": 0}, "reqs": []}, #? Wasteland Ascent 1 Exit East -> Wasteland Ascent 1 Exit West

    {"from": {"map": "ARN_02", "id": 0},         "to": {"map": "ARN_02", "id": "ItemA"},   "reqs": [["Kooper"]]}, #* Wasteland Ascent 1 Exit West -> ItemA (DizzyDial)
    {"from": {"map": "ARN_02", "id": 0},         "to": {"map": "ARN_02", "id": "ItemB"},   "reqs": []}, #* Wasteland Ascent 1 Exit West -> ItemB (Letter07)
    {"from": {"map": "ARN_02", "id": 0},         "to": {"map": "ARN_02", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Wasteland Ascent 1 Exit West -> YBlockA (Coin)
    {"from": {"map": "ARN_02", "id": "YBlockA"}, "to": {"map": "ARN_02", "id": "YBlockB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockB (Coin)
    {"from": {"map": "ARN_02", "id": "YBlockA"}, "to": {"map": "ARN_02", "id": "YBlockC"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockC (RepelGel)

    # ARN_03 Ghost Town 1
    {"from": {"map": "ARN_03", "id": 0}, "to": {"map": "ARN_07", "id": 1}, "reqs": []}, # Ghost Town 1 Exit West -> Windmill Exterior Exit East
    {"from": {"map": "ARN_03", "id": 1}, "to": {"map": "ARN_05", "id": 0}, "reqs": []}, # Ghost Town 1 Exit East -> Ghost Town 2 Exit West

    {"from": {"map": "ARN_03", "id": 0}, "to": {"map": "ARN_03", "id": 1}, "reqs": []}, #? Ghost Town 1 Exit West -> Ghost Town 1 Exit East
    {"from": {"map": "ARN_03", "id": 1}, "to": {"map": "ARN_03", "id": 0}, "reqs": []}, #? Ghost Town 1 Exit East -> Ghost Town 1 Exit West

    {"from": {"map": "ARN_03", "id": 0}, "to": {"map": "ARN_03", "id": "GiftA"},   "reqs": [["FAVOR_7_01_active"]]}, #* Ghost Town 1 Exit West -> GiftA (KootPackage)
    {"from": {"map": "ARN_03", "id": 0}, "to": {"map": "ARN_03", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Ghost Town 1 Exit West -> YBlockA (Coin)

    # ARN_04 Wasteland Ascent 2
    {"from": {"map": "ARN_04", "id": 0}, "to": {"map": "ARN_02", "id": 1}, "reqs": []}, # Wasteland Ascent 2 Exit West -> Wasteland Ascent 1 Exit East
    {"from": {"map": "ARN_04", "id": 1}, "to": {"map": "DGB_00", "id": 0}, "reqs": []}, # Wasteland Ascent 2 Exit East -> Escape Scene Exit West

    {"from": {"map": "ARN_04", "id": 0}, "to": {"map": "ARN_04", "id": 1}, "reqs": [["Parakarry"]]}, #? Wasteland Ascent 2 Exit West -> Wasteland Ascent 2 Exit East
    {"from": {"map": "ARN_04", "id": 1}, "to": {"map": "ARN_04", "id": 0}, "reqs": []}, #? Wasteland Ascent 2 Exit East -> Wasteland Ascent 2 Exit West

    {"from": {"map": "ARN_04", "id": 1},         "to": {"map": "ARN_04", "id": "ItemA"},   "reqs": []}, #* Wasteland Ascent 2 Exit East -> ItemA (StarPiece)
    {"from": {"map": "ARN_04", "id": 1},         "to": {"map": "ARN_04", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Wasteland Ascent 2 Exit East -> YBlockA (SuperShroom)
    {"from": {"map": "ARN_04", "id": "YBlockA"}, "to": {"map": "ARN_04", "id": "YBlockB"}, "reqs": []}, #+ SHARED REQUIREMENTS -> YBlockB (Coin)

    # ARN_05 Ghost Town 2
    {"from": {"map": "ARN_05", "id": 0}, "to": {"map": "ARN_03", "id": 1}, "reqs": []}, # Ghost Town 2 Exit West -> Ghost Town 1 Exit East
    {"from": {"map": "ARN_05", "id": 1}, "to": {"map": "ARN_02", "id": 0}, "reqs": []}, # Ghost Town 2 Exit East -> Wasteland Ascent 1 Exit West

    {"from": {"map": "ARN_05", "id": 0}, "to": {"map": "ARN_05", "id": 1}, "reqs": []}, #? Ghost Town 2 Exit West -> Ghost Town 2 Exit East
    {"from": {"map": "ARN_05", "id": 1}, "to": {"map": "ARN_05", "id": 0}, "reqs": []}, #? Ghost Town 2 Exit East -> Ghost Town 2 Exit West

    # ARN_07 Windmill Exterior
    {"from": {"map": "ARN_07", "id": 0}, "to": {"map": "ARN_08", "id": 0}, "reqs": []}, # Windmill Exterior Enter Windmill -> Windmill Interior Exit Windmill
    {"from": {"map": "ARN_07", "id": 1}, "to": {"map": "ARN_03", "id": 0}, "reqs": []}, # Windmill Exterior Exit East -> Ghost Town 1 Exit West
    {"from": {"map": "ARN_07", "id": 2}, "to": {"map": "MIM_12", "id": 1}, "reqs": []}, # Windmill Exterior Exit West -> Exit to Gusty Gulch Exit East

    {"from": {"map": "ARN_07", "id": 1}, "to": {"map": "ARN_07", "id": 0}, "reqs": [["MysticalKey"]]}, #? Windmill Exterior Exit East -> Windmill Exterior Enter Windmill
    {"from": {"map": "ARN_07", "id": 0}, "to": {"map": "ARN_07", "id": 1}, "reqs": []}, #? Windmill Exterior Enter Windmill -> Windmill Exterior Exit East
    {"from": {"map": "ARN_07", "id": 1}, "to": {"map": "ARN_07", "id": 2}, "reqs": []}, #? Windmill Exterior Exit East -> Windmill Exterior Exit West
    {"from": {"map": "ARN_07", "id": 2}, "to": {"map": "ARN_07", "id": 1}, "reqs": []}, #? Windmill Exterior Exit West -> Windmill Exterior Exit East

    {"from": {"map": "ARN_07", "id": 0}, "to": {"map": "ARN_07", "id": 0}, "reqs": [["RF_Ch3_HeartFledFirstTunnel"]], "pseudoitems": ["STARSPIRIT_3"]}, #+ Windmill Exterior Enter Windmill

    # ARN_08 Windmill Interior
    {"from": {"map": "ARN_08", "id": 0}, "to": {"map": "ARN_07", "id": 0}, "reqs": []}, # Windmill Interior Exit Windmill -> Windmill Exterior Enter Windmill
    {"from": {"map": "ARN_08", "id": 1}, "to": {"map": "ARN_09", "id": 1}, "reqs": []}, # Windmill Interior Into Well -> Windmill Tunnel Entry Spring Exit

    {"from": {"map": "ARN_08", "id": 0}, "to": {"map": "ARN_08", "id": 1}, "reqs": [["SuperBoots"]]}, #? Windmill Interior Exit Windmill -> Windmill Interior Into Well
    {"from": {"map": "ARN_08", "id": 1}, "to": {"map": "ARN_08", "id": 0}, "reqs": []}, #? Windmill Interior Into Well -> Windmill Interior Exit Windmill

    # ARN_09 Windmill Tunnel Entry
    {"from": {"map": "ARN_09", "id": 0}, "to": {"map": "ARN_10", "id": 0}, "reqs": []}, # Windmill Tunnel Entry Exit East -> Tunnel 1 Exit West
    {"from": {"map": "ARN_09", "id": 1}, "to": {"map": "ARN_08", "id": 1}, "reqs": []}, # Windmill Tunnel Entry Spring Exit -> Windmill Interior Into Well

    {"from": {"map": "ARN_09", "id": 0}, "to": {"map": "ARN_09", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Windmill Tunnel Entry Exit East -> Windmill Tunnel Entry Spring Exit
    {"from": {"map": "ARN_09", "id": 1}, "to": {"map": "ARN_09", "id": 0}, "reqs": []}, #? Windmill Tunnel Entry Spring Exit -> Windmill Tunnel Entry Exit East

    # ARN_10 Tunnel 1
    {"from": {"map": "ARN_10", "id": 0}, "to": {"map": "ARN_09", "id": 0}, "reqs": []}, # Tunnel 1 Exit West -> Windmill Tunnel Entry Exit East
    {"from": {"map": "ARN_10", "id": 1}, "to": {"map": "ARN_12", "id": 0}, "reqs": []}, # Tunnel 1 Exit East -> Tunnel 2 Exit West

    {"from": {"map": "ARN_10", "id": 0}, "to": {"map": "ARN_10", "id": 1}, "reqs": []}, #? Tunnel 1 Exit West -> Tunnel 1 Exit East
    {"from": {"map": "ARN_10", "id": 1}, "to": {"map": "ARN_10", "id": 0}, "reqs": []}, #? Tunnel 1 Exit East -> Tunnel 1 Exit West

    # ARN_11 Tubba's Heart Chamber
    {"from": {"map": "ARN_11", "id": 0}, "to": {"map": "ARN_13", "id": 1}, "reqs": []}, # Tubba's Heart Chamber Exit West -> Tunnel 3 Exit East

    {"from": {"map": "ARN_11", "id": 0}, "to": {"map": "ARN_11", "id": 0}, "reqs": [], "pseudoitems": ["RF_Ch3_HeartFledFirstTunnel"]}, #+ Tubba's Heart Chamber Exit West

    # ARN_12 Tunnel 2
    {"from": {"map": "ARN_12", "id": 0}, "to": {"map": "ARN_10", "id": 1}, "reqs": []}, # Tunnel 2 Exit West -> Tunnel 1 Exit East
    {"from": {"map": "ARN_12", "id": 1}, "to": {"map": "ARN_13", "id": 0}, "reqs": []}, # Tunnel 2 Exit East -> Tunnel 3 Exit West

    {"from": {"map": "ARN_12", "id": 0}, "to": {"map": "ARN_12", "id": 1}, "reqs": []}, #? Tunnel 2 Exit West -> Tunnel 2 Exit East
    {"from": {"map": "ARN_12", "id": 1}, "to": {"map": "ARN_12", "id": 0}, "reqs": []}, #? Tunnel 2 Exit East -> Tunnel 2 Exit West

    # ARN_13 Tunnel 3
    {"from": {"map": "ARN_13", "id": 0}, "to": {"map": "ARN_12", "id": 1}, "reqs": []}, # Tunnel 3 Exit West -> Tunnel 2 Exit East
    {"from": {"map": "ARN_13", "id": 1}, "to": {"map": "ARN_11", "id": 0}, "reqs": []}, # Tunnel 3 Exit East -> Tubba's Heart Chamber Exit West

    {"from": {"map": "ARN_13", "id": 0}, "to": {"map": "ARN_13", "id": 1}, "reqs": []}, #? Tunnel 3 Exit West -> Tunnel 3 Exit East
    {"from": {"map": "ARN_13", "id": 1}, "to": {"map": "ARN_13", "id": 0}, "reqs": []}, #? Tunnel 3 Exit East -> Tunnel 3 Exit West
]
