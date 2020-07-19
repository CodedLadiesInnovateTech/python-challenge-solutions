''' Write a Python program which accepts the radius of a circle from the user and compute the area.'''

def area(n):
    n = int(input("Please input a radius ? "))
    pi = 22/7
    result = pi * (n**2)
    print("The Area of the circle is {}".format(result))


area(0)

radius = int(input("Please input a radius ? "))
pi = 22/7
result = pi * (radius**2)
print("The Area of the circle is {}".format(round(result,2)))
