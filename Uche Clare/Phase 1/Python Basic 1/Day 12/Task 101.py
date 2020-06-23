# Write a Python program to access and print a URL's content to the console.

import urllib.request
url = urllib.request.urlopen("http://www.youtube.com")
data = url.read()
print(data)
