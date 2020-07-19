# Question 8
# Sum of the first n positive integers.

num = int(input("Enter number of integers: "))

total = 0
for i in range(num+1):
	total += i
print("Sum of the first " + str(num) + " positive integers: " + str(total))
		 
# Alternative,
""" total = num * (num + 1) / 2
print(total) """
