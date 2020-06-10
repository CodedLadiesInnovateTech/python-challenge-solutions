"""
Write a Python program that accepts six numbers as input and sort them in descending order.
"""
list1 = list(map(int, input("Input six digits(followed by a space after each number): ").split()))
list1.sort()
list1.reverse()
print(list1)