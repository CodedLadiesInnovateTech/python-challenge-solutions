"""
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
    Tools: abs function, input function, math
    """
import math
x = float(input("What is your x value ? "))
diff = x - 17
if x>17:
    print(2*abs(diff))