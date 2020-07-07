# Question 7
# Concatenate all elements in a list into a string

lst = [] # lst: list
elm = int(input("Enter number of elements in the list: "))  # elm: element

elm_str = ""
for i in range(elm):
	lst.append(int(input("Add a new integer to your list: ")))
	elm_str += str(lst[i])

print("Your list:", lst)
print("Concatenated elements as a string:", elm_str)

# if the list does not contain numbers, we just use following lines
""" 
lst.append(input("Add a new element to your list: "))
elm_str += lst[i]
"""
