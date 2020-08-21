def hist(items):
    for item in items:
        result = ''
        times = item
        while(times >0):
            result += '#'
            times -= 1
            print(result)

hist([1,2,3,4])