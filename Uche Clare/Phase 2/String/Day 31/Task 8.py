#Write a Python program to add a prefix text to all of the lines in a string. 
import textwrap
text = """Rather than attempting to seek out Python 3-specific recipes, the topics of this book are
merely inspired by existing code and techniques. Using these ideas as a springboard,
the writing is an original work that has been deliberately written with the most modern
Python programming techniques possible. """

text1 = textwrap.dedent(text)
prefix_text= textwrap.fill(text1, width=62)
prefix_text1 = textwrap.indent(prefix_text, "~")
print(prefix_text1)