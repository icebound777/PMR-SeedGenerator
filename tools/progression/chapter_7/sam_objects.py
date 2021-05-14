"""Requirements for item locations in sam: Mt. Shiver"""
requirements = {
#Map          ItemLocation      Requires            VanillaItem
# Shiver City Mayor Area
'SAM_01':    {'HiddenPanel':    [],                 # 'StarPiece',
              'GiftA':          [],                 # 'Bucket',
              'ChestA':         [],                 # 'AttackFXE'
              },
              #TODO Missing: Letter05 to Mayor
# Shiver City Center
'SAM_02':    {'ShopItemA':      [],                 # 'DizzyDial',
              'ShopItemB':      [],                 # 'ShootingStar',
              'ShopItemC':      [],                 # 'SnowmanDoll',
              'ShopItemD':      [],                 # 'MapleSyrup',
              'ShopItemE':      [],                 # 'LifeShroom',
              'ShopItemF':      [],                 # 'SuperShroom',
              'ItemA':          [],                 # 'IcedPotato',
              'ItemB':          [("Bucket", "Scarf")], # 'UltraShroom',
              'ItemC':          [("Bucket", "Scarf")], # 'Mushroom',
              'ItemD':          [("Bucket", "Scarf")], # 'Mushroom',
              'ItemE':          [("Bucket", "Scarf")], # 'Mushroom',
              'ItemF':          [("Bucket", "Scarf")], # 'Mushroom'
              },
# Shiver City Pond Area
'SAM_11':   {'ItemA':           [],                 # 'WarehouseKey'
             },
# Shiver Snowfield
'SAM_04':    {'HiddenPanel':    [],                 # 'StarPiece',
              'ItemA':          [],                 # 'Letter05',
              'ItemB':          [],                 # 'RepelGel'
              },
# Path to Starborn Valley
'SAM_05':   {'ItemA':           [],                 # 'Letter06',
             'HiddenYBlockA':   [],                 # 'StopWatch'
             },
# Starborn Valley
'SAM_06':   {'GiftA':           [],                 # 'Scarf'
             },
             #TODO Missing: Letter23 to Frost T.
# Shiver Mountain Passage
'SAM_07':   {'HiddenYBlockA':   [],                 # 'UltraShroom'
             },
#TODO SAM_08 missing: Respawning Pebble
#TODO SAM_09 missing: 3 ice wall items
# Shiver Mountain Peaks
'SAM_10':   {'RBlockA':         [],                 # 'MegaJump',
             'ItemA':           [],                 # 'StarPiece'
             },
# Merlar's Sanctuary
'SAM_12':   {'ItemA':           [],                 # 'StarStone',
             'ItemB':           [],                 # 'StarStone'
             },
            #TODO duplicate?
}