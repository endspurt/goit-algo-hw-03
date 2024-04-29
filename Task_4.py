from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Define the function to find users with birthdays in the next 7 days including today
    today = datetime.today().date()
    upcoming = []

    for user in users:
        # Parse the birthday string into a date object
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Calculate this year's birthday
        birthday_this_year = birthday_date.replace(year=today.year)

        # Check if this year's birthday has already passed and set the next birthday
        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=today.year + 1)

        # Calculate the day difference from today
        days_difference = (birthday_this_year - today).days

        # Check if the birthday is within the next 7 days
        if 0 <= days_difference <= 7:
            # Adjust for weekend birthdays
            if birthday_this_year.weekday() == 5:  # Saturday
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Sunday
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year

            # Store the user's name and the adjusted congratulation date
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming

# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Liste der Grüße für diese Woche:", upcoming_birthdays)
