string = input("Enter a word:")
string = string.lower()
if string[0:2] == "is":
    new_string = string
else:
    new_string = "is" + string
print("new string = ", new_string)