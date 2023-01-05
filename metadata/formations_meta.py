# Don't randomize these formations at all
dont_randomize_formations = [
    "01-XX", # GoombaKing
    "02-02", # JrTroopa1
    "02-03", # JrTroopa2
    "02-04", # JrTroopa3
    "02-05", # JrTroopa4
    "02-06", # JrTroopa5
    "02-07", # JrTroopa6
    "03-XX", # Dojo fights
    "04-XX", # GoombarioTutor, ch8 Embers, Ch1 Magikoopa Miniboss
    "05-18", # KentCKoopa,
    "06-17", # Billblaster x3, having a flying ennemy in the back prevents jumping on the billblasters
    "07-XX", # NinjaKoopas
    "08-XX", # GoombarioTutor2
    "09-0C", # Buzzar
    "09-0E", # EmptyMoleHole
    "09-0F", # EmptyMoleHole
    "09-10", # Whacka
    "0B-08", # StoneChomp x3
    "0C-XX", # Tutankoopa
    "0E-0F", # TubbasHeart
    "0E-10", # TubbaBlubba
    "0F-04", # TubbaBlubba
    "0F-05", # TubbaBlubba
    "10-09", # MysteryNote ShyGuys
    "10-2C", # AntiGuy
    "10-30", # SlotMachine
    "11-XX", # GeneralGuy
    "12-XX", # Toybox Minibosses
    "13-XX", # Fuzzipede
    "17-XX", # LavaPiranha
    "18-0C", # thrown spinies
    "18-16", # CrazeeDayzee x2 + AmazyDayzee
    "18-1D", # AmazyDayzee + Bzzap x2
    "19-XX", # HuffNPuff / Spike
    "1A-XX", # Toad Town Tunnels
    "1B-XX", # Toad Town Tunnels
    "1C-XX", # Toad Town Tunnels
    "1B-XX", # Bloopers
    "1E-00", # Monstar
    "20-XX", # CrystalKing
    "21-0C", # unused
    "21-0D", # unused
    "21-0E", # unused
    "21-0F", # unused
    "21-10", # unused
    "21-11", # unused
    "21-12", # unused
    "21-13", # unused
    "23-XX", # Bowser
    "24-00", # AntiGuy x3, duplighosts
    "25-05", # unused
    "25-06", # unused
    "25-07", # unused
    "25-08", # unused
    "26-XX", # KammyKoopa
    "27-XX", # demo battles
]

# Do not randomize these enemies into any formations they're not home to
dont_randomize_enemies = [
    "01_BlueGoomba1",
    "01_RedGoomba1",
    "01_BlueGoomba2",
    "01_RedGoomba2",
    "01_GoombaKing",
    "02_JrTroopa1",
    "02_JrTroopa2",
    "02_JrTroopa3",
    "02_JrTroopa4",
    "02_JrTroopa5",
    "02_JrTroopa6",
    "04_Magiclone",
    "04_FlyingMagiclone",
    "05_KentC",
    "06_BillBlaster",
    "09_EmptyMoleHole",
    "09_Buzzar",
    "09_WhackaA",
    "09_WhackaB",
    "09_WhackaC",
    "0A_BanditB", # spawns a coin actor
    "0C_Chomp",
    "0C_Tutankoopa",
    "0E_TubbasHeart",
    "0E_TubbaBlubba",
    "0F_TubbaBlubba",
    "10_AntiGuy",
    "18_AmazyDayzee",
    "1D_GhostGoombario",
    "1D_GhostKooper",
    "1D_GhostBombette",
    "1D_GhostParakarry",
    "1D_GhostBow",
    "1D_GhostWatt",
    "1D_GhostSushie",
    "1D_GhostLakilester",
    "1D_GulpitRocks",
    "21_GhostGoombario",
    "21_GhostKooper",
    "21_GhostBombette",
    "21_GhostParakarry",
    "21_GhostBow",
    "21_GhostWatt",
    "21_GhostSushie",
    "21_GhostLakilester",
    "22_Magiclone",
    "22_FlyingMagiclone",
    "24_AntiGuy",
    "24_GhostGoombario",
    "24_GhostKooper",
    "24_GhostBombette",
    "24_GhostParakarry",
    "24_GhostBow",
    "24_GhostWatt",
    "24_GhostSushie",
    "24_GhostLakilester",
    "25_BombshellBlaster",
    "25_Magiclone",
    "25_FlyingMagiclone",
    "27_EmptyMoleHole",
]

chapter_battle_mapping = {
    -1: [
        "1A", # tik / Toad Town Tunnels enemies
        "1B", # tik / Toad Town Tunnels Blooper minibosses
        "1C", # tik / Toad Town Tunnels Swooper & Swoopulas ???
        "03", # mac / Dojo battles
        "08", # trd / GoombarioTutor2 (Star Power tutorial)
        "27", # dig / demo reel battles
    ],
    0: [
        "00", # kmr / prolog enemies
        "01", # kmr / GoombaKing / GoombaBros
        "02", # kmr / JrTroopa & some random kmr enemies ???
    ],
    1: [
        "05", # nok / Koopa Region enemies
        "06", # trd / KoopaBros Fortress enemies
        "07", # trd / KoopaBros & FakeBowser
    ],
    2: [
        "09", # iwa / Mt. Rugged enemies
        "0A", # sbk / Dry Dry Desert enemies
        "0B", # isk / Dry Dry Ruins enemies
        "0C", # isk / Tutankoopa
    ],
    3: [
        "0D", # mim / Forever Forest enemies
        "0E", # arn / Gusty Gulch enemies
        "0F", # dgb / Tubba's Castle enemies
    ],
    4: [
        "10", # omo / ShyGuys Toybox enemies (incl. AntiGuy)
        "11", # omo / GeneralGuy and his ToyTank
        "12", # omo / ShyGuys Toybox minibosses and SlotMachine enemies
        "29", # omo / ShySquad only -> summon for GeneralGuy
        "2A", # omo / StiltGuy only -> summon for GeneralGuy
        "2B", # omo / ShyStack only -> summon for GeneralGuy
        "2C", # omo / ShyGuy only ?? -> summon for GeneralGuy
        "2D", # omo / ShySquad only -> summon for GeneralGuy
        "2E", # omo / ShyGuy only ?? -> summon for GeneralGuy
    ],
    5: [
        "13", # kgr / Inside the Whale Fuzzipede
        "14", # jan / Jade Jungle enemies
        "15", # jan / Jade Jungle minibosses
        "16", # kzn / Mt. Lavalava enemies
        "17", # kzn / LavaPiranha
    ],
    6: [
        "18", # flo / Flower Fields enemies
        "19", # flo / HuffnPuff & Spike & MontyMoles
    ],
    7: [
        "1D", # sam / Shiver Mountain enemies
        "1E", # sam / Shiver Mountain Monstar
        "1F", # pra / Crystal Palace enemies
        "20", # pra / Crystal King
        "21", # pra / Duplighosts ???
    ],
    8: [
        "04", # hos / ch8 Embers & GoombarioTutor & MagiKoopa miniboss
        "22", # kpa / Bowser's Castle enemies
        "23", # kpa / Bowser variations
        "24", # kpa / Duplighost and AntiGuy minibosses
        "25", # kpa / BombshellBlasters
        "26", # kkj / KammyKoopa
    ],
}

# Some battle stages have a ceiling for enemies to roost on. 
battlestage_ceilings = {
    "isk_bt04": 133,
    "isk_bt05": 112,
    "isk_bt08": 133,
    "pra_bt01": 133,
}

# Dict of battles that take place on stages with ceilings
battlestage_ceiling_formations = {
    "isk_bt04": [
        "0B-02",
        "0B-03",
        "0B-04",
        "0B-05",
        "0B-06",
    ],
    "isk_bt05": [
        "0B-0B",
        "0B-0C",
        "0B-0D",
        "0B-0E",
        "0B-0F",
        "0B-10",
        "0B-11",
        "0B-12",
        "0B-13",
    ],
    "isk_bt08": [], # unused stage (sadly; it looks cool)
    "pra_bt01": [
        "1F-00",
        "1F-01",
        "1F-02",
        "1F-03",
        "1F-04",
        "1F-05",
        "1F-06",
        "1F-07",
        "1F-08",
        "1F-09",
        "1F-0A",
        "1F-0B",
        "1F-0C",
        "1F-0D",
        "1F-0E",
        "21-00",
        "21-01",
        "21-02",
        "21-03",
        "21-04",
        "21-05",
        "21-06",
        "21-07",
        "21-08",
        "21-09",
        "21-0A",
        "21-0B",
    ],
}

# Handle these formation ids specially
special_random_formations = [
    "06-17", # Billblaster x3 -> add one extra random enemy
    "0B-07", # StoneChomp x2 -> add one extra random enemy
    "18-1C", # AmazyDayzee -> add one extra random enemy
    "25-02", # BombshellBlaster -> add one extra random enemy
    "25-03", # BombshellBlaster -> replace Koopatrol with random enemy
    "25-04", # BombshellBlaster -> replace Koopatrol with random enemy
]

# Some enemies have variable starting conditions coded via actor_vars
random_actor_vars = {
    "0B_BuzzyBeetle": {
        "Var0": [1] # If attached to ceiling, must set Var0 to 1.
    },
    #"14_SpearGuy": {
    #    "Var0": [0,1] # Spear pointing forward or upward
    #},
    "18_Spiny": {
        "Var0": [0,1] #  ?
    },
    "22_BonyBeetle": {
        "Var0": [0,1] # Spikes out or not
    }
}

# When Gulpits are present within a formation, add the gulpit rocks to the
# formation. Since gulpit rocks start at turn order 09, other enemies have to
# start on turn order 14
# The battle id has to be AND'ed with the first value in each row for complete
# the first words
gulpit_rocks = [
    0x0000FF09, 0x802295C4, 0xFFDD0000, 0xFFCC0000,
    0x0000FF08, 0x802295C4, 0xFFEC0000, 0xFFCE0000,
    0x0000FF07, 0x802295C4, 0xFFEF0000, 0xFFD80000,
    0x0000FF06, 0x802295C4, 0xFFF90000, 0xFFD00000,
    0x0000FF05, 0x802295C4, 0xFFE40000, 0xFFD20000,
]

flying_enemies = [
    "00_Paragoomba",
    "02_ParagoombaA",
    "02_ParagoombaB",
    "04_FlyingMagikoopa",
    "05_Paragoomba",
    "05_Paratroopa",
    "06_Paratroopa",
    "09_Buzzar",
    "0B_Swooper",
    "0D_Bzzap",
    "0E_HyperParagoomba",
    "10_MediGuy",
    "10_SkyGuy",
    "14_MediGuy",
    "15_FlyingWMagikoopa",
    "16_MediGuy",
    "16_FlyingRMagikoopa",
    "16_FlyingWMagikoopa",
    "18_Lakitu",
    "18_Bzzap",
    "18_RuffPuff",
    "18_MediGuy",
    "18_FlyingRMagikoopa",
    "18_FlyingGRNMagikoopa",
    "18_FlyingWMagikoopa",
    "18_FlyingYMagikoopa",
    "19_HuffNPuff",
    "19_TuffPuff",
    "19_Spike",
    "1A_DarkParatroopa",
    "1A_Paragloomba",
    "1B_Blooper",
    "1B_ElectroBlooper",
    "1B_SuperBlooper",
    "1B_BlooperBaby",
    "1C_Swooper",
    "1C_Swoopula",
    "1D_FlyingGRYMagikoopa",
    "1E_Paragoomba",
    "1E_FlyingGRYMagikoopa",
    "1F_Swoopula",
    "1F_FlyingRMagikoopa",
    "1F_FlyingGRNMagikoopa",
    "1F_FlyingYMagikoopa",
    "1F_FlyingGRYMagikoopa",
    "1F_FlyingWMagikoopa",
    "20_CrystalBitA",
    "20_CrystalBitB",
    "20_CrystalBitC",
    "21_Swoopula",
    "21_FlyingRMagikoopa",
    "21_FlyingGRYMagikoopa",
    "22_FlyingMagikoopa",
    "22_FlyingMagiclone",
    "25_FlyingMagikoopa",
    "25_FlyingMagiclone",
]

ceiling_enemies = [
    "0B_Swooper",
    "0B_BuzzyBeetle",
    "1C_Swooper",
    "1C_Swoopula",
    "1F_Swoopula",
    "21_Swoopula",
]

# List of all battles that are actually used in the vanilla game
vanilla_used_battles = [
    "00-00",
]

# During randomization, if we don't keep the front row enemy the same as the
# enemy seen in the field, then first strikes can get awkward.
front_row_enemies = {
    "00-00": "00_Goomba",
    "00-01": "00_Goomba",
    "00-02": "00_Goomba",
    "00-03": "00_Goomba",
    "00-04": "00_Goomba",
    "00-05": "00_Goomba",
    "00-06": "00_Goomba",
    "00-07": "00_Paragoomba",
    "00-08": "00_Paragoomba",
    "00-09": "00_Paragoomba",
    "00-0A": "00_SpikedGoomba",
    "00-0B": "00_SpikedGoomba",
    "01-00": "01_BlueGoomba1",
    "01-01": "01_GoombaKing",
    "02-00": "02_SpikedGoomba",
    "02-01": "02_ParagoombaB",
    "02-02": "02_JrTroopa1",
    "02-03": "02_JrTroopa2",
    "02-04": "02_JrTroopa3",
    "02-05": "02_JrTroopa4",
    "02-06": "02_JrTroopa5",
    "02-07": "02_JrTroopa6",
    "03-00": "03_Chan",
    "03-01": "03_Lee",
    "03-02": "03_TheMaster1",
    "03-03": "03_TheMaster2",
    "03-04": "03_TheMaster3",
    "03-05": "03_LeeGoombario",
    "03-06": "03_LeeKooper",
    "03-07": "03_LeeBombette",
    "03-08": "03_LeeParakarry",
    "03-09": "03_LeeBow",
    "03-0A": "03_LeeWatt",
    "03-0B": "03_LeeSushie",
    "03-0C": "03_LeeLakilester",
    "04-00": "04_GoombarioTutor1",
    "04-01": "04_Ember",
    "04-02": "04_Ember",
    "04-03": "04_FlyingMagikoopa",
    "04-04": "04_Ember",
    "04-05": "04_Magiclone",
    "04-06": "04_FlyingMagiclone",
    "05-00": "05_Goomba",
    "05-01": "05_Goomba",
    "05-02": "05_Paragoomba",
    "05-03": "05_SpikedGoomba",
    "05-04": "05_SpikedGoomba",
    "05-05": "05_SpikedGoomba",
    "05-06": "05_SpikedGoomba",
    "05-07": "05_SpikedGoomba",
    "05-08": "05_KoopaTroopa",
    "05-09": "05_KoopaTroopa",
    "05-0A": "05_KoopaTroopa",
    "05-0B": "05_KoopaTroopa",
    "05-0C": "05_KoopaTroopa",
    "05-0D": "05_KoopaTroopa",
    "05-0E": "05_KoopaTroopa",
    "05-0F": "05_KoopaTroopa",
    "05-10": "05_KoopaTroopa",
    "05-11": "05_Paratroopa",
    "05-12": "05_Paratroopa",
    "05-13": "05_Paratroopa",
    "05-14": "05_Paratroopa",
    "05-15": "05_Fuzzy",
    "05-16": "05_Fuzzy",
    "05-17": "05_Fuzzy",
    "05-18": "05_KentCKoopa",
    "06-00": "06_KoopaTroopa",
    "06-01": "06_KoopaTroopa",
    "06-02": "06_KoopaTroopa",
    "06-03": "06_KoopaTroopa",
    "06-04": "06_KoopaTroopa",
    "06-05": "06_KoopaTroopa",
    "06-06": "06_KoopaTroopa",
    "06-07": "06_KoopaTroopa",
    "06-08": "06_Paratroopa",
    "06-09": "06_Paratroopa",
    "06-0A": "06_Paratroopa",
    "06-0B": "06_Paratroopa",
    "06-0C": "06_Paratroopa",
    "06-0D": "06_Paratroopa",
    "06-0E": "06_Paratroopa",
    "06-0F": "06_Bobomb",
    "06-10": "06_Bobomb",
    "06-11": "06_Bobomb",
    "06-12": "06_Bobomb",
    "06-13": "06_Bobomb",
    "06-14": "06_Bobomb",
    "06-15": "06_Bobomb",
    "06-16": "06_KoopaTroopa",
    "06-17": "06_BillBlaster",
    "06-18": "06_BulletBill",
    "06-19": "06_BulletBill",
    "06-1A": "06_BulletBill",
    "06-1B": "06_BulletBill",
    "07-00": "07_GNinjakoopa",
    "08-00": "08_GoombarioTutor2",
    "09-00": "09_Cleft",
    "09-01": "09_Cleft",
    "09-02": "09_Cleft",
    "09-03": "09_Cleft",
    "09-04": "09_Cleft",
    "09-05": "09_MontyMole",
    "09-06": "09_MontyMole",
    "09-07": "09_MontyMole",
    "09-08": "09_MontyMole",
    "09-09": "09_MontyMole",
    "09-0A": "09_MontyMole",
    "09-0B": "09_MontyMole",
    "09-0C": "09_Buzzar",
    "09-0D": "09_Cleft",
    "09-0E": "09_EmptyMoleHole",
    "09-0F": "09_EmptyMoleHole",
    "09-10": "09_WhackaB",
    "0A-00": "0A_Pokey",
    "0A-01": "0A_Pokey",
    "0A-02": "0A_Pokey",
    "0A-03": "0A_Pokey",
    "0A-04": "0A_Pokey",
    "0A-05": "0A_Pokey",
    "0A-06": "0A_Pokey",
    "0A-07": "0A_Pokey",
    "0A-08": "0A_Pokey",
    "0A-09": "0A_BanditA",
    "0A-0A": "0A_BanditA",
    "0A-0B": "0A_BanditA",
    "0A-0C": "0A_BanditA",
    "0A-0D": "0A_BanditA",
    "0A-0E": "0A_BanditA",
    "0A-0F": "0A_BanditA",
    "0A-10": "0A_BanditA",
    "0A-11": "0A_Pokey",
    "0A-12": "0A_BanditB",
    "0B-00": "0B_PokeyMummy",
    "0B-01": "0B_PokeyMummy",
    "0B-02": "0B_PokeyMummy",
    "0B-03": "0B_PokeyMummy",
    "0B-04": "0B_PokeyMummy",
    "0B-05": "0B_Swooper",
    "0B-06": "0B_Swooper",
    "0B-07": "0B_StoneChomp",
    "0B-08": "0B_StoneChomp",
    "0B-09": "0B_BuzzyBeetle",
    "0B-0A": "0B_BuzzyBeetle",
    "0B-0B": "0B_BuzzyBeetle",
    "0B-0C": "0B_BuzzyBeetle",
    "0B-0D": "0B_BuzzyBeetle",
    "0B-0E": "0B_BuzzyBeetle",
    "0B-0F": "0B_BuzzyBeetle",
    "0B-10": "0B_BuzzyBeetle",
    "0B-11": "0B_BuzzyBeetle",
    "0B-12": "0B_BuzzyBeetle",
    "0B-13": "0B_BuzzyBeetle",
    "0C-00": "0C_Tutankoopa",
    "0C-01": "0C_Chomp",
    "0D-00": "0D_ForestFuzzy",
    "0D-01": "0D_ForestFuzzy",
    "0D-02": "0D_ForestFuzzy",
    "0D-03": "0D_ForestFuzzy",
    "0D-04": "0D_ForestFuzzy",
    "0D-05": "0D_ForestFuzzy",
    "0D-06": "0D_ForestFuzzy",
    "0D-07": "0D_ForestFuzzy",
    "0D-08": "0D_PiranhaPlant",
    "0D-09": "0D_PiranhaPlant",
    "0D-0A": "0D_PiranhaPlant",
    "0D-0B": "0D_PiranhaPlant",
    "0D-0C": "0D_PiranhaPlant",
    "0D-0D": "0D_PiranhaPlant",
    "0D-0E": "0D_PiranhaPlant",
    "0D-0F": "0D_PiranhaPlant",
    "0D-10": "0D_Bzzap",
    "0D-11": "0D_Bzzap",
    "0D-12": "0D_ForestFuzzy",
    "0E-00": "0E_HyperGoomba",
    "0E-01": "0E_HyperGoomba",
    "0E-02": "0E_HyperGoomba",
    "0E-03": "0E_HyperGoomba",
    "0E-04": "0E_HyperGoomba",
    "0E-05": "0E_HyperGoomba",
    "0E-06": "0E_HyperParagoomba",
    "0E-07": "0E_HyperParagoomba",
    "0E-08": "0E_HyperParagoomba",
    "0E-09": "0E_HyperParagoomba",
    "0E-0A": "0E_HyperCleft",
    "0E-0B": "0E_HyperCleft",
    "0E-0C": "0E_HyperCleft",
    "0E-0D": "0E_HyperCleft",
    "0E-0E": "0E_HyperCleft",
    "0E-0F": "0E_TubbasHeart",
    "0E-10": "0E_TubbaBlubba",
    "0F-00": "0F_Clubba",
    "0F-01": "0F_Clubba",
    "0F-02": "0F_Clubba",
    "0F-03": "0F_Clubba",
    "0F-04": "0F_TubbaBlubba",
    "0F-05": "0F_TubbaBlubba",
    "10-00": "10_ShyGuy_RED",
    "10-01": "10_ShyGuy_BLU",
    "10-02": "10_ShyGuy_YLW",
    "10-03": "10_ShyGuy_YLW",
    "10-04": "10_ShyGuy_PNK",
    "10-05": "10_ShyGuy_GRN",
    "10-06": "10_ShyGuy_RED",
    "10-07": "10_ShyGuy_BLU",
    "10-08": "10_ShyGuy_YLW",
    "10-09": "10_ShyGuy_YLW",
    "10-0A": "10_ShyGuy_PNK",
    "10-0B": "10_ShyGuy_PNK",
    "10-0C": "10_ShyGuy_GRN",
    "10-0D": "10_SkyGuy",
    "10-0E": "10_SkyGuy",
    "10-0F": "10_SkyGuy",
    "10-10": "10_SkyGuy",
    "10-11": "10_SkyGuy",
    "10-12": "10_SkyGuy",
    "10-13": "10_SkyGuy",
    "10-14": "10_SkyGuy",
    "10-15": "10_SpyGuy",
    "10-16": "10_SpyGuy",
    "10-17": "10_SpyGuy",
    "10-18": "10_SpyGuy",
    "10-19": "10_SpyGuy",
    "10-1A": "10_SpyGuy",
    "10-1B": "10_SpyGuy",
    "10-1C": "10_PyroGuy",
    "10-1D": "10_PyroGuy",
    "10-1E": "10_PyroGuy",
    "10-1F": "10_PyroGuy",
    "10-20": "10_PyroGuy",
    "10-21": "10_PyroGuy",
    "10-22": "10_PyroGuy",
    "10-23": "10_PyroGuy",
    "10-24": "10_PyroGuy",
    "10-25": "10_GrooveGuy",
    "10-26": "10_GrooveGuy",
    "10-27": "10_GrooveGuy",
    "10-28": "10_GrooveGuy",
    "10-29": "10_GrooveGuy",
    "10-2A": "10_GrooveGuy",
    "10-2B": "10_GrooveGuy",
    "10-2C": "10_AntiGuy",
    "10-2D": "10_ShyGuy_RED",
    "10-2E": "10_GrooveGuy",
    "10-2F": "10_MediGuy",
    "10-30": "10_SlotMachineStart",
#> WARNING: Could not find actor Actor_802313A8 for unit 00 of formation 01.
#> WARNING: Could not find actor Actor_802310DC for unit 00 of formation 02.
#> WARNING: Could not find actor Actor_80231418 for unit 00 of formation 03.
#> WARNING: Could not find actor Actor_80231418 for unit 00 of formation 04.
#> WARNING: Could not find actor Actor_802312E0 for unit 00 of formation 05.
#> WARNING: Could not find actor Actor_802312E0 for unit 00 of formation 06.
#> WARNING: Could not find actor Actor_802312F8 for unit 00 of formation 07.
    "11-00": "11_GeneralGuy",
    "11-01": "11_Actor_802313A8",
    "11-02": "11_Actor_802310DC",
    "11-03": "11_Actor_80231418",
    "11-04": "11_Actor_80231418",
    "11-05": "11_Actor_802312E0",
    "11-06": "11_Actor_802312E0",
    "11-07": "11_Actor_802312F8",
    "12-00": "12_BigLanternGhost",
    "12-01": "12_Goomba",
    "12-02": "12_Goomba",
    "12-03": "12_Clubba",
    "12-04": "12_Fuzzy",
    "12-05": "12_Fuzzy",
    "12-06": "12_HammerBros",
    "12-07": "12_HammerBros",
    "12-08": "12_Pokey",
    "12-09": "12_Koopatrol",
    "12-0A": "12_ShyGuy",
    "12-0B": "12_SlotMachineStart",
    "12-0C": "12_Pokey",
    "12-0D": "12_Koopatrol",
    "13-00": "13_Fuzzipede",
    "14-00": "14_SpearGuy",
    "14-01": "14_SpearGuy",
    "14-02": "14_SpearGuy",
    "14-03": "14_SpearGuy",
    "14-04": "14_SpearGuy",
    "14-05": "14_SpearGuy",
    "14-06": "14_SpearGuy",
    "14-07": "14_SpearGuy",
    "14-08": "14_HurtPlant",
    "14-09": "14_HurtPlant",
    "14-0A": "14_JungleFuzzy",
    "14-0B": "14_JungleFuzzy",
    "14-0C": "14_JungleFuzzy",
    "14-0D": "14_JungleFuzzy",
    "14-0E": "14_MBush",
    "14-0F": "14_MBush",
    "14-10": "14_MBush",
    "14-11": "14_SpearGuy",
    "14-12": "14_SpearGuy",
    "14-13": "14_JungleFuzzy",
    "15-00": "15_PutridPiranha",
    "15-01": "15_PutridPiranha",
    "15-02": "15_PutridPiranha",
    "15-03": "15_PutridPiranha",
    "16-00": "16_LavaBubble",
    "16-01": "16_LavaBubble",
    "16-02": "16_LavaBubble",
    "16-03": "16_LavaBubble",
    "16-04": "16_LavaBubble",
    "16-05": "16_LavaBubble",
    "16-06": "16_LavaBubble",
    "16-07": "16_LavaBubble",
    "16-08": "16_SpikeTop",
    "16-09": "16_SpikeTop",
    "16-0A": "16_SpikeTop",
    "16-0B": "16_SpikeTop",
    "16-0C": "16_SpikeTop",
    "16-0D": "16_SpikeTop",
    "16-0E": "16_SpikeTop",
    "16-0F": "16_PutridPiranha",
    "16-10": "16_PutridPiranha",
    "16-11": "16_PutridPiranha",
    "16-12": "16_PutridPiranha",
    "16-13": "16_PutridPiranha",
    "16-14": "16_PutridPiranha",
    "17-00": "17_LavaPiranha",
    "17-01": "17_PetitPiranha",
    "17-02": "17_LavaBud",
    "17-03": "17_LavaBud",
    "17-04": "17_PetitPiranha",
    "17-05": "17_PetitPiranha",
    "17-06": "17_PetitPiranhaBomb",
    "18-00": "18_Lakitu",
    "18-01": "18_Lakitu",
    "18-02": "18_Lakitu",
    "18-03": "18_Lakitu",
    "18-04": "18_Lakitu",
    "18-05": "18_Lakitu",
    "18-06": "18_Lakitu",
    "18-07": "18_Lakitu",
    "18-08": "18_Lakitu",
    "18-09": "18_Lakitu",
    "18-0A": "18_Lakitu",
    "18-0B": "18_Lakitu",
    "18-0C": "18_Spiny",
    "18-0D": "18_Spiny",
    "18-0E": "18_Spiny",
    "18-0F": "18_CrazeeDayzee",
    "18-10": "18_CrazeeDayzee",
    "18-11": "18_CrazeeDayzee",
    "18-12": "18_CrazeeDayzee",
    "18-13": "18_CrazeeDayzee",
    "18-14": "18_CrazeeDayzee",
    "18-15": "18_CrazeeDayzee",
    "18-16": "18_CrazeeDayzee",
    "18-17": "18_Bzzap",
    "18-18": "18_Bzzap",
    "18-19": "18_Bzzap",
    "18-1A": "18_Bzzap",
    "18-1B": "18_Bzzap",
    "18-1C": "18_AmazyDayzee",
    "18-1D": "18_AmazyDayzee",
    "18-1E": "18_AmazyDayzee",
    "18-1F": "18_RuffPuff",
    "18-20": "18_RuffPuff",
    "18-21": "18_RuffPuff",
    "18-22": "18_RuffPuff",
    "18-23": "18_RuffPuff",
    "18-24": "18_RuffPuff",
    "18-25": "18_Spiny",
    "19-00": "19_HuffNPuff",
    "19-01": "19_MontyMole",
    "19-02": "19_MontyMole",
    "19-03": "19_MontyMole",
    "19-04": "19_MontyMole",
    "19-05": "19_Spike",
    "19-06": "19_TuffPuff",
    "19-07": "19_TuffPuff",
    "19-08": "19_EmptyMoleHole",
    "19-09": "19_EmptyMoleHole",
    "1A-00": "1A_DarkKoopa",
    "1A-01": "1A_DarkKoopa",
    "1A-02": "1A_DarkKoopa",
    "1A-03": "1A_DarkKoopa",
    "1A-04": "1A_DarkKoopa",
    "1A-05": "1A_DarkKoopa",
    "1A-06": "1A_DarkKoopa",
    "1A-07": "1A_DarkKoopa",
    "1A-08": "1A_DarkParatroopa",
    "1A-09": "1A_DarkParatroopa",
    "1A-0A": "1A_Gloomba",
    "1A-0B": "1A_Gloomba",
    "1A-0C": "1A_Paragloomba",
    "1A-0D": "1A_Paragloomba",
    "1A-0E": "1A_SpikedGloomba",
    "1A-0F": "1A_SpikedGloomba",
    "1A-10": "1A_SpikedGloomba",
    "1A-11": "1A_SpikedGloomba",
    "1A-12": "1A_SpikedGloomba",
    "1A-13": "1A_SpikeTop",
    "1A-14": "1A_SpikeTop",
    "1A-15": "1A_BuzzyBeetle",
    "1A-16": "1A_Spiny",
    "1A-17": "1A_Spiny",
    "1A-18": "1A_Spiny",
    "1B-00": "1B_Blooper",
    "1B-01": "1B_ElectroBlooper",
    "1B-02": "1B_SuperBlooper",
    "1B-03": "1B_BlooperBaby",
    "1B-04": "1B_BlooperBaby",
    "1C-00": "1C_Swooper",
    "1C-01": "1C_Swooper",
    "1C-02": "1C_Swoopula",
    "1C-03": "1C_Swoopula",
    "1D-00": "1D_Duplighost",
    "1D-01": "1D_Gulpit",
    "1D-02": "1D_Gulpit",
    "1D-03": "1D_Gulpit",
    "1D-04": "1D_Gulpit",
    "1D-05": "1D_Gulpit",
    "1D-06": "1D_FrostPiranha",
    "1D-07": "1D_FrostPiranha",
    "1D-08": "1D_FrostPiranha",
    "1D-09": "1D_FrostPiranha",
    "1D-0A": "1D_FrostPiranha",
    "1D-0B": "1D_WhiteClubba",
    "1D-0C": "1D_WhiteClubba",
    "1D-0D": "1D_WhiteClubba",
    "1D-0E": "1D_GhostGoombario",
    "1D-0F": "1D_GhostKooper",
    "1D-10": "1D_GhostBombette",
    "1D-11": "1D_GhostParakarry",
    "1D-12": "1D_GhostBow",
    "1D-13": "1D_GhostWatt",
    "1D-14": "1D_GhostSushie",
    "1D-15": "1D_GhostLakilester",
    "1E-00": "1E_Monstar",
    "1E-01": "1E_Paragoomba",
    "1F-00": "1F_Swoopula",
    "1F-01": "1F_Swoopula",
    "1F-02": "1F_Swoopula",
    "1F-03": "1F_Swoopula",
    "1F-04": "1F_WhiteClubba",
    "1F-05": "1F_WhiteClubba",
    "1F-06": "1F_WhiteClubba",
    "1F-07": "1F_WhiteClubba",
    "1F-08": "1F_WhiteClubba",
    "1F-09": "1F_WhiteClubba",
    "1F-0A": "1F_WhiteClubba",
    "1F-0B": "1F_WhiteClubba",
    "1F-0C": "1F_WhiteClubba",
    "1F-0D": "1F_WhiteClubba",
    "1F-0E": "1F_AlbinoDino",
    "20-00": "20_CrystalKing",
    "20-01": "20_CrystalClone",
    "20-02": "20_CrystalBitA",
    "20-03": "20_CrystalBitB",
    "20-04": "20_CrystalBitC",
    "21-00": "21_Swoopula",
    "21-01": "21_Duplighost",
    "21-02": "21_Duplighost",
    "21-03": "21_Duplighost",
    "21-04": "21_Duplighost",
    "21-05": "21_Duplighost",
    "21-06": "21_Duplighost",
    "21-07": "21_Duplighost",
    "21-08": "21_Duplighost",
    "21-09": "21_Duplighost",
    "21-0A": "21_Duplighost",
    "21-0B": "21_WhiteClubba",
    "21-0C": "21_GhostGoombario",
    "21-0D": "21_GhostKooper",
    "21-0E": "21_GhostBombette",
    "21-0F": "21_GhostParakarry",
    "21-10": "21_GhostBow",
    "21-11": "21_GhostWatt",
    "21-12": "21_GhostSushie",
    "21-13": "21_GhostLakilester",
    "22-00": "22_BonyBeetle",
    "22-01": "22_BonyBeetle",
    "22-02": "22_BonyBeetle",
    "22-03": "22_BonyBeetle",
    "22-04": "22_BonyBeetle",
    "22-05": "22_BonyBeetle",
    "22-06": "22_BonyBeetle",
    "22-07": "22_DryBones",
    "22-08": "22_DryBones",
    "22-09": "22_DryBones",
    "22-0A": "22_DryBones",
    "22-0B": "22_DryBones",
    "22-0C": "22_DryBones",
    "22-0D": "22_DryBones",
    "22-0E": "22_DryBones",
    "22-0F": "22_HammerBros",
    "22-10": "22_HammerBros",
    "22-11": "22_HammerBros",
    "22-12": "22_HammerBros",
    "22-13": "22_HammerBros",
    "22-14": "22_HammerBros",
    "22-15": "22_HammerBros",
    "22-16": "22_HammerBros",
    "22-17": "22_Koopatrol",
    "22-18": "22_Koopatrol",
    "22-19": "22_Koopatrol",
    "22-1A": "22_Koopatrol",
    "22-1B": "22_Koopatrol",
    "22-1C": "22_Koopatrol",
    "22-1D": "22_Koopatrol",
    "22-1E": "22_Koopatrol",
    "22-1F": "22_Koopatrol",
    "22-20": "22_Koopatrol",
    "22-21": "22_Koopatrol",
    "22-22": "22_Koopatrol",
    "22-23": "22_Koopatrol",
    "22-24": "22_Koopatrol",
    "22-25": "22_Koopatrol",
    "22-26": "22_Magikoopa",
    "22-27": "22_Magikoopa",
    "22-28": "22_Magikoopa",
    "22-29": "22_Magikoopa",
    "22-2A": "22_Magikoopa",
    "22-2B": "22_Magikoopa",
    "22-2C": "22_Magikoopa",
    "22-2D": "22_Magikoopa",
    "22-2E": "22_Magikoopa",
    "22-2F": "22_Magikoopa",
    "22-30": "22_FlyingMagikoopa",
    "22-31": "22_FlyingMagikoopa",
    "22-32": "22_FlyingMagikoopa",
    "22-33": "22_FlyingMagikoopa",
    "22-34": "22_FlyingMagikoopa",
    "22-35": "22_FlyingMagikoopa",
    "22-36": "22_FlyingMagikoopa",
    "22-37": "22_FlyingMagikoopa",
    "22-38": "22_Koopatrol",
    "22-39": "22_Magiclone",
    "22-3A": "22_FlyingMagiclone",
    "22-3B": "22_Ember",
    "23-00": "23_UnusedBowser",
    "23-01": "23_IntroBowser",
    "23-02": "23_Bowser1",
    "23-03": "23_Bowser2",
    "23-04": "23_Bowser3",
    "24-00": "24_AntiGuy",
    "24-01": "24_Duplighost",
    "24-02": "24_Duplighost",
    "24-03": "24_GhostGoombario",
    "24-04": "24_GhostKooper",
    "24-05": "24_GhostBombette",
    "24-06": "24_GhostParakarry",
    "24-07": "24_GhostBow",
    "24-08": "24_GhostWatt",
    "24-09": "24_GhostSushie",
    "24-0A": "24_GhostLakilester",
    "25-00": "25_BombshellBill",
    "25-01": "25_BombshellBill",
    "25-02": "25_BombshellBlaster",
    "25-03": "25_BombshellBlaster",
    "25-04": "25_BombshellBlaster",
    "25-05": "25_BombshellBill",
    "25-06": "25_Koopatrol",
    "25-07": "25_Magiclone",
    "25-08": "25_FlyingMagiclone",
    "26-00": "26_KammyKoopa",
    "27-00": "27_Fuzzy",
    "27-01": "27_MontyMole",
    "27-02": "27_Pokey",
    "27-03": "27_ShyGuy",
    "27-04": "27_TubbaBlubba",
    "27-05": "27_Pokey",
    "27-06": "27_BanditB",
    "27-07": "27_EmptyMoleHole",
    "27-08": "27_EmptyMoleHole",
    "27-09": "27_SlotMachineStart",
}
