# program to count the number of equal numbers from three given integers.
def test_three_equal(x, y, z):
  result= set([x, y, z])
  if len(result)==3:
    return 0
  else:
    return (4 - len(result))

print(test_three_equal(1, 1, 1))
print(test_three_equal(1, 2, 2))
print(test_three_equal(-1, -2, -3))
print(test_three_equal(-1, -1, -1))