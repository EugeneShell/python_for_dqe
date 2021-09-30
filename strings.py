# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:32:21 2021

@author: Yauheny_Shaludzko
"""
# at first let put text into the variable
text = '''

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

sentences = text.split(".")  # split text to sentences on dots
sentfixed = [i.strip(' \t\n\r').capitalize() for i in sentences]  # trim whitespases and capitalize sentences via gen
addsent = []  # creating empty list for additional sentence
for i in sentfixed:
    wordlist = i.split(' ')  # splitting sentence to words
    addsent.append(wordlist[-1])  # getting the last word and appending it to the list
addsent1 = ' '.join(addsent).capitalize().rstrip() + '.'  # creating additional sentence with join&capitalize
next_text = ('. '.join(sentfixed) + addsent1).replace('iz', 'is')  # replacing iz/is
print(next_text)
print('Number of whitespace characters in given text:', text.count(' ') + text.count('\n '))  # counting whitespaces
