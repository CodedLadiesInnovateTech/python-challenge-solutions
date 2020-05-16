#program range of numbers
import math
number = int(input('Enter a number \n'))
if number in range(0, 100):
    print('The number is within 0-100')
elif number in range(100, 1000):
    print('The number is within 100-1000')   
elif number in range(1000, 2000):  
    print('The number is within 1000-2000')   
else:
    print('The number is out of the range')



