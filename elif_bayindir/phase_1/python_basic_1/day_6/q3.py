# Question 3
# Get OS name, platform and release information.

import os
import platform

print("OS name:", os.name)
print("Platform:", platform.system())
print("Release:", platform.release()) # print(os.uname().release)

# Alternative, print(os.uname())



