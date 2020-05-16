"""

7. Write a Python program to accept a filename from the user and print the extension of that.
        Sample filename : abc.java
        Output : java
    Tools: input function, slicing
    """

filename = input("enter filename:")

filename = filename.split('.')

print("Filename extension is ", repr(filename[-1]))