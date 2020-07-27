#program that accept a even number (>=4, Goldbach number) from the user and create a combinations that 
# express the given number as a sum of two prime numbers. Print the number of combinations.
import sys
from bisect import bisect_right
from itertools import chain, compress
print("Input an even number (0 to exit):") 
ub = 50000
is_prime = [0, 0, 1, 1] + [0]*(ub-3)
is_prime[5::6] = is_prime[7::6] = [1]*int(ub/6)
primes = [2, 3]
append = primes.append
 
for n in chain(range(5, ub, 6), range(7, ub, 6)):
    if is_prime[n]:
        append(n)
        is_prime[n*3::n*2] = [0]*((ub-n)//(n*2))
primes.sort()

for n in map(int, sys.stdin):
    if not n:
        break
    if n%2:
        print("Number of combinations:")  
        print(is_prime[n-2])
    else:
        print("Number of combinations:")  
        print(len([1 for p in primes[:bisect_right(primes, n/2)] if is_prime[n-p]]))