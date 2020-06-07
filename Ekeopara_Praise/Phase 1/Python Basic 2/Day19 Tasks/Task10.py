'''10. Write a Python program to reverse the digits of a given number and add it to the original,
If the sum is not a palindrome repeat this procedure.
Note: A palindrome is a word, number, or other sequence of characters which reads the same 
backward as forward, such as madam or racecar.'''

def reverseInteger(x):
    sign = -1 if x < 0 else 1
    x * sign 

    while x:
        if x % 10 == 0:
            x /= 10
        else:
            break

    x = str(x)
    lst =list(x)
    lst.reverse()
    x = "".join(lst)
    x = int(x)

    return sign*x
print(reverseInteger(234))
print(reverseInteger(894))