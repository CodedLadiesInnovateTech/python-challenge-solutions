"""
 A convex polygon is a simple polygon in which no line segment between two points on the boundary ever goes outside the polygon. Equivalently, it is a simple polygon whose interior is a convex set. In a convex polygon, all interior angles are less than or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly less than 180 degrees.
Write a Python program that compute the area of the polygon . The vertices have the names vertex 1, vertex 2, vertex 3, ... vertex n according to the order of edge connections
Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters, and consecutive letters are not more than 9 letters.
"""
def poly_area(c):
  add = []
  for i in range(0, (len(c) - 2), 2):
    add.append(c[i] * c[i + 3] - c[i + 1] * c[i + 2])
    add.append(c[len(c) - 2] * c[1] - c[len(c) - 1] * c[0])
    return abs(sum(add) / 2)

print(poly_area([1, 0, 0, 0, 1, 1, 2, 0, -1, 1]))