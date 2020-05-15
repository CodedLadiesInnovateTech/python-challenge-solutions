"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""
x = int(input("x = "))
y = int(input("y = "))
Ans = str(x+y)
if Ans in range(15,20):
    print("20")
else:
    print(Ans)
