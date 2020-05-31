# Question 7
# Convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure

kp = float(input("Enter pressure in kilopascals: "))
pps = 0.145037738 * kp
mm = 7.50061683 * kp
ap = 0.00986923266 * kp

print(str(round(pps, 2)) + " pounds per square inch, " + str(round(mm, 2)) + " millimeter of mercury (mmHg), " + str(round(ap, 2)) + " atmosphere pressure")
