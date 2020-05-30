# Question 1
# Get a directory listing, sorted by creation date

import os 

os.chdir('/home/elif/Desktop')
print(sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime))
