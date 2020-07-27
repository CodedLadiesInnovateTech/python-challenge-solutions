# Write a Python program to find the value of n where n degrees of number 2 are written sequentially in a line without spaces

def degrees(num):
    ans = True
    n, tempn, i = 2, 2, 2
    while ans:
        if str(tempn) in num:
            i += 1
            tempn = pow(n, i)
        else:
            ans = False
    return i-1;


print(degrees("248132"))
print(degrees("243264"))