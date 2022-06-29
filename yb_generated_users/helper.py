import random
import math


def _get_trade_quantity(price: float = 0.0, curr_quantity: int = None):
    # this is a sell
    if curr_quantity:
        # get a random quantity that is > 20% of curr quantity and less than 80%
        rand_quantity = random.randint(
            int(curr_quantity * 0.2), int(curr_quantity * 0.8)
        )

        if rand_quantity == curr_quantity:
            return -1 * (curr_quantity - 1)

        if rand_quantity == 0:
            return -1

        return rand_quantity * -1

    # this is a buy
    trade_value = random.randint(
        500, 5000
    )  # each buy strade can only be between 100 and 6000 total value
    return math.ceil(trade_value / price)


def add_data(prices_obj: object = None) -> object:
    for ticker in prices_obj:
        running_num_shares: int = 0

        trades = prices_obj[ticker]

        # first trade must be a buy
        trades[0]["type"] = "BUY"
        quantity = _get_trade_quantity(price=trades[0]["price"])
        trades[0]["quantity"] = quantity
        trades[0]["ticker"] = ticker

        running_num_shares += quantity

        for trade in trades[1::]:
            flip = random.random()
            trade_type = "BUY"
            if flip <= 0.60:  # slightly more likely to sell
                trade_type = "SELL"

            quantity = (
                _get_trade_quantity(price=trade["price"])
                if trade_type == "BUY"
                else _get_trade_quantity(
                    price=trade["price"], curr_quantity=running_num_shares
                )
            )

            # 90% chance of selling entire position if the last trade is a sale (0.9*0.6 = 54% chance user is selling entire holding on this trade)
            if trade == trades[-1] and trade_type == "SELL":
                flip = random.random()
                if flip <= 0.90:
                    quantity = -1 * running_num_shares

            trade["type"] = trade_type
            trade["quantity"] = quantity
            trade["ticker"] = ticker

            running_num_shares += quantity

    return prices_obj
