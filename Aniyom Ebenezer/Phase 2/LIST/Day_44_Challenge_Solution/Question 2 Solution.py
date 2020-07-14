"""
Write a Python to compute the difference between two lists.
"""
from collections import Counter
color1 = ['Red', 'Orange', 'Green', 'Blue', 'White']
color2 = ['Black', 'Yellow', 'Blue', 'Green']
counter1 = Counter(color1)
counter2 = Counter(color2)
print("Color1-Color2: ", list(counter1 - counter2))
print("Color2-COlor1: ", list(counter2 - counter1))