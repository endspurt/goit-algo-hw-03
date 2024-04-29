from datetime import datetime

def get_days_from_today(date):
    
    try:
        # Convert the input string to a datetime object
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Get today's date
        today = datetime.today().date()
        # Calculate the difference in days
        delta = input_date - today
        return delta.days
    except ValueError as e:
        # Print an error message if the input format is incorrect
        print(f"Please enter the date in the correct format 'YYYY-MM-DD'. Error: {e}")

# Examples of using the function
# These calls demonstrate how the function works. 
print(get_days_from_today("2020-10-09"))  # Example output 
print(get_days_from_today("2023-12-25"))  # Example output 
