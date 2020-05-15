'''4. Write a Python program to calculate number of days between two dates.
        Sample dates : (2014, 7, 2), (2014, 7, 11)
        Expected output : 9 days
    Tools: Datetime module, timedelta module'''

from datetime import date
yr1 = int(input("Please enter the dates of the first date\nEnter the fstyear: "))
mont1 = int(input("Enter the fstmonth: "))
dy1 = int(input("Enter the fstday: "))

yr2 = int(input("Please enter the dates of the second date..\nEnter the sec_year: "))
mont2 = int(input("Enter the sec_month: "))
dy2 = int(input("Enter the sec_day: "))
fst_date = date(yr1, mont1, dy1)
sec_date = date(yr2, mont2, dy2)

diff = sec_date - fst_date 
print(f"{diff.days}days")



