"""Requirements for item locations in tik: Toad Town Tunnels"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Hall to Blooper 1 (B1)
'TIK_18':    {'HiddenYBlockA':  [("Hammer",)],      # 'SuperShroom'
              },
# Blooper Boss 1 (B1)
'TIK_02':    {'ChestA':         [("Hammer",)],      # 'ShrinkStomp'
              },
# Short Elevator Room (B1)
'TIK_03':    {'YBlockA':        [("SuperHammer",)], # 'SnowmanDoll',
              'YBlockB':        [("SuperHammer",)], # 'Coin',
              'YBlockC':        [("SuperHammer",)], # 'Coin'
              },
# Spring Room (B2)
'TIK_05':    {'ChestA':         [("SuperHammer",)], # 'PowerSmash1'
              },
# Elevator Attic Room (B2)
'TIK_07':    {'ItemA':          [("Parakarry","SuperHammer")], # 'StarPiece'
              },
# Block Puzzle Room (B2)
'TIK_10':    {'HiddenYBlockA':  [("SuperBoots",)],  # 'Coin',
              'HiddenYBlockB':  [("SuperBoots",)],  # 'Coin',
              'HiddenYBlockC':  [("SuperBoots",)],  # 'Coin'
              },
#TODO Missing: 'TIK_15' and Rip Cheato's deals
# Room with Spikes (B2)
'TIK_20':    {'YBlockA':        [("Sushie","SuperBoots")], #'ShootingStar'
              },
# Hidden Blocks Room (B2)
'TIK_21':    {'YBlockA':        [("Sushie","UltraBoots")], # 'Coin',
              'HiddenYBlockA':  [("Sushie","UltraBoots")], # 'Coin',
              'HiddenYBlockB':  [("Sushie","UltraBoots")], # 'Coin',
              'HiddenYBlockC':  [("Sushie","UltraBoots")], # 'Coin',
              'HiddenYBlockD':  [("Sushie","UltraBoots")], # 'Coin'
              },
# Windy Path (B3)
'TIK_23':    {'HiddenYBlockA':  [("Sushie","Lakilester","SuperBoots")], # 'MapleSyrup',
              'HiddenYBlockB':  [("Sushie","Lakilester","SuperBoots")], # 'StopWatch',
              'HiddenYBlockC':  [("Sushie","Lakilester","SuperBoots")], # 'VoltShroom',
              'YBlockA':        [("Sushie","Lakilester","SuperBoots")], # 'Coin'
              },
# Hall to Ultra Boots (B3)
'TIK_24':    {'HiddenYBlockA':  [("Sushie","Lakilester","SuperBoots","SuperHammer")], # 'LifeShroom',
              'YBlockA':        [("Sushie","Lakilester","SuperBoots","SuperHammer")], # 'Coin',
              'YBlockB':        [("Sushie","Lakilester","SuperBoots","SuperHammer")], # 'Coin'
              },
#TODO Missing: 'TIK_25': {'BigChest': []} # 'UltraBoots'
}