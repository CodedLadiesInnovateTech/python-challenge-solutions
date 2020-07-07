'''2. Write a Python program to create all possible strings 
by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.'''
import random
lst = ['a', 'e', 'i', 'o', 'u']
random.shuffle(lst)
x = "".join(lst)
print(x)