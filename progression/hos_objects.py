"""Requirements for item locations in hos: Shooting Star Summit"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Shooting Star Path
'HOS_00':    {'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer",)], # 'StarPiece'
              },
              #TODO maybe missing: LuckyStar by Twink
# Shooting Star Summit
'HOS_01':    {'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer",)], # 'StarPiece',
              'ItemA':          [],                 # 'StarPiece'
              },
# Merluvlee's House
'HOS_06':    {'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer",)], # 'StarPiece',
              'GiftA':          [("CrystalBall","p_KKF08")], # 'Autograph2'
              },
              #TODO Missing: Letter06 to Merlow, Merlow's Badge x 15
# Star Haven
'HOS_03':    {'ShopItemA':      [("p_OpenedStarWay",)], # 'StopWatch',
              'ShopItemB':      [("p_OpenedStarWay",)], # 'ShootingStar',
              'ShopItemC':      [("p_OpenedStarWay",)], # 'SuperSoda',
              'ShopItemD':      [("p_OpenedStarWay",)], # 'MapleSyrup',
              'ShopItemE':      [("p_OpenedStarWay",)], # 'LifeShroom',
              'ShopItemF':      [("p_OpenedStarWay",)], # 'SuperShroom'
              },
}