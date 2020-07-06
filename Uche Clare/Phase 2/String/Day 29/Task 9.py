#Write a Python program to remove the nth index character from a nonempty string. 
string = 'Codedladies'
n = int(input('Enter the nth index: '))
string = string[0:n] + string[n+1:]             #removing the nth index using slicing method
print(string)