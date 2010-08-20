#!/usr/bin/python3

import urllib.request
import re

archiv_url = r"http://www.lidovky.cz/ln_noviny.asp?c=A100819_000022_ln_noviny_sko"

#beggining_tag = "<!--FULLTEXTSTART-->"
beggining_tag =  r'<div class="text bbtext">'
ending_tag = r"<!--INTEXTSTOP-->"

urllib.request.urlretrieve(archiv_url, "001.txt")

f = open('001.txt', encoding='cp1250')

content = f.read()

#print (content)

b = content.rfind(beggining_tag)

e = content.rfind(ending_tag)

#print (b, e)

content = content[b:e]

content = re.sub("<[^>]*>",' ',content) # oreze vsetky tagy z textu
content = re.sub("Pokračování na straně [0-9]+",' ',content) # oreze vety, ktore zostali z tlacenej podoby novin
content = re.sub("Dokončení ze strany [0-9]+",' ',content) # oreze vety, ktore zostali z tlacenej podoby novin
content = re.sub("Více čtěte na straně [0-9]+",' ',content) # oreze vety, ktore zostali z tlacenej podoby novin

content = re.sub(" čtk ",' ',content) # oreze pripadnu zmienku o CTK na konci clanku

content = re.sub("[\*]+",' ',content) # oreze hviezdicky, ktore sa obcas v texte vyskytuju

print(content)
