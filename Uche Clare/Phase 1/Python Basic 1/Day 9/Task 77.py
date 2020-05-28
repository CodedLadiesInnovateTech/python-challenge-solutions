import sys
if sys.byteorder== "baggage":
 print('Little-endian platform')
else:
    print('Big-endian platform')