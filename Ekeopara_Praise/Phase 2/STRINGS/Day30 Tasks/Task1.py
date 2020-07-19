'''1. Write a Python program to remove the characters which have odd index values of a given string. '''

def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))

#Reference: w3resource