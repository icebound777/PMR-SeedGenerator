"""Requirements for item locations in kzn: Mt. Lavalava"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Central Cavern
'KZN_03':   {'ItemA':           [("p_TalkedToRaphael",)],                 # 'FireShield',
             'ItemB':           [("Kooper","p_TalkedToRaphael"),
                                 ("UltraBoots","p_TalkedToRaphael")],     # 'POWBlock',
             'YBlockA':         [("p_TalkedToRaphael",)],                 # 'Coin',
             'YBlockB':         [("p_TalkedToRaphael",)],                 # 'Coin',
             'YBlockC':         [("p_TalkedToRaphael",)],                 # 'Coin',
             'YBlockD':         [("p_TalkedToRaphael",)],                 # 'Coin'
             },
# Flowing Lava Puzzle
'KZN_06':   {'HiddenYBlockA':   [("p_TalkedToRaphael",)],                 # 'LifeShroom'
             },
#TODO Missing: 'KZN_07': {'BigChest': [],} # 'UltraHammer'
# Dizzy Stomp Room
'KZN_08':   {'ChestA':          [("Parakarry","UltraHammer","p_TalkedToRaphael")], # 'DizzyStomp'
             },
# Zipline Cavern
'KZN_09':    {'HiddenPanel':    [("UltraHammer","p_TalkedToRaphael"),
                                 ("SuperBoots","p_TalkedToRaphael")], # 'StarPiece'
              },
# Boss Antechamber
'KZN_18':    {'HiddenPanel':    [("UltraHammer","p_TalkedToRaphael",)], # 'StarPiece'
              },
# Boss Room
'KZN_19':   {'YBlockA':         [("UltraHammer","p_TalkedToRaphael")], # 'SuperShroom',
             'YBlockB':         [("UltraHammer","p_TalkedToRaphael")], # 'MapleSyrup'
             },
}