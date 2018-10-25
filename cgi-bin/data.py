#!/usr/bin/env python3

import cgi
import html
import os

from _Data import Data
data = Data()


form = cgi.FieldStorage()
action = form.getfirst("action", "")


pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Стена</title>
</head>
<body>
    HABRAPARSE
    {posts}
</body>
</html>
'''

print('Content-type: text/html\n')

#print(pattern.format(posts=data.html_list_json()))
print(pattern.format(posts=data.html_list_db()))
