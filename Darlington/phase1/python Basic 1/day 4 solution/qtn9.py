#program to print out colors
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
for n in color_list_1:
    print(n)
for x in color_list_2:
    print(x)    
print(color_list_1.difference(color_list_2))