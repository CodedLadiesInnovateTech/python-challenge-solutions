#program to insert an element before each element of a list.
color = ['Red', 'Green', 'Black']
print("Original List: ",color)
color = [v for elt in color for v in ('c', elt)]
print("Original List: ",color)