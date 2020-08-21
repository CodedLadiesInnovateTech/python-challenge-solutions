#Write a Python program to display formatted text (width=50) as output. 
import textwrap

text = """
        Rather than attempting to seek out Python 3-specific recipes, the topics of this book are
merely inspired by existing code and techniques. Using these ideas as a springboard,
the writing is an original work that has been deliberately written with the most modern
Python programming techniques possible. """

print(textwrap.fill(text, width=50))