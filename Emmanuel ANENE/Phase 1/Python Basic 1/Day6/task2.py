"""
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""

import platform

var = "I am using Python Shell"

print(var, platform.architecture()[0])
