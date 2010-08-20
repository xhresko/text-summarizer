#!/usr/bin/python3


import urllib.request

archiv_url = r"http://www.lidovky.cz/ln_noviny.asp?c=A100819_000003_ln_noviny_sko"

beggining_tag = r"<!--FULLTEXTSTART-->"
ending_tag = r"<!--INTEXTSTOP-->"

urllib.request.urlretrieve(archiv_url, "001.txt")

f = open('001.txt', encoding='cp1250')

content = f.read()

print (content)

b = content.rfind(beggining_tag)

e = content.rfind(ending_tag)

print (b, e)

print (content[b:e])
