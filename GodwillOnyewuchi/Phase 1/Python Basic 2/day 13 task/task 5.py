# Python program to compute the product of a list of integers (without using for loop)

List = [21, 34, 56, 78, 45, 89]

Output = 1
i = 0
print(len(List))
while i < len(List):
    Output *= List[i]
    i += 1

print(f'Product of integers in {List} is {Output}')
