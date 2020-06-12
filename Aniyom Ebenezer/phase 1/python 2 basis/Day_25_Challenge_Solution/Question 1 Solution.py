"""
Write a Python program to randomly generate a list with 10 even numbers between 1 and 100 inclusive.
Note: Use random.sample() to generate a list of random values.
Sample Output:
[4, 22, 8, 20, 24, 12, 30, 98, 28, 48]
"""
import random
result = random.sample([i for i in range(1,100) if i%2==0], 10)
print(result)