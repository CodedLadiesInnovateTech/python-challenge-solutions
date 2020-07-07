# Python program to check whether a string is numeric.
string = "Cla73829re"
count = 0
string2 = ''
for i in string:
    if (i.isnumeric()) == True:
        count +=1
    else:
        string2 +=i
print(string2)
print(count)