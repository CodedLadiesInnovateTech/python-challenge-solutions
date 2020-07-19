# Question 6
# Create a histogram from a list of integers

lst = [] # lst: list
num = int(input("Enter length of the list: ")) 

for i in range(num):
	lst.append(int(input("Add a new number to your list: ")))
print("Your list:", lst)
for j in range(num):
	k = 0
	for k in range(lst[j]):
		print("#", end=' ')
	print(" ")

	

	

