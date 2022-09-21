import random

from db.node import Node

from rando_enums.enum_options import MerlowRewardPricing


def get_shop_price(
    node:Node,
    do_randomize_shops:bool,
    merlow_costs:int
) -> int:
    """
    Return the price for an item for offer within a shop (regular or Merlow's).
    Merlow gets special pricing rules as he deals in star pieces.
    """
    if "HOS_06" in node.identifier:
        # Merlow's shop
        if "ShopReward" in node.identifier:
            # Merlow's trade rewards
            # If Merlow is set to "cheap", then only adjust the pricing, but
            # not the actual star pieces required in logic. This makes it so
            # even if an item is placed in an expensive reward slot,
            # gathering the required star pieces becomes much easier
            # overall.
            if "ShopRewardA" in node.identifier:
                if merlow_costs == MerlowRewardPricing.CHEAP:
                    buy_price = 5
                else:
                    buy_price = 10
            elif "ShopRewardB" in node.identifier:
                if merlow_costs == MerlowRewardPricing.CHEAP:
                    buy_price = 10
                else:
                    buy_price = 20
            elif "ShopRewardC" in node.identifier:
                if merlow_costs == MerlowRewardPricing.CHEAP:
                    buy_price = 15
                else:
                    buy_price = 30
            elif "ShopRewardD" in node.identifier:
                if merlow_costs == MerlowRewardPricing.CHEAP:
                    buy_price = 20
                else:
                    buy_price = 40
            elif "ShopRewardE" in node.identifier:
                if merlow_costs == MerlowRewardPricing.CHEAP:
                    buy_price = 25
                else:
                    buy_price = 50
            else:
                if merlow_costs == MerlowRewardPricing.CHEAP:
                    buy_price = 30
                else:
                    buy_price = 60
        else:
            # Merlow's StarPiece trade (for a total cost of all 112 StarPieces)
            if any(True for i in ["ShopBadgeA","ShopBadgeB"] if i in node.identifier):
                buy_price = 1
            elif any(True for i in ["ShopBadgeC","ShopBadgeD"] if i in node.identifier):
                buy_price = 2
            elif any(True for i in ["ShopBadgeE","ShopBadgeF"] if i in node.identifier):
                buy_price = 4
            elif any(True for i in ["ShopBadgeG","ShopBadgeH"] if i in node.identifier):
                buy_price = 6
            elif any(True for i in ["ShopBadgeI","ShopBadgeJ"] if i in node.identifier):
                buy_price = 8
            elif any(True for i in ["ShopBadgeK","ShopBadgeL"] if i in node.identifier):
                buy_price = 10
            elif any(True for i in ["ShopBadgeM","ShopBadgeN"] if i in node.identifier):
                buy_price = 15
            elif any(True for i in ["ShopBadgeO"] if i in node.identifier):
                buy_price = 20
    else:
        # Regular Shop
        item_type = node.current_item.item_type

        if do_randomize_shops:
            if item_type == "ITEM":
                sell_price = node.current_item.base_price
                buy_price = round(sell_price * 1.5)

                # Randomly adjust price a bit
                rnd_factor = random.choice([0.75,0.9,1,1.1,1.25])

                buy_price = round(buy_price * rnd_factor)

                if buy_price == 0:
                    buy_price = 1

                # If below 5, let value stay, else round to nearest 5
                if (buy_price - (buy_price % 5)) != 0:
                    buy_price = round(buy_price / 5) * 5

            elif item_type in ["BADGE", "KEYITEM", "PARTNER", "GEAR"]:
                buy_price = random.choice([10,15,20,25,30])

            elif item_type == "COIN":
                buy_price = 1

            elif item_type == "STARPIECE":
                buy_price = random.choice([2,4,6,8,10])

            else:
                buy_price = 35
        else:
            buy_price = node.vanilla_price

    #print(f"Set price {node_id}({node.current_item}): {buy_price}")

    return buy_price
