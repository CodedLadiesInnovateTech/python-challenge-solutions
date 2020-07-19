#program to find least common multiple
def lcm(p, q):
   if p > q:
       t = p
   else:
       t = q

   while(True):
       if((t % p == 0) and (t % q == 0)):
           lcm = t
           break
       t += 1

   return lcm
print(lcm(20, 15))
print(lcm(42, 38))