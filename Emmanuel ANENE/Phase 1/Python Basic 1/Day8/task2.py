'''
Write a Python program to convert all units of time into seconds.
'''
try:
    varY = int(input("How many year(s)? "))
    varM = int(input("How many month(s)? "))
    varW = int(input("How many week(s)? "))
    varD = int(input("How many day(s)? "))
    varH = int(input("How many hour(s)? "))
    varm = int(input("How many minute(s)? "))
    if varY:
        totalY = varY * 31536000
        print("The number of seconds in {} year(s) is {}.".format(varY, totalY))
    elif varM:
        totalM = varM * 2628002.88
        print("The number of seconds in {} month(s) is {}.".format(varM, totalM))
    elif varW:
        totalW = varW * 604800
        print("The number of seconds in {} week(s) is {}.".format(varW, totalW))
    elif varD:
        totalD = varD * 86400
        print("The number of seconds in {} day(s) is {}.".format(varD, totalD))
    elif varH:
        totalH = varH * 3600
        print("The number of seconds in {} hour(s) is {}.".format(varH, totalH))
    elif varm:
        totalm = varm * 60
        print("The number of seconds in {} minute(s) is {}.".format(varm, totalm))
except:
    print("You just entered a wrong input.")





