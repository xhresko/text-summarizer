#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

word_groups = dict() # vysledna mnozina mnozin slov s rovnakym zaciatkom 
  
f = open("test.txt")  # TODO : nacitavanie suboru z parametru
content = f.read()
content = content.lower()                 # naformatujeme vsetko do lowercase
content = re.sub("[^a-ž]+", " ", content) # a vyberieme iba text

wordlist = content.split(" ") 

cleanset = set() # cisty zoznam slov


for word in wordlist : # slova v zozname sa oholia
    cleanset.add(word.strip())

used_words = set()

for word in cleanset :
    #print(word)
    if(len(word)>3 and word not in used_words) :        
        wordfamily =  ""
        matches = 0
        for other in cleanset :                          
            same_chars = 0
            min_len = len(other)
            max_len = len(word)
            if len(word) <= len(other) :
                min_len = len(word)                         
                max_len = len(other)
            for x in range(0,min_len) :
                if word[x] == other[x] :                    
                    same_chars += 1
                else :
                    break
            if same_chars > 4 and (max_len - same_chars) < 4 :
                wordfamily = wordfamily + "," + other
                matches += 1
                used_words.add(other)
        if matches > 1 :
            print(word[:4].upper())
            print(wordfamily)            

            word_groups.update({word[:4] : wordfamily })

def create_word_groups(word_bag) :
    """ Return 'word groups' - dictionary that contains """

