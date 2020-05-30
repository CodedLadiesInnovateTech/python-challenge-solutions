#function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False
print(distinct([1,5,7,9]))
print(distinct([2,4,5,5,7,9]))