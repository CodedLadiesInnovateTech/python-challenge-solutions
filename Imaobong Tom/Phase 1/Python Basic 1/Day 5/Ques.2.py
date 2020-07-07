def lowest_multiple(a,b):
    factors = []
    c = a * b
    if a > b:
        for i in range(a, c+1):
            if i % b == 0 or i % a == 0:
                factors.append(i)
        return print(f"The lowest common multiple of {a} and {b} is", factors[0])
    if b > a:
        for i in range (b, c+1):
            if  i % b == 0 and i % a == 0:
                factors.append(i)
        return print(f"The lowest common multiple of {a} and {b} is", factors[0])


lowest_multiple(6,22)


