#Write a Python function to reverses a string if it's length is a multiple of 4. 
strng = input('Enter a word: ')
if len(strng)%4==0:
    print(strng[::-1])
else:
    print(strng)