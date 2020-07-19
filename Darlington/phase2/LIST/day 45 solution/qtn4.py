#program to iterate over two lists simultaneously.
num = [1, 2, 3]
color = ['red', 'white', 'black']
for (b,a) in zip(num, color):
     print(b, a)