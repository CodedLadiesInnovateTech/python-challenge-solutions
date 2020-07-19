#Write a Python program to compute sum of digits of a given string.
string = "2468Uche"
add_digit = 0
for i in string:
    if i.isdigit() == True:
        x = int(i)
        add_digit += x
print(add_digit)
