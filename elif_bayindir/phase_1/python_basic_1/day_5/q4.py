# Question 4
# Sum of 2 integers, if sum is between 15 to 20 it will return 20

num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))

sum1 = num1 + num2
if sum1 >= 15 and sum1 < 20: # alternative,  if sum1 in range(15, 21):
	sum1 = 20
print(sum1)
