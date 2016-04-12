#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from collections import defaultdict
# import slang

stop = stopwords.words('english')
arpabet = nltk.corpus.cmudict.dict()

def check_alliteration(sentence):
	words = sentence.split(' ')
	new_words = []
	for word in words:
		word =  word.lower().strip('. \n \t" , ! ? :')
		if word not in stop:
			new_words.append(word)
	flag=0
	for word in new_words:
		try:
			phonetic = arpabet[word][0][0]
			count = 0
			for i in xrange(new_words.index(word)+1,len(new_words)):
				if word == new_words[i]:
					continue
				try:
					if phonetic == arpabet[new_words[i]][0][0]:
						flag=1
				except:
					pass
				i+=1
		except:
			pass
	# print flag
	return flag


def check_antonyms(sentence):
	words = sentence.split(' ')
	new_words = []
	for word in words:
		word =  word.lower().strip('. \n \t" , ! ? :')
		if word not in stop:
			new_words.append(word)
	flag=0
	for word in new_words:
		syno = []
		anto = []
		for syn in wn.synsets(word):
			for l in syn.lemmas():
				syno.append(l.name())
				if l.antonyms():
					anto.append(l.antonyms()[0].name())
					if l.antonyms()[0].name() in new_words:
						flag=1
	# print flag
	return flag

def check_slang(sentence):
	sentence = sentence.lower()
	flag=0
	fo = open('adult.txt','r+')
	a = fo.readlines()
	a = [x for x in a if x!='\n']
	for word in a:
		word = word.lower().strip('. \n " , ! ? :')
		if word in sentence:
			flag = 1
			break
	# print flag
	return flag



# check_alliteration(sentence)
# check_antonyms(sentence)
# check_slang(sentence)
