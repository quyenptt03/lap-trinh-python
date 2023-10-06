'''12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.'''

import calendar

month = int(input("Month: "))
year = int(input("Year: "))
print(calendar.month(year,month))