#program to find the elements in a given set that are not in another set.
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Difference of sn1 and sn2 using difference():")
print(sn1.difference(sn2))
print("Difference of sn2 and sn1 using difference():")
print(sn2.difference(sn1))
print("Difference of sn1 and sn2 using - operator:")
print(sn1-sn2)
print("Difference of sn2 and sn1 using - operator:")
print(sn2-sn1)