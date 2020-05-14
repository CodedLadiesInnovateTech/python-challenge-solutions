#1
print('Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, \n Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"')

2
import sys
print(sys.version)

3
import datetime
x = datetime.datetime.now()
print('Current date and time is: ', x)

4
print('Input the radius')
i = input()
r = i
p = 3.142
Area = int(p) * float(r)**2
print(Area)

#5
print('Enter First Name: ')
First_name = input()
print('Enter Last  Name:')
Last_name = input()
list = [First_name, Last_name]
print(list)
First_name,Last_name = Last_name,First_name
x = [First_name, Last_name]
print(x)
new_list = list.reverse()
print(new_list)

#6
nums = input('Enter your comma-separated numbers: ')
lst = list(nums.split(sep= ','))
tpl = tuple(lst)
print('List: ', lst)
print('Tuple: ', tpl)

#7
file_name = str(input('Enter the filename: '))
file_extn = file_name.split('.')
print('The file extension is: ' + repr(file_extn[-1]))

#8
color_list = ["Red", "Green", "White", "Black"]
x = [color_list[0], color_list[-1]]
print(x)

#9
exam_st_date = (11, 12, 2014)
x = exam_st_date[0]
y = exam_st_date[1]
z = exam_st_date[2]
a = (x,y,z,)
print('The examination will start from : %s / %s / %s' %(a) )

#10
print('Input th integer:')
n = int(input())
ans = n + n*n + n*n*n
print(ans)