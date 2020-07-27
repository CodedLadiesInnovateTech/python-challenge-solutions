#Write a Python program to set the indentation of the first line. 
import textwrap
text = """Rather than attempting to seek out Python 3-specific recipes, the topics of this book are
merely inspired by existing code and techniques. Using these ideas as a springboard,
the writing is an original work that has been deliberately written with the most modern
Python programming techniques possible. """
text1 = textwrap.dedent(text).strip()
indent_text= textwrap.fill(text1, initial_indent= " " * 3, subsequent_indent= "", width=100)
print(indent_text)