#!/usr/bin/python3
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
    dictionary.update({word : 1})
  else :
    dictionary.update({word : int(dictionary.get(word)) + 1})
  print(word + " - " + str(int(dictionary.get(word))))