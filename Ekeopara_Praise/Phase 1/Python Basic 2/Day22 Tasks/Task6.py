'''6. Write a Python program to sum of all numerical values (positive integers) embedded in a sentence.
Write a Python program to create maximum number of regions obtained by drawing n given straight lines.
Input:
Sentences with positive integers are given over multiple lines. Each line is a character string containing one-byte alphanumeric characters, symbols, spaces, or an empty line. However the input is 80 characters or less per line and the sum is 10,000 or less.
Input some text and numeric values ( to exit):
Sum of the numeric values: 80
None
Input some text and numeric values ( to exit):
Sum of the numeric values: 17
None
Input some text and numeric values ( to exit):
Sum of the numeric values: 10
None'''

import sys,re
def test(stri):
  print("Input some text and numeric values (<ctrl-d> to exit):")
  print("Sum of the numeric values: ",sum([sum(map(int,re.findall(r"[0-9]{1,5}",stri)))]))

print(test("sd1fdsfs23 dssd56"))
print(test("15apple2banana"))
print(test("flowers5fruit5"))

#Reference: w3resource