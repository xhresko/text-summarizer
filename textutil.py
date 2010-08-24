#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

f = open("test.txt")
#print(f.read())
content = f.read()
content = content.lower()
content = re.sub("[^a-ž]+", " ", content)
#print(content)
wordlist = content.split(" ")

dictionary = {"a":0}
#print(wordlist[4])
for word in wordlist :
  if word not in dictionary :
    dictionary.update({word.strip() : 1})
  else :
    dictionary.update({word.strip() : int(dictionary.get(word.strip())) + 1})
#  print(word + " - " + str(int(dictionary.get(word))))

sortlist = list()

#items = dictionary.items()


for item in dictionary.items() :    
    if len(str(item[0])) > 3 :
        hash_item = (str(item[1]).zfill(6) + " " + str(item[0]))
        sortlist.append(hash_item)
        #print(hash_item)

sortlist.sort()

for item in sortlist :
    print (item)


