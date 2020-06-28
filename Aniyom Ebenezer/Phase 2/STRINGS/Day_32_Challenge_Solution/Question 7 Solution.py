"""
Write a Python program to display a number in left, right and center aligned of width 10.
"""
x = 22
print("Original number is: {}".format(x))
print("Left Aligned (Width 10) is: {:<10d}".format(x))
print("Right Aligned (Width 10) is: {:10d}".format(x))
print("Centered Aligned (Width 10) is:{:^10d}".format(x))