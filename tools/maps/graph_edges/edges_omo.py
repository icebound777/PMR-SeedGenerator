import re
from rando_modules.simulate import *

"""This file represents all edges of the world graph that have origin-nodes in the OMO (Shy Guy's Toybox) area."""
edges_omo = [
    # OMO_01 BLU Large Playroom
    {"from": {"map": "OMO_01", "id": 0}, "to": {"map": "OMO_13", "id": 0}, "reqs": []}, # BLU Large Playroom Exit East -> BLU Anti-Guy Hall Exit West
    
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemA"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemA (Calculator)
    {"from": {"map": "OMO_01", "id": "ItemA"},         "to": {"map": "OMO_01", "id": 0},               "reqs": []}, #* ItemA (Calculator) -> BLU Large Playroom Exit East
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemB"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemB (MapleSyrup)
    {"from": {"map": "OMO_01", "id": "ItemB"},         "to": {"map": "OMO_01", "id": 0},               "reqs": []}, #* ItemB (MapleSyrup) -> BLU Large Playroom Exit East
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemC"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemC (CakeMix)
    {"from": {"map": "OMO_01", "id": "ItemC"},         "to": {"map": "OMO_01", "id": 0},               "reqs": []}, #* ItemC (CakeMix) -> BLU Large Playroom Exit East
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemD"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemD (CakeMix)
    {"from": {"map": "OMO_01", "id": "ItemD"},         "to": {"map": "OMO_01", "id": 0},               "reqs": []}, #* ItemD (CakeMix) -> BLU Large Playroom Exit East
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemE"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemE (Mushroom)
    {"from": {"map": "OMO_01", "id": "ItemE"},         "to": {"map": "OMO_01", "id": 0},               "reqs": []}, #* ItemE (Mushroom) -> BLU Large Playroom Exit East
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "ItemF"},         "reqs": []}, #* BLU Large Playroom Exit East -> ItemF (FireFLower)
    {"from": {"map": "OMO_01", "id": "ItemF"},         "to": {"map": "OMO_01", "id": 0},               "reqs": []}, #* ItemF (FireFLower) -> BLU Large Playroom Exit East
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt")]}, #* BLU Large Playroom Exit East -> HiddenYBlockA (Mystery)
    {"from": {"map": "OMO_01", "id": "HiddenYBlockA"}, "to": {"map": "OMO_01", "id": 0},               "reqs": []}, #* HiddenYBlockA (Mystery) -> BLU Large Playroom Exit East
    {"from": {"map": "OMO_01", "id": 0},               "to": {"map": "OMO_01", "id": "HiddenYBlockB"}, "reqs": [require(partner="Watt")]}, #* BLU Large Playroom Exit East -> HiddenYBlockB (FrightJar)
    {"from": {"map": "OMO_01", "id": "HiddenYBlockB"}, "to": {"map": "OMO_01", "id": 0},               "reqs": []}, #* HiddenYBlockB (FrightJar) -> BLU Large Playroom Exit East

    # OMO_02 RED Boss Barricade
    {"from": {"map": "OMO_02", "id": 0}, "to": {"map": "OMO_10", "id": 1}, "reqs": []}, # RED Boss Barricade Exit West -> RED Station Exit East
    {"from": {"map": "OMO_02", "id": 1}, "to": {"map": "OMO_14", "id": 0}, "reqs": []}, # RED Boss Barricade Exit East -> RED Boss Antechamber Exit West
    
    {"from": {"map": "OMO_02", "id": 0}, "to": {"map": "OMO_02", "id": 1}, "reqs": [require(partner="Bombette")]}, #? RED Boss Barricade Exit West -> RED Boss Barricade Exit East
    {"from": {"map": "OMO_02", "id": 1}, "to": {"map": "OMO_02", "id": 0}, "reqs": [require(partner="Bombette")]}, #? RED Boss Barricade Exit East -> RED Boss Barricade Exit West
    
    {"from": {"map": "OMO_02", "id": 1},               "to": {"map": "OMO_02", "id": "YBlockA"},       "reqs": []}, #* RED Boss Barricade Exit East -> YBlockA (SleepySheep)
    {"from": {"map": "OMO_02", "id": "YBlockA"},       "to": {"map": "OMO_02", "id": 1},               "reqs": []}, #* YBlockA (SleepySheep) -> RED Boss Barricade Exit East
    {"from": {"map": "OMO_02", "id": 1},               "to": {"map": "OMO_02", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt")]}, #* RED Boss Barricade Exit East -> HiddenYBlockA (Coin)
    {"from": {"map": "OMO_02", "id": "HiddenYBlockA"}, "to": {"map": "OMO_02", "id": 1},               "reqs": []}, #* HiddenYBlockA (Coin) -> RED Boss Barricade Exit East
    {"from": {"map": "OMO_02", "id": 1},               "to": {"map": "OMO_02", "id": "ItemA"},         "reqs": []}, #* RED Boss Barricade Exit East -> ItemA (ShootingStar)
    {"from": {"map": "OMO_02", "id": "ItemA"},         "to": {"map": "OMO_02", "id": 1},               "reqs": []}, #* ItemA (ShootingStar) -> RED Boss Barricade Exit East

    # OMO_03 BLU Station
    {"from": {"map": "OMO_03", "id": 0}, "to": {"map": "OMO_13", "id": 1}, "reqs": []}, # BLU Station Exit West -> BLU Anti-Guy Hall Exit East
    {"from": {"map": "OMO_03", "id": 1}, "to": {"map": "OMO_04", "id": 0}, "reqs": []}, # BLU Station Exit East -> BLU Block City Exit West
    {"from": {"map": "OMO_03", "id": 2}, "to": {"map": "OMO_10", "id": 3}, "reqs": []}, # BLU Station Ride Train West -> RED Station Ride Train East
    {"from": {"map": "OMO_03", "id": 3}, "to": {"map": "OMO_06", "id": 2}, "reqs": []}, # BLU Station Ride Train East -> PNK Station Ride Train West
    {"from": {"map": "OMO_03", "id": 4}, "to": {"map": "MAC_04", "id": 2}, "reqs": []}, # BLU Station Spring to Toad Town -> Residental District Toybox Spring
    
    {"from": {"map": "OMO_03", "id": 4}, "to": {"map": "OMO_03", "id": 0}, "reqs": []}, #? BLU Station Spring to Toad Town -> BLU Station Exit West
    {"from": {"map": "OMO_03", "id": 0}, "to": {"map": "OMO_03", "id": 4}, "reqs": []}, #? BLU Station Exit West -> BLU Station Spring to Toad Town
    {"from": {"map": "OMO_03", "id": 4}, "to": {"map": "OMO_03", "id": 1}, "reqs": []}, #? BLU Station Spring to Toad Town -> BLU Station Exit East
    {"from": {"map": "OMO_03", "id": 1}, "to": {"map": "OMO_03", "id": 4}, "reqs": []}, #? BLU Station Exit East -> BLU Station Spring to Toad Town
    {"from": {"map": "OMO_03", "id": 4}, "to": {"map": "OMO_03", "id": 2}, "reqs": [require(flag="MF_Ch4_ReturnedToyTrain"),require(flag="RF_BlueSwitchPulled")]}, #? BLU Station Spring to Toad Town -> BLU Station Ride Train West
    {"from": {"map": "OMO_03", "id": 2}, "to": {"map": "OMO_03", "id": 4}, "reqs": [], "pseudoitems": ["RF_BlueSwitchPulled"]}, #? BLU Station Ride Train West -> BLU Station Spring to Toad Town
    {"from": {"map": "OMO_03", "id": 4}, "to": {"map": "OMO_03", "id": 3}, "reqs": [require(flag="MF_Ch4_ReturnedToyTrain")]}, #? BLU Station Spring to Toad Town -> BLU Station Ride Train East
    {"from": {"map": "OMO_03", "id": 3}, "to": {"map": "OMO_03", "id": 4}, "reqs": []}, #? BLU Station Ride Train East -> BLU Station Spring to Toad Town
    
    {"from": {"map": "OMO_03", "id": 4},               "to": {"map": "OMO_03", "id": "HiddenPanel"},   "reqs": [can_flip_panels]}, #* BLU Station Spring to Toad Town -> HiddenPanel (StarPiece)
    {"from": {"map": "OMO_03", "id": "HiddenPanel"},   "to": {"map": "OMO_03", "id": 4},               "reqs": []}, #* HiddenPanel (StarPiece) -> BLU Station Spring to Toad Town
    {"from": {"map": "OMO_03", "id": 4},               "to": {"map": "OMO_03", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt")]}, #* BLU Station Spring to Toad Town -> HiddenYBlockA (StoneCap)
    {"from": {"map": "OMO_03", "id": "HiddenYBlockA"}, "to": {"map": "OMO_03", "id": 4},               "reqs": []}, #* HiddenYBlockA (StoneCap) -> BLU Station Spring to Toad Town

    # OMO_04 BLU Block City
    {"from": {"map": "OMO_04", "id": 0}, "to": {"map": "OMO_03", "id": 1}, "reqs": []}, # BLU Block City Exit West -> BLU Station Exit East
    
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemA"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemA (Mushroom)
    {"from": {"map": "OMO_04", "id": "ItemA"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemA (Mushroom) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ChestA"},  "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ChestA (StoreroomKey)
    {"from": {"map": "OMO_04", "id": "ChestA"},  "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ChestA (StoreroomKey) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "YBlockA"}, "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> YBlockA (Coin)
    {"from": {"map": "OMO_04", "id": "YBlockA"}, "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* YBlockA (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "YBlockB"}, "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> YBlockB (Coin)
    {"from": {"map": "OMO_04", "id": "YBlockB"}, "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* YBlockB (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "YBlockC"}, "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> YBlockC (ThunderBolt)
    {"from": {"map": "OMO_04", "id": "YBlockC"}, "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* YBlockC (ThunderBolt) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemB"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemB (Coin)
    {"from": {"map": "OMO_04", "id": "ItemB"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemB (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemC"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemC (Coin)
    {"from": {"map": "OMO_04", "id": "ItemC"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemC (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemD"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemD (Coin)
    {"from": {"map": "OMO_04", "id": "ItemD"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemD (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemE"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemE (Coin)
    {"from": {"map": "OMO_04", "id": "ItemE"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemE (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemF"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemF (Coin)
    {"from": {"map": "OMO_04", "id": "ItemF"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemF (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemG"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemG (Coin)
    {"from": {"map": "OMO_04", "id": "ItemG"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemG (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemH"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemH (Coin)
    {"from": {"map": "OMO_04", "id": "ItemH"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemH (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemI"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemI (Coin)
    {"from": {"map": "OMO_04", "id": "ItemI"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemI (Coin) -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemJ"},   "reqs": [require(hammer=0,boots=1),require(partner="Parakarry")]}, #* BLU Block City Exit West -> ItemJ (StarPiece) on building
    {"from": {"map": "OMO_04", "id": "ItemJ"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemJ (StarPiece) on building -> BLU Block City Exit West
    {"from": {"map": "OMO_04", "id": 0},         "to": {"map": "OMO_04", "id": "ItemK"},   "reqs": [require(hammer=0,boots=1)]}, #* BLU Block City Exit West -> ItemK (StarPiece)
    {"from": {"map": "OMO_04", "id": "ItemK"},   "to": {"map": "OMO_04", "id": 0},         "reqs": []}, #* ItemK (StarPiece) -> BLU Block City Exit West

    # OMO_05 PNK Gourmet Guy Crossing
    {"from": {"map": "OMO_05", "id": 0}, "to": {"map": "OMO_17", "id": 0}, "reqs": []}, # PNK Gourmet Guy Crossing Exit East (South) -> PNK Tracks Hallway Exit West (South)
    {"from": {"map": "OMO_05", "id": 1}, "to": {"map": "OMO_17", "id": 1}, "reqs": []}, # PNK Gourmet Guy Crossing Exit East (North) -> PNK Tracks Hallway Exit West (North)
    
    {"from": {"map": "OMO_05", "id": 0}, "to": {"map": "OMO_05", "id": 1}, "reqs": [require(flag="MF_Ch4_GaveCakeToGourmetGuy")]}, #? PNK Gourmet Guy Crossing Exit East (South) -> PNK Gourmet Guy Crossing Exit East (North)
    {"from": {"map": "OMO_05", "id": 1}, "to": {"map": "OMO_05", "id": 0}, "reqs": [require(flag="MF_Ch4_GaveCakeToGourmetGuy")]}, #? PNK Gourmet Guy Crossing Exit East (North) -> PNK Gourmet Guy Crossing Exit East (South)
    
    {"from": {"map": "OMO_05", "id": 0},               "to": {"map": "OMO_05", "id": "ItemA"},         "reqs": [require(flag="MF_Ch4_GaveCakeToGourmetGuy")]}, #* PNK Gourmet Guy Crossing Exit East (South) -> ItemA (Cookbook)
    {"from": {"map": "OMO_05", "id": "ItemA"},         "to": {"map": "OMO_05", "id": 0},               "reqs": []}, #* ItemA (Cookbook) -> PNK Gourmet Guy Crossing Exit East (South)
    {"from": {"map": "OMO_05", "id": 1},               "to": {"map": "OMO_05", "id": "YBlockA"},       "reqs": []}, #* PNK Gourmet Guy Crossing Exit East (North) -> YBlockA (Coin)
    {"from": {"map": "OMO_05", "id": "YBlockA"},       "to": {"map": "OMO_05", "id": 1},               "reqs": []}, #* YBlockA (Coin) -> PNK Gourmet Guy Crossing Exit East (North)
    {"from": {"map": "OMO_05", "id": 1},               "to": {"map": "OMO_05", "id": "YBlockB"},       "reqs": []}, #* PNK Gourmet Guy Crossing Exit East (North) -> YBlockB (Coin)
    {"from": {"map": "OMO_05", "id": "YBlockB"},       "to": {"map": "OMO_05", "id": 1},               "reqs": []}, #* YBlockB (Coin) -> PNK Gourmet Guy Crossing Exit East (North)
    {"from": {"map": "OMO_05", "id": 1},               "to": {"map": "OMO_05", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt")]}, #* PNK Gourmet Guy Crossing Exit East (North) -> HiddenYBlockA (DizzyDial)
    {"from": {"map": "OMO_05", "id": "HiddenYBlockA"}, "to": {"map": "OMO_05", "id": 1},               "reqs": []}, #* HiddenYBlockA (DizzyDial) -> PNK Gourmet Guy Crossing Exit East (North)
    {"from": {"map": "OMO_05", "id": 1},               "to": {"map": "OMO_05", "id": "HiddenYBlockB"}, "reqs": [require(partner="Watt")]}, #* PNK Gourmet Guy Crossing Exit East (North) -> HiddenYBlockB (SuperSoda)
    {"from": {"map": "OMO_05", "id": "HiddenYBlockB"}, "to": {"map": "OMO_05", "id": 1},               "reqs": []}, #* HiddenYBlockB (SuperSoda) -> PNK Gourmet Guy Crossing Exit East (North)

    {"from": {"map": "OMO_05", "id": 0}, "to": {"map": "OMO_05", "id": 0}, "reqs": [require(item="Cake")], "pseudoitems": ["MF_Ch4_GaveCakeToGourmetGuy"]}, #+ Give Cake to Gourmet Guy

    # OMO_06 PNK Station
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_17", "id": 2}, "reqs": []}, # PNK Station Exit West -> PNK Tracks Hallway Exit East (South)
    {"from": {"map": "OMO_06", "id": 1}, "to": {"map": "OMO_17", "id": 3}, "reqs": []}, # PNK Station Exit West (Switch Area) -> PNK Tracks Hallway Exit East (North)
    {"from": {"map": "OMO_06", "id": 2}, "to": {"map": "OMO_03", "id": 3}, "reqs": []}, # PNK Station Ride Train West -> BLU Station Ride Train East
    {"from": {"map": "OMO_06", "id": 3}, "to": {"map": "OMO_08", "id": 1}, "reqs": []}, # PNK Station Ride Train East -> GRN Station Ride Train West
    {"from": {"map": "OMO_06", "id": 4}, "to": {"map": "OMO_07", "id": 0}, "reqs": []}, # PNK Station Exit East -> PNK Playhouse Exit West
    
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": 2}, "reqs": []}, #? PNK Station Exit West -> PNK Station Ride Train West
    {"from": {"map": "OMO_06", "id": 2}, "to": {"map": "OMO_06", "id": 0}, "reqs": []}, #? PNK Station Ride Train West -> PNK Station Exit West
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": 3}, "reqs": [require(flag="MF_Ch4_PulledPinkSwitch")]}, #? PNK Station Exit West -> PNK Station Ride Train East
    {"from": {"map": "OMO_06", "id": 3}, "to": {"map": "OMO_06", "id": 0}, "reqs": []}, #? PNK Station Ride Train East -> PNK Station Exit West
    {"from": {"map": "OMO_06", "id": 0}, "to": {"map": "OMO_06", "id": 4}, "reqs": []}, #? PNK Station Exit West -> PNK Station Exit East
    {"from": {"map": "OMO_06", "id": 4}, "to": {"map": "OMO_06", "id": 0}, "reqs": []}, #? PNK Station Exit East -> PNK Station Exit West
    
    {"from": {"map": "OMO_06", "id": 0},               "to": {"map": "OMO_06", "id": "HiddenPanel"},   "reqs": [can_flip_panels]}, #* PNK Station Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "OMO_06", "id": "HiddenPanel"},   "to": {"map": "OMO_06", "id": 0},               "reqs": []}, #* HiddenPanel (StarPiece) -> PNK Station Exit West
    {"from": {"map": "OMO_06", "id": 0},               "to": {"map": "OMO_06", "id": "ChestA"},        "reqs": []}, #* PNK Station Exit West -> ChestA (Mailbag)
    {"from": {"map": "OMO_06", "id": "ChestA"},        "to": {"map": "OMO_06", "id": 0},               "reqs": []}, #* ChestA (Mailbag) -> PNK Station Exit West
    {"from": {"map": "OMO_06", "id": 1},               "to": {"map": "OMO_06", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt")]}, #* PNK Station Exit West (Switch Area) -> HiddenYBlockA (ThunderRage)
    {"from": {"map": "OMO_06", "id": "HiddenYBlockA"}, "to": {"map": "OMO_06", "id": 1},               "reqs": []}, #* HiddenYBlockA (ThunderRage) -> PNK Station Exit West (Switch Area)

    {"from": {"map": "OMO_06", "id": 1}, "to": {"map": "OMO_06", "id": 1}, "reqs": [], "pseudoitems": ["MF_Ch4_PulledPinkSwitch"]}, #+ Pull pink switch

    # OMO_07 PNK Playhouse
    {"from": {"map": "OMO_07", "id": 0}, "to": {"map": "OMO_06", "id": 4}, "reqs": []}, # PNK Playhouse Exit West -> PNK Station Exit East
    
    {"from": {"map": "OMO_07", "id": 0},         "to": {"map": "OMO_07", "id": "ItemA"},   "reqs": [require(hammer=0,boots=1)]}, #* PNK Playhouse Exit West -> ItemA (ThunderRage)
    {"from": {"map": "OMO_07", "id": "ItemA"},   "to": {"map": "OMO_07", "id": 0},         "reqs": []}, #* ItemA (ThunderRage) -> PNK Playhouse Exit West
    {"from": {"map": "OMO_07", "id": 0},         "to": {"map": "OMO_07", "id": "ChestA"},  "reqs": [require(hammer=0,boots=1)]}, #* PNK Playhouse Exit West -> ChestA (FryingPan)
    {"from": {"map": "OMO_07", "id": "ChestA"},  "to": {"map": "OMO_07", "id": 0},         "reqs": []}, #* ChestA (FryingPan) -> PNK Playhouse Exit West
    {"from": {"map": "OMO_07", "id": 0},         "to": {"map": "OMO_07", "id": "ChestB"},  "reqs": [require(hammer=0,boots=1)]}, #* PNK Playhouse Exit West -> ChestB (DefendPlusA)
    {"from": {"map": "OMO_07", "id": "ChestB"},  "to": {"map": "OMO_07", "id": 0},         "reqs": []}, #* ChestB (DefendPlusA) -> PNK Playhouse Exit West
    {"from": {"map": "OMO_07", "id": 0},         "to": {"map": "OMO_07", "id": "ChestC"},  "reqs": [require(hammer=0,boots=1)]}, #* PNK Playhouse Exit West -> ChestC (IcePower)
    {"from": {"map": "OMO_07", "id": "ChestC"},  "to": {"map": "OMO_07", "id": 0},         "reqs": []}, #* ChestC (IcePower) -> PNK Playhouse Exit West
    {"from": {"map": "OMO_07", "id": 0},         "to": {"map": "OMO_07", "id": "YBlockA"}, "reqs": [require(hammer=0,boots=1)]}, #* PNK Playhouse Exit West -> YBlockA (Coin)
    {"from": {"map": "OMO_07", "id": "YBlockA"}, "to": {"map": "OMO_07", "id": 0},         "reqs": []}, #* YBlockA (Coin) -> PNK Playhouse Exit West

    # OMO_08 GRN Station
    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_09", "id": 0}, "reqs": []}, # GRN Station Exit East -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_08", "id": 1}, "to": {"map": "OMO_06", "id": 3}, "reqs": []}, # GRN Station Ride Train West -> PNK Station Ride Train East
    {"from": {"map": "OMO_08", "id": 2}, "to": {"map": "OMO_10", "id": 2}, "reqs": []}, # GRN Station Ride Train East -> RED Station Ride Train West
    
    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_08", "id": 1}, "reqs": []}, #? GRN Station Exit East -> GRN Station Ride Train West
    {"from": {"map": "OMO_08", "id": 1}, "to": {"map": "OMO_08", "id": 0}, "reqs": []}, #? GRN Station Ride Train West -> GRN Station Exit East
    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_08", "id": 2}, "reqs": [require(flag="MF_Ch4_SolvedColorPuzzle")]}, #? GRN Station Exit East -> GRN Station Ride Train East
    {"from": {"map": "OMO_08", "id": 2}, "to": {"map": "OMO_08", "id": 0}, "reqs": []}, #? GRN Station Ride Train East -> GRN Station Exit East
    
    {"from": {"map": "OMO_08", "id": 0},               "to": {"map": "OMO_08", "id": "HiddenPanel"},   "reqs": [can_flip_panels]}, #* GRN Station Exit East -> HiddenPanel (StarPiece)
    {"from": {"map": "OMO_08", "id": "HiddenPanel"},   "to": {"map": "OMO_08", "id": 0},               "reqs": []}, #* HiddenPanel (StarPiece) -> GRN Station Exit East
    {"from": {"map": "OMO_08", "id": 0},               "to": {"map": "OMO_08", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt")]}, #* GRN Station Exit East -> HiddenYBlockA (FireFlower)
    {"from": {"map": "OMO_08", "id": "HiddenYBlockA"}, "to": {"map": "OMO_08", "id": 0},               "reqs": []}, #* HiddenYBlockA (FireFlower) -> GRN Station Exit East

    {"from": {"map": "OMO_08", "id": 0}, "to": {"map": "OMO_08", "id": 0}, "reqs": [require(flag="RF_CanSolveColorPuzzle")], "pseudoitems": ["MF_Ch4_SolvedColorPuzzle"]}, #+ Solve Color Puzzle

    # OMO_09 GRN Treadmills/Slot Machine
    {"from": {"map": "OMO_09", "id": 0}, "to": {"map": "OMO_08", "id": 0}, "reqs": []}, # GRN Treadmills/Slot Machine Exit West -> GRN Station Exit East
    
    {"from": {"map": "OMO_09", "id": 0},        "to": {"map": "OMO_09", "id": "ItemA"},  "reqs": [require(partner="Bow"),require(partner="Parakarry")]}, #* GRN Treadmills/Slot Machine Exit West -> ItemA (SuperSoda)
    {"from": {"map": "OMO_09", "id": "ItemA"},  "to": {"map": "OMO_09", "id": 0},        "reqs": []}, #* ItemA (SuperSoda) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},        "to": {"map": "OMO_09", "id": "ChestA"}, "reqs": [require(partner="Bow"),require(partner="Parakarry")]}, #* GRN Treadmills/Slot Machine Exit West -> ChestA (Dictionary)
    {"from": {"map": "OMO_09", "id": "ChestA"}, "to": {"map": "OMO_09", "id": 0},        "reqs": []}, #* ChestA (Dictionary) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},        "to": {"map": "OMO_09", "id": "ItemH"},  "reqs": [require(partner="Bow")]}, #* GRN Treadmills/Slot Machine Exit West -> ItemH (StarPiece)
    {"from": {"map": "OMO_09", "id": "ItemH"},  "to": {"map": "OMO_09", "id": 0},        "reqs": []}, #* ItemH (StarPiece) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},        "to": {"map": "OMO_09", "id": "ItemO"},  "reqs": [require(partner="Bow")]}, #* GRN Treadmills/Slot Machine Exit West -> ItemO (MysteryNote)
    {"from": {"map": "OMO_09", "id": "ItemO"},  "to": {"map": "OMO_09", "id": 0},        "reqs": []}, #* ItemO (MysteryNote) -> GRN Treadmills/Slot Machine Exit West
    # Treadmill Coins
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemB"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemB (Coin)
    {"from": {"map": "OMO_09", "id": "ItemB"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemB (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemC"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemC (Coin)
    {"from": {"map": "OMO_09", "id": "ItemC"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemC (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemD"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemD (Coin)
    {"from": {"map": "OMO_09", "id": "ItemD"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemD (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemE"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemE (Coin)
    {"from": {"map": "OMO_09", "id": "ItemE"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemE (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemF"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemF (Coin)
    {"from": {"map": "OMO_09", "id": "ItemF"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemF (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemG"}, "reqs": []}, #* GRN Treadmills/Slot Machine Exit West -> ItemG (Coin)
    {"from": {"map": "OMO_09", "id": "ItemG"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemG (Coin) -> GRN Treadmills/Slot Machine Exit West
    # Starpiece Coins
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemI"}, "reqs": [require(partner="Bow")]}, #* GRN Treadmills/Slot Machine Exit West -> ItemI (Coin)
    {"from": {"map": "OMO_09", "id": "ItemI"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemI (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemJ"}, "reqs": [require(partner="Bow")]}, #* GRN Treadmills/Slot Machine Exit West -> ItemJ (Coin)
    {"from": {"map": "OMO_09", "id": "ItemJ"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemJ (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemK"}, "reqs": [require(partner="Bow")]}, #* GRN Treadmills/Slot Machine Exit West -> ItemK (Coin)
    {"from": {"map": "OMO_09", "id": "ItemK"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemK (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemL"}, "reqs": [require(partner="Bow")]}, #* GRN Treadmills/Slot Machine Exit West -> ItemL (Coin)
    {"from": {"map": "OMO_09", "id": "ItemL"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemL (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemM"}, "reqs": [require(partner="Bow")]}, #* GRN Treadmills/Slot Machine Exit West -> ItemM (Coin)
    {"from": {"map": "OMO_09", "id": "ItemM"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemM (Coin) -> GRN Treadmills/Slot Machine Exit West
    {"from": {"map": "OMO_09", "id": 0},       "to": {"map": "OMO_09", "id": "ItemN"}, "reqs": [require(partner="Bow")]}, #* GRN Treadmills/Slot Machine Exit West -> ItemN (Coin)
    {"from": {"map": "OMO_09", "id": "ItemN"}, "to": {"map": "OMO_09", "id": 0},       "reqs": []}, #* ItemN (Coin) -> GRN Treadmills/Slot Machine Exit West

    # OMO_10 RED Station
    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_11", "id": 1}, "reqs": []}, # RED Station Exit West -> RED Moving Platforms Exit East
    {"from": {"map": "OMO_10", "id": 1}, "to": {"map": "OMO_02", "id": 0}, "reqs": []}, # RED Station Exit East -> RED Boss Barricade Exit West
    {"from": {"map": "OMO_10", "id": 2}, "to": {"map": "OMO_08", "id": 2}, "reqs": []}, # RED Station Ride Train West -> GRN Station Ride Train East
    {"from": {"map": "OMO_10", "id": 3}, "to": {"map": "OMO_03", "id": 2}, "reqs": []}, # RED Station Ride Train East -> BLU Station Ride Train West
    
    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_10", "id": 1}, "reqs": []}, #? RED Station Exit West -> RED Station Exit East
    {"from": {"map": "OMO_10", "id": 1}, "to": {"map": "OMO_10", "id": 0}, "reqs": []}, #? RED Station Exit East -> RED Station Exit West
    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_10", "id": 2}, "reqs": []}, #? RED Station Exit West -> RED Station Ride Train West
    {"from": {"map": "OMO_10", "id": 2}, "to": {"map": "OMO_10", "id": 0}, "reqs": []}, #? RED Station Ride Train West -> RED Station Exit West
    {"from": {"map": "OMO_10", "id": 0}, "to": {"map": "OMO_10", "id": 3}, "reqs": []}, #? RED Station Exit West -> RED Station Ride Train East
    {"from": {"map": "OMO_10", "id": 3}, "to": {"map": "OMO_10", "id": 0}, "reqs": []}, #? RED Station Ride Train East -> RED Station Exit West
    
    {"from": {"map": "OMO_10", "id": 0},               "to": {"map": "OMO_10", "id": "HiddenPanel"},   "reqs": [can_flip_panels]}, #* RED Station Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "OMO_10", "id": "HiddenPanel"},   "to": {"map": "OMO_10", "id": 0},               "reqs": []}, #* HiddenPanel (StarPiece) -> RED Station Exit West
    {"from": {"map": "OMO_10", "id": 0},               "to": {"map": "OMO_10", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt")]}, #* RED Station Exit West -> HiddenYBlockA (SuperShroom)
    {"from": {"map": "OMO_10", "id": "HiddenYBlockA"}, "to": {"map": "OMO_10", "id": 0},               "reqs": []}, #* HiddenYBlockA (SuperShroom) -> RED Station Exit West

    # OMO_11 RED Moving Platforms
    {"from": {"map": "OMO_11", "id": 0}, "to": {"map": "OMO_12", "id": 0}, "reqs": []}, # RED Moving Platforms Exit West -> RED Lantern Ghost Exit East
    {"from": {"map": "OMO_11", "id": 1}, "to": {"map": "OMO_10", "id": 0}, "reqs": []}, # RED Moving Platforms Exit East -> RED Station Exit West
    
    {"from": {"map": "OMO_11", "id": 0}, "to": {"map": "OMO_11", "id": 1}, "reqs": []}, #? RED Moving Platforms Exit West -> RED Moving Platforms Exit East
    {"from": {"map": "OMO_11", "id": 1}, "to": {"map": "OMO_11", "id": 0}, "reqs": []}, #? RED Moving Platforms Exit East -> RED Moving Platforms Exit West
    
    {"from": {"map": "OMO_11", "id": 0},               "to": {"map": "OMO_11", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt")]}, #* RED Moving Platforms Exit West -> HiddenYBlockA (VoltShroom)
    {"from": {"map": "OMO_11", "id": "HiddenYBlockA"}, "to": {"map": "OMO_11", "id": 0},               "reqs": []}, #* HiddenYBlockA (VoltShroom) -> RED Moving Platforms Exit West
    {"from": {"map": "OMO_11", "id": 0},               "to": {"map": "OMO_11", "id": "HiddenYBlockB"}, "reqs": [require(partner="Watt")]}, #* RED Moving Platforms Exit West -> HiddenYBlockB (SnowmanDoll)
    {"from": {"map": "OMO_11", "id": "HiddenYBlockB"}, "to": {"map": "OMO_11", "id": 0},               "reqs": []}, #* HiddenYBlockB (SnowmanDoll) -> RED Moving Platforms Exit West
    {"from": {"map": "OMO_11", "id": 0},               "to": {"map": "OMO_11", "id": "YBlockA"},       "reqs": []}, #* RED Moving Platforms Exit West -> YBlockA (Coin)
    {"from": {"map": "OMO_11", "id": "YBlockA"},       "to": {"map": "OMO_11", "id": 0},               "reqs": []}, #* YBlockA (Coin) -> RED Moving Platforms Exit West
    {"from": {"map": "OMO_11", "id": 0},               "to": {"map": "OMO_11", "id": "YBlockB"},       "reqs": []}, #* RED Moving Platforms Exit West -> YBlockB (Coin)
    {"from": {"map": "OMO_11", "id": "YBlockB"},       "to": {"map": "OMO_11", "id": 0},               "reqs": []}, #* YBlockB (Coin) -> RED Moving Platforms Exit West
    {"from": {"map": "OMO_11", "id": 0},               "to": {"map": "OMO_11", "id": "HiddenRBlockA"}, "reqs": [require(partner="Watt")]}, #* RED Moving Platforms Exit West -> HiddenRBlockA (DeepFocus2)
    {"from": {"map": "OMO_11", "id": "HiddenRBlockA"}, "to": {"map": "OMO_11", "id": 0},               "reqs": []}, #* HiddenRBlockA (DeepFocus2) -> RED Moving Platforms Exit West

    # OMO_12 RED Lantern Ghost
    {"from": {"map": "OMO_12", "id": 0}, "to": {"map": "OMO_11", "id": 0}, "reqs": []}, # RED Lantern Ghost Exit East -> RED Moving Platforms Exit West

    {"from": {"map": "OMO_12", "id": 0},         "to": {"map": "OMO_12", "id": "Partner"}, "reqs": [require(flag="RF_CanGetWatt")]}, #* RED Lantern Ghost Exit East -> Partner (Watt)
    {"from": {"map": "OMO_12", "id": "Partner"}, "to": {"map": "OMO_12", "id": 0},         "reqs": []}, #* Partner (Watt) -> RED Lantern Ghost Exit East

    # OMO_13 BLU Anti-Guy Hall
    {"from": {"map": "OMO_13", "id": 0}, "to": {"map": "OMO_01", "id": 0}, "reqs": []}, # BLU Anti-Guy Hall Exit West -> BLU Large Playroom Exit East
    {"from": {"map": "OMO_13", "id": 1}, "to": {"map": "OMO_03", "id": 0}, "reqs": []}, # BLU Anti-Guy Hall Exit East -> BLU Station Exit West
    
    {"from": {"map": "OMO_13", "id": 0}, "to": {"map": "OMO_13", "id": 1}, "reqs": []}, #? BLU Anti-Guy Hall Exit West -> BLU Anti-Guy Hall Exit East
    {"from": {"map": "OMO_13", "id": 1}, "to": {"map": "OMO_13", "id": 0}, "reqs": []}, #? BLU Anti-Guy Hall Exit East -> BLU Anti-Guy Hall Exit West
    
    {"from": {"map": "OMO_13", "id": 0},               "to": {"map": "OMO_13", "id": "ChestA"},        "reqs": [require(flag="RF_CanVisitTayceT"),require(item="Lemon"),require(item="Cookbook"),require(item="CakeMix")]}, #* BLU Anti-Guy Hall Exit West -> ChestA (PowerPlusB)
    {"from": {"map": "OMO_13", "id": "ChestA"},        "to": {"map": "OMO_13", "id": 0},               "reqs": []}, #* ChestA (PowerPlusB) -> BLU Anti-Guy Hall Exit West
    {"from": {"map": "OMO_13", "id": 0},               "to": {"map": "OMO_13", "id": "YBlockA"},       "reqs": []}, #* BLU Anti-Guy Hall Exit West -> YBlockA (Coin)
    {"from": {"map": "OMO_13", "id": "YBlockA"},       "to": {"map": "OMO_13", "id": 0},               "reqs": []}, #* YBlockA (Coin) -> BLU Anti-Guy Hall Exit West
    {"from": {"map": "OMO_13", "id": 0},               "to": {"map": "OMO_13", "id": "HiddenYBlockA"}, "reqs": [require(partner="Watt")]}, #* BLU Anti-Guy Hall Exit West -> HiddenYBlockA (MapleSyrup)
    {"from": {"map": "OMO_13", "id": "HiddenYBlockA"}, "to": {"map": "OMO_13", "id": 0},               "reqs": []}, #* HiddenYBlockA (MapleSyrup) -> BLU Anti-Guy Hall Exit West

    # OMO_14 RED Boss Antechamber
    {"from": {"map": "OMO_14", "id": 0}, "to": {"map": "OMO_02", "id": 1}, "reqs": []}, # RED Boss Antechamber Exit West -> RED Boss Barricade Exit East
    {"from": {"map": "OMO_14", "id": 1}, "to": {"map": "OMO_15", "id": 0}, "reqs": []}, # RED Boss Antechamber Exit East -> RED General Guy Room Exit West
    
    {"from": {"map": "OMO_14", "id": 0}, "to": {"map": "OMO_14", "id": 1}, "reqs": [require(partner="Watt")]}, #? RED Boss Antechamber Exit West -> RED Boss Antechamber Exit East
    {"from": {"map": "OMO_14", "id": 1}, "to": {"map": "OMO_14", "id": 0}, "reqs": []}, #? RED Boss Antechamber Exit East -> RED Boss Antechamber Exit West

    # OMO_15 RED General Guy Room
    {"from": {"map": "OMO_15", "id": 0}, "to": {"map": "OMO_14", "id": 1}, "reqs": []}, # RED General Guy Room Exit West -> RED Boss Antechamber Exit East

    {"from": {"map": "OMO_15", "id": 0}, "to": {"map": "OMO_15", "id": 0}, "reqs": [], "pseudoitems": ["STARSPIRIT"]}, # RED General Guy Room Exit West -> RED Boss Antechamber Exit East

    # OMO_17 PNK Tracks Hallway
    {"from": {"map": "OMO_17", "id": 0}, "to": {"map": "OMO_05", "id": 0}, "reqs": []}, # PNK Tracks Hallway Exit West (South) -> PNK Gourmet Guy Crossing Exit East (South)
    {"from": {"map": "OMO_17", "id": 1}, "to": {"map": "OMO_05", "id": 1}, "reqs": []}, # PNK Tracks Hallway Exit West (North) -> PNK Gourmet Guy Crossing Exit East (North)
    {"from": {"map": "OMO_17", "id": 2}, "to": {"map": "OMO_06", "id": 0}, "reqs": []}, # PNK Tracks Hallway Exit East (South) -> PNK Station Exit West
    {"from": {"map": "OMO_17", "id": 3}, "to": {"map": "OMO_06", "id": 1}, "reqs": []}, # PNK Tracks Hallway Exit East (North) -> PNK Station Exit West (Switch Area)
    
    {"from": {"map": "OMO_17", "id": 0}, "to": {"map": "OMO_17", "id": 2}, "reqs": []}, #? PNK Tracks Hallway Exit West (South) -> PNK Tracks Hallway Exit East (South)
    {"from": {"map": "OMO_17", "id": 2}, "to": {"map": "OMO_17", "id": 0}, "reqs": []}, #? PNK Tracks Hallway Exit East (South) -> PNK Tracks Hallway Exit West (South)
    {"from": {"map": "OMO_17", "id": 1}, "to": {"map": "OMO_17", "id": 3}, "reqs": []}, #? PNK Tracks Hallway Exit West (North) -> PNK Tracks Hallway Exit East (North)
    {"from": {"map": "OMO_17", "id": 3}, "to": {"map": "OMO_17", "id": 1}, "reqs": []}, #? PNK Tracks Hallway Exit East (North) -> PNK Tracks Hallway Exit West (North)
    
    {"from": {"map": "OMO_17", "id": 0},         "to": {"map": "OMO_17", "id": "YBlockA"}, "reqs": []}, #* PNK Tracks Hallway Exit West (South) -> YBlockA (Coin)
    {"from": {"map": "OMO_17", "id": "YBlockA"}, "to": {"map": "OMO_17", "id": 0},         "reqs": []}, #* YBlockA (Coin) -> PNK Tracks Hallway Exit West (South)
    {"from": {"map": "OMO_17", "id": 1},         "to": {"map": "OMO_17", "id": "YBlockB"}, "reqs": []}, #* PNK Tracks Hallway Exit West (North) -> YBlockB (Coin)
    {"from": {"map": "OMO_17", "id": "YBlockB"}, "to": {"map": "OMO_17", "id": 1},         "reqs": []}, #* YBlockB (Coin) -> PNK Tracks Hallway Exit West (North)
    {"from": {"map": "OMO_17", "id": 1},         "to": {"map": "OMO_17", "id": "YBlockC"}, "reqs": []}, #* PNK Tracks Hallway Exit West (North) -> YBlockC (Coin)
    {"from": {"map": "OMO_17", "id": "YBlockC"}, "to": {"map": "OMO_17", "id": 1},         "reqs": []}, #* YBlockC (Coin) -> PNK Tracks Hallway Exit West (North)
]