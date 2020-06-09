"""
Write a Python program to reverse the digits of a given number and add it to the original, if the sum
is not a palindrome repeat this process.
"""
def rev_number(n):
    s = 0
    while True:
        k = str(n)
        if k == k[::-1]:
            break
        else:
            m = int(k[::-1])
            n += m
            s += 1
    return n
print(rev_number(1234))