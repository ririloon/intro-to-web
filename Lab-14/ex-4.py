from datetime import datetime, timedelta

def simple_month_calendar(year, month):
    # Start with the first day of the month
    current_date = datetime(year, month, 1)

    # Determine the weekday for the first day (Monday=0, Sunday=6)
    start_weekday = current_date.weekday()

    # Find the first day of the next month to determine the last day of the current month
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    last_date = next_month - timedelta(days=1)

    # Print the calendar header
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Print indentation for the first week
    print("    " * start_weekday, end="")

    # Loop through all the days of the month
    while current_date <= last_date:
        # Print the day number, formatted to 3 spaces
        print(f"{current_date.day:3}", end=" ")
        # Check if the current day is Sunday (weekday 6 when Monday is 0)
        if current_date.weekday() == 6:
            print()  # New line at the end of the week
        # Move to the next day
        current_date += timedelta(days=1)

    print()  # New line at the end

# Generate a calendar for May 2025
simple_month_calendar(2025, 5)
