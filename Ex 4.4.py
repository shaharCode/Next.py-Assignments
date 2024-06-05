
def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month == 2:
        if leap_year:
            days = 29
        else:
            days = 28
    else:
        days = 30

    for day in range(1, days + 1):
        yield day


def gen_date():
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield "%02d/%02d/%04d %02d:%02d:%02d" % (day, month, year, hour, minute, second)


date_generator = gen_date()
iterations = 0

while True:
    date = next(date_generator)
    iterations += 1
    if iterations % 1000000 == 0:
        print(date)


# for gt in gen_time():
#     print(gt)
