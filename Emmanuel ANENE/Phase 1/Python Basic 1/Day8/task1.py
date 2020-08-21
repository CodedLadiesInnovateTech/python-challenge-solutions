'''
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
'''

varF = int(input("Enter your distance in feet: "))

totalI = round(float(varF * 12), 3)
totalY = round(float(varF * 0.33), 3)
totalM = round(float(varF * 0.000189394), 3)

print("The give distance in feet is: \n{0} inches, \n{1} miles and \n{2} yards.".format(totalI, totalM, totalY))

