def HCF (x,y):
    if x > y:
        d=[]
        for i in range(1,y+1):
            if y % i == 0 and x % i == 0:
                d.append(i)
        print(d[-1])
    elif x < y:
        d=[]
        for i in range(1,x+1):
            if y % i == 0 and x % i == 0:
                d.append(i)
        print(d[-1])

print(HCF(10,8))