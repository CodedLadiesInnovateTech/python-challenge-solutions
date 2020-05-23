#difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
x = int(input('Enter the number:'))
y = 17 
n = y-x
if x > 17:
    print(abs(n)*2)   
else:
    print(n)