"""Requirements for item locations in dro: Dry Dry Outpost"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Outpost 1
'DRO_01':    {'ShopItemA':      [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'ThunderBolt',
              'ShopItemB':      [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'DustyHammer',
              'ShopItemC':      [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'HoneySyrup',
              'ShopItemD':      [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'DriedShroom',
              'ShopItemE':      [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'DriedPasta',
              'ShopItemF':      [("SuperHammer",),
                                 ("Bombette","Parakarry")], # 'Mushroom',
              'GiftA':          [("SuperHammer","Lyrics"),
                                 ("Bombette","Parakarry","Lyrics")], # 'Melody',
              'GiftB':          [("SuperHammer"),
                                 ("Bombette","Parakarry")], # 'RedJar'
              },
# Outpost 2
'DRO_02':    {'HiddenPanel':    [("UltraHammer",),
                                 ("Bombette","Parakarry","SuperBoots")], # 'StarPiece',
              'ItemA':          [("SuperHammer"),
                                 ("Bombette","Parakarry")], # 'Letter08',
              'GiftA':          [("SuperHammer","p_KKF08"),
                                 ("Bombette","Parakarry","p_KKF08")], # 'CrystalBall',
              'GiftB':          [("SuperHammer"),
                                 ("Bombette","Parakarry")], # 'PulseStone'
              },
              #TODO Missing: Letter17 to Mr. E.
}