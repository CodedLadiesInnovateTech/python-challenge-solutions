'''10. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
    Tools: input function, slicing'''

word = str(input("Type in any string or word: "))
n = int(input("Enter the number of repititions: "))
ans = ""

for i in range(n):
    ans = ans + word
print(ans)
    

