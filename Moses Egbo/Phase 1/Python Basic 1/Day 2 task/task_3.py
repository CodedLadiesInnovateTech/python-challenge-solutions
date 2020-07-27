''' Write a Python program to display the current date and time.
    Sample Output :
        Current date and time : 2014-07-05 14:34:14 '''

from datetime import datetime
today = datetime.today()
print("Today's date and time is ",today)


import datetime
date_time = datetime.datetime.now()
print("Current date and time: ", date_time.strftime("%Y-%m-%d %H:%M:%S"))
