'''
Write a Python program to get OS name, platform and release information.
'''

import os as os
import platform

osname = input('''Care to know the OS of your sytem? 'y/n' or 'quit' to abort. ''')
plat = input("What about the platform it's running? ")
info = print("Since you selected the above, lemme give you the release info too :)\n\n")

if osname.lower().startswith("y"):
    print("OS name: ", os.name, end="\n")
else:
    print("Aborted!", end="\n")

if plat.lower().startswith("y"):
    print("Platform: ", platform.system(), end="\n")
else:
    print("Sorry, I can't do this.", end="\n")

if True:
    print("Release info: ", platform.release(), end="\n")
else:
    print("You can't be given the entire information.", end="\n")

print("*__*" * 10, end="\n\n")