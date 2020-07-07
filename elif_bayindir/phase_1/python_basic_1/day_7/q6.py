# Question 6
# Height and width of the console window.

import os 
  
print(os.get_terminal_size()) 

# Alternative,
""" import shutil
columns, rows = shutil.get_terminal_size()
print("columns: " + str(columns) + ", rows: " + str(rows)) """

	

