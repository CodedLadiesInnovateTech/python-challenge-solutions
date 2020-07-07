'''4. Write a Python program to check whether three given lengths (integers) of three sides
 form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No".
Input:
Integers separated by a single space.
1 = length of the side = 1,000
Input three integers(sides of a triangle)
8 6 7
No'''

def check_iftriangle(x, y, z):
    if x**2+y**2==z**2:
        response = 'Yes'
    else:
        response = 'No'
    return response
print(check_iftriangle(8, 6, 7))
print(check_iftriangle(4, 3, 5))

