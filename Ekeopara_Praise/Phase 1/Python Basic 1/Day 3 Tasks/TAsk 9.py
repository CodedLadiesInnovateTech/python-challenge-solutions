'''9. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
    Tools: input function, string formating'''

def Add_is(strng):
    if len(strng) >= 2 and strng[:2] == "Is":
        return strng
    return "Is" + strng

print(Add_is("Isme"))
print(Add_is("me"))

