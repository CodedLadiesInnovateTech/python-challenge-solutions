import math

y = int(input("Enter a positive integer:"))
x = int(input("Enter another positive integer:"))

z = math.gcd(x,y)

print("the greatest common divisor of", y, "and", x, "is", z)