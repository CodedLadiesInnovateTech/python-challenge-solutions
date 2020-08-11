#program to remove the intersection of a 2nd set from the 1st set.
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Remove the intersection of a 2nd set from the 1st set using difference_update():")
print(sn1.difference(sn2))
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(sn1-sn2)
