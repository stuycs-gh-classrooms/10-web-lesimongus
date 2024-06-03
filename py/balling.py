#!usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()

import cgi

from random import randint

header = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Hello</title>
</head>
"""

footer = """
</body>
</html>
"""

roll = randint(1, 20)
print(roll)