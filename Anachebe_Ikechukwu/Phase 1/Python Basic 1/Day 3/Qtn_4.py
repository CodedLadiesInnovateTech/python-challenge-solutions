#4. Write a Python program to calculate number of days between two dates.
       # Sample dates : (2014, 7, 2), (2014, 7, 11)
        #Expected output : 9 days
    #Tools: Datetime module, timedelta module

from datetime import date
date_1 = date(2020, 1, 24)
date_2 = date(2020, 6, 24)
days = date_2 - date_1
print(days.days)