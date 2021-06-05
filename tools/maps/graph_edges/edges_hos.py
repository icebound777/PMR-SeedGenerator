from simulate import *

"""This file represents all edges of the world graph that have origin-nodes in the HOS (Shooting Star Summit) area."""
edges_hos = [
    # HOS_00 Shooting Star Path
    {"from": {"map": "HOS_00", "id": 0}, "to": {"map": "OSR_01", "id": 1}, "reqs": []}, # Shooting Star Path Exit Left -> Ruined Castle Grounds Exit East
    {"from": {"map": "HOS_00", "id": 1}, "to": {"map": "HOS_01", "id": 0}, "reqs": []}, # Shooting Star Path Exit Top Right -> Shooting Star Summit Exit Bottom Left
    {"from": {"map": "HOS_00", "id": 2}, "to": {"map": "HOS_06", "id": 0}, "reqs": []}, # Shooting Star Path Exit Bottom Right -> Merluvlee's House Exit Left
    
    {"from": {"map": "HOS_00", "id": 0}, "to": {"map": "HOS_00", "id": 1}, "reqs": []}, #? Shooting Star Path Exit Left -> Shooting Star Path Exit Top Right
    {"from": {"map": "HOS_00", "id": 1}, "to": {"map": "HOS_00", "id": 0}, "reqs": []}, #? Shooting Star Path Exit Top Right -> Shooting Star Path Exit Left
    {"from": {"map": "HOS_00", "id": 0}, "to": {"map": "HOS_00", "id": 2}, "reqs": []}, #? Shooting Star Path Exit Left -> Shooting Star Path Exit Bottom Right
    {"from": {"map": "HOS_00", "id": 2}, "to": {"map": "HOS_00", "id": 0}, "reqs": []}, #? Shooting Star Path Exit Bottom Right -> Shooting Star Path Exit Left
    
    {"from": {"map": "HOS_00", "id": 0},             "to": {"map": "HOS_00", "id": "HiddenPanel"}, "reqs": [flip_panels]}, #* Shooting Star Path Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "HOS_00", "id": "HiddenPanel"}, "to": {"map": "HOS_00", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Shooting Star Path Exit Left

    # HOS_01 Shooting Star Summit
    {"from": {"map": "HOS_01", "id": 0}, "to": {"map": "HOS_00", "id": 1}, "reqs": []}, # Shooting Star Summit Exit Bottom Left -> Shooting Star Path Exit Top Right
    {"from": {"map": "HOS_01", "id": 1}, "to": {"map": "HOS_02", "id": 0}, "reqs": []}, # Shooting Star Summit Ride Up To Starway -> Star Way Ride Down To Summit
    
    {"from": {"map": "HOS_01", "id": 0}, "to": {"map": "HOS_01", "id": 1}, "reqs": [require(starspirits=7)]}, #? Shooting Star Summit Exit Bottom Left -> Shooting Star Summit Ride Up To Starway
    {"from": {"map": "HOS_01", "id": 1}, "to": {"map": "HOS_01", "id": 0}, "reqs": []}, #? Shooting Star Summit Ride Up To Starway -> Shooting Star Summit Exit Bottom Left
    
    {"from": {"map": "HOS_01", "id": 0},             "to": {"map": "HOS_01", "id": "HiddenPanel"}, "reqs": [flip_panels]}, #* Shooting Star Summit Exit Bottom Left -> HiddenPanel (StarPiece)
    {"from": {"map": "HOS_01", "id": "HiddenPanel"}, "to": {"map": "HOS_01", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Shooting Star Summit Exit Bottom Left
    {"from": {"map": "HOS_01", "id": 0},             "to": {"map": "HOS_01", "id": "ItemA"},       "reqs": []}, #* Shooting Star Summit Exit Bottom Left -> ItemA (StarPiece)
    {"from": {"map": "HOS_01", "id": "ItemA"},       "to": {"map": "HOS_01", "id": 0},             "reqs": []}, #* ItemA (StarPiece) -> Shooting Star Summit Exit Bottom Left

    # HOS_02 Star Way
    {"from": {"map": "HOS_02", "id": 0}, "to": {"map": "HOS_01", "id": 1}, "reqs": []}, # Star Way Ride Down To Summit -> Shooting Star Summit Ride Up To Starway
    {"from": {"map": "HOS_02", "id": 1}, "to": {"map": "HOS_03", "id": 0}, "reqs": []}, # Star Way Exit Top Right -> Star Haven Exit Bottom Left
    
    {"from": {"map": "HOS_02", "id": 0}, "to": {"map": "HOS_02", "id": 1}, "reqs": []}, #? Star Way Ride Down To Summit -> Star Way Exit Top Right
    {"from": {"map": "HOS_02", "id": 1}, "to": {"map": "HOS_02", "id": 0}, "reqs": []}, #? Star Way Exit Top Right -> Star Way Ride Down To Summit

    # HOS_03 Star Haven
    {"from": {"map": "HOS_03", "id": 0}, "to": {"map": "HOS_02", "id": 1}, "reqs": []}, # Star Haven Exit Bottom Left -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 1}, "to": {"map": "HOS_04", "id": 0}, "reqs": []}, # Star Haven Exit Top Right -> Outside the Sanctuary Exit Left
    
    {"from": {"map": "HOS_03", "id": 0}, "to": {"map": "HOS_03", "id": 1}, "reqs": []}, #? Star Haven Exit Bottom Left -> Star Haven Exit Top Right
    {"from": {"map": "HOS_03", "id": 1}, "to": {"map": "HOS_03", "id": 0}, "reqs": []}, #? Star Haven Exit Top Right -> Star Haven Exit Bottom Left
    
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemA"}, "reqs": []}, #* Star Haven Exit Bottom Left -> ShopItemA (StopWatch)
    {"from": {"map": "HOS_03", "id": "ShopItemA"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemA (StopWatch) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemB"}, "reqs": []}, #* Star Haven Exit Bottom Left -> ShopItemB (ShootingStar)
    {"from": {"map": "HOS_03", "id": "ShopItemB"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemB (ShootingStar) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemC"}, "reqs": []}, #* Star Haven Exit Bottom Left -> ShopItemC (SuperSoda)
    {"from": {"map": "HOS_03", "id": "ShopItemC"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemC (SuperSoda) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemD"}, "reqs": []}, #* Star Haven Exit Bottom Left -> ShopItemD (MapleSyrup)
    {"from": {"map": "HOS_03", "id": "ShopItemD"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemD (MapleSyrup) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemE"}, "reqs": []}, #* Star Haven Exit Bottom Left -> ShopItemE (LifeShroom)
    {"from": {"map": "HOS_03", "id": "ShopItemE"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemE (LifeShroom) -> Star Haven Exit Bottom Left
    {"from": {"map": "HOS_03", "id": 0},           "to": {"map": "HOS_03", "id": "ShopItemF"}, "reqs": []}, #* Star Haven Exit Bottom Left -> ShopItemF (SuperShroom)
    {"from": {"map": "HOS_03", "id": "ShopItemF"}, "to": {"map": "HOS_03", "id": 0},           "reqs": []}, #* ShopItemF (SuperShroom) -> Star Haven Exit Bottom Left

    # HOS_04 Outside the Sanctuary
    {"from": {"map": "HOS_04", "id": 0}, "to": {"map": "HOS_03", "id": 1}, "reqs": []}, # Outside the Sanctuary Exit Left -> Star Haven Exit Top Right
    {"from": {"map": "HOS_04", "id": 1}, "to": {"map": "HOS_05", "id": 0}, "reqs": []}, # Outside the Sanctuary Exit Right -> Star Sanctuary Exit Left
    
    {"from": {"map": "HOS_04", "id": 0}, "to": {"map": "HOS_04", "id": 1}, "reqs": []}, #? Outside the Sanctuary Exit Left -> Outside the Sanctuary Exit Right
    {"from": {"map": "HOS_04", "id": 1}, "to": {"map": "HOS_04", "id": 0}, "reqs": []}, #? Outside the Sanctuary Exit Right -> Outside the Sanctuary Exit Left

    # HOS_05 Star Sanctuary
    {"from": {"map": "HOS_05", "id": 0}, "to": {"map": "HOS_04", "id": 1}, "reqs": []}, # Star Sanctuary Exit Left -> Outside the Sanctuary Exit Right
    {"from": {"map": "HOS_05", "id": 1}, "to": {"map": "HOS_20", "id": 0}, "reqs": []}, # Star Sanctuary Fly Starship -> Riding Star Ship Scene Fly To Star Haven
    
    {"from": {"map": "HOS_05", "id": 0}, "to": {"map": "HOS_05", "id": 1}, "reqs": []}, #? Star Sanctuary Exit Left -> Star Sanctuary Fly Starship
    {"from": {"map": "HOS_05", "id": 1}, "to": {"map": "HOS_05", "id": 0}, "reqs": []}, #? Star Sanctuary Fly Starship -> Star Sanctuary Exit Left

    # HOS_06 Merluvlee's House
    {"from": {"map": "HOS_06", "id": 0}, "to": {"map": "HOS_00", "id": 2}, "reqs": []}, # Merluvlee's House Exit Left -> Shooting Star Path Exit Bottom Right
    
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "HiddenPanel"}, "reqs": [flip_panels]}, #* Merluvlee's House Exit Left -> HiddenPanel (StarPiece)
    {"from": {"map": "HOS_06", "id": "HiddenPanel"}, "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Merluvlee's House Exit Left
    {"from": {"map": "HOS_06", "id": 0},             "to": {"map": "HOS_06", "id": "GiftA"},       "reqs": [require(favor="FAVOR_CH2_3"), require(item="CrystalBall")]}, #* Merluvlee's House Exit Left -> GiftA (Autograph2)
    {"from": {"map": "HOS_06", "id": "GiftA"},       "to": {"map": "HOS_06", "id": 0},             "reqs": []}, #* GiftA (Autograph2) -> Merluvlee's House Exit Left
    
    {"from": {"map": "HOS_06", "id": 0}, "to": {"map": "HOS_06", "id": 0}, "reqs": [require(favor="FAVOR_CH2_3")], "pseudoitems": ["GF_HOS06_MerluvleeRequestedCrystalBall"]}, #+ Merluvlee's House Exit Left

    # HOS_20 Riding Star Ship Scene
    {"from": {"map": "HOS_20", "id": 0}, "to": {"map": "HOS_05", "id": 1}, "reqs": []}, # Riding Star Ship Scene Fly To Star Haven -> Star Sanctuary Fly Starship
    {"from": {"map": "HOS_20", "id": 2}, "to": {"map": "KPA_60", "id": 4}, "reqs": []}, # Riding Star Ship Scene Fly To Bowser's Castle -> Ship Enter/Exit Scenes Leave Hangar To Starhaven
    
    {"from": {"map": "HOS_20", "id": 0}, "to": {"map": "HOS_20", "id": 2}, "reqs": []}, #? Riding Star Ship Scene Fly To Star Haven -> Riding Star Ship Scene Fly To Bowser's Castle
    {"from": {"map": "HOS_20", "id": 2}, "to": {"map": "HOS_20", "id": 0}, "reqs": []}, #? Riding Star Ship Scene Fly To Bowser's Castle -> Riding Star Ship Scene Fly To Star Haven
]