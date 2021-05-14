"""Requirements for item locations in nok: Koopa Region"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Pleasant Path Entry
'NOK_11':    {'YBlockA':        [],                 # 'Coin',
              'RBlockA':        [],                 # 'DizzyAttack',
              'YBlockB':        [],                 # 'FrightJar'
              },
# Pleasant Path Bridge
'NOK_12':    {'YBlockA':        [],                 # 'POWBlock',
              'ItemA':          [],                 # 'StarPiece',
              'ItemB':          [],                 # 'SleepySheep'
              },
# Pleasant Crossroads
'NOK_13':    {'HiddenPanel':    [],                 # 'StarPiece',
              'RBlockA':        [],                 # 'AttackFXB',
              'ItemA':          [],                 # 'HoneySyrup'
              },
# Koopa Village 1
'NOK_01':    {'ShopItemA':      [],                 # 'DizzyDial',
              'ShopItemB':      [],                 # 'POWBlock',
              'ShopItemC':      [],                 # 'FireFlower',
              'ShopItemD':      [],                 # 'HoneySyrup',
              'ShopItemE':      [],                 # 'VoltShroom',
              'ShopItemF':      [],                 # 'Mushroom',
              'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer",)], # 'StarPiece',
              'Bush6A_Drop1A':  [("p_KKF15",)],     # 'Glasses',
              'Bush7A_Drop1A':  [("p_KKF06",)],     # 'EmptyWallet'
              },
              #TODO Missing: DriedShroom in bush, KoopaLeaf in bush, Letter03 to Mort T.
              #TODO          Letter14 to Koover, Letter16 to Koover
# Koopa Village 2
'NOK_02':    {'ItemA':          [],                 # 'StarPiece',
              'GiftA':          [],                 # 'KoopaLegends',
              'GiftB':          [],                 # 'SilverCredit',
              'GiftC':          [],                 # 'GoldCredit'
              },
              #TODO maybe missing: 3x StarPiece for Koopa Koot Favor x5
# Behind Koopa Village
'NOK_03':    {'ItemA':          [],                 # 'HPPlusB'
              },
# Fuzzy Forest
'NOK_04':    {'GiftA':          [],                 # 'KoopersShell'
              },
# Path to Fortress 1
'NOK_14':    {'HiddenPanel':    [],                 # 'StarPiece',
              'ItemA':          [],                 # 'Coin',
              'ItemB':          [],                 # 'Coin',
              'ItemC':          [],                 # 'Coin',
              'ItemD':          [],                 # 'Coin',
              'ItemE':          [],                 # 'Coin',
              'ItemF':          [],                 # 'ThunderBolt',
              'HiddenYBlockA':  [],                 # 'FireFlower'
              },
# Path to Fortress 2
'NOK_15':    {'Tree1_Drop1A':   [],                 # 'StarPiece'
              },
}