#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

f = open("test.txt")

content = f.read()
content = content.lower()
content = re.sub("[^a-ž]+", " ", content)

wordlist = content.split(" ")
cleanset = set()

for word in wordlist :
    cleanset.add(word.strip())

for word in cleanset :
    #print(word)
    if(len(word)>3) :        
        wordfamily = word.upper() + " - "
        matches = 0
        for other in cleanset :                          
            same_chars = 0
            min_len = len(other)
            if len(word) <= len(other) :
                min_len = len(word)                         
            for x in range(0,min_len) :
                if word[x] == other[x] :                    
                    same_chars += 1
                else :
                    break
            if same_chars > 4 :
                wordfamily = wordfamily + "," + other
                matches += 1
        if matches > 2 :
            print(wordfamily)







            



