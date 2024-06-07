#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()

import cgi

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
name = 'egg'
if ('name' in data):
    name = data['name'].value

def choices(options, subject, question):
    form = """
<form action="balling.py" method="GET">
"""
    form += question
    buttons = ''
    for stuff in options:
        choice = '<div>'
        choice += 'input type="radio" name="' + subject + '"value="' + stuff + '">'
        choice+= stuff + '</div>'
        buttons+= choice
    form+= buttons
    form+= '<input type="submit" value="Tell">'
    return form

html= HTML_HEADER
html+= '<h1>Awaken, ' + name + '</h1>'
html+= choices(['cool beans', 'kind fellow', 'I refuse to answer!'], 'description', 'What are you?')
html+= '<br><a href="TitlePending.html">Try Again</a>'
html+= HTML_FOOTER
print(html)


