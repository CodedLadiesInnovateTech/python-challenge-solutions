"""
Write a Python program using Seive Eratosthenes method for computing primes upto a specified number.
"""
n = 100
prime_list = [ ]
for i in range(2, n+1):
    if i not in prime_list:
        print(i)
        for j in range(i*i, n+1, i):
            print(prime_list.append(i))