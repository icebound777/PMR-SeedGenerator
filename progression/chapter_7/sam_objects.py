"""Requirements for item locations in sam: Mt. Shiver"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Shiver City Mayor Area
'SAM_01':    {'HiddenPanel':    [("Sushie","UltraBoots")], # 'StarPiece',
              'GiftA':          [("Sushie","UltraBoots")], # 'Bucket',
              'ChestA':         [("Sushie","UltraBoots")], # 'AttackFXE'
              },
              #TODO Missing: Letter05 to Mayor
# Shiver City Center
'SAM_02':    {'ShopItemA':      [("Sushie","UltraBoots")], # 'DizzyDial',
              'ShopItemB':      [("Sushie","UltraBoots")], # 'ShootingStar',
              'ShopItemC':      [("Sushie","UltraBoots")], # 'SnowmanDoll',
              'ShopItemD':      [("Sushie","UltraBoots")], # 'MapleSyrup',
              'ShopItemE':      [("Sushie","UltraBoots")], # 'LifeShroom',
              'ShopItemF':      [("Sushie","UltraBoots")], # 'SuperShroom',
              'ItemA':          [("Sushie","UltraBoots")], # 'IcedPotato',
              'ItemB':          [("Sushie","UltraBoots","Bucket","Scarf")], # 'UltraShroom',
              'ItemC':          [("Sushie","UltraBoots","Bucket","Scarf")], # 'Mushroom',
              'ItemD':          [("Sushie","UltraBoots","Bucket","Scarf")], # 'Mushroom',
              'ItemE':          [("Sushie","UltraBoots","Bucket","Scarf")], # 'Mushroom',
              'ItemF':          [("Sushie","UltraBoots","Bucket","Scarf")], # 'Mushroom'
              },
# Shiver City Pond Area
'SAM_11':   {'ItemA':           [("Sushie","UltraBoots")], # 'WarehouseKey'
             },
# Shiver Snowfield
'SAM_04':    {'HiddenPanel':    [("Sushie","UltraBoots")],          # 'StarPiece',
              'ItemA':          [("Sushie","Hammer","UltraBoots")], # 'Letter05',
              'ItemB':          [("Sushie","UltraBoots")],          # 'RepelGel'
              },
# Path to Starborn Valley
'SAM_05':   {'ItemA':           [("Sushie","UltraBoots")], # 'Letter06',
             'HiddenYBlockA':   [("Sushie","UltraBoots")], # 'StopWatch'
             },
# Starborn Valley
'SAM_06':   {'GiftA':           [("Sushie","UltraBoots")], # 'Scarf'
             },
             #TODO Missing: Letter23 to Frost T.
# Shiver Mountain Passage
'SAM_07':   {'HiddenYBlockA':   [("Sushie","UltraBoots","Bucket","Scarf")], # 'UltraShroom'
             },
#TODO SAM_08 missing: Respawning Pebble
#TODO SAM_09 missing: 3 ice wall items
# Shiver Mountain Peaks
'SAM_10':   {'RBlockA':         [("Sushie","UltraBoots","Bucket","Scarf","StarStone")], # 'MegaJump',
             'ItemA':           [("Sushie","UltraBoots","Bucket","Scarf","StarStone")], # 'StarPiece'
             },
             # ! Can block off access to Merlar's Sanctuary if StarStone is gotten early
# Merlar's Sanctuary
'SAM_12':   {'ItemA':           [("Bombette","Sushie","UltraBoots","Bucket","Scarf")], # 'StarStone',
             'ItemB':           [("Bombette","Sushie","UltraBoots","Bucket","Scarf")], # 'StarStone'
             },
            #TODO duplicate?
}