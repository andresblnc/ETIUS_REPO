import random
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

def random_dates_for_week(start_date, end_date):
    days_of_week = list(range(7))
    random_dates = []

    while days_of_week:
        random_date_found = False
        while not random_date_found:
            date = random_date(start_date, end_date)
            if date.weekday() in days_of_week:
                random_dates.append(date)
                days_of_week.remove(date.weekday())
                random_date_found = True

    return random_dates

# Ejemplo de uso
start_date = datetime.strptime('1975-01-01', '%Y-%m-%d')
end_date = datetime.strptime('1975-12-31', '%Y-%m-%d')

random_dates = random_dates_for_week(start_date, end_date)
for date in random_dates:
    print(date.strftime('%A, %Y-%m-%d'))