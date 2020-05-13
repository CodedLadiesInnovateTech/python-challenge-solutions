exam_st_date = (11, 12, 2014)
woo = exam_st_date.__str__()
lst = list()
lst2 = list()

for l in exam_st_date:
    lst.append(l)
    
wors = [str(do) for do in lst]
word = " / ".join(wors)
print("The examination will start from : ", word)

