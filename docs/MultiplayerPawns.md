# Multiplayer Pawns

The randomizer supports player pawns, which are simplistic NPCs without any AI.
Pawns are partially see-through Marios, which do not have a hitbox and cannot
interact with the general game world. These pawns are supposed to mirror other
players' locations, palettes and animations.
These may be used to see other players run around your game world.
While the pawns are active, the d-pad gets mapped to four different 'emote'
animations to somewhat communicate with the other players.
Additionally, consumable items thrown using the randomizer's item toss feature
can be thrown into another player's game world.

A third-party client/server application may read and write data to and from the
RAM headers and buffers outlined below to control up to 7 pawns at once.

To activate this feature, a seed has to be generated with the 'Multiplayer'
toggle set to `true`. This toggle is a seed setting like any other, but is not
available on the web generator.

All 7 pawns are always spawned in, but unused ones are placed out of bounds at
xyz (0 -1000 0).

## Header

Current Player Index (80358000)
(4 bytes) playerID (assumed from 0-7)
The networking plugin is responsible for writing playerID here

## Buffers

### Toss_Send

Range: (80358100 - 80358280, len = 16)
(1 byte) to playerID
(1 byte) from playerID
(2 byte) itemID (*** zero indicates entry is blank)
(0x14 bytes) additional data
Client will write entries to this buffer for the server to consume.
Server copies entries from this buffer to other player's Toss_Recv.
Server clears entries after consuming them.
`to playerID` is automatically set to closest other player at the time of tossing.

### Toss_Recv

Range: (80358280 - 80358400, len = 16)
(1 byte) to playerID
(1 byte) from playerID
(2 byte) itemID (*** zero indicates entry is blank)
(0x14 bytes) additional data
Server copies entries from other players into empty positions in this buffer.
Client will consume these entries to spawn the items.
Client clears entries after consuming them.

### Players

Range: (80358800 - 80359000)
(1 byte) enabled --- set to TRUE if a player with current array index (= playerID) is connected
(0x3F bytes) pawn data
Each client will update their own player record (i.e., player X updates entry X)
Plugin should gather these from all players, combine them, and broadcast to all players.
Plugin is responsbile for setting the 'enabled' flag to connected players only.

## Key item sharing

Finally, this feature allows sharing the key item inventory.
Since picking up certain key items has cascading effects (like setting global
flags), it is recommended to not simply share the key item inventory portion
of the game's RAM, but instead use the following Keys_Recv buffer.
This allows the randomizer mod to add the key items to the inventory while
setting flags and other related data as well.
(This part of the feature is also tied to the `Multiplayer` toggle)

### Keys_Recv

Range: (80358400 - 80358500, len = 128)
(2 bytes) itemID (*** zero indicates entry is blank)
Server should write into empty entries in this buffer.
Client will read them and clear entries after consuming them.
