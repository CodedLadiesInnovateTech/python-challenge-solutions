'''1. Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
   Sample data:
   /*
   X = [10, 20, 20, 20]
   Y = [10, 20, 30, 40]
   Z = [10, 30, 40, 20]
   target = 70
   */ '''
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]

for x in X:
   for y in Y:
      for z in Z:
         if x+y+z==70:
            print((x, y, z))

   