'''3. Write a Python program to display the current date and time.
    Sample Output :
        Current date and time : 2014-07-05 14:34:14'''

import datetime 
current_date_and_time = datetime.datetime.now()
print('Current date and time : ',current_date_and_time.strftime("%Y-%m-%d %H:%M:%S"))