#Python program to test whether the system is a big-endian platform or little-endian platform
import sys

if sys.byteorder == "little":
    print("Little-endian platform.")   # its an intel, alpha
else:
    print("Big-endian platform.")   # its a motorola, sparc