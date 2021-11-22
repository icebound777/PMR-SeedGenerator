from simulate import *

"""This file represents all edges of the world graph that have origin-nodes in the DRO (Dry Dry Outpost) area."""
edges_dro = [
    # DRO_01 Outpost 1
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "SBK_36", "id": 1}, "reqs": []}, # Outpost 1 Exit West -> E3 Outside Outpost Exit East
    {"from": {"map": "DRO_01", "id": 1}, "to": {"map": "DRO_02", "id": 0}, "reqs": []}, # Outpost 1 Exit East -> Outpost 2 Exit West
    {"from": {"map": "DRO_01", "id": 2}, "to": {"map": "TIK_01", "id": 4}, "reqs": []}, # Outpost 1 Blue Warp Pipe -> Warp Zone 1 (B1) Blue Warp Pipe (Left)
    
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": 1}, "reqs": []}, #? Outpost 1 Exit West -> Outpost 1 Exit East
    {"from": {"map": "DRO_01", "id": 1}, "to": {"map": "DRO_01", "id": 0}, "reqs": []}, #? Outpost 1 Exit East -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": 2}, "reqs": [require(flag="GF_DRO01_WarpPipe")]}, #? Outpost 1 Exit West -> Outpost 1 Blue Warp Pipe
    {"from": {"map": "DRO_01", "id": 2}, "to": {"map": "DRO_01", "id": 0}, "reqs": []}, #? Outpost 1 Blue Warp Pipe -> Outpost 1 Exit West
    
    {"from": {"map": "DRO_01", "id": 2}, "to": {"map": "DRO_01", "id": 2}, "reqs": [], "pseudoitems": ["GF_DRO01_WarpPipe"]}, #+ Outpost 1 Blue Warp Pipe
    
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "GiftA"},     "reqs": []}, #* Outpost 1 Exit West -> GiftA (Melody)
    {"from": {"map": "DRO_01", "id": "GiftA"},     "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* GiftA (Melody) -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "GiftB"},     "reqs": []}, #* Outpost 1 Exit West -> GiftB (RedJar)
    {"from": {"map": "DRO_01", "id": "GiftB"},     "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* GiftB (RedJar) -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemA"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemA (ThunderBolt)
    {"from": {"map": "DRO_01", "id": "ShopItemA"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemA (ThunderBolt) -> Outpost 1 Exit West
    # {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemB"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemB (DustyHammer)
    # {"from": {"map": "DRO_01", "id": "ShopItemB"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemB (DustyHammer) -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemC"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemC (HoneySyrup)
    {"from": {"map": "DRO_01", "id": "ShopItemC"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemC (HoneySyrup) -> Outpost 1 Exit West
    # {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemD"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemD (DriedShroom)
    # {"from": {"map": "DRO_01", "id": "ShopItemD"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemD (DriedShroom) -> Outpost 1 Exit West
    # {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemE"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemE (DriedPasta)
    # {"from": {"map": "DRO_01", "id": "ShopItemE"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemE (DriedPasta) -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemF"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemF (Mushroom)
    {"from": {"map": "DRO_01", "id": "ShopItemF"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemF (Mushroom) -> Outpost 1 Exit West
    
    # DRO_02 Outpost 2
    {"from": {"map": "DRO_02", "id": 0}, "to": {"map": "DRO_01", "id": 1}, "reqs": []}, # Outpost 2 Exit West -> Outpost 1 Exit East
    
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": "GiftA"},       "reqs": [require(flag="GF_HOS06_MerluvleeRequestedCrystalBall")]}, #* Outpost 2 Exit West -> GiftA (CrystalBall)
    {"from": {"map": "DRO_02", "id": "GiftA"},       "to": {"map": "DRO_02", "id": 0},             "reqs": []}, #* GiftA (CrystalBall) -> Outpost 2 Exit West
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": "GiftB"},       "reqs": []}, #* Outpost 2 Exit West -> GiftB (PulseStone)
    {"from": {"map": "DRO_02", "id": "GiftB"},       "to": {"map": "DRO_02", "id": 0},             "reqs": []}, #* GiftB (PulseStone) -> Outpost 2 Exit West
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": "HiddenPanel"}, "reqs": [can_flip_panels]}, #* Outpost 2 Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "DRO_02", "id": "HiddenPanel"}, "to": {"map": "DRO_02", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Outpost 2 Exit West
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": "ItemA"},       "reqs": []}, #* Outpost 2 Exit West -> ItemA (Letter08)
    {"from": {"map": "DRO_02", "id": "ItemA"},       "to": {"map": "DRO_02", "id": 0},             "reqs": []}, #* ItemA (Letter08) -> Outpost 2 Exit West
]