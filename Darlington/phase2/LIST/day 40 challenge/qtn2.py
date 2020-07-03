#def two_data(list1, list2):
 #    result = False
  #      for x in list2:
   #          if i == x:
    #             result = True
       #          return result
#print(two_data([3,4,5,6,2,3,4], [3,4, 6,7,8,9]))
#print(two_data([3,4,5,3,2,6,7], [8,9,0,1]))   
       
# Python program to print a specified list after removing the 0th, 4th and 5th elements. 
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
    
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

