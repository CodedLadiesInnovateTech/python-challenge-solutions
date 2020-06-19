'''9. Write a Python program to get the last part of a string before a specified character. 
https://www.codedladiesinnovateyech.com/about-us
Output:
https://www.codedladiesinnovateyech.com/about '''

def first_three(str):
	return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))

#Reference: w3resource