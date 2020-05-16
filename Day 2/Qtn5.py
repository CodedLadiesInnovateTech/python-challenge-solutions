"""
5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
    Tools: input function, list slicing

"""
first = input("enter firstname:")

last = input("enter lastname:")

name = [first, last]

name.reverse()

print(name)