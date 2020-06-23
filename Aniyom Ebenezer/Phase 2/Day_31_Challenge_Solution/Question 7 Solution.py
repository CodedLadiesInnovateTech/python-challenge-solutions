"""
 Write a Python program to remove existing indentation from all of the lines in a given text.
"""
import textwrap
text = """
    This site uses cookies to deliver oue services and to show you relevant ads.
    By using our site, you acknowledge that you have understood our privacy policy 
    """
text_without_Indentation = textwrap.dedent(text)
print()
print(text_without_Indentation)