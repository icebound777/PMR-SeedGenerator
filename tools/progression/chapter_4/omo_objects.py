"""Requirements for item locations in omo: Shy Guy's Toybox"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# BLU Station
'OMO_03':    {'HiddenPanel':    [("Bow","SuperBoots"),
                                 ("Bow","UltraHammer")], # 'StarPiece',
              'HiddenYBlockA':  [("Bow",)],              # 'StoneCap'
              },
# BLU Anti-Guy Hall
'OMO_13':   {'ChestA':          [("Bow","FryingPan")], # 'PowerPlusB',
             'YBlockA':         [("Bow",)], # 'Coin',
             'HiddenYBlockA':   [("Bow",)], # 'MapleSyrup'
             },
             # * Discuss: Require FryingPan for AntiGuy cause you can bribe him with a LemonCandy
# BLU Large Playroom
'OMO_01':    {'ItemA':          [("Bow",)], # 'Calculator',
              'HiddenYBlockA':  [("Bow",)], # 'Mystery',
              'HiddenYBlockB':  [("Bow",)], # 'FrightJar'
              },
              #TODO maybe missing: Other items carried by shy guys
# BLU Block City
'OMO_04':    {'ItemA':          [("p_NYI",)],       # 'Mushroom',
              'ChestA':         [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'StoreroomKey',
              'YBlockA':        [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'YBlockB':        [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'YBlockC':        [("Bow","Parakarry","SuperBoots"),
                                 ("Bow","Parakarry","Hammer")], # 'ThunderBolt',
              'ItemB':          [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'ItemC':          [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'ItemD':          [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'ItemE':          [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'ItemF':          [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'ItemG':          [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'ItemH':          [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'ItemI':          [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],    # 'Coin',
              'ItemJ':          [("Bow","Parakarry","SuperBoots"),
                                 ("Bow","Parakarry","Hammer")], # on building 'StarPiece',
              'ItemK':          [("Bow","SuperBoots"),
                                 ("Bow","Hammer")],  # behind building block 'StarPiece'
              },
              # * Mushroom only exists if Peach answers a certain way during previous intermission
# PNK Station
'OMO_06':    {'HiddenPanel':    [("Bow","SuperBoots","p_PlacedToyTrain"),
                                 ("Bow","UltraHammer","p_PlacedToyTrain")], # 'StarPiece',
              'ChestA':         [("Bow","p_PlacedToyTrain")], # 'Mailbag',
              'HiddenYBlockA':  [("Bow","p_PlacedToyTrain")], # 'ThunderRage'
              },
# PNK Tracks Hallway
'OMO_17':   {'YBlockA':         [("Bow","p_PlacedToyTrain")],                 # 'Coin',
             'YBlockB':         [("Bow","p_PlacedToyTrain")],                 # 'Coin',
             'YBlockC':         [("Bow","p_PlacedToyTrain")],                 # 'Coin'
             },
# PNK Gourmet Guy Crossing
'OMO_05':    {'ItemA':          [("Bow","p_PlacedToyTrain")],                 # 'Cookbook',
              'YBlockA':        [("Bow","p_PlacedToyTrain")],                 # 'Coin',
              'YBlockB':        [("Bow","p_PlacedToyTrain")],                 # 'Coin',
              'ItemB':          [("Bow","p_PlacedToyTrain")],                 # 'Cookbook',
              'HiddenYBlockA':  [("Bow","p_PlacedToyTrain")],                 # 'DizzyDial',
              'HiddenYBlockB':  [("Bow","p_PlacedToyTrain")],                 # 'SuperSoda'
              },
              #TODO duplicates?
# PNK Playhouse
'OMO_07':    {'ItemA':          [("p_NYI",)],                      # 'ThunderRage',
              'ChestA':         [("Hammer","Bow","p_PlacedToyTrain"),
                                 ("SuperBoots","Bow","p_PlacedToyTrain")], # 'FryingPan',
              'ChestB':         [("Hammer","Bow","p_PlacedToyTrain"),
                                 ("SuperBoots","Bow","p_PlacedToyTrain")], # 'DefendPlusA',
              'ChestC':         [("Hammer","Bow","p_PlacedToyTrain"),
                                 ("SuperBoots","Bow","p_PlacedToyTrain")], # 'IcePower',
              'YBlockA':        [("Hammer","Bow","p_PlacedToyTrain"),
                                 ("SuperBoots","Bow","p_PlacedToyTrain")], # 'Coin'
              },
              # * ThunderRage only exists if Peach answers a certain way during previous intermission
              # ! From here on down everything technically needs Cake for Gourment Guy
# GRN Station
'OMO_08':    {'HiddenPanel':    [("Bow","SuperBoots","p_PlacedToyTrain"),
                                 ("Bow","UltraHammer","p_PlacedToyTrain")], # 'StarPiece',
              'HiddenYBlockA':  [("Bow","p_PlacedToyTrain")],               # 'FireFlower'
              },
# GRN Treadmills/Slot Machine
'OMO_09':   {'ItemA':           [("p_NYI")],                      # 'SuperSoda',
             'ChestA':          [("Parakarry","Bow","p_PlacedToyTrain")], # 'Dictionary',
             'ItemB':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemC':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemD':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemE':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemF':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemG':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemH':           [("Bow","p_PlacedToyTrain")],             # 'StarPiece',
             'ItemI':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemJ':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemK':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemL':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemM':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemN':           [("Bow","p_PlacedToyTrain")],             # 'Coin',
             'ItemO':           [("Bow","p_PlacedToyTrain")],             # 'MysteryNote'
             },
             # * SuperSoda only exists if Peach answers a certain way during previous intermission
# RED Station
# * The logic from here on requires Hammer, since you have to do the box puzzle at GRN Station
# TODO maybe exchange Hammer requirement for p_Ch4_BoxPuzzle?
'OMO_10':    {'HiddenPanel':    [("Hammer","SuperBoots","Bow","p_PlacedToyTrain"),
                                 ("UltraHammer","Bow","p_PlacedToyTrain")], # 'StarPiece',
              'HiddenYBlockA':  [("Hammer","Bow","p_PlacedToyTrain")],      # 'SuperShroom'
              },
# RED Moving Platforms
'OMO_11':   {'HiddenYBlockA':   [("Hammer","Bow","p_PlacedToyTrain")],                 # 'VoltShroom',
             'HiddenYBlockB':   [("Hammer","Bow","p_PlacedToyTrain")],                 # 'SnowmanDoll',
             'YBlockA':         [("Hammer","Bow","p_PlacedToyTrain")],                 # 'Coin',
             'HiddenRBlockA':   [("Hammer","Bow","p_PlacedToyTrain")],                 # 'DeepFocus2',
             'YBlockB':         [("Hammer","Bow","p_PlacedToyTrain")],                 # 'Coin'
             },
# RED Boss Barricade
'OMO_02':    {'YBlockA':        [("Hamemr","Bow","p_PlacedToyTrain")],                 # 'SleepySheep',
              'HiddenYBlockA':  [("Hamemr","Bow","p_PlacedToyTrain")],                 # 'Coin',
              'ItemA':          [("Hammer","Kooper","Bow","p_PlacedToyTrain"),
                                 ("Hammer","UltraBoots","Bow","p_PlacedToyTrain")],    # 'ShootingStar'
              },
}