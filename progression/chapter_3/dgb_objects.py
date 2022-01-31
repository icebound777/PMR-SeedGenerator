"""Requirements for item locations in dgb: Tubba Blubba's Castle"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Study (1F)
'DGB_07':    {'ItemA':          [("Bow",)],         # 'StarPiece'
              },
              # * Technically doable without Bow, should be discussed
# Table/Clock Room (1/2F)
'DGB_03':    {'ItemA':          [("Bow","CastleKey1")], # 'StarPiece'
              },
# Basement
'DGB_06':    {'ChestA':         [("Bow","SuperBoots")], # 'CastleKey1'
              },
              # * Technically doable without Bow, should be discussed
# Covered Tables Room (1F)
'DGB_11':    {'ItemA':          [("Bombette","Parakarry","Bow","SuperBoots", "CastleKey1")], # 'DDownJump'
              },
# Spike Trap Room (2F)
'DGB_12':    {'ChestA':         [("Bow","CastleKey1")], # 'CastleKey1'
              },
# Hidden Bedroom (2F)
'DGB_13':    {'ItemA':          [("Parakarry","Bow","CastleKey1")], # 'MegaRush',
              'ItemB':          [("Parakarry","Bow","CastleKey1")], # 'Coin',
              'ItemC':          [("Parakarry","Bow","CastleKey1")], # 'Coin',
              'ItemD':          [("Parakarry","Bow","CastleKey1")], # 'Coin',
              'ItemE':          [("Parakarry","Bow","CastleKey1")], # 'Coin',
              'ItemF':          [("Parakarry","Bow","CastleKey1")], # 'Coin',
              'ItemG':          [("Parakarry","Bow","CastleKey1")], # 'Coin'
              },
# Stairs to Third Floor
'DGB_14':    {'YBlockA':        [("Bow","CastleKey1","CastleKey1")], # 'MapleSyrup'
              },
# Sleeping Clubbas Room (3F)
'DGB_16':    {'ItemA':          [("Bow","CastleKey1","CastleKey1")], # 'CastleKey1'
              },
#TODO Missing: 'DGB_18': {'Chest': ("Bow","CastleKey1","CastleKey1","CastleKey1")} ' 'MysticalKey'
}