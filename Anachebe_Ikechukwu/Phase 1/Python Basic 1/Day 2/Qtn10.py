"""

10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
        Sample value of n is 5
        Expected Result : 615
    Tools: input function, maths
"""

n = int(input("Enter an integer:"))

sum = n + n**2 + n**3

print("The sum is", sum)