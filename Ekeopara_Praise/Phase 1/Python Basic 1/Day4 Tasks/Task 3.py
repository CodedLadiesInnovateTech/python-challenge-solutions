
def check(strng, n):
    num = 2
    if num > len(strng):
        num = len(strng)
    ans = strng[:num] 
    
    val = ""
    for n in range(n):
        val = val + ans
    return ans

print(check('Praise', 2))
print(check('p', 3))