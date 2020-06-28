"""
Write a Python program to display formatted text (width=50) as output.
"""
import textwrap
text = """
    This site uses cookies to deliver oue services and to show you relevant ads.
    By using our site, you acknowledge that you have understood our privacy policy 
    """
print()
print(textwrap.fill(text, width=50))