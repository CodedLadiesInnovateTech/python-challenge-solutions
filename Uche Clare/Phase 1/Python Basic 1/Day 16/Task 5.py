#Write a Python program to test if a variable is a list or tuple or a set.
var = ['Apple','banana','cherries','orange']
var1 = {'Apple','banana','cherries','orange'}
var2 = ('Apple','banana','cherries','orange')
print(f'The program type for {var} is: ', type(var))
print(f'The program type for {var1} is: ', type(var1))
print(f'The program type for {var2} is: ', type(var2))