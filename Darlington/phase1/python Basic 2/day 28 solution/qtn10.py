#program to calculate Euclid's totient function of a given integer.
#  Use a primitive method to calculate Euclid's totient function.
def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)
print(phi_func(10))
print(phi_func(15))
print(phi_func(33))