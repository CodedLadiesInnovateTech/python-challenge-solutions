# Write a Python program to check the priority of the four operators (+, -, *, /)
__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}
operator1 = '+'
operator2 = '*'

Check = __priority__[operator1] >= __priority__[operator2]

print(Check)
