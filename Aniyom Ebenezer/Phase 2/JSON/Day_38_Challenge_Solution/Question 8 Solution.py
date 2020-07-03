"""
Write a Python program to check whether a JSON string contains complex object or not.
"""
import json
def is_complex_num(object):
    if '__complex__' in object:
        return complex(object['real'], object['img'])
    return object
complex_object = json.loads('{"__complex__": true, "real" : 4, "img" : 5}', object_hook=is_complex_num)
simple_object = json.loads('{"real" : 4, "img" : 3}', object_hook = is_complex_num)
print("Complex Object: ", complex_object)
print("Without complex object: ", simple_object)