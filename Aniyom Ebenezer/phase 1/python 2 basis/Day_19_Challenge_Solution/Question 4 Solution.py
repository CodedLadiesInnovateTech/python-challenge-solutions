"""
Write a Python program to find the number of divisors of a given integer is even or odd
"""
n = int(input("Input a number: "))
for i in range(n):
    x = len([i for i in range(1, n+1) if not n % i])
print(x)