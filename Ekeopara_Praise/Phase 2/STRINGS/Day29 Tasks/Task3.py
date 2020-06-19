'''3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.
    Sample String : 'codedladies'
    Expected Result : 'coes'
    Sample String : 'co'
    Expected Result : 'coco'
    Sample String : ' c'
    Expected Result : Empty String
    Click me to see the sample solution'''

def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

#Reference: w3resource