#program to convert height (in feet and inches) to centimeters.
print("Input your height: ")
hei_ft = int(input("Feet: "))
hei_inch = int(input("Inches: "))

hei_inch += hei_ft * 12
hei_cm = round(hei_inch * 2.54, 1)

print("Your height is : %d cm." % hei_cm)