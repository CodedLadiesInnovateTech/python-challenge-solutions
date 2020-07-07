# Question 9
# Sort three integers without using conditional statements and loops

num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))
num3 = int(input("Enter 3rd integer: "))

x = max(num1, num2, num3)
y = min(num1, num2, num3)
z = num1 + num2 + num3 - x - y
print("Sorted version:", y, z, x)
