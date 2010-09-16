#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

class RatedWordgroup:

    def __init__(self,wordgroup,rating):
        self.wordgroup = wordgroup
        self.rating = rating

    def __str__(self):
        result = str(self.wordgroup) +" - " + str(self.rating)
        return result

    def __eq__(self,other):
        return self.wordgroup.eq(other.wordgroup) and self.rating.eq(other.rating)

    def __hash__(self):
        return hash(self.__str__())

class RatedSentence:

    def __init__(self,position,sentence,rating):
        self.position = position
        self.sentence = sentence
        self.rating = rating

    def __str__(self):
        result = "(" + str(self.position) +") (" + str(self.rating) +") " + self.sentence
        return result

    def __eq__(self,other):
        return self.position.eq(other.position) and self.sentence.eq(other.sentence) and self.rating.eq(other.rating)

    def __hash__(self):
        return hash(self.rating)

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
    #print("The text contains " + str(len(word_bag)) + " words.")
    return word_bag

def get_sentences(text,delimiter='.') :
    """Zo zadaneho textu vrati zoznam obsahujuci vety."""
    text = re.sub("\n", " ", text)
    text = re.sub("[ ]+", " ", text)
    sentences = text.split(delimiter)
    #for sentence in sentences :
    #    print(sentence + "\n")
    print("The text contains " + str(len(sentences)) + " sentences.")
    return sentences

def group_words(text) :
    """ Vrati slova zoskupene podla prvych pismen """

    word_bag = get_word_bag(text)

    cleanset = set() # cisty zoznam slov
    used_words = set()
    word_groups = list()

    for word in word_bag : # slova sa zjednotia v mnozine
        cleanset.add(word.strip())

    for word in cleanset :
        if word not in used_words :
            wordfamily = list()
            wordfamily.append(word)
            if(len(word)>2) :
                used_words.add(word)
                for other in cleanset :
                    if other not in used_words :
                        same_chars = 0
                        (min_len,max_len) = (len(word),len(other)) if len(word) <= len(other) else (len(other),len(word))
                        for x in range(0,min_len) :
                            if word[x] == other[x] :
                                same_chars += 1
                            else :
                                break
                        if same_chars > 3 and (max_len - same_chars) < 7 :
                            wordfamily.append(other)
                            used_words.add(other)
            word_groups.append(wordfamily)
    print("The text contains " + str(len(word_groups)) + " word groups. (GW)")
    return word_groups

def get_wordlist_rate(text) :
    word_groups = group_words(text)
    word_bag = get_word_bag(text)
    rated_word_set = set()
    for group in word_groups :
        occur = 0
        for word in group :
            occur += word_bag.count(word)
        rated_word_set.add(RatedWordgroup(group,occur))
        #if(occur>5 and len(group[0]) > 4) :
        #    print(group)
        #    print(occur)
    #sort_wg = sorted(rated_word_set, key = lambda group : group.rating, reverse=True)
    #for rwg in sort_wg:
        #rwg = sort_wg[i]
    #    if rwg.rating > 4 and len(rwg.wordgroup[0]) > 4 and len(rwg.wordgroup) > 1:
    #        print(rwg)
    return rated_word_set

def rate_sentences(text,percentage=20,verbose=True) :
    result = str()
    sentences = get_sentences(text)
    wordlist = get_wordlist_rate(text)
    rated = list()
    topwords = list()
    sort_wg = sorted(wordlist, key = lambda group : group.rating, reverse=True)
    for rwg in sort_wg:
        if rwg.rating > 1 and len(rwg.wordgroup[0]) > 4 :
          #and len(rwg.wordgroup) > 1:
            weight = 1
            weight += rwg.rating/2
            weight += len(rwg.wordgroup[0])/2
            weight += len(rwg.wordgroup)/1
            for word in rwg.wordgroup :
                #topwords.add((word, weight))
                topwords.append((weight,word))
    if(verbose):
        for tw in sorted(topwords):
            print("(" + str(tw[0]) + ") - " + tw[1])
   #print(topwords)
    position = 0
    for sentence in sentences :
        rating = 0
        position += 1
        bag = get_word_bag(sentence)
        for word in bag :
            for record in topwords :
                 if word.lower()==record[1]:
                     rating += record[0]
        if(rating>0 and len(bag) > 0):
            rating = rating/((len(bag))/7)

        rated_sentence = RatedSentence(position, sentence, rating)

        rated.append(rated_sentence)

        #if rating > min_rating :
            #print(rating)
            #result += sentence + "."
            #print(str(position) + " " + sentence + ".")
            #print(rating)
    #for rs in rated:
    #    print(rs)

    sort_sentences = sorted(rated, key = lambda sen : sen.rating, reverse=True)

    for rs in sort_sentences:
        print(rs)

    num_of_sen = int((len(sentences) / 100.0) * percentage)

    print("Percentage :" + str(percentage))
    print("Num. of sentences :" + str(num_of_sen))

    unsorted_result = list()

    counter = 0
    for rs in sort_sentences:
        if(counter>num_of_sen):
            break
        else:
            unsorted_result.append(rs)
            counter += 1

    sort_result = sorted(unsorted_result, key = lambda sen : sen.position, reverse=False)

    for rs in sort_result:
        result += rs.sentence + "."

    return result

#f = open("test02.txt")
#content = f.read()
#get_sentences(content)
#get_text_stats(content)
#get_wordlist_rate(content)
#rate_sentences(content)
