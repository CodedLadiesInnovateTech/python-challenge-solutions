'''2. Write a Python program to compute the similarity between two lists. 
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow'] '''

def find_similiarity(list1, list2):
    list3 = list(set(list1) - set(list2))
    list4 = list(set(list2) - set(list1))
    return list3, list4
print(find_similiarity(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]))