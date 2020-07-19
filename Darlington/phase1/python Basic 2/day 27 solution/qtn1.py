# program to find the name of the oldest student from a given dictionary 
# containing the names and ages of a group of students.
def oldest_student(students):
	return max(students, key=students.get)

print(oldest_student({"Bernita Ahner": 12, "Kristie Marsico": 11, 
                      "Sara Pardee": 14, "Fallon Fabiano": 11, 
                      "Nidia Dominique": 15})) 
print(oldest_student({"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, 
                      "Sofia Park": 12.4, "Joannie Archibald": 12.6, 
                      "Becki Saunder": 12.7})) 