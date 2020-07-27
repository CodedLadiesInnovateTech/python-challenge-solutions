'''3. Write a Python program which adds up columns and rows of given table as shown in the specified figure.
Input number of rows/columns (0 to exit)
4
Input cell value:
25 69 51 26
68 35 29 54
54 57 45 63
61 68 47 59
Result:
25 69 51 26 171
68 35 29 54 186
54 57 45 63 219
61 68 47 59 235
208 229 172 202 811
Input number of rows/columns (0 to exit)'''

while True:
    print("Input number of rows/columns (0 to exit)")
    n = int(input())
    if n == 0:
        break
    print("Input cell value:")
    x = []
    for i in range(n):
        x.append([int(num) for num in input().split()])

    for i in range(n):
        sum = 0
        for j in range(n):
            sum += x[i][j]
        x[i].append(sum)

    x.append([])
    for i in range(n + 1):
        sum = 0
        for j in range(n):
            sum += x[j][i]
        x[n].append(sum)
    print("Result:")
    for i in range(n + 1):
        for j in range(n + 1):
            print('{0:>5}'.format(x[i][j]), end="")
        print()

#Reference: w3resource