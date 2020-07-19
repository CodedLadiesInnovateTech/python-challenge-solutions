"""
Write a Python program to set the indentation of the first line.
"""
import textwrap
text = """
    This site uses cookies to deliver oue services and to show you relevant ads.
    By using our site, you acknowledge that you have understood our privacy policy 
    """
text1 = textwrap.dedent(text).strip()
print()

print(textwrap.fill(text1,
                    initial_indent=' '*2,
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))

#reference: w3resource.com