# program which reads the two adjoined sides and
#  the diagonal of a parallelogram and check whether the parallelogram is a rectangle or a rhombus.
print("Input two adjoined sides and the diagonal of a parallelogram (comma separated):")
a,b,c = map(int, input().split(","))
if c**2 == a**2+b**2 :
    print("This is a rectangle.")
if a == b:
    print("This is a rhombus.")