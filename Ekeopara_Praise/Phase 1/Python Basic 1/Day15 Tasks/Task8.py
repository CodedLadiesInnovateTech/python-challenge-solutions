'''8. Write a Python program to convert true to 1 and false to 0.'''
def conv_1or2(value):
    if value == "True":
        ans = 1
    elif value =="False":
        ans = 0
    else:
        ans = "Please enter either True or False !!"
    return ans
print(conv_1or2("True"))
print(conv_1or2("False"))

