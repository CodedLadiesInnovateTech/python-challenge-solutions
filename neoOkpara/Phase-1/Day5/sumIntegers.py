def sum_integers(a, b, c):
    if (a == b) or (b == c) or (a == c):
        return 0
    return a + b + c


print (sum_integers(23, 46, 23))
print (sum_integers(23, 46, 25))