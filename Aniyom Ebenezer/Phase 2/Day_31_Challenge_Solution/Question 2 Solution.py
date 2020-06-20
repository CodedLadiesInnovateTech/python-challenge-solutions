"""
.Write a Python program to sort a string lexicographically.
"""
def lexicographic_sort(str1):
    return sorted(sorted(str1), key=str.upper)
print(lexicographic_sort("quockbrown"))
print(lexicographic_sort("Codedladies"))