import calendar


def weekdays_per_month(yy, mm=None):
    '''
    Return weekday count for a month if month is provided,
    else return the weekday count for each month for an year.
    Considering Saturday and Sunday as weekends
    '''
    month_range = range(1,13)
    week_days = 0
    week_days_count = {}
    total_weekdays = 0
    year = yy
    for month in month_range:
        month_metrix = calendar.monthcalendar(year,month)
        month_name = calendar.month_name[month]
        for week in month_metrix:
            for enum, day in enumerate(week):
                if enum in range(0,5) and day != 0:
                    week_days += 1
                    total_weekdays += 1
            week_days_count[month_name] = week_days
        week_days = 0

    if mm:
        month_name = calendar.month_name[mm]
        week_day_count = week_days_count[month_name]
        return f'{month_name}: {week_day_count}'
    return week_days_count, total_weekdays


## Testing --> uncomment below
# print(weekdays_per_month(2024,3))
# print(weekdays_per_month(2023))