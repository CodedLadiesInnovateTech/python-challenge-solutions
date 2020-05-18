"""
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
"""
filename = input("Enter the filename: ")
filext = filename.split(".")
print("Output:" + repr(filext[-1]))