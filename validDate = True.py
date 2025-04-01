validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1

# The maximum number of days in each month (adjusting for months with less than 31 days)
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Function to check if it's a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Adjust February for leap years
def adjust_february(year):
    if is_leap_year(year):
        days_in_month[2] = 29
    else:
        days_in_month[2] = 28

# Get user input
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# Adjust February days for leap year check
adjust_february(year)

# Check if year, month, and day are valid
validDate = True

if year <= MIN_YEAR:  # invalid year
    validDate = False
elif month < MIN_MONTH or month > MAX_MONTH:  # invalid month
    validDate = False
elif day < MIN_DAY or day > days_in_month.get(month, 31):  # invalid day
    validDate = False

# Output result
if validDate:
    print(f"{month}/{day}/{year} is a valid date.")
else:
    print(f"{month}/{day}/{year} is an invalid date.")