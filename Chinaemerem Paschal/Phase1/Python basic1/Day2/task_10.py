#program showing computation of integer value n in n+nn+nnn
n1 = int(input("ENTER AN INTEGER NUMBER: "))
n2 = n1*11
n3 = n1*111
n = n1+n2+n3
print("The value of n + nn + nnn is: ",n)