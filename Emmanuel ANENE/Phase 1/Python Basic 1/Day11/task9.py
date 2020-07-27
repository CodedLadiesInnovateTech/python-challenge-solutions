'''
Write a Python program to clear the screen or terminal.
'''

from os import system, name
from time import sleep

def clearScreen():
    if name == "nt":
        varClr = system('cls')
    else:
        varClr = system('clear')

print('#100DaysofPython \n' * 10)
print("This screen will cleared after 60 seconds.")

sleep(60)
clearScreen()
