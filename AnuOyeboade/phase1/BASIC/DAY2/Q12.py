"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""
import calendar
def calendarKnow(year, month):
    print(calendar.month(year, month))
y = int(input("Enter the year : "))
m = int(input("Enter the month : "))
calendarKnow(y, m)




