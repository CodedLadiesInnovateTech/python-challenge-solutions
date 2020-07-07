# Python program to concatenate N strings

Num = int(input("Enter the number of strings: "))

def inputStr():
    str1 = input("Enter a string: ")
    return str1

output = ""

for i in range(Num):

    output +=inputStr() + " "
print(output)