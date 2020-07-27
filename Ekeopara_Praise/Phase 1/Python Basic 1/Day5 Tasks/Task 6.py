'''6. Write a Python program to add two objects if both objects are an integer type.'''


def Add(val1, val2):
    try:
        ans = val1 + val2
        return ans
    except:
        return "They are of different data types"

print(Add(2, "b"))
print(Add(2, 4))

