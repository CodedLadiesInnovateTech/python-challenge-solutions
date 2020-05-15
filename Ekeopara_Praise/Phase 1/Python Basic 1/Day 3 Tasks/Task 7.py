'''7. Write a Python program to test whether a number is within 100 of 1000 or 2000.
    Tools: maths,input function'''

def test(val):
    return ((abs(1000 - val) <= 100) or (abs(2000 - val) <= 100))

print(test(2000)) 
print(test(27000)) 
print(test(100)) 
print(test(300))   