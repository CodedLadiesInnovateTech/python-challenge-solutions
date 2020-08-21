# Question 4
# File creation and modification date/times

import os
from datetime import datetime

file_name = input("Enter your file name: ") 
print("Modification date/time of a file:", datetime.fromtimestamp(os.path.getmtime(file_name)))
print("Creation date/time of a file:", datetime.fromtimestamp(os.stat(file_name).st_ctime))

# Note: for unix, creation date/time doesn't work.

