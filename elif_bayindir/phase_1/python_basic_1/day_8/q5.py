# Question 5
# Convert seconds to day, hour, minutes and seconds

second = float(input("Enter number of seconds: "))
day = second / (3600 * 24)
second %= (3600 * 24)
hour = second / 3600
second %= 3600
minute = second / 60
second %= 60
print("Day: " + str(round((day))) + ", hours: " + str(round((hour))) + ", minutes: " + str(round((minute))) + ", seconds: " + str(round((second))))


