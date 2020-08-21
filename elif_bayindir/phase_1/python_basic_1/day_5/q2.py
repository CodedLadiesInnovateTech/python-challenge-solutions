# Question 2
# Least common multiple of 2 positive integers

num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))

mul = num1 * num2 # mul: multiple

while(mul > 0):
	if mul % num1 == 0 and mul % num2 == 0:
		lcm = mul
	mul -= 1

print(lcm)

