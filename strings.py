# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:32:21 2021

@author: Yauheny_Shaludzko
"""

text = '''

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

sentences = text.split(".")
sentfixed = [i.strip(' \t\n\r').capitalize() for i in sentences]
addsent = []
for i in sentfixed:
    wordlist = i.split(' ')
    addsent.append(wordlist[-1])
addsent1 = ' '.join(addsent).capitalize().rstrip() + '.'
next_text = ('. '.join(sentfixed) + addsent1).replace('iz', 'is')
print(next_text)
print('Number of whitespace characters in given text:', text.count(' ') + text.count('\n '))

