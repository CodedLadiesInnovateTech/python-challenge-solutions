''' Write a Python program to display the examination schedule. (extract the date from exam_st_date).
        exam_st_date = (11, 12, 2014)
        Sample Output : The examination will start from : 11 / 12 / 2014 '''

exam_st_date = (11, 12, 2014)
print(f"The examination will start from :  {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]} ")

print("The examination date will start from: \n", '%i/%i/%i' %exam_st_date)