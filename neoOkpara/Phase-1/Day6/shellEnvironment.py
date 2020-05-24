import platform
import struct
import sys

print (platform.architecture()[0], sys.maxsize > 2 ** 32)

print(8 * struct.calcsize("P"))
