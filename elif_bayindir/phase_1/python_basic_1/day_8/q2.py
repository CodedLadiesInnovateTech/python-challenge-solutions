# Question 2
# Convert all units of time into seconds.

day = float(input("Enter number of days: "))
hour = float(input("Enter number of hours: "))
minute = float(input("Enter number of minutes: "))
second = float(input("Enter number of seconds: "))
day = day * 3600 * 24
hour *= 3600
minute *= 60
second = day + hour + minute + second
print("Time: " + str(round((second),2)) +" seconds. ")
