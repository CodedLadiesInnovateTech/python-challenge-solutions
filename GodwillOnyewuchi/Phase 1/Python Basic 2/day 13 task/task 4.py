# Python program to filter the positive numbers from a list

List = [12, 4, -4, 'him', 45, -23, 2, 40]

Output = []
for i in List:
    if type(i) == int and i + abs(i) != 0:
        Output.append(i)
        
print(Output)