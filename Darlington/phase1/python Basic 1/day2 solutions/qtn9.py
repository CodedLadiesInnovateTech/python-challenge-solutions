#exams start date
exam_st_date = (11, 12, 2014)
examDate = str(exam_st_date).replace("(", "").replace(")", "").replace(",", "/")

print(f'The examination will start from : {examDate}')