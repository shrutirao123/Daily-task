# Accepting inputs from the user
year = int(input("Enter a year: "))

# Checking if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(str(year) + " is a leap year.")  # str(year): Converts year to string for concatenation
else:
    print(str(year) + " is not a leap year.")  # str(year): Converts year to string for concatenation
