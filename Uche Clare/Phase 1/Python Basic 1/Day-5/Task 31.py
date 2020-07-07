#compute the greatest common divisor (GCD) of two positive integers.
def gcd(x, y):
    gcd=1
if x%y==0:
  print(y)
for i in range(int(y/2), 0, -1):
    if x%k ==0 and y%k==0:
         gcd = k 
         break
print(gcd)
print(gcd(27, 3))
print(gcd(144, 12))