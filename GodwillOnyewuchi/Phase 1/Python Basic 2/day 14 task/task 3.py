# Write a Python program to determine the largest and smallest integers, longs, floats

import sys

Largest_Float = sys.float_info.max
Smallest_Float = sys.float_info.min
Largest_Integer = sys.maxsize

print(f'Largest_Float number is {Largest_Float}')
print(f'Smallest Float number is {Smallest_Float}')
print(f'Largest integer is {Largest_Integer}')
