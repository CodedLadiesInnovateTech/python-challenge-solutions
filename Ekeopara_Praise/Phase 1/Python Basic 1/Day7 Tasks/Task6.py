'''6. Write a Python program to get height and width of the console window.'''


import shutil
columns, rows = shutil.get_terminal_size()
print(f"The height is {rows} and the width is {columns}")

