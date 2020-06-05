# Write a Python program to display some information about the OS where the script is running

import platform as pl

os_profile = [
            "architecture"
            "window_distributiion"
            "win_version"
            "machine"
            "node"
            "platform"
            "processor"
            "python_build"
            "python_compiler"
            "python_version"
            "Release"
            "system"
            "uname"
            "version"
]
for key in os_profile:
    if hasattr(pl, key):
        print(key + ":" + str(getattr(pl, key)()))

#refernce: w3resource