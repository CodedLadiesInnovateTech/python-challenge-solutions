from __future__ import print_function

import sys


# Assuming digit 3456 is depicted as abcd
def sum_integer_digits(num):
    if len(str(num)) > 4:
        print("Integer should not be more than four digits:", num,  file=sys.stderr, end="\n")
    else:
        a = num // 1000
        b = (num - a * 1000) // 100
        c = (num - a * 1000 - b * 100) // 10
        d = num - a * 1000 - b * 100 - c * 10
        print("The sum of digits in the number is", a + b + c + d)


number = int(input("Input an Integer not more than four digit numbers: "))
sum_integer_digits(number)
