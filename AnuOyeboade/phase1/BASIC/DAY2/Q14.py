"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
from datetime import date
first = date(2014,7,2)
second = date(2014,7,11)
Difference  = second - first
print(Difference.days)
