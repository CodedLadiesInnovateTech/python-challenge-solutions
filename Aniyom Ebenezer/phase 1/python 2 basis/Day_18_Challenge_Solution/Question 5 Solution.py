"""
Write a Python program to check the priority of four operators (+,-,*,/)
"""

from collections import deque
import re

__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
    '+':0,
    '-':0,
    '*':1,
    '/':1,
}
operator1 = input("Input one of the four operators: ")
operator2 = input("Input another operator from the list of the four: ")
print("The operators you entered are: {} and {}".format(operator1,operator2))
print("The priority of operator1 over operator2 is: ")
print(__priority__[operator1] >= __priority__[operator2])