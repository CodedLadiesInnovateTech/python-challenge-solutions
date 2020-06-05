# Question 1
# Concatenate N strings

list1 = []

x = input("Enter a string: ")
list1.append(x)

while x != "":
	x = input("Enter a string: ")
	list1.append(x)
print(''.join(list1))

# Alternative without append and join

""" list2 = ""
y = input("Enter a string: ")
list2 += y
while y != "":
	y = input("Enter a string: ")
	list2 += y
print(list2) """
