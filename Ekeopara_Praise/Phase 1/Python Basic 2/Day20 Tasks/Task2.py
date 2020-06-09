'''2. Write a python program to find heights of the top three building in descending order from eight given buildings.
Input:
0 = height of building (integer) = 10,000
Input the heights of eight buildings:
25
35
15
16
30
45
37
39
Heights of the top three buildings:
45
39
37'''
print("Input the heights of eight buildings:")
l = [int(input()) for i in range(8)]
print("Heights of the top three buildings:")
l = sorted(l)
print(*l[:4:-1], sep='\n')


