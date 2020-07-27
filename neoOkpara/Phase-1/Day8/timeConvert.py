from __future__ import print_function

# Converting Day to Seconds
day_num = int(input("Input number of days: "))
sec_in_day = day_num * 24 * 60 * 60
print ("There are {0} seconds in {1} day(s)".format(sec_in_day, day_num))

hours_num = int(input("Input number of hours: "))
sec_in_hour = hours_num * 60 * 60
print ("There are {0} seconds in {1} hour(s)".format(sec_in_hour, hours_num))

minutes_num = int(input("Input number of minutes: "))
sec_in_min = minutes_num * 60
print ("There are {0} seconds in {1} minute(s)".format(sec_in_min, minutes_num))
