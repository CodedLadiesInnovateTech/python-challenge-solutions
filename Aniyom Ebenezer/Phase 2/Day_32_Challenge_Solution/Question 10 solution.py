"""
Write a Python program to reverse words in a string.
"""
str1 = "This pandemic is something serious, in the sense that a virus can spread while lockdown is on. Let's re_examine this virus please."
for word in str1.split("\n"):
    print(" ".join(word.split()[::-1]))