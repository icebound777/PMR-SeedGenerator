"""Requirements for item locations in kpa: Bowser's Castle"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Ship Enter/Exit Scenes
'KPA_60':    {'RBlockA':         [],                # 'DeepFocus3'
              },
             # kpa_60.RBlockA and kpa_62.RBlockA are the same, keep in mind when writing logic!
#Front Door Exterior
'KPA_62':    {'RBlockA':         [],                # 'DeepFocus3'
              },
             # kpa_60.RBlockA and kpa_62.RBlockA are the same, keep in mind when writing logic!
# Outside Lower Jail (No Lava)
'KPA_10':    {'YBlockA':         [],                # 'LifeShroom'
              },
             # kpa_10.YBlockA and kpa_11.YBlockA are the same, keep in mind when writing logic!
             #TODO Keep in mind that CastleKey2 is no longer available after turning off lava!!!
# Outside Lower Jail (Lava)
'KPA_11':    {'ItemA':           [],                # 'CastleKey2',
              'YBlockA':         [],                # 'LifeShroom'
              },
             # kpa_10.YBlockA and kpa_11.YBlockA are the same, keep in mind when writing logic!
# Lower Jail
'KPA_17':    {'CrateA':          [],                # 'TastyTonic',
              'CrateB':          [],                # 'LifeShroom'
              },
# Lava Channel 3
'KPA_14':    {'ItemA':           [],                # 'Mystery',
              'ItemB':           [],                # 'ThunderRage'
              },
# Lava Key Room
'KPA_15':    {'ChestA':          [],                # 'CastleKey2'
              },
# Dark Cave 1
'KPA_01':    {'YBlockA':         [],                # 'POWBlock'
              },
# Dark Cave 2
'KPA_03':    {'YBlockA':         [],                # 'ShootingStar'
              },
# East Upper Jail
'KPA_91':    {'ItemA':           [],                # 'PrisonKey1'
              },
# Item Shop
'KPA_96':    {'ShopItemA':      [],                 # 'Mystery',
              'ShopItemB':      [],                 # 'DizzyDial',
              'ShopItemC':      [],                 # 'POWBlock',
              'ShopItemD':      [],                 # 'ThunderRage',
              'ShopItemE':      [],                 # 'MapleSyrup',
              'ShopItemF':      [],                 # 'SuperShroom'
              },
# Left Water Puzzle
'KPA_133':   {'ItemA':           [],                # 'CastleKey2'
              },
# Right Water Puzzle
'KPA_134':   {'HiddenYBlockA':   [],                # 'MapleSyrup'
              },
# Room with Hidden Door 1
'KPA_111':   {'YBlockA':         [],                # 'SuperShroom',
              'HiddenYBlockA':   [],                # 'MapleSyrup'
              },
# Hidden Key Room
'KPA_119':   {'ItemA':           [],                # 'CastleKey2'
              },
# Battlement
'KPA_61':    {'YBlockA':         [],                # 'SuperShroom',
              'YBlockB':         [],                # 'MapleSyrup',
              'YBlockC':         [],                # 'SuperShroom',
              'ItemA':           [],                # 'JamminJelly'
              },
# West Upper Jail
'KPA_95':    {'ItemA':           [],                # 'PrisonKey1'
              },
# Ultra Shroom Room
'KPA_101':   {'ItemA':           [],                # 'UltraShroom'
              },
# Castle Key Room
'KPA_100':   {'ItemA':           [],                # 'CastleKey2'
              },
}