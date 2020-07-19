# Write a Python program to find the number of divisors of a given integer is even or odd
#
number = 12
divisors = []
for i in range(1, number+1):
    if number % i == 0:
        divisors.append(i)

print(len(divisors))