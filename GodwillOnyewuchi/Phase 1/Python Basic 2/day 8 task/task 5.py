
import math
print("Conversion of seconds to hours, minutes and days ")

seconds = int(input("Enter the number of seconds: "))

minutes = math.ceil(seconds / 60)
print(f'{seconds} seconds is {minutes} minutes')

hours = math.ceil(seconds / 60 / 60)
print(f'{seconds} seconds is {hours} Hours')

days = math.ceil(seconds / 60 / 60 / 24)
print(f'{seconds} seconds is {days} days')