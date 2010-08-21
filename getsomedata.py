#!/usr/bin/python3
# -*- coding: utf-8 -*-


import urllib.request
import re
from datetime import date,timedelta

class LNTextRetriever:

    # premenne 
    global archiv_url, beggining_tag, ending_tag 

    archiv_url = r"http://www.lidovky.cz/ln_noviny.asp?c=A", r"_ln_noviny_sko"
    #beggining_tag = "<!--FULLTEXTSTART-->"
    beggining_tag =  r'<div class="text bbtext">'
    ending_tag = r"<!--INTEXTSTOP-->"
         

    def get_article_text(self,article_url,name):

        name = str(name) + ".txt"	
        urllib.request.urlretrieve(article_url, "temp.txt")
        f = open("temp.txt", encoding='cp1250')
        content = f.read()
        
        b = content.rfind(beggining_tag)
        e = content.rfind(ending_tag)
        
        content = content[b:e]

        content = re.sub("<[^>]*>",' ',content) # oreze vsetky tagy z textu
        content = re.sub("Pokračování na straně [0-9]+",' ',content) # oreze vety, ktore zostali z tlacenej podoby novin
        content = re.sub("Dokončení ze strany [0-9]+",' ',content) # oreze vety, ktore zostali z tlacenej podoby novin
        content = re.sub("Více čtěte na straně [0-9]+",' ',content) # oreze vety, ktore zostali z tlacenej podoby novin

        content = re.sub(" čtk ",' ',content) # oreze pripadnu zmienku o CTK na konci clanku

        content = re.sub("[\*]+",' ',content) # oreze hviezdicky, ktore sa obcas v texte vyskytuju
                
        f.close()
        
        out = open(name, 'w')
        out.write(content)
        out.close()
        
        return content

    def get_lndate(self,daydate):
        year = str(daydate.year-2000).zfill(2)
        month = str(daydate.month).zfill(2)
        day = str(daydate.day).zfill(2)
        return year+month+day

    def get_url(self,daydate,article_num):
        article_num = str(article_num).zfill(6)
        return archiv_url[0] + self.get_lndate(daydate) + '_' + article_num + archiv_url[1]


retriever = LNTextRetriever()
#print(retriever.get_article_text())

daydate = date.today() - timedelta(3)
#print(retriever.get_url(daydate,11))

for i in range(2,15) :
    name = str(i).zfill(3)
    name = 'test' + name
    retriever.get_article_text(retriever.get_url(daydate,i),name)
    