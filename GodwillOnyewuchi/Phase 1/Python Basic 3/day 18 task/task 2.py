# Write a Python program to create all possible permutations from a given collection of distinct numbers

Number = [1, 2, 3]
result = [[]]
for n in Number:
    permute = []
    for perm in result:
        for i in range(len(perm)+1):
            permute.append(perm[:i] + [n] + perm[i:])
        result = permute

print(result)
