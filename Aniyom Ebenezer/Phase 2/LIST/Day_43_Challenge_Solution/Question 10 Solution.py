"""
Write a Python program to sort a list of nested dictionaries.
"""
list1 = [{'key': {'subkey': 1}}, {'key': {'subkey':10}}, {'key': {'subkey':5}}]
print("Original list: ")
print(list1)
list1.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted List: ")
print(list1)