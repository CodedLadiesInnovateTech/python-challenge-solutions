'''5. Write a Python program that will return true if the two 
given integer values are equal or their sum or difference is 5.'''


def checker(n1, n2):
    if n1 == n2:
        return "True"
    elif n1+n2== 5:
        return "True"
    elif n1-n2==5:
        return "True"
    else:
        return "False"

print(checker(2, 2))
print(checker(2, 3))
print(checker(8, 3))
