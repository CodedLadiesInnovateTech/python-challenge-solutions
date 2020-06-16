"""
Write a Python program to find the name of the oldest student from a given dictionary containing the names and ages of a group of students.
Sample Output:
Nidia Dominique
Becki Saunder
"""
def oldest_student(students):
	return max(students, key=students.get)

print(oldest_student({"Bernita Ahner": 27, "Kristie Marsico": 20, 
                      "Sara Pardee": 19, "Fallon Fabiano": 20, 
                      "Nidia Dominique": 23})) 
                      