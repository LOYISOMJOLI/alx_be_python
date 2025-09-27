from datetime import date
from datetime import timedelta

def display_current_datetime:
    current_date = datetime.now()
    print("Current date and time:", current_date)
    numOfDays =int( input("Enter the number of days to add to the current date:"))
    future_date = current_date.today() + timedelta(numOfDays)
    print("future_date:",future_date)

display_current_datetime()
