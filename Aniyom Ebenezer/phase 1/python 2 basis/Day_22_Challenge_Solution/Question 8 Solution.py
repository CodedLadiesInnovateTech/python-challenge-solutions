"""
When character are consecutive in a string , it is possible to shorten the character string by replacing the character with a certain rule. For example, in the case of the character string YYYYY, if it is expressed as # 5 Y, it is compressed by one character.

Write a Python program to restore the original string by entering the compressed string with this rule. However, the # character does not appear in the restored character string.

Note: The original sentences are uppercase letters, lowercase letters, numbers, symbols, less than 100 letters, and consecutive letters are not more than 9 letters.

Input:
Multiple character strings are given. One string is given per line.
Output:
The restored character string for each character on one line.
"""
def restore_original_str(a1):
  result = ""
  ind = 0
  end = len(a1)
  while ind < end:
    if a1[ind] == "#":
      result += a1[ind + 2] * int(a1[ind + 1])
      ind += 3
    else:
      result += a1[ind]
      ind += 1
  return result
print("Original text:","XY#6Z1#4023")
print(restore_original_str("XY#6Z1#4023"))
print("Original text:","#39+1=1#30")
print(restore_original_str("#39+1=1#30"))
