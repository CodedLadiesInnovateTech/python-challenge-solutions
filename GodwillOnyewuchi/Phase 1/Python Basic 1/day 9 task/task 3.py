#Python program to calculate midpoints of a line
print(' Program to Calculate the midpoint of a line ')

x1 = float(input('The value of x (the first endpoint): '))
y1 = float(input('The value of y (the first endpoint): '))

x2 = float(input('The value of x (the first endpoint): '))
y2 = float(input('The value of y (the first endpoint): '))

x_axis = (x1 + x2)/2
y_axis = (y1 + y2)/2

print(f'The midpoint in x value is: {x_axis}')
print(f'The midpoint in y value is: {y_axis}')
