# Question 7
# Get the size of a file

import os

print("File size in bytes of a plain file:",os.stat("q1.py").st_size)

# Alternative
print("File size in bytes of a plain file:",os.path.getsize("q2.py"))
