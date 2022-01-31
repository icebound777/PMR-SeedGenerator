"""Requirements for item locations in pra: Crystal Palace"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Blue Key Room
'PRA_05':    {'ChestA':          [("Sushie","UltraBoots","Bucket","Scarf","StarStone")], # 'BlueKey'
              },
# Star Piece Cave
'PRA_15':    {'ItemA':           [("Sushie","UltraBoots","Bucket","Scarf","StarStone","BlueKey"),
                                  ("Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'StarPiece'
              },
# Reflected Save Room
'PRA_04':    {'YBlockA':         [("Sushie","UltraBoots","Bucket","Scarf","StarStone","BlueKey"),
                                  ("Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'SuperShroom'
              },
# Shooting Star Room
'PRA_06':    {'ItemA':           [("Sushie","UltraBoots","Bucket","Scarf","StarStone","BlueKey"),
                                  ("Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'ShootingStar'
              },
# P-Down, D-Up Room
'PRA_12':    {'ChestA':          [("Sushie","UltraBoots","Bucket","Scarf","StarStone","BlueKey"),
                                  ("Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'PDownDUp'
              },
# Red Key Room
'PRA_11':    {'ChestA':          [("Bombette","Sushie","UltraBoots","Bucket","Scarf","StarStone","BlueKey"),
                                  ("Bombette","Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'RedKey'
              },
# Triple Dip Room
'PRA_35':    {'ChestA':          [("Bombette","Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'TripleDip'
              },
# Huge Statue Room
'PRA_21':    {'HiddenPanel':     [("Kooper","Bombette","Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'StarPiece',
              'YBlockA':         [("Kooper","Bombette","Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'MapleSyrup'
              },
# Small Statue Room
'PRA_22':    {'HiddenPanel':     [("Kooper","Bombette","Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'StarPiece',
              'HiddenYBlockA':   [("Kooper","Bombette","Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'JamminJelly'
              },
# P-Up, D-Down Room
'PRA_28':    {'ChestA':          [("Kooper","Bombette","Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'PUpDDown'
              },
# Palace Key Room
'PRA_27':    {'ChestA':          [("Kooper","Bombette","Sushie","UltraBoots","Bucket","Scarf","StarStone","RedKey")], # 'PalaceKey'
              },
}