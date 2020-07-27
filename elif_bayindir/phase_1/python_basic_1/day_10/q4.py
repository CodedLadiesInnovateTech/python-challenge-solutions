# Question 4
# Count the number occurrence of a specific character in a string

string = input("Enter a string: ")
char = input("Enter a character: ")

k = 0
i = 0
for i in range(len(string)):
	if string[i] == char:
		k += 1
	else: 

		continue
print(k)

# Alternative,
# print(string.count(char))
