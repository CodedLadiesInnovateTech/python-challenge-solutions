'''5. Write a Python program to check whether a string is numeric.'''
def check_string(string):
    try:
        ans = int(string)
        check = 'Is Numeric'
    except:
        check = "Not Numeric"
    return check
print(check_string('123'))
print(check_string('abs'))
print(check_string('1a2b3'))




