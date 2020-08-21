#Write a Python program to find the operating system name, platform and platform release date.
import os
import platform
print('The Operating system name is ', os.name)
print('The Platform is', platform.system())
print('The Platform release date is ',platform.release())