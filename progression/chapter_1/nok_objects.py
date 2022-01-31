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
              'ItemA':          [("Kooper","Hammer")], # 'StarPiece',
              'ItemB':          [("Hammer",)],      # 'SleepySheep'
              },
# Pleasant Crossroads
'NOK_13':    {'HiddenPanel':    [("Hammer","SuperBoots"),
                                 ("UltraHammer")],  # 'StarPiece',
              'RBlockA':        [("Hammer",)],      # 'AttackFXB',
              'ItemA':          [("Hammer",)],      # 'HoneySyrup'
              },
# Koopa Village 1
'NOK_01':    {'ShopItemA':      [("Hammer",)],      # 'DizzyDial',
              'ShopItemB':      [("Hammer",)],      # 'POWBlock',
              'ShopItemC':      [("Hammer",)],      # 'FireFlower',
              'ShopItemD':      [("Hammer",)],      # 'HoneySyrup',
              'ShopItemE':      [("Hammer",)],      # 'VoltShroom',
              'ShopItemF':      [("Hammer",)],      # 'Mushroom',
              'HiddenPanel':    [("Hammer","SuperBoots"),
                                 ("UltraHammer",)], # 'StarPiece',
              'Bush6A_Drop1A':  [("Hammer","p_KKF15",)], # 'Glasses',
              'Bush7A_Drop1A':  [("Hammer","p_KKF06",)], # 'EmptyWallet'
              },
              #TODO Missing: DriedShroom in bush, KoopaLeaf in bush, Letter03 to Mort T.
              #TODO          Letter14 to Koover, Letter16 to Koover
# Koopa Village 2
'NOK_02':    {'ItemA':          [("Hammer","p_SavedKoopaVillage")], # 'StarPiece',
              'GiftA':          [("Hammer","p_KKF01")],             # 'KoopaLegends',
              'GiftB':          [("Hammer","p_KKF02")],             # 'SilverCredit',
              'GiftC':          [("Hammer","p_KKF10")],             # 'GoldCredit'
              },
              #TODO maybe missing: 3x StarPiece for Koopa Koot Favor x5
# Behind Koopa Village
'NOK_03':    {'ItemA':          [("Hammer","Kooper"),
                                 ("Hammer","Parakarry")], # 'HPPlusB'
              },
# Fuzzy Forest
'NOK_04':    {'GiftA':          [("Hammer",)],      # 'KoopersShell'
              },
# Path to Fortress 1
'NOK_14':    {'HiddenPanel':    [("Hammer","SuperBoots"),
                                 ("UltraHammer",)], # 'StarPiece',
              'ItemA':          [("Hammer",)],      # 'Coin',
              'ItemB':          [("Hammer",)],      # 'Coin',
              'ItemC':          [("Hammer",)],      # 'Coin',
              'ItemD':          [("Hammer",)],      # 'Coin',
              'ItemE':          [("Hammer",)],      # 'Coin',
              'ItemF':          [("Kooper","Hammer"),
                                 ("SuperBoots", "Hammer")], # 'ThunderBolt',
              'HiddenYBlockA':  [("Kooper","Hammer")], # 'FireFlower'
              },
# Path to Fortress 2
'NOK_15':    {'Tree1_Drop1A':   [("Kooper","Hammer")], # 'StarPiece'
              },
}