"""Requirements for item locations in iew: Mt. Rugged"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Train Station
'IWA_10':    {'GiftA':          [("p_NYI",)],       # 'Letter01',
              'GiftB':          [("p_NYI",)],       # 'Letter25',
              'GiftC':          [("p_NYI",)],       # 'Letter10'
              },
              # this ones a bit weird. Does Parakarry give back the letters once he joins you?
              #TODO Missing: Respawning Egg2 in bush
# Mt Rugged 1
'IWA_00':    {'ItemA':          [("SuperHammer",),
                                 ("Bombette",)],                 # 'Coin',
              'ItemB':          [("SuperHammer",),
                                 ("Bombette",)],                 # 'Coin',
              'ItemC':          [("SuperHammer",),
                                 ("Bombette",)],                 # 'Coin',
              'YBlockA':        [("SuperHammer",),
                                 ("Bombette",)],                 # 'SleepySheep',
              'ItemD':          [("SuperHammer",),
                                 ("Bombette","Hammer")],        # 'WhackasBump'
              },
              #TODO: Check: Does bombing Whacka give Whacka bumps like in the PAL version?
# Mt Rugged 2
'IWA_01':    {'HiddenPanel':    [("SuperHammer","SuperBoots"),
                                 ("UltraHammer",),
                                 ("Bombette","SuperBoots")],  # 'StarPiece',
              'ItemA':          [("Parakarry","SuperHammer"),
                                 ("Bombette","Parakarry")],   # 'QuakeHammer',
              'ItemB':          [("Parakarry","SuperHammer"),
                                 ("Bombette","Kooper"),
                                 ("Bombette","Parakarry")],   # 'Letter01'
              },
# Mt Rugged 3
'IWA_02':    {'ItemA':          [("SuperHammer",),
                                 ("Bombette",)],             # 'StarPiece',
              'GiftA':          [("Parakarry","SuperHammer"),
                                 ("Bombette","Parakarry")],  # 'MagicalSeed2'
              },
# Mt Rugged 4
'IWA_03':    {'ChestA':         [("SuperHammer",),
                                 ("Bombette",)],             # 'DamageDodgeB',
              'YBlockA':        [("SuperHammer",),
                                 ("Bombette","Hammer")],     # 'Coin',
              'YBlockB':        [("SuperHammer",),
                                 ("Bombette",)],             # 'Mushroom',
              'YBlockC':        [("SuperHammer"),
                                 ("Bombette","Hammer")],     # 'HoneySyrup',
              'ItemA':          [("SuperHammer",),
                                 ("Bombette",)],             # 'Letter25',
              'ItemB':          [("Parakarry","SuperHammer"),
                                 ("Bombette","Parakarry")],  # circle_center 'StarPiece',
              'ItemC':          [("Parakarry","SuperHammer"),
                                 ("Kooper","SuperHammer"),
                                 ("Kooper","Bombette"),
                                 ("Bombette","Parakarry")],  # circle_right 'Coin',
              'ItemD':          [("Parakarry","SuperHammer"),
                                 ("Bombette","Parakarry")],  # circle_left 'Coin',
              'ItemE':          [("Parakarry","SuperHammer"),
                                 ("Bombette","Parakarry")],  # circle_front_right 'Coin',
              'ItemF':          [("Parakarry","SuperHammer"),
                                 ("Bombette","Parakarry")],  # circle_front_left 'Coin',
              'ItemG':          [("Parakarry","SuperHammer"),
                                 ("Bombette","Parakarry")],  # circle_back_right 'Coin',
              'ItemH':          [("Parakarry","SuperHammer"),
                                 ("Bombette","Parakarry")],  # circle_back_left 'Coin',
              'ItemI':          [("SuperHammer",),
                                 ("Bombette",)],             # bottom_back 'Coin',
              'ItemJ':          [("SuperHammer",),
                                 ("Bombette",)],             # bottom_front 'Coin'
              },
# Suspension Bridge
'IWA_04':    {'ItemA':          [("SuperHammer"),
                                 ("Bombette",)],                 # 'Letter10'
              },
}