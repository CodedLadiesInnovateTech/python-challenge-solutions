#program to check whether a specific value is specified
def is_specified(data, n):
    for value in data:
        if n == value:
            return True
    return False
print(is_specified([1, 5, 8, 3], 3))
print(is_specified([1, 5, 8, 3], -1))