"""
Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
    Tools: input function, string formating
    """
string = str(input("Enter a word "))
new_string = "Is" + string
if string[0:2] == "Is":
    print(string)
else:
    print(new_string)
