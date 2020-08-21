def gcd(x, y):
    factor = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            factor = k
            break
    return factor


print (gcd(48, 180))
