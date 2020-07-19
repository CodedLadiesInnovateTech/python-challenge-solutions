# program to restore the original string by entering the compressed string with this rule. However,
#  the # character does not appear in the restored character string.
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