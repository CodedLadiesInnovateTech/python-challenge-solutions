#7. Write a Python program to test whether a number is within 100 of 1000 or 2000.
#    Tools: maths,input function

num = int(input("Enter an Integer number:"))

if (900 <= num <= 1100) or (1900 <= num <= 2100 ):
    print(True)
else:
    print(False)
