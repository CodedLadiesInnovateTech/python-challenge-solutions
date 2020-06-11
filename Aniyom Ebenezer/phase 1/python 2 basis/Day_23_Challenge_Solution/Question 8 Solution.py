"""
Write a Python program to count number of prime numbers less than a non-negative number.
"""
def count_primes_nums(n):
    ctr = 0

    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break

        else:
            ctr += 1
    return ctr
print(count_primes_nums(10))
print(count_primes_nums(100))