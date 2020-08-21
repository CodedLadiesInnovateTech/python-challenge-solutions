# Question 4
# Number of days between two dates

from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
print("Expected output: " + str((date2 - date1).days) + " days")

# I couldn't use timedelta module
