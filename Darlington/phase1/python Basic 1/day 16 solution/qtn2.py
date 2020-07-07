#program to find the operating system name, platform and platform release date.
import os, platform
print('Operating system name')
print(os.name)
print('platform name')
print(platform.system())
print('platform release date')
print(platform.release())