'''2. Write a Python program to print the calendar of a given month and year.
        Tools: Use 'calendar' module'''
#Solution
import calendar 
yr = int(input("Enter the year: "))
mont = int(input("Enter the month: "))
print(calendar.month(yr, mont))