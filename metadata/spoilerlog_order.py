"""Provides custom ordering values for map ids."""
custom_map_order = {
#area: {map_id: ordering}
    0: { # KMR - Goomba Region
        0: 0,   # Forest Clearing
        1: 1,   # Goomba Village
        4: 2,   # Behind the Village
        2: 3,   # Bottom of the Cliff
        3: 4,   # Jr. Troopas Playground
        7: 5,   # Goomba Road 1
        5: 6,   # Goomba Road 2
        6: 7,   # Goomba Road 3
        10: 8,  # Goomba Road 4
        9: 9,   # Goomba Kings Castle
        8: 10,  # Toad Town Entrance
        11: 11, # Marios House
    },
    1: { # MAC - Toad Town
        1: 0,   # Gate District
        2: 1,   # Plaza District
        3: 2,   # Southern District
        4: 3,   # Station District
        5: 4,   # Residental District
        6: 5,   # Port District
        7: 6,   # Riding the Whale
    },
    2: { # TIK - Toad Town Tunnels
        5: 0,   # Sewer Entrance (B1)
        14: 1,  # Hall to Blooper 1 (B1)
        1: 2,   # Blooper Boss 1 (B1)
        0: 3,   # Warp Zone 1 (B1)
        2: 4,   # Short Elevator Room (B1)
        3: 5,   # Scales Room (B2)
        4: 6,   # Spring Room (B2)
        6: 7,   # Elevator Attic Room (B2)
        10: 8,  # Metal Block Room (B3)
        7: 9,   # Second Level Entry (B2)
        8: 10,  # Warp Zone 2 (B2)
        9: 11,  # Blue Pushblock Room (B2)
        16: 12, # Room with Spikes (B2)
        19: 13, # Winding Path (Spiny Room)
        20: 14, # Hall to Ultra Boots (B3)
        21: 15, # Ultra Boots Room (B3)
        17: 16, # Bridge to Shiver City (B2)
        18: 17, # Pipe to Frozen Room (B2)
        13: 18, # Frozen Room (B3)
        11: 19, # Rip Cheato Antechamber (B3)
        12: 20, # Rip Cheatos Home (B3)
        15: 21,  # Under the Toad Town Pond
    },
    3: { # KGR - Inside the Whale
        0: 0,   # Whale Mouth
        1: 1,   # Whale Stomach
    },
    4: { # KKJ - Peachs Castle
        4: 0,   # Entry Hall (1F)
        15: 1,  # Inactive Quiz-Off (1F)
        13: 2,  # Kitchen (1F)
        14: 3,  # Guest Room (1F)
        5: 4,   # Upper Hall (2F)
        10: 5,  # Library (2F)
        9: 6,   # Passage Outlet (2F)
        8: 7,   # Peachs Room (2F)
        20: 8,  # Balcony (2F)
        11: 9,  # Storeroom (2F)
        12: 10, # Dining Room (2F)
        6: 11,  # Stairs Hallway (3F)
        7: 12,  # Window Hallway (4F)
        16: 13, # Double Staircase (4F)
        17: 14, # Rooftop (5F)
        18: 15, # Tower Staircase (5F)
        19: 16, # Final Boss Arena (6F)
    },
    5: { # HOS - Shooting Star Summit
        0: 0,   # Shooting Star Path
        6: 1,   # Merluvlees House
        1: 2,   # Shooting Star Summit
        2: 3,   # Star Way
        3: 4,   # Star Haven
        4: 5,   # Outside the Sanctuary
        5: 6,   # Star Sanctuary
        8: 7,   # Riding Star Ship Scene
    },
    6: { # NOK - Koopa Region
        4: 0,   # Pleasant Path Entry
        5: 1,   # Pleasant Path Bridge
        5: 2,   # Pleasant Path Bridge
        6: 3,   # Pleasant Crossroads
        7: 4,   # Path to Fortress 1
        8: 5,   # Path to Fortress 2
        0: 6,   # Koopa Village 1
        1: 7,   # Koopa Village 2
        2: 8,   # Behind Koopa Village
        3: 9,   # Fuzzy Forest
    },
    7: { # TRD - Koopa Bros Fortress
        0: 0,   # Fortress Exterior
        1: 1,   # Left Tower
        2: 2,   # Left Stairway
        3: 3,   # Central Hall
        4: 4,   # Right Starway
        5: 5,   # Right Tower
        6: 6,   # Jail
        7: 7,   # Dungeon Trap
        8: 8,   # Dungeon Fire Room
        9: 9,   # Battlement
        10: 10, # Boss Battle Room
    },
    8: { # IWA - Mt. Rugged
        6: 0,   # Train Ride Scene
        5: 1,   # Train Station
        0: 2,   # Mt Rugged 1
        1: 3,   # Mt Rugged 2
        2: 4,   # Mt Rugged 3
        3: 5,   # Mt Rugged 4
        4: 6,   # Suspension Bridge
    },
    9: { # DRO - Dry Dry Outpost
        0: 0,   # Outpost 1
        1: 1,   # Outpost 2
    },
    10: { # SBK - Dry Dry Desert
        49: 0,  # Entrance
        0: 1,   # N3W3
        1: 2,   # N3W2
        2: 3,   # N3W1 Ruins Entrance
        3: 4,   # N3
        4: 5,   # N3E1
        5: 6,   # N3E2 Pokey Army
        6: 7,   # N3E3
        7: 8,   # N2W3
        8: 9,   # N2W2
        9: 10,  # N2W1
        10: 11, # N2
        11: 12, # N2E1 (Tweester A)
        12: 13, # N2E2
        13: 14, # N2E3
        14: 15, # N1W3 Special Block
        15: 16, # N1W2
        16: 17, # N1W1
        17: 18, # N1 (Tweester B)
        18: 19, # N1E1 Palm Trio
        19: 20, # N1E2
        20: 21, # N1E3
        21: 22, # W3 Kolorado's Camp
        22: 23, # W2
        23: 24, # W1
        24: 25, # Center (Tweester C)
        25: 26, # E1 Nomadimouse
        26: 27, # E2
        27: 28, # E3 Outside Outpost
        28: 29, # S1W3
        29: 30, # S1W2 (Tweester D)
        30: 31, # S1W1
        31: 32, # S1
        32: 33, # S1E1
        33: 34, # S1E2 Small Bluffs
        34: 35, # S1E3 North of Oasis
        35: 36, # S2W3
        36: 37, # S2W2
        37: 38, # S2W1
        38: 39, # S2
        39: 40, # S2E1 Blue Cactus
        40: 41, # S2E2 West of Oasis
        41: 42, # S2E3 Oasis
        42: 43, # S3W3
        43: 44, # S3W2 Hidden AttackFX
        44: 45, # S3W1
        45: 46, # S3
        46: 47, # S3E1
        47: 48, # S3E2
        48: 49, # S3E3 South of Oasis
    },
    11: { # ISK - Dry Dry Ruins
        0: 0,   # Entrance
        1: 1,   # Sarcophagus Hall 1
        2: 2,   # Sand Drainage Room 1
        3: 3,   # Descending Stairs 1
        5: 4,   # Sand Drainage Room 2
        4: 5,   # Pyramid Stone Room
        6: 6,   # Sarcophagus Hall 2
        7: 7,   # Descending Stairs 2
        8: 8,   # Super Hammer Room
        9: 9,   # Vertical Shaft
        13: 10, # Diamond Stone Room
        15: 11, # Deep Tunnel
        10: 12, # Stone Puzzle Room
        11: 13, # Sand Drainage Room 3
        12: 14, # Lunar Stone Room
        16: 15, # Boss Antechamber
        14: 16, # Tutankoopa Room
    },
    12: { # MIM - Forever Forest
        9: 0,   # Exit to Toad Town
        0: 1,   # Flower Sounds
        1: 2,   # Stump Eyes
        2: 3,   # Flowers (Oaklie)
        3: 4,   # Tree Face (Bub-ulb)
        4: 5,   # Mushrooms (Path Splits)
        7: 6,   # Bee Hive (HP Plus)
        5: 7,   # Flowers Vanish
        6: 8,   # Laughing Rock
        8: 9,   # Flowers Appear (FP Plus)
        10: 10, # Outside Boo's Mansion
        11: 11, # Exit to Gusty Gulch
    },
    13: { # OBK - Boos Mansion
        0: 0,   # Foyer
        1: 1,   # Basement Stairs
        2: 2,   # Basement
        3: 3,   # Super Boots Room
        4: 4,   # Pot Room
        5: 5,   # Library
        6: 6,   # Record Player Room
        7: 7,   # Record Room
        8: 8,   # Lady Bows Room
    },
    14: { # ARN - Gusty Gulch
        4: 0,   # Windmill Exterior
        5: 1,   # Windmill Interior
        6: 2,   # Windmill Tunnel Entry
        7: 3,   # Tunnel 1
        9: 4,   # Tunnel 2
        10: 5,  # Tunnel 3
        8: 6,   # Tubba's Heart Chamber
        1: 7,   # Ghost Town 1
        3: 8,   # Ghost Town 2
        0: 9,   # Wasteland Ascent 1
        2: 10,  # Wasteland Ascent 2
    },
    15: { # DGB - Tubba Blubbas Castle
        0: 0,   # Outside Tubbas Castle
        1: 1,   # Great Hall
        2: 2,   # West Hall (1F)
        11: 3,  # Covered Tables Room (1F)
        7: 4,   # Study (1F)
        3: 5,   # Table/Clock Room (1/2F)
        5: 6,   # Stairs Above Basement
        6: 7,   # Basement
        4: 8,   # Stairs to Basement
        8: 9,   # East Hall (1/2F)
        9: 10,  # West Hall (2F)
        10: 11, # Sealed Room (2F)
        12: 12, # Spike Trap Room (2F)
        13: 13, # Hidden Bedroom (2F)
        14: 14, # Stairs to Third Floor
        15: 15, # West Hall (3F)
        16: 16, # Sleeping Clubbas Room (3F)
        17: 17, # Save Room (3F)
        18: 18, # Master Bedroom (3F)
    },
    16: { # OMO - Shy Guys Toybox
        2: 0,   # BLU Station
        12: 1,  # BLU Anti-Guy Hall
        0: 2,   # BLU Large Playroom
        3: 3,   # BLU Block City
        5: 4,   # PNK Station
        16: 5,  # PNK Tracks Hallway
        4: 6,   # PNK Gourmet Guy Crossing
        6: 7,   # PNK Playhouse
        7: 8,   # GRN Station
        8: 9,   # GRN Treadmills/Slot Machine
        9: 10,  # RED Station
        10: 11, # RED Moving Platforms
        11: 12, # RED Lantern Ghost
        1: 13,  # RED Boss Barricade
        13: 14, # RED Boss Antechamber
        14: 15, # RED General Guy Room
    },
    17: { # JAN - Jade Jungle
        0: 0,   # Whale Cove
        1: 1,   # Beach
        2: 2,   # Village Cove
        3: 3,   # Village Buildings
        20: 4,  # Path to the Volcano
        5: 5,   # SE Jungle (Quake Hammer)
        4: 6,   # Sushi Tree
        8: 7,   # SW Jungle (Super Block)
        9: 8,   # NW Jungle (Large Ledge)
        10: 9,  # Western Dead End
        11: 10, # Root Cavern
        6: 11,  # NE Jungle (Raven Statue)
        7: 12,  # Small Jungle Ledge
        12: 13,  # Deep Jungle 1
        13: 14,  # Deep Jungle 2 (Block Puzzle)
        14: 15,  # Deep Jungle 3
        15: 16,  # Deep Jungle 4 (Ambush)
        16: 17,  # Base of Great Tree
        17: 18,  # Lower Great Tree Interior
        18: 19,  # Great Tree Vine Ascent
        19: 20,  # Upper Great Tree Interior
        21: 21,  # Great Treetop Roost
    },
    18: { # KZN - Mt. Lavalava
        0: 0,   # Volcano Entrance
        1: 1,   # First Lava Lake
        2: 2,   # Central Cavern
        3: 3,   # Fire Bar Bridge
        4: 4,   # Descent Toward Ultra Hammer
        5: 5,   # Flowing Lava Puzzle
        6: 6,   # Ultra Hammer Room
        7: 7,   # Dizzy Stomp Room
        8: 8,   # Zipline Cavern
        9: 9,   # Descent Toward Boss
        10: 10, # Second Lava Lake
        11: 11, # Spike Roller Trap
        12: 12, # Boss Antechamber
        13: 13, # Boss Room
        14: 14, # Rising Lava 1
        15: 15, # Rising Lava 2
    },
    19: { # FLO - Flower Fields
        0: 0,   # Center
        11: 1,  # (NE) Elevators
        12: 2,  # (NE) Fallen Logs
        13: 3,  # (NE) Puff Puff Machine
        4: 4,   # (East) Triple Tree Path
        1: 5,   # (East) Petunias Field
        16: 6,  # (East) Old Well
        3: 7,   # (SE) Briar Platforming
        18: 8,  # (SE) Water Level Room
        5: 9,   # (SE) Lilys Fountain
        19: 10, # (SW) Path to Crystal Tree
        2: 11,  # (SW) Posie and Crystal Tree
        17: 12, # (West) Path to Maze
        6: 13,  # (West) Maze
        7: 14,  # (West) Rosies Trellis
        9: 15,  # (NW) Bubble Flower
        8: 16,  # (NW) Lakilester
        10: 17, # (NW) Sun Tower
        14: 18, # Cloudy Climb
        15: 19, # Huff N Puff Room
    },
    20: { # SAM Shiver Region
        1: 0,   # Shiver City Center
        0: 1,   # Shiver Mayor Area
        10: 2,  # Shiver Pond Area
        2: 3,   # Road to Shiver Snowfield
        3: 4,   # Shiver Snowfield
        4: 5,   # Path to Starborn Valley
        5: 6,   # Starborn Valley
        6: 7,   # Shiver Mountain Passage
        7: 8,   # Shiver Mountain Hills
        8: 9,   # Shiver Mountain Tunnel
        9: 10,  # Shiver Mountain Peaks
        11: 11, # Merlars Sanctuary
    },
    21: { # PRA - Crystal Palace
        0: 0,   # Entrance
        1: 1,   # Entry Hall
        2: 2,   # Save Room
        29: 3,  # Blue Key Hall
        4: 4,   # Blue Key Room
        6: 5,   # Red Key Hall
        8: 6,   # Red Key Room
        3: 7,   # Reflected Save Room
        30: 8,  # Shooting Star Hall
        5: 9,   # Shooting Star Room
        7: 10,  # P-Down, D-Up Hall
        9: 11,  # P-Down, D-Up Room
        12: 12, # Star Piece Cave
        10: 13, # Blue Mirror Hall 1
        11: 14, # Blue Mirror Hall 2
        13: 15, # Red Mirror Hall
        14: 16, # Bridge Mirror Hall
        24: 17, # Turnstyle Room
        26: 18, # Triple Dip Room
        15: 19, # Reflection Mimic Room
        16: 20, # Mirrored Door Room
        17: 21, # Huge Statue Room
        27: 22, # Palace Key Hall
        19: 23, # Palace Key Room
        18: 24, # Small Statue Room
        28: 25, # P-Up, D-Down Hall
        20: 26, # P-Up, D-Down Room
        21: 27, # Hidden Bridge Room
        25: 28, # Mirror Hole Room
        22: 29, # Dino Puzzle Room
        31: 30, # Boss Antechamber
        23: 31, # Crystal Summit
    },
    22: { # KPA - Bowsers Castle
        21: 0,   # Ship Enter/Exit Scenes
        24: 1,   # Hangar
        23: 2,   # Front Door Exterior
        25: 3,   # Entry Lava Hall
        17: 4,   # Hall to Guard Door 1
        26: 5,   # Guard Door 1
        12: 6,   # Lower Jail
        6: 7,    # Outside Lower Jail (lava)
        5: 8,    # Outside Lower Jail (no lava)
        7: 9,    # Lava Channel 1
        8: 10,   # Lava Channel 2
        10: 11,  # Lava Key Room
        9: 12,   # Lava Channel 3
        11: 13,  # Lava Control Room
        0: 14,   # Dark Cave 1
        1: 15,   # Dark Cave 2
        2: 16,   # Cave Exit
        13: 17,  # Lower Grand Hall
        29: 18,  # Stairs to East Upper Jail
        30: 19,  # East Upper Jail
        33: 20,  # Item Shop
        18: 21,  # Hall to Water Puzzle
        48: 22,  # Left Water Puzzle
        49: 23,  # Right Water Puzzle
        47: 24,  # Bill Blaster Hall
        37: 25,  # Room with Hidden Door 1
        38: 26,  # Hidden Passage 1
        39: 27,  # Room with Hidden Door 2
        40: 28,  # Hidden Passage 2
        41: 29,  # Room with Hidden Door 3
        42: 30,  # Dead End Passage
        43: 31,  # Dead End Room
        44: 32,  # Hidden Passage 3
        45: 33,  # Hidden Key Room
        27: 34,  # Guard Door 2
        22: 35,  # Battlement
        14: 36,  # Upper Grand Hall
        31: 37,  # Stairs to West Upper Jail
        32: 38,  # West Upper Jail
        4: 39,   # Ultra Shroom Timing Puzzle
        35: 40,  # Ultra Shroom Room
        19: 41,  # Split Level Hall
        3: 42,   # Castle Key Timing Puzzle
        34: 43,  # Castle Key Room
        15: 44,  # Maze Guide Room
        16: 45,  # Maze Room
        36: 46,  # Blue Fire Bridge
        20: 47,  # Fake Peach Hallway
        28: 48,  # Guard Door 3
        46: 49,  # Exit to Peachs Castle
    },
    23: { # OSR - Peachs Castle Grounds
        1: 0,  # Ruined Castle Grounds
        2: 0,  # Hijacked Castle Entrance
    },
    25: { # MGM - Playroom
        0: 0,  # Playroom Lobby
        1: 1,  # Playroom Jump Attack
        2: 2,  # Playroom Smash Attack
    }
}
