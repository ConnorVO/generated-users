from random import Random, random
import random

from yb_generated_users.intrinio.Enums.RandomNumberType import RandomNumberType


def get_random_number_for(type: RandomNumberType = RandomNumberType.NUM_TICKERS):
    if type == RandomNumberType.NUM_TICKERS:
        return random.randint(5, 50)
    if type == RandomNumberType.NUM_TRADES_PER_TICKER:
        return random.randint(1, 6)
