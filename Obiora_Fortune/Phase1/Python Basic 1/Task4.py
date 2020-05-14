'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
    Sample Output :
        r = 1.1
        Area = 3.8013271108436504
    Tools: input function
'''

#4
print('Input the radius')
i = input()
r = i
p = 3.142
Area = int(p) * float(r)**2
print(Area)