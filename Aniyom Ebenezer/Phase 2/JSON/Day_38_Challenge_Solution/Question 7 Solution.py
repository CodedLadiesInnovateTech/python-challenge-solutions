"""
Write a Python program to check whether an instance is complex or not.
"""
import json

def encode_complex(object):
    if isinstance(object, complex):
        return [object.real, object.imag]
    raise TypeError(repr(object) + " is not JSON serialized")

complex_obj = json.dumps(2 + 3j, default=encode_complex)
print(complex_obj) 