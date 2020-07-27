print("Conversion of feet to inches, yards and miles ")


feet = int(input("Enter the number of feet: "))

inches = feet * 12
print(f'{feet} feet is {inches} inches')

yards = feet / 3
print(f'{feet} feet is {yards} yards')

miles = feet / 5280
print(f'{feet} feet is {miles} miles')
