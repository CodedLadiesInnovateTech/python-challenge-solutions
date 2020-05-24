# Question 1
# Check whether a file exists.

import os.path

open("new_file.py", "w")
if os.path.isfile("new_file.py"):
	print("File exist")
else:
	print("File not exist")

