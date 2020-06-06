print("Conversion of hours, minutes and days to seconds")


hour = int(input("Enter the number of hours: "))

HSeconds = hour * 60 * 60
print(f'{hour} hours is {HSeconds} seconds')

minutes = int(input("Enter the number of minutes: "))
MSeconds = minutes * 60
print(f'{minutes} minutes is {MSeconds} seconds')

days = int(input("Enter the number of days: "))
Hdays = days * 60 * 60 * 24
print(f'{days} days is {Hdays} seconds')
