# Question 3
# Midpoints of a line



x1 = float(input("Enter x of 1st point: "))
y1 = float(input("Enter y of 1st point: "))
x2 = float(input("Enter x of 2nd point: "))
y2 = float(input("Enter y of 2nd point: "))

midpoint_x = abs(x1 + x2) / 2 
midpoint_y = abs(y1 + y2) / 2

print("Midpoint of a line: (" + str(midpoint_x) + ", " + str(midpoint_y) + ")")
