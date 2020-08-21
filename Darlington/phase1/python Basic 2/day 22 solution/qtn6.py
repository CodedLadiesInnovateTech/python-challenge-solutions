#program to sum of all numerical values (positive integers) embedded in a sentence.
import sys,re
def test(stri):
  print("Input some text and numeric values (<ctrl-d> to exit):")
  print("Sum of the numeric values: ",sum([sum(map(int,re.findall(r"[0-9]{1,5}",stri)))]))

print(test("sd1fdsfs23 dssd56"))
print(test("15apple2banana"))
print(test("flowers5fruit5"))