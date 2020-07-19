# program to test whether a given number is symmetrical or not.
def is_symmetrical_num(n):
  return str(n) == str(n)[::-1]
print(is_symmetrical_num(121))
print(is_symmetrical_num(0))
print(is_symmetrical_num(122))
print(is_symmetrical_num(990099))