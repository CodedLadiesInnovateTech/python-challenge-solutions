def LCM (a,b):
    if a > b:
        c = a*b
        d=[]
        for i in range(a,c+1):
            if i % b == 0 and i % a == 0:
                d.append(i)
        d.sort()
        return print(d[0])
    elif b > a:
        c = a * b
        d = []
        for i in range(b, c + 1):
            if i % b == 0 and i % a == 0:
                d.append(i)
        d.sort()
        return print(d[0])


print(LCM(81,27))