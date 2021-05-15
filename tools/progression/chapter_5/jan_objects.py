"""Requirements for item locations in jan: Jade Jungle"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
#Whale Cove
'JAN_00':   {'ItemA':           [],                 # 'Coin',
             'ItemB':           [],                 # 'Coin',
             'ItemC':           [],                 # 'StopWatch'
             },
              #TODO Missing: Respawning Coconut from palmtree
# Beach
'JAN_01':   {'ItemA':           [],                 # 'Letter11',
             'HiddenYBlockA':   [],                 # 'RepelGel',
             'HiddenYBlockB':   [],                 # 'Mystery',
             'ItemB':           [],                 # 'Coin',
             'ItemC':           [],                 # 'Coin'
             },
              #TODO Missing Respawning Coconut from palmtree x6, StarPiece from palmtree
# Village Cove
'JAN_02':    {'HiddenPanel':    [("SuperBoots"),
                                 ("UltraHammer")],      # 'StarPiece',
              'GiftA':          [("p_RescuedYoshis",)], # 'JadeRaven'
              },
              #TODO Missing: Respawning Coconut from palmtree x2
# Village Buildings
'JAN_03':    {'ShopItemA':      [],                 # 'SnowmanDoll',
              'ShopItemB':      [],                 # 'ThunderRage',
              'ShopItemC':      [],                 # 'FireFlower',
              'ShopItemD':      [],                 # 'TastyTonic',
              'ShopItemE':      [],                 # 'HoneySyrup',
              'ShopItemF':      [],                 # 'SuperShroom',
              'GiftA':          [("VolcanoVase","p_Ch5Done")], # 'MagicalSeed4'
              },
              #TODO Missing: Letter21 to Red Yoshi Kid, Respawning Coconut from palmtree
# SE Jungle (Quake Hammer)
'JAN_05':   {'RBlockA':         [("Sushie",)],      # 'PowerQuake'
             },
# Sushi Tree
'JAN_04':   {'ChestA':          [("p_Ch5Done")],       # 'VolcanoVase',
             'ItemA':           [("Sushie",)],         # 'StarPiece',
             'Tree2_Drop1A':    [("Sushie","Hammer")], # 'Letter04'
             },
# SW Jungle (Super Block)
'JAN_08':   {'ItemA':           [("Sushie",)],      # 'Coin',
             'ItemB':           [("Sushie",)],      # 'Coin',
             'ItemC':           [("Sushie",)],      # 'Coin',
             'HiddenYBlockA':   [("Sushie",)],      # 'ThunderRage'
             },
#TODO Missing: 'JAN_09': {'Tree': []} # 'FrightJar'
# NE Jungle (Raven Statue)
'JAN_06':   {'ItemA':           [("Sushie","Hammer")], # 'Coin'
             },
# Western Dead End
'JAN_10':   {'ItemA':           [("Sushie",)],      # 'StarPiece'
             },
# Deep Jungle 1
'JAN_12':   {'ItemA':           [("Sushie","Hammer","p_PlacedRavenStatue")], # 'Egg2',
             'HiddenYBlockA':   [("Sushie","p_PlacedRavenStatue")],          # 'StoneCap'
             },
# Deep Jungle 2 (Block Puzzle)
'JAN_13':   {'HiddenYBlockA':   [("Sushie","p_PlacedRavenStatue")],          # 'VoltShroom'
             },
# Deep Jungle 3
'JAN_14':   {'ItemA':           [("Sushie","p_PlacedRavenStatue")],          # 'FireFlower',
             'ItemB':           [("Sushie","p_PlacedRavenStatue")],          # 'Mushroom'
             },
# Deep Jungle 4 (Ambush)
'JAN_15':    {'HiddenPanel':    [("Sushie","SuperBoots","p_PlacedRavenStatue"),
                                 ("Sushie","UltraHammer","p_PlacedRavenStatue")], # 'StarPiece'
              },
# Great Tree Vine Ascent
'JAN_18':   {'ItemA':           [("Sushie","p_PlacedRavenStatue")],          # 'HappyHeartB'
             },
# Path to the Volcano
'JAN_22':   {'GiftA':           [("Sushie","p_PlacedRavenStatue")], # 'UltraStone',
             'ItemA':           [],                         # 'JamminJelly'
             },
}