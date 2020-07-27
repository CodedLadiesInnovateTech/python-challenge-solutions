# Question 3
# Test whether all numbers of a list is greater than a certain number

x = int(input("Enter length of your list: "))
list1 = []
for i in range(x):
	list1.append(float(input("Enter an element to a list: ")))

num_comp = float(input("Enter the number that you want to compare: "))

z = False
j = 0
while j < x:
	if num_comp < list1[j]:
		j += 1
		continue
	else:
		print("All numbers of your list is not greater than the number you give.")
		z = True
		break
if z == False:
	print("All numbers of your list is greater than the number you give.")

