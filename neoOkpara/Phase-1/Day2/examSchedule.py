exam_st_date = (11, 12, 2014)
listDate = list(exam_st_date)
# print(listDate)
stringDate = str(listDate).replace(',', ' /').replace('[', '').replace(']', '')
# print(stringDate)

sampleOutput = "The examination will start from : " + stringDate
print(sampleOutput)
