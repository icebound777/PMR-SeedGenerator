# Currently does not include Koot or letters since they arent relevent in
# randomizer for now
allowed_starting_key_items = [
    0x00F, # Ultra Stone
    0x012, # Pulse Stone
    0x014, # Crystal Palace Key
    0x015, # Lunar Stone
    0x016, # Pyramid Stone
    0x017, # Diamond Stone
    0x019, # Kooper Shell
    0x01B, # Forest Pass
    0x01C, # Boo Weight
    0x01D, # Boo Portrait
    0x01E, # Crystal Berry
    0x020, # Storeroom Key
    0x021, # Toy Train
    0x022, # Boo Record
    0x023, # Frying Pan
    0x024, # Dictionary
    0x025, # Mystery Note
    0x029, # Cookbook
    0x02A, # Jade Raven
    0x02B, # Magical Seed 1
    0x02C, # Magical Seed 2
    0x02D, # Magical Seed 3
    0x02E, # Magical Seed 4
    0x030, # Calculator
    0x031, # Snowman Bucket
    0x032, # Snowman Scarf
    0x033, # Red Key
    0x034, # Blue Key
    0x053, # Artifact
    0x056, # Dolly
    0x057, # Water Stone
    0x058, # Magical Bean
    0x059, # Fertile Soil
    0x059, # Miracle Water
    0x059, # Volcano Vase
    0x067, # Lyrics
    0x068, # Melody
    0x069, # Mailbag
    0x06B, # Odd Key
    0x06C, # Star Stone
    0x079, # Warehouse Key
    0x07B, # Silver Credit
    0x07C, # Gold Credit
    0x16D, # Koopa Fortress Key 1
    0x16E, # Koopa Fortress Key 2
    0x16F, # Koopa Fortress Key 3
    0x170, # Koopa Fortress Key 4
    0x171, # Ruins Key 1
    0x172, # Ruins Key 2
    0x173, # Ruins Key 3
    0x174, # Ruins Key 4
    0x175, # Tubba Castle Key 1
    0x176, # Tubba Castle Key 2
    0x177, # Tubba Castle Key 3
    0x178, # Bowser Castle Key 1
    0x179, # Bowser Castle Key 2
    0x17A, # Bowser Castle Key 3
    0x17B, # Bowser Castle Key 4
    0x17C, # Bowser Castle Key 5
    0x17D, # Prison Key 1
    0x17E, # Prison Key 2
]

allowed_starting_items = [
    0x080, # FireFlower
	0x081, # SnowmanDoll
	0x082, # ThunderRage
	0x083, # ShootingStar 
	0x084, # ThunderBolt
	0x085, # Pebble
	0x086, # DustyHammer
	0x088, # StoneCap
	0x089, # TastyTonic
	0x08A, # Mushroom
	0x08B, # VoltShroom
	0x08C, # SuperShroom
	0x08D, # DriedShroom
	0x08E, # UltraShroom
	0x08F, # SleepySheep
	0x090, # POWBlock
	0x091, # HustleDrink
	0x092, # StopWatch
	0x093, # WhackasBump
	0x094, # Apple
	0x095, # LifeShroom
	0x096, # Mystery
	0x097, # RepelGel
	0x098, # FrightJar
	0x09A, # DizzyDial
	0x09B, # SuperSoda
	0x09C, # Lemon
	0x09D, # Lime
	0x0A2, # JamminJelly
	0x0A3, # MapleSyrup
	0x0A4, # HoneySyrup
	0x0A5, # Goomnut
    0x0A6, # KoopaLeaf
    0x0A7, # DriedPasta
	0x0A8, # DriedFruit
	0x0A9, # StrangeLeaf
	0x0AA, # CakeMix
	0x0AB, # Egg
	0x0AC, # Coconut
	0x0AD, # Melon
	0x0AE, # StinkyHerb
	0x0AF, # IcedPotato
	0x0B0, # SpicySoup
	0x0B1, # ApplePie
	0x0B2, # HoneyUltra
	0x0B3, # MapleUltra
	0x0B4, # JellyUltra
	0x0B5, # Koopasta
	0x0B6, # FriedShroom
	0x0B7, # ShroomCake
	0x0B8, # ShroomSteak
	0x0B9, # HotShroom
	0x0BA, # SweetShroom
	0x0BB, # YummyMeal
	0x0BC, # HealthyJuice
	0x0BD, # BlandMeal
	0x0BE, # DeluxeFeast
    0x0BF, # SpecialShake
	0x0C0, # BigCookie
	0x0C1, # Cake
	0x0C2, # Mistake
	0x0C3, # KoopaTea
	0x0C4, # HoneySuper
	0x0C5, # MapleSuper
	0x0C6, # JellySuper
	0x0C7, # Spaghetti
	0x0C8, # EggMissile
	0x0C9, # FriedEgg
	0x0CA, # HoneyShroom
	0x0CB, # HoneyCandy
	0x0CC, # ElectroPop
	0x0CD, # FirePop
	0x0CE, # LimeCandy
	0x0CF, # CocoPop
	0x0D0, # LemonCandy
	0x0D1, # JellyPop
	0x0D2, # StrangeCake
	0x0D3, # KookyCookie
	0x0D4, # FrozenFries
	0x0D5, # PotatoSalad
	0x0D6, # NuttyCake
	0x0D7, # MapleShroom
	0x0D8, # BoiledEgg
	0x0D9, # YoshiCookie
	0x0DA, # JellyShroom,
	0x25D, # BlueBerryProxy1
	0x25F, # RedBerryProxy1
	0x261, # YellowBerryProxy1
	0x263, # BubbleBerryProxy1
]

allowed_starting_badges = [
    0x0E0, # SpinSmash
	0x0E1, # Multibounce
	0x0E2, # PowerPlusA
	0x0E3, # DodgeMaster
	0x0E4, # PowerBounce
	0x0E5, # SpikeShield
	0x0E6, # FirstAttack
	0x0E7, # HPPlusA
	0x0E8, # QuakeHammer
	0x0E9, # DoubleDip
	0x0EB, # SleepStomp
	0x0EC, # FireShield
	0x0ED, # QuickChange
	0x0EE, # DDownPound
	0x0EF, # DizzyStomp
	0x0F1, # PrettyLucky
	0x0F2, # FeelingFine
	0x0F3, # AttackFXA
	0x0F4, # AllOrNothing
	0x0F5, # HPDrain
	0x0F7, # SlowGo
	0x0F8, # FPPlusA
	0x0F9, # MegaRush
	0x0FA, # IcePower
	0x0FB, # DefendPlusA
	0x0FC, # PayOff
	0x0FD, # MoneyMoney
	0x0FE, # ChillOut
	0x0FF, # HappyHeartA
	0x100, # ZapTap
	0x103, # RunawayPay
	0x104, # Refund
	0x105, # FlowerSaverA
	0x106, # TripleDip
	0x107, # HammerThrow
	0x108, # MegaQuake
	0x109, # SmashCharge
	0x10A, # JumpCharge
	0x10B, # SSmashChg
	0x10C, # SJumpChg
	0x10D, # PowerRush
	0x111, # LastStand
	0x112, # CloseCall
	0x113, # PUpDDown
	0x114, # LuckyDay
	0x116, # PDownDUp
	0x117, # PowerQuake
	0x11A, # HeartFinder
	0x11B, # FlowerFinder
	0x11C, # SpinAttack
	0x11D, # DizzyAttack
	0x11E, # ISpy
	0x11F, # SpeedySpin
	0x120, # BumpAttack
	0x121, # PowerJump
	0x123, # MegaJump
	0x124, # PowerSmash
	0x126, # MegaSmash
	0x129, # DeepFocus1
	0x12E, # DDownJump
	0x12F, # ShrinkStomp
	0x130, # DamageDodgeA
	0x132, # DeepFocus2
	0x133, # DeepFocus3
	0x134, # HPPlusB
	0x135, # FPPlusB
	0x136, # HappyHeartB
	0x138, # FlowerSaverB
	0x13A, # DamageDodgeB
	0x13C, # PowerPlusB
	0x140, # HappyFlowerA
	0x141, # HappyFlowerB
	0x143, # GroupFocus
	0x144, # Peekaboo
	0x145, # AttackFXD
	0x146, # AttackFXB
	0x147, # AttackFXE
	0x148, # AttackFXC
	0x14A, # HPPlusC
	0x14D, # FPPlusC
]
