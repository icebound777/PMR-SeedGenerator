"""Requirements for item locations in mac: Toad Town"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Gate District
'MAC_00':    {'ShopItemA':      [],                 # 'FrightJar',
              'ShopItemB':      [],                 # 'SleepySheep',
              'ShopItemC':      [],                 # 'POWBlock',
              'ShopItemD':      [],                 # 'FireFlower',
              'ShopItemE':      [],                 # 'HoneySyrup',
              'ShopItemF':      [],                 # 'Mushroom',
              'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer",)], # 'StarPiece'
              'ItemA':          [("Sushie",)],      # 'StarPiece'
              },
              #TODO Missing: Radio Trade Event, Dictionary to Russ T., Letter04 to Russ T.,
              #TODO          Letter18 to Miss T.
# Plaza District
'MAC_01':    {'ItemA':          [("SuperBoots",)],  # 'QuickChange',
              'Tree1_Drop1A':   [("Hammer",)],      # 'StarPiece'
              },
              #TODO Missing: Calculator to Rowf, Mailbag to Postman, Letter01 to Merlon,
              #TODO          Letter09 to Minh T., Badge Shop x16
# Southern District
'MAC_02':    {'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer",)], # 'StarPiece',
              'ItemA':          [("Bombette","Sushie","SuperBoots")], # 'OddKey',
              'GiftA':          [],                 # 'MagicalSeed1'
              },
              #TODO Missing: FryingPan to Tayce T., Letter07 to Fice T.
# Station District
'MAC_03':    {'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer",)], # 'StarPiece',
              'GiftA':          [("Parakarry","Letter20")], # 'Letter21',
              'GiftB':          [("Parakarry","Letter22")], # 'Letter23'
              },
              #TODO maybe missing: Lil' Oinks item x10
# Residental District
'MAC_04':    {'ShopItemA':      [],                 # 'StoneCap',
              'ShopItemB':      [],                 # 'DizzyDial',
              'ShopItemC':      [],                 # 'ThunderRage',
              'ShopItemD':      [],                 # 'TastyTonic',
              'ShopItemE':      [],                 # 'VoltShroom',
              'ShopItemF':      [],                 # 'SuperShroom'
              },
              #TODO Missing: Storeroom item x4
# Port District
'MAC_05':    {'HiddenPanel':    [("SuperBoots",),
                                 ("UltraHammer",)], # 'StarPiece',
              'GiftA':          [],                 # 'Lyrics'
              },
              #TODO Missing: Melody to Writer, Letter15 to Fishmael
}