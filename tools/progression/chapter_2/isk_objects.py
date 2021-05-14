"""Requirements for item locations in isk: Dry Dry Ruins"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Sarcophagus Hall 1
'ISK_02':    {'ItemA':          [("SuperHammer","PulseStone"),
                                 ("Bombette","Parakarry","PulseStone")], # 'SpikeShield'
              },
# Sand Drainage Room 1
'ISK_03':    {'ItemA':          [("SuperHammer","PulseStone"),
                                 ("Bombette","Parakarry","PulseStone")], # 'RuinsKey'
              },
# Pyramid Stone Room
'ISK_05':    {'ItemA':          [("SuperHammer","PulseStone","RuinsKey")], # 'PyramidStone'
              },
# Sand Drainage Room 2
'ISK_06':    {'ItemA':          [("Bombette","SuperHammer","PulseStone","RuinsKey"),
                                 ("Bombette","Parakarry","PulseStone","RuinsKey")], # 'StarPiece',
              'ItemB':          [("Bombette","SuperHammer","PulseStone","RuinsKey"),
                                 ("Bombette","Parakarry","PulseStone","RuinsKey")], # 'RuinsKey'
              },
# Sarcophagus Hall 2
'ISK_07':    {'ItemA':          [("SuperHammer","PulseStone","RuinsKey","RuinsKey"),
                                 ("Bombette","Parakarry","PulseStone","RuinsKey","RuinsKey")], # 'RuinsKey',
              'ItemB':          [("SuperHammer","PulseStone","RuinsKey","RuinsKey")], # 'Artifact'
              },
# Super Hammer Room
'ISK_09':    {'ChestA':         [("SuperHammer","Parakarry","PulseStone","RuinsKey","RuinsKey","RuinsKey"),
                                 ("Bombette","Parakarry","PulseStone","RuinsKey","RuinsKey","RuinsKey")], # 'SlowGo'
              },
              #TODO Missing: SuperHammer from big chest
# Sand Drainage Room 3
'ISK_12':    {'ItemA':          [("p_NYI",)]#[("SuperHammer","PulseStone","RuinsKey","RuinsKey","RuinsKey")], # 'RuinsKey'
              },
              #TODO Keep in mind this item can get flooded!
# Lunar Stone Room
'ISK_13':    {'ItemA':          [("SuperHammer","PulseStone","RuinsKey","RuinsKey","RuinsKey","RuinsKey")], # 'LunarStone'
              },
# Diamond Stone Room
'ISK_14':    {'ItemA':          [("Bombette","SuperHammer","PulseStone","RuinsKey","RuinsKey","RuinsKey"),
                                 ("Bombette","Parakarry","PulseStone","RuinsKey","RuinsKey","RuinsKey")], # 'DiamondStone'
              },
}