# RAM Locations

This document will highlight some interesting RAM locations, what they're used for, and how to interpret their data. This file is mostly aimed at implementing auto-trackers.

## Unique Item Registry

The Unique Item Registry is an area of RAM where we track which unique items the player has already collected.
We treat the following item types as unique: Key items, badges, partners, hammer and boots upgrades, star pieces, the "key berry" items, the item pouches, power stars, and partner upgrade items.
Out of these item types star pieces may seem particularly odd, but to be able to track them we had to change the generic star piece item the vanilla game uses into dozens of unique star piece items.

The reason for tracking these items using the Unique Item Registry is to not spawn them when the player has already collected the item. This avoids spawning a unique item from an infinite source (like certain bushes and trees) a second time, and allows us to remove the item from a shop once bought.
The registry is also used for the in-game item tracker in the pause menu.

The Unique Item Registry starts at RAM location `80356B00`.
To find out which item is already collected, add to the start of the UIR the item ID as number of bytes.
So, to check whether the player has collected the Lunar Stone, which has item ID 0x15, you check the byte at location `80356B00 + 0x15 = 80356B15`. If the item is not collected, then that byte will have the value zero, if it has been collected, then that byte will have the value one.

Here's the list of all unique items we track that are relevant to auto-tracking:

### Key items

```text
ID  | Item
----+------------------------
00F | UltraStone
012 | PulseStone
015 | LunarStone
016 | PyramidStone
017 | DiamondStone
018 | VolcanoVase
019 | KooperShell
01B | ForestPass
01C | BooWeight
01D | BooPortrait
01E | CrystalBerry
01F | MysticalKey
020 | StoreroomKey
021 | ToyTrain
022 | BooRecord
023 | FryingPan
024 | Dictionary
025 | MysteryNote
027 | CrystalBall
029 | Cookbook
02A | JadeRaven
02B | MagicalSeed1
02C | MagicalSeed2
02D | MagicalSeed3
02E | MagicalSeed4
030 | Calculator
031 | SnowmanBucket
032 | SnowmanScarf
033 | RedKey
034 | BlueKey
036 | Letter01 (To Merlon)
037 | Letter02 (To Goompa)
038 | Letter03 (To Mort T.)
039 | Letter04 (To Russ T.)
03A | Letter05 (To Mayor Penguin)
03B | Letter06 (To Merlow)
03C | Letter07 (To Fice T.)
03D | Letter08 (To Nomadimouse)
03E | Letter09 (To Minh T.)
040 | Letter10 (To Goompapa 1)
041 | Letter11 (To Igor)
045 | Letter12 (To Franky)
046 | Letter13 (To Muss T.)
047 | Letter14 (To Koover 1)
048 | Letter15 (To Fishmael)
049 | Letter16 (To Koover 2)
04A | Letter17 (To Mr. E.)
04B | Letter18 (To Miss T.)
04C | Letter19 (To Little Mouser)
04E | Letter20 (To Dane T. 1)
04F | Letter21 (To Red Yoshi Kid)
050 | Letter22 (To Dane T. 2)
051 | Letter23 (To Frost T.)
052 | Letter24 (To Goompapa 2)
053 | Artifact
054 | Letter25 (To Kolorado)
056 | Dolly
057 | WaterStone
058 | MagicalBean
059 | FertileSoil
05A | MiracleWater
05B | VolcanoVase
05C | KootTheTape
067 | Lyrics
068 | Melody
069 | Mailbag
06B | OddKey
06C | StarStone
06E | KootKoopaLegends
06F | KootLuigiAutograph
070 | KootEmptyWallet
071 | KootMerluvleeAutograph
073 | KootOldPhoto
074 | KootGlasses
076 | KootPackage
077 | KootRedJar
079 | WarehouseKey
07B | SilverCredit
07C | GoldCredit
16D | KoopaFortressKeyA
16E | KoopaFortressKeyB
16F | KoopaFortressKeyC
170 | KoopaFortressKeyD
171 | RuinsKeyA
172 | RuinsKeyB
173 | RuinsKeyC
174 | RuinsKeyD
175 | TubbaCastleKeyA
176 | TubbaCastleKeyB
177 | TubbaCastleKeyC
178 | BowserCastleKeyA
179 | BowserCastleKeyB
17A | BowserCastleKeyC
17B | BowserCastleKeyD
17C | BowserCastleKeyE
17D | PrisonKeyA
17E | PrisonKeyB
180 | BlueBerryKey1
181 | BlueBerryKey2
182 | RedBerryKey
183 | YellowBerryKey
184 | BubbleBerryKey
```

### Gear Upgrades

```text
ID  | Item
----+------------------------
001 | Boots
002 | SuperBoots
003 | UltraBoots
004 | Hammer
005 | SuperHammer
006 | UltraHammer
```

### Partners

```text
ID  | Item
----+------------------------
2EF | Goombario
2F0 | Kooper
2F1 | Bombette
2F2 | Parakarry
2F4 | Watt
2F5 | Sushie
2F6 | Lakilester
2F7 | Bow
```

(for current partner upgrade level, there is no need to check the collected flags for partner upgrade items. Instead check the current partner level in the Player Data, as outlined below)

### Star Pieces

```text
ID  | Item
----+------------------------
185 | StarPiece00
186 | StarPiece01
187 | StarPiece02
.   | .
.   | .
.   | .
1D4 | StarPiece4F
1D5 | StarPiece50
1D6 | StarPiece51
1D7 | ThreeStarPieces0
1D8 | ThreeStarPieces1
1D9 | ThreeStarPieces2
1DA | ThreeStarPieces3
1DB | ThreeStarPieces4
```

(alternatively check the star piece count in the Player Data, as outlined below. This also does not track star pieces given by Quizmo)

### Power Stars

```text
ID  | Item
----+------------------------
1DC | PowerStar00
1DD | PowerStar01
1DE | PowerStar02
.   | .
.   | .
.   | .
259 | PowerStar7D
25A | PowerStar7E
25B | PowerStar7F
```

(we don't actually count and store the current number of power stars collected anywhere in RAM. Instead the game counts all the UIR collected flags every time it needs to check or display the power stars)

## Player Data

In the global player data you can find player and partner stats.
Similarly to the Unique Item Registry, the player data is saved in byte chunks, so each piece of data is offset from the start of the player data at `8010F290` by a number of bytes equal to a stat's ID.

```text
ID  | Stat
----+------------------------
002 | Current HP
003 | Current Max HP
004 | True Max HP (includes HP Plus badges)
005 | Current FP
006 | Current Max FP
007 | True Max FP (includes FP Plus badges)
008 | Max BP
009 | Mario's Level
00C | Coins
00F | Star Pieces
010 | Star Points
01D | Goombario Rank  (0: base, 1: super, 2: ultra)
025 | Kooper Rank     (0: base, 1: super, 2: ultra)
02D | Bombette Rank   (0: base, 1: super, 2: ultra)
035 | Parakarry Rank  (0: base, 1: super, 2: ultra)
045 | Watt Rank       (0: base, 1: super, 2: ultra)
04D | Sushie Rank     (0: base, 1: super, 2: ultra)
055 | Lakilester Rank (0: base, 1: super, 2: ultra)
05D | Bow Rank        (0: base, 1: super, 2: ultra)
28E | Max Star Power
```

## ModBytes

We store custom global byte data, which gets saved to the player's savefile, at `80356000 - 803560B0` (including).
Like addressing the Unique Item Registry and the Player Data mentioned above, one can get data by adding a field's ID as number of bytes onto the starting RAM address of `80356000`.
While there's isn't too much interesting in here for auto-tracking, the following info could be useful:

```text
ID  | Stat
----+------------------------
090 | Number of star spirits saved
091 | Star spirit saved 1st (0: not saved, 1-7: chapter number of spirit saved)
092 | Star spirit saved 2nd (0: not saved, 1-7: chapter number of spirit saved)
093 | Star spirit saved 3rd (0: not saved, 1-7: chapter number of spirit saved)
094 | Star spirit saved 4th (0: not saved, 1-7: chapter number of spirit saved)
095 | Star spirit saved 5th (0: not saved, 1-7: chapter number of spirit saved)
096 | Star spirit saved 6th (0: not saved, 1-7: chapter number of spirit saved)
097 | Star spirit saved 7th (0: not saved, 1-7: chapter number of spirit saved)
```

## GameFlags and ModFlags

There are two places in the RAM where we store flags: GameFlags (vanilla stuff) and ModFlags (our custom flags).
You find GameFlags at `800DBC70 - 800DBD6F` (including),
and ModFlags at `80357000 - 80357220` (including).

Flags are compressed into 8 flags per byte, so addressing them is a bit tricky. It is recommended to set up a helper function to turn the flag IDs into the actual RAM locations.

How it works: Each flag has a hex ID. These hex IDs don't correspond to the bits in order from left to right, like byte offsets would, though.
To address the first byte on `80357000` you'd just go `80357000 + 0x0`, the fourth byte would be `80357000 + 0x3`.
But with flags, the game treats each s32 (4 bytes) in the flag array as its own flag group.
So the flag with ID 0000 is neither the lowest-value bit of `80357000 + 0x0`, nor its highest-value bit. Instead, it's the lowest-value bit of `80357000 + 0x3`.

To visualize this, let's look at the range of the first 8 bytes of the mod flags,
`80357000 + 0x0` - `80357000 + 0x7`. The first are the 8 bytes, below that the corresponding bits.

```text
00000000  00000000

00000000  00000000
00000000  00000000
00000000  00000000
00000000  00000000
```

Setting flag ID 0000 to true:

```text
00000001  00000000

00000000  00000000
00000000  00000000
00000000  00000000
00000001  00000000
```

Then setting flag ID 001F to true:

```text
80000001  00000000

10000000  00000000
00000000  00000000
00000000  00000000
00000001  00000000
```

Then setting flag ID 0020 to true:

```text
80000001  00000001

10000000  00000000
00000000  00000000
00000000  00000000
00000001  00000001
```

Given this odd way of having to address the flags, here are some flags relevant to auto-tracking:

### Item hand-in flags

(for checking them off on the tracker)

```text
ModFlags:
StoreroomKey                - 0041
Dolly                       - 1001
Calculator                  - 1016
Letter01 (To Merlon)        - 1017
Letter02 (To Goompa)        - 1002
Letter03 (To Mort T.)       - 1037
Letter04 (To Russ T.)       - 1008
Letter05 (To Mayor Penguin) - 1092
Letter06 (To Merlow)        - 102B
Letter07 (To Fice T.)       - 101A
Letter08 (To Nomadimouse)   - 1055
Letter09 (To Minh T.)       - 1018
Letter10 (To Goompapa 1)    - 1003
Letter11 (To Igor)          - 105A
Letter12 (To Franky)        - 1059
Letter13 (To Muss T.)       - 10A6
Letter14 (To Koover 1)      - 1038
Letter15 (To Fishmael)      - 1023
Letter16 (To Koover 2)      - 1039
Letter17 (To Mr. E.)        - 1053
Letter18 (To Miss T.)       - 1009
Letter19 (To Little Mouser) - 104B
Letter20 (To Dane T. 1)     - 101B
Letter21 (To Red Yoshi Kid) - 107B
Letter22 (To Dane T. 2)     - 101C
Letter23 (To Frost T.)      - 109B
Letter24 (To Goompapa 2)    - 1004
Letter25 (To Kolorado)      - 1042
KooperShell                 - 1043
Frying Pan                  - 1019
WaterStone                  - 1087
Crystal Berry               - 1088

GameFlags:
Dictionary                  -  0F4
Mailbag                     -  10A
MagicalSeed1                -  114
MagicalSeed2                -  115
MagicalSeed3                -  116
MagicalSeed4                -  117
Melody                      -  126
Lyrics                      -  2F2
Artifact                    -  312
BooRecord                   -  3D2
VolcanoVase                 -  4FB
```

### Item check collected flags

Some of these behave oddly, as some item locations count as collected even though the player only spawned the item but didn't touch it, or the player simply entered the map the item check is on.
These are used on the pause menu map to display how many checks in a location the player has already collected.

#### Goomba Region

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Forest Clearing - Hidden Panel                 | GameFlag   056

Goomba Village - Bush Bottom Right             | GameFlag   02F
Goomba Village - Goompa Koopa Koot Favor       | GameFlag   064
Goomba Village - Goompa Gift                   | ModFlag   1000
Goomba Village - Goombaria Dolly Reward        | ModFlag   1001
Goomba Village - Goompa Letter Reward          | ModFlag   1002
Goomba Village - Goompapa Letter Reward 1      | ModFlag   1003
Goomba Village - Goompapa Letter Reward 2      | ModFlag   1004
Goomba Village - On The Balcony                | GameFlag   02E
Goomba Village - Goombario Partner             | ModFlag   1006
Goomba Village - Goomnut Tree                  | ModFlag   1005

Behind the Village - On Ledge                  | GameFlag   04A
Behind the Village - In Tree                   | GameFlag   049

Bottom of the Cliff - Hidden Panel             | GameFlag   058
Bottom of the Cliff - Above Stone Block        | GameFlag   034
Bottom of the Cliff - Floating Coin 1          | GameFlag   038
Bottom of the Cliff - Floating Coin 2          | GameFlag   039
Bottom of the Cliff - Floating Coin 3          | GameFlag   03A
Bottom of the Cliff - Floating Coin 4          | GameFlag   03B
Bottom of the Cliff - Upper Ledge              | GameFlag   031
Bottom of the Cliff - In Tree                  | GameFlag   035
Bottom of the Cliff - Block On Ground          | GameFlag   032

Jr. Troopas Playground - Bush Right            | GameFlag   03E
Jr. Troopas Playground - Bush Bottom Right     | GameFlag   03F
Jr. Troopas Playground - Bush Top 1            | GameFlag   040
Jr. Troopas Playground - Bush Top 2            | GameFlag   041
Jr. Troopas Playground - Bush Center           | GameFlag   042
Jr. Troopas Playground - Bush Top Left         | GameFlag   043
Jr. Troopas Playground - In Hammer Bush        | ModFlag   1007
Jr. Troopas Playground - In MultiCoinBlock     | GameFlag   046
Jr. Troopas Playground - In Tree Left          | GameFlag   03C
Jr. Troopas Playground - In Tree Top           | GameFlag   03D
Jr. Troopas Playground - In Tree Right         | GameFlag   01E

Goomba Road 1 - Yellow Block Left              | GameFlag   04D
Goomba Road 1 - Yellow Block Right             | GameFlag   04E

Goomba Road 2 - On the Sign                    | GameFlag   04F
Goomba Road 2 - Red Block                      | GameFlag   050

Goomba Kings Castle - Hidden Panel             | GameFlag   05A
Goomba Kings Castle - In Tree Left Of Fortress | GameFlag   052
Goomba Kings Castle - In Tree Right Of Cliff   | GameFlag   053
Goomba Kings Castle - Hidden Yellow Block      | GameFlag   051

Toad Town Entrance - Chest On Roof             | GameFlag   054
Toad Town Entrance - Yellow Block              | GameFlag   055

Marios House - Luigi Koopa Koot Favor          | GameFlag   063
```

#### Toad Town

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Gate District - Dojo: Chan                     | ModFlag   100B
Gate District - Dojo: Lee                      | ModFlag   100C
Gate District - Dojo: Master 1                 | ModFlag   100D
Gate District - Dojo: Master 2                 | ModFlag   100E
Gate District - Dojo: Master 3                 | ModFlag   100F
Gate District - Russ T. Dictionary Reward      | GameFlag   0F4
Gate District - Russ T. Letter Reward          | ModFlag   1008
Gate District - Miss T. Letter Reward          | ModFlag   1009
Gate District - Radio Trade Event 1 Reward     | ModFlag   100A
Gate District - Hidden Panel                   | GameFlag   127
Gate District - Sushie Island                  | GameFlag   12D
Gate District - Shop Item 1                    | ModFlag   1010
Gate District - Shop Item 2                    | ModFlag   1011
Gate District - Shop Item 3                    | ModFlag   1012
Gate District - Shop Item 4                    | ModFlag   1013
Gate District - Shop Item 5                    | ModFlag   1014
Gate District - Shop Item 6                    | ModFlag   1015

Plaza District - Rowfs Calculator Reward       | ModFlag   1016
Plaza District - Postmaster MailBag Reward     | GameFlag   10A
Plaza District - Merlon Letter Reward          | ModFlag   1017
Plaza District - Minh T. Letter Reward         | ModFlag   1018
Plaza District - Merlon House Stomping         | GameFlag   0FF
Plaza District - Rowfs Shop Set 1 - 1          | GameFlag   680
Plaza District - Rowfs Shop Set 1 - 2          | GameFlag   681
Plaza District - Rowfs Shop Set 1 - 3          | GameFlag   682
Plaza District - Rowfs Shop Set 1 - 4          | GameFlag   683
Plaza District - Rowfs Shop Set 2 - 1          | GameFlag   684
Plaza District - Rowfs Shop Set 2 - 2          | GameFlag   685
Plaza District - Rowfs Shop Set 2 - 3          | GameFlag   686
Plaza District - Rowfs Shop Set 3 - 1          | GameFlag   687
Plaza District - Rowfs Shop Set 3 - 2          | GameFlag   688
Plaza District - Rowfs Shop Set 3 - 3          | GameFlag   689
Plaza District - Rowfs Shop Set 4 - 1          | GameFlag   68A
Plaza District - Rowfs Shop Set 4 - 2          | GameFlag   68B
Plaza District - Rowfs Shop Set 4 - 3          | GameFlag   68C
Plaza District - Rowfs Shop Set 5 - 1          | GameFlag   68D
Plaza District - Rowfs Shop Set 5 - 2          | GameFlag   68E
Plaza District - Rowfs Shop Set 5 - 3          | GameFlag   68F
Plaza District - In Tree                       | GameFlag   12E

Southern District - Bub-ulb Gift               | GameFlag   11B
Southern District - Tayce T. Frying Pan Reward | ModFlag   1019
Southern District - Fice T. Letter Reward      | ModFlag   101A
Southern District - Fice T. Forest Pass        | ModFlag   10AE
Southern District - Hidden Panel               | GameFlag   129
Southern District - Inside Blue House          | GameFlag   084

Station District - Dane T. Letter Reward 1     | ModFlag   101B
Station District - Dane T. Letter Reward 2     | ModFlag   101C
Station District - Hidden Panel                | GameFlag   12A

Residental District - Storeroom Item 1         | GameFlag   12F
Residental District - Storeroom Item 2         | GameFlag   130
Residental District - Storeroom Item 3         | GameFlag   121
Residental District - Storeroom Item 4         | GameFlag   131
Residental District - Shop Item 1              | ModFlag   101D
Residental District - Shop Item 2              | ModFlag   101E
Residental District - Shop Item 3              | ModFlag   101F
Residental District - Shop Item 4              | ModFlag   1020
Residental District - Shop Item 5              | ModFlag   1021
Residental District - Shop Item 6              | ModFlag   1022

Port District - Poet Gift                      | GameFlag   125
Port District - Poet Melody Reward             | GameFlag   126
Port District - Fishmael Letter Reward         | ModFlag   1023
Port District - Radio Trade Event 3 Reward     | ModFlag   1024
Port District - Hidden Panel                   | GameFlag   12C
Port District - In MultiCoinBlock              | GameFlag   132
```

#### Toad Town Tunnels

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Hall to Blooper 1 (B1) - Hidden Block          | GameFlag   198
Hall to Blooper 1 (B1) - In MultiCoinBlock     | GameFlag   199

Blooper Boss 1 (B1) - Blooper Fight Reward     | GameFlag   18F

Short Elevator Room (B1) - Yellow Block Center | GameFlag   190
Short Elevator Room (B1) - Yellow Block Left   | GameFlag   191
Short Elevator Room (B1) - Yellow Block Right  | GameFlag   192

Spring Room (B2) - Chest On Ledge              | GameFlag   193

Elevator Attic Room (B2) - On Parakarry Ledge  | GameFlag   194
Elevator Attic Room (B2) - In SuperBlock       | GameFlag   1B1

Metal Block Room (B3) - In SuperBlock          | GameFlag   1B3

Blue Pushblock Room (B2) - Hidden Block Left   | GameFlag   195
Blue Pushblock Room (B2) - Hidden Block Center | GameFlag   196
Blue Pushblock Room (B2) - Hidden Block Right  | GameFlag   197
Blue Pushblock Room (B2) - In SuperBlock       | GameFlag   1B2

Room with Spikes (B2) - Yellow Block           | GameFlag   19A

Winding Path (Spiny Room) - Hidden Block Center| GameFlag   1A0
Winding Path (Spiny Room) - Hidden Block Right | GameFlag   1A1
Winding Path (Spiny Room) - Hidden Block Left  | GameFlag   1A2
Winding Path (Spiny Room) - Yellow Block       | GameFlag   1A3

Hall to Ultra Boots (B3) - Hidden Block        | GameFlag   1A4
Hall to Ultra Boots (B3) - Yellow Block Left   | GameFlag   1A5
Hall to Ultra Boots (B3) - Yellow Block Right  | GameFlag   1A6

Ultra Boots Room (B3) - In Big Chest           | GameFlag   1A7

Bridge to Shiver City (B2) - Yellow Block 1    | GameFlag   19B
Bridge to Shiver City (B2) - Yellow Block 2    | GameFlag   19C
Bridge to Shiver City (B2) - Yellow Block 3    | GameFlag   19D
Bridge to Shiver City (B2) - Yellow Block 4    | GameFlag   19E
Bridge to Shiver City (B2) - Yellow Block 5    | GameFlag   19F

Frozen Room (B3) - In SuperBlock               | GameFlag   1B4

Rip Cheatos Home (B3) - Rip Cheato Offer 1     | ModFlag   102C
Rip Cheatos Home (B3) - Rip Cheato Offer 2     | ModFlag   102D
Rip Cheatos Home (B3) - Rip Cheato Offer 3     | ModFlag   102E
Rip Cheatos Home (B3) - Rip Cheato Offer 4     | ModFlag   102F
Rip Cheatos Home (B3) - Rip Cheato Offer 5     | ModFlag   1030
Rip Cheatos Home (B3) - Rip Cheato Offer 6     | ModFlag   1031
Rip Cheatos Home (B3) - Rip Cheato Offer 7     | ModFlag   1032
Rip Cheatos Home (B3) - Rip Cheato Offer 8     | ModFlag   1033
Rip Cheatos Home (B3) - Rip Cheato Offer 9     | ModFlag   1034
Rip Cheatos Home (B3) - Rip Cheato Offer 10    | ModFlag   1035
Rip Cheatos Home (B3) - Rip Cheato Offer 11    | ModFlag   1036

Under the Toad Town Pond - In SuperBlock       | GameFlag   1B5
```

#### Shooting Star Summit

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Shooting Star Path - Hidden Panel              | GameFlag   21A

Merluvlees House - Merluvlee Koopa Koot Favor  | GameFlag   219
Merluvlees House - Merlow Letter Reward        | ModFlag   102B
Merluvlees House - Hidden Panel                | GameFlag   21C
Merluvlees House - Merlows Badges 1            | GameFlag   6EB
Merluvlees House - Merlows Badges 2            | GameFlag   6EC
Merluvlees House - Merlows Badges 3            | GameFlag   6ED
Merluvlees House - Merlows Badges 4            | GameFlag   6EE
Merluvlees House - Merlows Badges 5            | GameFlag   6EF
Merluvlees House - Merlows Badges 6            | GameFlag   6F0
Merluvlees House - Merlows Badges 7            | GameFlag   6F1
Merluvlees House - Merlows Badges 8            | GameFlag   6F2
Merluvlees House - Merlows Badges 9            | GameFlag   6F3
Merluvlees House - Merlows Badges 10           | GameFlag   6F4
Merluvlees House - Merlows Badges 11           | GameFlag   6F5
Merluvlees House - Merlows Badges 12           | GameFlag   6F6
Merluvlees House - Merlows Badges 13           | GameFlag   6F7
Merluvlees House - Merlows Badges 14           | GameFlag   6F8
Merluvlees House - Merlows Badges 15           | GameFlag   6F9
Merluvlees House - Merlows Rewards 1           | ModFlag   10A8
Merluvlees House - Merlows Rewards 2           | ModFlag   10A9
Merluvlees House - Merlows Rewards 3           | ModFlag   10AA
Merluvlees House - Merlows Rewards 4           | ModFlag   10AB
Merluvlees House - Merlows Rewards 5           | ModFlag   10AC
Merluvlees House - Merlows Rewards 6           | ModFlag   10AD

Shooting Star Summit - Hidden Panel            | GameFlag   21B
Shooting Star Summit - Behind The Summit       | GameFlag   220

Star Haven - Shop Item 1                       | ModFlag   1025
Star Haven - Shop Item 2                       | ModFlag   1026
Star Haven - Shop Item 3                       | ModFlag   1027
Star Haven - Shop Item 4                       | ModFlag   1028
Star Haven - Shop Item 5                       | ModFlag   1029
Star Haven - Shop Item 6                       | ModFlag   102A
```

#### Koopa Region

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Pleasant Path Entry - Red Block Center         | GameFlag   253
Pleasant Path Entry - Yellow Block Left        | GameFlag   252
Pleasant Path Entry - Yellow Block Right       | GameFlag   254

Pleasant Path Bridge - Kooper Island           | GameFlag   244
Pleasant Path Bridge - Behind Fence            | GameFlag   267
Pleasant Path Bridge - In MultiCoinBlock       | GameFlag   258
Pleasant Path Bridge - Yellow Block            | GameFlag   255

Pleasant Crossroads - Hidden Panel             | GameFlag   260
Pleasant Crossroads - Behind Peg               | GameFlag   268
Pleasant Crossroads - Brick Block Puzzle       | GameFlag   256

Path to Fortress 1 - Hidden Panel              | GameFlag   261
Path to Fortress 1 - Hidden Block              | GameFlag   257
Path to Fortress 1 - X On Ground 1             | GameFlag   246
Path to Fortress 1 - X On Ground 2             | GameFlag   247
Path to Fortress 1 - X On Ground 3             | GameFlag   248
Path to Fortress 1 - X On Ground 4             | GameFlag   249
Path to Fortress 1 - X On Ground 5             | GameFlag   24A
Path to Fortress 1 - On Brick Block            | GameFlag   245

Path to Fortress 2 - In Tree                   | GameFlag   251

Koopa Village 1 - Bush Far Left                | GameFlag   24C
Koopa Village 1 - Bush Left Front              | GameFlag   24D
Koopa Village 1 - Bush Infront Of Tree         | ModFlag   1049
Koopa Village 1 - Bush Second From Right       | GameFlag   24F
Koopa Village 1 - Bush Second From Left (Koopa Koot Favor) | GameFlag   263
Koopa Village 1 - Bush Far Right (Koopa Koot Favor) | GameFlag   264
Koopa Village 1 - Mort T. Letter Reward        | ModFlag   1037
Koopa Village 1 - Koover Letter Reward 1       | ModFlag   1038
Koopa Village 1 - Koover Letter Reward 2       | ModFlag   1039
Koopa Village 1 - Hidden Panel                 | GameFlag   25E
Koopa Village 1 - Shop Item 1                  | ModFlag   103A
Koopa Village 1 - Shop Item 2                  | ModFlag   103B
Koopa Village 1 - Shop Item 3                  | ModFlag   103C
Koopa Village 1 - Shop Item 4                  | ModFlag   103D
Koopa Village 1 - Shop Item 5                  | ModFlag   103E
Koopa Village 1 - Shop Item 6                  | ModFlag   103F

Koopa Village 2 - Bush Far Left                | ModFlag   104A
Koopa Village 2 - Bush Far Right               | ModFlag   10A7
Koopa Village 2 - Kolorados Wife (Koopa Koot Favor) | GameFlag   265
Koopa Village 2 - Koopa Koot Silver Credit     | ModFlag   1040
Koopa Village 2 - Koopa Koot Gold Credit       | ModFlag   1041
Koopa Village 2 - Kolorado Artifact Reward     | GameFlag   312
Koopa Village 2 - Kolorado Letter Reward       | ModFlag   1042
Koopa Village 2 - Push Block Puzzle            | GameFlag   243
Koopa Village 2 - Koopa Koot Reward 1          | GameFlag   6AD
Koopa Village 2 - Koopa Koot Reward 2          | GameFlag   6B0
Koopa Village 2 - Koopa Koot Reward 3          | GameFlag   6B3
Koopa Village 2 - Koopa Koot Reward 4          | GameFlag   6B6
Koopa Village 2 - Koopa Koot Reward 5          | GameFlag   6B9
Koopa Village 2 - Koopa Koot Reward 6          | GameFlag   6BC
Koopa Village 2 - Koopa Koot Reward 7          | GameFlag   6BF
Koopa Village 2 - Koopa Koot Reward 8          | GameFlag   6C2
Koopa Village 2 - Koopa Koot Reward 9          | GameFlag   6C5
Koopa Village 2 - Koopa Koot Reward 10         | GameFlag   6C8
Koopa Village 2 - Koopa Koot Reward 11         | GameFlag   6CB
Koopa Village 2 - Koopa Koot Reward 12         | GameFlag   6CE
Koopa Village 2 - Koopa Koot Reward 13         | GameFlag   6D1
Koopa Village 2 - Koopa Koot Reward 14         | GameFlag   6D4
Koopa Village 2 - Koopa Koot Reward 15         | GameFlag   6D7
Koopa Village 2 - Koopa Koot Reward 16         | GameFlag   6DA
Koopa Village 2 - Koopa Koot Reward 17         | GameFlag   6DD
Koopa Village 2 - Koopa Koot Reward 18         | GameFlag   6E0
Koopa Village 2 - Koopa Koot Reward 19         | GameFlag   6E3
Koopa Village 2 - Koopa Koot Reward 20         | GameFlag   6E6
Koopa Village 2 - Kooper Partner               | ModFlag   1043

Behind Koopa Village - On Stump                | GameFlag   242

Fuzzy Forest - Fuzzy Battle Reward             | ModFlag   1044
```

#### Koopa Bros Fortress

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Fortress Exterior - Chest Behind Fortress      | GameFlag   281
Fortress Exterior - Chest On Ledge             | GameFlag   282

Left Tower - Top Of Tower                      | GameFlag   27E
Left Tower - Koopa Troopa Reward               | GameFlag   285

Central Hall - Left Cell                       | GameFlag   286
Central Hall - Right Cell                      | GameFlag   287
Central Hall - Center Cell                     | GameFlag   27F

Jail - Bombette Partner                        | ModFlag   1045

Dungeon Fire Room - On The Ground              | GameFlag   288

Battlement - Block Behind Rock                 | GameFlag   280
```

#### Mt Rugged

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Train Station - Bush 1                         | GameFlag   2C5
Train Station - Bush 2                         | GameFlag   2C6
Train Station - Bush 3                         | GameFlag   2C7
Train Station - Bush Top                       | ModFlag   1047
Train Station - Parakarry Partner              | ModFlag   1048
Train Station - In SuperBlock                  | GameFlag   2D1

Mt Rugged 1 - On Slide 1                       | GameFlag   2B3
Mt Rugged 1 - On Slide 2                       | GameFlag   2B4
Mt Rugged 1 - On Slide 3                       | GameFlag   2B5
Mt Rugged 1 - Hurting Whacka                   | ModFlag   1046
Mt Rugged 1 - Yellow Block                     | GameFlag   2CB

Mt Rugged 2 - Hidden Panel                     | GameFlag   2CD
Mt Rugged 2 - Parakarry Ledge                  | GameFlag   2AE
Mt Rugged 2 - Kooper Ledge                     | GameFlag   2C1

Mt Rugged 3 - Bub-ulb Gift                     | GameFlag   2CC
Mt Rugged 3 - On Scaffolding                   | GameFlag   2AF

Mt Rugged 4 - Hidden Cave Chest                | GameFlag   2B1
Mt Rugged 4 - Slide Ledge                      | GameFlag   2C2
Mt Rugged 4 - Left Ledge Center                | GameFlag   2B0
Mt Rugged 4 - Left Ledge Right                 | GameFlag   2B8
Mt Rugged 4 - Left Ledge 3                     | GameFlag   2B9
Mt Rugged 4 - Left Ledge 4                     | GameFlag   2BA
Mt Rugged 4 - Left Ledge 5                     | GameFlag   2BB
Mt Rugged 4 - Left Ledge 6                     | GameFlag   2BC
Mt Rugged 4 - Left Ledge 7                     | GameFlag   2BD
Mt Rugged 4 - Bottom Left 1                    | GameFlag   2B6
Mt Rugged 4 - Bottom Left 2                    | GameFlag   2B7
Mt Rugged 4 - Yellow Block Top Left            | GameFlag   2BE
Mt Rugged 4 - Yellow Block Floating            | GameFlag   2BF
Mt Rugged 4 - Yellow Block Top Right           | GameFlag   2C0

Suspension Bridge - Bottom Of Cliff            | GameFlag   2C3
```

#### Dry Dry Desert

```text
Location (spoiler log name)                      | Flag type and ID
-------------------------------------------------+---------------------
N3W3 - Yellow Block Left                         | GameFlag   31D
N3W3 - Yellow Block Right                        | GameFlag   31E

N3W1 Ruins Entrance - Radio Trade Event 2 Reward | ModFlag   1054

N3E2 Pokey Army - Behind Cactus                  | GameFlag   33F

N3E3 - In Tree                                   | GameFlag   345
N3E3 - In MultiCoinBlock                         | GameFlag   330

N2W3 - Hidden Block                              | GameFlag   31F

N2E1 (Tweester A) - Yellow Block Left            | GameFlag   320
N2E1 (Tweester A) - Yellow Block Right           | GameFlag   321
N2E1 (Tweester A) - In MultiCoinBlock            | GameFlag   331

N1W3 Special Block - Hit Block                   | GameFlag   322
N1W3 Special Block - Hit Block Plenty            | GameFlag   323
N1W3 Special Block - Hit Block Very Much         | GameFlag   324

N1W1 - Yellow Block 1                            | GameFlag   325
N1W1 - Yellow Block 2                            | GameFlag   326
N1W1 - Yellow Block 3                            | GameFlag   327
N1W1 - Yellow Block 4                            | GameFlag   328
N1W1 - Yellow Block Center                       | GameFlag   329

N1E1 Palm Trio - Hidden Block                    | GameFlag   32A

N1E2 - In MultiCoinBlock Center                  | GameFlag   332
N1E2 - In MultiCoinBlock Bottom Right            | GameFlag   333

N1E3 - In Tree                                   | GameFlag   346

W3 Kolorados Camp - In Tree                      | GameFlag   340

Center (Tweester C) - Hidden Panel               | GameFlag   31C

E1 Nomadimouse - Nomadimouse Letter Reward       | ModFlag   1055
E1 Nomadimouse - In Tree                         | GameFlag   347

E2 - In Tree Far Left                            | GameFlag   348

E3 Outside Outpost - In Tree (Far Left)          | GameFlag   349
E3 Outside Outpost - In Tree (Second From Left)  | GameFlag   34A
E3 Outside Outpost - In Tree (Fourth From Right) | GameFlag   34B
E3 Outside Outpost - In Tree (Far Right)         | GameFlag   341

S1W3 - In MultiCoinBlock Top Left                | GameFlag   334

S1 - Yellow Block                                | GameFlag   32B

S1E2 Small Bluffs - On Brick Block               | GameFlag   343
S1E2 Small Bluffs - Ontop Of Bluffs              | GameFlag   342

S1E3 North of Oasis - Hidden Block               | GameFlag   32D
S1E3 North of Oasis - Tree Bottom Left           | GameFlag   34C
S1E3 North of Oasis - Yellow Block               | GameFlag   32C

S2W1 - In MultiCoinBlock Top                     | GameFlag   335

S2E2 West of Oasis - Behind Bush                 | GameFlag   344
S2E2 West of Oasis - In Tree                     | GameFlag   34D
S2E2 West of Oasis - In MultiCoinBlock           | GameFlag   336

S2E3 Oasis - In Fruit Tree (Left)                | ModFlag   1056
S2E3 Oasis - In Fruit Tree (Right)               | ModFlag   1057
S2E3 Oasis - In Tree (Far Left)                  | GameFlag   34E
S2E3 Oasis - In Tree (Front Right)               | GameFlag   34F
S2E3 Oasis - In SuperBlock                       | GameFlag   33D

S3W2 Hidden AttackFX - Hidden Block              | GameFlag   32E

S3E1 - Yellow Block                              | GameFlag   32F

S3E3 South of Oasis - In Tree (Far Right)            | GameFlag   350
S3E3 South of Oasis - In MultiCoinBlock Top Left     | GameFlag   337
S3E3 South of Oasis - In MultiCoinBlock Top Right    | GameFlag   338
S3E3 South of Oasis - In MultiCoinBlock Right        | GameFlag   339
S3E3 South of Oasis - In MultiCoinBlock Left         | GameFlag   33A
S3E3 South of Oasis - In MultiCoinBlock Bottom Left  | GameFlag   33B
S3E3 South of Oasis - In MultiCoinBlock Bottom Right | GameFlag   33C
```

#### Dry Dry Outpost

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Outpost 1 - Composer Lyrics Reward             | GameFlag   2F2
Outpost 1 - Store Legend                       | GameFlag   2F6
Outpost 1 - Little Mouser Letter Reward        | ModFlag   104B
Outpost 1 - Shop Item 1                        | ModFlag   104C
Outpost 1 - Shop Item 2                        | ModFlag   104D
Outpost 1 - Shop Item 3                        | ModFlag   104E
Outpost 1 - Shop Item 4                        | ModFlag   104F
Outpost 1 - Shop Item 5                        | ModFlag   1050
Outpost 1 - Shop Item 6                        | ModFlag   1051
Outpost 1 - In Red Tree                        | GameFlag   2F8

Outpost 2 - Merlee Request (Koopa Koot Favor)  | GameFlag   2F7
Outpost 2 - Moustafa Gift                      | ModFlag   1052
Outpost 2 - Mr. E. Letter Reward               | ModFlag   1053
Outpost 2 - Hidden Panel                       | GameFlag   2F4
Outpost 2 - Toad House Roof                    | GameFlag   2F5
```

#### Dry Dry Ruins

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Sarcophagus Hall 1 - In Sarcophagus            | GameFlag   694

Sand Drainage Room 1 - On The Ground           | GameFlag   367

Sand Drainage Room 2 - In The Sand             | GameFlag   375
Sand Drainage Room 2 - On Ledge                | GameFlag   36A

Pyramid Stone Room - On Pedestal               | GameFlag   372

Sarcophagus Hall 2 - Pokey Gauntlet Reward     | GameFlag   36B
Sarcophagus Hall 2 - Behind Hammer Block       | GameFlag   374

Super Hammer Room - In Big Chest               | GameFlag   384
Super Hammer Room - Hidden Chest               | GameFlag   385

Vertical Shaft - In SuperBlock                 | GameFlag   387

Diamond Stone Room - On Pedestal               | GameFlag   373

Sand Drainage Room 3 - On Ledge                | GameFlag   377

Lunar Stone Room - On Pedestal                 | GameFlag   371
```

#### Forever Forest

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Tree Face (Bub-ulb) - Bub-ulb Gift             | GameFlag   3A2
Bee Hive (HP Plus) - Central Block             | GameFlag   39D
Flowers Appear (FP Plus) - Central Block       | GameFlag   39E
Outside Boos Mansion - In Bush (Back Right)    | ModFlag   1058
Outside Boos Mansion - Yellow Block            | GameFlag   3A7
Exit to Gusty Gulch - Hidden Panel             | GameFlag   3A5
```

#### Boos Mansion

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Foyer - From Franky (Koopa Koot Favor)         | GameFlag   3BF
Foyer - Franky Letter Reward                   | ModFlag   1059
Foyer - Hidden Panel                           | GameFlag   3C1

Basement Stairs - Hidden Panel                 | GameFlag   3C4

Basement - In Crate                            | GameFlag   3C5
Basement - Igor Letter Reward                  | ModFlag   105A
Basement - Shop Item 1                         | ModFlag   105B
Basement - Shop Item 2                         | ModFlag   105C
Basement - Shop Item 3                         | ModFlag   105D
Basement - Shop Item 4                         | ModFlag   105E
Basement - Shop Item 5                         | ModFlag   105F
Basement - Shop Item 6                         | ModFlag   1060

Super Boots Room - In Big Chest                | GameFlag   3C7
Super Boots Room - In Crate                    | GameFlag   3CA
Super Boots Room - Hidden Panel                | GameFlag   3CC

Pot Room - In Crate 1                          | ModFlag   1061
Pot Room - In Crate 2                          | ModFlag   1062

Library - In Crate                             | GameFlag   3D0
Library - On Bookshelf                         | GameFlag   3CF

Record Player Room - In Chest                  | GameFlag   3D2

Record Room - Hidden Panel                     | GameFlag   3D4
Record Room - Beat Boo Game                    | GameFlag   3D3

Lady Bows Room - Bow Partner                   | ModFlag   1063
```

#### Gusty Gulch

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Ghost Town 1 - From Boo (Koopa Koot Favor)     | GameFlag   3F7
Ghost Town 1 - Yellow Block In House           | GameFlag   3EF

Wasteland Ascent 1 - On Rock                   | GameFlag   3ED
Wasteland Ascent 1 - Infront Of Branch         | GameFlag   3EE
Wasteland Ascent 1 - Yellow Block 1            | GameFlag   3EA
Wasteland Ascent 1 - Yellow Block 2            | GameFlag   3EB
Wasteland Ascent 1 - Yellow Block Right        | GameFlag   3EC

Wasteland Ascent 2 - Behind Rock               | GameFlag   3FB
Wasteland Ascent 2 - In MultiCoinBlock         | GameFlag   3F2
Wasteland Ascent 2 - Yellow Block Left         | GameFlag   3F0
Wasteland Ascent 2 - Yellow Block Right        | GameFlag   3F1
```

#### Tubbas Castle

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Covered Tables Room (1F) - On Table            | GameFlag   41F

Study (1F) - On Table                          | GameFlag   41A

Table/Clock Room (1/2F) - On Table             | GameFlag   412

Basement - In Chest                            | GameFlag   418

Stairs to Basement - In SuperBlock             | GameFlag   416

Spike Trap Room (2F) - In Chest                | GameFlag   421

Hidden Bedroom (2F) - In Hidden Room           | GameFlag   422
Hidden Bedroom (2F) - On Bed 1                 | GameFlag   423
Hidden Bedroom (2F) - On Bed 2                 | GameFlag   424
Hidden Bedroom (2F) - On Bed 3                 | GameFlag   425
Hidden Bedroom (2F) - On Bed 4                 | GameFlag   426
Hidden Bedroom (2F) - On Bed 5                 | GameFlag   427
Hidden Bedroom (2F) - On Bed 6                 | GameFlag   428

Stairs to Third Floor - Yellow Block           | GameFlag   429

Sleeping Clubbas Room (3F) - On Pedestal       | GameFlag   42D
```

#### Shy Guys Toybox

```text
Location (spoiler log name)                      | Flag type and ID
-------------------------------------------------+-------------------
BLU Station - Hidden Panel                       | GameFlag   4A6
BLU Station - Hidden Block                       | GameFlag   45D

BLU Anti-Guy Hall - In Chest                     | GameFlag   49F
BLU Anti-Guy Hall - Hidden Block                 | GameFlag   4A1
BLU Anti-Guy Hall - Yellow Block                 | GameFlag   4A0

BLU Large Playroom - Hidden Block 1              | GameFlag   456
BLU Large Playroom - Hidden Block 2              | GameFlag   457
BLU Large Playroom - Calculator Thief 1          | GameFlag   454
BLU Large Playroom - Calculator Thief 2          | ModFlag   1064
BLU Large Playroom - Shy Guy 2                   | ModFlag   1065
BLU Large Playroom - Shy Guy 3                   | ModFlag   1066
BLU Large Playroom - Shy Guy 4                   | ModFlag   1067
BLU Large Playroom - Shy Guy 5                   | ModFlag   1068

BLU Block City - In Chest                        | GameFlag   45F
BLU Block City - Infront Of Chest                | GameFlag   44E
BLU Block City - Midair 1                        | GameFlag   463
BLU Block City - Midair 2                        | GameFlag   464
BLU Block City - Midair 3                        | GameFlag   465
BLU Block City - Midair 4                        | GameFlag   466
BLU Block City - Midair 5                        | GameFlag   467
BLU Block City - Midair 6                        | GameFlag   468
BLU Block City - Midair 7                        | GameFlag   469
BLU Block City - Midair 8                        | GameFlag   46A
BLU Block City - On Building                     | GameFlag   46C
BLU Block City - Behind Building Block           | GameFlag   46D
BLU Block City - Yellow Block 1                  | GameFlag   460
BLU Block City - Yellow Block 2                  | GameFlag   461
BLU Block City - Yellow Block On Ledge           | GameFlag   462

PNK Station - In Chest                           | GameFlag   472
PNK Station - Hidden Panel                       | GameFlag   4A7
PNK Station - Hidden Block                       | GameFlag   473

PNK Tracks Hallway - In MultiCoinBlock           | GameFlag   4A5
PNK Tracks Hallway - Yellow Block South          | GameFlag   4A2
PNK Tracks Hallway - Yellow Block North 1        | GameFlag   4A3
PNK Tracks Hallway - Yellow Block North 2        | GameFlag   4A4

PNK Gourmet Guy Crossing - Hidden Block Right    | GameFlag   470
PNK Gourmet Guy Crossing - Hidden Block Left     | GameFlag   471
PNK Gourmet Guy Crossing - Gourmet Guy Reward    | GameFlag   452
PNK Gourmet Guy Crossing - Yellow Block 1        | GameFlag   46E
PNK Gourmet Guy Crossing - Yellow Block 2        | GameFlag   46F

PNK Playhouse - In Chest (Far Right)             | GameFlag   476
PNK Playhouse - In Chest (Top Left)              | GameFlag   477
PNK Playhouse - In Chest (Right)                 | GameFlag   478
PNK Playhouse - Infront Of Chest (Right)         | GameFlag   44F
PNK Playhouse - Yellow Block                     | GameFlag   475

GRN Station - Hidden Panel                       | GameFlag   4A8
GRN Station - Hidden Block                       | GameFlag   479

GRN Treadmills/Slot Machine - In Chest           | GameFlag   47B
GRN Treadmills/Slot Machine - Infront Of Chest   | GameFlag   450
GRN Treadmills/Slot Machine - On Treadmill 1     | GameFlag   47E
GRN Treadmills/Slot Machine - On Treadmill 2     | GameFlag   47F
GRN Treadmills/Slot Machine - On Treadmill 3     | GameFlag   480
GRN Treadmills/Slot Machine - On Treadmill 4     | GameFlag   481
GRN Treadmills/Slot Machine - On Treadmill 5     | GameFlag   482
GRN Treadmills/Slot Machine - On Treadmill 6     | GameFlag   483
GRN Treadmills/Slot Machine - Hidden Room Center | GameFlag   496
GRN Treadmills/Slot Machine - Hidden Room 1      | GameFlag   488
GRN Treadmills/Slot Machine - Hidden Room 2      | GameFlag   489
GRN Treadmills/Slot Machine - Hidden Room 3      | GameFlag   48D
GRN Treadmills/Slot Machine - Hidden Room 4      | GameFlag   48E
GRN Treadmills/Slot Machine - Hidden Room 5      | GameFlag   492
GRN Treadmills/Slot Machine - Hidden Room 6      | GameFlag   493
GRN Treadmills/Slot Machine - Defeat Shy Guy     | GameFlag   47D
GRN Treadmills/Slot Machine - In MultiCoinBlock  | GameFlag   497

RED Station - Hidden Panel                       | GameFlag   4A9
RED Station - Hidden Block                       | GameFlag   498

RED Moving Platforms - Hidden Block Center       | GameFlag   49A
RED Moving Platforms - Hidden Block Right        | GameFlag   49D
RED Moving Platforms - Hidden Block Left         | GameFlag   49E
RED Moving Platforms - In SuperBlock             | GameFlag   4AA
RED Moving Platforms - In MultiCoinBlock         | GameFlag   499
RED Moving Platforms - Yellow Block 1            | GameFlag   49C
RED Moving Platforms - Yellow Block 2            | GameFlag   49B

RED Lantern Ghost - Watt Partner                 | ModFlag   1069

RED Boss Barricade - Hidden Block Left           | GameFlag   45B
RED Boss Barricade - On Brick Block              | GameFlag   45C
RED Boss Barricade - Yellow Block Right          | GameFlag   45A
```

#### Jade Jungle

```text
Location (spoiler log name)                      | Flag type and ID
-------------------------------------------------+-------------------
Whale Cove - Over Flower 1                       | GameFlag   4C0
Whale Cove - Over Flower 2                       | GameFlag   4C1
Whale Cove - Behind Bush                         | GameFlag   4C3
Whale Cove - In Palm Tree                        | ModFlag   106A

Beach - Hidden Block Left                        | GameFlag   4DE
Beach - Hidden Block Right                       | GameFlag   4DF
Beach - On The Rocks                             | GameFlag   4C6
Beach - Over Flower 1                            | GameFlag   4C5
Beach - Over Flower 2                            | GameFlag   4FD
Beach - In Palm Tree 1                           | ModFlag   106B
Beach - In Palm Tree 2                           | ModFlag   106C
Beach - In Palm Tree 3                           | ModFlag   106D
Beach - In Palm Tree 4                           | ModFlag   106E
Beach - In Palm Tree 5                           | ModFlag   106F
Beach - In Palm Tree 6                           | GameFlag   4E4
Beach - In Palm Tree 6 2                         | ModFlag   1070

Village Cove - Village Leader Reward             | ModFlag   1071
Village Cove - Hidden Panel                      | GameFlag   4F5
Village Cove - In Palm Tree Left                 | ModFlag   1072
Village Cove - In Palm Tree Right                | ModFlag   1073

Village Buildings - Kolorado Volcano Vase Reward | GameFlag   4FB
Village Buildings - Yellow Yoshi Food Reward     | ModFlag   107A
Village Buildings - Red Yoshi Kid Letter Reward  | ModFlag   107B
Village Buildings - Shop Item 1                  | ModFlag   1074
Village Buildings - Shop Item 2                  | ModFlag   1075
Village Buildings - Shop Item 3                  | ModFlag   1076
Village Buildings - Shop Item 4                  | ModFlag   1077
Village Buildings - Shop Item 5                  | ModFlag   1078
Village Buildings - Shop Item 6                  | ModFlag   1079
Village Buildings - In Palm Tree                 | ModFlag   107C

Path to the Volcano - Raphael Gift               | ModFlag   107E
Path to the Volcano - Behind Tree                | GameFlag   4D9

SE Jungle (Quake Hammer) - Bush (Bottom Right)   | GameFlag   4F0
SE Jungle (Quake Hammer) - Bush (Bottom Left)    | GameFlag   4D7
SE Jungle (Quake Hammer) - Red Block             | GameFlag   4D6
SE Jungle (Quake Hammer) - In Tree (Right)       | GameFlag   4E5

Sushi Tree - In Volcano Chest                    | GameFlag   4CC
Sushi Tree - On Island                           | GameFlag   4CD
Sushi Tree - Sushie Partner                      | ModFlag   107D
Sushi Tree - In Island Tree                      | GameFlag   4CB

SW Jungle (Super Block) - Bush (Top Right)       | GameFlag   4F1
SW Jungle (Super Block) - Bush (Bottom Left)     | GameFlag   4F2
SW Jungle (Super Block) - Hidden Block           | GameFlag   4E1
SW Jungle (Super Block) - Underwater 1           | GameFlag   4FF
SW Jungle (Super Block) - Underwater 2           | GameFlag   500
SW Jungle (Super Block) - Underwater 3           | GameFlag   501
SW Jungle (Super Block) - In SuperBlock          | GameFlag   4FE
SW Jungle (Super Block) - In Tree (Top)          | GameFlag   4E8
SW Jungle (Super Block) - In Tree (Right)        | GameFlag   4E9

NW Jungle (Large Ledge) - Bush 1                 | GameFlag   4F3
NW Jungle (Large Ledge) - Bush 2                 | GameFlag   4F4
NW Jungle (Large Ledge) - In Tree On Ledge       | GameFlag   4EA
NW Jungle (Large Ledge) - In Tree Right          | GameFlag   4EB

Western Dead End - Underwater                    | GameFlag   502

NE Jungle (Raven Statue) - Underwater            | GameFlag   4D8
NE Jungle (Raven Statue) - In Tree (Top Left)    | GameFlag   4E6

Small Jungle Ledge - In Tree                     | GameFlag   4E7

Deep Jungle 1 - Hidden Block                     | GameFlag   4E2
Deep Jungle 1 - In Tree (Vine)                   | GameFlag   4DA
Deep Jungle 1 - In Tree (Hit)                    | GameFlag   4EC

Deep Jungle 2 (Block Puzzle) - Hidden Block      | GameFlag   4E3
Deep Jungle 2 (Block Puzzle) - In Tree (Left)    | GameFlag   4ED

Deep Jungle 3 - Tree Vine Second Left            | GameFlag   4DB
Deep Jungle 3 - Tree Vine Far Right              | GameFlag   4DC

Deep Jungle 4 (Ambush) - Hidden Panel            | GameFlag   4F6
Deep Jungle 4 (Ambush) - In Tree (Right)         | GameFlag   4EE

Great Tree Vine Ascent - End Of Vine             | GameFlag   4DD
```

#### Mt Lavalava

```text
Location (spoiler log name)                    | Flag type and ID
-----------------------------------------------+---------------------
Central Cavern - On Stone Pillar               | GameFlag   532
Central Cavern - On Brick Block                | GameFlag   533
Central Cavern - Yellow Block 1                | GameFlag   534
Central Cavern - Yellow Block 2                | GameFlag   535
Central Cavern - Yellow Block 3                | GameFlag   536
Central Cavern - Yellow Block 4                | GameFlag   537

Fire Bar Bridge - In SuperBlock                | GameFlag   530

Flowing Lava Puzzle - Hidden Block             | GameFlag   520

Ultra Hammer Room - In Big Chest               | GameFlag   523

Dizzy Stomp Room - In Chest                    | GameFlag   52C

Zipline Cavern - Hidden Panel                  | GameFlag   53A
Zipline Cavern - In SuperBlock                 | GameFlag   531

Boss Antechamber - Hidden Panel                | GameFlag   53B

Boss Room - Yellow Block Left                  | GameFlag   538
Boss Room - Yellow Block Right                 | GameFlag   539
```

#### Flower Fields

```text
Location (spoiler log name)                      | Flag type and ID
-------------------------------------------------+-------------------
(NE) Elevators - Stomp On Ledge                  | GameFlag   56C
(NE) Elevators - Leftside Vine                   | ModFlag   108B
(NE) Elevators - In SuperBlock                   | GameFlag   57B

(NE) Fallen Logs - Hidden Block                  | GameFlag   56E
(NE) Fallen Logs - In The Flowers                | GameFlag   56D

(East) Triple Tree Path - Leftmost Vine          | ModFlag   1086
(East) Triple Tree Path - Tree Puzzle Reward     | GameFlag   566

(East) Petunias Field - Petunia Gift             | ModFlag   107F
(East) Petunias Field - Hidden Panel             | GameFlag   57C
(East) Petunias Field - In Tree 1                | ModFlag   1080
(East) Petunias Field - In Tree 2                | ModFlag   1081

(East) Old Well - Well Reward                    | GameFlag   570

(SE) Briar Platforming - In The Flowers          | GameFlag   565
(SE) Briar Platforming - Left Side Vine          | ModFlag   1083
(SE) Briar Platforming - In SuperBlock           | GameFlag   57A
(SE) Briar Platforming - In Tree 1               | ModFlag   1084
(SE) Briar Platforming - In Tree 2               | ModFlag   1085

(SE) Water Level Room - Hidden Panel             | GameFlag   57E
(SE) Water Level Room - Hidden Block             | GameFlag   572
(SE) Water Level Room - In Tree 1                | ModFlag   108C
(SE) Water Level Room - In Tree 2                | ModFlag   108D
(SE) Water Level Room - Yellow Block             | GameFlag   571

(SE) Lilys Fountain - Lily Reward For WaterStone | ModFlag   1087
(SE) Lilys Fountain - In Tree                    | GameFlag   567

(SW) Path to Crystal Tree - Hidden Panel         | GameFlag   57F
(SW) Path to Crystal Tree - Central Vine         | ModFlag   108E
(SW) Path to Crystal Tree - In Tree 1            | ModFlag   108F
(SW) Path to Crystal Tree - In Tree 2            | ModFlag   1090

(SW) Posie and Crystal Tree - Posie Gift 1       | ModFlag   1082
(SW) Posie and Crystal Tree - Posie Gift 2       | GameFlag   55E

(West) Path to Maze - Upper Hidden Block         | GameFlag   581
(West) Path to Maze - Lower Hidden Block         | GameFlag   580

(West) Maze - In MultiCoinBlock                  | GameFlag   568

(West) Rosies Trellis - Rosie Gift               | ModFlag   1088

(NW) Bubble Flower - On Ledge                    | GameFlag   56B
(NW) Bubble Flower - Right Vine                  | ModFlag   108A

(NW) Lakilester - Cage Under Rock                | GameFlag   569
(NW) Lakilester - In The Flowers                 | GameFlag   56A
(NW) Lakilester - Lakilester Partner             | ModFlag   1089

Cloudy Climb - On Cloud                          | GameFlag   56F
```

#### Shiver Region

```text
Location (spoiler log name)                          | Flag type and ID
-----------------------------------------------------+---------------
Shiver City Center - Toad House Breakfast            | ModFlag   1093
Shiver City Center - Snowmen Gift 1                  | GameFlag   5A0
Shiver City Center - Snowmen Gift 2                  | GameFlag   5A1
Shiver City Center - Snowmen Gift 3                  | GameFlag   5A2
Shiver City Center - Snowmen Gift 4                  | GameFlag   5A3
Shiver City Center - Snowmen Gift 5                  | GameFlag   5A4
Shiver City Center - Shop Item 1                     | ModFlag   1094
Shiver City Center - Shop Item 2                     | ModFlag   1095
Shiver City Center - Shop Item 3                     | ModFlag   1096
Shiver City Center - Shop Item 4                     | ModFlag   1097
Shiver City Center - Shop Item 5                     | ModFlag   1098
Shiver City Center - Shop Item 6                     | ModFlag   1099

Shiver City Mayor Area - Chest In House              | GameFlag   59B
Shiver City Mayor Area - Mayor Penguin Gift          | ModFlag   1091
Shiver City Mayor Area - Mayor Penguin Letter Reward | ModFlag   1092
Shiver City Mayor Area - Hidden Panel                | GameFlag   59C

Shiver City Pond Area - In Frozen Pond               | GameFlag   5BA

Shiver Snowfield - Hidden Panel                      | GameFlag   5A5
Shiver Snowfield - Behind Tree Right                 | GameFlag   5A7
Shiver Snowfield - In Tree Left                      | GameFlag   5A6

Path to Starborn Valley - Hidden Block               | GameFlag   5AA
Path to Starborn Valley - Behind Icicle              | GameFlag   5A9

Starborn Valley - Merle Gift                         | ModFlag   109A
Starborn Valley - Frost T. Letter Reward             | ModFlag   109B

Shiver Mountain Passage - Hidden Block               | GameFlag   5B0

Shiver Mountain Hills - Bottom Path                  | ModFlag   109C
Shiver Mountain Hills - In SuperBlock                | GameFlag   5B1

Shiver Mountain Tunnel - Socket 1                    | ModFlag   109D
Shiver Mountain Tunnel - Socket 2                    | ModFlag   109E
Shiver Mountain Tunnel - Socket 3                    | ModFlag   109F

Shiver Mountain Peaks - Left Ledge                   | GameFlag   5B8
Shiver Mountain Peaks - Red Block                    | GameFlag   5B7

Merlars Sanctuary - On Pedestal                      | GameFlag   599
```

#### Crystal Palace

```text
Location (spoiler log name)                      | Flag type and ID
-------------------------------------------------+-------------------
Blue Key Room - In Chest                         | GameFlag   5D5

Red Key Room - In Chest                          | GameFlag   5D4

Reflected Save Room - Yellow Block               | GameFlag   5DA

Shooting Star Room - On The Ground               | GameFlag   5DB

P-Down, D-Up Room - In Chest                     | GameFlag   5DD

Star Piece Cave - On The Ground                  | GameFlag   5E2

Blue Mirror Hall 2 - In MultiCoinBlock Front     | GameFlag   5E0
Blue Mirror Hall 2 - In MultiCoinBlock Back      | GameFlag   5E1

Triple Dip Room - In Chest                       | GameFlag   5ED

Huge Statue Room - Hidden Panel                  | GameFlag   5E6
Huge Statue Room - Yellow Block                  | GameFlag   5E5

Palace Key Room - In Chest                       | GameFlag   5E9

Small Statue Room - Hidden Panel                 | GameFlag   5E8
Small Statue Room - Hidden Block                 | GameFlag   5E7

P-Up, D-Down Room - In Chest                     | GameFlag   5EA
```

#### Bowsers Castle

```text
Location (spoiler log name)                      | Flag type and ID
-------------------------------------------------+-------------------
Front Door Exterior - Red Block                  | GameFlag   61D

Lower Jail - In Crate 1                          | GameFlag   617
Lower Jail - In Crate 2                          | GameFlag   618

Outside Lower Jail - Defeat Koopatrol Reward     | GameFlag   60D
Outside Lower Jail - Yellow Block                | GameFlag   60B

Lava Key Room - In Chest                         | GameFlag   613

Lava Channel 3 - On Island 1                     | GameFlag   611
Lava Channel 3 - On Island 2                     | GameFlag   612

Dark Cave 1 - Yellow Block                       | GameFlag   609

Dark Cave 2 - Yellow Block                       | GameFlag   60A

East Upper Jail - Defeat Koopatrol Reward        | GameFlag   627

Item Shop - Shop Item 1                          | ModFlag   10A0
Item Shop - Shop Item 2                          | ModFlag   10A1
Item Shop - Shop Item 3                          | ModFlag   10A2
Item Shop - Shop Item 4                          | ModFlag   10A3
Item Shop - Shop Item 5                          | ModFlag   10A4
Item Shop - Shop Item 6                          | ModFlag   10A5

Left Water Puzzle - Top Left Ledge               | GameFlag   632

Right Water Puzzle - Hidden Block                | GameFlag   637

Room with Hidden Door 1 - Hidden Block           | GameFlag   62E
Room with Hidden Door 1 - Yellow Block           | GameFlag   62D

Hidden Key Room - On The Ground                  | GameFlag   630

Battlement - On Ledge                            | GameFlag   622
Battlement - Yellow Block Left                   | GameFlag   61F
Battlement - Yellow Block Center                 | GameFlag   620
Battlement - Yellow Block Right                  | GameFlag   621

West Upper Jail - Defeat Koopatrol Reward        | GameFlag   62A

Ultra Shroom Room - On The Ground                | GameFlag   62C

Castle Key Room - On The Ground                  | GameFlag   62B
```

#### Peachs Castle

```text
Location (spoiler log name)                      | Flag type and ID
-------------------------------------------------+-------------------
Guest Room (1F) - In Chest                       | GameFlag   1E7

Library (2F) - Upper Level                       | GameFlag   1F8
Library (2F) - Between Bookshelves               | GameFlag   1E4

Storeroom (2F) - On The Ground                   | GameFlag   1E6
```

#### Peachs Castle Grounds

```text
Location (spoiler log name)                      | Flag type and ID
-------------------------------------------------+-------------------
Ruined Castle Grounds - Muss T. Letter Reward    | ModFlag   10A6
Hijacked Castle Entrance - Hidden Block          | GameFlag   66B
```
