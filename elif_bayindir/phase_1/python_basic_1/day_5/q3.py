# Question 3
# Sum of 3 integers, if 2 values are equal sum will be zero.

num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))
num3 = int(input("Enter 3rd integer: "))

if num1 == num2 or num2 == num3 or num1 == num3:
	print("Sum of 3 integers:", 0)
else:
	print("Sum of 3 integers:", num1 + num2 + num3)
