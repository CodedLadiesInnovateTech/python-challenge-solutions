#program to calculate the hypotenuse of a right angled triangle
import math
def hypotenuse(a, b):
 c= (math.sqrt(math.pow(a, 2) + math.pow(b, 2)))
 return c
print(hypotenuse(5,4))