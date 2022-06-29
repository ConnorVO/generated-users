from settings import intrinio


def get_stock_prices(
    identifier: str = "",
    start_date: str = "",
    end_date: str = "",
    frequency: str = "daily",
    page_size: int = 100,
    next_page: str = "",
    results: list[object] = [],
):
    if not results:
        results = []

    response = intrinio.SecurityApi().get_security_stock_prices(
        identifier,
        start_date=start_date,
        end_date=end_date,
        frequency=frequency,
        page_size=page_size,
        next_page=next_page,
    )

    results.extend(
        [{"date": sp.date, "price": sp.adj_close} for sp in response.stock_prices]
    )

    if response.next_page:
        print(f"Getting next page for stock prices: {response.next_page}")
        return get_stock_prices(
            identifier=identifier,
            start_date=start_date,
            end_date=end_date,
            frequency=frequency,
            page_size=page_size,
            next_page=response.next_page,
            results=results,
        )

    return results
