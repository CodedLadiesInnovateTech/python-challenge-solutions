# Write a Python program to find common divisors between two numbers in a given pair

a = 12
b = 16
divisors = []
if a > b:
    smaller = b
else:
    smaller = a
print(smaller)
for i in range(1, smaller + 1):
    if a % i == 0 and b % i == 0:
        divisors.append(i)

print(divisors)
