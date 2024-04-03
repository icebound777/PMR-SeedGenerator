# Multiworld

Some information in regards to multiworld features.

## Toggle

The main toggle to activate multiworld-related features is called `MultiworldEnabled`.
The seed generator itself, as well as the web generator, will never set this toggle to `True`, so that has to be done by a third-party tool for generating the multiworld seed.

Turning on `MultiworldEnabled` will activate the Keys_Recv buffer, as mentioned in the MultiplayerPawns docs.
However, instead of reading the entire buffer on map load, the `MultiworldEnabled` setting will cause that buffer to read only the first item, shift all remaining items over, and then wait 30 frames before checking and, if needed, consuming the next item ID placed in the buffer.
The goal of this delay is to allow a planned feature, the scrolling item send/received log, to not lag the game too hard.

Additionally, each consumed item will make a sequence counter increment, to keep track of how many items have been consumed in the current game.
This sequence counter can be found on the ModBytes 0x134 and 0x135, taken together as unsigned 16bit integer.

So, to add off-world item to the current game, a multiworld client will first want to check the sequence counter. If that counter is lower on the mod side than on the server side, then the first slot of the Keys_Recv has to be checked (as the game may be busy working through a previously written list of items). If the first slot is empty, the client is free to write one or more items into the buffer, for the game to add to Mario's inventory.

This method currently only allows for adding non-consumable items.

## Special Items

There are two kinds of special items for multiworld:

* A generic multiworld item on ID 0x25C
* 93 key multiworld items on IDs 0x25D - 0x2B9

The key multiworld items are tracked in the Unique Item Registry (see RAMLocations docs), and are intended to be placed in replenishing item locations, like certain bushes, trees and vines, as well as the shops. Each of these key items is only to be placed once per game by the multiworld seed generator.

The generic multiworld item can be placed everywhere else.

Collecting either the generic mw item or any of the key mw items does absolutely nothing to Mario's inventory except set the item collection flag. The multiworld client has to track item collection via these `item check collected flags` (see RAMLocations docs).
