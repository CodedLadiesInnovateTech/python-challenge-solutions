#Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.
int1 = int(input('int1 = '))
int2 = int(input('int2 = '))
if int1>int2:
    if int1%int2==0:
        print('True')
    else:
        print('False')
elif int1<int2:
    if int2%int1==0:
        print('True')
    else:
        print('False')