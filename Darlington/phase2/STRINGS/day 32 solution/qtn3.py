# program to print the following integers with zeros on the left of specified width.
x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x));
print("Original Number: ", y)
print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y));
print()