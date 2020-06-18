'''7. Write a Python program to make a request to a web page, and test the status code, also display the html code of the specified web page.
Sample Output:
Web page status: <Response [200]>
HTML code of the above web page:
<!doctype html>
<html>
<head>
<title>Example Domain</title>
<meta charset="utf-8" />
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>
<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>'''

import requests
url = 'http://www.example.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh) Gecko/20100101 Firefox/38.0'}
request = requests.get(url, headers=headers)
print("Web page status: ", request)
print("\nHTML code of the above web page:")
if request.ok:
    print(request.text)

#Reference: w3resource 