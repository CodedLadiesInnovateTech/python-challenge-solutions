"""10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
        Sample value of n is 5
        Expected Result : 615
    Tools: input function, maths"""

n = str(input("Eneter the number: "))
n = (n)
nn = (n + n)
nnn = (n + n + n)
ans = int(n) + int(nn) + int(nnn)
print(ans) 
