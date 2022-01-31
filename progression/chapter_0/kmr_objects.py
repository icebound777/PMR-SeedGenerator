"""Requirements for item locations in kmr: Goomba Region"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Forest Clearing
'KMR_00':    {'HiddenPanel':    [("SuperBoots","SuperHammer"),
                                 ("UltraBoots",)],  # 'StarPiece'
              },
# Goomba Village
'KMR_02':    {'GiftA':          [("SuperHammer",)], # 'Tape',
              'ItemA':          [("SuperHammer",)], # 'ShootingStar',
              'Tree1_Drop1A':   [("SuperHammer",)], # 'Goomnut'
              },
              #TODO Missing: Dolly to Goombaria, Goompa save reward, Letter02 to Goompa,
              #TODO          Letter10 to Goompapa, Letter24 to Goompapa
# Jr. Troopa's Playground
'KMR_04':    {'ItemA':          [("SuperHammer",)], # 'Dolly'
              },
              #TODO Missing: Hammer in bush
# Bottom of the Cliff
'KMR_03':    {'HiddenPanel':    [("SuperBoots","SuperHammer"),
                                 ("UltraBoots",)],  # 'StarPiece',
              'HiddenYBlockA':  [("SuperHammer",)], # 'RepelGel',
              'YBlockA':        [("SuperHammer",)], # 'Coin',
              'ItemA':          [("SuperHammer",)], # 'Coin',
              'ItemB':          [("SuperHammer",)], # 'Coin',
              'ItemC':          [("SuperHammer",)], # 'Coin',
              'ItemD':          [("SuperHammer",)], # 'Coin',
              'ItemE':          [("SuperHammer",)], # 'FireFlower',
              'ItemF':          [("SuperHammer",)], # 'Mushroom'
              },
# Behind the Village
'KMR_05':    {'ItemA':          [("SuperHammer",)], # 'StarPiece',
              'ItemB':          [("SuperHammer",)], # 'Coin'
              },
# Goomba Road 1
'KMR_09':    {'YBlockA':        [("SuperHammer",)], # 'Coin',
              'YBlockB':        [("SuperHammer",)], # 'Coin'
              },
# Goomba Road 2
'KMR_06':    {'RBlockA':        [("SuperHammer",)], # 'CloseCall',
              'ItemA':          [("SuperHammer",)], # 'Mushroom'
              },
# Goomba King's Castle
'KMR_11':    {'HiddenPanel':    [("SuperBoots",),
                                 ("UltraBoots",)],  # 'StarPiece',
              'YBlockA':        [("Hammer",)],      # 'SuperShroom',
              'Tree1_Drop1A':   [("SuperHammer",)], # 'StarPiece'
              },
# Toad Town Entrance
'KMR_10':    {'ChestA':         [("Hammer",)],      # 'HammerThrow',
              'YBlockA':        [],                 # 'SleepySheep'
              },
#TODO Missing:
#TODO 'KMR_20': {'LuigiReward': [],} # Autograph1
}