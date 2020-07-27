#program to calculate midpoints of a line.
x1 = float(input('The value of x1: '))
y1 = float(input('The value of y1: '))

x2 = float(input('The value of x1: '))
y2 = float(input('The value of y2: '))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print();
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print(f"The midpoint of line is : {(x_m_point, y_m_point)}")
