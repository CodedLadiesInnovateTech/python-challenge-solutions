#Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values.
def string_both_ends(str):
    if len(str) < 2:
        return ''

    return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))