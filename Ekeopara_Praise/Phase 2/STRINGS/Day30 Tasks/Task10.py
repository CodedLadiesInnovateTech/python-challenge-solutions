'''10. Write a Python function to reverses a string if it's length is a multiple of 4. '''

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))

#Reference: w3resource