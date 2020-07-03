"""
Write a Python function to insert a string in the middle of a string. 
Sample function and result :
insert_string_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_string_middle('{{}}', 'PHP') -> {{PHP}}
"""
def insert_string_middle(str, word):
    return str[:2] + word + str[2:]
print(insert_string_middle("[[]]", "Python"))
print(insert_string_middle("{[]}", "PHP"))