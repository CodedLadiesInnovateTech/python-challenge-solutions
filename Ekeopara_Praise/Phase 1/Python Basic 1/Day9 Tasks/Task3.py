'''3. Write a Python program to calculate midpoints of a line.'''
def midpoint(x1, y1, x2, y2):
    x = (x1+x2)/2
    y = (y1+y2)/2
    return f"The midpoints of x and y are {x} and {y} respectively"
print(midpoint(2, 2, 4, 4))

