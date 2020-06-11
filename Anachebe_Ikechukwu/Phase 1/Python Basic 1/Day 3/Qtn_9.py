#9. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
#    Tools: input function, string formating

str = input("Enter a string:")

if str.startswith("Is"):
    print(str)
else:
    print("Is",str)