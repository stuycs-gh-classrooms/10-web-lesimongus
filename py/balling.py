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

roll = randint(1, 20)
print(roll)

data = cgi.FieldStorage()
name = 'you nameless loser'
gender = 'This does matter'
identity = "You didn't, actually"
if ('name' in data):
    name = data['name'].value
if ('gender' in data):
    gender = data['gender'].value
if ('identity' in data):
    identity = data['identity'].value

html= HTML_HEADER
html+= '<h1>Awaken, ' + name + '</h1>'
html+= HTML_FOOTER
print(html)