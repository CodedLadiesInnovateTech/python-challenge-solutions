'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
        Sample value of n is 5
        Expected Result : 615
    Tools: input function, maths
'''

#10
print('Input th integer:')
n = int(input())
ans = n + n*n + n*n*n
print(ans)