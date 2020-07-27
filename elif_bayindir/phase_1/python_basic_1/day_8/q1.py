# Question 1
# Convert the distance (in feet) to inches, yards, and miles

height = float(input("Enter the distance (in feet): "))

inch = height * 12
yard = height / 3
mile = height / 5280

print("Distance: " + str(inch) +" inches, " + str(round((yard),2)) +" yards, " + str(round((mile),4)) +" miles.")


