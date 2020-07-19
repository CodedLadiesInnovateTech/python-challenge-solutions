import time
def sum(n):
    start = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end= time.time()
    return s, end-start
print('Execution Time is: ')
print(sum(15))