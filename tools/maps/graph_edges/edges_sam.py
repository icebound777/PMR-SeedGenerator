"""This file represents all edges of the world graph that have origin-nodes in the SAM (Shiver Mountain) area."""
edges_sam = [
    # SAM_01 Shiver City Mayor Area
    {"from": {"map": "SAM_01", "id": 0}, "to": {"map": "SAM_02", "id": 0}, "reqs": []}, # Shiver City Mayor Area Exit East -> Shiver City Center Exit West
    
    {"from": {"map": "SAM_01", "id": 0},             "to": {"map": "SAM_01", "id": "HiddenPanel"}, "reqs": []}, #* Shiver City Mayor Area Exit East -> HiddenPanel (StarPiece)
    {"from": {"map": "SAM_01", "id": "HiddenPanel"}, "to": {"map": "SAM_01", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Shiver City Mayor Area Exit East
    {"from": {"map": "SAM_01", "id": 0},             "to": {"map": "SAM_01", "id": "GiftA"},       "reqs": []}, #* Shiver City Mayor Area Exit East -> GiftA (Bucket)
    {"from": {"map": "SAM_01", "id": "GiftA"},       "to": {"map": "SAM_01", "id": 0},             "reqs": []}, #* GiftA (Bucket) -> Shiver City Mayor Area Exit East
    {"from": {"map": "SAM_01", "id": 0},             "to": {"map": "SAM_01", "id": "ChestA"},      "reqs": []}, #* Shiver City Mayor Area Exit East -> ChestA (AttackFXE)
    {"from": {"map": "SAM_01", "id": "ChestA"},      "to": {"map": "SAM_01", "id": 0},             "reqs": []}, #* ChestA (AttackFXE) -> Shiver City Mayor Area Exit East

    # SAM_02 Shiver City Center
    {"from": {"map": "SAM_02", "id": 0}, "to": {"map": "SAM_01", "id": 0}, "reqs": []}, # Shiver City Center Exit West -> Shiver City Mayor Area Exit East
    {"from": {"map": "SAM_02", "id": 1}, "to": {"map": "SAM_11", "id": 0}, "reqs": []}, # Shiver City Center Exit East -> Shiver City Pond Area Exit West
    {"from": {"map": "SAM_02", "id": 2}, "to": {"map": "TIK_17", "id": 1}, "reqs": []}, # Shiver City Center Pipe Entrance -> Frozen Room (B3) Green Pipe Right
    
    {"from": {"map": "SAM_02", "id": 0}, "to": {"map": "SAM_02", "id": 1}, "reqs": []}, #? Shiver City Center Exit West -> Shiver City Center Exit East
    {"from": {"map": "SAM_02", "id": 1}, "to": {"map": "SAM_02", "id": 0}, "reqs": []}, #? Shiver City Center Exit East -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0}, "to": {"map": "SAM_02", "id": 2}, "reqs": []}, #? Shiver City Center Exit West -> Shiver City Center Pipe Entrance
    {"from": {"map": "SAM_02", "id": 2}, "to": {"map": "SAM_02", "id": 0}, "reqs": []}, #? Shiver City Center Pipe Entrance -> Shiver City Center Exit West
    
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ItemA"},     "reqs": []}, #* Shiver City Center Exit West -> ItemA (IcedPotato)
    {"from": {"map": "SAM_02", "id": "ItemA"},     "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ItemA (IcedPotato) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ItemB"},     "reqs": []}, #* Shiver City Center Exit West -> ItemB (UltraShroom)
    {"from": {"map": "SAM_02", "id": "ItemB"},     "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ItemB (UltraShroom) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ItemC"},     "reqs": []}, #* Shiver City Center Exit West -> ItemC (Mushroom)
    {"from": {"map": "SAM_02", "id": "ItemC"},     "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ItemC (Mushroom) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ItemD"},     "reqs": []}, #* Shiver City Center Exit West -> ItemD (Mushroom)
    {"from": {"map": "SAM_02", "id": "ItemD"},     "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ItemD (Mushroom) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ItemE"},     "reqs": []}, #* Shiver City Center Exit West -> ItemE (Mushroom)
    {"from": {"map": "SAM_02", "id": "ItemE"},     "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ItemE (Mushroom) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ItemF"},     "reqs": []}, #* Shiver City Center Exit West -> ItemF (Mushroom)
    {"from": {"map": "SAM_02", "id": "ItemF"},     "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ItemF (Mushroom) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ShopItemA"}, "reqs": []}, #* Shiver City Center Exit West -> ShopItemA (DizzyDial)
    {"from": {"map": "SAM_02", "id": "ShopItemA"}, "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ShopItemA (DizzyDial) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ShopItemB"}, "reqs": []}, #* Shiver City Center Exit West -> ShopItemB (ShootingStar)
    {"from": {"map": "SAM_02", "id": "ShopItemB"}, "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ShopItemB (ShootingStar) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ShopItemC"}, "reqs": []}, #* Shiver City Center Exit West -> ShopItemC (SnowmanDoll)
    {"from": {"map": "SAM_02", "id": "ShopItemC"}, "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ShopItemC (SnowmanDoll) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ShopItemD"}, "reqs": []}, #* Shiver City Center Exit West -> ShopItemD (MapleSyrup)
    {"from": {"map": "SAM_02", "id": "ShopItemD"}, "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ShopItemD (MapleSyrup) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ShopItemE"}, "reqs": []}, #* Shiver City Center Exit West -> ShopItemE (LifeShroom)
    {"from": {"map": "SAM_02", "id": "ShopItemE"}, "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ShopItemE (LifeShroom) -> Shiver City Center Exit West
    {"from": {"map": "SAM_02", "id": 0},           "to": {"map": "SAM_02", "id": "ShopItemF"}, "reqs": []}, #* Shiver City Center Exit West -> ShopItemF (SuperShroom)
    {"from": {"map": "SAM_02", "id": "ShopItemF"}, "to": {"map": "SAM_02", "id": 0},           "reqs": []}, #* ShopItemF (SuperShroom) -> Shiver City Center Exit West

    # SAM_03 Road to Shiver Snowfield
    {"from": {"map": "SAM_03", "id": 0}, "to": {"map": "SAM_11", "id": 1}, "reqs": []}, # Road to Shiver Snowfield Exit West -> Shiver City Pond Area Exit East
    {"from": {"map": "SAM_03", "id": 1}, "to": {"map": "SAM_04", "id": 0}, "reqs": []}, # Road to Shiver Snowfield Exit East -> Shiver Snowfield Exit West
    
    {"from": {"map": "SAM_03", "id": 0}, "to": {"map": "SAM_03", "id": 1}, "reqs": []}, #? Road to Shiver Snowfield Exit West -> Road to Shiver Snowfield Exit East
    {"from": {"map": "SAM_03", "id": 1}, "to": {"map": "SAM_03", "id": 0}, "reqs": []}, #? Road to Shiver Snowfield Exit East -> Road to Shiver Snowfield Exit West

    # SAM_04 Shiver Snowfield
    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_03", "id": 1}, "reqs": []}, # Shiver Snowfield Exit West -> Road to Shiver Snowfield Exit East
    {"from": {"map": "SAM_04", "id": 1}, "to": {"map": "SAM_05", "id": 0}, "reqs": []}, # Shiver Snowfield Exit East -> Path to Starborn Valley Exit West
    {"from": {"map": "SAM_04", "id": 2}, "to": {"map": "SAM_07", "id": 0}, "reqs": []}, # Shiver Snowfield Mountain Entrance -> Shiver Mountain Passage Mountain Entrance
    
    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_04", "id": 1}, "reqs": []}, #? Shiver Snowfield Exit West -> Shiver Snowfield Exit East
    {"from": {"map": "SAM_04", "id": 1}, "to": {"map": "SAM_04", "id": 0}, "reqs": []}, #? Shiver Snowfield Exit East -> Shiver Snowfield Exit West
    {"from": {"map": "SAM_04", "id": 0}, "to": {"map": "SAM_04", "id": 2}, "reqs": []}, #? Shiver Snowfield Exit West -> Shiver Snowfield Mountain Entrance
    {"from": {"map": "SAM_04", "id": 2}, "to": {"map": "SAM_04", "id": 0}, "reqs": []}, #? Shiver Snowfield Mountain Entrance -> Shiver Snowfield Exit West
    
    {"from": {"map": "SAM_04", "id": 0},             "to": {"map": "SAM_04", "id": "HiddenPanel"}, "reqs": []}, #* Shiver Snowfield Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "SAM_04", "id": "HiddenPanel"}, "to": {"map": "SAM_04", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Shiver Snowfield Exit West
    {"from": {"map": "SAM_04", "id": 0},             "to": {"map": "SAM_04", "id": "ItemA"},       "reqs": []}, #* Shiver Snowfield Exit West -> ItemA (Letter05)
    {"from": {"map": "SAM_04", "id": "ItemA"},       "to": {"map": "SAM_04", "id": 0},             "reqs": []}, #* ItemA (Letter05) -> Shiver Snowfield Exit West
    {"from": {"map": "SAM_04", "id": 0},             "to": {"map": "SAM_04", "id": "ItemB"},       "reqs": []}, #* Shiver Snowfield Exit West -> ItemB (RepelGel)
    {"from": {"map": "SAM_04", "id": "ItemB"},       "to": {"map": "SAM_04", "id": 0},             "reqs": []}, #* ItemB (RepelGel) -> Shiver Snowfield Exit West

    # SAM_05 Path to Starborn Valley
    {"from": {"map": "SAM_05", "id": 0}, "to": {"map": "SAM_04", "id": 1}, "reqs": []}, # Path to Starborn Valley Exit West -> Shiver Snowfield Exit East
    {"from": {"map": "SAM_05", "id": 1}, "to": {"map": "SAM_06", "id": 0}, "reqs": []}, # Path to Starborn Valley Exit East -> Starborn Valley Town Entrance
    
    {"from": {"map": "SAM_05", "id": 0}, "to": {"map": "SAM_05", "id": 1}, "reqs": []}, #? Path to Starborn Valley Exit West -> Path to Starborn Valley Exit East
    {"from": {"map": "SAM_05", "id": 1}, "to": {"map": "SAM_05", "id": 0}, "reqs": []}, #? Path to Starborn Valley Exit East -> Path to Starborn Valley Exit West
    
    {"from": {"map": "SAM_05", "id": 0},               "to": {"map": "SAM_05", "id": "ItemA"},         "reqs": []}, #* Path to Starborn Valley Exit West -> ItemA (Letter06)
    {"from": {"map": "SAM_05", "id": "ItemA"},         "to": {"map": "SAM_05", "id": 0},               "reqs": []}, #* ItemA (Letter06) -> Path to Starborn Valley Exit West
    {"from": {"map": "SAM_05", "id": 0},               "to": {"map": "SAM_05", "id": "HiddenYBlockA"}, "reqs": []}, #* Path to Starborn Valley Exit West -> HiddenYBlockA (StopWatch)
    {"from": {"map": "SAM_05", "id": "HiddenYBlockA"}, "to": {"map": "SAM_05", "id": 0},               "reqs": []}, #* HiddenYBlockA (StopWatch) -> Path to Starborn Valley Exit West

    # SAM_06 Starborn Valley
    {"from": {"map": "SAM_06", "id": 0}, "to": {"map": "SAM_05", "id": 1}, "reqs": []}, # Starborn Valley Town Entrance -> Path to Starborn Valley Exit East
    
    {"from": {"map": "SAM_06", "id": 0},       "to": {"map": "SAM_06", "id": "GiftA"}, "reqs": []}, #* Starborn Valley Town Entrance -> GiftA (Scarf)
    {"from": {"map": "SAM_06", "id": "GiftA"}, "to": {"map": "SAM_06", "id": 0},       "reqs": []}, #* GiftA (Scarf) -> Starborn Valley Town Entrance

    # SAM_07 Shiver Mountain Passage
    {"from": {"map": "SAM_07", "id": 0}, "to": {"map": "SAM_04", "id": 2}, "reqs": []}, # Shiver Mountain Passage Mountain Entrance -> Shiver Snowfield Mountain Entrance
    {"from": {"map": "SAM_07", "id": 1}, "to": {"map": "SAM_08", "id": 0}, "reqs": []}, # Shiver Mountain Passage Exit East -> Shiver Mountain Hills Exit West
    
    {"from": {"map": "SAM_07", "id": 0}, "to": {"map": "SAM_07", "id": 1}, "reqs": []}, #? Shiver Mountain Passage Mountain Entrance -> Shiver Mountain Passage Exit East
    {"from": {"map": "SAM_07", "id": 1}, "to": {"map": "SAM_07", "id": 0}, "reqs": []}, #? Shiver Mountain Passage Exit East -> Shiver Mountain Passage Mountain Entrance
    
    {"from": {"map": "SAM_07", "id": 1},               "to": {"map": "SAM_07", "id": "HiddenYBlockA"}, "reqs": []}, #* Shiver Mountain Passage Exit East -> HiddenYBlockA (UltraShroom)
    {"from": {"map": "SAM_07", "id": "HiddenYBlockA"}, "to": {"map": "SAM_07", "id": 1},               "reqs": []}, #* HiddenYBlockA (UltraShroom) -> Shiver Mountain Passage Exit East

    # SAM_08 Shiver Mountain Hills
    {"from": {"map": "SAM_08", "id": 0}, "to": {"map": "SAM_07", "id": 1}, "reqs": []}, # Shiver Mountain Hills Exit West -> Shiver Mountain Passage Exit East
    {"from": {"map": "SAM_08", "id": 1}, "to": {"map": "SAM_09", "id": 0}, "reqs": []}, # Shiver Mountain Hills Exit East -> Shiver Mountain Tunnel Exit West
    
    {"from": {"map": "SAM_08", "id": 0}, "to": {"map": "SAM_08", "id": 1}, "reqs": []}, #? Shiver Mountain Hills Exit West -> Shiver Mountain Hills Exit East
    {"from": {"map": "SAM_08", "id": 1}, "to": {"map": "SAM_08", "id": 0}, "reqs": []}, #? Shiver Mountain Hills Exit East -> Shiver Mountain Hills Exit West

    {"from": {"map": "SAM_08", "id": 0},       "to": {"map": "SAM_08", "id": "ItemA"}, "reqs": []}, #* Shiver Mountain Hills Exit West -> ItemA (Pebble)
    {"from": {"map": "SAM_08", "id": "ItemA"}, "to": {"map": "SAM_08", "id": 0},       "reqs": []}, #* ItemA (Pebble) -> Shiver Mountain Hills Exit West

    # SAM_09 Shiver Mountain Tunnel
    {"from": {"map": "SAM_09", "id": 0}, "to": {"map": "SAM_08", "id": 1}, "reqs": []}, # Shiver Mountain Tunnel Exit West -> Shiver Mountain Hills Exit East
    {"from": {"map": "SAM_09", "id": 1}, "to": {"map": "SAM_10", "id": 0}, "reqs": []}, # Shiver Mountain Tunnel Exit East -> Shiver Mountain Peaks Exit West
    
    {"from": {"map": "SAM_09", "id": 0}, "to": {"map": "SAM_09", "id": 1}, "reqs": []}, #? Shiver Mountain Tunnel Exit West -> Shiver Mountain Tunnel Exit East
    {"from": {"map": "SAM_09", "id": 1}, "to": {"map": "SAM_09", "id": 0}, "reqs": []}, #? Shiver Mountain Tunnel Exit East -> Shiver Mountain Tunnel Exit West

    {"from": {"map": "SAM_09", "id": 0},       "to": {"map": "SAM_09", "id": "ItemA"}, "reqs": []}, #* Shiver Mountain Tunnel Exit West -> ItemA (ShootingStar)
    {"from": {"map": "SAM_09", "id": "ItemA"}, "to": {"map": "SAM_09", "id": 0}      , "reqs": []}, #* ItemA (ShootingStar) -> Shiver Mountain Tunnel Exit West
    {"from": {"map": "SAM_09", "id": 0},       "to": {"map": "SAM_09", "id": "ItemB"}, "reqs": []}, #* Shiver Mountain Tunnel Exit West -> ItemB (SnowmanDoll)
    {"from": {"map": "SAM_09", "id": "ItemB"}, "to": {"map": "SAM_09", "id": 0}      , "reqs": []}, #* ItemB (SnowmanDoll) -> Shiver Mountain Tunnel Exit West
    {"from": {"map": "SAM_09", "id": 0},       "to": {"map": "SAM_09", "id": "ItemC"}, "reqs": []}, #* Shiver Mountain Tunnel Exit West -> ItemC (ThunderRage)
    {"from": {"map": "SAM_09", "id": "ItemC"}, "to": {"map": "SAM_09", "id": 0}      , "reqs": []}, #* ItemC (ThunderRage) -> Shiver Mountain Tunnel Exit West
    
    # SAM_10 Shiver Mountain Peaks
    {"from": {"map": "SAM_10", "id": 0}, "to": {"map": "SAM_09", "id": 1}, "reqs": []}, # Shiver Mountain Peaks Exit West -> Shiver Mountain Tunnel Exit East
    {"from": {"map": "SAM_10", "id": 1}, "to": {"map": "PRA_01", "id": 0}, "reqs": []}, # Shiver Mountain Peaks Exit East -> Entrance Exit West
    {"from": {"map": "SAM_10", "id": 2}, "to": {"map": "SAM_12", "id": 0}, "reqs": []}, # Shiver Mountain Peaks Bombable Wall -> Merlar's Sanctuary Bombable Wall
    
    {"from": {"map": "SAM_10", "id": 0}, "to": {"map": "SAM_10", "id": 1}, "reqs": []}, #? Shiver Mountain Peaks Exit West -> Shiver Mountain Peaks Exit East
    {"from": {"map": "SAM_10", "id": 1}, "to": {"map": "SAM_10", "id": 0}, "reqs": []}, #? Shiver Mountain Peaks Exit East -> Shiver Mountain Peaks Exit West
    {"from": {"map": "SAM_10", "id": 0}, "to": {"map": "SAM_10", "id": 2}, "reqs": []}, #? Shiver Mountain Peaks Exit West -> Shiver Mountain Peaks Bombable Wall
    {"from": {"map": "SAM_10", "id": 2}, "to": {"map": "SAM_10", "id": 0}, "reqs": []}, #? Shiver Mountain Peaks Bombable Wall -> Shiver Mountain Peaks Exit West
    
    {"from": {"map": "SAM_10", "id": 0},         "to": {"map": "SAM_10", "id": "RBlockA"}, "reqs": []}, #* Shiver Mountain Peaks Exit West -> RBlockA (MegaJump)
    {"from": {"map": "SAM_10", "id": "RBlockA"}, "to": {"map": "SAM_10", "id": 0},         "reqs": []}, #* RBlockA (MegaJump) -> Shiver Mountain Peaks Exit West
    {"from": {"map": "SAM_10", "id": 0},         "to": {"map": "SAM_10", "id": "ItemA"},   "reqs": []}, #* Shiver Mountain Peaks Exit West -> ItemA (StarPiece)
    {"from": {"map": "SAM_10", "id": "ItemA"},   "to": {"map": "SAM_10", "id": 0},         "reqs": []}, #* ItemA (StarPiece) -> Shiver Mountain Peaks Exit West

    # SAM_11 Shiver City Pond Area
    {"from": {"map": "SAM_11", "id": 0}, "to": {"map": "SAM_02", "id": 1}, "reqs": []}, # Shiver City Pond Area Exit West -> Shiver City Center Exit East
    {"from": {"map": "SAM_11", "id": 1}, "to": {"map": "SAM_03", "id": 0}, "reqs": []}, # Shiver City Pond Area Exit East -> Road to Shiver Snowfield Exit West
    
    {"from": {"map": "SAM_11", "id": 0}, "to": {"map": "SAM_11", "id": 1}, "reqs": []}, #? Shiver City Pond Area Exit West -> Shiver City Pond Area Exit East
    {"from": {"map": "SAM_11", "id": 1}, "to": {"map": "SAM_11", "id": 0}, "reqs": []}, #? Shiver City Pond Area Exit East -> Shiver City Pond Area Exit West
    
    {"from": {"map": "SAM_11", "id": 0},       "to": {"map": "SAM_11", "id": "ItemA"}, "reqs": []}, #* Shiver City Pond Area Exit West -> ItemA (WarehouseKey)
    {"from": {"map": "SAM_11", "id": "ItemA"}, "to": {"map": "SAM_11", "id": 0},       "reqs": []}, #* ItemA (WarehouseKey) -> Shiver City Pond Area Exit West

    # SAM_12 Merlar's Sanctuary
    {"from": {"map": "SAM_12", "id": 0}, "to": {"map": "SAM_10", "id": 2}, "reqs": []}, # Merlar's Sanctuary Bombable Wall -> Shiver Mountain Peaks Bombable Wall

    {"from": {"map": "SAM_12", "id": 0},       "to": {"map": "SAM_12", "id": "ItemA"}, "reqs": []}, #* Merlar's Sanctuary Bombable Wall -> ItemA (StarStone)
    {"from": {"map": "SAM_12", "id": "ItemA"}, "to": {"map": "SAM_12", "id": 0},       "reqs": []}, #* ItemA (StarStone) -> Merlar's Sanctuary Bombable Wall
]