"""Requirements for item locations in kkj: Peach's Castle"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Guest Room (1F)
'KKJ_20':    {'ChestA':         [("CastleKey2","CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'LastStand'
              },
#TODO Missing: 'KKJ_29': {'WinQuizOff': []} # 'JamminJelly'
# Library (2F)
'KKJ_16':    {'ItemA':          [("CastleKey2","CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'LifeShroom',
              'ItemB':          [("CastleKey2","CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'PowerRush'
              },
# Storeroom (2F)
'KKJ_17':    {'ItemA':          [("CastleKey2","CastleKey2","CastleKey2","CastleKey2","p_OpenedStarWay","p_DarkDoor1")], # 'DeepFocus1'
              },
}