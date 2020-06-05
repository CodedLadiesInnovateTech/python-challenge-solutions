# Question 8
# get the system time.
# Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.

from datetime import datetime

print("System time:", datetime.now().strftime("%H:%M:%S"))

# Alternative,

import time

print("System time:", time.strftime("%H:%M:%S", time.localtime()))

# Alternative,

import time

print(time.ctime())
