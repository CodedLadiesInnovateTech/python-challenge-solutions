#program to that reads a date (from 2016/1/1 to 2016/12/31) 
# and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year.
from datetime import date
print("Input month and date (separated by a single space):")
m, d = map(int, input().split())
weeks = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
w = date.isoweekday(date(2016, m, d))
print("Name of the date: ",weeks[w])