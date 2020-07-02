"""
Write a Python program to convert Python objects into JSON strings. Print all the values.
"""
import json
python_dict = {"name":"David", "Age": 6, "class": "I"}
python_list = ["Red", "Green", "Black"]
python_str = "Python json"
Python_int = (1234)
python_float = (21.34)
python_T = (True)
python_F = (False)
python_N = (None)

j_dict = json.dumps(python_dict)
j_list = json.dumps(python_list)
j_str = json.dumps(python_str)
j_int = json.dumps(Python_int)
j_float = json.dumps(python_float)
j_T = json.dumps(python_T)
j_F = json.dumps(python_F)
j_N = json.dumps(python_N)

print("json dict :", j_dict)
print("json list: ", j_list)
print("json str : ", j_str)
print("json int: ", j_int)
print("json float: ", j_float)
print("json Boolean(True) : ", j_T)
print("json Boolean(Fasle): ", j_F)
print("json None: ", j_N)