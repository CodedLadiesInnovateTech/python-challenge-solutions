import datetime
now=datetime.datetime.now()
print("current date and time",end=":")
print(now.strftime("%Y-%m-%d  %H:%M:%S"))