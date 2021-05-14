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
'OMO_06':    {'HiddenPanel':    [("Bow","SuperBoots","ToyTrain"),
                                 ("Bow","UltraHammer","ToyTrain")], # 'StarPiece',
              'ChestA':         [("Bow","ToyTrain")], # 'Mailbag',
              'HiddenYBlockA':  [("Bow","ToyTrain")], # 'ThunderRage'
              },
# PNK Tracks Hallway
'OMO_17':   {'YBlockA':         [("Bow","ToyTrain")],                 # 'Coin',
             'YBlockB':         [("Bow","ToyTrain")],                 # 'Coin',
             'YBlockC':         [("Bow","ToyTrain")],                 # 'Coin'
             },
# PNK Gourmet Guy Crossing
'OMO_05':    {'ItemA':          [("Bow","ToyTrain")],                 # 'Cookbook',
              'YBlockA':        [("Bow","ToyTrain")],                 # 'Coin',
              'YBlockB':        [("Bow","ToyTrain")],                 # 'Coin',
              'ItemB':          [("Bow","ToyTrain")],                 # 'Cookbook',
              'HiddenYBlockA':  [("Bow","ToyTrain")],                 # 'DizzyDial',
              'HiddenYBlockB':  [("Bow","ToyTrain")],                 # 'SuperSoda'
              },
              #TODO duplicates?
# PNK Playhouse
'OMO_07':    {'ItemA':          [("p_NYI",)],                      # 'ThunderRage',
              'ChestA':         [("Hammer","Bow","ToyTrain"),
                                 ("SuperBoots","Bow","ToyTrain")], # 'FryingPan',
              'ChestB':         [("Hammer","Bow","ToyTrain"),
                                 ("SuperBoots","Bow","ToyTrain")], # 'DefendPlusA',
              'ChestC':         [("Hammer","Bow","ToyTrain"),
                                 ("SuperBoots","Bow","ToyTrain")], # 'IcePower',
              'YBlockA':        [("Hammer","Bow","ToyTrain"),
                                 ("SuperBoots","Bow","ToyTrain")], # 'Coin'
              },
              # * ThunderRage only exists if Peach answers a certain way during previous intermission
              # ! From here on down everything technically needs Cake for Gourment Guy
# GRN Station
'OMO_08':    {'HiddenPanel':    [("Bow","ToyTrain")],                 # 'StarPiece',
              'HiddenYBlockA':  [("Bow","ToyTrain")],                 # 'FireFlower'
              },
# GRN Treadmills/Slot Machine
'OMO_09':   {'ItemA':           [("Bow","ToyTrain")],                 # 'SuperSoda',
             'ChestA':          [("Bow","ToyTrain")],                 # 'Dictionary',
             'ItemB':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemC':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemD':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemE':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemF':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemG':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemH':           [("Bow","ToyTrain")],                 # 'StarPiece',
             'ItemI':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemJ':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemK':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemL':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemM':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemN':           [("Bow","ToyTrain")],                 # 'Coin',
             'ItemO':           [("Bow","ToyTrain")],                 # 'MysteryNote'
             },
# RED Station
'OMO_10':    {'HiddenPanel':    [("Bow","ToyTrain")],                 # 'StarPiece',
              'HiddenYBlockA':  [("Bow","ToyTrain")],                 # 'SuperShroom'
              },
# RED Moving Platforms
'OMO_11':   {'HiddenYBlockA':   [("Bow","ToyTrain")],                 # 'VoltShroom',
             'HiddenYBlockB':   [("Bow","ToyTrain")],                 # 'SnowmanDoll',
             'YBlockA':         [("Bow","ToyTrain")],                 # 'Coin',
             'HiddenRBlockA':   [("Bow","ToyTrain")],                 # 'DeepFocus2',
             'YBlockB':         [("Bow","ToyTrain")],                 # 'Coin'
             },
# RED Boss Barricade
'OMO_02':    {'YBlockA':        [("Bow","ToyTrain")],                 # 'SleepySheep',
              'HiddenYBlockA':  [("Bow","ToyTrain")],                 # 'Coin',
              'ItemA':          [("Bow","ToyTrain")],                 # 'ShootingStar'
              },
}