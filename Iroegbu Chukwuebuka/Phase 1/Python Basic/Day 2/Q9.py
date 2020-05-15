"""Python program to display the examination schedule. (extract the date from exam_st_date)"""
exam_st_date = (11, 12, 2014)
new_exam = str(exam_st_date[0])+' / '+str(exam_st_date[1])+' / '+str(exam_st_date[2])
print('The examination will start from : ' + new_exam)