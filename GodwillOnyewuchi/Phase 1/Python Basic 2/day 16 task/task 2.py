# Write a Python program to find the operating system name, platform and platform release date

import os
import platform
print(f'Operating system name: {os.name}')
print()
print(f'Platform name: {platform.system()}')
print()
print(f'Platform release: {platform.release()}')

