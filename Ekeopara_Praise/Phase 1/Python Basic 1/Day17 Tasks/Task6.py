'''6. Write a Python program to get the third side of right angled triangle from two given sides.'''
#from math import sqrt
def thirdside(hypo, oppo, adj):
    if hypo == 'x':
        sd3 = (oppo**2 + adj**2)**0.5
    elif oppo == 'x':
        sd3 = (hypo**2 - adj**2)**0.5
    elif adj == 'x':
        sd3 = (hypo**2 - oppo**2)**0.5
    else:
        print("Enter the right values")

    return sd3
print(thirdside('x', 4, 5))
print(thirdside(6, 'x', 5))
print(thirdside(5, 4, 'x'))

