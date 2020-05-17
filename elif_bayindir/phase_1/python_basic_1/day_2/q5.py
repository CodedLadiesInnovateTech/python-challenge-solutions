# Question 5

# Reverse of your first and last name by list slicing

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
print(name[::-1] + " " + last_name[::-1])

# slice(start, end, step) 
# name[0:len(name)] == name[:len(name)], normal order
# name[-3:], start from third element from the end and goes to end
# name[0:-1] == name[:-1], don't contain last element
# 3rd parameter is step parameter
# name[::4], first element to last element by step 4
# name[::-1], negative step creates reversed list,
# name[-1::-1], again reversed list -1 is the last element of the list
