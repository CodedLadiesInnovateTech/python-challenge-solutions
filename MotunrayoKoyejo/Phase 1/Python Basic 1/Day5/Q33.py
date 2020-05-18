def sum (a,b,c):
    if a==b or b==c or a==c:
        return 0
    return a+b+c

print(sum(2,3,4))
print(sum(2,3,3))