#program to access only unique key value of a Python object.
import json
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(python_obj)
json_obj = json.loads(python_obj)
print("\nUnique Key in a JSON object:")
print(json_obj) 