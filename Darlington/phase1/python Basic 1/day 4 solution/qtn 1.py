#program even or odd number
import math
num = int(input('Enter any positive integer \n'))
even = num % 2
#print(even)
if even == 0:
    print(f'{num} is an even number!!')
else:
    print(f'{num} is an odd number!!')        