#!usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()

import cgi

from random import randint

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Can you really call this an rpg i didn't receive a sword on my birthday or anythi</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""

data = cgi.FieldStorage()
name = 'you nameless loser'
if ('name' in data):
    name = data['name'].value

html= HTML_HEADER
html+= '<h1>Awaken, ' + name + '</h1>'
html+= '<br><a href="TitlePending.html">Try Again</a>'
html+= HTML_FOOTER
print(html)
