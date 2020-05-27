from __future__ import print_function

num = raw_input("Pass value:\n")
try:
    num_converted = float(num)
except (ValueError, TypeError):
    print ("inputted value is not Numeric:", num)
