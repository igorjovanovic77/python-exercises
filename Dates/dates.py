
def leap_year(year):
    if year % 4 > 0:
        return False
    elif year % 100 > 0:
        return True
    elif year % 400 > 0:
        return False

    return True

def days_per_year(year):
    return 365 if not leap_year(year) else 366

def days_between_years(year1, year2):
    year = year2 - 1
    result = days_per_year(year1 + 1)
    while year > year1 + 1:
        result = result + days_per_year(year)
        year = year - 1
    return result

def days_in_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month != 2:
        return 30

    return 29 if leap_year(year) else 28


def add_one_day(tdate):

    y,m,d = tdate

    d=d+1
    if d > days_in_month(y, m):
        d = 1
        m = m+1

    if m == 13:
        d = 1
        m = 1
        y += 1

    return (y, m, d)

def days_between_dates(from_date, to_date):

    the_date = from_date
    nr_days = 0
    while the_date != to_date:
        nr_days += 1
        the_date = add_one_day(the_date)

    return nr_days

