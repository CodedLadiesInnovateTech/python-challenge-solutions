#5. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

x = int(input("Enter an integer:"))
y = int(input("Enter another Integer:"))

if(x == y) or (y - x == 5) or (x - y ==5) or (x + y == 5):

    sum = True
else:
    sum = False

print(sum)