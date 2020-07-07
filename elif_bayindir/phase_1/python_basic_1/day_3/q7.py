# Question 7
# Test a number is in range

import math

num = float(input("Enter a number: "))

if num in range(100, 1000):
	print("Your number is in range (100, 1000)")
else num in range(100, 2000):
	print("Your number is in range (100, 2000)")
else:
	print("Your number is smaller than 100 or larger than 2000")
