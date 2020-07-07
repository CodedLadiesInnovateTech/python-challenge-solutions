'''6. Write a Python program to compute the amount of the debt in n months. The borrowing amount is $100,000
and the loan adds 5% interest of the debt and rounds it to the nearest 1,000 above month by month.
Input:
An integer n (0 = n = 100)
Input number of months:
7 Amount of debt: $144000'''

def round_n(n):
    if n%1000:
        return (1+n//1000)*1000
    else:
        return n
     
def compute_debt(n):
    if n==0: return 100000
    return int(round_n(compute_debt(n-1)*1.05))

print("Input number of months:")
result = compute_debt(int(input()))
print("Amount of debt: ","$"+str(result).strip())

#Reference: w3reource