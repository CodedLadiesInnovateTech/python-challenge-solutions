""" 
Write a Python program to add two objects if both objects are an integer type.
"""
class Addition:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Addition(self.x+other.x, self.y+other.y)
first = Addition(5,7)
second = Addition(3,6)
result = first + second
print(result.x)
print(result.y)
