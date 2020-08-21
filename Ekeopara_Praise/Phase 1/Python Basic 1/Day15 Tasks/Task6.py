'''6. Write a Python program to find files and skip directories of a given directory.'''
import os
print([f for f in os.listdir(r'C:\Users\Sir_Praise\Documents\PYTHON LEARNING\ATM_machine.py') if os.path.isfile(os.path.join(r'C:\Users\Sir_Praise\Documents\PYTHON LEARNING\ATM_machine.py', f))])