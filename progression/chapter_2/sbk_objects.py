"""Requirements for item locations in sbk: Dry Dry Desert"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# N3W3
'SBK_00':    {'YBlockA':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'FrightJar',
              'YBlockB':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Coin'
              },
# N3E2 Pokey Army
'SBK_05':    {'ItemA':          [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'FireFlower'
              },
# N2W3
'SBK_10':    {'HiddenYBlockA':  [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'ThunderRage'
              },
# N2E1 (Tweester A)
'SBK_14':    {'YBlockA':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Coin',
              'YBlockB':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'HoneySyrup'
              },
# N1W3 Special Block
'SBK_20':    {'YBlockA':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Mushroom',
              'YBlockB':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'SuperShroom',
              'YBlockC':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'UltraShroom'
              },
# N1W1
'SBK_22':    {'YBlockA':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Coin',
              'YBlockB':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Coin',
              'YBlockC':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Coin',
              'YBlockD':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Coin',
              'YBlockE':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'FireFlower'
              },
# N1E1 Palm Trio
'SBK_24':    {'HiddenRBlockA':  [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'RunawayPay'
              },
# W3 Kolorado's Camp
'SBK_30':    {'Tree2_Drop1A':   [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'Letter02'
              },
              #TODO Missing: Artifact to Kolorado
              #TODO Kolorado needs to leave before tree is available
# Center (Tweester C)
'SBK_33':    {'HiddenPanel':    [("UltraHammer",),
                                 ("Bombette","Parakarry","SuperBoots")], # 'StarPiece'
              },
#TODO Missing: 'SBK_34': {'GiftA': []} # StarPiece from Letter08 to Nomadimouse
# E3 Outside Outpost
'SBK_36':    {'Tree9_Drop1A':   [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Letter03'
              },
# S1
'SBK_43':    {'YBlockA':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Coin'
              },
# S1E2 Small Bluffs
'SBK_45':    {'ItemA':          [("Kooper","SuperHammer"),
                                 ("SuperHammer", "SuperBoots"),
                                 ("Kooper","Bombette","Parakarry"),
                                 ("Bombette","Parakarry","SuperBoots")], # 'StopWatch',
              'ItemB':          [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'SpinAttack'
              },
#S1E3 North of Oasis
'SBK_46':    {'YBlockA':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Coin',
              'HiddenYBlockA':  [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'LifeShroom'
              },
# S2E2 West of Oasis
'SBK_55':    {'ItemA':          [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'TastyTonic'
              },
# S2E3 Oasis
'SBK_56':    {'Tree1_Drop1A':   [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Lemon',
              'Tree2_Drop1A':   [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Lime'
              },
# S3W2 Hidden AttackFX
'SBK_61':    {'HiddenRBlockA':  [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'AttackFXC'
              },
# S3E1
'SBK_64':    {'YBlockA':        [("SuperHammer",),
                                 ("Bombette","Parakarry","Hammer")], # 'Coin'
              },
}