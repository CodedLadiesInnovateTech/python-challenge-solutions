'''
5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
    Tools: input function, list slicing
'''

#5
print('Enter First Name: ')
First_name = input()
print('Enter Last  Name:')
Last_name = input()
list = [First_name, Last_name]
print(list)
First_name,Last_name = Last_name,First_name
x = [First_name, Last_name]
print(x)
new_list = list.reverse()
print(new_list)