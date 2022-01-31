"""Requirements for item locations in trd: Koopa Bros. Fortress"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Fortress Exterior
'TRD_00':    {'ChestA':         [("Kooper","Bombette","Hammer")], # 'Refund',
              'ChestB':         [("Kooper","Bombette","Hammer","FortressKey")], # 'FPPlusB'
              },
# Left Tower
'TRD_01':    {'ItemA':          [("Kooper","Hammer","FortressKey","FortressKey","FortressKey","FortressKey")], # 'SmashCharge',
              'ItemB':          [("Kooper","Hammer")], # 'FortressKey'
              },
# Central Hall
'TRD_03':    {'ItemA':          [("Kooper", "Bombette", "FortressKey", "FortressKey", "FortressKey")], # left 'FortressKey',
              'ItemB':          [("Kooper", "Bombette", "FortressKey")], # right 'FortressKey',
              'ItemC':          [("Kooper","Hammer","FortressKey")], # 'PowerBounce'
              },
# Dungeon Fire Room
'TRD_08':    {'ItemA':          [("Kooper","Hammer","FortressKey")], # 'FortressKey'
              },
# Battlement
'TRD_09':    {'YBlockA':        [("Kooper","Bombette","Hammer","FortressKey","FortressKey","FortressKey","FortressKey")], # 'MapleSyrup'
              },
}