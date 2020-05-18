def lcm(a,b):
    if a > b:
        c =a
    else:
        c = b
    while(True):
        if ((c%a ==0) and (c%b==0)):
            lcm = c
            break
        c+=1

    return lcm

print(lcm(2,4))