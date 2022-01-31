"""Requirements for item locations in flo: Flower Fields"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
#TODO flo as a whole is very story trigger locked. these are missing in here for now
# (East) Triple Tree Path
'FLO_09':    {'ItemA':          [("Hammer","p_OpenedFlowerFields")],        # 'HappyFlowerB'
              },
              #TODO Missing: Respawning StinkyHerb from ivy
# (East) Petunia's Field
'FLO_03':    {'HiddenPanel':    [("SuperBoots","p_OpenedFlowerFields"),
                                 ("UltraHammer","p_OpenedFlowerFields")],   # 'StarPiece',
              'GiftA':          [("p_OpenedFlowerFields")],                 # 'MagicalBean'
              },
              #TODO Missing: Respawning RedBerry drops x2 from tree
# (East) Old Well
'FLO_22':    {'ItemA':          [("p_OpenedFlowerFields")],                 # 'FlowerSaverB',
              'ItemB':          [("p_OpenedFlowerFields")],                 # 'FlowerSaverB'
              },
              #TODO duplicates
              #TODO add BlueBerry to requirement
# (SW) Path to Crystal Tree
'FLO_25':    {'HiddenPanel':    [("SuperBoots","p_OpenedFlowerFields"),
                                 ("UltraHammer","p_OpenedFlowerFields")],   # 'StarPiece'
              },
              #TODO Missing: Respawning StinkyHerb from ivy, Respawning YellowBerry x2 from tree
              #TODO add RedBerry to requirement
# (SW) Posie and Crystal Tree
'FLO_07':    {'ItemA':          [("p_OpenedFlowerFields")],                 # 'CrystalBerry',
              'ItemB':          [("p_OpenedFlowerFields")],                 # 'CrystalBerry',
              'GiftA':          [("p_OpenedFlowerFields")],                 # 'FertileSoil',
              'ItemC':          [("p_OpenedFlowerFields")],                 # 'CrystalBerry',
              'ItemD':          [("p_OpenedFlowerFields")],                 # 'CrystalBerry'
              },
              #TODO duplicates
              #TODO
# (NE) Elevators
'FLO_16':    {'ItemA':          [("Lakilester","SuperBoots","p_OpenedFlowerFields")], # 'StarPiece'
              },
              #TODO Missing: Respawning StinkyHerb from ivy
# (NE) Fallen Logs
'FLO_17':    {'HiddenYBlockA':  [("Lakilester","SuperBoots","p_OpenedFlowerFields")], # 'ThunderRage',
              'ItemA':          [("Lakilester","SuperBoots","p_OpenedFlowerFields")], # 'Letter09'
              },
# (SE) Briar Platforming
'FLO_08':    {'ItemA':          [("Parakarry","p_OpenedFlowerFields")], # 'StarPiece'
              },
              #TODO Missing: Respawning StinkyHerb from ivy, Respawning BlueBerry x2 from tree
              # TODO add YellowBerry to requirement
# (SE) Water Level Room
'FLO_24':    {'HiddenPanel':    [("Parakarry","SuperBoots","p_OpenedFlowerFields"),
                                 ("Parakarry","UltraHammer","p_OpenedFlowerFields")], # 'StarPiece',
              'YBlockA':        [("Parakarry","p_OpenedFlowerFields")],     # 'DizzyDial',
              'HiddenYBlockA':  [("Parakarry","p_OpenedFlowerFields")],     # 'MapleSyrup'
              },
              #TODO Missing: Respawning BubbleBerry x2 from tree
              # TODO add YellowBerry to requirement
# (SE) Lily's Fountain
'FLO_10':    {'GiftA':          [("p_OpenedFlowerFields")],                 # 'MiracleWater'
              },
              #TODO Missing: JamminJelly from tree
              # TODO add YellowBerry to requirement
# (West) Path to Maze
'FLO_23':    {'HiddenYBlockA':  [("p_OpenedFlowerFields")],                 # 'ShootingStar',
              'HiddenYBlockB':  [("p_OpenedFlowerFields")],                 # 'Coin'
              },
              #TODO add BlueBerry to requirement
# (West) Rosie's Trellis
'FLO_12':    {'GiftA':          [("p_OpenedFlowerFields")],                 # 'WaterStone'
              },
              #TODO add BlueBerry to requirement
# (NW) Bubble Flower
'FLO_14':    {'ItemA':          [("p_OpenedFlowerFields")],                 # 'StarPiece'
              },
              #TODO Missing: Respawning StinkyHerb from ivy
# (NW) Lakilester
'FLO_13':    {'ItemA':          [("Lakilester","p_OpenedFlowerFields")], # 'MegaSmash',
              'ItemB':          [("Lakilester","p_OpenedFlowerFields")], # 'ShootingStar'
              },
              #TODO add BubbleBerry to requirements
# Cloudy Climb
'FLO_19':    {'ItemA':          [("p_OpenedFlowerFields", "p_PlantedBeanstalk")], # 'SJumpChg'
              },
}