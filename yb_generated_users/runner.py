import json
import re
from yb_generated_users.helper import add_data
from yb_generated_users.google_sheets.google_sheets import create_sheets_data

from yb_generated_users.intrinio.intrinio import get_tickers_and_prices


def _ask_for_username() -> str:
    username_input: str = input("What is the username?\n")

    if not username_input or not re.search("[a-zA-Z]", username_input):
        print("Username not valid")
        quit()

    return username_input.lower()


def _ask_for_tickers() -> list[int]:
    valid_inputs = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
    ]
    tickers_input: str = input(
        """
    Which tickers do you want to include (comma separated list, no spaces):
    1) All
    2) Only top 100
    3) Only above $1B
    4) Only above $10B
    5) Penny stocks
    6) Retail
    7) Software
    8) Semiconductors
    9) Real Estate
    10) Pharmaceuticals
    11) Insurance
    12) Energy / Gold
    13) Medical
    14) Machinery
    15) Media
    16) Food
    17) Electronics
    18) Communications
    19) Commercial
    20) Chemicals
    21) Banks
    22) Aerospace
    23) Airlines
    24) Auto
    """
    )

    try:
        ticker_list = [int(ticker) for ticker in tickers_input.split(",")]
    except:
        print("Can't split ticker list or can't convert to int")
        quit()

    result = all(elem in valid_inputs for elem in ticker_list)

    if not result:
        print("Invalid item in list")
        quit()

    return ticker_list


def generate_new_user():
    """This is called to start the process
    Run with => pipenv run python3 -c 'import yb_generated_users.runner; yb_generated_users.runner.generate_new_user()'
    """
    username = _ask_for_username()
    ticker_list = _ask_for_tickers()

    with open("./data/users.json", "r") as f:
        data = json.load(f)

        if username not in data:
            print("Username not in users db")
            quit()

        user = data[username]

    prices_obj = get_tickers_and_prices(ticker_type_input_list=ticker_list)
    prices_obj_with_quantity_and_type = add_data(prices_obj=prices_obj)

    all_trades: list[object] = []
    for key in prices_obj_with_quantity_and_type:
        all_trades += prices_obj_with_quantity_and_type[key]
    all_trades.sort(reverse=True, key=lambda x: x["date"])

    create_sheets_data(sheet_id=user["google_sheets_id"], trades=all_trades)
