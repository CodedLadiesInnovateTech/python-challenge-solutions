#2. Write a Python program to print the calendar of a given month and year.
       # Tools: Use 'calendar' module.

import calendar

y = int(input("Enter year: "))
m = int(input("Enter month: "))
print(calendar.month(y, m))