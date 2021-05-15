"""Requirements for item locations in kpa: Bowser's Castle"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Ship Enter/Exit Scenes
'KPA_60':    {'RBlockA':         [("Lakilester","CastleKey2","p_OpenedStarWay")], # 'DeepFocus3'
              },
              # * kpa_60.RBlockA and kpa_62.RBlockA are the same, keep in mind when writing logic!
#Front Door Exterior
'KPA_62':    {'RBlockA':         [("Lakilester","CastleKey2","p_OpenedStarWay")], # 'DeepFocus3'
              },
              # * kpa_60.RBlockA and kpa_62.RBlockA are the same, keep in mind when writing logic!
# Outside Lower Jail (No Lava)
'KPA_10':    {'YBlockA':         [("Lakilester","CastleKey2","p_OpenedStarWay")], # 'LifeShroom'
              },
              # * kpa_10.YBlockA and kpa_11.YBlockA are the same, keep in mind when writing logic!
              # ! Keep in mind that CastleKey2 is no longer available after cooling off lava
              # ! Keep in mind that Dark Cave and Lava Channel must be traversed backwards if GuardDoor starts opened
# Outside Lower Jail (Lava)
'KPA_11':    {'ItemA':           [("p_OpenedStarWay",)],                # 'CastleKey2',
              'YBlockA':         [("Lakilester","CastleKey2","p_OpenedStarWay")], # 'LifeShroom'
              },
              # * kpa_10.YBlockA and kpa_11.YBlockA are the same, keep in mind when writing logic!
              # ! Keep in mind that Dark Cave and Lava Channel must be traversed backwards if GuardDoor starts opened
# Lower Jail
'KPA_17':    {'CrateA':          [("SuperBoots","CastleKey2","p_OpenedStarWay")], # 'TastyTonic',
              'CrateB':          [("SuperBoots","CastleKey2","p_OpenedStarWay")], # 'LifeShroom'
              },
              # ! Keep in mind that Dark Cave and Lava Channel must be traversed backwards if GuardDoor starts opened
# Lava Channel 3
'KPA_14':    {'ItemA':           [("Parakarry","Bow","Lakilester","CastleKey2","p_OpenedStarWay")], # 'Mystery',
              'ItemB':           [("Parakarry","Bow","Lakilester","CastleKey2","p_OpenedStarWay")], # 'ThunderRage'
              },
              # ! Keep in mind that Dark Cave and Lava Channel must be traversed backwards if GuardDoor starts opened
# Lava Key Room
'KPA_15':    {'ChestA':          [("Parakarry","Bow","Lakilester","CastleKey2","p_OpenedStarWay")], # 'CastleKey2'
              },
              # ! Keep in mind that Dark Cave and Lava Channel must be traversed backwards if GuardDoor starts opened
# Dark Cave 1
'KPA_01':    {'YBlockA':         [("Parakarry","Bow","Lakilester","CastleKey2","CastleKey2","p_OpenedStarWay")], # 'POWBlock'
              },
              # ! Keep in mind that Dark Cave and Lava Channel must be traversed backwards if GuardDoor starts opened
# Dark Cave 2
'KPA_03':    {'YBlockA':         [("Parakarry","Bow","Lakilester","CastleKey2","CastleKey2","p_OpenedStarWay")], # 'ShootingStar'
              },
              # ! Keep in mind that Dark Cave and Lava Channel must be traversed backwards if GuardDoor starts opened
# East Upper Jail
'KPA_91':    {'ItemA':           [("p_OpenedStarWay","p_DarkDoor1")], # 'PrisonKey1'
              },
# Item Shop
'KPA_96':    {'ShopItemA':       [("p_OpenedStarWay","p_DarkDoor1")], # 'Mystery',
              'ShopItemB':       [("p_OpenedStarWay","p_DarkDoor1")], # 'DizzyDial',
              'ShopItemC':       [("p_OpenedStarWay","p_DarkDoor1")], # 'POWBlock',
              'ShopItemD':       [("p_OpenedStarWay","p_DarkDoor1")], # 'ThunderRage',
              'ShopItemE':       [("p_OpenedStarWay","p_DarkDoor1")], # 'MapleSyrup',
              'ShopItemF':       [("p_OpenedStarWay","p_DarkDoor1")], # 'SuperShroom'
              },
# Left Water Puzzle
'KPA_133':   {'ItemA':           [("Bombette","Sushie","p_OpenedStarWay","p_DarkDoor1")], # 'CastleKey2'
              },
# Right Water Puzzle
'KPA_134':   {'HiddenYBlockA':   [("Bombette","Sushie","p_OpenedStarWay","p_DarkDoor1")], # 'MapleSyrup'
              },
# Room with Hidden Door 1
'KPA_111':   {'YBlockA':         [("CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'SuperShroom',
              'HiddenYBlockA':   [("CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'MapleSyrup'
              },
# Hidden Key Room
'KPA_119':   {'ItemA':           [("CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'CastleKey2'
              },
# Battlement
'KPA_61':    {'YBlockA':         [("CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'SuperShroom',
              'YBlockB':         [("CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'MapleSyrup',
              'YBlockC':         [("CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'SuperShroom',
              'ItemA':           [("CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'JamminJelly'
              },
# West Upper Jail
'KPA_95':    {'ItemA':           [("CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'PrisonKey1'
              },
# Ultra Shroom Room
'KPA_101':   {'ItemA':           [("Bombette","CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'UltraShroom'
              },
# Castle Key Room
'KPA_100':   {'ItemA':           [("Bombette","CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'CastleKey2'
              },
}