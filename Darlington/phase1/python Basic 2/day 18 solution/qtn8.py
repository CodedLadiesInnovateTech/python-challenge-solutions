# program to find the median among three given numbers.
x = input("Input the first number:")
y = input("Input the second number:")
z = input("Input the third number:")
print("Median of the above three numbers -")

if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)
    
elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)
    
elif y < z and z < x:
    print(z)    
elif x < z and z < y:
    print(z)