"""
Write a Python function to create the HTML string with tags around the word(s). 
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""
print("Input a tag with its corresponding word separated by a space")
tag, word = map(str, input().split())
print("<{}>{}</{}>".format(tag,word,tag))