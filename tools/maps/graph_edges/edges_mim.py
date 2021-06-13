from simulate import *

"""This file represents all edges of the world graph that have origin-nodes in the MIM (Forever Forest) area."""
edges_mim = [
    # MIM_01 Flower Sounds
    {"from": {"map": "MIM_01", "id": 0}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 1
    {"from": {"map": "MIM_01", "id": 1}, "to": {"map": "MIM_10", "id": 1}, "reqs": []}, # Flower Sounds Forever Forest Entrance (Toad Town) -> Exit to Toad Town Entry to Forever Forest
    {"from": {"map": "MIM_01", "id": 2}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 2
    {"from": {"map": "MIM_01", "id": 3}, "to": {"map": "MIM_02", "id": 1}, "reqs": []}, # Flower Sounds Correct Exit -> Stump Eyes Wrong Exit (To Previous)
    
    {"from": {"map": "MIM_01", "id": 1}, "to": {"map": "MIM_01", "id": 0}, "reqs": []}, #? Flower Sounds Forever Forest Entrance (Toad Town) -> Get Lost In The Forest 1
    {"from": {"map": "MIM_01", "id": 0}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, #? Get Lost In The Forest 1 -> Flower Sounds Forever Forest Entrance (Toad Town)
    {"from": {"map": "MIM_01", "id": 1}, "to": {"map": "MIM_01", "id": 2}, "reqs": []}, #? Flower Sounds Forever Forest Entrance (Toad Town) -> Get Lost In The Forest 2
    {"from": {"map": "MIM_01", "id": 2}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, #? Get Lost In The Forest 2 -> Flower Sounds Forever Forest Entrance (Toad Town)
    {"from": {"map": "MIM_01", "id": 1}, "to": {"map": "MIM_01", "id": 3}, "reqs": []}, #? Flower Sounds Forever Forest Entrance (Toad Town) -> Flower Sounds Correct Exit
    {"from": {"map": "MIM_01", "id": 3}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, #? Flower Sounds Correct Exit -> Flower Sounds Forever Forest Entrance (Toad Town)

    # MIM_02 Stump Eyes
    {"from": {"map": "MIM_02", "id": 0}, "to": {"map": "MIM_03", "id": 2}, "reqs": []}, # Stump Eyes Correct Exit -> Flowers (Oaklie) Wrong Exit (To Previous)
    {"from": {"map": "MIM_02", "id": 1}, "to": {"map": "MIM_01", "id": 3}, "reqs": []}, # Stump Eyes Wrong Exit (To Previous) -> Flower Sounds Correct Exit
    {"from": {"map": "MIM_02", "id": 2}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 1
    {"from": {"map": "MIM_02", "id": 3}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 2
    
    {"from": {"map": "MIM_02", "id": 1}, "to": {"map": "MIM_02", "id": 0}, "reqs": []}, #? Stump Eyes Wrong Exit (To Previous) -> Stump Eyes Correct Exit
    {"from": {"map": "MIM_02", "id": 0}, "to": {"map": "MIM_02", "id": 1}, "reqs": []}, #? Stump Eyes Correct Exit -> Stump Eyes Wrong Exit (To Previous)
    {"from": {"map": "MIM_02", "id": 1}, "to": {"map": "MIM_02", "id": 2}, "reqs": []}, #? Stump Eyes Wrong Exit (To Previous) -> Get Lost In The Forest 1
    {"from": {"map": "MIM_02", "id": 2}, "to": {"map": "MIM_02", "id": 1}, "reqs": []}, #? Get Lost In The Forest 1 -> Stump Eyes Wrong Exit (To Previous)
    {"from": {"map": "MIM_02", "id": 1}, "to": {"map": "MIM_02", "id": 3}, "reqs": []}, #? Stump Eyes Wrong Exit (To Previous) -> Get Lost In The Forest 2
    {"from": {"map": "MIM_02", "id": 3}, "to": {"map": "MIM_02", "id": 1}, "reqs": []}, #? Get Lost In The Forest 2 -> Stump Eyes Wrong Exit (To Previous)

    # MIM_03 Flowers (Oaklie)
    {"from": {"map": "MIM_03", "id": 0}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 1
    {"from": {"map": "MIM_03", "id": 1}, "to": {"map": "MIM_04", "id": 3}, "reqs": []}, # Flowers (Oaklie) Correct Exit -> Tree Face (Bub-ulb) Wrong Exit (To Previous)
    {"from": {"map": "MIM_03", "id": 2}, "to": {"map": "MIM_02", "id": 0}, "reqs": []}, # Flowers (Oaklie) Wrong Exit (To Previous) -> Stump Eyes Correct Exit
    {"from": {"map": "MIM_03", "id": 3}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 2
    
    {"from": {"map": "MIM_03", "id": 2}, "to": {"map": "MIM_03", "id": 0}, "reqs": []}, #? Flowers (Oaklie) Wrong Exit (To Previous) -> Get Lost In The Forest 1
    {"from": {"map": "MIM_03", "id": 0}, "to": {"map": "MIM_03", "id": 2}, "reqs": []}, #? Get Lost In The Forest 1 -> Flowers (Oaklie) Wrong Exit (To Previous)
    {"from": {"map": "MIM_03", "id": 2}, "to": {"map": "MIM_03", "id": 1}, "reqs": []}, #? Flowers (Oaklie) Wrong Exit (To Previous) -> Flowers (Oaklie) Correct Exit
    {"from": {"map": "MIM_03", "id": 1}, "to": {"map": "MIM_03", "id": 2}, "reqs": []}, #? Flowers (Oaklie) Correct Exit -> Flowers (Oaklie) Wrong Exit (To Previous)
    {"from": {"map": "MIM_03", "id": 2}, "to": {"map": "MIM_03", "id": 3}, "reqs": []}, #? Flowers (Oaklie) Wrong Exit (To Previous) -> Get Lost In The Forest 2
    {"from": {"map": "MIM_03", "id": 3}, "to": {"map": "MIM_03", "id": 2}, "reqs": []}, #? Get Lost In The Forest 2 -> Flowers (Oaklie) Wrong Exit (To Previous)

    # MIM_04 Tree Face (Bub-ulb)
    {"from": {"map": "MIM_04", "id": 0}, "to": {"map": "MIM_05", "id": 2}, "reqs": []}, # Tree Face (Bub-ulb) Correct Exit -> MIM_05 Wrong Exit (To Previous)
    {"from": {"map": "MIM_04", "id": 1}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 1
    {"from": {"map": "MIM_04", "id": 2}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 2
    {"from": {"map": "MIM_04", "id": 3}, "to": {"map": "MIM_03", "id": 1}, "reqs": []}, # Tree Face (Bub-ulb) Wrong Exit (To Previous) -> Flowers (Oaklie) Correct Exit
    
    {"from": {"map": "MIM_04", "id": 3}, "to": {"map": "MIM_04", "id": 0}, "reqs": []}, #? Tree Face (Bub-ulb) Wrong Exit (To Previous) -> Tree Face (Bub-ulb) Correct Exit
    {"from": {"map": "MIM_04", "id": 0}, "to": {"map": "MIM_04", "id": 3}, "reqs": []}, #? Tree Face (Bub-ulb) Correct Exit -> Tree Face (Bub-ulb) Wrong Exit (To Previous)
    {"from": {"map": "MIM_04", "id": 3}, "to": {"map": "MIM_04", "id": 1}, "reqs": []}, #? Tree Face (Bub-ulb) Wrong Exit (To Previous) -> Get Lost In The Forest 1
    {"from": {"map": "MIM_04", "id": 1}, "to": {"map": "MIM_04", "id": 3}, "reqs": []}, #? Get Lost In The Forest 1 -> Tree Face (Bub-ulb) Wrong Exit (To Previous)
    {"from": {"map": "MIM_04", "id": 3}, "to": {"map": "MIM_04", "id": 2}, "reqs": []}, #? Tree Face (Bub-ulb) Wrong Exit (To Previous) -> Get Lost In The Forest 2
    {"from": {"map": "MIM_04", "id": 2}, "to": {"map": "MIM_04", "id": 3}, "reqs": []}, #? Get Lost In The Forest 2 -> Tree Face (Bub-ulb) Wrong Exit (To Previous)
    
    {"from": {"map": "MIM_04", "id": 3},       "to": {"map": "MIM_04", "id": "GiftA"}, "reqs": []}, #* Tree Face (Bub-ulb) Wrong Exit (To Previous) -> GiftA (MagicalSeed3)
    {"from": {"map": "MIM_04", "id": "GiftA"}, "to": {"map": "MIM_04", "id": 3},       "reqs": []}, #* GiftA (MagicalSeed3) -> Tree Face (Bub-ulb) Wrong Exit (To Previous)

    # MIM_05
    {"from": {"map": "MIM_05", "id": 0}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest
    {"from": {"map": "MIM_05", "id": 1}, "to": {"map": "MIM_06", "id": 3}, "reqs": []}, # MIM_05 Correct Exit -> MIM_06 Wrong Exit (To Previous)
    {"from": {"map": "MIM_05", "id": 2}, "to": {"map": "MIM_04", "id": 0}, "reqs": []}, # MIM_05 Wrong Exit (To Previous) -> Tree Face (Bub-ulb) Correct Exit
    {"from": {"map": "MIM_05", "id": 3}, "to": {"map": "MIM_08", "id": 1}, "reqs": []}, # MIM_05 To HPPlus -> MIM_08 Correct Exit
    
    {"from": {"map": "MIM_05", "id": 2}, "to": {"map": "MIM_05", "id": 0}, "reqs": []}, #? MIM_05 Wrong Exit (To Previous) -> Get Lost In The Forest
    {"from": {"map": "MIM_05", "id": 0}, "to": {"map": "MIM_05", "id": 2}, "reqs": []}, #? Get Lost In The Forest -> MIM_05 Wrong Exit (To Previous)
    {"from": {"map": "MIM_05", "id": 2}, "to": {"map": "MIM_05", "id": 1}, "reqs": []}, #? MIM_05 Wrong Exit (To Previous) -> MIM_05 Correct Exit
    {"from": {"map": "MIM_05", "id": 1}, "to": {"map": "MIM_05", "id": 2}, "reqs": []}, #? MIM_05 Correct Exit -> MIM_05 Wrong Exit (To Previous)
    {"from": {"map": "MIM_05", "id": 2}, "to": {"map": "MIM_05", "id": 3}, "reqs": []}, #? MIM_05 Wrong Exit (To Previous) -> MIM_05 To HPPlus
    {"from": {"map": "MIM_05", "id": 3}, "to": {"map": "MIM_05", "id": 2}, "reqs": []}, #? MIM_05 To HPPlus -> MIM_05 Wrong Exit (To Previous)

    # MIM_06
    {"from": {"map": "MIM_06", "id": 0}, "to": {"map": "MIM_07", "id": 2}, "reqs": []}, # MIM_06 Correct Exit -> MIM_07 Wrong Exit (To Previous)
    {"from": {"map": "MIM_06", "id": 1}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 1
    {"from": {"map": "MIM_06", "id": 2}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 2
    {"from": {"map": "MIM_06", "id": 3}, "to": {"map": "MIM_05", "id": 1}, "reqs": []}, # MIM_06 Wrong Exit (To Previous) -> MIM_05 Correct Exit
    
    {"from": {"map": "MIM_06", "id": 3}, "to": {"map": "MIM_06", "id": 0}, "reqs": []}, #? MIM_06 Wrong Exit (To Previous) -> MIM_06 Correct Exit
    {"from": {"map": "MIM_06", "id": 0}, "to": {"map": "MIM_06", "id": 3}, "reqs": []}, #? MIM_06 Correct Exit -> MIM_06 Wrong Exit (To Previous)
    {"from": {"map": "MIM_06", "id": 3}, "to": {"map": "MIM_06", "id": 1}, "reqs": []}, #? MIM_06 Wrong Exit (To Previous) -> Get Lost In The Forest 1
    {"from": {"map": "MIM_06", "id": 1}, "to": {"map": "MIM_06", "id": 3}, "reqs": []}, #? Get Lost In The Forest 1 -> MIM_06 Wrong Exit (To Previous)
    {"from": {"map": "MIM_06", "id": 3}, "to": {"map": "MIM_06", "id": 2}, "reqs": []}, #? MIM_06 Wrong Exit (To Previous) -> Get Lost In The Forest 2
    {"from": {"map": "MIM_06", "id": 2}, "to": {"map": "MIM_06", "id": 3}, "reqs": []}, #? Get Lost In The Forest 2 -> MIM_06 Wrong Exit (To Previous)

    # MIM_07
    {"from": {"map": "MIM_07", "id": 0}, "to": {"map": "MIM_09", "id": 2}, "reqs": []}, # MIM_07 To FPPlus -> Flowers Appear (FP Plus) Correct Exit
    {"from": {"map": "MIM_07", "id": 1}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest
    {"from": {"map": "MIM_07", "id": 2}, "to": {"map": "MIM_06", "id": 0}, "reqs": []}, # MIM_07 Wrong Exit (To Previous) -> MIM_06 Correct Exit
    {"from": {"map": "MIM_07", "id": 3}, "to": {"map": "MIM_11", "id": 0}, "reqs": []}, # MIM_07 Forever Forest Entrance (Boo's Mansion) -> Outside Boo's Mansion Forever Forest Entrance
    
    {"from": {"map": "MIM_07", "id": 2}, "to": {"map": "MIM_07", "id": 0}, "reqs": []}, #? MIM_07 Wrong Exit (To Previous) -> MIM_07 To FPPlus
    {"from": {"map": "MIM_07", "id": 0}, "to": {"map": "MIM_07", "id": 2}, "reqs": []}, #? MIM_07 To FPPlus -> MIM_07 Wrong Exit (To Previous)
    {"from": {"map": "MIM_07", "id": 2}, "to": {"map": "MIM_07", "id": 1}, "reqs": []}, #? MIM_07 Wrong Exit (To Previous) -> Get Lost In The Forest
    {"from": {"map": "MIM_07", "id": 1}, "to": {"map": "MIM_07", "id": 2}, "reqs": []}, #? Get Lost In The Forest -> MIM_07 Wrong Exit (To Previous)
    {"from": {"map": "MIM_07", "id": 2}, "to": {"map": "MIM_07", "id": 3}, "reqs": []}, #? MIM_07 Wrong Exit (To Previous) -> MIM_07 Forever Forest Entrance (Boo's Mansion)
    {"from": {"map": "MIM_07", "id": 3}, "to": {"map": "MIM_07", "id": 2}, "reqs": []}, #? MIM_07 Forever Forest Entrance (Boo's Mansion) -> MIM_07 Wrong Exit (To Previous)

    # MIM_08
    {"from": {"map": "MIM_08", "id": 0}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 1
    {"from": {"map": "MIM_08", "id": 1}, "to": {"map": "MIM_05", "id": 3}, "reqs": []}, # MIM_08 Correct Exit -> MIM_05 To HPPlus
    {"from": {"map": "MIM_08", "id": 2}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 2
    {"from": {"map": "MIM_08", "id": 3}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 3
    
    {"from": {"map": "MIM_08", "id": 1}, "to": {"map": "MIM_08", "id": 0}, "reqs": []}, #? MIM_08 Correct Exit -> Get Lost In The Forest 1
    {"from": {"map": "MIM_08", "id": 0}, "to": {"map": "MIM_08", "id": 1}, "reqs": []}, #? Get Lost In The Forest 1 -> MIM_08 Correct Exit
    {"from": {"map": "MIM_08", "id": 1}, "to": {"map": "MIM_08", "id": 2}, "reqs": []}, #? MIM_08 Correct Exit -> Get Lost In The Forest 2
    {"from": {"map": "MIM_08", "id": 2}, "to": {"map": "MIM_08", "id": 1}, "reqs": []}, #? Get Lost In The Forest 2 -> MIM_08 Correct Exit
    {"from": {"map": "MIM_08", "id": 1}, "to": {"map": "MIM_08", "id": 3}, "reqs": []}, #? MIM_08 Correct Exit -> Get Lost In The Forest 3
    {"from": {"map": "MIM_08", "id": 3}, "to": {"map": "MIM_08", "id": 1}, "reqs": []}, #? Get Lost In The Forest 3 -> MIM_08 Correct Exit
    
    {"from": {"map": "MIM_08", "id": 1},         "to": {"map": "MIM_08", "id": "RBlockA"}, "reqs": []}, #* MIM_08 Correct Exit -> RBlockA (HPPlus)
    {"from": {"map": "MIM_08", "id": "RBlockA"}, "to": {"map": "MIM_08", "id": 1},         "reqs": []}, #* RBlockA (HPPlus) -> MIM_08 Correct Exit

    # MIM_09 Flowers Appear (FP Plus)
    {"from": {"map": "MIM_09", "id": 0}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 1
    {"from": {"map": "MIM_09", "id": 1}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 2
    {"from": {"map": "MIM_09", "id": 2}, "to": {"map": "MIM_07", "id": 0}, "reqs": []}, # Flowers Appear (FP Plus) Correct Exit -> MIM_07 To FPPlus
    {"from": {"map": "MIM_09", "id": 3}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Get Lost In The Forest 3
    
    {"from": {"map": "MIM_09", "id": 2}, "to": {"map": "MIM_09", "id": 0}, "reqs": []}, #? Flowers Appear (FP Plus) Correct Exit -> Get Lost In The Forest 1
    {"from": {"map": "MIM_09", "id": 0}, "to": {"map": "MIM_09", "id": 2}, "reqs": []}, #? Get Lost In The Forest 1 -> Flowers Appear (FP Plus) Correct Exit
    {"from": {"map": "MIM_09", "id": 2}, "to": {"map": "MIM_09", "id": 1}, "reqs": []}, #? Flowers Appear (FP Plus) Correct Exit -> Get Lost In The Forest 2
    {"from": {"map": "MIM_09", "id": 1}, "to": {"map": "MIM_09", "id": 2}, "reqs": []}, #? Get Lost In The Forest 2 -> Flowers Appear (FP Plus) Correct Exit
    {"from": {"map": "MIM_09", "id": 2}, "to": {"map": "MIM_09", "id": 3}, "reqs": []}, #? Flowers Appear (FP Plus) Correct Exit -> Get Lost In The Forest 3
    {"from": {"map": "MIM_09", "id": 3}, "to": {"map": "MIM_09", "id": 2}, "reqs": []}, #? Get Lost In The Forest 3 -> Flowers Appear (FP Plus) Correct Exit
    
    {"from": {"map": "MIM_09", "id": 2},         "to": {"map": "MIM_09", "id": "RBlockA"}, "reqs": []}, #* Flowers Appear (FP Plus) Correct Exit -> RBlockA (FPPlus)
    {"from": {"map": "MIM_09", "id": "RBlockA"}, "to": {"map": "MIM_09", "id": 2},         "reqs": []}, #* RBlockA (FPPlus) -> Flowers Appear (FP Plus) Correct Exit

    # MIM_10 Exit to Toad Town
    {"from": {"map": "MIM_10", "id": 0}, "to": {"map": "MAC_02", "id": 1}, "reqs": []}, # Exit to Toad Town Toad Town Entrance -> Southern District Exit Right
    {"from": {"map": "MIM_10", "id": 1}, "to": {"map": "MIM_01", "id": 1}, "reqs": []}, # Exit to Toad Town Entry to Forever Forest -> Flower Sounds Forever Forest Entrance (Toad Town)
    
    {"from": {"map": "MIM_10", "id": 0}, "to": {"map": "MIM_10", "id": 1}, "reqs": []}, #? Exit to Toad Town Toad Town Entrance -> Exit to Toad Town Entry to Forever Forest
    {"from": {"map": "MIM_10", "id": 1}, "to": {"map": "MIM_10", "id": 0}, "reqs": []}, #? Exit to Toad Town Entry to Forever Forest -> Exit to Toad Town Toad Town Entrance

    # MIM_11 Outside Boo's Mansion
    {"from": {"map": "MIM_11", "id": 0}, "to": {"map": "MIM_07", "id": 3}, "reqs": []}, # Outside Boo's Mansion Forever Forest Entrance -> MIM_07 Forever Forest Entrance (Boo's Mansion)
    {"from": {"map": "MIM_11", "id": 1}, "to": {"map": "MIM_12", "id": 0}, "reqs": []}, # Outside Boo's Mansion Entrance to Wasteland -> Exit to Gusty Gulch Exit West
    {"from": {"map": "MIM_11", "id": 2}, "to": {"map": "OBK_01", "id": 0}, "reqs": []}, # Outside Boo's Mansion Front Door -> Foyer Leave Mansion
    {"from": {"map": "MIM_11", "id": 3}, "to": {"map": "TIK_09", "id": 2}, "reqs": []}, # Outside Boo's Mansion Blue Warp Pipe -> Warp Zone 2 (B2) Blue Warp Pipe
    
    {"from": {"map": "MIM_11", "id": 0}, "to": {"map": "MIM_11", "id": 1}, "reqs": []}, #? Outside Boo's Mansion Forever Forest Entrance -> Outside Boo's Mansion Entrance to Wasteland
    {"from": {"map": "MIM_11", "id": 1}, "to": {"map": "MIM_11", "id": 0}, "reqs": []}, #? Outside Boo's Mansion Entrance to Wasteland -> Outside Boo's Mansion Forever Forest Entrance
    {"from": {"map": "MIM_11", "id": 0}, "to": {"map": "MIM_11", "id": 2}, "reqs": []}, #? Outside Boo's Mansion Forever Forest Entrance -> Outside Boo's Mansion Front Door
    {"from": {"map": "MIM_11", "id": 2}, "to": {"map": "MIM_11", "id": 0}, "reqs": []}, #? Outside Boo's Mansion Front Door -> Outside Boo's Mansion Forever Forest Entrance
    {"from": {"map": "MIM_11", "id": 0}, "to": {"map": "MIM_11", "id": 3}, "reqs": [require(flag="GF_MIM11_WarpPipe")]}, #? Outside Boo's Mansion Forever Forest Entrance -> Outside Boo's Mansion Blue Warp Pipe
    {"from": {"map": "MIM_11", "id": 3}, "to": {"map": "MIM_11", "id": 0}, "reqs": []}, #? Outside Boo's Mansion Blue Warp Pipe -> Outside Boo's Mansion Forever Forest Entrance
    
    {"from": {"map": "MIM_11", "id": 3}, "to": {"map": "MIM_11", "id": 3}, "reqs": [], "pseudoitems": ["GF_MIM11_WarpPipe"]}, #+ Outside Boo's Mansion Blue Warp Pipe
    
    {"from": {"map": "MIM_11", "id": 0},         "to": {"map": "MIM_11", "id": "YBlockA"}, "reqs": []}, #* Outside Boo's Mansion Forever Forest Entrance -> YBlockA (VoltShroom)
    {"from": {"map": "MIM_11", "id": "YBlockA"}, "to": {"map": "MIM_11", "id": 0},         "reqs": []}, #* YBlockA (VoltShroom) -> Outside Boo's Mansion Forever Forest Entrance
    {"from": {"map": "MIM_11", "id": 1},         "to": {"map": "MIM_11", "id": "ItemA"},   "reqs": []}, #* Outside Boo's Mansion Entrance to Wasteland -> ItemA (StrangeLeaf)
    {"from": {"map": "MIM_11", "id": "ItemA"},   "to": {"map": "MIM_11", "id": 1},         "reqs": []}, #* ItemA (StrangeLeaf) -> Outside Boo's Mansion Entrance to Wasteland
    
    # MIM_12 Exit to Gusty Gulch
    {"from": {"map": "MIM_12", "id": 0}, "to": {"map": "MIM_11", "id": 1}, "reqs": []}, # Exit to Gusty Gulch Exit West -> Outside Boo's Mansion Entrance to Wasteland
    {"from": {"map": "MIM_12", "id": 1}, "to": {"map": "ARN_07", "id": 2}, "reqs": []}, # Exit to Gusty Gulch Exit East -> Windmill Exterior Exit Left
    
    {"from": {"map": "MIM_12", "id": 0}, "to": {"map": "MIM_12", "id": 1}, "reqs": []}, #? Exit to Gusty Gulch Exit West -> Exit to Gusty Gulch Exit East
    {"from": {"map": "MIM_12", "id": 1}, "to": {"map": "MIM_12", "id": 0}, "reqs": []}, #? Exit to Gusty Gulch Exit East -> Exit to Gusty Gulch Exit West
    
    {"from": {"map": "MIM_12", "id": 1},             "to": {"map": "MIM_12", "id": "HiddenPanel"}, "reqs": [flip_panels]}, #* Exit to Gusty Gulch Exit East -> HiddenPanel (StarPiece)
    {"from": {"map": "MIM_12", "id": "HiddenPanel"}, "to": {"map": "MIM_12", "id": 1},             "reqs": []}, #* HiddenPanel (StarPiece) -> Exit to Gusty Gulch Exit East
]