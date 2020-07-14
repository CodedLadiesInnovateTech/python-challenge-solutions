"""
Write a Python program to generate the combinations of n distinct objects taken from the elements of a given lisy.
"""
def combination(n, n_list):
    if n<=0:
        yield []
        return
    for i in range(len(n_list)):
        c_num = n_list[i:i+1]
        for a_num in combination (n-1, n_list[i+1:]):
            yield c_num + a_num
n_list = [1, 2, 3, 4, 7, 8, 4, 9, 0]
print("Original List: \n{}".format(n_list))
print()
n = 3
result = combination(n, n_list)
print("\nCombinations of", n, "distinct objects:")
for e in result:
    print(e)