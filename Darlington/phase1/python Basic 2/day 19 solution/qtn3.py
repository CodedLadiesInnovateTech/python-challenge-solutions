#program that accept a positive number and subtract from this number the sum of its digits and so on.
#  Continues this operation until the number is positive.
def repeat_times(n):
  s = 0
  n_str = str(n)
  while (n > 0):
    n -= sum([int(i) for i in list(n_str)])
    n_str = list(str(n))
    s += 1
  return s
print(repeat_times(9))
print(repeat_times(21))