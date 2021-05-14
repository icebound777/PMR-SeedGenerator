"""Requirements for item locations in obk: Boo's Mansion"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Foyer
'OBK_01':    {'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer")],  # 'StarPiece',
              'GiftA':          [("p_KKF12",)],     # 'OldPhoto'
              },
              #TODO Missing: Letter12 to Franky
# Pot Room
'OBK_05':    {'CrateA':         [("SuperBoots",)],  # 'Apple',
              'CrateB':         [("SuperBoots",)],  # 'Apple'
              },
# Record Room
'OBK_08':    {'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer")],  # 'StarPiece',
              'ItemA':          [],                 # 'Record'
              },
# Record Player Room
'OBK_07':    {'ChestA':         [("Record",)],      # 'Weight'
              },
# Basement Stairs
'OBK_02':    {'HiddenPanel':    [("Weight",)],      # 'StarPiece'
              },
# Basement
'OBK_03':    {'ShopItemA':      [],                 # 'Mystery',
              'ShopItemB':      [],                 # 'StopWatch',
              'ShopItemC':      [],                 # 'SnowmanDoll',
              'ShopItemD':      [],                 # 'MapleSyrup',
              'ShopItemE':      [],                 # 'LifeShroom',
              'ShopItemF':      [],                 # 'SuperShroom',
              'CrateA':         [("SuperBoots","Weight")], # 'SuperShroom'
              },
              #TODO Missing: Letter11 to Igor
# Super Boots Room
'OBK_04':    {'HiddenPanel':    [("SuperBoots","Weight"),
                                 ("UltraHammer","Weight")], # 'StarPiece',
              'CrateA':         [("SuperBoots","Weight")],  # 'MapleSyrup'
              },
              #TODO Missing: SuperBoots
# Library
'OBK_06':    {'ItemA':          [("Parakarry","SuperBoots")], # 'BoosPortrait',
              'CrateA':         [("SuperBoots",)],            # 'StarPiece'
              },
              # * Can softlock in library if entered from the top w/o Bombette
}