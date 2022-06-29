from yb_generated_users.intrinio.Enums.TickerType import TickerType


def get_ticker_types_from_ints(
    ticker_type_input_list: list[int] = [],
) -> list[TickerType]:
    ticker_types: list[TickerType] = []

    for num in ticker_type_input_list:
        ticker_types.append(TickerType(num))

    return ticker_types
