'''8. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. 
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt'''

def first_three(str):
	return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))

#Reference: w3resource