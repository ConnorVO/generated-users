from datetime import datetime
import random

from yb_generated_users.intrinio.Enums.RandomNumberType import RandomNumberType
from yb_generated_users.intrinio.utils.helpers.api import get_stock_prices
from yb_generated_users.intrinio.utils.helpers.dates import (
    get_random_date_for_beginning_portfolio,
)
from yb_generated_users.intrinio.utils.helpers.random_numbers import (
    get_random_number_for,
)
from yb_generated_users.intrinio.utils.helpers.ticker_list import get_tickers_from_files
from yb_generated_users.intrinio.utils.helpers.ticker_type import (
    get_ticker_types_from_ints,
)


def _get_tickers(ticker_type_input_list: list[int] = []) -> list[str]:
    num_tickers = get_random_number_for(type=RandomNumberType.NUM_TICKERS)

    ticker_types = get_ticker_types_from_ints(
        ticker_type_input_list=ticker_type_input_list
    )
    tickers: list[str] = get_tickers_from_files(
        ticker_type_list=ticker_types, num=num_tickers
    )

    return tickers


def get_tickers_and_prices(ticker_type_input_list: list[int] = []):
    print("Getting tickers and prices")
    tickers: list[str] = _get_tickers(ticker_type_input_list=ticker_type_input_list)
    print(f"Got {len(tickers)} tickers")
    portfolio_start_date: str = get_random_date_for_beginning_portfolio().strftime(
        "%Y-%m-%d"
    )
    print(f"Portfolio start date: {portfolio_start_date}")
    prices_obj = {}
    for ticker in tickers:
        print(f"\nGetting Prices for Ticker: {ticker}")
        prices = get_stock_prices(
            identifier=ticker,
            start_date=portfolio_start_date,
            end_date=datetime.now().strftime("%Y-%m-%d"),
        )
        num_trades = get_random_number_for(type=RandomNumberType.NUM_TRADES_PER_TICKER)
        print(f"Num trades for ticker: {num_trades}")
        random_sample_of_prices = random.sample(
            prices, num_trades if num_trades <= len(prices) else len(prices)
        )
        random_sample_of_prices.sort(key=lambda x: x["date"])
        print(f"price_objects for ticker:\n{random_sample_of_prices}")

        prices_obj[ticker] = random_sample_of_prices

    return prices_obj
