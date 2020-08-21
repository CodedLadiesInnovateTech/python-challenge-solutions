#program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
name= str(input('Enter name:'))
copies=(int(input('Enter number=')))
n=name[0:2]
if len(n)>=2:
 print(n*copies)
else:
    print(name*copies)