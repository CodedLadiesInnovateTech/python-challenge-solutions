count = 5
lst = list()
tpl = None

while count > 0:
    num = input("Enter a number: ")
    lst.append(num)
    tpl = tuple(lst)
    count -= 1
print("List: ", lst)
print("Tuple: ",tpl)