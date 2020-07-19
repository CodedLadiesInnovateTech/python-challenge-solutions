#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
import random
vowels = ['a', 'e', 'i', 'o', 'u']

random.shuffle(vowels)
char = "".join(vowels)

print(char)

