# Question 5
# Return true if the two given integer values are equal or their sum or difference is 5.

num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))

if num1 == num2 or num1 + num2 == 5 or num1 - num2 == 5 or num2 - num1 == 5:
	print(True)
