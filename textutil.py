#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

def get_text_stats(text) :
    """Vrati slovnik - obsahuje slova a pocet ich vyskytov"""
    dictionary = dict()
    for word in get_word_bag(text) :
        if word not in dictionary :
            dictionary.update({word : 1})
        else :
            dictionary.update({word : int(dictionary.get(word)) + 1})

    #sortlist = list()
    #for item in dictionary.items() :
    #    if len(str(item[0])) > 3 :
    #        hash_item = (str(item[1]).zfill(6) + " " + str(item[0]))
    #        sortlist.append(hash_item)
    #sortlist.sort()
    #for item in sortlist :
    #    print (item)
    return dictionary

def get_word_bag(text) :
    """Zo zadaneho textu vracia "bag of words" - v lowercase """
    text = text.lower()
    text = re.sub("[^a-ž]+", " ", text)
    text = re.sub("\n", " ", text)
    text = re.sub("[ ]+", " ", text)
    wordlist = text.split(" ")
    word_bag = list()
    for word in wordlist :
        word_bag.append(word.strip())
    return word_bag

def get_sentences(text,delimiter='.') :
    """Zo zadaneho textu vrati zoznam obsahujuci vety."""
    text = re.sub("\n", " ", text)
    text = re.sub("[ ]+", " ", text)
    sentences = content.split(delimiter)
    #for sentence in sentences :
    #    print(sentence + "\n")
    return sentences

def create_word_groups(text) :
    """ Vrati slova zoskupene podla prvych pismen """

    word_bag = get_word_bag(text)

    word_groups = dict() # vysledna mnozina mnozin slov s rovnakym zaciatkom
    cleanset = set() # cisty zoznam slov

    for word in word_bag : # slova sa zjednotia v mnozine
        cleanset.add(word.strip())

    used_words = set()

    for word in cleanset :
        #print(word)
        if(len(word)>3 and word not in used_words) :
            wordfamily = list()
            wordfamily.append(word)
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
                    wordfamily.append(other)
                    matches += 1
                    used_words.add(other)
            if matches > 1 :
                word_groups.update({word[:4] : wordfamily })

    return word_groups

f = open("test.txt")
content = f.read()
get_sentences(content)
get_text_stats(content)

word_groups = create_word_groups(content)

for group in word_groups :
    print(group)