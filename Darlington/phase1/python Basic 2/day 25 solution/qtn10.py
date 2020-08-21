#program to replace all but the last five characters of a given string into "*" 
# and returns the new masked string.
def mask_string(str1):
  return '*'*(len(str1)-5) + str1[-5:]

print(mask_string("kdi39323swe"))
print(mask_string("12345abcdef"))
print(mask_string("12345")) 