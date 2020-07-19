# Question 2
# Count number 4 in a list

list1 = [1, 2, 10, 4, 3, 4, 4, 4, 1, 3, 5]

x = 0 
for i in range(len(list1)):
	if list1[i] == 4:
		 x += 1
print("Number of 4 in the list:", x)
