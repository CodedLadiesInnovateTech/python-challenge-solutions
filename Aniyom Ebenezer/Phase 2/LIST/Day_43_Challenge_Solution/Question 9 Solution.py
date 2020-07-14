"""
Write a Python program to convert list to list dictionaries.
"""
color_name = ["Black", "Red", "Maroon"]
color_code = ["#000000", "FF0000", "#800000"]
print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])