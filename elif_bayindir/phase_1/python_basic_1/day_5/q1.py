# Question 1
# Greatest common divisor of 2 positive integers 

num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))

if num1 > num2:
	if num1 % num2 == 0:
		gcd1 = num2
	a = num2
elif num2 > num1:
	if num2 % num1 == 0:
		gcd1 = num1
	a = num1
gcd2 = 1
for i in range(2, a+1):
	if num1 % i == 0 and num2 % i == 0:
		gcd2 = i

print(gcd2)
