'''2. Write a Python program to wrap a given string into a paragraph of given width.
    Sample Output:
    Input a string: The quick brown fox.
    Input the width of the paragraph: 10
    Result:
    The quick
    brown fox.'''

import textwrap
s = input("Input a string: ")
w = int(input("Input the width of the paragraph: ").strip())
print("Result:")
print(textwrap.fill(s,w))

#Reference: w3resource