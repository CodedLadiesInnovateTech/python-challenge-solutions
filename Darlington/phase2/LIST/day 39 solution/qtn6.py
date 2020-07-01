#program to get a list, sorted in increasing order by the 
#last element in each tuple from a given list of non-empty tuples.
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))