import sys

if sys.byteorder == "little":
    # intel, alpha
    print("Little-endian platform.")
else:
    # motorola, sparc
    print("Big-endian platform. \n")
