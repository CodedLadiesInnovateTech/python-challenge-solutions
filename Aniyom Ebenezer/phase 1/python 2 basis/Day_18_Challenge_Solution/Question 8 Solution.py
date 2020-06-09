"""
Write a Python program to find the median among three numbers
"""
x = int(input("Input the first number: "))
y = int(input("Input the second number: "))
z = int(input("Input the third number: "))
print("The median among the three numbers {}, {} and {} is: ".format(x, y, z))
if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)
elif x < y and y < z:
    print(y)
elif z < y and y < x:
    print(y)
elif x < z and z < y:
    print(z)
elif y < z and z < x:
    print(z)
else:
    print("The numbers are equal.")