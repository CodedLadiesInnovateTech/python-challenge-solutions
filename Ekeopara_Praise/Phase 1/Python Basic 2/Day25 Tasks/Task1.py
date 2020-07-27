'''1. Write a Python program to randomly generate a list with 10 even numbers between 1 and 100 inclusive.
Note: Use random.sample() to generate a list of random values.
Sample Output:
[4, 22, 8, 20, 24, 12, 30, 98, 28, 48]'''

import random 
evenlist = list(filter(lambda x: x % 2 ==0, list(range(1, 101))))
print(random.sample(evenlist, 10))