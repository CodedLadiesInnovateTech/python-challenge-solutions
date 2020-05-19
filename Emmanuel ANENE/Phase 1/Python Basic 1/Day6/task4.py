'''
Write a Python program to locate Python site-packages.
'''

import site

print("My Python Site Packages can be found here below:",
site.getsitepackages(),sep="\n \n", end="\n \n")