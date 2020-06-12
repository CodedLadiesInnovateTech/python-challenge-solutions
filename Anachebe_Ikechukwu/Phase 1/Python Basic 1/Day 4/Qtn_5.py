#5. Write a Python program to check whether a specified value is contained in a group of values.
#Test Data :
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False


ab = int(input("Enter a number:"))

xy = [1, 2, 3, 5, 7, 11, 13]

if ab in xy:
    print(True)
else:
    print(False)