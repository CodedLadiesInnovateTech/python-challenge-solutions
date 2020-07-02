"""
Write a Python program to convert JSON data to Python object.
"""
import json
json_obj = '{"Name" : "David", "class": "I", "Age" : 6}'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ", python_obj["Name"])
print("Class: ", python_obj["class"])