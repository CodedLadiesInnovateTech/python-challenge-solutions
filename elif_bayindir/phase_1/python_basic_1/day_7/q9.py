# Question 9
# Convert height (in feet and inches) to centimeters.

height = float(input("Enter the height (in feet and inches): "))
types = input("Feet or Inch? ")

if types == 'Feet':
	height *= 30.48
elif types == 'Inch':
	height *= 2.54
print("Height: " + str(height) +" cm")
