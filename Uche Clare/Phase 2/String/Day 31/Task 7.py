#Write a Python program to remove existing indentation from all of the lines in a given text. 
import textwrap

text = """Rather than attempting to seek out Python 3-specific recipes, the topics of this book are
merely inspired by existing code and techniques. Using these ideas as a springboard,
the writing is an original work that has been deliberately written with the most modern
Python programming techniques possible. """

print(textwrap.dedent(text))