#Write a Python program to display some information about the OS where the script is running.
import platform
os_profile = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]
for key in os_profile:
  if hasattr(platform, key):
    print(key +  ": " + str(getattr(platform, key)()))