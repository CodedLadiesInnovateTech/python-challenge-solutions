"""
Write a Python program to convert a string to a list.
"""
import ast
color = "['red', 'green', 'white']"
print(ast.literal_eval(color))