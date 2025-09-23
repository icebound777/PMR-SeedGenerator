"""This file represents all edges of the world graph that have origin-nodes in the KGR (Inside the Whale) area."""
edges_kgr = [
    # KGR_01 Whale Mouth
    {"from": {"map": "KGR_01", "id": 0}, "to": {"map": "MAC_05", "id": 3}, "reqs": []}, # Whale Mouth Exit West -> Port District Enter Whale
    {"from": {"map": "KGR_01", "id": 1}, "to": {"map": "KGR_02", "id": 0}, "reqs": []}, # Whale Mouth Exit East -> Whale Stomach Exit West

    {"from": {"map": "KGR_01", "id": 0}, "to": {"map": "KGR_01", "id": 1}, "reqs": []}, #? Whale Mouth Exit West -> Whale Mouth Exit East
    {"from": {"map": "KGR_01", "id": 1}, "to": {"map": "KGR_01", "id": 0}, "reqs": []}, #? Whale Mouth Exit East -> Whale Mouth Exit West

    # KGR_02 Whale Stomach
    {"from": {"map": "KGR_02", "id": 0}, "to": {"map": "KGR_01", "id": 1}, "reqs": []}, # Whale Stomach Exit West -> Whale Mouth Exit East
    {"from": {"map": "KGR_02", "id": 0}, "to": {"map": "KGR_02", "id": 0}, "reqs": [["Watt"]], "pseudoitems":["RF_CanRideWhale"]}, #+ Defeat Fuzzipede
]
