import calendar
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

Calendar = calendar.month(year, month)
print(Calendar)