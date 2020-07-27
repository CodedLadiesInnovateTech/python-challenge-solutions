'''8. Write a Python program to swap comma and dot in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23" '''

amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)