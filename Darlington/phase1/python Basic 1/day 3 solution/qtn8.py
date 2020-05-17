#program sum of three numbers

import math
num1 = float(input('Enter a number 1 \n'))
num2 = float(input('Enter a number 2 \n'))
num3 = float(input('Enter a number 3 \n'))
sum = num1+num2+num3
if num1 == num2 == num3:
    print(sum*3)
else:
    print(sum)    