# Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers

List = [-2, -4, -6, 3, 5, 3, -6, 5, -2, 6]
total = []
new = []
for i in range(len(List)):
    for j in range(len(List)):
        for k in range(len(List)):
            if i != j:
                if i != k:
                    if List[i] + List[j] + List[k] == 0:
                        new = [List[i], List[j], List[k]]
                        total.append(new)


for i in range(len(total)):
    for j in range(len(total)):
        if i == j:
            total.pop(j)

print(new)
print(total)