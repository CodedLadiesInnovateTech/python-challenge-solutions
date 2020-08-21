'''
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
        exam_st_date = (11, 12, 2014)
        Sample Output : The examination will start from : 11 / 12 / 2014
    Tools:slicing,indexing
'''

#9
exam_st_date = (11, 12, 2014)
x = exam_st_date[0]
y = exam_st_date[1]
z = exam_st_date[2]
a = (x,y,z,)
print('The examination will start from : %s / %s / %s' %(a) )