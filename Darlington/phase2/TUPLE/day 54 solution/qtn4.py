#program to count the elements in a list until an element is a tuple.
num = [10,20,30,(10,20),40]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1
print(ctr)