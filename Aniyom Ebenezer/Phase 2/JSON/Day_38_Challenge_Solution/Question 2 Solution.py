"""
Write a Python program to convert Python object to JSON data.
"""
import json
python_obj = {
    "name" : "David",
    "class" : "I",
    "age" : 6
}
print(type(python_obj))
j_data = json.dumps(python_obj)
print(j_data)