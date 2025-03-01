from datetime import datetime

today = datetime.now()

new_years_eve = datetime(today.year, 12, 31)

if today > new_years_eve:
    new_years_eve = datetime(today.year + 1, 12, 31)

time_until_new_year = new_years_eve - today

print("Days until New Year's Eve:", time_until_new_year.days)
