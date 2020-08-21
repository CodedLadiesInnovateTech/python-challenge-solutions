'''1. Write a Python program to find the first non-repeating character in given string.'''
def firstNonRepeatingChar(str1):
   char_order = []
   counts = {}
   for c in str1:
      if c in counts:
         counts[c] += 1
      else:
         counts[c] = 1
         char_order.append(c)
   for c in char_order:
      if counts[c] == 1:
          return c
   return None

print(firstNonRepeatingChar('PythonforallPythonMustforall'))
print(firstNonRepeatingChar('Justtocheckout'))
print(firstNonRepeatingChar('AABBCC'))