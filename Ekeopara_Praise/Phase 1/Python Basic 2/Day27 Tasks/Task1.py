'''1. Write a Python program to find the name of the oldest student from a given dictionary containing the names and ages of a group of students.
Sample Output:
Nidia Dominique
Becki Saunder'''

def oldest_of_students(student_data):
    oldest_student = max(student_data, key=student_data.get)
    return oldest_student
print(oldest_of_students({'Ebenezer': 23, 'Donald': 16, 'Peace': 25}))
print(oldest_of_students({'Michael': 23, 'Praise': 30, 'Christian': 20}))
print(oldest_of_students({'Cyril': 20, 'Julia': 30, 'Kimberly': 20}))