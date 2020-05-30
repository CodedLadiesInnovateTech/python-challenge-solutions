# program to determine if the python shell is executing in 32bit or 64bit mode on operating system.
import struct
print(struct.calcsize("p") * 8)