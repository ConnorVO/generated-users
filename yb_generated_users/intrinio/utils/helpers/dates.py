from datetime import datetime, timedelta
import random


def get_random_date_for_beginning_portfolio(
    start_date: datetime = datetime.now() - timedelta(days=1461),
    end_date: datetime = datetime.now() - timedelta(days=366),
) -> datetime:
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    return random_date
