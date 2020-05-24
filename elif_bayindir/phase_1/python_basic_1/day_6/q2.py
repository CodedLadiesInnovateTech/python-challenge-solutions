# Question 2
# 32 bit or 64 bit mode on OS.

import struct
print(struct.calcsize('P') * 8)
