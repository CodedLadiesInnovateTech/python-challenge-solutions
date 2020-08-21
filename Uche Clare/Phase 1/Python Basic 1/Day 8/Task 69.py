#program to sort three integers without using conditional statements and loops.
list = []
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

list.append(a)
list.append(b)
list.append(c)

print(sorted(list))