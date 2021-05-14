"""Requirements for item locations in tik: Toad Town Tunnels"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Hall to Blooper 1 (B1)
'TIK_18':    {'HiddenYBlockA':  [],                 # 'SuperShroom'
              },
# Blooper Boss 1 (B1)
'TIK_02':    {'ChestA':         [],                 # 'ShrinkStomp'
              },
# Short Elevator Room (B1)
'TIK_03':    {'YBlockA':        [],                 # 'SnowmanDoll',
              'YBlockB':        [],                 # 'Coin',
              'YBlockC':        [],                 # 'Coin'
              },
# Spring Room (B2)
'TIK_05':    {'ChestA':         [],                 # 'PowerSmash1'
              },
# Elevator Attic Room (B2)
'TIK_07':    {'ItemA':          [],                 # 'StarPiece'
              },
# Block Puzzle Room (B2)
'TIK_10':    {'HiddenYBlockA':  [],                 # 'Coin',
              'HiddenYBlockB':  [],                 # 'Coin',
              'HiddenYBlockC':  [],                 # 'Coin'
              },
#TODO Missing: 'TIK_15' and Rip Cheato's deals
# Room with Spikes (B2)
'TIK_20':    {'YBlockA':        [],                 #'ShootingStar'
              },
# Hidden Blocks Room (B2)
'TIK_21':    {'YBlockA':        [],                 # 'Coin',
              'HiddenYBlockA':  [],                 # 'Coin',
              'HiddenYBlockB':  [],                 # 'Coin',
              'HiddenYBlockC':  [],                 # 'Coin',
              'HiddenYBlockD':  [],                 # 'Coin'
              },
# Windy Path (B3)
'TIK_23':    {'HiddenYBlockA':  [],                 # 'MapleSyrup',
              'HiddenYBlockB':  [],                 # 'StopWatch',
              'HiddenYBlockC':  [],                 # 'VoltShroom',
              'YBlockA':        [],                 # 'Coin'
              },
# Hall to Ultra Boots (B3)
'TIK_24':    {'HiddenYBlockA':  [],                 # 'LifeShroom',
              'YBlockA':        [],                 # 'Coin',
              'YBlockB':        [],                 # 'Coin'
              },
#TODO Missing: 'TIK_25': {'BigChest': []} # 'UltraBoots'
}