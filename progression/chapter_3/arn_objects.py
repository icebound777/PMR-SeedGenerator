"""Requirements for item locations in arn: Gusty Gulch"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Wasteland Ascent 1
'ARN_02':    {'ItemA':          [("Kooper",)],      # 'DizzyDial',
              'ItemB':          [],                 # 'Letter07',
              'YBlockA':        [],                 # 'Coin',
              'YBlockB':        [],                 # 'Coin',
              'YBlockC':        [],                 # 'RepelGel'
              },
# Ghost Town 1
'ARN_03':    {'GiftA':          [("p_KKF18")],      # 'Package',
              'YBlockA':        [],                 # 'Coin'
              },
# Wasteland Ascent 2
'ARN_04':    {'YBlockA':        [("Parakarry",)],   # 'SuperShroom',
              'YBlockB':        [("Parakarry",)],   # 'Coin',
              'ItemA':          [("Parakarry",)],   # 'StarPiece'
              },
}